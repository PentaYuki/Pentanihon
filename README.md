# 🎌 Pentanihon - Cẩm Nang Ôn Luyện JLPT N2 & Kể Chuyện Mỗi Ngày

<p align="center">
  <img src="https://img.shields.io/badge/JLPT-N2%20Master-red?style=for-the-badge&logo=japan" alt="JLPT N2" />
  <img src="https://img.shields.io/badge/Shinkanzen-5%20Books%20Complete-green?style=for-the-badge" alt="Shinkanzen 5 Books" />
  <img src="https://img.shields.io/badge/Daily-Stories%20Included-orange?style=for-the-badge" alt="Daily Stories" />
  <img src="https://img.shields.io/badge/Hiragana-100%25%20Annotated-blue?style=for-the-badge" alt="Hiragana Annotated" />
  <img src="https://img.shields.io/badge/Audio--Ready-TTS%20Metadata-purple?style=for-the-badge" alt="Audio Ready" />
</p>

Chào mừng bạn đến với **Pentanihon** – dự án học tiếng Nhật toàn diện được thiết kế đặc biệt cho kỳ thi **JLPT N2**, kết hợp phương pháp học giáo trình kinh điển **Shinkanzen Master** và phương pháp học cảm xúc qua **Truyện kể mỗi ngày (Storytelling)** dưới sự đồng hành của **"Người chị gái dễ thương"**.

---

## 🌟 Những Điểm Nổi Bật Của Dự Án

- 🌸 **Đồng hành cùng Chị Gái Dễ Thương:** Giọng văn chỉ bảo ân cần, hóm hỉnh, phân tích sắc thái tâm lý người Nhật, mẹo nhớ đời và chỉ điểm các cạm bẫy trắc nghiệm hay gặp.
- 🔤 **Phiên âm Hiragana 100%:** Mọi chữ Hán trong câu ví dụ, hội thoại nghe, bài đọc hiểu và đề thi trắc nghiệm đều được chú thích Hiragana `漢字（かんじ）` để người học đọc mượt mà, không bị khựng lại.
- 🎧 **Dữ liệu Nghe sẵn sàng cho Tool Audio (TTS-Ready):** Toàn bộ file kịch bản nghe đều có cấu trúc trường rõ ràng (`track_id`, `speakers: ["Narrator", "Man", "Woman"]`) giúp dễ dàng lập trình bot đọc audio hoặc tích hợp ứng dụng di động.
- 📖 **Tiểu Thuyết Ngắn Tương Tác N2 ([`novel/index.html`](./novel/index.html)):** Cuốn sách ngắn 6 chương **「東京（とうきょう）の小さな書斎（しょさい）」** (*Căn Phòng Đọc Nhỏ Giữa Lòng Tokyo*) vận dụng trực tiếp từ vựng & ngữ pháp Shinkanzen với Hiragana đứng kế bên; **click vào từ có trong Shinkanzen sẽ tự phát sáng + mở Bảng Hướng Dẫn chi tiết**, đi kèm câu hỏi trắc nghiệm ngay bên cạnh mỗi chương.
- ☕ **Series Dài Tập Nhật Ngữ (`story/`):** Bộ truyện dài tập chính thức **「東京（とうきょう）あおぞら物語（ものがたり）」** (*Câu Chuyện Bầu Trời Xanh Tokyo - Quyển Sổ Ước Mơ Của Ren Và Chị Yuki*). Cốt truyện liên hoàn nhiều tập, lồng ghép khéo léo ngữ pháp N2, từ vựng đắt giá và câu hỏi đọc hiểu Dokkai kịch tính.
- ⏰ **Tự Động Hóa & Đặt Lịch:** Tích hợp script [**`daily_study_scheduler.py`**](./scripts/daily_study_scheduler.py) và **GitHub Actions Workflow** tự động chạy lịch học mỗi ngày.

---

## 🗂️ Cấu Trúc Thư Mục Dự Án

