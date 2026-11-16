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
from build_dokkai_choukai import build_dokkai_choukai
from build_novel import build_novel

from shinkanzen_bunpou_data_p1a import BUNPOU_PART1_A
from shinkanzen_bunpou_data_p1b import BUNPOU_PART1_B
from shinkanzen_bunpou_data_p23 import BUNPOU_PART2, BUNPOU_PART3
from shinkanzen_goi_data_p1 import GOI_PART1
from shinkanzen_goi_data_p2 import GOI_PART2
from shinkanzen_kanji_data_s1 import KANJI_STEP1
from shinkanzen_kanji_data_s2 import KANJI_STEP2
from shinkanzen_kanji_data_s3a import KANJI_STEP3_A
from shinkanzen_kanji_data_s3b import KANJI_STEP3_B
from shinkanzen_dokkai_data import DOKKAI_PART1_2, DOKKAI_PART3
from shinkanzen_choukai_data import CHOUKAI_LESSONS
from shinkanzen_novel_data import NOVEL_CHAPTERS

SHINKANZEN_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../shinkanzen"))


def write_shinkanzen_master_readme():
    content = """# 📚 Trọn Bộ Giáo Trình Shinkanzen Master N2 (新完全マスター N2 — Chuẩn 5 Cuốn)

> 🌸 **Lời nhắn của chị Yuki:**  
> *"Bộ giáo trình này được tái cấu trúc chuẩn 100% theo **5 cuốn sách gốc 新完全マスター N2** của nhà xuất bản 3A Corporation (スリーエーネットワーク). Em không còn phải học gộp lệch bài nữa — mỗi kỹ năng đều đi đúng thứ tự chương, bài, chủ điểm, bẫy đề thi JLPT thực chiến và đầy đủ Furigana!"*

---

## 🗺️ Bản Đồ 5 Cuốn Sách Shinkanzen Master N2

| Cuốn sách (日本語) | Thư mục & Mục lục | Quy mô chuẩn sách gốc | Công cụ đặc biệt đi kèm |
| :--- | :--- | :--- | :--- |
| **1. 文法 (Ngữ pháp)** | [**`ngu-phap/README.md`**](./ngu-phap/README.md) | **Phần 1** (`26 bài`) + **Phần 2 ★** (`3 bài`) + **Phần 3** (`12 bài`) + **Kính ngữ** (`42 bài`) | Bảng đối chiếu mẫu dễ nhầm, bẫy thi & quiz Mondai 7–9 |
| **2. 語彙 (Từ vựng)** | [**`tu-vung/README.md`**](./tu-vung/README.md) | **Phần 1 (Chủ đề):** `9 chương, 21 bài` + **Phần 2 (Tính chất):** `7 chương, 16 bài` (`37 bài`, `780 từ`) | [**🎴 Web Flashcards Trắng Đen + In A4 + Anki TSV**](./tu-vung/flashcards.html) |
| **3. 漢字 (Chữ Hán)** | [**`kanji/README.md`**](./kanji/README.md) | **Step 1** (`14 bài`) + **Step 2** (`16 bài`) + **Step 3** (`23 bài`) = **53 bài (`1.046 chữ`)** | **2 Cột Challenge & Phụ lục 別冊1** (Âm đọc đặc biệt) |
| **4. 読解 (Đọc hiểu)** | [**`doc-hieu/README.md`**](./doc-hieu/README.md) | **Phần 1 & 2 (Kỹ năng):** `4 bài` + **Phần 3 (Thực chiến):** `4 dạng Mondai` (`8 bài`) | Bài đọc 100% Furigana + bẫy loại trừ `言い過ぎ・逆転・※` |
| **5. 聴解 (Nghe hiểu)** | [**`nghe-hieu/README.md`**](./nghe-hieu/README.md) | **Chương I – VI:** Đặc trưng âm, Phản xạ nhanh, Mondai 1–5 (`6 chương`) | Kịch bản chuẩn TTS (`track_id` / `speakers`) + luyện Shadowing |

---

## 🚀 Lộ Trình Đề Xuất Dành Cho Em

1. **Mỗi ngày 1 cặp Từ vựng + Chữ Hán (30 phút):**
   - Mở 1 bài trong [**Từ vựng (37 bài)**](./tu-vung/README.md) và lật luôn bộ [**Flashcards 37 bài**](./tu-vung/flashcards.html) (hoặc in A4 gập đôi mang theo bên người).
   - Đi kèm 1 bài trong [**Chữ Hán (53 bài — 1.046 chữ)**](./kanji/README.md), mỗi bài chỉ ~18–20 chữ kèm 2 từ ghép sát đề thi.
2. **Cách ngày 1 bài Ngữ pháp (30 phút):**
   - Hoàn thành trọn [**Phần 1: 26 bài Văn pháp 1**](./ngu-phap/phan-1/bai-01.md) để nắm 100% mẫu câu N2.
   - Chuyển sang [**Phần 2: Sắp xếp dấu sao ★**](./ngu-phap/phan-2/bai-01.md) và [**Phần 3: Ngữ pháp đoạn văn (12 bài)**](./ngu-phap/phan-3/bai-01.md).
3. **Cuối tuần luyện Đọc hiểu & Nghe hiểu (45 phút):**
   - Học kỹ 4 bài kỹ năng trước rồi bấm giờ giải 4 dạng Mondai trong [**Đọc hiểu**](./doc-hieu/README.md).
   - Đọc Shadowing toàn bộ kịch bản văn nói rút gọn trong [**Nghe hiểu Chương I–VI**](./nghe-hieu/README.md).
4. **Đọc thư giãn & ôn phản xạ thực chiến với Tiểu thuyết tương tác ([`novel/index.html`](../novel/index.html)):**
   - Đọc trọn bộ tiểu thuyết ngắn 6 chương **「東京（とうきょう）の小さな書斎（しょさい）」** đầy đủ Hiragana kế bên; bấm vào bất kỳ từ Shinkanzen nào trong truyện để bật sáng và mở ngay Bảng Hướng Dẫn chi tiết kèm câu hỏi từng chương!

---
[🏠 Quay lại Trang chủ PentaNihonGo](../README.md)
"""
    with open(os.path.join(SHINKANZEN_DIR, "README.md"), "w", encoding="utf-8") as f:
        f.write(content)
    print("✅ Built master TOC: shinkanzen/README.md")


