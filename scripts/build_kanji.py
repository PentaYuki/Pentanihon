# -*- coding: utf-8 -*-
"""
Builder tạo trọn bộ Shinkanzen Master Chữ Hán N2 (新完全マスター漢字 N2):
- Step 1: 第1回 ～ 第14回 (280 chữ) -> shinkanzen/kanji/step-1/bai-01..14.md
- Step 2: 第15回 ～ 第30回 (320 chữ) -> shinkanzen/kanji/step-2/bai-15..30.md
- Step 3: 第31回 ～ 第53回 (446 chữ) -> shinkanzen/kanji/step-3/bai-31..53.md
- Tổng cộng: Đúng chuẩn 1.046 chữ Hán (0 chữ trùng lặp)
- Cột luyện Challenge & Phụ lục 別冊1: cot-luyen_1-2.md, cot-luyen_3-4.md, phu-luc_dac-biet.md
- Mục lục shinkanzen/kanji/README.md
"""
import os
from shinkanzen_kanji_data_s1 import KANJI_STEP1
from shinkanzen_kanji_data_s2 import KANJI_STEP2
from shinkanzen_kanji_data_s3a import KANJI_STEP3_A
from shinkanzen_kanji_data_s3b import KANJI_STEP3_B
from shinkanzen_kanji_appendix import CHALLENGE_1_2, CHALLENGE_3_4, BESATSU_APPENDIX

BASE_OUT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../shinkanzen/kanji"))


def render_kanji_lesson(lesson, rel_path, prev_rel, next_rel):
    num = lesson["num"]
    lines = [
        f"# 🈷️ {lesson['title_jp']} — {lesson['title_vi']}",
        f"## Giáo trình: 新完全マスター漢字 N2 — {lesson['step']}",
        "",
        "> 🌸 **Lời dặn của chị Yuki:**  ",
        f"> *\"{lesson['focus']}\"*",
        "",
        "---",
        "",
        f"## 1. Bảng {len(lesson['kanji_list'])} Chữ Hán Trọng Tâm (Bài {num:02d})",
        "",
        "| STT | Kanji | Hán Việt | Âm On (カタカナ) | Âm Kun (ひらがな) | Nghĩa cốt lõi | Từ ghép tiêu biểu (Đề thi N2) |",
        "| :---: | :---: | :--- | :--- | :--- | :--- | :--- |",
    ]
    for idx, (ch, hv, on_y, kun_y, mean, comps) in enumerate(lesson["kanji_list"], 1):
        lines.append(f"| {idx} | **<span style='font-size:1.3em'>{ch}</span>** | {hv} | `{on_y}` | `{kun_y}` | {mean} | {comps} |")

    lines.extend([
        "",
        "---",
        "",
        f"## ✍️ 2. Luyện Tập Đọc Kanji Bài {num:02d} (Mondai 1–2)",
        "",
    ])
    for q_idx, (prompt, opts, ans, exp) in enumerate(lesson["quiz"], 1):
        assert 1 <= ans <= len(opts), f"Invalid quiz index in Kanji lesson {num} Q{q_idx}"
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
        nav.append(f"[⬅️ Bài {num - 1:02d}]({prev_rel})")
    nav.append("[📋 Mục lục Chữ Hán](../README.md)")
    if num == 30:
        nav.append("[🏋️ Tổng hợp & Challenge 1-2](../cot-luyen_1-2.md)")
    elif num == 53:
        nav.append("[🏋️ Tổng hợp & Challenge 3-4](../cot-luyen_3-4.md)")
        nav.append("[📕 Phụ lục 別冊1](../phu-luc_dac-biet.md)")
    if next_rel:
        nav.append(f"[Bài {num + 1:02d} ➡️]({next_rel})")
    lines.append("---")
    lines.append(" | ".join(nav))
    lines.append("")
    return "\n".join(lines)


def render_challenge_1_2():
    d = CHALLENGE_1_2
    lines = [
        f"# {d['title']}",
        f"## {d['subtitle']}",
        "",
        "> 🌸 **Lời dặn của chị Yuki:**  ",
        f"> *\"{d['intro']}\"*",
        "",
        "---",
        "",
        "## 1. Challenge 1 — 接辞① (Tiền Tố & Hậu Tố Hay Ra Mondai 3)",
        "",
        "| Tiền tố / Hậu tố | Ý nghĩa | Từ ghép mẫu N2 |",
        "| :--- | :--- | :--- |",
    ]
    for a, m, ex in d["affixes"]:
        lines.append(f"| **{a}** | {m} | {ex} |")

    lines.extend([
        "",
        "## 2. Challenge 2 — 読み方と意味 (Khác Âm Đọc -> Khác Nghĩa)",
        "",
        "| Từ Kanji | 2 Cách Đọc | Phân Biệt Ngữ Cảnh |",
        "| :---: | :--- | :--- |",
    ])
    for w, r, note in d["reading_meaning"]:
        lines.append(f"| **{w}** | {r} | {note} |")

    lines.extend(["", "---", "", "## ✍️ 3. 総合問題 1 (Bài Tập Kiểm Tra Tổng Hợp Step 1–2)", ""])
    for q_idx, (prompt, opts, ans, exp) in enumerate(d["quiz"], 1):
        lines.append(f"### Câu {q_idx}: {prompt}")
        for o_idx, opt in enumerate(opts, 1):
            lines.append(f"{o_idx}. {opt}  ")
        lines.append("<details><summary>👉 Xem đáp án & giải thích</summary>\n")
        lines.append(f"**Đáp án đúng:** {ans} (`{opts[ans - 1]}`) — {exp}")
        lines.append("</details>\n")

    lines.append("---")
    lines.append("[⬅️ Step 2 Bài 30](./step-2/bai-30.md) | [📋 Mục lục Chữ Hán](./README.md) | [Step 3 Bài 31 ➡️](./step-3/bai-31.md)\n")
    return "\n".join(lines)


