# -*- coding: utf-8 -*-
"""
Builder tạo trọn bộ Shinkanzen Master Đọc Hiểu N2 & Nghe Hiểu N2:
1. shinkanzen/doc-hieu/ (新完全マスター読解 N2):
   - README.md
   - phan-1_luyen-ky-nang/: 4 bài (Đoạn văn lý thuyết + Kỹ thuật giải câu hỏi + Quảng cáo/Thông báo + Hướng dẫn/Bảng biểu)
   - phan-2_thuc-chien/: 4 bài (Nội dung Trung văn + Chủ trương Trường văn + Tổng hợp 2 văn bản + Tìm kiếm thông tin)
2. shinkanzen/nghe-hieu/ (新完全マスター聴解 N2):
   - README.md
   - 01_am-thanh-dac-trung.md .. 06_tougou-rikai.md (6 chương Ⅰ〜Ⅵ chuẩn sách, kèm track_id TTS & Hiragana đầy đủ)
"""
import os
from shinkanzen_dokkai_data import DOKKAI_PART1_2, DOKKAI_PART3
from shinkanzen_choukai_data import CHOUKAI_LESSONS

SHINKANZEN_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../shinkanzen"))
DOKKAI_DIR = os.path.join(SHINKANZEN_DIR, "doc-hieu")
CHOUKAI_DIR = os.path.join(SHINKANZEN_DIR, "nghe-hieu")