def write_nav_manifest():
    """Sinh shinkanzen/nav-manifest.js giúp reader.html điều hướng Trước/Sau & chọn bài cho mọi cuốn sách."""
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

    dokkai_items = [{"file": "shinkanzen/doc-hieu/README.md", "title": "📋 Mục lục Đọc hiểu N2"}]
    dokkai_items.extend(
        {"file": f"shinkanzen/doc-hieu/phan-1_luyen-ky-nang/{d['filename']}", "title": d["title_vi"]}
        for d in DOKKAI_PART1_2
    )
    dokkai_items.extend(
        {"file": f"shinkanzen/doc-hieu/phan-2_thuc-chien/{d['filename']}", "title": d["title_vi"]}
        for d in DOKKAI_PART3
    )

    choukai_items = [{"file": "shinkanzen/nghe-hieu/README.md", "title": "📋 Mục lục Nghe hiểu N2"}]
    choukai_items.extend(
        {"file": f"shinkanzen/nghe-hieu/{c['filename']}", "title": c["title_vi"]}
        for c in CHOUKAI_LESSONS
    )

    novel_items = [{"file": "novel/README.md", "title": "📋 Mục lục Tiểu thuyết N2 (Markdown)"}]
    novel_items.extend(
        {"file": f"novel/{ch['slug']}.md", "title": ch["title_vi"]}
        for ch in NOVEL_CHAPTERS
    )

    catalog = [
        {"label": "🗺️ Tổng quan 5 cuốn Shinkanzen", "items": [{"file": "shinkanzen/README.md", "title": "🗺️ Bản đồ trọn bộ Shinkanzen Master N2"}]},
        {"label": "⛩️ Shinkanzen 1: Ngữ Pháp (文法)", "items": bunpou_items},
        {"label": "📚 Shinkanzen 2: Từ Vựng (語彙)", "items": goi_items},
        {"label": "🈷️ Shinkanzen 3: Chữ Hán (漢字)", "items": kanji_items},
        {"label": "📖 Shinkanzen 4: Đọc Hiểu (読解)", "items": dokkai_items},
        {"label": "🎧 Shinkanzen 5: Nghe Hiểu (聴解)", "items": choukai_items},
        {"label": "📓 Tiểu Thuyết Tương Tác N2", "items": novel_items},
        {"label": "📑 Cẩm Nang Tóm Lược N2", "items": [
            {"file": "docs/01_Tu_Vung_Kanji_N2.md", "title": "Từ Vựng & Kanji N2 Cốt Lõi"},
            {"file": "docs/02_Ngu_Phap_N2_Trong_Tam.md", "title": "120+ Mẫu Ngữ Pháp N2 Trọng Tâm"},
            {"file": "docs/03_Chien_Thuat_Doc_Hieu_N2.md", "title": "Chiến Thuật Bẻ Khóa Đọc Hiểu"},
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
    build_dokkai_choukai()
    build_novel()
    write_shinkanzen_master_readme()
    write_nav_manifest()


if __name__ == "__main__":
    build_all()
