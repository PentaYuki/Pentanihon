# -*- coding: utf-8 -*-
"""
Dữ liệu Shinkanzen Master Đọc Hiểu N2 (新完全マスター読解 N2)
実力養成編:
- 第1部 評論・解説・エッセイなど (2 bài tổng hợp 10 kỹ năng cốt lõi)
- 第2部 広告・お知らせ・説明書きなど (2 bài kỹ năng đọc tìm kiếm & biểu bảng)
- 第3部 実戦問題 (4 dạng Mondai chuẩn đề JLPT N2: 中文・長文・統合理解・情報検索)
"""

DOKKAI_PART1_2 = [
    {
        "filename": "01_cau-truc-bai-van.md",
        "part_label": "実力養成編 第1部 — 文章のしくみを理解する",
        "title_jp": "文章のしくみを理解する（5つの基本構造）",
        "title_vi": "Bài 01 — Nắm Bắt Cấu Trúc Bài Văn (5 Kỹ Thuật Cốt Lõi)",
        "intro": "Đọc hiểu N2 không phải dịch từng chữ từ đầu đến cuối như N4-N3 đâu nhé! Ở chương mở đầu **Shinkanzen Master Đọc hiểu N2**, em sẽ học cách 'nhìn xuyên khung xương' bài văn qua 5 tín hiệu: **Đối chiếu (対比)**, **Diễn giải (言い換え)**, **Ẩn dụ (比喩)**, **Câu hỏi nêu vấn đề (疑問提示文)** và **Câu khẳng định chủ trương (主張表現)**.",
        "skills": [
            (
                "1) [対比] Đối chiếu / So sánh (ほかのものと比べる)",
                "A の場合（ばあい）〜。一方（いっぽう）、B は〜 / A に対して B は / A に比べ（くらべ）ると B は",
                "Khi tác giả đặt A bên cạnh B (ví dụ: Nhật Bản ⇄ phương Tây, quá khứ ⇄ hiện tại, tự nhiên ⇄ nhân tạo), **ý chính thường nằm ở vế B (sau `一方` / `それに対して` / `しかし`)** nhằm làm nổi bật nét riêng hoặc quan điểm tác giả muốn nhấn mạnh."
            ),
            (
                "2) [言い換え] Nói lại bằng từ khác (ほかの言葉で言い換える)",
                "つまり / すなわち / 要する（ようする）に / 言（い）い換（か）えると",
                "Câu trước có thể dùng từ chuyên ngành khó hoặc cách nói trừu tượng, nhưng sau `つまり` tác giả dịch lại bằng ngôn ngữ bình dân hơn — **đây chính là đáp án paraphrase cho câu hỏi gạch chân!**"
            ),
            (
                "3) [比喩] So sánh ví von (ほかのものにたとえる)",
                "まるで〜ようだ / 〜にたとえられる / 〜のようなものだ",
                "Đừng hiểu nghĩa đen câu ví von! Nếu tác giả viết 'ngôn ngữ giống như dòng sông', ý thực chất không phải về nước mà là 'luôn biến đổi không ngừng theo thời đại'."
            ),
            (
                "4) [疑問提示文] Câu hỏi dẫn nhập (疑問文を使って話題を提示する)",
                "なぜ〜のだろうか / 本当（ほんとう）に〜といえるだろうか / いったい何（なに）が〜か",
                "Tác giả đặt câu hỏi giữa bài KHÔNG phải để hỏi độc giả tự đoán, mà ngay sau đó tác giả sẽ đưa ra **câu trả lời = Luận điểm chính của bài** (`〜ではないだろうか`, `その理由は〜だ`)."
            ),
            (
                "5) [主張表現] Tín hiệu câu chủ trương (自分の意見であることを示す)",
                "〜に違（ちが）いない / 〜と言（い）える / 〜べきだ / 〜のではないだろうか / 〜と私（わたし）は考（かんが）える",
                "Gặp những đuôi câu này ở cuối đoạn hoặc cuối bài là phải khoanh ngay lại! Câu hỏi `筆者の主張` (Quan điểm tác giả) 90% xoay quanh các câu có đuôi `〜ではないだろうか` (nhận định mềm nhưng dứt khoát) hoặc `〜べきだ`."
            ),
        ],
        "passages": [
            {
                "title": "Bài đọc mẫu 1 — Kỹ thuật Đối chiếu & Câu hỏi nêu vấn đề (対比・疑問提示)",
                "jp": (
                    "最近（さいきん）、街（まち）の中（なか）でスマートフォンを見（み）ながら歩（ある）く人（ひと）をよく見（み）かける。"
                    "情報（じょうほう）をいつでも手（て）に入（い）れられるという点（てん）では、確（たし）かに便利（べんり）になったと言（い）える。"
                    "しかし、便利（べんり）さと引（ひ）き換（か）えに、私（わたし）たちは何（なに）か大切（たいせつ）なものを失（うしな）っているのではないだろうか。"
                    "昔（むかし）は電車（でんしゃ）の中（なか）で本（ほん）を読（よ）んだり、窓（まど）の外（そと）の景色（けしき）をぼんやり眺（なが）めたりする時間（じかん）があった。"
                    "何（なに）もしないその「余白（よはく）」の時間（じかん）こそが、人（ひと）の創造力（そうぞうりょく）を育（そだ）てていたのだ。ところが現在（げんざい）は、わずか数分（すうふん）の空（あ）き時間（じかん）さえも画面（がめん）からの情報（じょうほう）で埋（う）め尽（つ）くされている。"
                    "情報（じょうほう）に追（お）われる毎日（まいにち）から少（すこ）し離（はな）れて、頭（あたま）を休（やす）める時間（じかん）を意識的（いしきてき）に作（つく）るべきだろう。"
                ),
                "vi": "Gần đây ta thường thấy nhiều người vừa đi vừa nhìn smartphone trên phố. Xét trên phương diện có thể lấy thông tin bất cứ lúc nào thì quả thực đã tiện lợi hơn. Thế nhưng, đánh đổi với sự tiện lợi đó, phải chăng chúng ta đang đánh mất thứ gì đó quan trọng? Ngày xưa trên tàu điện còn có thời gian đọc sách hoặc ngắm cảnh qua cửa sổ một cách thảnh thơi. Chính khoảng thời gian 'khoảng trống' không làm gì đó đã nuôi dưỡng sức sáng tạo của con người. Trái lại hiện nay, ngay cả vài phút trống ít ỏi cũng bị lấp đầy bởi thông tin từ màn hình. Có lẽ chúng ta nên chủ động tách khỏi cuộc sống bị thông tin đuổi theo mỗi ngày để tạo thời gian cho đầu óc nghỉ ngơi.",
                "analysis": [
                    "**Câu nhử (`譲歩`):** `情報（じょうほう）をいつでも…確（たし）かに便利（べんり）になった` -> Thừa nhận mặt tốt trước (`確かに〜が`).",
                    "**Câu hỏi dẫn (`疑問提示文`):** `失（うしな）っているのではないだろうか` -> Báo hiệu trọng tâm tác giả sắp nói về thứ bị đánh mất.",
                    "**Đối chiếu (`対比`):** `昔（むかし）は…「余白（よはく）」の時間（じかん）があった` ⇄ `ところが現在（げんざい）は…埋（う）め尽（つ）くされている`.",
                    "**Câu chủ trương (`主張`):** `頭（あたま）を休（やす）める時間（じかん）を意識的（いしきてき）に作（つく）るべきだろう` -> Khuyên nên chủ động tạo khoảng thời gian nghỉ ngơi khỏi màn hình."
                ],
                "quiz": [
                    ("筆者（ひっしゃ）によると、昔（むかし）の電車（でんしゃ）の中（なか）の時間（じかん）にはどのような役割（やくわり）があったか。", [
                        "仕事（しごと）に役立（やくだ）つ最新（さいしん）の情報（じょうほう）を集（あつ）める役割（やくわり）",
                        "何（なに）もしない時間（じかん）によって人（ひと）の創造力（そうぞうりょく）を育（そだ）てる役割（やくわり）",
                        "他人（たにん）と積極的（せっきょくてき）にコミュニケーションをとる役割（やくわり）",
                        "スマートフォンを使（つか）って頭（あたま）を休（やす）める役割（やくわり）"
                    ], 2, "Câu giữa bài nêu rõ: 何もしないその「余白」の時間こそが、人の創造力を育てていたのだ -> Đáp án 2."),
                    ("この文章（ぶんしょう）で筆者（ひっしゃ）が最（もっと）も言（い）いたいことは何（なに）か。", [
                        "街（まち）の中（なか）でスマートフォンを見（み）ながら歩（ある）くのは危険（きけん）だから禁止（きんし）すべきだ。",
                        "便利（べんり）なスマートフォンのおかげで、空（あ）き時間（じかん）を有効（ゆうこう）に使（つか）えるようになった。",
                        "情報（じょうほう）から少（すこ）し離（はな）れて、頭（あたま）を休（やす）める「余白（よはく）」の時間（じかん）を作（つく）るべきだ。",
                        "電車（でんしゃ）に乗（の）るときは必（かなら）ず本（ほん）を読（よ）む習慣（しゅうかん）をつけたほうがいい。"
                    ], 3, "Bẫy 1 & 4 quá cụ thể/sai phạm vi (`禁止すべき`, `必ず本を読む`). Bẫy 2 đi ngược mạch chỉ trích sự quá tải thông tin. Đáp án 3 khớp trực tiếp câu主張 cuối bài.")
                ]
            }
        ]
    },
    {
        "filename": "02_ky-thuat-giai-cau-hoi.md",
        "part_label": "実力養成編 第1部 — 問いを解く技術を身につける",
        "title_jp": "問いを解く技術を身につける（指示語・主述・下線部・理由・例）",
        "title_vi": "Bài 02 — 5 Kỹ Thuật Giải Quyết Câu Hỏi & Nhận Diện Bẫy Đáp Án",
        "intro": "Hiểu bài văn rồi nhưng sao chọn A lại trúng B? Vì đề JLPT N2 gài bẫy cực tinh ở 5 dạng câu hỏi trọng tâm trong Phần 1 Mục 2 của sách **Shinkanzen Master Đọc hiểu N2**: câu hỏi **Chỉ thị từ (`指示語`)**, **Chủ ngữ-Vị ngữ (`だれが・何が`)**, **Nghĩa gạch chân (`下線部`)**, **Lý do (`理由`)**, và **Ví dụ (`例`)**.",
        "skills": [
            (
                "1) 指示語を問う (Câu hỏi đại từ chỉ thị: これ・それ・あれ・その〜)",
                "Câu gạch chân có `このような〜` / `それ` / `この点`",
                "Đáp án hầu như nằm ở **1–2 câu ngay phía trước** từ chỉ thị! Nhớ kỹ kỹ năng **thay thế ngược**: nhét nội dung phương án chọn vào vị trí `これ/その〜` xem câu đọc lên có mượt tự nhiên cả về ngữ pháp lẫn ý nghĩa không."
            ),
            (
                "2)「だれが」「何が」「何を」などを問う (Tách Chủ-Vị trong câu phức dài)",
                "Câu dài 3-4 dòng nhiều định ngữ bổ nghĩa chồng chéo",
                "Gạch bỏ tạm các cụm định ngữ đứng trước danh từ, tìm **Chủ ngữ gốc đi với `は/が`** và **Động từ chốt ở cuối câu**. Bẫy thi hay hoán đổi vị trí A gây ra B thành B gây ra A!"
            ),
            (
                "3) 下線部の意味を問う (Giải thích cụm từ/hình ảnh gạch chân)",
                "`〜とあるが、どういうことか` / `〜とあるが、なぜか`",
                "Không tự suy diễn nghĩa từ điển ngoài bài! Hãy tìm câu ngay trước/sau phần gạch chân xem tác giả có dùng `つまり`, `すなわち`, `というのは` hay ví dụ song song để giải thích cụm đó không."
            ),
            (
                "4) 理由を問う (Câu hỏi lý do: なぜか / 理由は何か)",
                "Tín hiệu trả lời: `〜からだ` / `〜ためだ` / `〜によって` / `というのは〜`",
                "Ngoài việc đọc xung quanh chữ `からだ・ため`, phải kiểm tra xem có lý do **gián tiếp ở đoạn trên** không — nhiều khi đề hỏi lý do sâu xa chứ không phải nguyên nhân bề mặt ngay cạnh dấu gạch."
            ),
            (
                "5) 例を問う (Câu hỏi về vai trò của Ví dụ: どんな例・なぜ出したか)",
                "Tín hiệu: `たとえば` / trích dẫn câu chuyện đời thường, lịch sử",
                "Đừng bao giờ chọn đáp án chỉ mô tả thuần túy chi tiết của ví dụ! Khi đề hỏi về ví dụ, đáp án đúng phải kết nối được **ví dụ đó chứng minh cho luận điểm khái quát nào của tác giả**."
            ),
        ],
        "passages": [
            {
                "title": "Bài đọc mẫu 2 — Luyện 4 loại bẫy kinh điển JLPT N2",
                "jp": (
                    "料理（りょうり）をするとき、レシピ通（どお）りに材料（ざいりょう）の分量（ぶんりょう）をきっちり計（はか）らなければおいしく作（つく）れないと思（おも）っている人（ひと）は多（おお）い。"
                    "もちろん、初（はじ）めて作（つく）る料理（りょうり）や菓子（かし）作（づく）りの場合（ばあい）は正確（せいかく）さが大切（たいせつ）だ。"
                    "しかし、日常（にちじょう）の家庭（かてい）料理（りょうり）においては、その日（ひ）の気温（きおん）や材料（ざいりょう）の鮮度（せんど）によって火加減（ひかげん）や味付（あじつ）けが微妙（びみょう）に変（か）わるものである。"
                    "たとえ同（おな）じニンジンでも、季節（きせつ）によって甘（あま）みや水分量（すいぶんりょう）が違（ちが）うため、教科書（きょうかしょ）どおりの分量（ぶんりょう）に頼（たよ）りすぎるのは<u>かえって失敗（しっぱい）のもと</u>になることがある。"
                    "本当（ほんとう）に大切（たいせつ）なのは、自分（じぶん）の目（め）と舌（した）で確（たし）かめながら柔軟（じゅうなん）に調整（ちょうせい）する感覚（かんかく）なのである。"
                ),
                "vi": "Khi nấu ăn, có nhiều người nghĩ rằng nếu không cân đo chính xác từng gam nguyên liệu theo công thức thì không thể nấu ngon. Đương nhiên với món lần đầu nấu hay làm bánh thì sự chính xác rất quan trọng. Tuy nhiên trong nấu ăn gia đình hàng ngày, độ lửa hay nêm nếm thường thay đổi tinh tế tùy vào nhiệt độ hôm đó hay độ tươi của nguyên liệu. Ngay cả cùng là cà rốt nhưng tùy mùa mà vị ngọt và lượng nước cũng khác nhau, vì vậy việc quá phụ thuộc vào định lượng rập khuôn sách giáo khoa trái lại có thể trở thành nguyên nhân gây hỏng món. Điều thực sự quan trọng chính là cảm quan tự điều chỉnh linh hoạt trong lúc tự kiểm tra bằng mắt và vị giác của bản thân.",
                "analysis": [
                    "**Bẫy thường gặp ở N2:**",
                    "- `言い過ぎ` (Nói quá lên): dùng `まったく・必ず・一切・だけ` khi bài chỉ nói `ある/ことがある`.",
                    "- `逆転` (Đảo ngược): bài bảo quá phụ thuộc dễ hỏng -> đáp án sai bảo lúc nào cũng nên làm đúng công thức.",
                    "- `すり替え` (Đánh tráo chi tiết): lấy ví dụ `菓子作り` (làm bánh cần chính xác) gán cho nấu ăn gia đình hàng ngày."
                ],
                "quiz": [
                    ("<u>かえって失敗（しっぱい）のもと</u>とあるが、なぜか。", [
                        "家庭（かてい）料理（りょうり）は菓子（かし）作（づく）りよりも正確（せいかく）な計量（けいりょう）が必要（ひつよう）だから。",
                        "同じ（おな）レシピを使（つか）っても、料理（りょうり）する人（ひと）の好（この）みが毎日（まいにち）違（ちが）うから。",
                        "季節（きせつ）や気候（きこう）などによって材料（ざいりょう）の状態（じょうたい）や味（あじ）が異（こと）なるから。",
                        "教科書（きょうかしょ）に書（か）かれている分量（ぶんりょう）自体（じたい）が間違（まちが）っていることが多いから。"
                    ], 3, "Ngay trước phần gạch chân giải thích rõ: `その日の気温や材料の鮮度によって…季節によって甘みや水分量が違うため` -> Đáp án 3."),
                    ("ニンジンの例（れい）を出（だ）して筆者（ひっしゃ）が言（い）いたいことは何（なに）か。", [
                        "ニンジンは季節（きせつ）を問（と）わず同（おな）じ味（あじ）になるよう品種（ひんしゅ）改良（かいりょう）されている。",
                        "食材（しょくざい）の状態（じょうたい）に合（あ）わせて、自分（じぶん）の感覚（かんかく）で柔軟（じゅうなん）に調整（ちょうせい）することが大切（たいせつ）だ。",
                        "おいしく作（つく）りたいなら新鮮（しんせん）なニンジンだけを選（えら）んで買（か）うべきだ。",
                        "初（はじ）めて料理（りょうり）する人（ひと）は、まずニンジンの料理（りょうり）から練習（れんしゅう）したほうがいい。"
                    ], 2, "Câu hỏi về Ví dụ (`例を問う`): ví dụ củ cà rốt dùng để minh họa cho luận điểm câu cuối (`自分の目と舌で確かめながら柔軟に調整する感覚が大切`) -> Đáp án 2.")
                ]
            }
        ]
    },
    {
        "filename": "03_thong-bao-quang-cao.md",
        "part_label": "実力養成編 第2部 — 広告・お知らせ・説明書きなど（1）",
        "title_jp": "全体をつかむ・情報を探し出す（1）広告・（2）お知らせ",
        "title_vi": "Bài 03 — Đọc Quảng Cáo & Thông Báo Thực Tế (Scanning Siêu Tốc)",
        "intro": "Phần 2 của **Shinkanzen Master Đọc hiểu N2** chuyển sang các văn bản đời sống thực tế: **Quảng cáo (`広告`)** và **Thông báo (`お知らせ`)**. Mục tiêu là **không đọc toàn văn ngay lập tức** mà quét thẳng tiêu đề lớn, đối tượng áp dụng, thời hạn và **dòng chú thích nhỏ có dấu `※` ở cuối tờ** — nơi chứa 80% bẫy điểm liệt!",
        "skills": [
            (
                "Bước 1 — Nhìn tiêu đề & câu hỏi trước (全体をつかむ)",
                "Xem ngay bài là thông báo gì (chuyển lịch, tuyển sinh, khuyến mãi, ngưng phục vụ) và đề hỏi AI / CÁI GÌ / KHI NÀO.",
                "Tuyệt đối không đọc từ chữ đầu tiên xuống dưới như tiểu thuyết! Đọc câu hỏi -> Khoanh từ khóa điều kiện (ngày tháng, giá tiền, đối tượng loại trừ)."
            ),
            (
                "Bước 2 — Soi các cụm phủ định & điều kiện ngoại lệ (情報を探し出す)",
                "`※ただし〜を除く` (ngoại trừ...), `〜に限る` (chỉ giới hạn...), `〜に限りません` (không giới hạn chỉ...), `〜は対象外` (không thuộc đối tượng).",
                "Khi tờ rơi ghi chữ to `全品30%OFF!`, hãy lập tức nhìn xuống chữ nhỏ xíu bên dưới xem có ghi `※食品・書籍・セール品は除きます` hay `※会員限定` không!"
            ),
        ],
        "passages": [
            {
                "title": "Văn bản mẫu — Thông báo lớp học cộng đồng (お知らせ)",
                "jp": (
                    "【さくら市民（しみん）センター「春（はる）のパソコン講座（こうざ）」のご案内（あんない）】\n\n"
                    "地域（ちいき）の皆様（みなさま）を対象（たいしょう）に、仕事（しごと）や生活（せいかつ）に役立（やくだ）つパソコン講座（こうざ）を開催（かいさい）します。\n"
                    "● コース・日時（にちじ）：\n"
                    "  ① 基礎（きそ）コース（電源（でんげん）の入（い）れ方（かた）〜文字（もじ）入力（にゅうりょく））：4月10日・17日（水（すい））10:00〜12:00\n"
                    "  ② 表計算（ひょうけいさん）コース（Excel基本（きほん））：4月12日・19日（金（きん））14:00〜16:00\n"
                    "● 対象（たいしょう）：さくら市（し）にお住（す）まい、または市内（しない）の会社（かいしゃ）・学校（がっこう）に通（かよ）っている方（かた）（高校生（こうこうせい）以上（いじょう））。\n"
                    "● 受講料（じゅこうりょう）：各（かく）コース 2,000円（テキスト代（だい）を含（ふく）む）。当日（とうじつ）受付（うけつけ）にてお支払（しはら）いください。\n"
                    "● 申込方法（もうしこみほうほう）：3月25日（月（つき））までに、センター窓口（まどぐち）または公式（こうしき）サイトよりお申（もう）し込（こ）みください。電話（でんわ）での受付（うけつけ）は行（おこな）っておりません。\n"
                    "※ 定員（ていいん）20名（めい）を超（こ）えた場合（ばあい）は抽選（ちゅうせん）となります（先着順（せんちゃくじゅん）ではありません）。\n"
                    "※ 両方（りょうほう）のコースに申（もう）し込（こ）むことも可能（かのう）ですが、別々（べつべつ）に申込書（もうしこみしょ）を提出（ていしゅつ）してください。"
                ),
                "vi": "Thông báo Khóa học Máy tính Mùa xuân — Trung tâm Công dân Sakura: Khóa ① Cơ bản (T4 10:00-12:00); Khóa ② Excel cơ bản (T6 14:00-16:00). Đối tượng: Người sống ở TP Sakura HOẶC đang đi làm/học tại TP Sakura (từ THPT trở lên). Học phí: 2,000 Yên/khóa (đã gồm giáo trình), đóng tại quầy vào ngày học. Cách đăng ký: Trước 25/3 trực tiếp tại quầy hoặc website chính thức (KHÔNG nhận qua điện thoại). ※ Nếu vượt 20 người sẽ bốc thăm chứ KHÔNG xét ai đăng ký trước. ※ Có thể đăng ký cả 2 khóa nhưng phải nộp đơn riêng.",
                "analysis": [
                    "**Bẫy số 1 (`在住` vs `通勤・通学`):** Sống ngoài thành phố nhưng **đang làm việc tại thành phố Sakura** VẪN ĐƯỢC đăng ký (`または市内の会社・学校に通っている方`)!",
                    "**Bẫy số 2 (`電話`):** KHÔNG nhận đăng ký qua điện thoại.",
                    "**Bẫy số 3 (`先着順` vs `抽選`):** Vượt 20 người là bốc thăm (`抽選`), đăng ký sớm chưa chắc trúng!",
                    "**Bẫy số 4 (`テキスト代` & `支払時期`):** 2,000 Yên đã bao gồm sách và đóng **vào ngày đi học**, không đóng lúc nộp đơn."
                ],
                "quiz": [
                    ("この講座（こうざ）に申（もう）し込（こ）むことができる人（ひと）はだれか。", [
                        "さくら市（し）以外（いがい）に住（す）んでいて、他（ほか）の市（し）の会社（かいしゃ）に勤（つと）めている大人（おとな）",
                        "さくら市（し）以外（いがい）に住（す）んでいるが、さくら市内（しない）の大学（だいがく）に通（かよ）う大学生（だいがくせい）",
                        "さくら市内（しない）の小学校（しょうがっこう）に通（かよ）っている小学生（しょうがくせい）",
                        "電話（でんわ）で両方（りょうほう）のコースを一度（いちど）に予約（よやく）したい市民（しみん）"
                    ], 2, "Sinh viên ĐH sống ngoài TP nhưng học tại ĐH trong TP Sakura thỏa mãn cả 2 điều kiện (`市内の学校に通っている` + `高校生以上`) -> Đáp án 2."),
                    ("このお知らせの内容（ないよう）と合（あ）っているものはどれか。", [
                        "受講料（じゅこうりょう）2,000円とは別（べつ）に、教科書（きょうかしょ）のお金（かね）を払（はら）う必要（ひつよう）がある。",
                        "早（はや）く申（もう）し込（こ）んだ人（ひと）から順（じゅん）に20名（めい）が選（えら）ばれる。",
                        "2つのコースを受（う）けたい場合（ばあい）は、1枚（いちまい）の申込書（もうしこみしょ）に両方（りょうほう）書（か）いて出（だ）せばよい。",
                        "受講料（じゅこうりょう）は申込時（もうしこみじ）ではなく、授業（じゅぎょう）の当日（とうじつ）に支払（しはら）う。"
                    ], 4, "Bẫy 1 sai (`テキスト代を含む`); Bẫy 2 sai (`先着順ではありません`); Bẫy 3 sai (`別々に提出`). Đáp án 4 đúng theo `当日受付にてお支払い`!")
                ]
            }
        ]
    },
    {
        "filename": "04_huong-dan-bang-bieu.md",
        "part_label": "実力養成編 第2部 — 広告・お知らせ・説明書きなど（2）",
        "title_jp": "情報を探し出す（3）説明書き・（4）表・リスト",
        "title_vi": "Bài 04 — Đọc Hướng Dẫn Sử Dụng & Biểu Bảng Nhiều Điều Kiện",
        "intro": "Phần tiếp theo của Phần 2 trong **Shinkanzen Master Đọc hiểu N2** luyện đọc **Hướng dẫn kỹ thuật / Cách sử dụng (`説明書き`)** và **Bảng biểu / Danh mục (`表・リスト`)**. Bí quyết ăn trọn điểm ở đây là chuyển hóa chữ thành bảng điều kiện `[Điều kiện ➔ Kết quả / Mức phí]`.",
        "skills": [
            (
                "Kỹ năng đọc（3）説明書き (Hướng dẫn, quy trình, bảo hành)",
                "Cấu trúc thường có 3 khối: 1. Cách làm đúng (`手順`), 2. Lưu ý cấm (`禁止事項・警告`), 3. Cách xử lý lỗi (`故障かなと思ったら`).",
                "Hay thi kiểu: 'Khi máy bị hiện tượng X thì khách hàng nên làm bước nào đầu tiên?' -> Soi thẳng mục X, nhớ loại đáp án bảo tự tháo máy nếu sách cấm (`分解しないでください`)."
            ),
            (
                "Kỹ năng đọc（4）表・リスト (Bảng biểu giá cước, lịch trình, danh sách chọn)",
                "Đọc tiêu đề hàng (dọc) & cột (ngang), cộng thêm **hệ số giảm giá / phụ phí ở các dòng chú thích `注` bên dưới bảng**.",
                "Đừng quên tính **cả chiều đi lẫn tổng thời gian / phụ thu cuối tuần / độ tuổi** nếu nhân vật trong câu hỏi đi 2 người hoặc đi vào Chủ nhật!"
            ),
        ],
        "passages": [
            {
                "title": "Văn bản mẫu — Hướng dẫn & Bảng phí dịch vụ giao hành lý (説明書き＋表)",
                "jp": (
                    "【空港（くうこう）手荷物（てにもつ）配送（はいそう）サービスのご案内（あんない）】\n"
                    "| サイズ（縦＋横＋高さの合計（ごうけい）） | 重（おも）さ上限（じょうげん） | 基本料金（きほんりょうきん）（税込（ぜいこみ）） |\n"
                    "| Sサイズ（120cm以内（いない）） | 15kgまで | 1,800円 |\n"
                    "| Mサイズ（140cm以内（いない）） | 20kgまで | 2,200円 |\n"
                    "| Lサイズ（160cm以内（いない）） | 25kgまで | 2,800円 |\n\n"
                    "■ ご注意（ちゅうい）：\n"
                    "1. サイズか重（おも）さのどちらか一方（いっぽう）でも上限（じょうげん）を超（こ）えた場合（ばあい）は、1つ上（うえ）のサイズの料金（りょうきん）が適用（てきよう）されます（Lサイズを超（こ）えるものは受付不可（うけつけふか））。\n"
                    "2. 土曜・日曜・祝日（しゅくじつ）の配達（はいたつ）は、基本料金（きほんりょうきん）に **＋300円** の追加（ついか）料金（りょうきん）がかかります。\n"
                    "3. 往復（おうふく）で同時（どうじ）にお申（もう）し込（こ）みの場合（ばあい）、合計（ごうけい）金額（きんがく）から **500円割引（わりびき）** いたします。\n"
                    "4. 壊（こわ）れやすいガラス製品（せいひん）や現金（げんきん）・パスポートなどの貴重品（きちょうひん）はお預（あず）かりできません。"
                ),
                "vi": "Bảng giá giao hành lý sân bay: Size S (<=120cm, <=15kg): 1,800 Yên; Size M (<=140cm, <=20kg): 2,200 Yên; Size L (<=160cm, <=25kg): 2,800 Yên. Chú ý: 1) Vượt kích thước HOẶC cân nặng dù chỉ 1 tiêu chí sẽ tính lên 1 bậc (vượt L từ chối nhận); 2) Giao vào T7/CN/Lễ cộng thêm +300 Yên/lượt; 3) Đặt khứ hồi cùng lúc giảm 500 Yên trên tổng tiền; 4) Không nhận đồ thủy tinh dễ vỡ và tiền mặt/hộ chiếu.",
                "analysis": [
                    "**Áp dụng bẫy thực chiến:**",
                    "Giả sử bạn có vali tổng kích thước **115cm** (lọt size S) nhưng nặng **17kg** (vượt mức 15kg của S)! Theo chú ý số 1 (`どちらか一方でも超えた場合は1つ上のサイズ`), vali đó **phải trả giá Size M = 2,200 Yên** chứ không phải S!"
                ],
                "quiz": [
                    ("サイズ合計（ごうけい）115cm・重（おも）さ17kgのスーツケース1つを、日曜日（にちようび）に自宅（じたく）へ片道（かたみち）だけで送（おく）る場合（ばあい）、料金（りょうきん）はいくらか。", [
                        "1,800円",
                        "2,100円",
                        "2,200円",
                        "2,500円"
                    ], 4, "Kích thước 115cm (S) nhưng nặng 17kg (>15kg) -> bị đẩy lên Size M (2,200 Yên). Thêm phí giao ngày Chủ nhật (+300 Yên) -> 2,200 + 300 = 2,500 Yên! Đáp án 4."),
                    ("このサービスで送（おく）ることができない組合（くみあわ）せはどれか。", [
                        "サイズ130cm・重（おも）さ18kgの衣類（いるい）が入（はい）ったカバン",
                        "サイズ150cm・重（おも）さ22kgだが、中（なか）にパソコンが入（はい）っている荷物（にもつ）（貴重品ではない仕事用具）",
                        "サイズ145cm・重（おも）さ27kgのスキー板（いた）入（い）りバッグ",
                        "サイズ110cm・重（おも）さ10kgの食品（しょくひん）（ガラス瓶（びん）ではないもの）"
                    ], 3, "Nặng 27kg vượt ngưỡng tối đa 25kg của Size L -> 受付不可 (không nhận gửi). Đáp án 3.")
                ]
            }
        ]
    }
]

