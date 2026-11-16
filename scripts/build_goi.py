# -*- coding: utf-8 -*-
"""
Builder tạo trọn bộ Shinkanzen Master Từ Vựng N2 (新完全マスター語彙 N2):
- Phần 1 (話題別に言葉を学ぼう): 9 chương, 21 bài -> shinkanzen/tu-vung/phan-1/*.md
- Phần 2 (性質別に言葉を学ぼう): 7 chương, 16 bài -> shinkanzen/tu-vung/phan-2/*.md
- Tổng cộng: 37 bài chuẩn mục lục sách gốc
- Hệ thống Flashcards tương tác & in A4 cho cả 37 bài: flashcards-data.js, flashcards.html, flashcards-anki.tsv, flashcards.md
- Mục lục shinkanzen/tu-vung/README.md
"""
import json
import os
import html
from collections import OrderedDict

from shinkanzen_goi_data_p1 import GOI_PART1
from shinkanzen_goi_data_p2 import GOI_PART2

BASE_OUT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../shinkanzen/tu-vung"))


def escape_md_cell(text):
    return str(text).replace("|", "\\|").replace("\n", " ")


def render_goi_lesson(lesson, idx, total, part_num, prev_rel, next_rel):
    lines = [
        f"# 🌸 {lesson['chapter']} — {lesson['lesson']}: {lesson['title_vi']}",
        f"## Giáo trình: 新完全マスター語彙 N2 — 第{part_num}部（{lesson['chapter']}）",
        "",
        "> 🌸 **Lời dặn của chị Yuki:**  ",
        f"> *\"{lesson['intro']}\"*",
        "",
        f"🎴 [**Mở Flashcards tương tác & Bản in A4 riêng cho bài này**](../flashcards.html?lesson={lesson['id']})",
        "",
        "---",
        "",
        "## 1. Bảng Từ Vựng Trọng Tâm Theo Nhóm",
        "",
    ]

    groups = OrderedDict()
    for w in lesson["words"]:
        assert len(w) == 8, f"Invalid word tuple in {lesson['id']}: {w}"
        groups.setdefault(w[7], []).append(w)

    for g_idx, (g_name, items) in enumerate(groups.items(), 1):
        lines.append(f"### Nhóm {g_idx}: {g_name} ({len(items)} từ)")
        lines.append("")
        lines.append("| STT | Từ vựng (漢字・ふりがな) | Cách đọc | Hán Việt | Nghĩa tiếng Việt | Cụm từ đi kèm (Collocation) |")
        lines.append("| :---: | :--- | :--- | :--- | :--- | :--- |")
        for w_idx, (furi, plain, reading, hv, mean, col_jp, col_vi, _) in enumerate(items, 1):
            col_cell = f"{escape_md_cell(col_jp)}<br>*({escape_md_cell(col_vi)})*"
            lines.append(
                f"| {w_idx} | **{escape_md_cell(furi)}** | `{escape_md_cell(reading)}` | {escape_md_cell(hv)} | {escape_md_cell(mean)} | {col_cell} |"
            )
        lines.append("")

    lines.append("---")
    lines.append("")
    lines.append("## 💡 2. Ghi Chú Phân Biệt & Bẫy Đề Thi (Sister's Notes)")
    lines.append("")
    for note in lesson["notes"]:
        lines.append(f"- {note}")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append(f"## ✍️ 3. Luyện Tập Nhanh ({lesson['lesson']})")
    lines.append("")

    for q_idx, (prompt, opts, ans, exp) in enumerate(lesson["quiz"], 1):
        assert 1 <= ans <= len(opts), f"Invalid quiz answer index in {lesson['id']} Q{q_idx}"
        lines.append(f"### Câu {q_idx}: {prompt}")
        for o_idx, opt in enumerate(opts, 1):
            lines.append(f"{o_idx}. {opt}  ")
        lines.append("<details><summary>👉 Xem đáp án & giải thích của chị</summary>\n")
        lines.append(f"**Đáp án đúng:** {ans} (`{opts[ans - 1]}`)  ")
        lines.append(f"**Giải thích:** {exp}")
        lines.append("</details>")
        lines.append("")

    nav = []
    if prev_rel:
        nav.append(f"[⬅️ Bài trước]({prev_rel})")
    nav.append("[📋 Mục lục Từ vựng](../README.md)")
    nav.append(f"[🎴 Flashcards bài này](../flashcards.html?lesson={lesson['id']})")
    if next_rel:
        nav.append(f"[Bài tiếp theo ➡️]({next_rel})")
    lines.append("---")
    lines.append(" | ".join(nav))
    lines.append("")
    return "\n".join(lines)