def build_dokkai():
    p1_dir = os.path.join(DOKKAI_DIR, "phan-1_luyen-ky-nang")
    p2_dir = os.path.join(DOKKAI_DIR, "phan-2_thuc-chien")
    os.makedirs(p1_dir, exist_ok=True)
    os.makedirs(p2_dir, exist_ok=True)

    # Render Part 1 & 2 skill guides (4 files)
    for idx, d in enumerate(DOKKAI_PART1_2):
        lines = [
            f"# 📖 {d['title_jp']}",
            f"## {d['title_vi']} ({d['part_label']})",
            "",
            "> 🌸 **Lời dặn của chị Yuki:**  ",
            f"> *\"{d['intro']}\"*",
            "",
            "---",
            "",
            "## 1. Hệ Thống Kỹ Năng Cốt Lõi Theo Sách Shinkanzen",
            "",
            "| Kỹ năng | Dấu hiệu / Từ khóa nhận diện | Chiến thuật áp dụng nhanh |",
            "| :--- | :--- | :--- |",
        ]
        for s_name, sig, strat in d["skills"]:
            lines.append(f"| **{s_name}** | {sig} | {strat} |")
        lines.append("")

        for p in d["passages"]:
            lines.extend([
                "---",
                "",
                f"## 📝 {p['title']}",
                "",
                "### Bài đọc tiếng Nhật (100% Furigana)",
                "",
                p["jp"],
                "",
                "<details><summary>👉 Xem bản dịch tiếng Việt & Phân tích chi tiết của chị</summary>\n",
                f"**Dịch nghĩa:**  \n{p['vi']}\n",
                "**Phân tích kỹ thuật:**",
            ])
            for a in p["analysis"]:
                lines.append(f"- {a}")
            lines.append("\n</details>\n")

            lines.append("### ✍️ Câu hỏi kiểm tra kỹ năng")
            lines.append("")
            for q_idx, (prompt, opts, ans, exp) in enumerate(p["quiz"], 1):
                assert 1 <= ans <= len(opts)
                lines.append(f"**Câu {q_idx}:** {prompt}")
                for o_idx, opt in enumerate(opts, 1):
                    lines.append(f"{o_idx}. {opt}  ")
                lines.append("<details><summary>👉 Xem đáp án & giải thích</summary>\n")
                lines.append(f"**Đáp án đúng:** {ans}  ")
                lines.append(f"**Giải thích:** {exp}")
                lines.append("</details>\n")

        nav = []
        if idx > 0:
            nav.append(f"[⬅️ Bài trước](./{DOKKAI_PART1_2[idx - 1]['filename']})")
        nav.append("[📋 Mục lục Đọc hiểu](../README.md)")
        if idx + 1 < len(DOKKAI_PART1_2):
            nav.append(f"[Bài tiếp theo ➡️](./{DOKKAI_PART1_2[idx + 1]['filename']})")
        else:
            nav.append(f"[Thực chiến: {DOKKAI_PART3[0]['mondai']} ➡️](../phan-2_thuc-chien/{DOKKAI_PART3[0]['filename']})")
        lines.append("---")
        lines.append(" | ".join(nav) + "\n")

        with open(os.path.join(p1_dir, d["filename"]), "w", encoding="utf-8") as f:
            f.write("\n".join(lines))

    # Render Part 3 real-practice Mondai (4 files)
    for idx, d in enumerate(DOKKAI_PART3):
        lines = [
            f"# 📰 {d['title_jp']}",
            f"## {d['title_vi']} ({d['mondai']})",
            "",
            "> 🌸 **Lời dặn của chị Yuki:**  ",
            f"> *\"{d['intro']}\"*",
            "",
            "## 1. Chiến Thuật Giải Đề 3 Bước",
            "",
        ]
        for st in d["strategy"]:
            lines.append(f"- {st}")
        lines.extend([
            "",
            "---",
            "",
            f"## 2. {d['text_title']}",
            "",
            d["passage_jp"],
            "",
            "<details><summary>👉 Xem bản dịch trọn văn bản của chị</summary>\n",
            d["passage_vi"],
            "\n</details>\n",
            "---",
            "",
            f"## ✍️ 3. Câu Hỏi Thực Chiến ({d['mondai']})",
            "",
        ])
        for q_idx, (prompt, opts, ans, exp) in enumerate(d["quiz"], 1):
            assert 1 <= ans <= len(opts)
            lines.append(f"### Câu {q_idx}: {prompt}")
            for o_idx, opt in enumerate(opts, 1):
                lines.append(f"{o_idx}. {opt}  ")
            lines.append("<details><summary>👉 Xem đáp án & giải thích chi tiết</summary>\n")
            lines.append(f"**Đáp án đúng:** {ans}  ")
            lines.append(f"**Giải thích:** {exp}")
            lines.append("</details>\n")

        nav = []
        if idx == 0:
            nav.append(f"[⬅️ Luyện kỹ năng: {DOKKAI_PART1_2[-1]['title_vi']}](../phan-1_luyen-ky-nang/{DOKKAI_PART1_2[-1]['filename']})")
        else:
            nav.append(f"[⬅️ Bài trước](./{DOKKAI_PART3[idx - 1]['filename']})")
        nav.append("[📋 Mục lục Đọc hiểu](../README.md)")
        if idx + 1 < len(DOKKAI_PART3):
            nav.append(f"[Bài tiếp theo ➡️](./{DOKKAI_PART3[idx + 1]['filename']})")
        lines.append("---")
        lines.append(" | ".join(nav) + "\n")

        with open(os.path.join(p2_dir, d["filename"]), "w", encoding="utf-8") as f:
            f.write("\n".join(lines))

    # Build doc-hieu/README.md
    readme = [
        "# 📖 新完全マスター読解 N2 — Mục Lục Trọn Bộ Đọc Hiểu",
        "",
        "Lộ trình chuẩn 100% theo 3 phần của **Shinkanzen Master Đọc hiểu N2** (`実力養成編 第1部・第2部・第3部`): từ cấu trúc đoạn văn, 5 kỹ thuật trả lời câu hỏi, đọc lướt thông báo/bảng biểu cho đến 4 dạng Mondai thi thật N2.",
        "",
        "---",
        "",
        "## 🛠️ 第1部 & 第2部 — Luyện Kỹ Năng Nền Tảng (4 Bài Chuyên Sâu)",
        "",
        "| STT | Nội dung theo sách | Tài liệu học |",
        "| :---: | :--- | :--- |",
    ]
    for idx, d in enumerate(DOKKAI_PART1_2, 1):
        readme.append(f"| {idx:02d} | {d['part_label']} | [**{d['title_vi']}**](./phan-1_luyen-ky-nang/{d['filename']}) |")

    readme.extend([
        "",
        "---",
        "",
        "## 🎯 第3部 — 実戦問題 (Thực Chiến 4 Dạng Đề JLPT N2)",
        "",
        "| STT | Dạng Mondai | Chủ đề thực hành |",
        "| :---: | :--- | :--- |",
    ])
    for idx, d in enumerate(DOKKAI_PART3, 1):
        readme.append(f"| {idx:02d} | `{d['mondai']}` | [**{d['title_vi']}**](./phan-2_thuc-chien/{d['filename']}) |")

    readme.extend(["", "---", "[⬅️ Quay lại Mục lục tổng 5 cuốn Shinkanzen](../README.md)", ""])
    with open(os.path.join(DOKKAI_DIR, "README.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(readme))

    print(f"✅ Built Dokkai N2: {len(DOKKAI_PART1_2)} skill guides + {len(DOKKAI_PART3)} practice units = 8 files + README.")


def build_choukai():
    os.makedirs(CHOUKAI_DIR, exist_ok=True)
    total_tracks = 0

    for idx, c in enumerate(CHOUKAI_LESSONS):
        lines = [
            f"# 🎧 {c['chapter']} — {c['title_jp']}",
            f"## {c['title_vi']}",
            "",
            "> 🌸 **Lời dặn của chị Yuki:**  ",
            f"> *\"{c['intro']}\"*",
            "",
            "---",
            "",
            "## 1. Quy Luật & Cạm Bẫy Cốt Lõi Theo Sách Shinkanzen",
            "",
            "| Hiện tượng / Bẫy thi | Dấu hiệu nhận biết | Cách xử lý chuẩn N2 |",
            "| :--- | :--- | :--- |",
        ]
        for a, b, tip in c["theory_table"]:
            lines.append(f"| **{a}** | {b} | {tip} |")

        lines.extend(["", "## 💡 2. Mẹo Luyện Tai & Ghi Chú Thực Chiến", ""])
        for s in c["strategies"]:
            lines.append(f"- {s}")

        lines.extend(["", "---", "", f"## 🎙️ 3. Script Thực Hành Chuẩn TTS & Luyện Nghe ({len(c['tracks'])} Track)", ""])
        for t_idx, tr in enumerate(c["tracks"], 1):
            total_tracks += 1
            lines.extend([
                f"### Track {t_idx} (`track_id: {tr['track_id']}` | Speakers: {tr['speakers']})",
                f"*{tr['context']}*",
                "",
                "**Kịch bản (100% Furigana — Khuyến khích dùng để tự đọc/Shadowing hoặc chạy TTS đa giọng):**",
                "",
            ])
            for spk, line_txt in tr["script_lines"]:
                lines.append(f"- **{spk}:** {line_txt}")
            lines.extend([
                "",
                f"**Câu hỏi:** {tr['question']}",
                "",
            ])
            for o_idx, opt in enumerate(tr["options"], 1):
                lines.append(f"{o_idx}. {opt}  ")
            assert 1 <= tr["ans"] <= len(tr["options"])
            lines.append("<details><summary>👉 Xem bản dịch tiếng Việt & Đáp án giải thích</summary>\n")
            lines.append(f"**Dịch hội thoại:**  \n{tr['vi'].replace(chr(10), '  ' + chr(10))}\n")
            lines.append(f"**Đáp án đúng:** {tr['ans']} (`{tr['options'][tr['ans'] - 1]}`)  ")
            lines.append(f"**Phân tích bẫy:** {tr['exp']}")
            lines.append("</details>\n")

        nav = []
        if idx > 0:
            nav.append(f"[⬅️ {CHOUKAI_LESSONS[idx - 1]['chapter']}](./{CHOUKAI_LESSONS[idx - 1]['filename']})")
        nav.append("[📋 Mục lục Nghe hiểu](./README.md)")
        if idx + 1 < len(CHOUKAI_LESSONS):
            nav.append(f"[{CHOUKAI_LESSONS[idx + 1]['chapter']} ➡️](./{CHOUKAI_LESSONS[idx + 1]['filename']})")
        lines.append("---")
        lines.append(" | ".join(nav) + "\n")

        with open(os.path.join(CHOUKAI_DIR, c["filename"]), "w", encoding="utf-8") as f:
            f.write("\n".join(lines))

    # Build nghe-hieu/README.md
    readme = [
        "# 🎧 新完全マスター聴解 N2 — Mục Lục Trọn Bộ Nghe Hiểu (Chương I–VI)",
        "",
        f"Sắp xếp chuẩn 100% theo mục lục **実力養成編 Ⅰ〜Ⅵ** của **Shinkanzen Master Nghe hiểu N2**, tích hợp **{total_tracks} Track kịch bản chuẩn TTS** có gắn sẵn `track_id`, phân vai `speakers` và đầy đủ Furigana cho Shadowing.",
        "",
        "---",
        "",
        "| Chương | Tên Theo Sách (日本語) | Kỹ Năng Trọng Tâm | Số Track Mẫu |",
        "| :---: | :--- | :--- | :---: |",
    ]
    for c in CHOUKAI_LESSONS:
        readme.append(
            f"| **{c['chapter'].split()[-1]}** | {c['title_jp']} | [**{c['title_vi']}**](./{c['filename']}) | {len(c['tracks'])} |"
        )

    readme.extend(["", "---", "[⬅️ Quay lại Mục lục tổng 5 cuốn Shinkanzen](../README.md)", ""])
    with open(os.path.join(CHOUKAI_DIR, "README.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(readme))

    print(f"✅ Built Choukai N2: {len(CHOUKAI_LESSONS)} chapters ({total_tracks} TTS-ready tracks) + README.")


def build_dokkai_choukai():
    build_dokkai()
    build_choukai()


if __name__ == "__main__":
    build_dokkai_choukai()