```text
Pentanihon/
├── README.md                          # Trang chủ tổng quan dự án
├── .github/workflows/
│   └── daily-story.yml                # GitHub Actions tự động chạy lịch học mỗi ngày
├── docs/                              # Cẩm nang tóm lược kiến thức N2 cốt lõi
│   ├── 01_Tu_Vung_Kanji_N2.md         # Tổng hợp phó từ, tiền tố, hậu tố, từ đồng nghĩa
│   ├── 02_Ngu_Phap_N2_Trong_Tam.md    # 120+ mẫu ngữ pháp phân loại theo cụm ý nghĩa
│   └── 03_Chien_Thuat_Doc_Hieu_N2.md  # Kỹ thuật bẻ khóa bài đọc và 4 loại bẫy kinh điển
├── shinkanzen/                        # Trọn bộ 5 cuốn Shinkanzen Master N2 chuẩn sách gốc
│   ├── README.md                      # Bản đồ tổng hợp lộ trình học cả 5 cuốn N2
│   ├── ngu-phap/                      # ⛩️ Văn pháp (Phần 1: 26 bài, Phần 2 ★: 3 bài, Phần 3: 12 bài, Kính ngữ)
│   ├── tu-vung/                       # 📚 Từ vựng (Phần 1: 21 bài chủ đề, Phần 2: 16 bài tính chất + Flashcards)
│   │   ├── flashcards.html            # Web Flashcards Trắng Đen & Bản in A4 gập đôi cả 37 bài
│   │   └── flashcards-anki.tsv        # Deck 780 từ vựng N2 import trực tiếp vào Anki
│   ├── kanji/                         # 🈷️ Chữ Hán (Step 1-3: 53 bài đủ 1.046 chữ + Challenge + 別冊1)
│   ├── doc-hieu/                      # 📖 Đọc hiểu (4 chuyên đề kỹ năng + 4 dạng thực chiến Mondai N2)
│   └── nghe-hieu/                     # 🎧 Nghe hiểu (Chương I-VI chuẩn TTS + Furigana Shadowing)
├── novel/                             # 📖 Tiểu thuyết ngắn 6 chương vận dụng từ Shinkanzen (tương tác)
│   ├── index.html                     # Trình đọc sách: click từ Shinkanzen phát sáng + Popover hướng dẫn + Quiz
│   ├── README.md                      # Mục lục bản Markdown 6 chương
│   └── chuong-01..06.md               # Nội dung đầy đủ Hiragana, bảng từ Shinkanzen & câu hỏi mỗi chương
├── story/                             # Series Dài Tập: Tokyo Aozora Monogatari
│   ├── README.md                      # Mục lục, sơ đồ nhân vật & hướng dẫn học
│   ├── series-01_tap-01_chiec_vali_ga_tokyo.md  # Tập 01: Chiếc Vali Ở Ga Tokyo
│   ├── series-01_tap-02_tach_ca_phe_aozora.md   # Tập 02: Hương Cà Phê & Lời Hứa Ban Đầu
│   ├── series-01_tap-03_ong_lao_pho_sach.md     # Tập 03: Ông Lão Phố Sách Cổ & Bản CV
│   ├── series-01_tap-04_con_mua_shibuya.md      # Tập 04: Cơn Mưa Rào Shibuya & Cuộc Gặp Gỡ
│   ├── series-01_tap-05_canh_cua_phong_van.md   # Tập 05: Cánh Cửa Phỏng Vấn Vòng Một
│   ├── series-01_tap-06_dem_dong_jimbocho.md    # Tập 06: Đêm Đông Jimbocho & Ký Ức Chị Yuki
│   └── oneshots/                      # Lưu trữ các truyện ngắn độc lập trước đây
└── scripts/
    ├── build_shinkanzen_all.py        # Orchestrator sinh trọn bộ 5 cuốn Shinkanzen chuẩn sách gốc
    ├── daily_study_scheduler.py       # Script quản lý tiến độ và lịch học hàng ngày
    └── generate_daily_story.py        # Engine tự động xuất bản tập tiếp theo của Series
```

