# -*- coding: utf-8 -*-
"""
Builder tạo trọn bộ Shinkanzen Master Ngữ Pháp N2 (新完全マスター文法 N2):
- Phần 1 (文の文法1): 26 bài (bai-01.md .. bai-26.md)
- Phần 2 (文の文法2 - 組み立て ★): 3 bài (bai-01.md .. bai-03.md)
- Phần 3 (文章の文法): 12 bài (bai-01.md .. bai-12.md)
- Phụ lục Kính ngữ N2 (phu-luc_kinh-ngu.md)
- Mục lục shinkanzen/ngu-phap/README.md
"""
import os
from shinkanzen_bunpou_data_p1a import BUNPOU_PART1_A
from shinkanzen_bunpou_data_p1b import BUNPOU_PART1_B
from shinkanzen_bunpou_data_p23 import BUNPOU_PART2, BUNPOU_PART3, KEIGO_APPENDIX

BASE_OUT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../shinkanzen/ngu-phap"))


def render_part1_lesson(num, data):
    lines = [
        f"# ⛩️ Bài {num:02d}: {data['title_jp']} — {data['title_vi']}",
        f"## Giáo trình: 新完全マスター文法 N2 — 第1部（{data['section']}）第{num}課",
        "",
        "> 🌸 **Lời dặn của chị Yuki:**  ",
        f"> *\"{data['intro']}\"*",
        "",
        "---",
        "",
        "## 1. Các Mẫu Ngữ Pháp Trọng Tâm",
        "",
    ]

    for p in data["patterns"]:
        lines.append(f"### {p['name']}")
        lines.append(f"- **Ý nghĩa:** {p['meaning']}")
        lines.append(f"- **Cấu trúc liên kết (接続):** `{p['connection']}`")
        lines.append("- **Ví dụ mẫu (例文 - れいぶん):**")
        for idx, (jp, vi) in enumerate(p["examples"], 1):
            lines.append(f"  {idx}. {jp}  ")
            lines.append(f"     *({vi})*")
        lines.append(f"- 💡 **Ghi chú của chị:** {p['note']}")
        lines.append("")
        lines.append("---")
        lines.append("")

    if data.get("comparison"):
        lines.append("## 2. Bảng Phân Biệt Các Mẫu Dễ Nhầm")
        lines.append("")
        lines.append("| Mẫu ngữ pháp | Đặc trưng cốt lõi | Điểm cần lưu ý (Bẫy đề thi) |")
        lines.append("| :--- | :--- | :--- |")
        for row in data["comparison"]:
            lines.append(f"| **{row[0]}** | {row[1]} | {row[2]} |")
        lines.append("")
        lines.append("---")
        lines.append("")

    lines.append("## 3. Cảnh Báo Cạm Bẫy Thi Thật (Sister's Warning)")
    lines.append("")
    for trap in data["pitfalls"]:
        lines.append(f"- {trap}")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append(f"## 4. ✍️ Luyện Tập Thực Chiến Bài {num:02d} (Mondai 7)")
    lines.append("")

    for q_idx, (prompt, opts, ans, exp) in enumerate(data["quiz"], 1):
        lines.append(f"### Câu {q_idx}: {prompt}")
        for o_idx, opt in enumerate(opts, 1):
            lines.append(f"{o_idx}. {opt}  ")
        lines.append(f"<details><summary>👉 Xem đáp án & giải thích của chị</summary>\n")
        lines.append(f"**Đáp án đúng:** {ans} (`{opts[ans - 1]}`)  ")
        lines.append(f"**Giải thích:** {exp}")
        lines.append("</details>")
        lines.append("")

    # Navigation links
    nav = []
    if num > 1:
        nav.append(f"[⬅️ Bài {num-1:02d}](./bai-{num-1:02d}.md)")
    nav.append("[📋 Mục lục Ngữ pháp](../README.md)")
    if num < 26:
        nav.append(f"[Bài {num+1:02d} ➡️](./bai-{num+1:02d}.md)")
    else:
        nav.append("[Phần 2: Văn pháp ★ ➡️](../phan-2/bai-01.md)")
    lines.append("---")
    lines.append(" | ".join(nav))
    lines.append("")
    return "\n".join(lines)