def render_challenge_3_4():
    d = CHALLENGE_3_4
    lines = [
        f"# {d['title']}",
        f"## {d['subtitle']}",
        "",
        "> 🌸 **Lời dặn của chị Yuki:**  ",
        f"> *\"{d['intro']}\"*",
        "",
        "---",
        "",
        "## 1. 言葉の構成 (5 Kiểu Cấu Tạo Từ Ghép Hán-Nhật)",
        "",
        "| Dạng cấu tạo | Ví dụ chuẩn N2 | Cách đoán nghĩa nhanh |",
        "| :--- | :--- | :--- |",
    ]
    for t, ex, tip in d["word_structures"]:
        lines.append(f"| **{t}** | {ex} | {tip} |")

    lines.extend([
        "",
        "## 2. 音の変化 (Quy Luật Biến Âm & Xúc Âm Cần Thuộc)",
        "",
        "| Quy tắc biến âm | Ví dụ thực chiến | Giải thích |",
        "| :--- | :--- | :--- |",
    ])
    for r, ex, exp in d["sound_changes"]:
        lines.append(f"| **{r}** | {ex} | {exp} |")

    lines.extend([
        "",
        "## 3. 読解 (Luyện Đọc Đoạn Văn Kanji N2)",
        "",
        "> " + d["reading_passage"]["jp"],
        "",
        f"*Dịch nghĩa:* {d['reading_passage']['vi']}",
        "",
        "---",
        "",
        "## ✍️ 4. 総合問題 2 (Bài Tập Tổng Hợp Step 3)",
        "",
    ])
    for q_idx, (prompt, opts, ans, exp) in enumerate(d["quiz"], 1):
        lines.append(f"### Câu {q_idx}: {prompt}")
        for o_idx, opt in enumerate(opts, 1):
            lines.append(f"{o_idx}. {opt}  ")
        lines.append("<details><summary>👉 Xem đáp án & giải thích</summary>\n")
        lines.append(f"**Đáp án đúng:** {ans} (`{opts[ans - 1]}`) — {exp}")
        lines.append("</details>\n")

    lines.append("---")
    lines.append("[⬅️ Step 3 Bài 53](./step-3/bai-53.md) | [📋 Mục lục Chữ Hán](./README.md) | [📕 Phụ lục 別冊1 ➡️](./phu-luc_dac-biet.md)\n")
    return "\n".join(lines)


def render_besatsu():
    d = BESATSU_APPENDIX
    lines = [
        f"# {d['title']}",
        f"## {d['subtitle']}",
        "",
        "> 🌸 **Lời dặn của chị Yuki:**  ",
        f"> *\"{d['intro']}\"*",
        "",
        "---",
        "",
        "## 1. 特別な読み方をする漢字の言葉 (Từ Đọc Đặc Biệt - Jukujikun & Ateji)",
        "",
        "| Từ Kanji | Cách đọc đặc biệt | Ghi chú |",
        "| :--- | :--- | :--- |",
    ]
    for w, r, n in d["special_readings"]:
        lines.append(f"| **{w}** | `{r}` | {n} |")

    lines.extend([
        "",
        "## 2. 訓読みが二つ以上ある漢字 (Chữ Có Nhiều Âm Kun)",
        "",
        "| Kanji | Các âm Kun cần nhớ | Ví dụ phân biệt |",
        "| :---: | :--- | :--- |",
    ])
    for ch, kuns, ex in d["multi_kun"]:
        lines.append(f"| **<span style='font-size:1.3em'>{ch}</span>** | `{kuns}` | {ex} |")

    lines.extend([
        "",
        "## 3. 音読みが二つ以上ある漢字 (Chữ Có Nhiều Âm On)",
        "",
        "| Kanji | Các âm On hay thi | Ví dụ đối chiếu |",
        "| :---: | :--- | :--- |",
    ])
    for ch, ons, ex in d["multi_on"]:
        lines.append(f"| **<span style='font-size:1.3em'>{ch}</span>** | `{ons}` | {ex} |")

    lines.append("")
    lines.append("---")
    lines.append("[⬅️ Tổng hợp Challenge 3-4](./cot-luyen_3-4.md) | [📋 Mục lục Chữ Hán](./README.md)\n")
    return "\n".join(lines)