---

## 🗺️ Lộ Trình Ôn Luyện Shinkanzen Master N2 Chuẩn 5 Cuốn Sách Gốc

| Giáo trình | Mục lục chính | Trọng tâm kiến thức |
| :--- | :--- | :--- |
| **1. 文法 (Ngữ pháp)** | [**`shinkanzen/ngu-phap/README.md`**](./shinkanzen/ngu-phap/README.md) | 26 bài Văn pháp câu 1, 3 bài sắp xếp dấu sao ★, 12 bài Văn pháp đoạn văn & Kính ngữ |
| **2. 語彙 (Từ vựng)** | [**`shinkanzen/tu-vung/README.md`**](./shinkanzen/tu-vung/README.md) | 21 bài theo chủ đề + 16 bài theo tính chất (đa nghĩa, phó từ, láy âm, cấu tạo từ) + Flashcards |
| **3. 漢字 (Chữ Hán)** | [**`shinkanzen/kanji/README.md`**](./shinkanzen/kanji/README.md) | 53 bài phủ đúng 1.046 chữ (Step 1–3) + Challenge + Phụ lục âm đọc đặc biệt 別冊1 |
| **4. 読解 (Đọc hiểu)** | [**`shinkanzen/doc-hieu/README.md`**](./shinkanzen/doc-hieu/README.md) | 5 cấu trúc bài văn, 5 kỹ thuật giải câu hỏi, đọc tờ rơi/bảng biểu & 4 dạng Mondai thực chiến |
| **5. 聴解 (Nghe hiểu)** | [**`shinkanzen/nghe-hieu/README.md`**](./shinkanzen/nghe-hieu/README.md) | Rút gọn âm văn nói, Phản xạ nhanh (Mondai 4) & toàn bộ kỹ năng Mondai 1–5 (TTS-ready) |

👉 Bản đồ chi tiết và hướng dẫn kết hợp 5 cuốn xem tại: [**`shinkanzen/README.md`**](./shinkanzen/README.md)

---

## ☕ Series Dài Tập: 「東京（とうきょう）あおぞら物語（ものがたり）」 (`story/`)

Thay vì những đoạn văn nhỏ rời rạc, dự án phát hành theo **Series phim truyền hình dài tập**:
1. **Theo chân nhân vật xuyên suốt:** Ren (kỹ sư IT trẻ) và chị Yuki (chủ quán cà phê sách Jimbocho).
2. **Cốt truyện liền mạch:** Từng tập có phần tóm tắt tập trước (`前回のあらすじ`) và hé lộ tập sau (`次回予告`).
3. **Thấm nhuần ngữ pháp N2 tự nhiên:** 4-5 mẫu ngữ pháp thực tế được đan cài khéo léo trong lời thoại.
4. **Luyện đọc hiểu Dokkai:** Câu hỏi trắc nghiệm kiểm tra độ sâu sắc của việc cảm thụ văn bản.

👉 Khám phá sơ đồ nhân vật & toàn bộ các tập tại: [**`story/README.md`**](./story/README.md)

---

## 🚀 Hướng Dẫn Sử Dụng & Tự Động Hóa

### Chạy Dashboard Lịch Học:
```bash
python3 scripts/daily_study_scheduler.py
```

### Kích hoạt GitHub Actions:
Workflow tự động được lên lịch chạy vào lúc **07:00 sáng mỗi ngày (giờ Việt Nam)**, hoặc bạn có thể vào tab **Actions** trên GitHub và nhấn **Run workflow** bất cứ lúc nào.

---

## 💖 Lời Nhắn Từ Chị Gái
> *"Học một ngôn ngữ mới cũng như trồng một mầm cây vậy, mỗi ngày tưới một chút nước kiên trì thì nhất định sẽ nở hoa thơm ngát. Chúc bé của chị ôn thi thật tốt và luôn vững tin vào chính mình nha!"*