def render_part2_lesson(num, data):
    lines = [
        f"# ⭐ Phần 2 — Bài {num:02d}: {data['title_jp']} ({data['title_vi']})",
        f"## Giáo trình: 新完全マスター文法 N2 — 第2部 文の文法2（文の組み立て）",
        "",
        "> 🌸 **Lời dặn của chị Yuki:**  ",
        f"> *\"{data['intro']}\"*",
        "",
        "---",
        "",
        "## 1. Chiến Thuật Lắp Ghép Câu Dấu Sao (★)",
        "",
    ]
    for title, rule, tip in data["strategies"]:
        lines.append(f"### 💡 {title}")
        lines.append(f"- **Quy luật:** {rule}")
        lines.append(f"- **Mẹo xử lý nhanh:** {tip}")
        lines.append("")

    lines.append("---")
    lines.append("")
    lines.append("## 2. Bài Tập Dấu Sao (★の文法問題)")
    lines.append("")
    for idx, (prompt, opts, order, star_num, full_sentence, exp) in enumerate(data["star_exercises"], 1):
        lines.append(f"### Câu {idx}:")
        lines.append(f"{prompt}  ")
        for o_i, opt in enumerate(opts, 1):
            lines.append(f"{o_i}. {opt}  ")
        lines.append(f"<details><summary>👉 Xem thứ tự ghép & vị trí ★</summary>\n")
        lines.append(f"**Thứ tự đúng:** {' - '.join(str(x) for x in order)} (**★ là số {star_num}**: `{opts[star_num - 1]}`)  ")
        lines.append(f"**Câu hoàn chỉnh:** {full_sentence}  ")
        lines.append(f"**Phân tích:** {exp}")
        lines.append("</details>")
        lines.append("")

    nav = []
    if num > 1:
        nav.append(f"[⬅️ Phần 2 Bài {num-1:02d}](./bai-{num-1:02d}.md)")
    else:
        nav.append("[⬅️ Phần 1 Bài 26](../phan-1/bai-26.md)")
    nav.append("[📋 Mục lục Ngữ pháp](../README.md)")
    if num < 3:
        nav.append(f"[Phần 2 Bài {num+1:02d} ➡️](./bai-{num+1:02d}.md)")
    else:
        nav.append("[Phần 3: Ngữ pháp đoạn văn ➡️](../phan-3/bai-01.md)")
    lines.append("---")
    lines.append(" | ".join(nav))
    lines.append("")
    return "\n".join(lines)


def render_part3_lesson(num, data):
    lines = [
        f"# 📝 Phần 3 — Bài {num:02d}: {data['title_jp']} ({data['title_vi']})",
        f"## Giáo trình: 新完全マスター文法 N2 — 第3部 文章の文法（第{num}課）",
        "",
        "> 🌸 **Lời dặn của chị Yuki:**  ",
        f"> *\"{data['summary']}\"*",
        "",
        "---",
        "",
        "## 1. Nguyên Tắc Cốt Lõi Khi Làm Mondai 9",
        "",
    ]
    for pt in data["points"]:
        lines.append(f"- {pt}")

    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 2. Thực Hành Ngữ Pháp Đoạn Văn (文章の文法)")
    lines.append("")
    lines.append(f"> {data['passage_jp']}")
    lines.append("")
    lines.append(f"**Câu hỏi:** {data['question']}")
    for o_i, opt in enumerate(data["options"], 1):
        lines.append(f"{o_i}. {opt}  ")
    lines.append("")
    lines.append("<details><summary>👉 Xem đáp án & phân tích mạch văn</summary>\n")
    lines.append(f"**Đáp án đúng:** {data['answer']} (`{data['options'][data['answer'] - 1]}`)  ")
    lines.append(f"**Giải thích:** {data['explanation']}")
    lines.append("</details>")
    lines.append("")

    nav = []
    if num > 1:
        nav.append(f"[⬅️ Phần 3 Bài {num-1:02d}](./bai-{num-1:02d}.md)")
    else:
        nav.append("[⬅️ Phần 2 Bài 03](../phan-2/bai-03.md)")
    nav.append("[📋 Mục lục Ngữ pháp](../README.md)")
    if num < 12:
        nav.append(f"[Phần 3 Bài {num+1:02d} ➡️](./bai-{num+1:02d}.md)")
    else:
        nav.append("[Phụ lục Kính ngữ ➡️](../phu-luc_kinh-ngu.md)")
    lines.append("---")
    lines.append(" | ".join(nav))
    lines.append("")
    return "\n".join(lines)


def render_keigo():
    lines = [
        f"# 🙇 {KEIGO_APPENDIX['title']}",
        "",
        "> 🌸 **Lời dặn của chị Yuki:**  ",
        f"> *\"{KEIGO_APPENDIX['intro']}\"*",
        "",
        "---",
        "",
        "## 1. Bảng Đối Chiếu Động Từ Kính Ngữ Cốt Lõi",
        "",
        "| Động từ thường | Tôn kính ngữ (尊敬語 - Người trên) | Khiêm nhường ngữ (謙譲語 - Bản thân/Phe mình) | Nghĩa |",
        "| :--- | :--- | :--- | :--- |",
    ]
    for base, sonkei, kenjou, vi in KEIGO_APPENDIX["table"]:
        lines.append(f"| **{base}** | {sonkei} | {kenjou} | {vi} |")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 2. 3 Bẫy Kính Ngữ Kinh Điển Trong Kỳ Thi")
    lines.append("")
    for t in KEIGO_APPENDIX["traps"]:
        lines.append(f"- {t}")
    lines.append("")
    lines.append("---")
    lines.append("[⬅️ Phần 3 Bài 12](./phan-3/bai-12.md) | [📋 Mục lục Ngữ pháp](./README.md)")
    lines.append("")
    return "\n".join(lines)


