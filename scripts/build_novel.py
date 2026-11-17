# -*- coding: utf-8 -*-
"""
Builder tạo Cuốn Tiểu Thuyết Tương Tác JLPT N2:
『東京（とうきょう）の小さな書斎（しょさい）』— Căn Phòng Đọc Nhỏ Giữa Lòng Tokyo
Xuất ra tại thư mục novel/:
- novel/index.html      : Trình đọc tiểu thuyết tương tác (Highlight/Click từ Shinkanzen + Popover bảng hướng dẫn + Câu hỏi trắc nghiệm kế bên + Nghe đọc TTS + Bật/tắt Hiragana kế bên)
- novel/novel-data.js   : Dữ liệu 6 chương + từ điển khớp tự động với Shinkanzen N2 (Từ vựng, Ngữ pháp, Chữ Hán)
- novel/README.md       : Mục lục bản Markdown đọc trên reader.html
- novel/chuong-01..06.md: 6 chương bản Markdown đầy đủ Hiragana, giải nghĩa từ Shinkanzen và câu hỏi
"""
import json
import os
import re

from shinkanzen_goi_data_p1 import GOI_PART1
from shinkanzen_goi_data_p2 import GOI_PART2
from shinkanzen_novel_data import NOVEL_META, NOVEL_CHAPTERS, EXTRA_SHINKANZEN_ENTRIES

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
NOVEL_DIR = os.path.join(ROOT_DIR, "novel")


def build_unified_shinkanzen_index():
    """Hợp nhất toàn bộ 780 từ vựng Shinkanzen + mục mở rộng ngữ pháp/kanji."""
    idx = {}
    lesson_md_map = {}

    for part_num, arr in ((1, GOI_PART1), (2, GOI_PART2)):
        for l in arr:
            rel_md = f"../shinkanzen/tu-vung/phan-{part_num}/{l['filename']}"
            lesson_md_map[l["id"]] = rel_md
            for furi, plain, reading, hv, mean, col_jp, col_vi, group in l["words"]:
                entry = {
                    "id": f"goi_{l['id']}_{plain}",
                    "kind": "vocab",
                    "plain": plain,
                    "furi": furi,
                    "reading": reading,
                    "hv": hv,
                    "mean": mean,
                    "collocJp": col_jp,
                    "collocVi": col_vi,
                    "group": group,
                    "bookLabel": f"Từ vựng N2 — 第{part_num}部 {l['chapter']}・{l['lesson']}",
                    "mdLink": rel_md,
                    "flashLink": f"../shinkanzen/tu-vung/flashcards.html?lesson={l['id']}",
                }
                if plain not in idx:
                    idx[plain] = entry

    for key, data in EXTRA_SHINKANZEN_ENTRIES.items():
        flash = data.get("flashLink", "")
        resolved_md = data["mdLink"]
        if "?lesson=" in flash:
            lid = flash.split("?lesson=", 1)[1]
            if lid in lesson_md_map:
                resolved_md = lesson_md_map[lid]
        assert os.path.isfile(os.path.join(ROOT_DIR, resolved_md.replace("../", ""))), f"Missing target MD file for {key}: {resolved_md}"
        idx[key] = {
            "id": f"extra_{data['plain']}",
            "kind": data["kind"],
            "plain": data["plain"],
            "furi": data["furi"],
            "reading": data["reading"],
            "hv": data["hv"],
            "mean": data["mean"],
            "collocJp": data["collocJp"],
            "collocVi": data["collocVi"],
            "group": data.get("group", ""),
            "bookLabel": data["bookLabel"],
            "mdLink": resolved_md,
            "flashLink": flash,
        }
    return idx


def compile_auto_goi_regex(vocab_index):
    """Tạo regex khớp tự động thêm các từ Shinkanzen (dạng Kanji >= 2 chữ) xuất hiện tự nhiên ngoài thẻ [[...]]."""
    kanji_only = re.compile(r"^[一-龯々]{2,}$")
    # Chỉ nhận từ toàn chữ Hán >= 2 chữ để tránh tách nhầm động từ chia thể hoặc từ quá ngắn
    candidates = [
        k for k, v in vocab_index.items()
        if v["kind"] == "vocab" and kanji_only.match(k) and len(k) >= 2
    ]
    candidates.sort(key=len, reverse=True)
    if not candidates:
        return None, {}

    pat_map = {}
    parts = []
    for k in candidates:
        # Mỗi chữ Kanji cho phép theo sau bởi （ひらがな）
        piece = "".join(re.escape(ch) + r"(?:（[^）]+）)?" for ch in k)
        parts.append(piece)
        pat_map[k] = piece

    # Không bắt đầu hoặc kết thúc ngay giữa cụm từ Kanji liền kề khác
    regex_str = r"(?<![一-龯々])(?:" + "|".join(parts) + r")(?![一-龯々（])"
    return re.compile(regex_str), vocab_index


def strip_furi(text):
    return re.sub(r"（[^）]*）", "", text)


def parse_text_segments(raw_text, vocab_index, auto_regex):
    """Chuyển văn bản có [[...]] + từ Shinkanzen tự động thành mảng segments [{type:'text'|'token', ...}]."""
    explicit_pat = re.compile(r"\[\[([^\]]+)\]\]")
    segments = []
    pos = 0
    found_keys = []

    def emit_plain_chunk(chunk):
        if not chunk:
            return
        if not auto_regex:
            segments.append({"t": "text", "v": chunk})
            return
        sub_pos = 0
        for am in auto_regex.finditer(chunk):
            if am.start() > sub_pos:
                segments.append({"t": "text", "v": chunk[sub_pos:am.start()]})
            matched_disp = am.group(0)
            matched_key = strip_furi(matched_disp)
            if matched_key in vocab_index:
                segments.append({"t": "tok", "v": matched_disp, "k": matched_key})
                found_keys.append(matched_key)
            else:
                segments.append({"t": "text", "v": matched_disp})
            sub_pos = am.end()
        if sub_pos < len(chunk):
            segments.append({"t": "text", "v": chunk[sub_pos:]})

    for m in explicit_pat.finditer(raw_text):
        if m.start() > pos:
            emit_plain_chunk(raw_text[pos:m.start()])
        inner = m.group(1)
        if "|" in inner:
            disp, key = inner.split("|", 1)
        else:
            disp = inner
            key = strip_furi(inner)
        assert key in vocab_index, f"Key '{key}' (từ '{disp}') không tồn tại trong kho Shinkanzen!"
        segments.append({"t": "tok", "v": disp, "k": key})
        found_keys.append(key)
        pos = m.end()

    if pos < len(raw_text):
        emit_plain_chunk(raw_text[pos:])

    return segments, found_keys