DOKKAI_PART3 = [
    {
        "filename": "01_naiyou-rikai-chubun.md",
        "mondai": "Mondai 11 — 内容理解（中文）",
        "title_jp": "実戦問題 1：内容理解（中文・450〜550字）",
        "title_vi": "Thực Chiến 01 — Đọc Hiểu Nội Dung Trung Văn",
        "intro": "Mở đầu **実力養成編 第3部 実戦問題**, dạng bài **内容理解（中文）** chiếm số câu rất lớn trong kỳ thi JLPT N2 (3 bài trung văn, mỗi bài 3 câu hỏi = 9 câu). Hãy luyện cách đọc theo từng đoạn: **Đoạn 1: Bối cảnh -> Đoạn 2: Vấn đề/Giải thích -> Đoạn 3: Kết luận**.",
        "strategy": [
            "Đọc lướt câu hỏi trước khi lao vào bài đọc để biết chỗ nào có gạch chân (`下線部`) cần dừng lại kỹ.",
            "Thường có 1 câu hỏi từng đoạn và 1 câu cuối (`この文章の内容と合っているもの` hoặc `筆者の考え`) quét toàn bài.",
            "Luôn kiểm tra lỗi **phạm vi** và **nguyên nhân-kết quả** khi so sánh 4 đáp án."
        ],
        "text_title": "Đoạn văn thực chiến N2 —「ほめる」ことと「認（みと）める」こと",
        "passage_jp": (
            "職場（しょくば）や子育て（こそだて）の場面（ばめん）で、「相手（あいて）をほめて伸（の）ばす」ことが大切（たいせつ）だとよく言（い）われる。"
            "もちろん、誰（だれ）かに「すごいね」「えらいね」と言（い）われればうれしくなるものだ。"
            "しかし、ほめることばかりに気（き）を取（と）られると、かえって逆効果（ぎゃくこうか）になる場合（ばあい）もあるという。\n\n"
            "「ほめる」という行為（こうい）は、実（じつ）はほめる側（がわ）が上（うえ）の立場（たちば）に立（た）って相手（あいて）を評価（ひょうか）するという側面（そくめん）を持（も）っている。"
            "たとえば、部下（ぶか）や子ども（こども）がいつも上司（じょうし）や親（おや）にほめられることばかりを期待（きたい）するようになると、「ほめられないならやらない」「失敗（しっぱい）したら評価（ひょうか）が下（さ）がるから挑戦（ちょうせん）しない」という消極的（しょうきょくてき）な態度（たいど）につながりやすい。\n\n"
            "そこで重要（じゅうよう）なのが、単（たん）に評価（ひょうか）としてほめるのではなく、相手（あいて）の行動（こうどう）や変化（へんか）を「認（みと）める」ことである。"
            "「今日（きょう）は昨日（きのう）より丁寧（ていねい）に字（じ）が書（か）けたね」「遅（おそ）くまで資料（しりょう）を準備（じゅんび）してくれて助（たす）かったよ」というように、相手（あいて）が実際（じっさい）に行った（おこな）プロセスや工夫（くふう）に目（め）を向（む）けて言葉（ことば）にして伝（つた）えるのだ。"
            "そうすることで、相手（あいて）は自分（じぶん）の存在（そんざい）が尊重（そんちょう）されていると実感（じっかん）し、自発的（じはつてき）な意欲（いよく）がわいてくるのである。"
        ),
        "passage_vi": "Ở nơi làm việc hay khi nuôi dạy con cái, người ta hay nói việc 'khen để giúp đối phương phát triển' rất quan trọng. Đương nhiên được ai khen 'giỏi quá' sẽ thấy vui. Nhưng nếu chỉ chăm chăm vào việc khen, đôi khi lại gây tác dụng ngược.\n\nHành vi 'khen' thực chất mang khía cạnh người khen đứng ở vị thế bề trên đánh giá đối phương. Chẳng hạn nếu cấp dưới hay con trẻ chỉ trông đợi được sếp hoặc cha mẹ khen, chúng dễ nảy sinh thái độ thụ động kiểu 'không được khen thì chẳng làm' hay 'nếu thất bại sẽ bị hạ đánh giá nên không dám thử thách'.\n\nDo đó điều quan trọng không phải khen đơn thuần như lời đánh giá, mà là 'ghi nhận' hành động và sự thay đổi của đối phương. Tức là hướng ánh nhìn vào quá trình và nỗ lực thực tế mà đối phương đã làm rồi diễn đạt bằng lời như 'Hôm nay con viết chữ nắn nót hơn hôm qua đấy', 'Cảm ơn cậu đã chuẩn bị tài liệu đến muộn nhé'. Nhờ vậy, đối phương cảm nhận được sự tồn tại của mình được tôn trọng và động lực tự phát sẽ dâng lên.",
        "quiz": [
            ("筆者（ひっしゃ）によると、「ほめること」にはどのような問題点（もんだいてん）があるか。", [
                "ほめられた側（がわ）が自信（じしん）を持（も）ちすぎて、他人（たにん）の意見（いけん）を聞（き）かなくなる点（てん）",
                "ほめる側（がわ）が相手（あいて）を評価（ひょうか）する形（かたち）になり、相手（あいて）が失敗（しっぱい）を恐（おそ）れて消極的（しょうきょくてき）になりやすい点（てん）",
                "上司（じょうし）や親（おや）がほめ言葉（ことば）をすぐに見（み）つけられず、コミュニケーションが減（へ）ってしまう点（てん）",
                "ほめられても相手（あいて）はうれしさを感（かん）じないため、信頼（しんらい）関係（かんけい）が築（きず）けない点（てん）"
            ], 2, "Đoạn 2 chỉ ra 2 điểm chính: mang tính đánh giá bề trên và khiến người nghe ngại thất bại/chỉ làm để được khen ->消極的な態度につながりやすい. Đáp án 2."),
            ("筆者（ひっしゃ）が勧（すす）める「認（みと）める」とはどのようなことか。", [
                "結果（けっか）の良（よ）し悪（あ）しだけを厳（きび）しく指摘（してき）して改善（かいぜん）させること",
                "相手（あいて）が工夫（くふう）したことや変化（へんか）、努力（どりょく）した事実（じじつ）を見（み）て言葉（ことば）で伝（つた）えること",
                "相手（あいて）が自分（じぶん）から行動（こうどう）するまで、何（なに）も言（い）わずに黙（だま）って見守（みまも）ること",
                "いつも「すごいね」「えらいね」と大（おお）げさに声（こえ）をかけて励（はげ）ますこと"
            ], 2, "Đoạn 3: `相手が実際に行ったプロセスや工夫に目を向けて言葉にして伝えるのだ` -> Đáp án 2.")
        ]
    },
    {
        "filename": "02_shuchou-rikai-choubun.md",
        "mondai": "Mondai 12 — 主張理解（長文）",
        "title_jp": "実戦問題 2：主張理解（長文・800〜900字）",
        "title_vi": "Thực Chiến 02 — Đọc Hiểu Luận Điểm Trường Văn",
        "intro": "Bài **主張理解（長文）** (Mondai 12) là bài văn dài nhất trong đề N2, nhưng thực tế lại dễ gỡ điểm nếu biết **tìm câu chủ đề từng đoạn** và đọc kỹ **đoạn kết** nơi tác giả tổng hợp lập luận.",
        "strategy": [
            "Mỗi đoạn chỉ đọc 2 câu đầu + 2 câu cuối để lấy ý sườn trước khi giải các câu hỏi cục bộ.",
            "Chú ý mạch chuyển hướng `しかし` / `ところが` ở đầu đoạn giữa bài — nơi tác giả bác bỏ quan điểm thông thường (`一般論`).",
            "Câu hỏi cuối luôn hỏi: `筆者の主張` (Chủ trương xuyên suốt bài) — tránh chọn chi tiết lẻ chỉ xuất hiện ở 1 đoạn."
        ],
        "text_title": "Trường văn thực chiến N2 — 失敗（しっぱい）を「ムダ」で終（お）わらせない社会（しゃかい）へ",
        "passage_jp": (
            "現代（げんだい）社会（しゃかい）では、効率（こうりつ）やスピードが何（なに）よりも重視（じゅうし）され、「最初（さいしょ）から失敗（しっぱい）しないこと」が優秀（ゆうしゅう）さの証（あかし）のように見（み）なされがちである。"
            "就職（しゅうしょく）活動（かつどう）でも新製品（しんせいひん）の開発（かいはつ）でも、一度（いちど）もつまずかずに最短（さいたん）ルートを進（すす）むことが理想（りそう）だと語（かた）られることが多（おお）い。\n\n"
            "しかし、本当（ほんとう）に新しい（あたら）価値（かち）や発見（はっけん）は、計画（けいかく）どおりの成功（せいこう）から生（う）まれるものなのだろうか。"
            "歴史（れきし）を振り返（ふりかえ）ってみれば、世界（せかい）を変（か）えた多（おお）くの発明（はつめい）や研究（けんきゅう）成果（せいか）の陰（かげ）には、数（かぞ）え切（き）れないほどの試行錯誤（しこうさくご）と失敗（しっぱい）があったことがわかる。"
            "失敗（しっぱい）とは、単（たん）なるマイナスや損失（そんしつ）ではない。それは『この方法（ほうほう）ではうまくいかない』という貴重（きちょう）なデータを得（え）たということなのである。\n\n"
            "ところが、日本（にほん）の学校（がっこう）や企業（きぎょう）の多（おお）くでは、失敗（しっぱい）を極端（きょくたん）に恐（おそ）れる空気（くうき）が強（つよ）い。"
            "減点（げんてん）方式（ほうしき）の評価（ひょうか）制度（せいど）の下（もと）では、挑戦（ちょうせん）して失敗（しっぱい）するよりも、無難（ぶなん）にマニュアルどおり動（うご）いてミスを避（さ）けるほうが有利（ゆうり）になってしまうからだ。"
            "その結果（けっか）、誰（だれ）も新（あたら）しい試（こころ）みに手（て）を出（だ）さなくなり、組織（そしき）全体（ぜんたい）の活力（かつりょく）が徐々（じょじょ）に失（うしな）われていく。\n\n"
            "これから私（わたし）たちが目指（めざ）すべきなのは、失敗（しっぱい）を責（せ）めて隠（かく）させる文化（ぶんか）ではなく、なぜ失敗（しっぱい）したかを皆（みな）で共有（きょうゆう）し、次（つぎ）の挑戦（ちょうせん）に生（い）かせる社会（しゃかい）である。"
            "何度（なんど）でもやり直（なお）せる環境（かんきょう）を整（ととの）えてこそ、人（ひと）は初（はじ）めて本当（ほんとう）の意味（み）で創造的（そうぞうてき）になれるのではないだろうか。"
        ),
        "passage_vi": "Trong xã hội hiện đại, hiệu suất và tốc độ được coi trọng hơn hết, khiến việc 'không thất bại ngay từ đầu' dễ bị xem là minh chứng của sự xuất sắc. Dù là tìm việc hay phát triển sản phẩm mới, người ta thường ca ngợi việc đi theo tuyến đường ngắn nhất không một lần vấp ngã là lý tưởng.\n\nThế nhưng, liệu giá trị hay khám phá thực sự mới mẻ có sinh ra từ thành công đúng kế hoạch hay không? Nhìn lại lịch sử, đằng sau nhiều phát minh làm thay đổi thế giới là vô số thử nghiệm sai lầm. Thất bại không đơn thuần là điểm trừ hay tổn thất; nó có nghĩa là ta đã thu được dữ liệu quý giá rằng 'cách làm này không hiệu quả'.\n\nẤy vậy mà ở nhiều trường học và doanh nghiệp Nhật Bản, bầu không khí sợ hãi thất bại quá mức vẫn rất mạnh mẽ. Bởi dưới hệ thống đánh giá trừ điểm, tránh lỗi bằng cách làm an toàn theo sách mẫu lại có lợi hơn việc thử thách rồi thất bại. Hệ quả là không ai dám thử điều mới, và sinh lực của cả tổ chức dần biến mất.\n\nĐiều chúng ta cần hướng tới từ nay không phải văn hóa trách móc khiến người ta giấu giếm thất bại, mà là một xã hội biết cùng nhau chia sẻ nguyên nhân thất bại để ứng dụng cho thử thách tiếp theo. Phải chăng chỉ khi chuẩn bị được môi trường cho phép làm lại nhiều lần, con người mới thực sự trở nên sáng tạo?",
        "quiz": [
            ("筆者（ひっしゃ）は「失敗（しっぱい）」をどのようなものだと考（かんが）えているか。", [
                "最短（さいたん）ルートを進（すす）むために絶対に（ぜったい）避（さ）けるべき損失（そんしつ）",
                "計画（けいかく）を立て（た）る能力（のうりょく）が不足（ふそく）していることを示（しめ）す証拠（しょうこ）",
                "「その方法（ほうほう）はうまくいかない」と教（おし）えてくれる貴重（きちょう）なデータ",
                "優秀（ゆうしゅう）な人（ひと）にはほとんど起（お）きない特別（とくべつ）な出来事（できごと）"
            ], 3, "Đoạn 2 định nghĩa trực tiếp bằng mẫu `〜とは〜である`: `『この方法ではうまくいかない』という貴重なデータを得たということ` -> Đáp án 3."),
            ("減点（げんてん）方式（ほうしき）の評価（ひょうか）制度（せいど）は、どのような結果（けっか）をもたらしていると筆者は述（の）べているか。", [
                "失敗（しっぱい）の原因（げんいん）をみんなで共有（きょうゆう）する習慣（しゅうかん）が広（ひろ）まった。",
                "ミスを恐（おそ）れて新（あたら）しい挑戦（ちょうせん）をしなくなり、組織（そしき）の活力（かつりょく）が失（うしな）われている。",
                "マニュアルどおりに動（うご）く人（ひと）が減（へ）り、創造的（そうぞうてき）な社員（しゃいん）が増（ふ）えた。",
                "仕事（しごと）の効率（こうりつ）やスピードが劇的（げきてき）に向上（こうじょう）した。"
            ], 2, "Đoạn 3: `誰も新しい試みに手を出さなくなり、組織全体の活力が徐々に失われていく` -> Đáp án 2."),
            ("この文章（ぶんしょう）で筆者（ひっしゃ）が最（もっと）も主張（しゅちょう）したいことは何（なに）か。", [
                "失敗（しっぱい）から学（まな）び何度（なんど）でもやり直（なお）せる社会（しゃかい）を作（つく）るべきだ。",
                "企業（きぎょう）の評価（ひょうか）制度（せいど）をすべて廃止（はいし）して、自由（じゆう）に競争（きょうそう）させるべきだ。",
                "歴史（れきし）上（じょう）の発明（はつめい）を学校（がっこう）でもっと詳（くわ）しく教（おし）えるべきだ。",
                "失敗（しっぱい）した人（ひと）は責任（せきにん）を取（と）って組織（そしき）を離（はな）れるべきだ。"
            ], 1, "Đoạn kết khẳng định văn hóa chia sẻ thất bại & môi trường làm lại -> Đáp án 1.")
        ]
    },
    {
        "filename": "03_tougou-rikai.md",
        "mondai": "Mondai 13 — 統合理解（複数文書比較）",
        "title_jp": "実戦問題 3：統合理解（2つの文章を比べる）",
        "title_vi": "Thực Chiến 03 — Đọc Hiểu Tổng Hợp (So Sánh 2 Văn Bản A & B)",
        "intro": "Bài **統合理解** (Mondai 13) yêu cầu đọc cùng lúc 2 bài viết ngắn A và B về cùng 1 chủ đề (ví dụ: nên làm việc từ xa hay đến văn phòng, nên đọc sách giấy hay sách điện tử). Cách nhanh nhất của chị Yuki là kẻ ngay **Ma trận A ⇄ B**: Điểm giống nhau là gì? Điểm khác nhau nằm ở đâu?",
        "strategy": [
            "Đọc Văn bản A -> tóm 1 dòng ngắn bên lề: `[A ủng hộ X vì Lý do 1]`.",
            "Đọc Văn bản B -> tóm 1 dòng: `[B ủng hộ Y / hoặc cũng ủng hộ X nhưng lưu ý điều kiện Z]`.",
            "Dạng câu hỏi kinh điển: `AとBのどちらにも述べられていることはどれか` (Cả A và B đều nói?) và `AとBの考え方の違いは何か` (Khác biệt giữa A và B?)."
        ],
        "text_title": "So sánh A & B — 電子書籍（でんししょせき）と紙（かみ）の本（ほん）",
        "passage_jp": (
            "【文章A】\n"
            "スマートフォンやタブレットで読（よ）める電子（でんし）書籍（しょせき）が急速（きゅうそく）に普及（ふきゅう）している。重（おも）い本（ほん）を何冊（なんさつ）も持（も）ち歩（ある）く必要（ひつよう）がなく、満員（まんいん）電車（でんしゃ）の中（なか）でも片手（かたて）で気軽（きがる）にページをめくれるのは大（おお）きな魅力（みりょく）だ。"
            "文字（もじ）の大（おお）きさを自分（じぶん）の視力（しりょく）に合（あ）わせて変（か）えられる点（てん）も優（すぐ）れている。私（わたし）は今後（こんご）、持ち運び（もちはこ）の便利（べんり）さや保管（ほかん）スペースを取（と）らない点（てん）から、電子書籍（でんししょせき）が読書（どくしょ）の主流（しゅりゅう）になっていくだろうと思（おも）う。\n\n"
            "【文章B】\n"
            "最近（さいきん）、電子書籍（でんししょせき）を利用（りよう）する人（ひと）が増（ふ）え、どこでも手軽（てがる）に読書（どくしょ）が楽（たの）しめるようになったのは喜（よろこ）ばしい。"
            "しかし、長編（ちょうへん）小説（しょうせつ）や専門書（せんもんしょ）をじっくり読（よ）むときには、やはり紙（かみ）の本（ほん）に勝（まさ）るものはない。"
            "紙（かみ）の本（ほん）は『今（いま）全体（ぜんたい）のどのあたりを読（よ）んでいるか』を指（ゆび）の感覚（かんかく）でつかみやすく、前（まえ）のページに戻（もど）って見比（みくら）べるのも簡単（かんたん）だからだ。手軽（てがる）さでは電子（でんし）が有利（ゆうり）だが、理解（りかい）を深（ふか）める読書（どくしょ）には紙（かみ）の本（ほん）が向（む）いている。"
        ),
        "passage_vi": "[Văn bản A]: Sách điện tử đọc trên điện thoại/máy tính bảng đang phổ biến nhanh. Không cần mang vác nhiều sách nặng, trên tàu đông vẫn dễ dàng lật trang bằng một tay và chỉnh cỡ chữ hợp mắt. Tôi cho rằng do tính tiện mang theo và không tốn diện tích lưu trữ, sách điện tử sẽ trở thành xu hướng chủ đạo trong tương lai.\n\n[Văn bản B]: Việc sách điện tử tăng lên giúp mọi người đọc sách dễ dàng ở mọi nơi là điều đáng mừng. Nhưng khi đọc kỹ tiểu thuyết dài hay sách chuyên môn, vẫn không gì bằng sách giấy. Vì sách giấy giúp cảm nhận bằng ngón tay 'mình đang đọc đến đoạn nào của tổng thể' và lật lại đối chiếu rất dễ. Về sự gọn nhẹ thì sách điện tử có lợi thế, nhưng để đọc hiểu sâu thì sách giấy phù hợp hơn.",
        "quiz": [
            ("文章Aと文章Bが共通（きょうつう）して認（みと）めている電子書籍（でんししょせき）の良（よ）さはどれか。", [
                "難（むずか）しい専門書（せんもんしょ）の内容（ないよう）を深（ふか）く理解（りかい）しやすい点（てん）",
                "どこへでも手軽（てがる）に持ち歩（もちある）いて読（よ）むことができる点（てん）",
                "本棚（ほんだな）に並（なら）べてコレクションする楽（たの）しみがある点（てん）",
                "前（まえ）のページにすぐ戻（もど）って確認（かくにん）しやすい点（てん）"
            ], 2, "Văn bản A nói `重い本を持ち歩く必要がなく…手軽`, Văn bản B cũng công nhận `どこでも手軽に読書が楽しめる…手軽さでは電子が有利` -> Đáp án 2."),
            ("紙（かみ）の本（ほん）に対（たい）する文章Bの筆者（ひっしゃ）の考（かんが）えに合（あ）うものはどれか。", [
                "電子（でんし）書籍（しょせき）が普及（ふきゅう）したため、紙（かみ）の本（ほん）は近（ちか）いうちになくなるだろう。",
                "手軽（てがる）に読（よ）みたいときは紙（かみ）の本（ほん）を使（つか）うほうが便利（べんり）だ。",
                "内容（ないよう）をじっくり理解（りかい）したい読書（どくしょ）には、紙（かみ）の本（ほん）のほうが適（てき）している。",
                "紙（かみ）の本（ほん）は文字（もじ）の大（おお）きさを調整（ちょうせい）できないので読（よ）みにくい。"
            ], 3, "Văn bản B: `理解を深める読書には紙の本が向いている` -> Đáp án 3.")
        ]
    },
    {
        "filename": "04_jouhou-kensaku.md",
        "mondai": "Mondai 14 — 情報検索（Tìm kiếm thông tin）",
        "title_jp": "実戦問題 4：情報検索（700字程度の実用文書・時間勝負）",
        "title_vi": "Thực Chiến 04 — Tìm Kiếm Thông Tin Thực Tế (Chốt Điểm Nhanh Trong 3 Phút)",
        "intro": "Bài cuối cùng trong đề thi Đọc hiểu JLPT N2 (**Mondai 14 - 情報検索**) là dạng tờ rơi tuyển dụng, danh sách tour du lịch, hoặc quy định sử dụng thư viện gồm 4-5 gói dịch vụ với nhiều điều kiện chồng chéo. Đây là **câu ăn chắc 100% điểm** nếu em làm đúng trình tự 3 bước của sách **Shinkanzen Master**!",
        "strategy": [
            "**Bước 1:** Đọc kỹ câu hỏi số 1 trước để lấy bộ lọc điều kiện của nhân vật (Ngân sách? Thời gian rảnh? Yêu cầu bắt buộc?).",
            "**Bước 2:** Kẻ bảng loại trừ nhanh từng phương án A/B/C/D trong tờ rơi: cái nào vi phạm 1 điều kiện là **gạch chéo ngay**, không cần đọc hết dòng tiếp theo!",
            "**Bước 3:** Với câu hỏi số 2 (thủ tục nộp hồ sơ / thời hạn), chú ý ngày cuối tuần/giờ đóng cửa/cách gửi bưu điện."
        ],
        "text_title": "Tài liệu thực chiến N2 — あおぞら図書館（としょかん）「夏（なつ）のボランティア募集（ぼしゅう）」",
        "passage_jp": (
            "あおぞら図書館では、活動（かつどう）に参加（さんか）してくれるボランティアを募集（ぼしゅう）しています。\n\n"
            "【活動（かつどう）グループ一覧（いちらん）】\n"
            "| グループ名（めい） | 活動内容（かつどうないよう） | 活動日時（にちじ） | 応募（おうぼ）条件（じょうけん） |\n"
            "| ① 本（ほん）の修理（しゅうり） | 破（やぶ）れた本のテープ貼（は）り・カバーかけ | 毎週水曜（まいしゅうすいよう） 10:00〜12:00 | 特（とく）になし（初心者（しょしんしゃ）歓迎（かんげい）） |\n"
            "| ② 読（よ）み聞（き）かせ | 小学生（しょうがくせい）向（む）けの絵本（えほん）朗読（ろうどく） | 第1・第3土曜（どよう） 14:00〜15:30 | 朗読（ろうどく）経験（けいけん）1年以上（いちねんいじょう） |\n"
            "| ③ 外国語（がいこくご）案内（あんない） | 外国人（がいこくじん）利用者（りようしゃ）への館内（かんない）ガイド | 毎週日曜（にちよう） 13:00〜16:00 | 英語（えいご）またはベトナム語（ご）が話（はな）せる方 |\n"
            "| ④ パソコン入力（にゅうりょく） | 新着（しんちゃく）本のデータ登録（とうろく） | 第2・第4木曜（もくよう） 18:00〜20:00 | 高校生（こうこうせい）以上（いじょう）・Excel操作（そうさ）可（か） |\n\n"
            "■ 共通（きょうつう）ルール・申込方法（もうしこみほうほう）：\n"
            "・交通費（こうつうひ）・報酬（ほうしゅう）の支給（しきゅう）はありません（全活動（ぜんかつどう）無償（むしょう））。\n"
            "・中学生（ちゅうがくせい）以下（いか）は保護者（ほごしゃ）の同意書（どういしょ）が必要（ひつよう）です（④は高校生以上限定（げんてい））。\n"
            "・希望者（きぼうしゃ）は、希望（きぼう）グループの記号（きごう）を書（か）いた申込書（もうしこみしょ）を**7月15日（月・祝）必着（ひっちゃく）**で図書館カウンターへ持参（じさん）するか郵送（ゆうそう）してください。\n"
            "・7月20日（土）10:00から行（おこな）う事前（じぜん）説明会（せつめいかい）への出席（しゅっせき）が必須（ひっす）です（出席（しゅっせき）できない場合（ばあい）は今回（こんかい）参加（さんか）できません）。"
        ),
        "passage_vi": "Thư viện Aozora tuyển tình nguyện viên: Nhóm ① Sửa sách (Thứ 4 10-12h, không yêu cầu điều kiện); Nhóm ② Đọc sách cho thiếu nhi (Thứ 7 tuần 1 & 3, 14-15h30, cần >=1 năm kinh nghiệm đọc diễn cảm); Nhóm ③ Hướng dẫn tiếng nước ngoài (Chủ nhật 13-16h, nói được tiếng Anh hoặc tiếng Việt); Nhóm ④ Nhập liệu máy tính (Thứ 5 tuần 2 & 4, 18-20h, từ THPT trở lên & biết Excel). Quy định chung: Không trả lương/phí đi lại; từ THCS trở xuống cần giấy đồng ý của phụ huynh (nhóm ④ chỉ từ THPT); nộp đơn trực tiếp hoặc gửi bưu điện (đến nơi trễ nhất 15/7); BẮT BUỘC dự buổi hướng dẫn ngày 20/7 lúc 10h sáng.",
        "quiz": [
            ("大学（だいがく）1年生のランさんは、ベトナム語（ご）と英語（えいご）が話（はな）せて、Excelの操作（そうさ）も得意（とくい）だ。平日の昼（ひる）は授業（じゅぎょう）があり、土曜日の午後（ごご）もアルバイトがあるが、日曜日の午後と木曜日の夜（よる）は空（あ）いている。ランさんが応募（おうぼ）できるグループはどれか。", [
                "① と ③",
                "② と ④",
                "③ と ④",
                "③ のみ"
            ], 3, "Soi điều kiện của Lan: Thứ 4 sáng bận học (loại ①); Thứ 7 chiều bận làm thêm + chưa chắc có 1 năm kn (loại ②); Chủ nhật chiều rảnh + biết tiếng Việt/Anh -> khớp ③!; Thứ 5 tối rảnh + SV ĐH (>=THPT) + giỏi Excel -> khớp ④! Vậy chọn đáp án 3 (`③ と ④`)."),
            ("中学（ちゅうがく）2年生の健太（けんた）くんがグループ①に参加（さんか）したい場合（ばあい）、必（かなら）ずしなければならないことはどれか。", [
                "絵本（えほん）の朗読（ろうどく）経験（けいけん）を1年以上（いちねんいじょう）積（つ）むこと",
                "保護者（ほごしゃ）の同意書（どういしょ）を用意（ようい）し、7月15日（じゅうごにち）に投函（とうかん）し、20日の説明会（せつめいかい）に出（で）ること",
                "7月15日（じゅうごにち）までに図書館（としょかん）に届（とど）くように申込書（もうしこみしょ）を出（だ）し、保護者（ほごしゃ）の同意書（どういしょ）とともに出（だ）して、20日の説明会（せつめいかい）に出席（しゅっせき）すること",
                "交通費（こうつうひ）の申請（しんせい）書類（しょるい）をカウンターへ持参（じさん）すること"
            ], 3, "Bẫy `必着` (bưu điện phải ĐẾN NƠI hạn chót ngày 15/7, chứ không phải ngày 15 mới bỏ thùng thư - đáp án 2 sai ở chỗ `15日に投函`!) + HS THCS cần giấy đồng ý phụ huynh + bắt buộc dự họp ngày 20/7 -> Đáp án 3.")
        ]
    }
]