def build_flashcards_html(lessons_meta):
    options_html = []
    options_html.append('          <option value="ALL_P1">📘 Toàn bộ Phần 1 (21 bài - Theo chủ đề)</option>')
    options_html.append('          <option value="ALL_P2">📗 Toàn bộ Phần 2 (16 bài - Theo tính chất)</option>')
    for l in lessons_meta:
        part_tag = "P1" if l["part"] == 1 else "P2"
        label = f"[{part_tag}] {l['chapter']} • {l['lesson']}: {l['title_vi']} ({len(l['words'])} từ)"
        options_html.append(f'          <option value="{html.escape(l["id"])}">{html.escape(label)}</option>')
    options_block = "\n".join(options_html)

    return f"""<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Shinkanzen Master N2 Từ Vựng — Flashcards Trắng Đen (37 Bài)</title>
  <style>
    :root {{
      --bg-color: #ffffff;
      --text-main: #000000;
      --text-muted: #555555;
      --border-color: #000000;
      --border-light: #cccccc;
      --accent-bg: #f5f5f5;
      --target-size: 24px;
    }}

    @media (pointer: coarse) {{
      :root {{
        --target-size: 44px;
      }}
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    body {{
      font-family: 'Segoe UI', 'Hiragino Sans', 'Hiragino Kaku Gothic ProN', 'Yu Gothic', Arial, sans-serif;
      background-color: var(--bg-color);
      color: var(--text-main);
      line-height: 1.5;
      padding: 20px;
      overflow-wrap: anywhere;
    }}

    :where(a, button, select, input, [tabindex]):focus-visible {{
      outline: 2px solid CanvasText;
      outline-offset: 3px;
    }}

    :where(.btn, .tab-btn, .nav-pill, select) {{
      min-block-size: var(--target-size);
      touch-action: manipulation;
    }}

    .container {{
      max-width: 940px;
      margin: 0 auto;
    }}

    header {{
      border-bottom: 2px solid var(--border-color);
      padding-bottom: 14px;
      margin-bottom: 18px;
      display: flex;
      justify-content: space-between;
      align-items: flex-end;
      flex-wrap: wrap;
      gap: 10px;
    }}

    h1 {{
      font-size: 1.45rem;
      font-weight: 700;
      letter-spacing: -0.5px;
    }}

    .subtitle {{
      font-size: 0.9rem;
      color: var(--text-muted);
      margin-top: 2px;
    }}

    .header-links {{
      display: flex;
      gap: 8px;
      flex-wrap: wrap;
    }}

    .nav-pill {{
      color: #000;
      text-decoration: none;
      border: 1.5px solid #000;
      padding: 5px 10px;
      font-size: 0.82rem;
      font-weight: 700;
      background: #fff;
    }}

    .nav-pill:hover {{
      background: #000;
      color: #fff;
    }}

    .tabs {{
      display: flex;
      gap: 10px;
      margin-bottom: 18px;
      flex-wrap: wrap;
    }}

    .tab-btn {{
      background: #ffffff;
      color: #000000;
      border: 1.5px solid #000000;
      padding: 8px 16px;
      font-size: 0.9rem;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.15s ease;
    }}

    .tab-btn:hover {{
      background: var(--accent-bg);
    }}

    .tab-btn.active {{
      background: #000000;
      color: #ffffff;
    }}

    #view-interactive {{
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 16px;
    }}

    .controls-bar {{
      width: 100%;
      display: flex;
      flex-direction: column;
      gap: 10px;
      background: var(--accent-bg);
      padding: 12px 15px;
      border: 1.5px solid #000;
      font-size: 0.88rem;
    }}

    .controls-row {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 10px;
    }}

    .controls-row > * {{
      min-width: 0;
      max-width: 100%;
    }}

    .filter-field {{
      display: flex;
      align-items: center;
      flex-wrap: wrap;
      gap: 8px;
      min-width: 0;
      max-width: 100%;
    }}

    .filter-field-lesson {{
      flex: 1 1 260px;
    }}

    .filter-select {{
      padding: 6px 10px;
      border: 1.5px solid #000;
      background: #fff;
      font-size: 0.88rem;
      font-weight: 600;
      min-width: 0;
      max-width: 100%;
      flex: 1 1 180px;
    }}

    .toggle-group {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      cursor: pointer;
      font-weight: 600;
    }}

    .flashcard-stage {{
      width: 100%;
      max-width: 680px;
      height: 360px;
      perspective: 1000px;
      cursor: grab;
      position: relative;
      touch-action: pan-y;
      overscroll-behavior-x: contain;
      user-select: none;
      -webkit-user-select: none;
    }}

    @media (prefers-reduced-motion: no-preference) {{
      .flashcard-stage {{
        transition: transform 0.22s cubic-bezier(0.22, 1, 0.36, 1), opacity 0.2s ease-out;
      }}
      .flashcard-stage.is-dragging {{
        transition: none;
      }}
    }}

    .flashcard-stage.is-dragging {{
      cursor: grabbing;
    }}

    .swipe-cue {{
      position: absolute;
      top: 14px;
      left: 50%;
      transform: translateX(-50%);
      z-index: 6;
      pointer-events: none;
      background: #000000;
      color: #ffffff;
      font-size: 0.78rem;
      font-weight: 700;
      padding: 4px 12px;
      border-radius: 999px;
      opacity: 0;
      transition: opacity 0.12s ease;
      white-space: nowrap;
    }}

    .swipe-cue.is-visible {{
      opacity: 0.92;
    }}

    .flashcard-inner {{
      width: 100%;
      height: 100%;
      position: relative;
      transition: transform 0.4s cubic-bezier(0.2, 0.85, 0.4, 1);
      transform-style: preserve-3d;
      border: 2px solid #000000;
      box-shadow: 6px 6px 0px #000000;
      background: #ffffff;
    }}

    .flashcard-stage.is-flipped .flashcard-inner {{
      transform: rotateY(180deg);
    }}

    .card-face {{
      position: absolute;
      width: 100%;
      height: 100%;
      backface-visibility: hidden;
      overflow-y: auto;
      padding: 26px 24px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      background: #ffffff;
    }}

    .flashcard-stage.is-flipped .card-front {{
      pointer-events: none;
    }}

    .flashcard-stage:not(.is-flipped) .card-back {{
      pointer-events: none;
    }}

    .card-back {{
      transform: rotateY(180deg);
    }}

    .card-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 0.8rem;
      font-weight: 600;
      border-bottom: 1px dashed var(--border-light);
      padding-bottom: 8px;
      gap: 8px;
    }}

    .card-badge {{
      background: #000000;
      color: #ffffff;
      padding: 2px 8px;
      font-size: 0.74rem;
      border-radius: 2px;
    }}

    .card-center {{
      margin: auto 0;
      text-align: center;
    }}

    .furigana-text {{
      font-size: 1.15rem;
      color: var(--text-muted);
      margin-bottom: 4px;
      min-height: 1.5rem;
      transition: opacity 0.2s;
    }}

    .furigana-text.hidden {{
      opacity: 0;
      visibility: hidden;
    }}

    .kanji-text {{
      font-size: 2.7rem;
      font-weight: 700;
      letter-spacing: 1px;
      color: #000000;
      line-height: 1.25;
    }}

    .hanviet-text {{
      font-size: 0.96rem;
      font-weight: 700;
      letter-spacing: 1.5px;
      text-transform: uppercase;
      margin-top: 8px;
      color: var(--text-muted);
    }}

    .card-hint {{
      font-size: 0.8rem;
      color: #777777;
      border-top: 1px dashed var(--border-light);
      padding-top: 8px;
      text-align: center;
    }}

    .back-meaning {{
      font-size: 1.25rem;
      font-weight: 700;
      margin-bottom: 12px;
      text-align: left;
    }}

    .back-collocation {{
      background: #f8f8f8;
      border-left: 3px solid #000;
      padding: 10px 14px;
      text-align: left;
      font-size: 0.95rem;
      margin-bottom: 10px;
    }}

    .back-collocation-jp {{
      font-weight: 600;
      font-size: 1.02rem;
      margin-bottom: 4px;
    }}

    .back-note {{
      font-size: 0.84rem;
      color: #333333;
      text-align: left;
      border: 1px solid #d9d9d9;
      padding: 7px 10px;
      margin-top: 6px;
    }}

    .action-row {{
      display: flex;
      gap: 12px;
      align-items: center;
      justify-content: center;
      width: 100%;
      max-width: 680px;
    }}

    .btn {{
      background: #ffffff;
      color: #000000;
      border: 2px solid #000000;
      padding: 10px 20px;
      font-size: 0.95rem;
      font-weight: 700;
      cursor: pointer;
      box-shadow: 3px 3px 0px #000000;
      transition: all 0.1s ease;
    }}

    .btn:active {{
      transform: translate(2px, 2px);
      box-shadow: 1px 1px 0px #000000;
    }}

    .btn-flip {{
      flex: 1;
      background: #000000;
      color: #ffffff;
    }}

    .progress-bar {{
      font-size: 0.9rem;
      font-weight: 600;
    }}

    .keyboard-tips {{
      font-size: 0.78rem;
      color: #555555;
      text-align: center;
    }}

    @media (max-width: 600px) {{
      body {{
        padding: 12px;
      }}
      .controls-row {{
        flex-direction: column;
        align-items: stretch;
      }}
      .filter-field {{
        flex: 1 1 auto;
      }}
      .filter-select {{
        width: 100%;
        flex: 1 1 100%;
      }}
      .flashcard-stage {{
        height: 340px;
      }}
      .card-face {{
        padding: 18px 16px;
      }}
      .kanji-text {{
        font-size: 2.2rem;
      }}
      .action-row {{
        gap: 8px;
        flex-wrap: wrap;
      }}
      .action-row .btn {{
        flex: 1 1 auto;
      }}
    }}

    #view-print {{
      display: none;
    }}

    .print-instructions {{
      background: #f8f8f8;
      border: 1.5px solid #000000;
      padding: 14px 18px;
      margin-bottom: 20px;
      font-size: 0.9rem;
    }}

    .print-instructions h3 {{
      font-size: 1rem;
      margin-bottom: 6px;
    }}

    .print-instructions ul {{
      padding-left: 20px;
      margin-top: 6px;
    }}

    .print-options-bar {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 18px;
      flex-wrap: wrap;
      gap: 10px;
    }}

    .print-grid {{
      display: grid;
      grid-template-columns: 1fr;
      gap: 12px;
    }}

    .foldable-card-row {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      border: 1.5px dashed #000000;
      page-break-inside: avoid;
      background: #ffffff;
      min-height: 142px;
      position: relative;
    }}

    .foldable-card-row::before {{
      content: "✂";
      position: absolute;
      top: -10px;
      left: 10px;
      background: #fff;
      padding: 0 4px;
      font-size: 12px;
    }}

    .cut-col-front {{
      border-right: 1.5px dotted #666666;
      padding: 12px 14px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      text-align: center;
    }}

    .cut-col-back {{
      padding: 12px 14px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }}

    .cut-card-num {{
      font-size: 0.7rem;
      font-weight: 700;
      text-align: left;
      border-bottom: 1px solid #e0e0e0;
      padding-bottom: 2px;
      margin-bottom: 4px;
      display: flex;
      justify-content: space-between;
      gap: 6px;
    }}

    .cut-card-kanji {{
      font-size: 1.55rem;
      font-weight: 800;
      line-height: 1.25;
    }}

    .cut-card-furi {{
      font-size: 0.85rem;
      color: #444;
      margin-bottom: 2px;
    }}

    .cut-card-hv {{
      font-size: 0.74rem;
      font-weight: 700;
      letter-spacing: 1px;
      color: #555;
    }}

    .cut-card-meaning {{
      font-size: 0.92rem;
      font-weight: 700;
      margin-bottom: 4px;
      border-bottom: 1px solid #eee;
      padding-bottom: 4px;
    }}

    .cut-card-example {{
      font-size: 0.78rem;
      line-height: 1.35;
      color: #222;
    }}

    .cut-card-colloc {{
      font-weight: 600;
    }}

    .cut-card-subtip {{
      font-size: 0.72rem;
      color: #555;
      margin-top: 4px;
      font-style: italic;
    }}

    .fold-line-label {{
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%) rotate(90deg);
      font-size: 0.62rem;
      color: #999;
      background: #fff;
      padding: 2px 4px;
      letter-spacing: 1px;
      pointer-events: none;
    }}

    @media print {{
      @page {{
        size: A4 portrait;
        margin: 10mm;
      }}

      body {{
        padding: 0;
        background: #fff;
        color: #000;
      }}

      header, .tabs, .controls-bar, .print-instructions, .print-options-bar, #view-interactive, .keyboard-tips {{
        display: none !important;
      }}

      #view-print {{
        display: block !important;
      }}

      .container {{
        max-width: 100%;
        margin: 0;
      }}

      .foldable-card-row {{
        border: 1px dashed #000000 !important;
        break-inside: avoid;
        page-break-inside: avoid;
        margin-bottom: 8px;
        min-height: 135px;
      }}

      .cut-col-front {{
        border-right: 1px dotted #000000 !important;
      }}
    }}
  </style>
</head>
<body>

<div class="container">
  <header>
    <div>
      <h1>Shinkanzen Master N2 Từ Vựng — Flashcards (37 Bài)</h1>
      <div class="subtitle" id="deckSubtitle">Chuẩn sách 新完全マスター語彙 N2 (第1部 21 bài + 第2部 16 bài) • Trắng & Đen tiết kiệm mực</div>
    </div>
    <div class="header-links">
      <a href="../../index.html" class="nav-pill">🏠 Trang chủ</a>
      <a href="../../novel/index.html" class="nav-pill">📓 Tiểu thuyết N2</a>
      <a id="openLessonMdBtn" href="../../reader.html?file=shinkanzen/tu-vung/README.md" class="nav-pill">📖 Đọc bài học</a>
      <a href="./flashcards-anki.tsv" download class="nav-pill">📥 Tải Anki TSV</a>
    </div>
  </header>

  <div class="tabs">
    <button type="button" class="tab-btn active" onclick="switchView('interactive')">🎴 Học Lật Thẻ Tương Tác</button>
    <button type="button" class="tab-btn" onclick="switchView('print')">🖨️ Bản In A4 Cắt Rời (Gập Đôi)</button>
  </div>

  <div class="controls-bar" id="sharedControls">
    <div class="controls-row">
      <div class="filter-field filter-field-lesson">
        <label for="lesson-select" style="font-weight: 700;">📚 Bài học:</label>
        <select id="lesson-select" class="filter-select" onchange="onLessonChange()">
{options_block}
        </select>
      </div>
      <div class="filter-field">
        <label for="group-filter" style="font-weight: 700;">🏷️ Nhóm:</label>
        <select id="group-filter" class="filter-select" onchange="onGroupChange()">
          <option value="ALL">Tất cả nhóm</option>
        </select>
      </div>
    </div>
    <div class="controls-row">
      <div style="display: flex; gap: 16px; align-items: center; flex-wrap: wrap;">
        <label class="toggle-group">
          <input type="checkbox" id="toggle-furigana" onchange="toggleFurigana(this.checked)" checked>
          <span>Hiện Furigana</span>
        </label>
        <label class="toggle-group">
          <input type="checkbox" id="toggle-reverse" onchange="toggleReverse(this.checked)">
          <span>Đảo mặt (Nghĩa Việt ➔ Kanji)</span>
        </label>
      </div>
      <div style="display: flex; gap: 8px; flex-wrap: wrap;">
        <button type="button" class="tab-btn" style="padding: 5px 12px;" onclick="shuffleCards()">🔀 Xáo thẻ</button>
        <button type="button" class="tab-btn" style="padding: 5px 12px;" onclick="resetOrder()">↺ Thứ tự sách</button>
      </div>
    </div>
  </div>

  <div id="view-interactive" style="margin-top: 16px;">
    <div class="flashcard-stage" id="cardStage" role="region" aria-roledescription="flashcard" aria-label="Thẻ từ vựng hiện tại">
      <div class="swipe-cue" id="swipeCue" aria-hidden="true"></div>
      <div class="flashcard-inner" id="cardInner">
        <div class="card-face card-front">
          <div class="card-header">
            <span class="card-badge" id="card-group-badge">Bài 1</span>
            <span id="card-counter-badge">1 / 1</span>
          </div>
          <div class="card-center">
            <div class="furigana-text" id="front-furi">そせん</div>
            <div class="kanji-text" id="front-kanji">祖先</div>
            <div class="hanviet-text" id="front-hv">[ TỔ TIÊN ]</div>
          </div>
          <div class="card-hint">
            👆 Vuốt trái / phải để qua từ khác • Chạm thẻ hoặc [Space] để lật ➔
          </div>
        </div>

        <div class="card-face card-back">
          <div class="card-header">
            <span class="card-badge" id="back-group-badge">Bài 1</span>
            <span id="back-kanji-small" style="font-weight: 700; font-size: 0.95rem;">祖先（そせん）</span>
          </div>
          <div class="card-center" style="text-align: left;">
            <div class="back-meaning" id="back-meaning">Tổ tiên</div>
            <div class="back-collocation">
              <div style="font-size: 0.74rem; text-transform: uppercase; color: #666; margin-bottom: 2px;">Cụm từ Collocation Shinkanzen:</div>
              <div class="back-collocation-jp" id="back-colloc-jp">人類の祖先</div>
              <div style="font-size: 0.85rem; color: #333;" id="back-colloc-vi">Tổ tiên loài người</div>
            </div>
            <div class="back-note" id="back-note">
              💡 <strong>Bài học:</strong> Shinkanzen Master N2
            </div>
          </div>
          <div class="card-hint">
            👆 Vuốt trái / phải để qua từ khác • Chạm thẻ để quay lại mặt trước ↺
          </div>
        </div>
      </div>
    </div>

    <div class="action-row">
      <button type="button" class="btn" onclick="prevCard()" title="Vuốt sang phải hoặc mũi tên Trái [←]">◀ Trước</button>
      <button type="button" class="btn btn-flip" onclick="flipCard()">Lật Thẻ (Space)</button>
      <button type="button" class="btn" onclick="nextCard()" title="Vuốt sang trái hoặc mũi tên Phải [→]">Sau ▶</button>
    </div>

    <div class="progress-bar" id="progressText" role="status" aria-live="polite">Thẻ 1 / 1</div>

    <div class="keyboard-tips">
      👆 Cảm ứng / Trackpad: <strong>Vuốt trái / phải</strong> để đổi từ • ⌨️ Phím: <strong>[Space]</strong> Lật mặt • <strong>[←] / [→]</strong> Trước / Sau • <strong>[F]</strong> Furigana • <strong>[R]</strong> Đảo mặt
    </div>
  </div>

  <div id="view-print" style="margin-top: 16px;">
    <div class="print-instructions">
      <h3>✂️ Hướng Dẫn In Ấn & Cắt Thẻ Trắng Đen (Khổ A4)</h3>
      <ul>
        <li>Chọn bài học hoặc nhóm từ ở thanh công cụ phía trên trước khi nhấn nút In.</li>
        <li>Mỗi hàng là 1 thẻ hoàn chỉnh (Nửa trái: Mặt trước, Nửa phải: Mặt sau). Cắt theo nét đứt ✂️ rồi <strong>gập đôi ở trục giữa</strong> — không bao giờ bị lệch trang khi in 1 mặt.</li>
      </ul>
    </div>

    <div class="print-options-bar">
      <div id="printCountLabel"><strong>Số thẻ sẽ in:</strong> 0 thẻ</div>
      <div>
        <button type="button" class="btn btn-flip" style="padding: 8px 18px;" onclick="window.print()">🖨️ In Bộ Thẻ Đang Chọn (Ctrl/Cmd + P)</button>
      </div>
    </div>

    <div class="print-grid" id="printCardsContainer"></div>
  </div>
</div>

<script src="./flashcards-data.js"></script>
<script>
const LESSONS = window.SHINKANZEN_GOI_LESSONS || [];
let baseCards = [];
let deck = [];
let currentIndex = 0;
let showFuri = true;
let reverseMode = false;

function esc(s) {{
  return String(s || "").replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");
}}

function getLessonCards(selectionId) {{
  if (selectionId === "ALL_P1") {{
    return LESSONS.filter(l => l.part === 1).flatMap(l => l.words.map(w => ({{ ...w, lessonLabel: `${{l.chapter}} • ${{l.lesson}}`, mdPath: l.mdPath }})));
  }}
  if (selectionId === "ALL_P2") {{
    return LESSONS.filter(l => l.part === 2).flatMap(l => l.words.map(w => ({{ ...w, lessonLabel: `${{l.chapter}} • ${{l.lesson}}`, mdPath: l.mdPath }})));
  }}
  const found = LESSONS.find(l => l.id === selectionId) || LESSONS[0];
  if (!found) return [];
  return found.words.map(w => ({{ ...w, lessonLabel: `${{found.chapter}} • ${{found.lesson}}`, mdPath: found.mdPath }}));
}}

function populateGroupFilter(cards) {{
  const select = document.getElementById("group-filter");
  const groups = Array.from(new Set(cards.map(c => c.group)));
  select.innerHTML = `<option value="ALL">Tất cả (${{cards.length}} từ)</option>`;
  groups.forEach(g => {{
    const count = cards.filter(c => c.group === g).length;
    const opt = document.createElement("option");
    opt.value = g;
    opt.textContent = `${{g}} (${{count}})`;
    select.appendChild(opt);
  }});
}}

function updateHeaderLinks(selectionId) {{
  const found = LESSONS.find(l => l.id === selectionId);
  const btn = document.getElementById("openLessonMdBtn");
  const sub = document.getElementById("deckSubtitle");
  if (found) {{
    btn.href = `../../reader.html?file=shinkanzen/tu-vung/${{found.mdPath}}`;
    btn.textContent = `📖 Đọc bài: ${{found.lesson}}`;
    sub.textContent = `Phần ${{found.part}} • ${{found.chapter}} — ${{found.lesson}}: ${{found.title_vi}} (${{found.words.length}} từ)`;
  }} else {{
    btn.href = "../../reader.html?file=shinkanzen/tu-vung/README.md";
    btn.textContent = "📋 Mục lục Từ vựng";
    sub.textContent = selectionId === "ALL_P1"
      ? "Toàn bộ Phần 1 (21 bài theo chủ đề • 新完全マスター語彙 N2)"
      : "Toàn bộ Phần 2 (16 bài theo tính chất • 新完全マスター語彙 N2)";
  }}
}}

function onLessonChange() {{
  const selectionId = document.getElementById("lesson-select").value;
  baseCards = getLessonCards(selectionId);
  populateGroupFilter(baseCards);
  updateHeaderLinks(selectionId);
  try {{
    const url = new URL(window.location.href);
    url.searchParams.set("lesson", selectionId);
    window.history.replaceState({{}}, "", url.toString());
  }} catch (_) {{}}
  onGroupChange();
}}

function onGroupChange() {{
  settlePendingTransition();
  hideSwipeCue();
  resetCardTransform(false);
  const grp = document.getElementById("group-filter").value;
  deck = grp === "ALL" ? [...baseCards] : baseCards.filter(c => c.group === grp);
  currentIndex = 0;
  cardStage.classList.remove("is-flipped");
  renderCard();
  renderPrintCards();
}}

function renderCard() {{
  if (!deck.length) return;
  const item = deck[currentIndex];
  const furiEl = document.getElementById("front-furi");
  const kanjiEl = document.getElementById("front-kanji");
  const hvEl = document.getElementById("front-hv");

  document.getElementById("card-group-badge").textContent = item.group;
  document.getElementById("back-group-badge").textContent = item.lessonLabel;
  document.getElementById("card-counter-badge").textContent = `${{currentIndex + 1}} / ${{deck.length}}`;
  document.getElementById("progressText").textContent = `Thẻ ${{currentIndex + 1}} / ${{deck.length}}`;

  if (!reverseMode) {{
    furiEl.textContent = item.reading;
    furiEl.classList.toggle("hidden", !showFuri);
    kanjiEl.textContent = item.plain;
    kanjiEl.style.fontSize = item.plain.length > 8 ? "2rem" : "2.7rem";
    hvEl.textContent = `[ ${{item.hv}} ]`;

    document.getElementById("back-kanji-small").textContent = item.furi;
    document.getElementById("back-meaning").textContent = item.mean;
  }} else {{
    furiEl.textContent = `[ ${{item.hv}} ]`;
    furiEl.classList.remove("hidden");
    kanjiEl.textContent = item.mean;
    kanjiEl.style.fontSize = "1.55rem";
    hvEl.textContent = item.group;

    document.getElementById("back-kanji-small").textContent = item.mean;
    document.getElementById("back-meaning").textContent = item.furi;
  }}

  document.getElementById("back-colloc-jp").textContent = item.collocJp;
  document.getElementById("back-colloc-vi").textContent = item.collocVi;
  document.getElementById("back-note").innerHTML = `💡 <strong>Chủ điểm:</strong> ${{esc(item.lessonLabel)}} — <em>${{esc(item.group)}}</em>`;
}}

const cardStage = document.getElementById("cardStage");
const swipeCue = document.getElementById("swipeCue");
const prefersReducedMotion = () => Boolean(window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches);
let cardExitTimer = null;
let cardEnterRaf = null;
let pendingCommit = null;
let suppressClickUntil = 0;

function hideSwipeCue() {{
  swipeCue.classList.remove("is-visible");
  swipeCue.textContent = "";
}}

function resetCardTransform(withTransition = true) {{
  if (!withTransition) cardStage.classList.add("is-dragging");
  cardStage.style.transform = "";
  cardStage.style.opacity = "";
  if (!withTransition) {{
    void cardStage.offsetWidth;
    cardStage.classList.remove("is-dragging");
  }}
}}

function settlePendingTransition() {{
  if (cardExitTimer) {{
    clearTimeout(cardExitTimer);
    cardExitTimer = null;
  }}
  if (cardEnterRaf) {{
    cancelAnimationFrame(cardEnterRaf);
    cardEnterRaf = null;
  }}
  if (pendingCommit) {{
    const fn = pendingCommit;
    pendingCommit = null;
    fn();
  }}
}}

function flipCard() {{
  cardStage.classList.toggle("is-flipped");
}}

function goCard(step) {{
  if (!deck.length) return;
  hideSwipeCue();
  settlePendingTransition();
  if (deck.length === 1) {{
    resetCardTransform(true);
    cardStage.classList.remove("is-flipped");
    renderCard();
    return;
  }}

  cardStage.classList.remove("is-flipped");
  const commit = () => {{
    currentIndex = (currentIndex + step + deck.length) % deck.length;
    renderCard();
  }};

  if (prefersReducedMotion()) {{
    commit();
    resetCardTransform(false);
    return;
  }}

  pendingCommit = commit;
  cardStage.classList.remove("is-dragging");
  const exitX = step > 0 ? -105 : 105;
  const exitRot = step > 0 ? -4 : 4;
  cardStage.style.transform = `translate3d(${{exitX}}px, 0, 0) rotate(${{exitRot}}deg)`;
  cardStage.style.opacity = "0";

  cardExitTimer = setTimeout(() => {{
    cardExitTimer = null;
    if (pendingCommit) {{
      const fn = pendingCommit;
      pendingCommit = null;
      fn();
    }}
    cardStage.classList.add("is-dragging");
    const enterX = step > 0 ? 70 : -70;
    cardStage.style.transform = `translate3d(${{enterX}}px, 0, 0) rotate(${{-exitRot * 0.5}}deg)`;
    cardStage.style.opacity = "0";
    void cardStage.offsetWidth;

    cardEnterRaf = requestAnimationFrame(() => {{
      cardEnterRaf = null;
      cardStage.classList.remove("is-dragging");
      cardStage.style.transform = "";
      cardStage.style.opacity = "";
    }});
  }}, 125);
}}

function nextCard() {{
  goCard(1);
}}

function prevCard() {{
  goCard(-1);
}}

(function attachCardSwipe() {{
  cardStage.addEventListener("click", (e) => {{
    if (Date.now() < suppressClickUntil) {{
      e.preventDefault();
      return;
    }}
    flipCard();
  }});

  let activeId = null;
  let startX = 0;
  let startY = 0;
  let startTime = 0;
  let lastDx = 0;
  let isHorizontal = false;
  let isVertical = false;

  cardStage.addEventListener("pointerdown", (e) => {{
    if (!e.isPrimary) return;
    if (e.pointerType === "mouse" && e.button !== 0) return;
    settlePendingTransition();
    activeId = e.pointerId;
    startX = e.clientX;
    startY = e.clientY;
    startTime = Date.now();
    lastDx = 0;
    isHorizontal = false;
    isVertical = false;
  }});

  cardStage.addEventListener("pointermove", (e) => {{
    if (activeId !== e.pointerId || isVertical) return;
    const dx = e.clientX - startX;
    const dy = e.clientY - startY;

    if (!isHorizontal) {{
      if (Math.abs(dy) > 10 && Math.abs(dy) >= Math.abs(dx)) {{
        isVertical = true;
        activeId = null;
        return;
      }}
      if (Math.abs(dx) > 10 && Math.abs(dx) > Math.abs(dy) * 1.15) {{
        isHorizontal = true;
        cardStage.classList.add("is-dragging");
        try {{ cardStage.setPointerCapture(e.pointerId); }} catch (_) {{}}
      }} else {{
        return;
      }}
    }}

    lastDx = dx;
    const previewX = deck.length > 1 ? dx : dx * 0.25;
    const rot = Math.max(-5, Math.min(5, previewX * 0.025));
    cardStage.style.transform = `translate3d(${{previewX}}px, 0, 0) rotate(${{rot}}deg)`;
    cardStage.style.opacity = String(Math.max(0.55, 1 - Math.abs(previewX) / 360));

    if (deck.length > 1 && Math.abs(dx) > 18) {{
      swipeCue.textContent = dx < 0 ? "Thẻ sau ➔" : "⬅ Thẻ trước";
      swipeCue.classList.add("is-visible");
    }} else {{
      hideSwipeCue();
    }}
  }});

  function endSwipe(e) {{
    if (activeId !== e.pointerId) return;
    const wasHorizontal = isHorizontal;
    const dx = lastDx;
    const dt = Math.max(1, Date.now() - startTime);
    const velocity = Math.abs(dx) / dt;
    activeId = null;
    isHorizontal = false;
    isVertical = false;
    cardStage.classList.remove("is-dragging");
    hideSwipeCue();

    if (wasHorizontal) {{
      suppressClickUntil = Date.now() + 360;
      const distThreshold = Math.min(72, Math.max(38, cardStage.clientWidth * 0.16));
      if (e.type === "pointerup" && deck.length > 1 && (Math.abs(dx) >= distThreshold || (Math.abs(dx) >= 24 && velocity >= 0.32))) {{
        goCard(dx < 0 ? 1 : -1);
      }} else {{
        resetCardTransform(true);
      }}
    }}
  }}

  cardStage.addEventListener("pointerup", endSwipe);
  cardStage.addEventListener("pointercancel", endSwipe);

  let wheelLockUntil = 0;
  cardStage.addEventListener("wheel", (e) => {{
    if (e.ctrlKey) return;
    if (Math.abs(e.deltaX) > Math.abs(e.deltaY) * 1.45 && Math.abs(e.deltaX) >= 24) {{
      e.preventDefault();
      const now = Date.now();
      if (now < wheelLockUntil) return;
      wheelLockUntil = now + 520;
      goCard(e.deltaX > 0 ? 1 : -1);
    }}
  }}, {{ passive: false }});
}})();

function shuffleCards() {{
  for (let i = deck.length - 1; i > 0; i--) {{
    const j = Math.floor(Math.random() * (i + 1));
    [deck[i], deck[j]] = [deck[j], deck[i]];
  }}
  currentIndex = 0;
  document.getElementById("cardStage").classList.remove("is-flipped");
  renderCard();
  renderPrintCards();
}}

function resetOrder() {{
  onGroupChange();
}}

function toggleFurigana(val) {{
  showFuri = val;
  renderCard();
}}

function toggleReverse(val) {{
  reverseMode = val;
  document.getElementById("cardStage").classList.remove("is-flipped");
  renderCard();
}}

function switchView(viewName) {{
  const btns = document.querySelectorAll(".tabs .tab-btn");
  const vInteractive = document.getElementById("view-interactive");
  const vPrint = document.getElementById("view-print");
  if (viewName === "interactive") {{
    btns[0].classList.add("active");
    btns[1].classList.remove("active");
    vInteractive.style.display = "flex";
    vPrint.style.display = "none";
  }} else {{
    btns[1].classList.add("active");
    btns[0].classList.remove("active");
    vInteractive.style.display = "none";
    vPrint.style.display = "block";
    renderPrintCards();
  }}
}}

function renderPrintCards() {{
  const container = document.getElementById("printCardsContainer");
  const countLabel = document.getElementById("printCountLabel");
  container.innerHTML = "";
  countLabel.innerHTML = `<strong>Số thẻ sẽ in:</strong> ${{deck.length}} thẻ (~${{Math.max(1, Math.ceil(deck.length / 7))}} trang A4)`;

  deck.forEach((item, idx) => {{
    const row = document.createElement("div");
    row.className = "foldable-card-row";
    row.innerHTML = `
      <span class="fold-line-label">ĐƯỜNG GẬP ĐÔI</span>
      <div class="cut-col-front">
        <div class="cut-card-num">
          <span>THẺ #${{idx + 1}}</span>
          <span>N2 • ${{esc(item.lessonId.toUpperCase())}}</span>
        </div>
        <div style="margin: auto 0;">
          <div class="cut-card-furi">${{esc(item.reading)}}</div>
          <div class="cut-card-kanji">${{esc(item.plain)}}</div>
          <div class="cut-card-hv">[ ${{esc(item.hv)}} ]</div>
        </div>
        <div style="font-size: 0.65rem; color: #666; text-align: center;">${{esc(item.group)}}</div>
      </div>
      <div class="cut-col-back">
        <div>
          <div class="cut-card-num">
            <span>Ý NGHĨA & CỤM TỪ</span>
            <span>${{esc(item.plain)}}（${{esc(item.reading)}}）</span>
          </div>
          <div class="cut-card-meaning">${{esc(item.mean)}}</div>
          <div class="cut-card-example">
            <span class="cut-card-colloc">${{esc(item.collocJp)}}</span><br>
            <span style="color: #444;">↳ ${{esc(item.collocVi)}}</span>
          </div>
        </div>
        <div class="cut-card-subtip">${{esc(item.lessonLabel)}}</div>
      </div>
    `;
    container.appendChild(row);
  }});
}}

window.addEventListener("keydown", (e) => {{
  const vInteractive = document.getElementById("view-interactive");
  if (vInteractive.style.display === "none") return;
  if (["INPUT", "SELECT", "TEXTAREA"].includes(document.activeElement.tagName)) return;

  if (e.code === "Space") {{
    e.preventDefault();
    flipCard();
  }} else if (e.code === "ArrowRight") {{
    e.preventDefault();
    nextCard();
  }} else if (e.code === "ArrowLeft") {{
    e.preventDefault();
    prevCard();
  }} else if (e.code === "KeyF") {{
    const cb = document.getElementById("toggle-furigana");
    cb.checked = !cb.checked;
    toggleFurigana(cb.checked);
  }} else if (e.code === "KeyR") {{
    const cb = document.getElementById("toggle-reverse");
    cb.checked = !cb.checked;
    toggleReverse(cb.checked);
  }}
}});

(function init() {{
  const params = new URLSearchParams(window.location.search);
  const reqLesson = params.get("lesson");
  const select = document.getElementById("lesson-select");
  if (reqLesson && Array.from(select.options).some(o => o.value === reqLesson)) {{
    select.value = reqLesson;
  }} else if (LESSONS.length > 0) {{
    select.value = LESSONS[0].id;
  }}
  onLessonChange();
}})();
</script>
</body>
</html>
"""


