# -*- coding: utf-8 -*-
"""
Sinh âm thanh MP3 chuẩn giọng Nhật (Microsoft Edge Neural TTS qua `edge-tts`)
cho kho học liệu Pentanihon còn lại:
1. 780 từ vựng + 780 câu collocation Flashcards (shinkanzen/tu-vung/audio/)
2. Các tập truyện & oneshots trong story/ (story/audio/)
3. Xuất manifest shinkanzen/audio-manifest.js cho reader.html
"""

import asyncio
import glob
import json
import os
import re
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(SCRIPT_DIR)
sys.path.insert(0, SCRIPT_DIR)

try:
    import edge_tts
except ImportError:
    edge_tts = None

VOICE_FEMALE = "ja-JP-NanamiNeural"
VOICE_MALE = "ja-JP-KeitaNeural"


def strip_furigana(text: str) -> str:
    """Loại bỏ chú thích Hiragana/Katakana trong ngoặc ngay sau Kanji để TTS không đọc lặp."""
    s = re.sub(r"([\u4e00-\u9faf\u3005々ヶぁ-んァ-ヶー])（[\u3040-\u30ffー]+）", r"\1", str(text or ""))
    return s


def clean_jp_for_tts(text: str) -> str:
    """Làm sạch ký tự Markdown trước khi đọc TTS."""
    s = strip_furigana(text)
    lines = []
    for raw in s.splitlines():
        line = raw.strip()
        if not line:
            continue
        if re.fullmatch(r"[\|\s:\-]+", line):
            continue
        line = re.sub(r"[*_`#■・]", "", line)
        line = re.sub(r"^\|\s*|\s*\|$", "", line)
        line = re.sub(r"\s*\|\s*", "、", line)
        if line.strip():
            lines.append(line.strip())
    return "。\n".join(lines) if len(lines) > 1 else (lines[0] if lines else "")


def is_mainly_jp(text: str) -> bool:
    jp = len(re.findall(r"[\u3040-\u30ff\u4e00-\u9faf]", text))
    lat = len(re.findall(r"[A-Za-zÀ-ỹà-ỹ]", text))
    return jp >= 8 and jp > lat * 2


def extract_story_jp(md_path: str) -> str:
    """Trích phần văn bản tiếng Nhật trong tập truyện để đọc TTS tự nhiên."""
    with open(md_path, "r", encoding="utf-8") as f:
        txt = f.read()
    m = re.search(
        r"(?:Diễn Biến Câu Chuyện|Nội Dung Câu Chuyện)[^\n]*\n(.*?)(?=\n##\s*\d+\.|\n---\s*\n##\s*\d+)",
        txt,
        re.S,
    )
    sec = m.group(1) if m else txt
    jp_lines = []
    for raw in sec.splitlines():
        line = strip_furigana(raw).strip()
        if not line or line.startswith("---"):
            continue
        cleaned = re.sub(r"[*_`>]", "", line).strip()
        if is_mainly_jp(cleaned):
            jp_lines.append(cleaned)
        else:
            for quote in re.findall(r"「([^」]{6,})」", cleaned):
                if is_mainly_jp(quote):
                    jp_lines.append("「" + quote + "」")
    return "\n".join(jp_lines)


async def synth_bytes(text: str, voice: str = VOICE_FEMALE, rate: str = "+0%", retries: int = 3) -> bytes:
    """Tổng hợp mảng byte MP3 từ edge-tts có retry an toàn."""
    clean = str(text or "").strip()
    if not clean:
        return b""
    last_err = None
    for attempt in range(retries):
        try:
            comm = edge_tts.Communicate(clean, voice, rate=rate)
            buf = bytearray()
            async for chunk in comm.stream():
                if chunk.get("type") == "audio":
                    buf.extend(chunk["data"])
            if len(buf) > 256:
                return bytes(buf)
        except Exception as err:
            last_err = err
            await asyncio.sleep(0.5 * (attempt + 1))
    raise RuntimeError(f"TTS failed for {clean[:40]!r}: {last_err}")


async def synth_to_file(
    sem: asyncio.Semaphore,
    out_rel: str,
    segments: list,
    stats: dict,
):
    """Tổng hợp danh sách đoạn [(text, voice, rate), ...] và lưu thành 1 file MP3."""
    out_abs = os.path.join(ROOT_DIR, out_rel)
    if os.path.exists(out_abs) and os.path.getsize(out_abs) > 512:
        stats["skipped"] += 1
        return
    os.makedirs(os.path.dirname(out_abs), exist_ok=True)
    async with sem:
        parts = []
        for text, voice, rate in segments:
            b = await synth_bytes(text, voice=voice, rate=rate)
            if b:
                parts.append(b)
        if not parts:
            return
        tmp_abs = out_abs + ".tmp"
        with open(tmp_abs, "wb") as f:
            f.write(b"".join(parts))
        os.replace(tmp_abs, out_abs)
        stats["created"] += 1
        done = stats["created"] + stats["skipped"]
        if done % 100 == 0 or done == stats["total"]:
            print(f"   🔊 Audio progress: {done}/{stats['total']} (created {stats['created']}, cached {stats['skipped']})", flush=True)