def build_kanji():
    all_lessons = (
        [("step-1", l) for l in KANJI_STEP1]
        + [("step-2", l) for l in KANJI_STEP2]
        + [("step-3", l) for l in KANJI_STEP3_A]
        + [("step-3", l) for l in KANJI_STEP3_B]
    )
    assert len(all_lessons) == 53, f"Expected 53 lessons, got {len(all_lessons)}"

    seen_kanji = set()
    for step_dir, l in all_lessons:
        for tup in l["kanji_list"]:
            ch = tup[0]
            assert len(ch) == 1, f"Invalid kanji char: {ch} in lesson {l['num']}"
            assert ch not in seen_kanji, f"Duplicate kanji {ch} in lesson {l['num']}"
            seen_kanji.add(ch)

    assert len(seen_kanji) == 1046, f"Expected exactly 1046 unique kanji, got {len(seen_kanji)}"

    for d in ("step-1", "step-2", "step-3"):
        os.makedirs(os.path.join(BASE_OUT, d), exist_ok=True)

    for idx, (step_dir, l) in enumerate(all_lessons):
        rel = f"{step_dir}/bai-{l['num']:02d}.md"
        prev_rel = f"../{all_lessons[idx - 1][0]}/bai-{all_lessons[idx - 1][1]['num']:02d}.md" if idx > 0 else None
        next_rel = f"../{all_lessons[idx + 1][0]}/bai-{all_lessons[idx + 1][1]['num']:02d}.md" if idx + 1 < len(all_lessons) else None
        out_path = os.path.join(BASE_OUT, rel)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(render_kanji_lesson(l, rel, prev_rel, next_rel))

    with open(os.path.join(BASE_OUT, "cot-luyen_1-2.md"), "w", encoding="utf-8") as f:
        f.write(render_challenge_1_2())
    with open(os.path.join(BASE_OUT, "cot-luyen_3-4.md"), "w", encoding="utf-8") as f:
        f.write(render_challenge_3_4())
    with open(os.path.join(BASE_OUT, "phu-luc_dac-biet.md"), "w", encoding="utf-8") as f:
        f.write(render_besatsu())

    readme = [
        "# 🈷️ 新完全マスター漢字 N2 — Mục Lục Trọn Bộ 1.046 Chữ Hán (53 Bài)",
        "",
        "Sắp xếp theo đúng 3 chặng của giáo trình **Shinkanzen Master Chữ Hán N2**: **Step 1 (第1〜14回)**, **Step 2 (第15〜30回)**, **Step 3 (第31〜53回)** + **Cột Challenge & 総合問題** + **別冊 1** — tổng cộng chính xác **1.046 chữ Hán không trùng lặp**.",
        "",
        "---",
        "",
    ]
    step_groups = [
        ("📘 Step 1（第1回 〜 第14回）— 280 Chữ Nền Tảng", [x for x in all_lessons if x[0] == "step-1"]),
        ("📗 Step 2（第15回 〜 第30回）— 320 Chữ Trọng Tâm", [x for x in all_lessons if x[0] == "step-2"]),
        ("📙 Step 3（第31回 〜 第53回）— 446 Chữ Nâng Cao & Tổng Hoàn Thành 1.046 Chữ", [x for x in all_lessons if x[0] == "step-3"]),
    ]
    for title, items in step_groups:
        readme.append(f"## {title}")
        readme.append("")
        readme.append("| Bài | Nội dung & Chữ Hán tiêu biểu | Số chữ |")
        readme.append("| :---: | :--- | :---: |")
        for step_dir, l in items:
            sample = "・".join(k[0] for k in l["kanji_list"][:8]) + "…"
            readme.append(
                f"| **{l['num']:02d}** | [**{l['title_jp']}** — {l['title_vi']}](./{step_dir}/bai-{l['num']:02d}.md) (`{sample}`) | {len(l['kanji_list'])} |"
            )
        readme.append("")

    readme.extend([
        "---",
        "",
        "## 🏋️ Tổng Hợp, Cột Challenge & Phụ Lục 別冊 1",
        "- [**Tổng hợp Step 2 & Challenge ①② (接辞①・読み方と意味)**](./cot-luyen_1-2.md)",
        "- [**Tổng hợp Step 3 & Challenge ②③④ (言葉の構成・音の変化・読解)**](./cot-luyen_3-4.md)",
        "- [**Phụ lục 別冊 1: 特別な読み方・訓読み複数・音読み複数**](./phu-luc_dac-biet.md)",
        "",
        "[⬅️ Quay lại Mục lục tổng 5 cuốn Shinkanzen](../README.md)",
        "",
    ])
    with open(os.path.join(BASE_OUT, "README.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(readme))

    print(f"✅ Built Kanji N2: 53 lessons totaling {len(seen_kanji)} unique Kanji + 2 Challenge guides + Besatsu Appendix + README.")


if __name__ == "__main__":
    build_kanji()