def build_goi():
    assert len(GOI_PART1) == 21, f"Expected 21 Part 1 lessons, got {len(GOI_PART1)}"
    assert len(GOI_PART2) == 16, f"Expected 16 Part 2 lessons, got {len(GOI_PART2)}"

    p1_dir = os.path.join(BASE_OUT, "phan-1")
    p2_dir = os.path.join(BASE_OUT, "phan-2")
    os.makedirs(p1_dir, exist_ok=True)
    os.makedirs(p2_dir, exist_ok=True)

    all_lessons_ordered = []
    for l in GOI_PART1:
        all_lessons_ordered.append((1, l, f"phan-1/{l['filename']}"))
    for l in GOI_PART2:
        all_lessons_ordered.append((2, l, f"phan-2/{l['filename']}"))

    seen_ids = set()
    seen_paths = set()
    total_words = 0
    anki_rows = ["#separator:tab", "#html:true", "#tags column:5"]
    js_lessons = []

    for idx, (part_num, lesson, rel_path) in enumerate(all_lessons_ordered):
        assert lesson["id"] not in seen_ids, f"Duplicate lesson id: {lesson['id']}"
        assert rel_path not in seen_paths, f"Duplicate path: {rel_path}"
        seen_ids.add(lesson["id"])
        seen_paths.add(rel_path)

        prev_rel = f"../{all_lessons_ordered[idx - 1][2]}" if idx > 0 else None
        next_rel = f"../{all_lessons_ordered[idx + 1][2]}" if idx + 1 < len(all_lessons_ordered) else None

        md_content = render_goi_lesson(lesson, idx + 1, len(all_lessons_ordered), part_num, prev_rel, next_rel)
        out_path = os.path.join(BASE_OUT, rel_path)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(md_content)

        words_js = []
        for w_idx, (furi, plain, reading, hv, mean, col_jp, col_vi, group) in enumerate(lesson["words"], 1):
            total_words += 1
            words_js.append({
                "id": w_idx,
                "lessonId": lesson["id"],
                "group": group,
                "furi": furi,
                "plain": plain,
                "reading": reading,
                "hv": hv,
                "mean": mean,
                "collocJp": col_jp,
                "collocVi": col_vi,
            })

            front_html = f"<div style='font-size:28px;font-weight:bold'>{html.escape(plain)}</div><div style='color:#666'>{html.escape(reading)} • [{html.escape(hv)}]</div>"
            back_html = f"<div><b>{html.escape(mean)}</b></div><hr><div>{html.escape(col_jp)}</div><div style='color:#444'><i>{html.escape(col_vi)}</i></div>"
            clean_group = group.replace(" ", "_")
            tags = f"N2 Shinkanzen TuVung {lesson['id']} {clean_group}"
            anki_rows.append(
                f"{front_html}\t{back_html}\t{html.escape(furi)}\t{html.escape(lesson['chapter'] + ' - ' + lesson['lesson'])}\t{tags}"
            )

        js_lessons.append({
            "id": lesson["id"],
            "part": part_num,
            "chapter": lesson["chapter"],
            "lesson": lesson["lesson"],
            "title_vi": lesson["title_vi"],
            "mdPath": rel_path,
            "words": words_js,
        })

    # Write flashcards-data.js
    with open(os.path.join(BASE_OUT, "flashcards-data.js"), "w", encoding="utf-8") as f:
        f.write("// Auto-generated by scripts/build_goi.py — Do not edit manually\n")
        f.write("window.SHINKANZEN_GOI_LESSONS = ")
        json.dump(js_lessons, f, ensure_ascii=False, indent=2)
        f.write(";\n")

    # Write flashcards-anki.tsv
    with open(os.path.join(BASE_OUT, "flashcards-anki.tsv"), "w", encoding="utf-8") as f:
        f.write("\n".join(anki_rows) + "\n")

    # Write flashcards.html
    with open(os.path.join(BASE_OUT, "flashcards.html"), "w", encoding="utf-8") as f:
        f.write(build_flashcards_html(js_lessons))

    # Write flashcards.md
    flashcards_md = [
        "# 🎴 Hệ Thống Flashcards Từ Vựng Shinkanzen Master N2 (37 Bài)",
        "",
        f"Tổng cộng **{total_words} từ vựng trọng tâm** phủ trọn **第1部 (21 bài theo chủ đề)** và **第2部 (16 bài theo tính chất)**.",
        "",
        "## 1. Các Công Cụ Luyện Thẻ Sẵn Có",
        "- [**Mở Web Flashcards Trắng Đen + In A4 Gập Đôi**](./flashcards.html): Lọc theo từng bài hoặc học trọn Phần 1 / Phần 2, đảo mặt Việt ➔ Nhật, ẩn/hiện Furigana, bấm in A4 không bao giờ lệch trang.",
        "- [**Tải Bộ Deck Anki (`flashcards-anki.tsv`)**](./flashcards-anki.tsv): Import trực tiếp vào Anki Desktop/Mobile (`File -> Import`, phân tách `Tab`, bật `Allow HTML`, Tags ở cột 5).",
        "",
        "## 2. Mở Nhanh Flashcards Từng Bài",
        "",
        "| Phần | Chương & Bài | Tên Tiếng Việt | Số từ | Link Flashcard |",
        "| :---: | :--- | :--- | :---: | :--- |",
    ]
    for l in js_lessons:
        flashcards_md.append(
            f"| 第{l['part']}部 | {l['chapter']} • {l['lesson']} | [{l['title_vi']}](./{l['mdPath']}) | {len(l['words'])} | [🎴 Luyện thẻ](./flashcards.html?lesson={l['id']}) |"
        )
    flashcards_md.extend(["", "[⬅️ Quay lại Mục lục Từ vựng](./README.md)", ""])
    with open(os.path.join(BASE_OUT, "flashcards.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(flashcards_md))

    # Write tu-vung/README.md
    readme = [
        "# 📚 新完全マスター語彙 N2 — Mục Lục Trọn Bộ Từ Vựng (37 Bài)",
        "",
        f"Tổng hợp **37 bài học ({total_words} từ vựng & collocation cốt lõi)** bám sát 100% mục lục giáo trình **Shinkanzen Master Từ vựng N2** (スリーエーネットワーク).",
        "",
        "🎴 [**Mở Flashcards Tương Tác & Bản In A4 (Cả 37 Bài)**](./flashcards.html) | 📥 [**Anki TSV**](./flashcards-anki.tsv) | 📖 [**Hướng dẫn Flashcards**](./flashcards.md)",
        "",
        "---",
        "",
        "## 📘 第1部：話題別に言葉を学ぼう (Phần 1: Theo Chủ Đề — 9 Chương, 21 Bài)",
        "",
        "| STT | Chương | Bài Theo Sách | Chủ Đề Tiếng Việt | Số từ |",
        "| :---: | :--- | :--- | :--- | :---: |",
    ]
    for idx, l in enumerate(GOI_PART1, 1):
        readme.append(
            f"| {idx:02d} | {l['chapter']} | {l['lesson']} | [**{l['title_vi']}**](./phan-1/{l['filename']}) | {len(l['words'])} |"
        )

    readme.extend([
        "",
        "---",
        "",
        "## 📗 第2部：性質別に言葉を学ぼう (Phần 2: Theo Tính Chất — 7 Chương, 16 Bài)",
        "",
        "| STT | Chương | Bài Theo Sách | Chủ Đề Tiếng Việt | Số từ |",
        "| :---: | :--- | :--- | :--- | :---: |",
    ])
    for idx, l in enumerate(GOI_PART2, 1):
        readme.append(
            f"| {idx:02d} | {l['chapter']} | {l['lesson']} | [**{l['title_vi']}**](./phan-2/{l['filename']}) | {len(l['words'])} |"
        )

    readme.extend([
        "",
        "---",
        "[⬅️ Quay lại Mục lục tổng 5 cuốn Shinkanzen](../README.md)",
        "",
    ])
    with open(os.path.join(BASE_OUT, "README.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(readme))

    print(f"✅ Built Goi N2: 21 Part-1 + 16 Part-2 = 37 lessons ({total_words} vocab items) + Flashcards + Anki TSV + README.")


if __name__ == "__main__":
    build_goi()