def collect_jobs():
    """Thu thập toàn bộ công việc MP3 và dựng dữ liệu manifest."""
    jobs = []
    reader_manifest = {}
    novel_vocab_map = {}

    # 1. Flashcards Từ vựng Shinkanzen (780 từ + 780 câu ví dụ)
    goi_js = os.path.join(ROOT_DIR, "shinkanzen/tu-vung/flashcards-data.js")
    goi_data = json.loads(open(goi_js, "r", encoding="utf-8").read().split("=", 1)[1].rstrip(";\n "))
    for lesson in goi_data:
        lid = lesson["id"]
        for w in lesson["words"]:
            wid = w["id"]
            # Đọc Hiragana cho từ đơn để không bao giờ đọc sai âm Kanji đồng tự
            word_text = (w.get("reading") or strip_furigana(w.get("plain", ""))).strip()
            colloc_text = clean_jp_for_tts(w.get("collocJp", ""))
            if word_text:
                jobs.append((f"shinkanzen/tu-vung/audio/words/{lid}_{wid}.mp3", [(word_text, VOICE_FEMALE, "-5%")]))
            if colloc_text:
                jobs.append((f"shinkanzen/tu-vung/audio/collocs/{lid}_{wid}.mp3", [(colloc_text, VOICE_FEMALE, "-4%")]))

    # 2. Truyện ngắn hàng ngày & One-shots hiện có trong story/
    story_files = sorted(glob.glob(os.path.join(ROOT_DIR, "story", "**", "*.md"), recursive=True))
    for abs_p in story_files:
        rel_p = os.path.relpath(abs_p, ROOT_DIR).replace("\\", "/")
        if rel_p.endswith("README.md") or rel_p.endswith("quotes.md"):
            continue
        jp_body = extract_story_jp(abs_p)
        if not jp_body:
            continue
        base_slug = os.path.splitext(rel_p[len("story/"):])[0].replace("/", "__")
        out_rel = f"story/audio/{base_slug}.mp3"
        lines = [(ln, VOICE_FEMALE, "-6%") for ln in jp_body.splitlines() if ln.strip()]
        if lines:
            jobs.append((out_rel, lines))
            reader_manifest[rel_p] = [{
                "id": base_slug,
                "title": "🎧 Nghe đọc truyện tiếng Nhật (Giọng bản xứ)",
                "src": out_rel,
            }]

    return jobs, reader_manifest, novel_vocab_map


def write_audio_manifest_only():
    _, reader_manifest, _ = collect_jobs()
    manifest_path = os.path.join(ROOT_DIR, "shinkanzen", "audio-manifest.js")
    with open(manifest_path, "w", encoding="utf-8") as f:
        f.write("// Auto-generated by scripts/build_audio.py — Do not edit manually\n")
        f.write("window.PENTANIHON_AUDIO_MANIFEST = ")
        json.dump(reader_manifest, f, ensure_ascii=False, indent=2)
        f.write(";\n")
    print(f"✅ Updated shinkanzen/audio-manifest.js ({len(reader_manifest)} story tracks)")


async def run_all():
    if "--manifest-only" in sys.argv or edge_tts is None:
        write_audio_manifest_only()
        return

    jobs, reader_manifest, _ = collect_jobs()
    stats = {"total": len(jobs), "created": 0, "skipped": 0}
    print(f"🎙️ Preparing {len(jobs)} audio files via edge-tts ({VOICE_FEMALE} & {VOICE_MALE})...", flush=True)

    sem = asyncio.Semaphore(10)
    tasks = [synth_to_file(sem, rel_path, segs, stats) for rel_path, segs in jobs]
    await asyncio.gather(*tasks)

    write_audio_manifest_only()

    total_bytes = 0
    for rel_path, _ in jobs:
        ap = os.path.join(ROOT_DIR, rel_path)
        if os.path.exists(ap):
            total_bytes += os.path.getsize(ap)
    print(
        f"✅ Audio build complete: {stats['total']} tracks "
        f"(new {stats['created']}, cached {stats['skipped']}) — {total_bytes / (1024 * 1024):.2f} MB total."
    )


if __name__ == "__main__":
    asyncio.run(run_all())
