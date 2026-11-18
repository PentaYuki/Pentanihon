# -*- coding: utf-8 -*-
"""
Orchestrator tổng hợp xây dựng trọn bộ 5 cuốn Shinkanzen Master N2 (新完全マスター N2):
1. Ngữ pháp (文法): 26 + 3 + 12 + Phụ lục Kính ngữ = 42 file
2. Từ vựng (語彙): 21 + 16 + Flashcards (Web / Print A4 / Anki TSV) = 37 bài
3. Chữ Hán (漢字): 53 bài (đúng chuẩn 1.046 chữ) + 2 Cột Challenge + Phụ lục 別冊1
4. Đọc hiểu (読解): 4 bài kỹ năng + 4 bài thực chiến = 8 file
5. Nghe hiểu (聴解): 6 chương (kịch bản + Hiragana + Track TTS)
Và tạo mục lục tổng shinkanzen/README.md
"""
import json
import os
from build_bunpou import build_bunpou
from build_goi import build_goi
from build_kanji import build_kanji
from build_novel import build_novel
from build_exam import build_exam

from shinkanzen_bunpou_data_p1a import BUNPOU_PART1_A
from shinkanzen_bunpou_data_p1b import BUNPOU_PART1_B
from shinkanzen_bunpou_data_p23 import BUNPOU_PART2, BUNPOU_PART3
from shinkanzen_goi_data_p1 import GOI_PART1
from shinkanzen_goi_data_p2 import GOI_PART2
from shinkanzen_kanji_data_s1 import KANJI_STEP1
from shinkanzen_kanji_data_s2 import KANJI_STEP2
from shinkanzen_kanji_data_s3a import KANJI_STEP3_A
from shinkanzen_kanji_data_s3b import KANJI_STEP3_B
from novel_data_romcom import ROMCOM_NOVEL
from novel_data_yandere import YANDERE_NOVEL
from novel_data_isekai import ISEKAI_NOVEL

SHINKANZEN_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../shinkanzen"))