def build_bunpou():
    p1 = {**BUNPOU_PART1_A, **BUNPOU_PART1_B}
    assert len(p1) == 26, f"Expected 26 Part 1 lessons, got {len(p1)}"

    p1_dir = os.path.join(BASE_OUT, "phan-1")
    p2_dir = os.path.join(BASE_OUT, "phan-2")
    p3_dir = os.path.join(BASE_OUT, "phan-3")
    for d in (p1_dir, p2_dir, p3_dir):
        os.makedirs(d, exist_ok=True)

    for num, data in sorted(p1.items()):
        with open(os.path.join(p1_dir, f"bai-{num:02d}.md"), "w", encoding="utf-8") as f:
            f.write(render_part1_lesson(num, data))

    for num, data in sorted(BUNPOU_PART2.items()):
        with open(os.path.join(p2_dir, f"bai-{num:02d}.md"), "w", encoding="utf-8") as f:
            f.write(render_part2_lesson(num, data))

    for num, data in sorted(BUNPOU_PART3.items()):
        with open(os.path.join(p3_dir, f"bai-{num:02d}.md"), "w", encoding="utf-8") as f:
            f.write(render_part3_lesson(num, data))

    with open(os.path.join(BASE_OUT, "phu-luc_kinh-ngu.md"), "w", encoding="utf-8") as f:
        f.write(render_keigo())

    # Build ngu-phap/README.md
    readme = [
        "# ⛩️ 新完全マスター文法 N2 — Mục Lục Trọn Bộ Ngữ Pháp",
        "",
        "Sắp xếp chuẩn 100% theo giáo trình **Shinkanzen Master Ngữ Pháp N2** (スリーエーネットワーク): **Phần 1 (26 bài)** + **Phần 2 (3 bài dấu sao ★)** + **Phần 3 (12 bài ngữ pháp đoạn văn)** + **Phụ lục Kính ngữ**.",
        "",
        "---",
        "",
        "## 📘 第1部 文の文法 1 (26 Bài Theo Nhóm Ý Nghĩa)",
        "",
        "| Bài | Tên bài theo sách (日本語) | Trọng tâm ngữ pháp |",
        "| :---: | :--- | :--- |",
    ]
    for num in range(1, 27):
        d = p1[num]
        pts = ", ".join(p["name"].split(". ", 1)[1].split(" / ")[0] for p in d["patterns"])
        readme.append(f"| **{num:02d}** | [**第{num}課: {d['title_jp']}** *({d['title_vi']})*](./phan-1/bai-{num:02d}.md) | `{pts}` |")

    readme.extend([
        "",
        "---",
        "",
        "## ⭐ 第2部 文の文法 2 (Lắp Ghép Câu Dấu Sao ★ - 3 Bài)",
        "",
        "| Bài | Chủ đề | Chi tiết |",
        "| :---: | :--- | :--- |",
    ])
    for num, d in sorted(BUNPOU_PART2.items()):
        readme.append(f"| **{num:02d}** | [**{d['title_jp']}** *({d['title_vi']})*](./phan-2/bai-{num:02d}.md) | Chiến thuật + Bài tập ★ |")

    readme.extend([
        "",
        "---",
        "",
        "## 📝 第3部 文章の文法 (Ngữ Pháp Đoạn Văn - 12 Bài)",
        "",
        "| Bài | Chủ đề | Chi tiết |",
        "| :---: | :--- | :--- |",
    ])
    for num, d in sorted(BUNPOU_PART3.items()):
        readme.append(f"| **{num:02d}** | [**{d['title_jp']}** *({d['title_vi']})*](./phan-3/bai-{num:02d}.md) | Phân tích mạch văn + Mondai 9 |")

    readme.extend([
        "",
        "---",
        "",
        "## 🙇 Phụ Lục Bổ Trợ",
        "- [**Bảng Tổng Hợp Kính Ngữ N2 (敬語：尊敬語・謙譲語・丁寧語)**](./phu-luc_kinh-ngu.md)",
        "",
        "[⬅️ Quay lại Mục lục tổng 5 cuốn Shinkanzen](../README.md)",
        "",
    ])

    with open(os.path.join(BASE_OUT, "README.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(readme))

    print(f"✅ Built Bunpou N2: 26 Part-1 + 3 Part-2 + 12 Part-3 + Keigo Appendix = 42 lesson files + README.")


if __name__ == "__main__":
    build_bunpou()