def build_novel_markdown(chapters_built, glossary):
    """Sinh thêm bản Markdown cho novel/README.md và 6 chương để tương thích reader.html."""
    for ch in chapters_built:
        lines = [
            f"# 📖 {NOVEL_META['title_jp']} — {ch['title_vi']}",
            f"## {ch['title_jp']}",
            "",
            f"> 🌸 **Lời nhắn của chị Yuki:** *\"{ch['yuki_tip']}\"*",
            "",
            "✨ [**Mở Trình Đọc Tương Tác (Click từ Shinkanzen tự phát sáng + Bảng hướng dẫn + Quiz kế bên)**](./index.html?chapter=" + str(ch["num"]) + ")",
            "",
            "---",
            "",
            "## 1. Nội Dung Chương Truyện (Có Hiragana Kế Bên)",
            "",
        ]
        for p in ch["paragraphs"]:
            # Làm nổi bật in đậm từ Shinkanzen trong Markdown
            md_p = "".join(
                f"**{seg['v']}**" if seg["t"] == "tok" else seg["v"]
                for seg in p["segments"]
            )
            lines.append(md_p)
            lines.append("")

        lines.extend([
            "<details><summary>👉 Xem bản dịch tiếng Việt trọn chương</summary>\n",
        ])
        for p in ch["paragraphs"]:
            lines.append(p["vi"])
            lines.append("")
        lines.append("</details>\n")

        lines.extend([
            "---",
            "",
            f"## 📚 2. Kho Từ Vựng & Ngữ Pháp Shinkanzen Trong Chương {ch['num']:02d} ({len(ch['vocab_keys'])} mục)",
            "",
            "| Từ / Mẫu | Cách đọc | Hán Việt | Nghĩa & Ví dụ Shinkanzen | Nguồn Sách |",
            "| :--- | :--- | :--- | :--- | :--- |",
        ])
        for k in ch["vocab_keys"]:
            item = glossary[k]
            md_link_rel = item["mdLink"]
            lines.append(
                f"| **{item['furi']}** | `{item['reading']}` | {item['hv']} | {item['mean']} *(VD: {item['collocJp']})* | [Xem bài]({md_link_rel}) |"
            )

        lines.extend([
            "",
            "---",
            "",
            f"## ✍️ 3. Câu Hỏi Đọc Hiểu & Vận Dụng Chương {ch['num']:02d}",
            "",
        ])
        for q_idx, q in enumerate(ch["quiz"], 1):
            q_txt = "".join(seg["v"] for seg in q["prompt_segments"])
            lines.append(f"### Câu {q_idx}: {q_txt}")
            for o_idx, opt in enumerate(q["options"], 1):
                lines.append(f"{o_idx}. {opt}  ")
            lines.append("<details><summary>👉 Xem đáp án & giải thích</summary>\n")
            lines.append(f"**Đáp án đúng:** {q['ans']} (`{q['options'][q['ans'] - 1]}`)  ")
            lines.append(f"**Giải thích:** {q['exp']}")
            lines.append("</details>\n")

        nav = []
        if ch["num"] > 1:
            nav.append(f"[⬅️ Chương {ch['num'] - 1:02d}](./chuong-{ch['num'] - 1:02d}.md)")
        nav.append("[📋 Mục lục Tiểu thuyết](./README.md)")
        nav.append("[✨ Đọc bản Tương tác](./index.html?chapter=" + str(ch["num"]) + ")")
        if ch["num"] < len(chapters_built):
            nav.append(f"[Chương {ch['num'] + 1:02d} ➡️](./chuong-{ch['num'] + 1:02d}.md)")
        lines.append("---")
        lines.append(" | ".join(nav) + "\n")

        with open(os.path.join(NOVEL_DIR, f"{ch['slug']}.md"), "w", encoding="utf-8") as f:
            f.write("\n".join(lines))

    # Build novel/README.md
    readme = [
        f"# 📖 {NOVEL_META['title_jp']} — {NOVEL_META['title_vi']}",
        "",
        f"> 🌸 **Lời nhắn của chị Yuki:** *\"{NOVEL_META['author_note']}\"*",
        "",
        "✨ [**Mở Bản Web Tương Tác Chính Thức (Click từ trong truyện -> Sáng lên + Bảng hướng dẫn Shinkanzen)**](./index.html)",
        "",
        "---",
        "",
        "## 📑 Mục Lục 6 Chương Tiểu Thuyết",
        "",
        "| Chương | Tiêu đề (日本語) | Tên Tiếng Việt | Số từ Shinkanzen | Mở đọc |",
        "| :---: | :--- | :--- | :---: | :--- |",
    ]
    for ch in chapters_built:
        t_clean = "".join(seg["v"] for seg in ch["title_segments"])
        readme.append(
            f"| **{ch['num']:02d}** | {t_clean} | [**{ch['title_vi']}**](./{ch['slug']}.md) | {len(ch['vocab_keys'])} | [✨ Tương tác](./index.html?chapter={ch['num']}) |"
        )
    readme.extend(["", "---", "[🏠 Quay lại Trang chủ PentaNihonGo](../README.md)", ""])
    with open(os.path.join(NOVEL_DIR, "README.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(readme))


def render_novel_html():
    return """<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Tiểu Thuyết Tương Tác N2 — Căn Phòng Đọc Nhỏ Giữa Lòng Tokyo</title>
  <meta name="description" content="Tiểu thuyết ngắn 6 chương vận dụng từ vựng & ngữ pháp Shinkanzen Master N2 có Hiragana kế bên, click từ để sáng lên và xem bảng hướng dẫn chi tiết kèm câu hỏi từng chương.">
  <link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>📖</text></svg>">
  <style>
    :root {
      --bg: #f8f5ef;
      --paper: #fffdf8;
      --panel: #ffffff;
      --text: #221f1c;
      --text-muted: #5c564f;
      --border: #e4ddd2;
      --border-strong: #c8bfb0;
      --accent: #b92b27;
      --accent-soft: #fff1ef;
      --glow: #ffe066;
      --glow-border: #e09f00;
      --highlight-idle-bg: #fff8dc;
      --highlight-idle-line: #d4a72c;
      --grammar-idle-bg: #eef4ff;
      --grammar-idle-line: #3b6fd8;
      --ok: #2b8a3e;
      --ok-bg: #ebfbee;
      --err: #c92a2a;
      --err-bg: #fff5f5;
      --radius: 10px;
      --font-vi: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      --font-jp: "Hiragino Kaku Gothic ProN", "Yu Gothic", "Noto Sans JP", "Meiryo", sans-serif;
    }

    * { box-sizing: border-box; }

    html, body {
      overflow-x: clip;
      overscroll-behavior-x: none;
      max-width: 100%;
    }

    body {
      margin: 0;
      font-family: var(--font-vi);
      background: var(--bg);
      color: var(--text);
      line-height: 1.65;
      overflow-wrap: anywhere;
    }

    .visually-hidden:where(:not(:focus-within, :active)) {
      position: absolute !important;
      clip-path: inset(50%) !important;
      overflow: hidden !important;
      width: 1px !important;
      height: 1px !important;
      margin: -1px !important;
      padding: 0 !important;
      border: 0 !important;
      white-space: nowrap !important;
    }

    .skip-link {
      background: #111;
      color: #fff;
      padding: 8px 14px;
      font-weight: 700;
      text-decoration: none;
      z-index: 999;
      position: fixed;
      top: 8px;
      left: 8px;
      border-radius: 6px;
    }

    :where(a:any-link, button, summary, input, select):focus-visible {
      outline: 3px solid var(--accent);
      outline-offset: 2px;
    }

    /* TOP BAR */
    .topbar {
      background: var(--panel);
      border-bottom: 1px solid var(--border);
      position: sticky;
      top: 0;
      z-index: 40;
    }

    .topbar-inner {
      max-width: 1280px;
      margin: 0 auto;
      padding: 10px 18px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 10px;
    }

    .nav-group {
      display: flex;
      gap: 8px;
      align-items: center;
      flex-wrap: wrap;
    }

    .nav-btn {
      display: inline-flex;
      align-items: center;
      gap: 5px;
      min-block-size: 36px;
      padding: 6px 12px;
      border: 1px solid var(--border-strong);
      border-radius: 6px;
      background: #fff;
      color: var(--text);
      text-decoration: none;
      font-size: 0.86rem;
      font-weight: 600;
      cursor: pointer;
    }

    .nav-btn:hover {
      background: #f3efe8;
    }

    .nav-btn.is-on {
      background: #1f1c19;
      color: #fff;
      border-color: #1f1c19;
    }

    /* HERO HEADER */
    .book-header {
      max-width: 1280px;
      margin: 0 auto;
      padding: 20px 18px 12px;
    }

    .book-eyebrow {
      display: inline-block;
      font-size: 0.78rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      color: var(--accent);
      background: var(--accent-soft);
      border: 1px solid #f4c7c5;
      padding: 2px 10px;
      border-radius: 99px;
      margin-bottom: 8px;
    }

    .book-header h1 {
      font-size: 1.7rem;
      line-height: 1.3;
      margin: 0 0 6px;
    }

    .book-subtitle {
      color: var(--text-muted);
      font-size: 0.94rem;
      margin: 0 0 14px;
    }

    /* CHAPTER TABS */
    .chapter-nav {
      display: flex;
      gap: 8px;
      flex-wrap: wrap;
      margin-bottom: 14px;
    }

    .chap-tab {
      min-block-size: 38px;
      padding: 6px 14px;
      border: 1px solid var(--border-strong);
      border-radius: 99px;
      background: #fff;
      color: var(--text);
      font-size: 0.86rem;
      font-weight: 700;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }

    .chap-tab.active {
      background: var(--accent);
      color: #fff;
      border-color: var(--accent);
    }

    .chap-tab .quiz-done-dot {
      font-size: 0.78rem;
    }

    /* TOOLBAR */
    .reading-controls {
      background: var(--panel);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 10px 14px;
      display: flex;
      flex-wrap: wrap;
      justify-content: space-between;
      align-items: center;
      gap: 10px;
    }

    .toggle-pill {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      min-block-size: 34px;
      padding: 4px 10px;
      border-radius: 6px;
      border: 1px solid var(--border-strong);
      background: #faf7f2;
      font-size: 0.84rem;
      font-weight: 600;
      cursor: pointer;
    }

    .toggle-pill[aria-pressed="true"] {
      background: #fff7d6;
      border-color: #d4a72c;
      color: #6b4c00;
    }

    /* TWO-COLUMN WORKSPACE: BOOK PAGE + COMPANION PANEL */
    .workspace {
      max-width: 1280px;
      margin: 0 auto 50px;
      padding: 10px 18px;
      display: grid;
      grid-template-columns: minmax(0, 1.45fr) minmax(320px, 1fr);
      gap: 22px;
      align-items: start;
    }

    /* BOOK PAGE */
    .book-page {
      background: var(--paper);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 28px 30px;
      box-shadow: 0 6px 24px rgba(34, 31, 28, 0.05);
    }

    .chapter-title-jp {
      font-family: var(--font-jp);
      font-size: 1.4rem;
      font-weight: 800;
      margin: 0 0 4px;
      color: #111;
    }

    .chapter-title-vi {
      font-size: 1rem;
      color: var(--text-muted);
      font-weight: 600;
      margin: 0 0 16px;
    }

    .yuki-tip-box {
      background: var(--accent-soft);
      border-left: 4px solid var(--accent);
      padding: 12px 16px;
      border-radius: 0 8px 8px 0;
      margin-bottom: 22px;
      font-size: 0.92rem;
    }

    .story-body {
      font-family: var(--font-jp);
      font-size: 1.16rem;
      line-height: 2.15;
      letter-spacing: 0.02em;
    }

    .para-block {
      margin-bottom: 18px;
      padding: 6px 8px 12px;
      border-radius: 8px;
      border-bottom: 1px dashed #ece5da;
      transition: background-color 0.18s ease;
    }

    .para-block.is-speaking {
      background: #fffbeb;
      box-shadow: inset 3px 0 0 #d97706;
    }

    .para-block:last-child {
      border-bottom: none;
    }

    .para-jp-row {
      display: flex;
      gap: 10px;
      align-items: flex-start;
    }

    .para-jp-text {
      flex: 1;
      margin: 0;
    }

    .para-speak-btn {
      flex-shrink: 0;
      min-block-size: 32px;
      min-inline-size: 32px;
      border: 1px solid var(--border-strong);
      border-radius: 6px;
      background: #fff;
      cursor: pointer;
      font-size: 0.85rem;
      margin-top: 6px;
    }

    .para-speak-btn:hover,
    .para-speak-btn.is-playing {
      background: #1f1c19;
      color: #fff;
      border-color: #1f1c19;
    }

    .audio-speed-select {
      min-block-size: 36px;
      padding: 4px 8px;
      border: 1px solid var(--border-strong);
      border-radius: 6px;
      background: #fff;
      color: var(--text);
      font-size: max(16px, 0.85rem);
      font-weight: 600;
    }

    .vg-speak-btn {
      background: #1f1c19;
      color: #fff;
      border: 1px solid #1f1c19;
    }

    .vg-speak-btn:hover {
      background: #3d3832;
    }

    .para-vi {
      margin: 8px 0 0;
      padding: 8px 12px;
      background: #f4f1ea;
      border-radius: 6px;
      font-family: var(--font-vi);
      font-size: 0.92rem;
      line-height: 1.55;
      color: #3d3832;
    }

    .hide-translations .para-vi {
      display: none;
    }

    /* HIRAGANA INLINE TOGGLE */
    .furi-inline {
      color: #6b645c;
      font-size: 0.84em;
      font-weight: 500;
    }

    .hide-furi .furi-inline {
      display: none;
    }

    /* SHINKANZEN INTERACTIVE WORD TOKENS */
    .skz-word {
      appearance: none;
      font: inherit;
      color: inherit;
      background: transparent;
      border: 1px solid transparent;
      border-bottom: 2px dotted transparent;
      border-radius: 5px;
      padding: 1px 3px;
      margin: 0 1px;
      cursor: pointer;
      display: inline;
      text-align: inherit;
      line-height: 1.5;
      transition: background-color 0.16s ease, box-shadow 0.16s ease, border-color 0.16s ease, transform 0.12s ease;
    }

    /* Mode 1: Highlighter luôn sáng nhẹ từ có trong Shinkanzen */
    .highlight-all .skz-word[data-kind="vocab"],
    .highlight-all .skz-word[data-kind="kanji"] {
      background: var(--highlight-idle-bg);
      border-bottom: 2px solid var(--highlight-idle-line);
    }

    .highlight-all .skz-word[data-kind="grammar"] {
      background: var(--grammar-idle-bg);
      border-bottom: 2px dashed var(--grammar-idle-line);
    }

    /* Mode 2: Click-to-glow (ẩn highlight cho tới khi hover/focus/click) */
    .skz-word:hover {
      background: #fff3bf;
      border-color: #f08c00;
    }

    /* Trạng thái SÁNG RỰC KHI ĐƯỢC CLICK */
    .skz-word.is-lit,
    .skz-word[aria-pressed="true"] {
      background: var(--glow) !important;
      color: #000 !important;
      border: 1.5px solid #c77c00 !important;
      box-shadow: 0 0 0 3px rgba(255, 212, 59, 0.55), 0 3px 10px rgba(217, 119, 6, 0.25);
      font-weight: 700;
    }

    .skz-word.is-mastered::after {
      content: " ✓";
      font-size: 0.75em;
      color: var(--ok);
      font-weight: 800;
    }

    .chapter-footer-nav {
      margin-top: 26px;
      padding-top: 16px;
      border-top: 1px solid var(--border);
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 10px;
      flex-wrap: wrap;
    }

    /* COMPANION PANEL (KẾ BÊN CHƯƠNG TIỂU THUYẾT) */
    .companion-panel {
      background: var(--panel);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      position: sticky;
      top: 68px;
      max-height: calc(100vh - 86px);
      display: flex;
      flex-direction: column;
      overflow: hidden;
      box-shadow: 0 4px 18px rgba(0, 0, 0, 0.04);
    }

    .panel-tabs {
      display: grid;
      grid-template-columns: 1fr 1fr;
      border-bottom: 1px solid var(--border);
      background: #faf7f2;
    }

    .panel-tab-btn {
      min-block-size: 44px;
      border: none;
      background: transparent;
      padding: 10px 12px;
      font-size: 0.88rem;
      font-weight: 700;
      color: var(--text-muted);
      cursor: pointer;
      border-bottom: 3px solid transparent;
    }

    .panel-tab-btn[aria-selected="true"] {
      background: #fff;
      color: var(--accent);
      border-bottom-color: var(--accent);
    }

    .panel-body {
      padding: 16px;
      overflow-y: auto;
      flex: 1;
    }

    .panel-heading {
      font-size: 1rem;
      margin: 0 0 12px;
      color: #111;
    }

    /* QUIZ CARDS */
    .quiz-card {
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 14px;
      margin-bottom: 14px;
      background: #fcfbfa;
    }

    .quiz-prompt {
      font-family: var(--font-jp);
      font-size: 0.96rem;
      font-weight: 700;
      margin: 0 0 10px;
      line-height: 1.65;
    }

    .quiz-options {
      display: flex;
      flex-direction: column;
      gap: 7px;
    }

    .quiz-opt-btn {
      width: 100%;
      text-align: left;
      min-block-size: 36px;
      padding: 8px 10px;
      border: 1px solid var(--border-strong);
      border-radius: 6px;
      background: #fff;
      font-family: var(--font-jp);
      font-size: 0.88rem;
      line-height: 1.45;
      cursor: pointer;
    }

    .quiz-opt-btn:hover {
      background: #f5f0e8;
    }

    .quiz-opt-btn.is-correct {
      background: var(--ok-bg);
      border-color: var(--ok);
      color: #165924;
      font-weight: 700;
    }

    .quiz-opt-btn.is-wrong {
      background: var(--err-bg);
      border-color: var(--err);
      color: #9e1c1c;
    }

    .quiz-exp {
      margin-top: 10px;
      padding: 9px 11px;
      border-radius: 6px;
      background: #eef6ff;
      border-left: 3px solid #228be6;
      font-size: 0.85rem;
      line-height: 1.5;
    }

    .quiz-score-banner {
      padding: 10px 12px;
      border-radius: 8px;
      background: #fff7e6;
      border: 1px solid #ffd480;
      font-size: 0.88rem;
      font-weight: 700;
      margin-bottom: 14px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    /* VOCAB LIST IN PANEL */
    .glossary-item {
      width: 100%;
      text-align: left;
      border: 1px solid var(--border);
      border-radius: 8px;
      background: #fff;
      padding: 10px 12px;
      margin-bottom: 8px;
      cursor: pointer;
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 8px;
    }

    .glossary-item:hover {
      border-color: #d4a72c;
      background: #fffdf0;
    }

    .glossary-item.is-lit {
      border-color: #d97706;
      background: #fff3bf;
    }

    .gl-jp {
      font-family: var(--font-jp);
      font-weight: 700;
      font-size: 0.96rem;
    }

    .gl-mean {
      font-size: 0.82rem;
      color: var(--text-muted);
      margin-top: 2px;
    }

    .gl-badge {
      font-size: 0.72rem;
      font-weight: 700;
      padding: 2px 7px;
      border-radius: 99px;
      background: #f1f3f5;
      color: #495057;
      white-space: nowrap;
    }

    /* NATIVE POPOVER VOCAB GUIDE DIALOG (Rule 2 Modern Web Guidance) */
    dialog#vocab-guide {
      border: 2px solid #1f1c19;
      border-radius: 12px;
      padding: 0;
      max-width: 440px;
      width: calc(100vw - 24px);
      max-height: calc(100vh - 36px);
      overflow-y: auto;
      background: #fff;
      color: var(--text);
      box-shadow: 0 18px 45px rgba(0, 0, 0, 0.22);
      z-index: 200;
      touch-action: pan-y;
      overscroll-behavior-x: contain;
    }

    @media (prefers-reduced-motion: no-preference) {
      dialog#vocab-guide {
        transition: transform 0.2s cubic-bezier(0.22, 1, 0.36, 1), opacity 0.18s ease-out;
      }
      dialog#vocab-guide.is-dragging {
        transition: none;
      }
    }

    dialog#vocab-guide.is-dragging {
      user-select: none;
      -webkit-user-select: none;
    }

    dialog#vocab-guide:is(:popover-open, .\\:popover-open) {
      display: block;
    }

    dialog#vocab-guide.is-fallback-open {
      display: block;
    }

    @supports (position-area: block-end) {
      dialog#vocab-guide.is-anchored {
        inset: auto;
        margin: 0;
        position-anchor: --active-skz-word;
        position-area: block-end span-inline-end;
        position-try-fallbacks: flip-block, flip-inline, flip-block flip-inline;
      }
    }

    dialog#vocab-guide:not(.is-anchored) {
      position: fixed;
      inset: auto 20px 20px auto;
      margin: 0;
    }

    @supports not (position-area: block-end) {
      dialog#vocab-guide {
        position: fixed;
        inset: auto 20px 20px auto;
        margin: 0;
      }
    }

    .vg-head {
      background: #1f1c19;
      color: #fff;
      padding: 12px 16px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 10px;
    }

    .vg-title {
      margin: 0;
      font-family: var(--font-jp);
      font-size: 1.18rem;
      line-height: 1.3;
    }

    .vg-close-btn {
      min-block-size: 32px;
      min-inline-size: 32px;
      border: 1px solid rgba(255, 255, 255, 0.35);
      border-radius: 6px;
      background: transparent;
      color: #fff;
      font-size: 1rem;
      font-weight: 700;
      cursor: pointer;
    }

    .vg-body {
      padding: 15px 16px 16px;
      font-size: 0.9rem;
    }

    .vg-meta-row {
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
      align-items: center;
      margin-bottom: 10px;
    }

    .vg-hv {
      background: #f1ede4;
      color: #4a3f32;
      font-weight: 800;
      font-size: 0.78rem;
      letter-spacing: 0.8px;
      padding: 2px 8px;
      border-radius: 4px;
    }

    .vg-book {
      font-size: 0.78rem;
      font-weight: 700;
      color: var(--accent);
      background: var(--accent-soft);
      padding: 2px 8px;
      border-radius: 4px;
    }

    .vg-mean {
      font-size: 1.05rem;
      font-weight: 700;
      color: #111;
      margin: 0 0 10px;
    }

    .vg-colloc {
      background: #f8f6f1;
      border-left: 3px solid #1f1c19;
      padding: 8px 12px;
      border-radius: 0 6px 6px 0;
      margin-bottom: 12px;
    }

    .vg-colloc-jp {
      font-family: var(--font-jp);
      font-weight: 600;
      margin-bottom: 2px;
    }

    .vg-colloc-vi {
      color: var(--text-muted);
      font-size: 0.84rem;
    }

    .vg-actions {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
    }

    .vg-action-link, .vg-action-btn {
      display: inline-flex;
      align-items: center;
      min-block-size: 34px;
      padding: 5px 11px;
      border-radius: 6px;
      font-size: 0.82rem;
      font-weight: 700;
      text-decoration: none;
      cursor: pointer;
    }

    .vg-action-link {
      background: #f1f3f5;
      color: #212529;
      border: 1px solid #ced4da;
    }

    .vg-action-link:hover {
      background: #e9ecef;
    }

    .vg-action-btn {
      background: #fff;
      color: var(--ok);
      border: 1px solid var(--ok);
    }

    .vg-action-btn[aria-pressed="true"] {
      background: var(--ok);
      color: #fff;
    }

    .vg-swipe-bar {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 8px;
      margin-top: 12px;
      padding-top: 10px;
      border-top: 1px dashed var(--border);
    }

    .vg-nav-btn {
      min-block-size: 32px;
      padding: 4px 10px;
      border: 1px solid #ced4da;
      border-radius: 6px;
      background: #fff;
      color: var(--text);
      font-size: 0.8rem;
      font-weight: 700;
      cursor: pointer;
      touch-action: manipulation;
    }

    .vg-nav-btn:hover:not(:disabled) {
      background: #f1f3f5;
      border-color: #495057;
    }

    .vg-nav-btn:disabled {
      opacity: 0.45;
      cursor: default;
    }

    .vg-counter {
      font-size: 0.78rem;
      color: var(--text-muted);
      font-weight: 700;
      text-align: center;
    }

    @media (pointer: coarse) {
      .vg-close-btn,
      .vg-nav-btn,
      .vg-action-link,
      .vg-action-btn {
        min-block-size: 44px;
      }
    }

    footer {
      text-align: center;
      padding: 24px 18px;
      color: var(--text-muted);
      font-size: 0.85rem;
      border-top: 1px solid var(--border);
      background: var(--panel);
    }

    @media (max-width: 960px) {
      .workspace {
        grid-template-columns: 1fr;
      }
      .companion-panel {
        position: static;
        max-height: none;
      }
      @supports not (position-area: block-end) {
        dialog#vocab-guide {
          inset: auto 12px 12px 12px;
          width: auto;
        }
      }
    }

    @media (max-width: 768px) {
      dialog#vocab-guide,
      dialog#vocab-guide.is-anchored {
        position: fixed !important;
        position-anchor: none !important;
        position-area: none !important;
        inset: auto 10px max(10px, env(safe-area-inset-bottom, 0px)) 10px !important;
        width: auto !important;
        max-width: none !important;
        max-height: 58dvh;
        margin: 0 !important;
        z-index: 250;
      }
    }
  </style>
</head>
<body>
  <a href="#novel-main" class="skip-link visually-hidden">Chuyển tới nội dung chương truyện</a>

  <header class="topbar">
    <div class="topbar-inner">
      <div class="nav-group">
        <a href="../index.html" class="nav-btn">🏠 Trang chủ</a>
        <a href="../reader.html?file=shinkanzen/README.md" class="nav-btn">📚 Giáo trình Shinkanzen</a>
        <a href="../shinkanzen/tu-vung/flashcards.html" class="nav-btn">🎴 Flashcards 37 Bài</a>
      </div>
      <div class="nav-group">
        <button type="button" id="btn-speak-chapter" class="nav-btn">🔊 Nghe đọc chương</button>
        <select id="novel-speed" class="audio-speed-select" aria-label="Tốc độ đọc truyện">
          <option value="0.85">0.85x</option>
          <option value="1" selected>1.0x</option>
          <option value="1.15">1.15x</option>
        </select>
      </div>
    </div>
  </header>

  <div class="book-header">
    <span class="book-eyebrow">Tiểu Thuyết Ngắn Thực Chiến Shinkanzen Master N2 • 6 Chương</span>
    <h1 lang="ja">東京（とうきょう）の小さな書斎（しょさい） — <span lang="vi">Căn Phòng Đọc Nhỏ Giữa Lòng Tokyo</span></h1>
    <p class="book-subtitle" id="book-subtitle">Vận dụng từ vựng &amp; ngữ pháp Shinkanzen có Hiragana đứng kế bên. Bấm vào bất kỳ từ Shinkanzen nào trong truyện để bật sáng và mở bảng hướng dẫn!</p>

    <nav class="chapter-nav" id="chapter-nav" aria-label="Chọn chương tiểu thuyết"></nav>

    <div class="reading-controls">
      <div class="nav-group">
        <button type="button" id="btn-toggle-highlight" class="toggle-pill" aria-pressed="true">
          ✨ Luôn đánh dấu nhẹ từ Shinkanzen
        </button>
        <button type="button" id="btn-toggle-furi" class="toggle-pill" aria-pressed="true">
          🔤 Hiragana kế bên
        </button>
        <button type="button" id="btn-toggle-vi" class="toggle-pill" aria-pressed="false">
          🇻🇳 Hiện dịch tiếng Việt
        </button>
      </div>
      <div id="chapter-vocab-counter" style="font-size: 0.84rem; font-weight: 700; color: var(--text-muted);">
        Đang tải dữ liệu...
      </div>
    </div>
  </div>

  <main id="novel-main" class="workspace" tabindex="-1">
    <article class="book-page hide-translations highlight-all" id="book-page" aria-labelledby="chap-title-jp">
      <h2 class="chapter-title-jp" id="chap-title-jp" lang="ja"></h2>
      <div class="chapter-title-vi" id="chap-title-vi"></div>
      <div class="yuki-tip-box" id="yuki-tip"></div>
      <div class="story-body" id="story-body"></div>

      <div class="chapter-footer-nav">
        <button type="button" id="btn-prev-chap" class="nav-btn">⬅️ Chương trước</button>
        <a id="link-chapter-md" href="../reader.html?file=novel/chuong-01.md" class="nav-btn">📝 Mở bản Markdown</a>
        <button type="button" id="btn-next-chap" class="nav-btn">Chương tiếp theo ➡️</button>
      </div>
    </article>

    <aside class="companion-panel" aria-label="Câu hỏi và kho từ vựng chương">
      <div class="panel-tabs" role="tablist" aria-label="Công cụ học tập bên cạnh chương">
        <button type="button" role="tab" id="tab-quiz" class="panel-tab-btn" aria-selected="true" aria-controls="panel-quiz">
          ❓ Câu hỏi chương
        </button>
        <button type="button" role="tab" id="tab-vocab" class="panel-tab-btn" aria-selected="false" aria-controls="panel-vocab">
          📚 Từ Shinkanzen
        </button>
      </div>

      <div class="panel-body">
        <section id="panel-quiz" role="tabpanel" aria-labelledby="tab-quiz">
          <div class="quiz-score-banner">
            <span id="quiz-score-text">Điểm chương này: 0 / 0</span>
            <button type="button" id="btn-reset-quiz" class="nav-btn" style="min-block-size:28px; padding:2px 8px; font-size:0.78rem;">↺ Làm lại</button>
          </div>
          <h2 class="panel-heading" id="quiz-heading">Kiểm tra đọc hiểu &amp; từ vựng chương</h2>
          <div id="quiz-container"></div>
        </section>

        <section id="panel-vocab" role="tabpanel" aria-labelledby="tab-vocab" hidden>
          <h2 class="panel-heading">Từ Shinkanzen dùng trong chương (bấm để bật sáng)</h2>
          <div id="glossary-list"></div>
        </section>
      </div>
    </aside>
  </main>

  <dialog id="vocab-guide" popover="manual" aria-labelledby="vg-title">
    <div class="vg-head">
      <h3 class="vg-title" id="vg-title" lang="ja">Từ vựng</h3>
      <button type="button" id="vg-close" class="vg-close-btn" popovertarget="vocab-guide" popovertargetaction="hide" aria-label="Đóng bảng hướng dẫn từ vựng">✕</button>
    </div>
    <div class="vg-body">
      <div class="vg-meta-row">
        <span class="vg-hv" id="vg-hv"></span>
        <span class="vg-book" id="vg-book"></span>
      </div>
      <p class="vg-mean" id="vg-mean"></p>
      <div class="vg-colloc">
        <div class="vg-colloc-jp" id="vg-colloc-jp" lang="ja"></div>
        <div class="vg-colloc-vi" id="vg-colloc-vi"></div>
      </div>
      <div class="vg-actions">
        <button type="button" id="vg-speak-word" class="vg-action-btn vg-speak-btn">🔊 Nghe phát âm</button>
        <a id="vg-open-lesson" href="#" class="vg-action-link">📖 Xem bài Shinkanzen</a>
        <a id="vg-open-flash" href="#" class="vg-action-link" hidden>🎴 Luyện Flashcard</a>
        <button type="button" id="vg-mark-mastered" class="vg-action-btn" aria-pressed="false">✓ Đánh dấu đã thuộc</button>
      </div>
      <div class="vg-swipe-bar">
        <button type="button" id="vg-prev-word" class="vg-nav-btn" aria-label="Từ Shinkanzen trước trong chương">◀ Từ trước</button>
        <span class="vg-counter" id="vg-counter">1 / 1 • Vuốt ⇄</span>
        <button type="button" id="vg-next-word" class="vg-nav-btn" aria-label="Từ Shinkanzen tiếp theo trong chương">Từ sau ▶</button>
      </div>
    </div>
  </dialog>

  <div id="live-announcer" class="visually-hidden" aria-live="polite"></div>

  <audio id="novelAudio" preload="none"></audio>

  <footer>
    🌸 <strong>PentaNihonGo Novel</strong> — Tiểu thuyết thực chiến tích hợp kho dữ liệu 5 cuốn <strong>Shinkanzen Master N2</strong>.
  </footer>

  <script src="./novel-data.js"></script>
  <script src="./audio-map.js"></script>
  <script type="module">
    if (!Object.hasOwn(HTMLElement.prototype, "popover")) {
      import("https://unpkg.com/@oddbird/popover-polyfill@latest/dist/popover.min.js").catch(() => {});
    }
  </script>
  <script>
    (function () {
      const DATA = window.SHINKANZEN_NOVEL_DATA;
      const VOCAB_AUDIO = window.SHINKANZEN_NOVEL_AUDIO || {};
      if (!DATA || !DATA.chapters) return;

      const novelAudio = document.getElementById("novelAudio");
      const speedSelect = document.getElementById("novel-speed");
      let audioRate = 1.0;
      let chapterPlaying = false;
      let currentPlayingTag = null;
      let playSessionId = 0;

      const STORAGE_MASTERED = "penta_novel_mastered_v1";
      const STORAGE_QUIZ = "penta_novel_quiz_v1";
      let masteredSet = new Set(JSON.parse(localStorage.getItem(STORAGE_MASTERED) || "[]"));
      let quizState = JSON.parse(localStorage.getItem(STORAGE_QUIZ) || "{}");

      let currentChapterNum = 1;
      let activeKey = null;
      let activeTokenEl = null;

      const bookPage = document.getElementById("book-page");
      const chapterNav = document.getElementById("chapter-nav");
      const storyBody = document.getElementById("story-body");
      const quizContainer = document.getElementById("quiz-container");
      const glossaryList = document.getElementById("glossary-list");
      const vocabDialog = document.getElementById("vocab-guide");
      const announcer = document.getElementById("live-announcer");

      function announce(msg) {
        announcer.textContent = msg;
      }

      function formatFuriHTML(raw) {
        const safe = String(raw || "")
          .replace(/&/g, "&amp;")
          .replace(/</g, "&lt;")
          .replace(/>/g, "&gt;");
        return safe.replace(/（([^）]+)）/g, '<span class="furi-inline">（$1）</span>');
      }

      function formatRichNote(raw) {
        return formatFuriHTML(raw)
          .replace(/\\*\\*([^*]+)\\*\\*/g, "<strong>$1</strong>")
          .replace(/`([^`]+)`/g, "<code>$1</code>");
      }

      function stripFuri(raw) {
        return String(raw || "").replace(/（[^）]*）/g, "");
      }

      function renderSegmentsInto(parentEl, segments) {
        segments.forEach(seg => {
          if (seg.t === "text") {
            const span = document.createElement("span");
            span.innerHTML = formatFuriHTML(seg.v);
            parentEl.appendChild(span);
          } else {
            const entry = DATA.glossary[seg.k];
            const btn = document.createElement("button");
            btn.type = "button";
            btn.className = "skz-word";
            btn.dataset.key = seg.k;
            btn.dataset.kind = entry ? entry.kind : "vocab";
            btn.setAttribute("aria-pressed", "false");
            btn.setAttribute("lang", "ja");
            if (masteredSet.has(seg.k)) btn.classList.add("is-mastered");
            btn.innerHTML = formatFuriHTML(seg.v);
            btn.addEventListener("click", (e) => {
              e.stopPropagation();
              selectShinkanzenWord(seg.k, btn);
            });
            parentEl.appendChild(btn);
          }
        });
      }

      function clearWordHighlights() {
        document.querySelectorAll(".skz-word.is-lit, .glossary-item.is-lit").forEach(el => {
          el.classList.remove("is-lit");
          if (el.hasAttribute("aria-pressed")) el.setAttribute("aria-pressed", "false");
        });
        if (activeTokenEl) {
          activeTokenEl.style.removeProperty("anchor-name");
          activeTokenEl = null;
        }
      }

      const prefersReducedMotion = () => Boolean(window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches);
      let vgAnimTimer = null;
      let vgEnterRaf = null;

      function clearVgAnim() {
        if (vgAnimTimer) { clearTimeout(vgAnimTimer); vgAnimTimer = null; }
        if (vgEnterRaf) { cancelAnimationFrame(vgEnterRaf); vgEnterRaf = null; }
        vocabDialog.classList.remove("is-dragging");
        vocabDialog.style.transform = "";
        vocabDialog.style.opacity = "";
      }

      function hideVocabGuide() {
        clearVgAnim();
        if (typeof vocabDialog.hidePopover === "function") {
          try { vocabDialog.hidePopover(); } catch (_) {}
        }
        vocabDialog.classList.remove("is-fallback-open");
        clearWordHighlights();
      }

      function selectShinkanzenWord(key, sourceBtn, scrollIntoView = false) {
        const entry = DATA.glossary[key];
        if (!entry) return;

        clearVgAnim();
        clearWordHighlights();
        activeKey = key;

        // Thắp sáng toàn bộ từ này trong chương hiện tại & thẻ danh sách bên phải
        const matches = Array.from(storyBody.querySelectorAll('.skz-word[data-key="' + CSS.escape(key) + '"]'));
        matches.forEach(m => {
          m.classList.add("is-lit");
          m.setAttribute("aria-pressed", "true");
        });

        const targetToken = (sourceBtn && sourceBtn.classList.contains("skz-word")) ? sourceBtn : matches[0];
        vocabDialog.classList.toggle("is-anchored", Boolean(targetToken));
        if (targetToken) {
          activeTokenEl = targetToken;
          targetToken.style.setProperty("anchor-name", "--active-skz-word");
          if (scrollIntoView) {
            const behavior = prefersReducedMotion() ? "auto" : "smooth";
            if (window.innerWidth <= 768) {
              const rect = targetToken.getBoundingClientRect();
              const top = Math.max(0, rect.top + window.scrollY - window.innerHeight * 0.25);
              window.scrollTo({ top, behavior });
            } else {
              targetToken.scrollIntoView({ behavior, block: "center" });
            }
          }
        }

        const listMatch = glossaryList.querySelector('.glossary-item[data-key="' + CSS.escape(key) + '"]');
        if (listMatch) listMatch.classList.add("is-lit");

        // Điền nội dung Bảng Hướng Dẫn Từ Vựng
        document.getElementById("vg-title").innerHTML = formatFuriHTML(entry.furi);
        document.getElementById("vg-hv").textContent = entry.hv ? `[ ${entry.hv} ]` : "SHINKANZEN N2";
        document.getElementById("vg-book").textContent = entry.bookLabel;
        document.getElementById("vg-mean").textContent = entry.mean;
        document.getElementById("vg-colloc-jp").innerHTML = formatFuriHTML(entry.collocJp);
        document.getElementById("vg-colloc-vi").textContent = entry.collocVi ? `↳ ${entry.collocVi}` : "";

        const openLesson = document.getElementById("vg-open-lesson");
        openLesson.href = "../reader.html?file=" + encodeURIComponent(entry.mdLink.replace("../", ""));

        const openFlash = document.getElementById("vg-open-flash");
        if (entry.flashLink) {
          openFlash.href = entry.flashLink;
          openFlash.hidden = false;
        } else {
          openFlash.hidden = true;
        }

        const masterBtn = document.getElementById("vg-mark-mastered");
        const isMastered = masteredSet.has(key);
        masterBtn.setAttribute("aria-pressed", String(isMastered));
        masterBtn.textContent = isMastered ? "✓ Đã thuộc từ này" : "✓ Đánh dấu đã thuộc";

        const ch = DATA.chapters.find(c => c.num === currentChapterNum);
        const chapKeys = ch && Array.isArray(ch.vocab_keys) ? ch.vocab_keys : [];
        const wordPos = Math.max(0, chapKeys.indexOf(key));
        const totalWords = Math.max(1, chapKeys.length);
        document.getElementById("vg-counter").textContent = `${wordPos + 1} / ${totalWords} • Vuốt ⇄`;
        document.getElementById("vg-prev-word").disabled = chapKeys.length <= 1;
        document.getElementById("vg-next-word").disabled = chapKeys.length <= 1;

        // Mở Popover không chặn thao tác cuộn/click khác (Dialog Rule 2)
        if (typeof vocabDialog.showPopover === "function") {
          try {
            if (!vocabDialog.matches(":popover-open")) {
              vocabDialog.showPopover();
            }
          } catch (_) {
            vocabDialog.classList.add("is-fallback-open");
          }
        } else {
          vocabDialog.classList.add("is-fallback-open");
        }
        announce(`Đang xem hướng dẫn từ ${stripFuri(entry.plain)}: ${entry.mean}`);
      }

      function renderChapterNav() {
        chapterNav.innerHTML = "";
        DATA.chapters.forEach(ch => {
          const btn = document.createElement("button");
          btn.type = "button";
          btn.className = "chap-tab" + (ch.num === currentChapterNum ? " active" : "");
          const ansMap = quizState[ch.num] || {};
          const solved = Object.keys(ansMap).length;
          const allRight = solved === ch.quiz.length && ch.quiz.every((q, i) => ansMap[i] === q.ans);
          btn.innerHTML = `<span>Chương ${ch.num}</span>` + (allRight ? `<span class="quiz-done-dot" aria-label="Đã hoàn thành">✅</span>` : "");
          btn.addEventListener("click", () => loadChapter(ch.num));
          chapterNav.appendChild(btn);
        });
      }

      function renderQuiz(ch) {
        quizContainer.innerHTML = "";
        if (!quizState[ch.num]) quizState[ch.num] = {};

        const updateScoreBanner = () => {
          const map = quizState[ch.num] || {};
          let score = 0;
          ch.quiz.forEach((q, idx) => {
            if (map[idx] === q.ans) score++;
          });
          document.getElementById("quiz-score-text").textContent = `Điểm chương ${ch.num}: ${score} / ${ch.quiz.length}`;
          renderChapterNav();
        };

        ch.quiz.forEach((q, qIdx) => {
          const card = document.createElement("div");
          card.className = "quiz-card";

          const promptP = document.createElement("p");
          promptP.className = "quiz-prompt";
          const numSpan = document.createElement("span");
          numSpan.textContent = `Câu ${qIdx + 1}: `;
          promptP.appendChild(numSpan);
          renderSegmentsInto(promptP, q.prompt_segments);
          card.appendChild(promptP);

          const optsWrap = document.createElement("div");
          optsWrap.className = "quiz-options";

          const expDiv = document.createElement("div");
          expDiv.className = "quiz-exp";
          expDiv.hidden = true;
          expDiv.innerHTML = `<strong>Giải thích:</strong> ${formatRichNote(q.exp)}`;

          const applyChoice = (chosenIdx) => {
            const optBtns = optsWrap.querySelectorAll(".quiz-opt-btn");
            optBtns.forEach((b, bIdx) => {
              const oNum = bIdx + 1;
              b.classList.remove("is-correct", "is-wrong");
              if (oNum === q.ans) b.classList.add("is-correct");
              else if (oNum === chosenIdx) b.classList.add("is-wrong");
            });
            expDiv.hidden = false;
          };

          q.options.forEach((optText, oIdx) => {
            const oNum = oIdx + 1;
            const ob = document.createElement("button");
            ob.type = "button";
            ob.className = "quiz-opt-btn";
            ob.innerHTML = `${oNum}. ${formatFuriHTML(optText)}`;
            ob.addEventListener("click", () => {
              quizState[ch.num][qIdx] = oNum;
              localStorage.setItem(STORAGE_QUIZ, JSON.stringify(quizState));
              applyChoice(oNum);
              updateScoreBanner();
              announce(oNum === q.ans ? `Câu ${qIdx + 1} chính xác!` : `Câu ${qIdx + 1} chưa đúng, hãy xem giải thích bên dưới.`);
            });
            optsWrap.appendChild(ob);
          });

          if (quizState[ch.num][qIdx]) {
            applyChoice(quizState[ch.num][qIdx]);
          }

          card.appendChild(optsWrap);
          card.appendChild(expDiv);
          quizContainer.appendChild(card);
        });

        updateScoreBanner();
      }

      function renderGlossaryPanel(ch) {
        glossaryList.innerHTML = "";
        ch.vocab_keys.forEach(k => {
          const item = DATA.glossary[k];
          if (!item) return;
          const btn = document.createElement("button");
          btn.type = "button";
          btn.className = "glossary-item" + (activeKey === k ? " is-lit" : "");
          btn.dataset.key = k;
          btn.innerHTML = `
            <div>
              <div class="gl-jp" lang="ja">${formatFuriHTML(item.furi)}</div>
              <div class="gl-mean">${formatRichNote(item.mean)}</div>
            </div>
            <span class="gl-badge">${item.kind === "grammar" ? "Ngữ pháp" : item.kind === "kanji" ? "Chữ Hán" : "Từ vựng"}</span>
          `;
          btn.addEventListener("click", () => selectShinkanzenWord(k, null, true));
          glossaryList.appendChild(btn);
        });
      }

      function clearSpeakingHighlight() {
        document.querySelectorAll(".para-block.is-speaking").forEach(el => el.classList.remove("is-speaking"));
        document.querySelectorAll(".para-speak-btn.is-playing").forEach(el => el.classList.remove("is-playing"));
      }

      function stopAllAudio() {
        playSessionId++;
        chapterPlaying = false;
        currentPlayingTag = null;
        if (novelAudio) {
          novelAudio.onended = null;
          novelAudio.onerror = null;
          novelAudio.pause();
          novelAudio.removeAttribute("src");
        }
        if ("speechSynthesis" in window) window.speechSynthesis.cancel();
        clearSpeakingHighlight();
        const chBtn = document.getElementById("btn-speak-chapter");
        if (chBtn) chBtn.textContent = "🔊 Nghe đọc chương";
      }

      function speakWithBrowser(text, onFinished) {
        if (!("speechSynthesis" in window)) {
          announce("Trình duyệt hiện tại không hỗ trợ đọc giọng nói TTS.");
          if (onFinished) onFinished();
          return;
        }
        window.speechSynthesis.cancel();
        const utter = new SpeechSynthesisUtterance(stripFuri(text));
        utter.lang = "ja-JP";
        utter.rate = Math.max(0.7, Math.min(1.5, audioRate * 0.94));
        if (onFinished) {
          utter.onend = onFinished;
          utter.onerror = onFinished;
        }
        window.speechSynthesis.speak(utter);
      }

      function playMp3Track(src, fallbackText, tag, onDone) {
        const mySession = playSessionId;
        clearSpeakingHighlight();
        currentPlayingTag = tag;
        if (!novelAudio || !src) {
          speakWithBrowser(fallbackText, () => {
            if (playSessionId === mySession && onDone) onDone();
          });
          return;
        }
        novelAudio.playbackRate = audioRate;
        novelAudio.onended = () => {
          if (playSessionId !== mySession) return;
          if (onDone) onDone();
        };
        novelAudio.onerror = () => {
          if (playSessionId !== mySession) return;
          speakWithBrowser(fallbackText, () => {
            if (playSessionId === mySession && onDone) onDone();
          });
        };
        novelAudio.src = src;
        novelAudio.play().catch(() => {
          if (playSessionId !== mySession) return;
          speakWithBrowser(fallbackText, () => {
            if (playSessionId === mySession && onDone) onDone();
          });
        });
      }

      function loadChapter(num) {
        stopAllAudio();
        hideVocabGuide();

        const ch = DATA.chapters.find(c => c.num === num) || DATA.chapters[0];
        currentChapterNum = ch.num;

        const titleJpEl = document.getElementById("chap-title-jp");
        titleJpEl.innerHTML = "";
        renderSegmentsInto(titleJpEl, ch.title_segments);

        document.getElementById("chap-title-vi").textContent = ch.title_vi;
        document.getElementById("yuki-tip").innerHTML = `🌸 <strong>Lời dặn của chị Yuki:</strong> ${formatRichNote(ch.yuki_tip)}`;
        document.getElementById("chapter-vocab-counter").textContent = `Chương ${ch.num}/6 • ${ch.vocab_keys.length} từ & mẫu Shinkanzen tương tác`;

        storyBody.innerHTML = "";
        ch.paragraphs.forEach((p, idx) => {
          const pNum = idx + 1;
          const pTag = `c${String(ch.num).padStart(2, "0")}_p${String(pNum).padStart(2, "0")}`;
          const mp3Src = `./audio/p/${pTag}.mp3`;

          const block = document.createElement("div");
          block.className = "para-block";
          block.dataset.ptag = pTag;

          const jpRow = document.createElement("div");
          jpRow.className = "para-jp-row";

          const jpP = document.createElement("p");
          jpP.className = "para-jp-text";
          jpP.setAttribute("lang", "ja");
          renderSegmentsInto(jpP, p.segments);

          const spBtn = document.createElement("button");
          spBtn.type = "button";
          spBtn.className = "para-speak-btn";
          spBtn.setAttribute("aria-label", `Nghe đọc đoạn ${pNum} bằng tiếng Nhật`);
          spBtn.textContent = "🔊";
          spBtn.addEventListener("click", () => {
            if (currentPlayingTag === pTag && !chapterPlaying) {
              stopAllAudio();
              return;
            }
            stopAllAudio();
            block.classList.add("is-speaking");
            spBtn.classList.add("is-playing");
            playMp3Track(mp3Src, p.plain_text, pTag, () => {
              stopAllAudio();
            });
          });

          jpRow.appendChild(jpP);
          jpRow.appendChild(spBtn);

          const viP = document.createElement("p");
          viP.className = "para-vi";
          viP.textContent = p.vi;

          block.appendChild(jpRow);
          block.appendChild(viP);
          storyBody.appendChild(block);
        });

        document.getElementById("link-chapter-md").href = `../reader.html?file=novel/${ch.slug}.md`;
        document.getElementById("btn-prev-chap").disabled = ch.num <= 1;
        document.getElementById("btn-next-chap").disabled = ch.num >= DATA.chapters.length;

        renderQuiz(ch);
        renderGlossaryPanel(ch);
        renderChapterNav();

        const url = new URL(window.location.href);
        url.searchParams.set("chapter", String(ch.num));
        window.history.replaceState({}, "", url.toString());
        window.scrollTo({ top: 0, behavior: prefersReducedMotion() ? "auto" : "smooth" });
      }

      // EVENT LISTENERS (Không dùng inline onclick theo Modern Web Guidance)
      speedSelect.addEventListener("change", function () {
        const val = parseFloat(this.value);
        audioRate = Number.isFinite(val) ? val : 1.0;
        if (novelAudio) novelAudio.playbackRate = audioRate;
      });

      document.getElementById("btn-toggle-highlight").addEventListener("click", function () {
        const pressed = this.getAttribute("aria-pressed") === "true";
        const next = !pressed;
        this.setAttribute("aria-pressed", String(next));
        bookPage.classList.toggle("highlight-all", next);
        this.textContent = next ? "✨ Luôn đánh dấu nhẹ từ Shinkanzen" : "👆 Chỉ sáng khi Click vào từ";
      });

      document.getElementById("btn-toggle-furi").addEventListener("click", function () {
        const pressed = this.getAttribute("aria-pressed") === "true";
        const next = !pressed;
        this.setAttribute("aria-pressed", String(next));
        bookPage.classList.toggle("hide-furi", !next);
        this.textContent = next ? "🔤 Hiragana kế bên: Bật" : "🔤 Hiragana kế bên: Tắt";
      });

      document.getElementById("btn-toggle-vi").addEventListener("click", function () {
        const pressed = this.getAttribute("aria-pressed") === "true";
        const next = !pressed;
        this.setAttribute("aria-pressed", String(next));
        bookPage.classList.toggle("hide-translations", !next);
        this.textContent = next ? "🇻🇳 Đang hiện dịch tiếng Việt" : "🇻🇳 Hiện dịch tiếng Việt";
      });

      document.getElementById("btn-speak-chapter").addEventListener("click", function () {
        if (chapterPlaying) {
          stopAllAudio();
          return;
        }
        const ch = DATA.chapters.find(c => c.num === currentChapterNum);
        if (!ch || !ch.paragraphs.length) return;

        stopAllAudio();
        chapterPlaying = true;
        const mySession = playSessionId;
        const blocks = Array.from(storyBody.querySelectorAll(".para-block"));

        const playNext = (idx) => {
          if (!chapterPlaying || playSessionId !== mySession) return;
          if (idx >= ch.paragraphs.length) {
            stopAllAudio();
            return;
          }
          const p = ch.paragraphs[idx];
          const pTag = `c${String(ch.num).padStart(2, "0")}_p${String(idx + 1).padStart(2, "0")}`;
          const mp3Src = `./audio/p/${pTag}.mp3`;
          this.textContent = `⏹ Dừng (${idx + 1}/${ch.paragraphs.length})`;

          playMp3Track(mp3Src, p.plain_text, pTag, () => playNext(idx + 1));
          const blk = blocks[idx];
          if (blk) {
            blk.classList.add("is-speaking");
            const sb = blk.querySelector(".para-speak-btn");
            if (sb) sb.classList.add("is-playing");
          }
        };

        playNext(0);
      });

      document.getElementById("vg-speak-word").addEventListener("click", () => {
        if (!activeKey) return;
        const entry = DATA.glossary[activeKey];
        if (!entry) return;
        stopAllAudio();
        const audioFile = VOCAB_AUDIO[activeKey];
        const mp3Src = audioFile ? `./audio/v/${audioFile}` : null;
        const fallback = (entry.reading && entry.kind !== "grammar")
          ? entry.reading
          : stripFuri(entry.plain || entry.furi || activeKey).replace(/〜/g, "");
        playMp3Track(mp3Src, fallback, `v_${activeKey}`, () => {
          currentPlayingTag = null;
        });
      });

      document.getElementById("btn-prev-chap").addEventListener("click", () => {
        if (currentChapterNum > 1) loadChapter(currentChapterNum - 1);
      });

      document.getElementById("btn-next-chap").addEventListener("click", () => {
        if (currentChapterNum < DATA.chapters.length) loadChapter(currentChapterNum + 1);
      });

      document.getElementById("btn-reset-quiz").addEventListener("click", () => {
        quizState[currentChapterNum] = {};
        localStorage.setItem(STORAGE_QUIZ, JSON.stringify(quizState));
        const ch = DATA.chapters.find(c => c.num === currentChapterNum);
        if (ch) renderQuiz(ch);
      });

      // Companion Tabs
      const tabQuiz = document.getElementById("tab-quiz");
      const tabVocab = document.getElementById("tab-vocab");
      const panelQuiz = document.getElementById("panel-quiz");
      const panelVocab = document.getElementById("panel-vocab");

      function switchCompanionTab(target) {
        const isQuiz = target === "quiz";
        tabQuiz.setAttribute("aria-selected", String(isQuiz));
        tabVocab.setAttribute("aria-selected", String(!isQuiz));
        panelQuiz.hidden = !isQuiz;
        panelVocab.hidden = isQuiz;
      }

      tabQuiz.addEventListener("click", () => switchCompanionTab("quiz"));
      tabVocab.addEventListener("click", () => switchCompanionTab("vocab"));

      // Mastered toggle inside popover
      document.getElementById("vg-mark-mastered").addEventListener("click", function () {
        if (!activeKey) return;
        if (masteredSet.has(activeKey)) masteredSet.delete(activeKey);
        else masteredSet.add(activeKey);
        localStorage.setItem(STORAGE_MASTERED, JSON.stringify(Array.from(masteredSet)));

        const nowMastered = masteredSet.has(activeKey);
        this.setAttribute("aria-pressed", String(nowMastered));
        this.textContent = nowMastered ? "✓ Đã thuộc từ này" : "✓ Đánh dấu đã thuộc";
        storyBody.querySelectorAll('.skz-word[data-key="' + CSS.escape(activeKey) + '"]').forEach(el => {
          el.classList.toggle("is-mastered", nowMastered);
        });
      });

      document.getElementById("vg-close").addEventListener("click", hideVocabGuide);

      function stepChapterVocab(step, animate = true) {
        const ch = DATA.chapters.find(c => c.num === currentChapterNum);
        const chapKeys = ch && Array.isArray(ch.vocab_keys) ? ch.vocab_keys : [];
        if (chapKeys.length <= 1) return;
        const idx = chapKeys.indexOf(activeKey);
        const nextIdx = idx >= 0 ? (idx + step + chapKeys.length) % chapKeys.length : 0;
        const nextKey = chapKeys[nextIdx];

        if (vgAnimTimer) { clearTimeout(vgAnimTimer); vgAnimTimer = null; }
        if (vgEnterRaf) { cancelAnimationFrame(vgEnterRaf); vgEnterRaf = null; }

        if (!animate || prefersReducedMotion()) {
          vocabDialog.style.transform = "";
          vocabDialog.style.opacity = "";
          selectShinkanzenWord(nextKey, null, true);
          return;
        }

        vocabDialog.classList.remove("is-dragging");
        vocabDialog.style.transform = `translate3d(${step > 0 ? -48 : 48}px, 0, 0)`;
        vocabDialog.style.opacity = "0";
        vgAnimTimer = setTimeout(() => {
          vgAnimTimer = null;
          selectShinkanzenWord(nextKey, null, true);
          vocabDialog.classList.add("is-dragging");
          vocabDialog.style.transform = `translate3d(${step > 0 ? 36 : -36}px, 0, 0)`;
          vocabDialog.style.opacity = "0";
          void vocabDialog.offsetWidth;
          vgEnterRaf = requestAnimationFrame(() => {
            vgEnterRaf = null;
            vocabDialog.classList.remove("is-dragging");
            vocabDialog.style.transform = "";
            vocabDialog.style.opacity = "";
          });
        }, 95);
      }

      document.getElementById("vg-prev-word").addEventListener("click", () => stepChapterVocab(-1));
      document.getElementById("vg-next-word").addEventListener("click", () => stepChapterVocab(1));

      (function attachVocabGuideSwipe() {
        // Touch phones: passive:false touchmove guarantees iOS Safari & Android Chrome won't cancel horizontal thumb swipes
        let tId = null;
        let tStartX = 0;
        let tStartY = 0;
        let tStartTime = 0;
        let tLastDx = 0;
        let tAxis = null;

        vocabDialog.addEventListener("touchstart", (e) => {
          if (e.touches.length !== 1) return;
          if (e.target.closest("a, button")) return;
          const t = e.touches[0];
          tId = t.identifier;
          tStartX = t.clientX;
          tStartY = t.clientY;
          tStartTime = Date.now();
          tLastDx = 0;
          tAxis = null;
        }, { passive: true });

        vocabDialog.addEventListener("touchmove", (e) => {
          if (tId === null) return;
          const t = Array.from(e.touches).find(pt => pt.identifier === tId);
          if (!t) return;
          const dx = t.clientX - tStartX;
          const dy = t.clientY - tStartY;
          const adx = Math.abs(dx);
          const ady = Math.abs(dy);

          if (tAxis === null) {
            if (adx < 8 && ady < 8) return;
            if (adx >= 8 && adx >= ady * 0.85) {
              tAxis = "x";
              vocabDialog.classList.add("is-dragging");
            } else if (ady > 16 && ady > adx * 1.35) {
              tAxis = "y";
              return;
            } else {
              return;
            }
          }

          if (tAxis === "x") {
            e.preventDefault();
            tLastDx = dx;
            const slideX = Math.max(-54, Math.min(54, dx * 0.55));
            vocabDialog.style.transform = `translate3d(${slideX}px, 0, 0)`;
            vocabDialog.style.opacity = String(Math.max(0.65, 1 - Math.abs(slideX) / 220));
          }
        }, { passive: false });

        function endTouchSwipe() {
          if (tId === null) return;
          const wasX = tAxis === "x";
          const dx = tLastDx;
          const vel = Math.abs(dx) / Math.max(1, Date.now() - tStartTime);
          tId = null;
          tAxis = null;
          vocabDialog.classList.remove("is-dragging");
          if (wasX) {
            if (Math.abs(dx) >= 32 || (Math.abs(dx) >= 18 && vel >= 0.25)) {
              stepChapterVocab(dx < 0 ? 1 : -1, true);
            } else {
              vocabDialog.style.transform = "";
              vocabDialog.style.opacity = "";
            }
          }
        }

        vocabDialog.addEventListener("touchend", endTouchSwipe);
        vocabDialog.addEventListener("touchcancel", endTouchSwipe);

        // Desktop mouse & pen pointer drag (touches are handled above by native touch listeners)
        let activeId = null;
        let startX = 0;
        let startY = 0;
        let startTime = 0;
        let lastDx = 0;
        let isHorizontal = false;
        let isVertical = false;

        vocabDialog.addEventListener("pointerdown", (e) => {
          if (!e.isPrimary || e.pointerType === "touch") return;
          if (e.pointerType === "mouse" && e.button !== 0) return;
          if (e.target.closest("a, button")) return;
          activeId = e.pointerId;
          startX = e.clientX;
          startY = e.clientY;
          startTime = Date.now();
          lastDx = 0;
          isHorizontal = false;
          isVertical = false;
        });

        vocabDialog.addEventListener("pointermove", (e) => {
          if (activeId !== e.pointerId || isVertical || e.pointerType === "touch") return;
          const dx = e.clientX - startX;
          const dy = e.clientY - startY;
          if (!isHorizontal) {
            if (Math.abs(dy) > 12 && Math.abs(dy) >= Math.abs(dx) * 1.2) {
              isVertical = true;
              activeId = null;
              return;
            }
            if (Math.abs(dx) > 10 && Math.abs(dx) > Math.abs(dy)) {
              isHorizontal = true;
              vocabDialog.classList.add("is-dragging");
              try { vocabDialog.setPointerCapture(e.pointerId); } catch (_) {}
            } else {
              return;
            }
          }
          lastDx = dx;
          const slideX = Math.max(-54, Math.min(54, dx * 0.55));
          vocabDialog.style.transform = `translate3d(${slideX}px, 0, 0)`;
          vocabDialog.style.opacity = String(Math.max(0.65, 1 - Math.abs(slideX) / 220));
        });

        function endVgSwipe(e) {
          if (activeId !== e.pointerId || e.pointerType === "touch") return;
          const wasHorizontal = isHorizontal;
          const dx = lastDx;
          const velocity = Math.abs(dx) / Math.max(1, Date.now() - startTime);
          activeId = null;
          isHorizontal = false;
          isVertical = false;
          vocabDialog.classList.remove("is-dragging");
          if (wasHorizontal) {
            const threshold = Math.min(56, Math.max(32, vocabDialog.clientWidth * 0.14));
            if (Math.abs(dx) >= threshold || (Math.abs(dx) >= 20 && velocity >= 0.25)) {
              stepChapterVocab(dx < 0 ? 1 : -1, true);
            } else {
              vocabDialog.style.transform = "";
              vocabDialog.style.opacity = "";
            }
          }
        }

        vocabDialog.addEventListener("pointerup", endVgSwipe);
        vocabDialog.addEventListener("pointercancel", endVgSwipe);

        let vgWheelLock = 0;
        vocabDialog.addEventListener("wheel", (e) => {
          if (e.ctrlKey) return;
          if (Math.abs(e.deltaX) > Math.abs(e.deltaY) * 1.45 && Math.abs(e.deltaX) >= 24) {
            e.preventDefault();
            const now = Date.now();
            if (now < vgWheelLock) return;
            vgWheelLock = now + 520;
            stepChapterVocab(e.deltaX > 0 ? 1 : -1, true);
          }
        }, { passive: false });
      })();

      document.addEventListener("pointerdown", (e) => {
        const isOpen = vocabDialog.classList.contains("is-fallback-open") ||
          (typeof vocabDialog.matches === "function" && vocabDialog.matches(":popover-open"));
        if (!isOpen) return;
        if (e.target.closest("#vocab-guide, .skz-word, .glossary-item")) return;
        hideVocabGuide();
      });

      document.addEventListener("keydown", (e) => {
        const isOpen = vocabDialog.classList.contains("is-fallback-open") ||
          (typeof vocabDialog.matches === "function" && vocabDialog.matches(":popover-open"));
        if (e.key === "Escape") {
          hideVocabGuide();
        } else if (isOpen && vocabDialog.contains(document.activeElement)) {
          if (e.key === "ArrowLeft") {
            e.preventDefault();
            stepChapterVocab(-1);
          } else if (e.key === "ArrowRight") {
            e.preventDefault();
            stepChapterVocab(1);
          }
        }
      });

      // Init từ URL param
      const reqChap = parseInt(new URLSearchParams(window.location.search).get("chapter") || "1", 10);
      loadChapter(Number.isFinite(reqChap) && reqChap >= 1 && reqChap <= DATA.chapters.length ? reqChap : 1);
    })();
  </script>
</body>
</html>
"""


def build_novel():
    os.makedirs(NOVEL_DIR, exist_ok=True)
    vocab_index = build_unified_shinkanzen_index()
    auto_regex, _ = compile_auto_goi_regex(vocab_index)

    chapters_built = []
    used_glossary_keys = set()

    for ch in NOVEL_CHAPTERS:
        title_segs, title_keys = parse_text_segments(ch["title_jp"], vocab_index, auto_regex)
        chap_keys = list(dict.fromkeys(title_keys))

        paras_built = []
        for raw_jp, vi_txt in ch["paragraphs"]:
            segs, keys = parse_text_segments(raw_jp, vocab_index, auto_regex)
            for k in keys:
                if k not in chap_keys:
                    chap_keys.append(k)
            plain_clean = "".join(strip_furi(s["v"]) for s in segs)
            paras_built.append({
                "segments": segs,
                "plain_text": plain_clean,
                "vi": vi_txt,
            })

        quizzes_built = []
        for q_prompt, q_opts, q_ans, q_exp in ch["quiz"]:
            assert 1 <= q_ans <= len(q_opts), f"Invalid quiz ans in chapter {ch['num']}"
            q_segs, q_keys = parse_text_segments(q_prompt, vocab_index, auto_regex)
            for k in q_keys:
                if k not in chap_keys:
                    chap_keys.append(k)
            quizzes_built.append({
                "prompt_segments": q_segs,
                "options": q_opts,
                "ans": q_ans,
                "exp": q_exp,
            })

        used_glossary_keys.update(chap_keys)
        chapters_built.append({
            "num": ch["num"],
            "slug": ch["slug"],
            "title_jp": ch["title_jp"],
            "title_vi": ch["title_vi"],
            "title_segments": title_segs,
            "yuki_tip": ch["yuki_tip"],
            "paragraphs": paras_built,
            "quiz": quizzes_built,
            "vocab_keys": chap_keys,
        })

    # Chỉ xuất từ điển rút gọn cho những từ/mẫu xuất hiện thực tế trong tiểu thuyết
    glossary_out = {k: vocab_index[k] for k in sorted(used_glossary_keys)}

    payload = {
        "meta": NOVEL_META,
        "chapters": chapters_built,
        "glossary": glossary_out,
    }

    with open(os.path.join(NOVEL_DIR, "novel-data.js"), "w", encoding="utf-8") as f:
        f.write("// Auto-generated by scripts/build_novel.py — Do not edit manually\n")
        f.write("window.SHINKANZEN_NOVEL_DATA = ")
        json.dump(payload, f, ensure_ascii=False, indent=2)
        f.write(";\n")

    with open(os.path.join(NOVEL_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(render_novel_html())

    build_novel_markdown(chapters_built, glossary_out)

    print(
        f"✅ Built Shinkanzen Interactive Novel: {len(chapters_built)} chapters, "
        f"{len(glossary_out)} unique clickable Shinkanzen N2 terms matched across the novel."
    )


if __name__ == "__main__":
    build_novel()