def write_shinkanzen_master_readme():
    content = """# 📚 Hệ Thống Học Tập Shinkanzen N2 × 3 Bộ Tiểu Thuyết & Đề Thi Chuẩn JLPT

> 🌸 **Lời nhắn nhẹ nhàng từ chị Yuki:**  
> *"Hệ thống mới của tụi mình đã loại bỏ hoàn toàn các bài Đọc hiểu & Nghe hiểu cũ, thay bằng **3 Bộ Tiểu Thuyết Romcom — Yandere — Isekai (37 chương)** chứa trọn vẹn **100% 37 bài / 780 từ vựng Shinkanzen Từ Vựng N2**, kèm **Trung tâm Đề Thi Chuẩn JLPT N2 (222 câu tự chấm & giải thích Đúng/Sai)**! Học mà cuốn như đọc light novel luôn đó em~ 💕"*

---

## 🗺️ Bản Đồ Hệ Thống N2 Mới

| Phân hệ (日本語) | Thư mục & Mục lục | Quy mô nội dung | Công cụ nổi bật đi kèm |
| :--- | :--- | :--- | :--- |
| **1. 文法 (Ngữ pháp)** | [**`ngu-phap/README.md`**](./ngu-phap/README.md) | **Phần 1** (`26 bài`) + **Phần 2 ★** (`3 bài`) + **Phần 3** (`12 bài`) + **Kính ngữ** | Bảng đối chiếu mẫu dễ nhầm, bẫy thi & quiz Mondai 7–9 |
| **2. 語彙 (Từ vựng)** | [**`tu-vung/README.md`**](./tu-vung/README.md) | **Phần 1:** `9 chương, 21 bài` + **Phần 2:** `7 chương, 16 bài` (`37 bài`, `780 từ`) | [**🎴 Flashcards 780 Từ**](./tu-vung/flashcards.html) + Link thẳng tới từng chương Tiểu thuyết |
| **3. 漢字 (Chữ Hán)** | [**`kanji/README.md`**](./kanji/README.md) | **Step 1** (`14 bài`) + **Step 2** (`16 bài`) + **Step 3** (`23 bài`) = **53 bài (`1.046 chữ`)** | **2 Cột Challenge & Phụ lục 別冊1** (Âm đọc đặc biệt) |
| **4. 📓 3 Bộ Tiểu Thuyết** | [**`../novel/README.md`**](../novel/README.md) | **Romcom** (`13 chương`) + **Yandere** (`12 chương`) + **Isekai** (`12 chương`) | [**✨ Đọc Tương Tác**](../novel/index.html) • Dịch trọn chương • Bảng nghĩa bên dưới • 185 Câu Quiz |
| **5. 🎯 Đề Thi Chuẩn JLPT** | [**`../exam/README.md`**](../exam/README.md) | **3 Đề Full JLPT N2 (Mondai 1–9)** + **3 Đề Ôn Tiểu thuyết** (`222 câu`) | [**🎯 Thi Thử Auto-Grade**](../exam/index.html) • Giải thích chi tiết cả ĐÚNG lẫn SAI |

---

## 🚀 Lộ Trình Đề Xuất Dành Cho Em

1. **Học từ vựng qua Tiểu thuyết mỗi ngày 1 chương:**
   - Chọn thể loại em mê trong [**3 Bộ Tiểu Thuyết N2**](../novel/index.html): 💕 **Romcom** (Bài 1–14...), 🖤 **Yandere Tâm Lý** (Cảm xúc, Công nghệ, Phó từ...), ⚔️ **Isekai Kiến Quốc** (Kinh tế, Chính trị, Khoa học, Onomatopoeia, Cấu tạo từ!).
   - Bấm vào từ phát sáng để nghe MP3 chuẩn Nhật, xem bản dịch tiếng Việt & bảng từ vựng đầy đủ ngay dưới mỗi chương, rồi làm ngay 5 câu quiz kèm lời nhắc dịu dàng của chị Yuki.
2. **Củng cố Chữ Hán & Ngữ pháp song song:**
   - Đi kèm 1 bài [**Ngữ pháp (42 bài)**](./ngu-phap/README.md) và 1 bài [**Chữ Hán (53 bài)**](./kanji/README.md).
3. **Kiểm tra thực chiến với Đề Chuẩn JLPT N2 ([`exam/index.html`](../exam/index.html)):**
   - Làm Đề Ôn 20 câu ngay khi đọc xong mỗi bộ truyện, rồi bấm giờ 55 phút làm trọn **3 Đề Full JLPT N2 言語知識（文字・語彙・文法）**!

---
[🏠 Quay lại Trang chủ PentaNihonGo](../README.md)
"""
    with open(os.path.join(SHINKANZEN_DIR, "README.md"), "w", encoding="utf-8") as f:
        f.write(content)
    print("✅ Built master TOC: shinkanzen/README.md")


