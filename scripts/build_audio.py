# -*- coding: utf-8 -*-
"""
Sinh âm thanh MP3 chuẩn giọng Nhật (Microsoft Edge Neural TTS qua `edge-tts`)
cho toàn bộ kho học liệu Pentanihon:
1. 780 từ vựng + 780 câu collocation Flashcards (shinkanzen/tu-vung/audio/)
2. 6 chương tiểu thuyết (41 đoạn văn) + 113 từ vựng glossary (novel/audio/ + novel/audio-map.js)
3. 8 bài Đọc hiểu Shinkanzen N2 (shinkanzen/doc-hieu/audio/)
4. 10 track Nghe hiểu Shinkanzen N2 đa giọng Nam/Nữ (shinkanzen/nghe-hieu/audio/)
5. 28 tập truyện & oneshots hiện có (story/audio/)
6. Xuất manifest shinkanzen/audio-manifest.js cho reader.html
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

import edge_tts
import shinkanzen_choukai_data as ck
import shinkanzen_dokkai_data as dk

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

    # 2. Tiểu thuyết tương tác N2 (41 đoạn văn + 113 từ glossary)
    novel_js = os.path.join(ROOT_DIR, "novel/novel-data.js")
    novel_data = json.loads(open(novel_js, "r", encoding="utf-8").read().split("=", 1)[1].rstrip(";\n "))
    for ch in novel_data["chapters"]:
        cnum = ch["num"]
        slug = ch["slug"]
        ch_tracks = []
        para_texts = []
        for p_idx, p in enumerate(ch["paragraphs"], 1):
            p_text = clean_jp_for_tts(p.get("plain_text", ""))
            if not p_text:
                continue
            rel = f"novel/audio/p/c{cnum:02d}_p{p_idx:02d}.mp3"
            jobs.append((rel, [(p_text, VOICE_FEMALE, "-6%")]))
            para_texts.append((p_text, VOICE_FEMALE, "-6%"))
        # Cũng tạo bản gộp 1 file cho reader.html đọc bản Markdown chương truyện
        full_rel = f"novel/audio/{slug}.mp3"
        if para_texts:
            jobs.append((full_rel, para_texts))
            ch_tracks.append({
                "id": slug,
                "title": f"Nghe đọc Chương {cnum}: {ch['title_vi']}",
                "src": full_rel,
            })
            reader_manifest[f"novel/{slug}.md"] = ch_tracks

    for g_idx, (key, entry) in enumerate(sorted(novel_data["glossary"].items()), 1):
        audio_name = f"g{g_idx:03d}.mp3"
        novel_vocab_map[key] = audio_name
        # Nếu là từ đơn có trường reading, đọc theo kana chuẩn; mẫu ngữ pháp giữ plain sạch furigana
        text_to_speak = (entry.get("reading") or "").strip() if entry.get("kind") != "grammar" else ""
        if not text_to_speak or "〜" in text_to_speak:
            text_to_speak = clean_jp_for_tts(entry.get("plain") or entry.get("furi") or key)
            text_to_speak = text_to_speak.replace("〜", "").replace("・", " ").strip()
        if text_to_speak:
            jobs.append((f"novel/audio/v/{audio_name}", [(text_to_speak, VOICE_FEMALE, "-6%")]))

    # 3. Đọc hiểu Shinkanzen (8 bài)
    for item in dk.DOKKAI_PART1_2:
        md_rel = f"shinkanzen/doc-hieu/phan-1_luyen-ky-nang/{item['filename']}"
        slug = item["filename"].replace(".md", "")
        tracks = []
        for idx, p in enumerate(item.get("passages", []), 1):
            jp_clean = clean_jp_for_tts(p.get("jp", ""))
            if not jp_clean:
                continue
            out_rel = f"shinkanzen/doc-hieu/audio/p1_{slug}_{idx}.mp3"
            jobs.append((out_rel, [(jp_clean, VOICE_FEMALE, "-6%")]))
            tracks.append({
                "id": f"p1-{slug}-{idx}",
                "title": p.get("title", "Bài đọc mẫu tiếng Nhật"),
                "src": out_rel,
            })
        if tracks:
            reader_manifest[md_rel] = tracks

    for item in dk.DOKKAI_PART3:
        md_rel = f"shinkanzen/doc-hieu/phan-2_thuc-chien/{item['filename']}"
        slug = item["filename"].replace(".md", "")
        jp_clean = clean_jp_for_tts(item.get("passage_jp", ""))
        if jp_clean:
            out_rel = f"shinkanzen/doc-hieu/audio/p2_{slug}.mp3"
            jobs.append((out_rel, [(jp_clean, VOICE_FEMALE, "-6%")]))
            reader_manifest[md_rel] = [{
                "id": f"p2-{slug}",
                "title": item.get("text_title", "Đoạn văn thực chiến N2"),
                "src": out_rel,
            }]

    # 4. Nghe hiểu Shinkanzen (6 chương, 10 track đa giọng Nam/Nữ)
    for ch in ck.CHOUKAI_LESSONS:
        md_rel = f"shinkanzen/nghe-hieu/{ch['filename']}"
        tracks = []
        for tr in ch.get("tracks", []):
            tid = tr["track_id"]
            segments = []
            for speaker, line in tr.get("script_lines", []):
                voice = VOICE_FEMALE if speaker == "女" else VOICE_MALE
                spoken = clean_jp_for_tts(line)
                if spoken:
                    segments.append((spoken, voice, "-4%"))
            if segments:
                out_rel = f"shinkanzen/nghe-hieu/audio/{tid}.mp3"
                jobs.append((out_rel, segments))
                tracks.append({
                    "id": tid,
                    "title": f"{tid} • {tr.get('speakers', '')}",
                    "src": out_rel,
                })
        if tracks:
            reader_manifest[md_rel] = tracks

    # 5. Truyện ngắn hàng ngày & One-shots hiện có trong story/
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


async def run_all():
    jobs, reader_manifest, novel_vocab_map = collect_jobs()
    stats = {"total": len(jobs), "created": 0, "skipped": 0}
    print(f"🎙️ Preparing {len(jobs)} audio files via edge-tts ({VOICE_FEMALE} & {VOICE_MALE})...", flush=True)

    sem = asyncio.Semaphore(10)
    tasks = [synth_to_file(sem, rel_path, segs, stats) for rel_path, segs in jobs]
    await asyncio.gather(*tasks)

    # Ghi novel/audio-map.js
    map_path = os.path.join(ROOT_DIR, "novel", "audio-map.js")
    with open(map_path, "w", encoding="utf-8") as f:
        f.write("// Auto-generated by scripts/build_audio.py — Do not edit manually\n")
        f.write("window.SHINKANZEN_NOVEL_AUDIO = ")
        json.dump(novel_vocab_map, f, ensure_ascii=False, indent=2)
        f.write(";\n")

    # Ghi shinkanzen/audio-manifest.js
    manifest_path = os.path.join(ROOT_DIR, "shinkanzen", "audio-manifest.js")
    with open(manifest_path, "w", encoding="utf-8") as f:
        f.write("// Auto-generated by scripts/build_audio.py — Do not edit manually\n")
        f.write("window.PENTANIHON_AUDIO_MANIFEST = ")
        json.dump(reader_manifest, f, ensure_ascii=False, indent=2)
        f.write(";\n")

    # Thống kê dung lượng thực tế
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