def write_nav_manifest():
    """Sinh shinkanzen/nav-manifest.js giúp reader.html điều hướng Trước/Sau & chọn bài."""
    p1_bunpou = {**BUNPOU_PART1_A, **BUNPOU_PART1_B}
    bunpou_items = [{"file": "shinkanzen/ngu-phap/README.md", "title": "📋 Mục lục Ngữ pháp N2"}]
    bunpou_items.extend(
        {"file": f"shinkanzen/ngu-phap/phan-1/bai-{n:02d}.md", "title": f"Phần 1 • Bài {n:02d}: {d['title_vi']}"}
        for n, d in sorted(p1_bunpou.items())
    )
    bunpou_items.extend(
        {"file": f"shinkanzen/ngu-phap/phan-2/bai-{n:02d}.md", "title": f"Phần 2 ★ • Bài {n:02d}: {d['title_vi']}"}
        for n, d in sorted(BUNPOU_PART2.items())
    )
    bunpou_items.extend(
        {"file": f"shinkanzen/ngu-phap/phan-3/bai-{n:02d}.md", "title": f"Phần 3 Đoạn văn • Bài {n:02d}: {d['title_vi']}"}
        for n, d in sorted(BUNPOU_PART3.items())
    )
    bunpou_items.append({"file": "shinkanzen/ngu-phap/phu-luc_kinh-ngu.md", "title": "Phụ lục Kính ngữ (敬語)"})

    goi_items = [{"file": "shinkanzen/tu-vung/README.md", "title": "📋 Mục lục Từ vựng N2"}]
    goi_items.extend(
        {"file": f"shinkanzen/tu-vung/phan-1/{l['filename']}", "title": f"Phần 1 • {l['chapter']} {l['lesson']}: {l['title_vi']}"}
        for l in GOI_PART1
    )
    goi_items.extend(
        {"file": f"shinkanzen/tu-vung/phan-2/{l['filename']}", "title": f"Phần 2 • {l['chapter']} {l['lesson']}: {l['title_vi']}"}
        for l in GOI_PART2
    )
    goi_items.append({"file": "shinkanzen/tu-vung/flashcards.md", "title": "🎴 Hướng dẫn Flashcards & Anki TSV"})

    kanji_items = [{"file": "shinkanzen/kanji/README.md", "title": "📋 Mục lục Chữ Hán (1.046 chữ)"}]
    for step_dir, arr in (("step-1", KANJI_STEP1), ("step-2", KANJI_STEP2)):
        for l in arr:
            kanji_items.append({"file": f"shinkanzen/kanji/{step_dir}/bai-{l['num']:02d}.md", "title": l["title_vi"]})
    kanji_items.append({"file": "shinkanzen/kanji/cot-luyen_1-2.md", "title": "🏋️ Challenge ①② & 総合問題 1"})
    for l in KANJI_STEP3_A + KANJI_STEP3_B:
        kanji_items.append({"file": f"shinkanzen/kanji/step-3/bai-{l['num']:02d}.md", "title": l["title_vi"]})
    kanji_items.append({"file": "shinkanzen/kanji/cot-luyen_3-4.md", "title": "🏋️ Challenge ②③④ & 総合問題 2"})
    kanji_items.append({"file": "shinkanzen/kanji/phu-luc_dac-biet.md", "title": "📕 Phụ lục 別冊1 (Âm đọc đặc biệt)"})

    novel_items = [{"file": "novel/README.md", "title": "📋 Mục lục 3 Tiểu thuyết (37 chương)"}]
    for nov, tag in ((ROMCOM_NOVEL, "Romcom"), (YANDERE_NOVEL, "Yandere"), (ISEKAI_NOVEL, "Isekai")):
        for ch in nov["chapters"]:
            novel_items.append({
                "file": f"novel/{nov['slug']}/{ch['slug']}.md",
                "title": f"{tag} Ch.{ch['num']:02d}: {ch['title_vi']}",
            })

    exam_items = [{"file": "exam/README.md", "title": "🎯 Tổng quan 6 Đề Thi Chuẩn JLPT N2"}]

    catalog = [
        {"label": "🗺️ Bản đồ Hệ thống N2", "items": [{"file": "shinkanzen/README.md", "title": "🗺️ Tổng quan Học liệu Shinkanzen × Tiểu thuyết × JLPT"}]},
        {"label": "📖 3 Bộ Tiểu Thuyết N2 (37 Bài)", "items": novel_items},
        {"label": "🎯 Đề Thi Chuẩn JLPT N2", "items": exam_items},
        {"label": "⛩️ Shinkanzen 1: Ngữ Pháp (文法)", "items": bunpou_items},
        {"label": "📚 Shinkanzen 2: Từ Vựng (語彙)", "items": goi_items},
        {"label": "🈷️ Shinkanzen 3: Chữ Hán (漢字)", "items": kanji_items},
        {"label": "📑 Cẩm Nang Tóm Lược N2", "items": [
            {"file": "docs/01_Tu_Vung_Kanji_N2.md", "title": "Từ Vựng & Kanji N2 Cốt Lõi"},
            {"file": "docs/02_Ngu_Phap_N2_Trong_Tam.md", "title": "120+ Mẫu Ngữ Pháp N2 Trọng Tâm"},
            {"file": "docs/03_Bi_Kip_Luyen_De_JLPT_N2.md", "title": "Bí Kíp Luyện Đề Chuẩn JLPT N2"},
        ]},
    ]
    out_path = os.path.join(SHINKANZEN_DIR, "nav-manifest.js")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("// Auto-generated by scripts/build_shinkanzen_all.py — Do not edit manually\n")
        f.write("window.PENTANIHON_NAV_CATALOG = ")
        json.dump(catalog, f, ensure_ascii=False, indent=2)
        f.write(";\n")
    print(f"✅ Built reader navigation manifest: shinkanzen/nav-manifest.js ({len(catalog)} collections)")


def build_all():
    build_bunpou()
    build_goi()
    build_kanji()
    build_novel()
    build_exam()
    write_shinkanzen_master_readme()
    write_nav_manifest()


if __name__ == "__main__":
    build_all()
