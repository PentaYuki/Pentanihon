# -*- coding: utf-8 -*-
"""
Dữ liệu Ngữ Pháp Shinkanzen Master N2 (新完全マスター文法 N2)
Phần 1: 文の文法 1 — Bài 01 đến Bài 13
"""

BUNPOU_PART1_A = {
    1: {
        "title_jp": "〜とき・〜直後に",
        "title_vi": "Thời Điểm & Ngay Sau Khi",
        "section": "I. ことがらを説明する",
        "intro": "Bài 01 trong **Shinkanzen Master Ngữ pháp N2** tổng hợp 5 mẫu câu diễn tả **thời điểm thực hiện hành động** và **sự việc xảy ra ngay tức thì sau hành động trước**. Đề thi rất hay cài bẫy về tính lịch sự, tính ý chí và ngôi thứ của chủ ngữ.",
        "patterns": [
            {
                "name": "1. 〜際（さい）（に）",
                "meaning": "Khi / Vào lúc / Nhân dịp... (Cách nói trang trọng, lịch sự của `〜とき`, hay dùng trong thông báo, hướng dẫn, công sở).",
                "connection": "V-る / V-た / N + の + 際（さい）（に / は / には）",
                "examples": [
                    ("チケットをお買（か）い求（もと）めの**際（さい）は**、窓口（まどぐち）でお名前（なまえ）をおっしゃってください。", "Khi mua vé, quý khách vui lòng đọc tên tại quầy giao dịch."),
                    ("この書類（しょるい）は、パスポートを申請（しんせい）する**際（さい）に**必要（ひつよう）となります。", "Tài liệu này sẽ cần thiết khi bạn nộp đơn xin hộ chiếu."),
                ],
                "note": "Chỉ dùng trong văn cảnh trang trọng, lịch sự hoặc thông báo công cộng; không dùng cho sinh hoạt suồng sã hàng ngày."
            },
            {
                "name": "2. 〜に際（さい）して / 〜にあたって",
                "meaning": "Nhân dịp / Trước thềm / Khi bước vào... (Dùng cho các sự kiện đặc biệt, mang tính bước ngoặt một lần như khai trương, kết hôn, du học, khởi nghiệp).",
                "connection": "V-る / N + に際（さい）して（は） / にあたって（は）",
                "examples": [
                    ("新（あたら）しい事業（じぎょう）を始（はじ）める**にあたって**、綿密（めんみつ）な市場（しじょう）調査（ちょうさ）を行（おこな）った。", "Trước thềm khởi sự công việc kinh doanh mới, chúng tôi đã tiến hành khảo sát thị trường kỹ lưỡng."),
                    ("留学（りゅうがく）する**に際（さい）して**、多（おお）くの方々（かたがた）から温（あたた）かい励（はげ）ましをいただいた。", "Nhân dịp đi du học, tôi đã nhận được lời động viên ấm áp từ rất nhiều người."),
                ],
                "note": "`にあたって` mang sắc thái tích cực, chuẩn bị hướng tới tương lai (không dùng cho việc buồn như đám tang); `に際して` dùng trung tính hơn cho sự kiện trang trọng."
            },
            {
                "name": "3. 〜たとたん（に）",
                "meaning": "Vừa mới... thì ngay lập tức... (Hành động B xảy ra bất ngờ ngay khoảnh khắc A vừa dứt).",
                "connection": "V-た + とたん（に）",
                "examples": [
                    ("窓（まど）を開（あ）けた**とたんに**、強（つよ）い風（かぜ）が吹（ふ）き込（こ）んできた。", "Vừa mới mở cửa sổ ra thì gió mạnh liền thổi ùa vào."),
                    ("薬（くすり）を飲（の）んだ**とたん**、急（きゅう）に眠気（ねむけ）が襲（おそ）ってきた。", "Vừa mới uống thuốc xong thì cơn buồn ngủ bất ngờ ập đến."),
                ],
                "note": "BẪY KINH ĐIỂN: Vế sau TUYỆT ĐỐI KHÔNG dùng câu ý chí, mệnh lệnh, rủ rê (`〜よう`, `〜てください`, `〜つもりだ`)."
            },
            {
                "name": "4. 〜（か）と思（おも）うと / 〜（か）と思（おも）ったら",
                "meaning": "Vừa mới thấy... thì đã... / Cứ ngỡ... ai ngờ thoắt cái lại... (Biến đổi chớp nhoáng khiến người nói ngạc nhiên).",
                "connection": "V-た + （か）と思（おも）うと / （か）と思（おも）ったら",
                "examples": [
                    ("赤（あか）ん坊（ぼう）はさっきまで泣（な）いていた**かと思（おも）ったら**、もう笑（わら）っている。", "Em bé vừa mới khóc lúc nãy mà chớp mắt đã cười ngay được rồi."),
                    ("空（そら）が暗（くら）くなった**かと思（おも）うと**、大粒（おおつぶ）の雨（あめ）が降（ふ）り出（だ）した。", "Trời vừa mới sầm tối lại một cái thì mưa nặng hạt đã trút xuống."),
                ],
                "note": "Người nói **quan sát sự vật/người khác**, KHÔNG dùng cho hành động chủ động của chính bản thân mình (✗ `私がドアを開けたかと思うと...`)."
            },
            {
                "name": "5. 〜か〜ないかのうちに",
                "meaning": "Vừa mới... (hoặc chưa kịp dứt hẳn) thì đã... (Hai hành động nối tiếp nhau trong một tích tắc).",
                "connection": "V-る / V-た + か + V-ない + かのうちに",
                "examples": [
                    ("授業（じゅぎょう）終了（しゅうりょう）のベルが鳴（な）る**か鳴（な）らないかのうちに**、学生（がくせい）たちは飛（と）び出（だ）した。", "Chuông báo hết giờ học vừa reo chưa kịp dứt thì sinh viên đã ùa ra ngoài."),
                    ("布団（ふとん）に入（はい）る**か入（はい）らないかのうちに**、眠（ねむ）ってしまった。", "Vừa mới chui vào chăn chưa kịp ấm chỗ thì đã ngủ thiếp đi rồi."),
                ],
                "note": "Hai động từ ở trước `か` và trước `ないかのうちに` phải là **cùng một động từ**."
            },
        ],
        "comparison": [
            ("〜たとたん（に）", "Nhấn mạnh sự bất ngờ ngoài ý muốn ngay sau V-た.", "Dùng được cho chủ ngữ là chính mình (`私が立ったとたん`), nhưng vế sau cấm ý chí/mệnh lệnh."),
            ("〜（か）と思うと", "Nhấn mạnh sự biến đổi trạng thái thoắt cái làm người quan sát ngỡ ngàng.", "KHÔNG dùng cho hành động có chủ đích của bản thân (ngôi thứ nhất)."),
            ("〜か〜ないかのうちに", "Nhấn mạnh hai việc xảy ra gần như đồng thời trong tích tắc.", "Lặp lại cùng 1 động từ (`V-る/た + か + V-ない`)."),
        ],
        "pitfalls": [
            "⚠️ `〜に際して / 〜にあたって` chỉ dùng cho dịp đặc biệt một lần (kết hôn, khai trương, du học). Không dùng cho việc lặp lại hàng ngày như ăn cơm, đi ngủ.",
            "⚠️ `〜たとたん（に）` vế sau không được chứa ý chí (`〜つもりだ`, `〜てください`, `〜よう`).",
            "⚠️ `〜かと思うと` không dùng với chủ ngữ `私（わたし）` khi tự thực hiện hành động."
        ],
        "quiz": [
            ("工場（こうじょう）見学（けんがく）の（　　）、ヘルメットを着用（ちゃくよう）してください。", ["とたん", "際（さい）に", "かと思（おも）うと", "うちに"], 2, "Văn phong thông báo hướng dẫn trang trọng sau danh từ + の -> 際に."),
            ("新店舗（しんてんぽ）のオープン（　　）、近隣（きんりん）の方々（かたがた）へご挨拶（あいさつ）に伺（うかが）った。", ["にあたって", "とたんに", "かと思（おも）ったら", "かのうちに"], 1, "Sự kiện đặc biệt (khai trương) chuẩn bị tiến hành -> にあたって."),
            ("彼（かれ）はベッドに横（よこ）になった（　　）、いびきをかき始（はじ）めた。", ["に際（さい）して", "とたんに", "にあたって", "うちは"], 2, "Hành động B xảy ra ngay lập tức ngoài tầm kiểm soát sau V-た -> とたんに."),
            ("さっきまで晴（は）れていた（　　）、急（きゅう）に雷雨（らいう）になった。", ["に際（さい）して", "かと思（おも）うと", "にあたって", "とたんは"], 2, "Quan sát thời tiết thay đổi nhanh bất ngờ -> かと思うと."),
            ("ベルが（　　）、電車（でんしゃ）のドアが閉（し）まった。", ["鳴（な）るか鳴（な）らないかのうちに", "鳴（な）ったかと思（おも）うなら", "鳴（な）るに際（さい）して", "鳴（な）ったとたんは"], 1, "Mẫu cố định lặp cùng một động từ: V-るかV-ないかのうちに."),
        ]
    },
    2: {
        "title_jp": "〜している",
        "title_vi": "Đang Diễn Ra & Biến Đổi Tiến Triển",
        "section": "I. ことがらを説明する",
        "intro": "Bài 02 trong **Shinkanzen Master Ngữ pháp N2** tập trung vào 6 cấu trúc diễn tả hành động **đang ở cao trào**, **tranh thủ trong lúc còn...**, hoặc **xu hướng biến đổi đang diễn ra** (`〜最中だ`, `〜うちに`, `〜ばかりだ・〜一方だ`, `〜（よ）うとしている`, `〜つつある`, `〜つつ`).",
        "patterns": [
            {
                "name": "1. 〜最中（さいちゅう）だ / 〜最中（さいちゅう）に",
                "meaning": "Đúng lúc đang (ở giữa cao trào của hành động/sự kiện)... thì có chuyện xen vào.",
                "connection": "V-ている / N + の + 最中（さいちゅう）だ / 最中（さいちゅう）に",
                "examples": [
                    ("重要（じゅうよう）な会議（かいぎ）の**最中（さいちゅう）に**、携帯電話（けいたいでんわ）が鳴（な）ってしまった。", "Đúng ngay giữa cuộc họp quan trọng thì điện thoại lại reo lên."),
                    ("食事（しょくじ）をして**いる最中（さいちゅう）に**、地震（じしん）が起（お）きた。", "Đúng lúc đang ăn cơm thì động đất xảy ra."),
                ],
                "note": "Thường đi với các danh từ chỉ hành động/sự kiện có quá trình kéo dài (`会議・試合・テスト・食事`). Không dùng với việc diễn ra tức thời (✗ `起きている最中に`)."
            },
            {
                "name": "2. 〜うちに",
                "meaning": "1) Trong lúc trạng thái A còn chưa thay đổi thì tranh thủ làm B; 2) Trong suốt lúc làm A thì tự nhiên dẫn đến biến đổi B.",
                "connection": "V-る / V-ている / V-ない / Aい / Naな / Nの + うちに",
                "examples": [
                    ("料理（りょうり）が温（あたた）かい**うちに**、早（はや）く食（た）べましょう。", "Tranh thủ lúc đồ ăn còn nóng, chúng ta mau ăn đi thôi."),
                    ("何度（なんど）も練習（れんしゅう）して**いるうちに**、自然（しぜん）と話（はな）せるようになった。", "Trong quá trình luyện tập nhiều lần, tự nhiên tôi đã nói được trôi chảy."),
                ],
                "note": "Ở nghĩa (1) vế sau là hành động có ý chí tranh thủ trước khi muộn; ở nghĩa (2) vế trước thường là `V-ている` và vế sau là biến đổi tự nhiên không chủ đích."
            },
            {
                "name": "3. 〜ばかりだ / 〜一方（いっぽう）だ",
                "meaning": "Ngày càng... / Cứ thế tiến triển theo một chiều hướng (thường không dừng lại).",
                "connection": "V-る（động từ chỉ sự thay đổi: 増える・減る・悪くなる...） + ばかりだ / 一方（いっぽう）だ",
                "examples": [
                    ("最近（さいきん）、物価（ぶっか）は上（あ）がる**一方（いっぽう）だ**。", "Dạo gần đây vật giá cứ tăng vùn vụt theo một chiều."),
                    ("運動（うんどう）不足（ぶそく）で体重（たいじゅう）は増（ふ）える**ばかりだ**。", "Vì thiếu vận động nên cân nặng cứ thế tăng lên mãi."),
                ],
                "note": "`〜ばかりだ` gần như luôn mang sắc thái **tiêu cực/lo ngại** của người nói; `〜一方だ` dùng được cả cho sự tăng/giảm mang tính khách quan nhưng cũng thường là xu hướng đáng lo."
            },
            {
                "name": "4. 〜（よ）うとしている",
                "meaning": "Đang định / Sắp sửa bắt đầu (ngay thời điểm chuyển từ chưa làm sang làm, hoặc hiện tượng tự nhiên sắp bộc phát).",
                "connection": "V-よう（thể ý chí） + としている",
                "examples": [
                    ("ちょうど出（で）かけ**ようとしていた**ところに、友達（ともだち）が訪（たず）ねてきた。", "Đúng lúc tôi vừa sửa soạn bước ra khỏi nhà thì bạn lại ghé thăm."),
                    ("桜（さくら）の花（はな）が今（いま）まさに咲（さ）**こうとしている**。", "Những bông hoa anh đào ngay lúc này sắp sửa bung nở."),
                ],
                "note": "Không chỉ dùng cho ý chí con người mà còn dùng cho hiện tượng tự nhiên sắp xảy ra (`日が沈もうとしている`)."
            },
            {
                "name": "5. 〜つつある",
                "meaning": "Đang dần dần (biến đổi từng bước một cách rõ rệt — văn viết trang trọng).",
                "connection": "V-ます（bỏ ます） + つつある",
                "examples": [
                    ("地球（ちきゅう）の温暖化（おんだんか）は、確実（かくじつ）に進（すす）み**つつある**。", "Sự nóng lên toàn cầu đang tiến triển dần một cách chắc chắn."),
                    ("景気（けいき）は徐々（じょじょ）に回復（かいふく）し**つつある**ようだ。", "Có vẻ như nền kinh tế đang dần từng bước phục hồi."),
                ],
                "note": "Chỉ kết hợp với động từ chỉ sự biến đổi (`変わる・増える・回復する`). Không dùng cho hành động nhất thời (✗ `ご飯を食べつつある`)."
            },
            {
                "name": "6. 〜つつ",
                "meaning": "Vừa... vừa... (thực hiện hai hành động đồng thời; mang sắc thái văn viết trang trọng hơn `ながら`).",
                "connection": "V-ます（bỏ ます） + つつ",
                "examples": [
                    ("将来（しょうらい）のことを考（かんが）え**つつ**、今（いま）できることに全力を注（そそ）ぐ。", "Vừa suy nghĩ về tương lai, vừa dồn toàn lực vào những việc có thể làm ngay lúc này."),
                    ("先生（せんせい）の説明（せつめい）を聞（き）き**つつ**、ノートにメモを取（と）った。", "Tôi vừa lắng nghe lời giảng của thầy vừa ghi chép vào vở."),
                ],
                "note": "Phân biệt với Bài 14 `〜つつ（も）`: ở Bài 02 là hai hành động song song (đồng thời), còn ở Bài 14 là nhượng bộ \"dù biết là... nhưng vẫn...\"."
            },
        ],
        "comparison": [
            ("〜最中に", "Ngay giữa cao trào của hành động/sự kiện kéo dài thì có việc bất ngờ chen vào.", "Vế sau thường là sự cố ngoài ý muốn xen ngang."),
            ("〜うちに", "Trong khi trạng thái A còn giữ nguyên -> tranh thủ làm B.", "Vế trước hay dùng với tính từ hoặc thể phủ định `暗くならないうちに`."),
            ("〜ばかりだ / 〜一方だ", "Xu hướng biến đổi một chiều.", "`ばかりだ` thiên về đánh giá tiêu cực; không dùng động từ nhất thời."),
            ("〜つつある", "Đang trong quá trình biến đổi dần dần (văn viết).", "Không dùng với động từ hành động đơn thuần như `食べる・読む`."),
        ],
        "pitfalls": [
            "⚠️ Không nhầm `〜つつ` (vừa làm A vừa làm B — Bài 02) với `〜つつ（も）` (tuy A nhưng vẫn B — Bài 14).",
            "⚠️ `〜最中に` không đứng sau động từ khoảnh khắc (✗ `家に着いた最中に`).",
            "⚠️ `〜つつある` chỉ đi với động từ mang tính biến đổi theo thời gian (`増加する`, `消える`, `変化する`)."
        ],
        "quiz": [
            ("せっかくの料理（りょうり）が冷（さ）めない（　　）、どうぞ召（め）し上（あ）がってください。", ["最中（さいちゅう）に", "うちに", "一方（いっぽう）だ", "つつある"], 2, "Tranh thủ khi đồ ăn còn chưa nguội -> V-ない + うちに."),
            ("新（あたら）しい技術（ぎじゅつ）の導入（どうにゅう）により、作業（さぎょう）効率（こうりつ）は改善（かいぜん）され（　　）。", ["つつある", "最中（さいちゅう）だ", "ようとしている", "うちに"], 1, "Quá trình cải thiện đang dần tiến triển trong văn viết -> つつある."),
            ("会議（かいぎ）の（　　）、突然（とつぜん）停電（ていでん）になってしまった。", ["うちに", "最中（さいちゅう）に", "ばかりに", "つつ"], 2, "Đúng giữa lúc cuộc họp đang diễn ra thì mất điện -> 最中に."),
            ("スマートフォンが普及（ふきゅう）してから、漢字（かんじ）を手書（てが）きする機会（きかい）は減（へ）る（　　）。", ["一方（いっぽう）だ", "最中（さいちゅう）だ", "つつ", "うちに"], 1, "Xu hướng suy giảm liên tục theo một chiều -> 減る一方だ."),
            ("ちょうど家（いえ）を出（で）（　　）ところに、宅配便（たくはいびん）が届（とど）いた。", ["ようとしていた", "つつあった", "ばかりだった", "最中（さいちゅう）だった"], 1, "Đúng lúc sắp sửa bước ra ngoài -> V-ようとしていた."),
        ]
    },
    3: {
        "title_jp": "〜後で",
        "title_vi": "Sau Khi & Trình Tự Hoàn Tất",
        "section": "I. ことがらを説明する",
        "intro": "Bài 03 trong **Shinkanzen Master Ngữ pháp N2** gom các cấu trúc biểu thị **sau khi một việc xảy ra/hoàn tất** mới dẫn tới hành động, nhận thức hoặc điều kiện tiên quyết tiếp theo (`〜てはじめて`, `〜上（で）`, `〜次第`, `〜て以来・〜てこのかた`, `〜てからでないと`).",
        "patterns": [
            {
                "name": "1. 〜てはじめて",
                "meaning": "Chỉ sau khi trải qua... thì lần đầu tiên mới nhận ra / mới làm được... (Nhấn mạnh sự thay đổi nhận thức sau mốc trải nghiệm).",
                "connection": "V-て + はじめて",
                "examples": [
                    ("病気（びょうき）になって**はじめて**、健康（けんこう）の大切（たいせつ）さが分（わ）かった。", "Chỉ sau khi bị ốm rồi tôi mới thấm thía được tầm quan trọng của sức khỏe."),
                    ("親（おや）になって**はじめて**、両親（りょうしん）の苦労（くろう）に気（き）づいた。", "Chỉ đến khi tự mình làm cha mẹ thì mới nhận ra nỗi vất vả của đấng sinh thành."),
                ],
                "note": "Thường đi với các động từ nhận thức, cảm ngộ ở vế sau (`分かる・気づく・知る`). Không dùng cho chuỗi hành động đơn thuần kiểu ✗ `起きてはじめて朝ご飯を食べる`."
            },
            {
                "name": "2. 〜上（うえ）（で）",
                "meaning": "Sau khi đã chuẩn bị/hoàn thành kỹ bước A rồi mới tiến hành bước B.",
                "connection": "V-た / N（danh động từ）+ の + 上（うえ）（で）",
                "examples": [
                    ("内容（ないよう）をよく確認（かくにん）した**上（うえ）で**、契約書（けいやくしょ）にサインしてください。", "Sau khi kiểm tra thật kỹ nội dung, xin hãy ký vào hợp đồng."),
                    ("家族（かぞく）と相談（そうだん）の**上（うえ）**、転職（てんしょく）を決意（けつい）した。", "Sau khi bàn bạc kỹ lưỡng với gia đình, tôi đã quyết tâm chuyển việc."),
                ],
                "note": "Nhấn mạnh A là bước chuẩn bị có chủ đích làm tiền đề cho quyết định/hành động B ở vế sau. Phân biệt với `〜上に` (hơn nữa, Bài 06) và `〜上で` (về mặt..., trong quá trình...)."
            },
            {
                "name": "3. 〜次第（しだい）",
                "meaning": "Ngay sau khi (A hoàn tất/có kết quả) thì sẽ lập tức làm B.",
                "connection": "V-ます（bỏ ます） + 次第（しだい）",
                "examples": [
                    ("詳（くわ）しい日程（にってい）が決（き）まり**次第（しだい）**、ご連絡（れんらく）いたします。", "Ngay sau khi lịch trình cụ thể được chốt, tôi sẽ lập tức liên lạc với anh/chị."),
                    ("準備（じゅんび）が整（ととの）い**次第（しだい）**、会議（かいぎ）を始（はじ）めます。", "Ngay sau khi công tác chuẩn bị hoàn tất, chúng tôi sẽ bắt đầu cuộc họp."),
                ],
                "note": "Vế sau LUÔN là hành động có ý chí hướng về tương lai/hiện tại của người nói (`連絡します`, `始めます`). KHÔNG chia quá khứ ở vế sau (✗ `着き次第、電話した`)!"
            },
            {
                "name": "4. 〜て以来（いらい） / 〜てこのかた",
                "meaning": "Kể từ sau khi... đến tận bây giờ (trạng thái tiếp diễn liên tục không đổi suốt một khoảng thời gian dài).",
                "connection": "V-て + 以来（いらい） / このかた（cũng có `N + 以来`）",
                "examples": [
                    ("日本（にほん）へ来（き）て**以来（いらい）**、一度（いちど）も国（くに）へ帰（かえ）っていない。", "Kể từ khi sang Nhật đến giờ, tôi vẫn chưa về nước lấy một lần."),
                    ("あの事故（じこ）に遭（あ）って**このかた**、車（くるま）を運転（うんてん）するのが怖（こわ）くなった。", "Kể từ sau khi gặp vụ tai nạn đó đến nay, tôi đâm ra sợ lái xe."),
                ],
                "note": "Không dùng cho sự việc mới xảy ra tức thời vài phút trước (✗ `朝起きて以来`). Phải là một mốc thời gian tương đối xa đến hiện tại."
            },
            {
                "name": "5. 〜てからでないと / 〜てからでなければ",
                "meaning": "Nếu không làm A trước rồi mới... thì không thể làm B (A là điều kiện tiên quyết bắt buộc trước khi làm B).",
                "connection": "V-て + からでないと / からでなければ + (vế sau phủ định)",
                "examples": [
                    ("実物（じつぶつ）を見（み）て**からでないと**、買（か）うかどうか決（き）められない。", "Nếu không xem tận mắt sản phẩm trước thì tôi không thể quyết định có mua hay không."),
                    ("宿題（しゅくだい）を終（お）わらせて**からでなければ**、遊（あそ）びに行（い）ってはいけません。", "Nếu chưa làm xong bài tập trước thì con không được phép đi chơi."),
                ],
                "note": "Vế sau luôn mang ý nghĩa phủ định hoặc không thể (`〜ない`, `〜られない`, `〜てはいけない`)."
            },
        ],
        "comparison": [
            ("〜てはじめて", "Trải qua A mới ngộ ra / lần đầu làm B (thường quá khứ).", "Vế sau hay đi với động từ nhận thức (`分かった`, `気づいた`)."),
            ("〜上（うえ）で", "Sau khi chuẩn bị/xem xét kỹ bước A mới làm B.", "Luôn dùng `V-た` hoặc `Nの`, khác với `〜上に` (thêm vào đó)."),
            ("〜次第（しだい）", "Ngay khi A vừa xong là lập tức làm B (tương lai).", "Vế sau là ý chí/kế hoạch, KHÔNG chia quá khứ."),
            ("〜てからでないと", "Phải xong A trước thì mới có thể làm B.", "Vế sau mang tính phủ định / cấm đoán / không thể."),
        ],
        "pitfalls": [
            "⚠️ Không bao giờ dùng thì quá khứ sau `〜次第` (✗ `東京に着き次第、連絡した` -> phải sửa thành `着いたらすぐ連絡した`).",
            "⚠️ Phân biệt `〜上（うえ）で` (sau khi làm gì — Bài 03) với `〜上（うえ）に` (hơn nữa — Bài 06) và `〜上（うえ）は` (một khi đã... — Bài 17)."
        ],
        "quiz": [
            ("詳（くわ）しい結果（けっか）が（　　）次第（しだい）、皆様（みなさま）にお知（し）らせいたします。", ["分（わ）かり", "分（わ）かって", "分（わ）かる", "分（わ）かった"], 1, "Cấu trúc `V-ます (bỏ ます) + 次第` -> 分かり次第."),
            ("実際（じっさい）に一人（ひとり）暮（ぐ）らしを始め（　　）、親（おや）のありがたみが分（わ）かった。", ["てはじめて", "てこのかた", "た上（うえ）で", "次第（しだい）"], 1, "Sau khi trải nghiệm mới thấu hiểu ra -> てはじめて."),
            ("責任者（せきにんしゃ）に確認（かくにん）して（　　）、勝手（かって）に返事（へんじ）をすることはできない。", ["からでないと", "以来（いらい）", "はじめて", "上（うえ）で"], 1, "Nếu chưa xác nhận trước thì không thể trả lời -> てからでないと."),
            ("大学（だいがく）を卒業（そつぎょう）して（　　）、彼女（かのじょ）とは一度（いちど）も会（あ）っていない。", ["以来（いらい）", "上（うえ）で", "次第（しだい）", "からでないと"], 1, "Từ cột mốc tốt nghiệp đến tận bây giờ -> て以来."),
            ("双方（そうほう）でよく話（はな）し合（あ）った（　　）、結論（けつろん）を出（だ）しましょう。", ["上（うえ）で", "次第（しだい）", "てはじめて", "以来（いらい）"], 1, "Sau khi bàn bạc kỹ lưỡng làm tiền đề -> V-た + 上で."),
        ]
    },
    4: {
        "title_jp": "範囲の始まりと終わり・その間",
        "title_vi": "Khởi Điểm, Phạm Vi & Giới Hạn Suốt Khoảng",
        "section": "I. ことがらを説明する",
        "intro": "Bài 04 trong **Shinkanzen Master Ngữ pháp N2** tổng hợp các cấu trúc chỉ **điểm bắt đầu tiêu biểu, phạm vi trải dài trong không gian/thời gian, và giới hạn tối đa** (`〜をはじめ`, `〜からして`, `〜にわたって`, `〜を通じて・〜を通して`, `〜限り`, `〜だけ`).",
        "patterns": [
            {
                "name": "1. 〜をはじめ（として）",
                "meaning": "Trước hết phải kể đến là... / Tiêu biểu là... (Đưa ra đại diện nổi bật nhất trong một nhóm cùng loại).",
                "connection": "N + をはじめ（として） / をはじめとする + N",
                "examples": [
                    ("日本（にほん）には富士山（ふじさん）**をはじめ**、多（おお）くの美（うつく）しい山々（やまやま）がある。", "Ở Nhật Bản, tiêu biểu phải kể đến núi Phú Sĩ cùng rất nhiều ngọn núi đẹp khác."),
                    ("東京（とうきょう）**をはじめとする**大都市（だいとし）では、交通（こうつう）網（もう）が発達（はったつ）している。", "Tại các thành phố lớn, đứng đầu là Tokyo, mạng lưới giao thông rất phát triển."),
                ],
                "note": "Từ đứng trước luôn là ví dụ tiêu biểu, đại diện nổi tiếng nhất; vế sau thường có `多くの〜`, `さまざまな〜`, `など`."
            },
            {
                "name": "2. 〜からして",
                "meaning": "Ngay từ... đã... (Lấy một điểm cơ bản/nhỏ nhất làm dẫn chứng, thường để chê toàn bộ hoặc làm căn cứ suy đoán).",
                "connection": "N + からして",
                "examples": [
                    ("彼（かれ）は挨拶（あいさつ）の態度（たいど）**からして**失礼（しつれい）だ。", "Anh ta ngay từ thái độ chào hỏi cơ bản đã thấy bất lịch sự rồi."),
                    ("この店（みせ）は看板（かんばん）の文字（もじ）**からして**古（ふる）びた雰囲気（ふんいき）がある。", "Quán này ngay từ nét chữ trên biển hiệu đã toát lên vẻ cổ kính."),
                ],
                "note": "Thường mang hàm ý chê bai từ chi tiết sơ đẳng (`〜からしてだめだ`), hoặc dùng căn cứ giác quan để đánh giá."
            },
            {
                "name": "3. 〜にわたって / 〜にわたり / 〜にわたる",
                "meaning": "Suốt... / Trải rộng khắp... (Nhấn mạnh độ dài thời gian, độ rộng không gian hoặc số lần lớn).",
                "connection": "N（khoảng thời gian/không gian/số lượng lớn）+ にわたって / にわたり / にわたる + N",
                "examples": [
                    ("台風（たいふう）の影響（えいきょう）で、3日間（みっかかん）**にわたって**大雨（おおあめ）が続（つづ）いた。", "Do ảnh hưởng của bão, mưa lớn đã kéo dài suốt 3 ngày liền."),
                    ("関東（かんとう）地方（ちほう）の全域（ぜんいき）**にわたる**停電（ていでん）が発生（はっせい）した。", "Đã xảy ra sự cố mất điện trên diện rộng toàn vùng Kanto."),
                ],
                "note": "KHÔNG dùng cho phạm vi quá nhỏ hẹp (✗ `5分間にわたって待つ`)."
            },
            {
                "name": "4. 〜を通（つう）じて / 〜を通（とお）して",
                "meaning": "1) Suốt một chu kỳ thời gian không gián đoạn; 2) Thông qua phương tiện/người trung gian.",
                "connection": "N + を通（つう）じて / を通（とお）して",
                "examples": [
                    ("この地方（ちほう）は一年（いちねん）**を通（つう）じて**温暖（おんだん）な気候（きこう）だ。", "Vùng này quanh năm suốt 4 mùa đều có khí hậu ấm áp."),
                    ("友人（ゆうじん）**を通（とお）して**、彼女（かのじょ）と知（し）り合（あ）うことができた。", "Thông qua một người bạn, tôi đã quen biết được cô ấy."),
                ],
                "note": "`を通じて` thiên về thời gian liên tục hoặc sự việc tự nhiên; `を通して` hay dùng khi có chủ ý thông qua người/kênh trung gian."
            },
            {
                "name": "5. 〜限（かぎ）り",
                "meaning": "Toàn bộ / Hết mức có thể trong phạm vi...",
                "connection": "V-る（できる・ある・知力...） / N + の + 限（かぎ）り",
                "examples": [
                    ("今（いま）の私（わたし）にできる**限（かぎ）り**のことをやってみよう。", "Tôi sẽ thử làm hết sức tất cả những gì mình có thể làm hiện nay."),
                    ("力（ちから）の**限（かぎ）り**走（はし）ったが、終電（しゅうでん）に間（ま）に合（あ）わなかった。", "Tôi đã chạy hết sức bình sinh nhưng vẫn không kịp chuyến tàu cuối."),
                ],
                "note": "Trong Bài 04 nhấn mạnh nghĩa \"dốc toàn lực, toàn bộ phạm vi tối đa\" (`声の限り`, `できる限り`). Nghĩa điều kiện/giới hạn tiếp tục được học ở Bài 05."
            },
            {
                "name": "6. 〜だけ",
                "meaning": "Hết mức / Toàn bộ số lượng có thể...",
                "connection": "V-る（khả năng: できる・ある・ほしい...） + だけ",
                "examples": [
                    ("引（ひ）っ越（こ）しに必要（ひつよう）な荷物（にもつ）は、できる**だけ**少（すく）なくしたい。", "Hành lý cần cho việc chuyển nhà, tôi muốn giảm thiểu ít nhất có thể."),
                    ("好（す）きな**だけ**食（た）べていいですよ。", "Cậu cứ ăn thoải mái bao nhiêu tùy thích nhé."),
                ],
                "note": "Hay dùng trong các cụm `できるだけ`, `言いたいだけ言う`, `あるだけ全部`."
            },
        ],
        "comparison": [
            ("〜にわたって", "Nhấn mạnh quy mô lớn, kéo dài về thời gian/không gian (`3年間`, `全国`).", "Không dùng cho khoảng nhỏ vài phút."),
            ("〜を通じて", "Nhấn mạnh tính liên tục suốt một chu kỳ (`四季を通じて`, `一生を通じて`) hoặc qua trung gian.", "Ít nhấn mạnh độ rộng hoành tráng bằng `にわたって`."),
            ("〜をはじめ", "Đưa ví dụ đại diện tiêu biểu tích cực/lớn.", "Danh từ sau thường mang tính tổng hợp (`多くの〜`, `さまざまな〜`)."),
            ("〜からして", "Đưa ví dụ nhỏ/sơ đẳng để đánh giá toàn bộ (thường chê).", "Hay kèm `まして〜はなおさら`."),
        ],
        "pitfalls": [
            "⚠️ Nhớ kỹ danh từ đi với `〜にわたって` phải là từ chỉ quy mô/thời lượng lớn (`数ヶ月`, `広範囲`, `数十回`).",
            "⚠️ Không nhầm `〜からして` (ngay từ cái cơ bản đã... -> chê) với `〜をはじめ` (tiêu biểu là... -> liệt kê tích cực)."
        ],
        "quiz": [
            ("日本（にほん）には、京都（きょうと）（　　）、古（ふる）いお寺（てら）が多（おお）い地域（ちいき）がたくさんある。", ["をはじめ", "からして", "にわたって", "かぎりに"], 1, "Nêu Kyoto làm đại diện tiêu biểu nhất -> をはじめ."),
            ("あの新入（しんにゅう）社員（しゃいん）は、言葉遣（ことばづか）い（　　）全（まった）くなっていない。", ["をはじめ", "からして", "を通じて", "にわたって"], 2, "Ngay từ lời ăn tiếng nói cơ bản đã tệ -> からして."),
            ("調査（ちょうさ）は過去（かこ）10年間（じゅうねんかん）（　　）詳（くわ）しく行（おこな）われた。", ["にわたって", "からして", "をはじめ", "だけに"], 1, "Khoảng thời gian kéo dài suốt 10 năm -> にわたって."),
            ("この動物園（どうぶつえん）は、一年（いちねん）（　　）毎日（まいにち）開園（かいえん）している。", ["を通（つう）じて", "をはじめ", "からして", "につれて"], 1, "Suốt cả chu kỳ 1 năm không gián đoạn -> を通じて."),
            ("大会（たいかい）では、自分（じぶん）の力（ちから）の（　　）悔（く）いのないように戦（たたか）った。", ["限（かぎ）り", "からして", "ばかり", "ほど"], 1, "Dốc hết toàn bộ sức lực: 力の限り."),
        ]
    },
    5: {
        "title_jp": "〜だけ",
        "title_vi": "Giới Hạn & Duy Nhất (Chỉ... / Chừng Nào...)",
        "section": "I. ことがらを説明する",
        "intro": "Bài 05 trong **Shinkanzen Master Ngữ pháp N2** đi sâu vào các sắc thái giới hạn của chữ **限（かぎ）** (`〜に限り`, `〜限り（は）`, `〜限りでは`, `〜に限って`). Đây là 4 mẫu cực dễ nhầm lẫn trong Mondai 7!",
        "patterns": [
            {
                "name": "1. 〜に限（かぎ）り",
                "meaning": "Chỉ giới hạn trong đối tượng/thời gian/số lượng đặc biệt này thôi (rất hay gặp trong thông báo, quảng cáo, ưu đãi).",
                "connection": "N + に限（かぎ）り",
                "examples": [
                    ("本日（ほんじつ）**に限（かぎ）り**、全品（ぜんぴん）20％引（び）きで販売（はんばい）いたします。", "Chỉ duy nhất hôm nay, toàn bộ mặt hàng được giảm giá 20%."),
                    ("女性（じょせい）のお客様（きゃくさま）**に限（かぎ）り**、ドリンクを1杯（いっぱい）サービスします。", "Chỉ riêng quý khách nữ được tặng miễn phí 1 đồ uống."),
                ],
                "note": "Thường đi với thời gian/đối tượng cụ thể trong bảng tin (`初回に限り`, `会員に限り`, `雨の日に限り`)."
            },
            {
                "name": "2. 〜限（かぎ）り（は）",
                "meaning": "Chừng nào mà trạng thái này còn duy trì thì... vẫn... (Giới hạn điều kiện kéo dài).",
                "connection": "V-る / V-ている / V-ない / Aい / Naな / Nである + 限（かぎ）り（は）",
                "examples": [
                    ("私（わたし）が生きている**限（かぎ）り（は）**、家族（かぞく）を守（まも）り抜（ぬ）くつもりだ。", "Chừng nào tôi còn sống trên đời này, tôi quyết tâm bảo vệ gia đình đến cùng."),
                    ("無理（むり）なスケジュールを変更（へんこう）しない**限（かぎ）り**、この計画（けいかく）は成功（せいこう）しないだろう。", "Chừng nào chưa thay đổi lịch trình bất hợp lý kia thì kế hoạch này khó mà thành công."),
                ],
                "note": "`V-ない限り` tương đương \"trừ phi... nếu không thì...\". Vế sau mang tính duy trì trạng thái hoặc dự đoán chắc chắn."
            },
            {
                "name": "3. 〜限（かぎ）りでは",
                "meaning": "Trong phạm vi (những gì tôi biết / nghe / thấy / điều tra được) thì...",
                "connection": "V-る / V-ている / V-た（động từ tri giác/thông tin: 知る・見る・聞く・調べる...） / Nの + 限（かぎ）りでは",
                "examples": [
                    ("私（わたし）が知（し）っている**限（かぎ）りでは**、彼（かれ）が遅刻（ちこく）したことは一度（いちど）もない。", "Trong phạm vi những gì tôi biết, cậu ấy chưa từng đi muộn lần nào."),
                    ("新聞（しんぶん）で読（よ）んだ**限（かぎ）りでは**、新（あたら）しい制度（せいど）は来月（らいげつ）から始（はじ）まるそうだ。", "Theo phạm vi những gì tôi đọc trên báo thì chế độ mới sẽ bắt đầu từ tháng sau."),
                ],
                "note": "Luôn đứng sau động từ nhận thức thông tin (`知る・見る・聞く・調べる・記憶する`) và thường có trợ từ `では`."
            },
            {
                "name": "4. 〜に限（かぎ）って",
                "meaning": "1) Đúng lúc/đúng ngày... thì lại gặp chuyện xui xẻo; 2) Riêng người/vật đó thì chắc chắn không làm chuyện xấu đâu.",
                "connection": "N / V-る・V-ている + 時（とき） + に限（かぎ）って",
                "examples": [
                    ("傘（かさ）を持（も）っていない日（ひ）**に限（かぎ）って**、急（きゅう）に雨（あめ）が降（ふ）り出（だ）すものだ。", "Cứ đúng cái hôm không mang theo ô thì trời lại đổ mưa bất chợt mới xui chứ."),
                    ("まじめな田中（たなか）さん**に限（かぎ）って**、そんな無責任（むせきにん）なことはしないはずだ。", "Riêng anh Tanaka nghiêm túc thì chắc chắn không bao giờ làm chuyện vô trách nhiệm như vậy."),
                ],
                "note": "Có 2 nghĩa hoàn toàn khác nhau: nghĩa (1) luôn đi với sự cố trớ trêu (\"đúng lúc đang vội thì lại...\"); nghĩa (2) luôn đi với phủ định khẳng định niềm tin (`〜ないはずだ`)."
            },
        ],
        "comparison": [
            ("〜に限り", "Thông báo giới hạn ưu đãi/quy định (`本日限り`, `会員に限り`).", "Chỉ đi sau danh từ."),
            ("〜限り（は）", "Điều kiện duy trì \"chừng nào còn...\" / \"nếu không...\".", "Dùng với `V-ている`, `V-ない`, `Nである`."),
            ("〜限りでは", "Giới hạn nguồn thông tin (`私の知る限りでは`).", "Chỉ đi với động từ biết/nghe/thấy/tra cứu."),
            ("〜に限って", "Đúng lúc... thì lại xui / Riêng... thì chắc chắn không.", "Coi chừng nhầm với `に限らず` (Bài 06 — không chỉ riêng)."),
        ],
        "pitfalls": [
            "⚠️ Đừng nhầm cặp `〜に限って` (chỉ riêng/đúng lúc) với `〜に限らず` (không chỉ riêng — Bài 06).",
            "⚠️ `〜限りでは` luôn giới hạn độ chính xác của thông tin mình nắm được (`聞いた限りでは`, `調べた限りでは`)."
        ],
        "quiz": [
            ("明日（あした）のセールは、ポイントカードをお持ちのお客様（きゃくさま）（　　）10%オフとなります。", ["に限（かぎ）り", "に限（かぎ）って", "限（かぎ）りでは", "限（かぎ）りは"], 1, "Thông báo giới hạn đối tượng ưu đãi -> に限り."),
            ("このルールを守（まも）らない（　　）、試合（しあい）に出場（しゅつじょう）することはできない。", ["限（かぎ）り", "限（かぎ）りでは", "に限（かぎ）って", "に限（かぎ）り"], 1, "V-ない + 限り: chừng nào không tuân thủ... thì không thể."),
            ("今朝（けさ）の天気（てんき）予報（よほう）を見（み）た（　　）、週末（しゅうまつ）は晴（は）れるようだ。", ["限（かぎ）りでは", "に限（かぎ）って", "に限（かぎ）り", "限（かぎ）りは"], 1, "Giới hạn thông tin từ việc xem dự báo thời tiết -> 限りでは."),
            ("急（いそ）いでいる朝（あさ）（　　）、電車（でんしゃ）が遅延（ちえん）してイライラした。", ["に限（かぎ）って", "に限（かぎ）り", "限（かぎ）りでは", "限（かぎ）りは"], 1, "Đúng lúc đang vội thì lại gặp chuyện trớ trêu -> に限って."),
            ("あんなに親切（しんせつ）な彼女（かのじょ）（　　）、人（ひと）を騙（だま）すようなことは絶対（ぜったい）にしない。", ["に限（かぎ）って", "に限（かぎ）り", "限（かぎ）りでは", "限（かぎ）りは"], 1, "Khẳng định niềm tin riêng cô ấy chắc chắn không làm -> に限って + phủ định."),
        ]
    },
    6: {
        "title_jp": "〜だけでなく・それに加えて",
        "title_vi": "Không Chỉ... Mà Còn... (Bổ Sung & Tăng Tiến)",
        "section": "I. ことがらを説明する",
        "intro": "Bài 06 trong **Shinkanzen Master Ngữ pháp N2** tập hợp 5 cấu trúc **bổ sung và tăng tiến** (`〜に限らず`, `〜のみならず`, `〜ばかりか`, `〜はもとより`, `〜上（に）`). Đề thi cực hay hỏi cách chia tính từ `な` / danh từ trước mỗi mẫu!",
        "patterns": [
            {
                "name": "1. 〜に限（かぎ）らず",
                "meaning": "Không chỉ giới hạn ở A mà còn rộng khắp B... (Phạm vi mở rộng vượt ra khỏi A).",
                "connection": "N + に限（かぎ）らず",
                "examples": [
                    ("このアニメは子ども**に限（かぎ）らず**、大人（おとな）からも広（ひろ）く愛（あい）されている。", "Bộ phim hoạt hình này không chỉ riêng trẻ em mà người lớn cũng rất yêu thích."),
                    ("日本（にほん）**に限（かぎ）らず**、世界中（せかいじゅう）で環境（かんきょう）問題（もんだい）が深刻（しんこく）化（か）している。", "Không chỉ ở Nhật Bản mà trên toàn thế giới, vấn đề môi trường đang ngày càng nghiêm trọng."),
                ],
                "note": "CHỈ đi sau Danh từ; vế sau luôn mang phạm vi rộng hơn (`〜も`, `〜誰でも`, `〜どこでも`)."
            },
            {
                "name": "2. 〜のみならず",
                "meaning": "Không chỉ A mà còn cả B nữa (Dạng văn viết trang trọng của `だけでなく`).",
                "connection": "V-thông thường / Aい / Na（な・である） / N（である） + のみならず",
                "examples": [
                    ("この技術（ぎじゅつ）は国内（こくない）**のみならず**、海外（かいがい）でも高（たか）く評価（ひょうか）されている。", "Công nghệ này không chỉ được đánh giá cao ở trong nước mà cả ở nước ngoài."),
                    ("台風（たいふう）による被害（ひがい）は住宅（じゅうたく）**のみならず**、農作物（のうさくぶつ）にも及（およ）んだ。", "Thiệt hại do bão không chỉ dừng ở nhà cửa mà còn lan sang cả nông sản."),
                ],
                "note": "Vế sau thường đi với `〜も` hoặc `〜まで`. Khi nối danh từ có thể gắn trực tiếp `N + のみならず`."
            },
            {
                "name": "3. 〜ばかりか",
                "meaning": "Không những A mà thậm chí còn B nữa (Vế sau mang mức độ vượt ngoài dự đoán, tăng tiến hơn vế trước).",
                "connection": "V-thông thường / Aい / Na-な（である） / N（である） + ばかりか",
                "examples": [
                    ("彼（かれ）は英語（えいご）**ばかりか**、フランス語（ご）や中国語（ちゅうごくご）まで話（はな）せる。", "Anh ấy không chỉ nói được tiếng Anh mà thậm chí còn nói được cả tiếng Pháp và tiếng Trung."),
                    ("このマンションは家賃（やちん）が高（たか）い**ばかりか**、部屋（へや）も狭（せま）くて日当（ひあ）たりが悪（わる）い。", "Chung cư này không những tiền thuê đắt mà phòng lại còn chật và thiếu nắng."),
                ],
                "note": "Vế sau hay dùng `〜も`, `〜まで`, `〜さえ`. Không dùng cho câu mệnh lệnh/nhờ vả ở vế sau (khi đó dùng `だけでなく`)."
            },
            {
                "name": "4. 〜はもとより",
                "meaning": "A thì đương nhiên rồi, đến cả B cũng... (Đưa A làm điều hiển nhiên để nhấn mạnh thêm B).",
                "connection": "N + はもとより",
                "examples": [
                    ("このレストランは味（あじ）**はもとより**、店員（てんいん）の接客（せっきゃく）態度（たいど）も素晴（すば）らしい。", "Nhà hàng này hương vị thì khỏi bàn rồi, ngay cả thái độ phục vụ của nhân viên cũng tuyệt vời."),
                    ("家族（かぞく）**はもとより**、友人（ゆうじん）や近所（きんじょ）の人（ひと）にも祝福（しゅくふく）された。", "Gia đình thì đương nhiên rồi, cả bạn bè và hàng xóm cũng chúc phúc cho tôi."),
                ],
                "note": "A luôn là điều hiển nhiên, dễ thấy; B là điều được nhấn mạnh bổ sung thêm."
            },
            {
                "name": "5. 〜上（うえ）（に）",
                "meaning": "Hơn nữa, thêm vào đó (Cộng dồn hai đặc điểm CÙNG CHIỀU: tốt + tốt hoặc xấu + xấu).",
                "connection": "V-thông thường / Aい / Na-な / Nの + 上（うえ）（に）",
                "examples": [
                    ("この店（みせ）は値段（ねだん）が安（やす）い**上（うえ）に**、ボリュームもあっておいしい。", "Quán này giá cả đã rẻ lại còn đầy đặn và ngon miệng nữa."),
                    ("雨（あめ）が降（ふ）ってきた**上（うえ）に**、道（みち）まで渋滞（じゅうたい）し始（はじ）めた。", "Trời đã đổ mưa lại còn bắt đầu tắc đường nữa chứ."),
                ],
                "note": "BẮT BUỘC hai vế cùng chiều đánh giá (cùng khen hoặc cùng chê). ✗ `安い上にまずい`."
            },
        ],
        "comparison": [
            ("〜に限らず", "Mở rộng phạm vi đối tượng/nơi chốn.", "Chỉ đi sau Danh từ (`男性に限らず`, `春に限らず`)."),
            ("〜のみならず", "Văn viết trang trọng của `だけでなく`.", "Nối được với V, A, Na, N."),
            ("〜ばかりか", "Tăng tiến gây ngạc nhiên; vế sau hay có `まで / さえ`.", "Không dùng cho câu ý chí/mệnh lệnh ở vế sau."),
            ("〜はもとより", "A đương nhiên rồi, B cũng thế.", "Chỉ dùng với Danh từ."),
            ("〜上に", "Cộng dồn hai tính chất CÙNG CHIỀU.", "Trước `上に` dùng `Naな / Nの`."),
        ],
        "pitfalls": [
            "⚠️ Bẫy nối từ: `N + の + 上（うえ）に` (hơn nữa), nhưng `N + である + のみならず` / `N + のみならず`.",
            "⚠️ Không nhầm `〜上に` (thêm vào đó — Bài 06) với `〜上で` (sau khi làm — Bài 03) và `〜上は` (một khi đã — Bài 17)."
        ],
        "quiz": [
            ("この公園（こうえん）は桜（さくら）の季節（きせつ）（　　）、一年（いちねん）中（じゅう）花（はな）が楽（たの）しめる。", ["に限（かぎ）らず", "ばかりか", "はもとより", "上（うえ）に"], 1, "Không chỉ riêng mùa hoa anh đào -> sau N mở rộng phạm vi: に限らず."),
            ("田中（たなか）さんは仕事（しごと）ができる（　　）、人柄（ひとがら）もとても優（やさ）しい。", ["上（うえ）に", "に限（かぎ）らず", "はもとより", "上（うえ）で"], 1, "Hai ưu điểm cùng chiều nối sau V-る -> 上に."),
            ("大雪（おおゆき）のせいで電車（でんしゃ）が止（と）まった（　　）、停電（ていでん）まで起（お）きてしまった。", ["ばかりか", "に限（かぎ）らず", "はもとより", "際（さい）に"], 1, "Không những dừng tàu mà thậm chí mất điện (vế sau có まで) -> ばかりか."),
            ("漢字（かんじ）の読（よ）み（　　）、正（ただ）しく書（か）く練習（れんしゅう）も重要（じゅうよう）だ。", ["はもとより", "ばかりか", "上（うえ）に", "のみならず"], 1, "Đọc thì đương nhiên rồi, viết cũng quan trọng -> N + はもとより."),
            ("この新薬（しんやく）は人間（にんげん）の健康（けんこう）（　　）、動物（どうぶつ）の治療（ちりょう）にも役立（やくだ）つと期待（きたい）されている。", ["のみならず", "上（うえ）に", "につれて", "にあたって"], 1, "Văn viết trang trọng \"không chỉ... mà còn...\" -> のみならず."),
        ]
    },
    7: {
        "title_jp": "〜について・〜を相手にして",
        "title_vi": "Liên Quan, Đối Tượng & Đáp Ứng",
        "section": "I. ことがらを説明する",
        "intro": "Bài 07 trong **Shinkanzen Master Ngữ pháp N2** gom 5 mẫu diễn đạt **chủ đề liên quan, vấn đề gây tranh cãi, sở trường và thái độ hướng tới đối phương** (`〜に関して`, `〜をめぐって`, `〜にかけては`, `〜に対して`, `〜にこたえて`).",
        "patterns": [
            {
                "name": "1. 〜に関（かん）して / 〜に関（かん）する",
                "meaning": "Liên quan đến... / Về vấn đề... (Cách nói trang trọng của `〜について`).",
                "connection": "N + に関（かん）して（は / も） / に関（かん）する + N",
                "examples": [
                    ("今回（こんかい）の計画（けいかく）**に関（かん）して**、質問（しつもん）がある方（かた）は挙手（きょしゅ）をお願（ねが）いします。", "Liên quan đến kế hoạch lần này, ai có câu hỏi xin vui lòng giơ tay."),
                    ("環境（かんきょう）保護（ほご）**に関（かん）する**本（ほん）をたくさん読（よ）んでいる。", "Tôi đang đọc rất nhiều sách liên quan đến bảo vệ môi trường."),
                ],
                "note": "Bổ nghĩa trực tiếp cho danh từ phía sau bắt buộc dùng `に関する + N`."
            },
            {
                "name": "2. 〜をめぐって / 〜をめぐる",
                "meaning": "Xoay quanh... (Một vấn đề gây tranh luận, mâu thuẫn, tranh giành giữa nhiều bên).",
                "connection": "N + をめぐって / をめぐり / をめぐる + N",
                "examples": [
                    ("遺産（いさん）の相続（そうぞく）**をめぐって**、兄弟（きょうだい）の間（あいだ）で争（あらそ）いが起（お）きた。", "Xoay quanh việc thừa kế di sản, giữa các anh em đã nảy sinh tranh chấp."),
                    ("新（あたら）しい空港（くうこう）の建設（けんせつ）**をめぐる**議論（ぎろん）が続（つづ）いている。", "Những cuộc tranh luận xoay quanh việc xây dựng sân bay mới vẫn đang tiếp diễn."),
                ],
                "note": "Vế sau BẮT BUỘC liên quan đến tranh cãi/đối đầu nhiều bên (`議論する`, `対立する`, `争う`, `もめる`)."
            },
            {
                "name": "3. 〜にかけては",
                "meaning": "Riêng về mặt / lĩnh vực... thì (giỏi nhất, không thua kém ai).",
                "connection": "N + にかけては",
                "examples": [
                    ("足（あし）の速（はや）さ**にかけては**、クラスの誰（だれ）にも負（ま）けない。", "Riêng về khoản chạy nhanh thì tôi không thua bất kỳ ai trong lớp."),
                    ("古美術（こびじゅつ）の知識（ちしき）**にかけては**、彼（かれ）の右（みぎ）に出（で）る者（もの）はいない。", "Riêng về kiến thức mỹ thuật cổ thì không ai qua mặt được anh ấy."),
                ],
                "note": "Luôn dùng với **lời khen** năng lực vượt trội; KHÔNG dùng để chê (✗ `遅刻にかけては一番だ`)."
            },
            {
                "name": "4. 〜に対（たい）して / 〜に対（たい）する",
                "meaning": "1) Đối với... (thái độ/hành động hướng về đối tượng); 2) Ngược lại với A thì B... (đối chiếu 2 mặt).",
                "connection": "N + に対（たい）して / に対（たい）する + N ｜ V・A普通形 / Naな・Nな（である） + のに対して",
                "examples": [
                    ("目上（めうえ）の人（ひと）**に対（たい）して**は、丁寧（ていねい）な言葉遣（ことばづか）いを心（こころ）がけるべきだ。", "Đối với người bề trên, ta nên chú ý dùng ngôn từ lịch sự."),
                    ("兄（あに）が社交的（しゃこうてき）な**のに対（たい）して**、弟（おとうと）はおとなしい性格（せいかく）だ。", "Trái ngược với người anh hướng ngoại, người em có tính cách trầm lặng."),
                ],
                "note": "Nghĩa (1) đi sau Danh từ chỉ đối tượng; nghĩa (2) nối 2 mệnh đề tương phản (`〜のに対して`)."
            },
            {
                "name": "5. 〜に応（こた）えて / 〜に応（こた）える",
                "meaning": "Đáp lại / Hưởng ứng (kỳ vọng, nguyện vọng, yêu cầu, tiếng cổ vũ).",
                "connection": "N（期待・要望・声援・アンコール...）+ に応（こた）えて / に応（こた）える + N",
                "examples": [
                    ("ファンの熱（あつ）い声援（せいえん）**に応（こた）えて**、選手（せんしゅ）たちは全力（ぜんりょく）を尽（つ）くした。", "Đáp lại sự cổ vũ nồng nhiệt của người hâm mộ, các tuyển thủ đã chiến đấu hết mình."),
                    ("住民（じゅうみん）の要望（ようぼう）**に応（こた）える**形（かたち）で、新（あたら）しいバス路線（ろせん）ができた。", "Tuyến xe buýt mới đã được mở ra để đáp ứng nguyện vọng của cư dân."),
                ],
                "note": "Chú ý chữ Hán viết là **応える** (đáp ứng), không viết 答える (trả lời câu hỏi)."
            },
        ],
        "comparison": [
            ("〜に関して", "Chủ đề nói chung, khách quan (trang trọng của について).", "Không đòi hỏi có tranh cãi."),
            ("〜をめぐって", "Xoay quanh vấn đề tranh chấp, bàn cãi nhiều phía.", "Vế sau phải có tranh luận, xung đột (`議論・対立・争い`)."),
            ("〜に対して", "Hướng thái độ đến đối tượng hoặc đối chiếu 2 vế ngược nhau.", "Phân biệt với `にとって` (đối với góc nhìn/đánh giá — Bài 19)."),
        ],
        "pitfalls": [
            "⚠️ `〜にかけては` luôn đi với đánh giá tích cực (`一番だ`, `右に出る者はいない`).",
            "⚠️ Không nhầm `〜に対して` (thái độ/hành động hướng tới A) với `〜にとって` (đứng trên lập trường của A để đánh giá — Bài 19)."
        ],
        "quiz": [
            ("新（あたら）しい税制（ぜいせい）（　　）、国会（こっかい）で激（はげ）しい議論（ぎろん）が行（おこな）われた。", ["をめぐって", "にかけては", "に応（こた）えて", "に対（たい）する"], 1, "Có tranh luận gay gắt nhiều bên xoay quanh dự luật -> をめぐって."),
            ("語学（ごがく）の才能（さいのう）（　　）、彼（かれ）にかなう人（ひと）はいない。", ["にかけては", "をめぐって", "に関（かん）して", "に応（こた）えて"], 1, "Khen ngợi sở trường vượt trội -> にかけては."),
            ("お客様（きゃくさま）のご要望（ようぼう）（　　）、営業時間（えいぎょうじかん）を延長（えんちょう）いたしました。", ["に応（こた）えて", "をめぐって", "にかけては", "に関（かん）する"], 1, "Đáp lại nguyện vọng của khách hàng -> に応えて."),
            ("この地域の気候（きこう）（　　）資料（しりょう）を集（あつ）めている。", ["に関（かん）する", "をめぐって", "にかけては", "に応（こた）えて"], 1, "Bổ nghĩa cho danh từ 資料 phía sau -> に関する."),
            ("都市部（としぶ）では人口（じんこう）が増（ふ）えている（　　）、地方（ちほう）では過疎化（かそか）が進（すす）んでいる。", ["のに対（たい）して", "をめぐって", "に応（こた）えて", "に関（かん）して"], 1, "Đối chiếu hai thực trạng trái ngược nhau -> のに対して."),
        ]
    },
    8: {
        "title_jp": "〜を基準にして",
        "title_vi": "Dựa Trên Cơ Sở, Tiêu Chuẩn & Đối Tượng",
        "section": "I. ことがらを説明する",
        "intro": "Bài 08 trong **Shinkanzen Master Ngữ pháp N2** gồm 5 mẫu diễn tả **lấy cái gì làm gốc/căn cứ/khuôn khổ/đối tượng phục vụ** (`〜をもとに（して）`, `〜に基づいて`, `〜に沿って`, `〜のもとで・〜のもとに`, `〜向けだ`).",
        "patterns": [
            {
                "name": "1. 〜をもとに（して）",
                "meaning": "Dựa trên cơ sở, chất liệu gốc... để sáng tạo, xây dựng cái mới.",
                "connection": "N + をもとに（して）",
                "examples": [
                    ("この映画（えいが）は実際（じっさい）に起（お）きた事件（じけん）**をもとに**作（つく）られた。", "Bộ phim này được dựng lên dựa trên một vụ án có thật."),
                    ("アンケート結果（けっか）**をもとにして**、新商品（しんしょうひん）を開発（かいはつ）した。", "Dựa trên kết quả khảo sát, chúng tôi đã phát triển sản phẩm mới."),
                ],
                "note": "Thường dùng với ý lấy dữ liệu, câu chuyện, nguyên mẫu làm chất liệu sáng tạo/xây dựng tác phẩm hoặc sản phẩm."
            },
            {
                "name": "2. 〜に基（もと）づいて / 〜に基（もと）づく",
                "meaning": "Dựa trên căn cứ, quy tắc, dữ liệu thực tế, pháp luật... (Văn phong nghiêm túc, chuẩn mực).",
                "connection": "N + に基（もと）づいて / に基（もと）づき / に基（もと）づく + N / に基（もと）づいた + N",
                "examples": [
                    ("法律（ほうりつ）**に基（もと）づいて**公正（こうせい）に判断（はんだん）する。", "Phán xét một cách công minh dựa trên căn cứ pháp luật."),
                    ("長年（ながねん）の経験（けいけん）**に基（もと）づく**アドバイスはとても役（やく）に立（た）つ。", "Lời khuyên dựa trên kinh nghiệm nhiều năm vô cùng hữu ích."),
                ],
                "note": "Thiên về căn cứ mang tính quy chuẩn, khoa học, luật lệ, dữ liệu xác thực."
            },
            {
                "name": "3. 〜に沿（そ）って / 〜に沿（そ）う",
                "meaning": "Dựa theo / Tuân theo sát (phương châm, kế hoạch, ý nguyện, đường lối — nghĩa đen là đi dọc theo bờ sông/con đường).",
                "connection": "N + に沿（そ）って / に沿（そ）う / に沿（そ）った + N",
                "examples": [
                    ("政府（せいふ）の方針（ほうしん）**に沿（そ）って**、新（あたら）しい規則（きそく）が作（つく）られた。", "Quy tắc mới được lập ra bám sát theo đường lối của chính phủ."),
                    ("お客様（きゃくさま）のご希望（きぼう）**に沿（そ）う**プランをご提案（ていあん）します。", "Chúng tôi xin đề xuất gói dịch vụ phù hợp sát với mong muốn của quý khách."),
                ],
                "note": "Hay đi với `方針・計画・マニュアル・希望・趣旨` (không tách rời khỏi lộ trình có sẵn)."
            },
            {
                "name": "4. 〜のもとで / 〜のもとに",
                "meaning": "Dưới sự (chỉ đạo, ảnh hưởng, bảo trợ, điều kiện...) của ai đó/cái gì.",
                "connection": "N + のもとで / のもとに",
                "examples": [
                    ("優秀（ゆうしゅう）なコーチの指導（しどう）**のもとで**、毎日（まいにち）練習（れんしゅう）に励（はげ）んでいる。", "Dưới sự chỉ dẫn của huấn luyện viên xuất sắc, tôi chăm chỉ luyện tập mỗi ngày."),
                    ("平等（びょうどう）な条件（じょうけん）**のもとに**競争（きょうそう）が行（おこな）われた。", "Cuộc cạnh tranh đã diễn ra dưới các điều kiện bình đẳng."),
                ],
                "note": "`のもとで` nhấn mạnh không gian/môi trường chịu ảnh hưởng; `のもとに` hay đi với điều kiện, danh nghĩa (`〜という条件のもとに`)."
            },
            {
                "name": "5. 〜向（む）けだ",
                "meaning": "Dành riêng cho đối tượng... (được thiết kế/sản xuất hướng tới nhóm đối tượng cụ thể đó).",
                "connection": "N + 向（む）けだ / 向（む）けに / 向（む）けの + N",
                "examples": [
                    ("これは外国人（がいこくじん）留学生（りゅうがくせい）**向（む）けの**ガイドブックだ。", "Đây là sách hướng dẫn được biên soạn dành riêng cho du học sinh nước ngoài."),
                    ("このマンションは一人（ひとり）暮（ぐ）らしの若者（わかもの）**向（む）けに**設計（せっけい）されている。", "Chung cư này được thiết kế dành riêng cho người trẻ sống một mình."),
                ],
                "note": "Phân biệt: `〜向け` (được tạo ra **dành cho** đối tượng A) vs `〜向き` (có tính chất **thích hợp** với A, dù không hẳn làm riêng cho A)."
            },
        ],
        "comparison": [
            ("〜をもとに", "Lấy nguyên liệu/ý tưởng gốc để tạo tác phẩm, sản phẩm (`実話をもとに`).", "Mang tính sáng tạo, phát triển từ gốc."),
            ("〜に基づいて", "Dựa trên quy định, dữ kiện, luật pháp (`調査データに基づいて`).", "Mang tính logic, căn cứ khách quan."),
            ("〜に沿って", "Đi sát theo đường lối, kế hoạch, yêu cầu có sẵn (`マニュアルに沿って`).", "Không đi chệch khỏi khung đã định."),
            ("〜向け vs 〜向き", "`向け`: chủ đích làm dành cho ai; `向き`: hợp với ai.", "`子供向け番組` (làm cho trẻ con) vs `夏向きの服` (áo hợp mặc mùa hè)."),
        ],
        "pitfalls": [
            "⚠️ Bẫy `〜向け` vs `〜向き`: Nếu câu nói \"tính chất phù hợp\" (`初心者向き`, `家族向きの間取り`) thì dùng `向き`; nếu nói \"sản xuất hướng tới đối tượng\" (`留学生向けに発行する`) dùng `向け`.",
            "⚠️ `〜のもとで` đứng sau danh từ + の (`指導のもとで`, `両親のもとで`)."
        ],
        "quiz": [
            ("この小説（しょうせつ）は、著者（ちょしゃ）自身（じしん）の体験（たいけん）（　　）書（か）かれた。", ["をもとに", "に沿って", "のもとに", "向（む）けに"], 1, "Chất liệu sáng tác từ trải nghiệm bản thân -> をもとに."),
            ("厳密（げんみつ）なデータ（　　）、来年（らいねん）の経済（けいざい）成長（せいちょう）を予測（よそく）する。", ["に基（もと）づいて", "をもとに", "のもとに", "向（む）けに"], 1, "Dự báo dựa trên căn cứ số liệu chính xác -> に基づいて."),
            ("会社（かいしゃ）の新しい方針（ほうしん）（　　）業務（ぎょうむ）を進（すす）める。", ["に沿（そ）って", "のもとで", "をもとに", "向（む）けだ"], 1, "Tiến hành công việc bám sát theo đường lối -> に沿って."),
            ("厳（きび）しい監督（かんとく）（　　）、チームは全国（ぜんこく）優勝（ゆうしょう）を果（は）たした。", ["のもとで", "に基（もと）づいて", "に沿（そ）って", "をもとに"], 1, "Dưới sự dẫn dắt của huấn luyện viên -> のもとで."),
            ("この辞書（じしょ）は専門（せんもん）用語（ようご）が多（おお）く、上級者（じょうきゅうしゃ）（　　）作（つく）られている。", ["向（む）けに", "をもとに", "のもとで", "に沿（そ）って"], 1, "Được biên soạn dành cho đối tượng người học trình độ cao -> 向けに."),
        ]
    },
    9: {
        "title_jp": "〜に関連して・〜に対応して",
        "title_vi": "Biến Đổi Tương Ứng & Phản Ứng Theo",
        "section": "I. ことがらを説明する",
        "intro": "Bài 09 trong **Shinkanzen Master Ngữ pháp N2** tập hợp 5 cấu trúc biểu thị **sự thay đổi kéo theo tỷ lệ thuận**, **sự phụ thuộc**, **sự ứng biến phù hợp** và **cảm xúc nảy sinh mỗi khi...** (`〜につれて`, `〜に伴って`, `〜次第だ`, `〜に応じて`, `〜につけて`).",
        "patterns": [
            {
                "name": "1. 〜につれて / 〜にしたがって",
                "meaning": "Cùng với sự thay đổi A thì B cũng dần thay đổi theo (tỷ lệ thuận tự nhiên).",
                "connection": "V-る / N（biến đổi） + につれて / にしたがって",
                "examples": [
                    ("年（とし）をとる**につれて**、体力（たいりょく）が落（お）ちてきた。", "Cùng với việc có tuổi, thể lực cũng dần suy giảm."),
                    ("台風（たいふう）が近（ちか）づく**にしたがって**、風雨（ふうう）が強（つよ）くなってきた。", "Bão càng tiến lại gần thì gió mưa càng trở nên dữ dội."),
                ],
                "note": "Thường chỉ sự thay đổi tự nhiên một chiều (tăng dần hoặc giảm dần), vế sau KHÔNG dùng câu ý chí, mệnh lệnh. Lưu ý: `にしたがって` còn có nghĩa \"làm theo chỉ thị/quy tắc\"."
            },
            {
                "name": "2. 〜に伴（ともな）って / 〜とともに",
                "meaning": "Cùng với sự biến đổi/sự kiện A thì B kéo theo xảy ra (trang trọng, văn viết; cũng dùng cho việc đi kèm).",
                "connection": "V-る / N + に伴（ともな）って（に伴い・に伴う） / とともに",
                "examples": [
                    ("人口（じんこう）の増加（ぞうか）**に伴（ともな）って**、ごみの量（りょう）も増（ふ）えている。", "Cùng với sự gia tăng dân số, lượng rác thải cũng đang tăng lên."),
                    ("経済（けいざい）の発展（はってん）**とともに**、人々（ひとびと）の生活（せいかつ）も豊（ゆた）かになった。", "Cùng với sự phát triển kinh tế, đời sống người dân cũng trở nên sung túc."),
                ],
                "note": "`に伴って` hay dùng cho hệ quả kéo theo của một biến động xã hội/tự nhiên hoặc tác động kèm theo (`地震に伴う津波`). `とともに` còn có nghĩa \"đồng thời cùng lúc với...\"."
            },
            {
                "name": "3. 〜次第（しだい）だ",
                "meaning": "Tùy thuộc hoàn toàn vào A (kết quả thay đổi tùy theo A thế nào).",
                "connection": "N + 次第（しだい）だ / 次第（しだい）で",
                "examples": [
                    ("合格（ごうかく）できるかどうかは、これからの努力（どりょく）**次第（しだい）だ**。", "Có đỗ được hay không là tùy thuộc vào nỗ lực từ nay về sau của em."),
                    ("物事（ものごと）は考（かんが）え方（かた）**次第（しだい）で**、楽（たの）しくも辛（つら）くもなる。", "Mọi việc tùy thuộc vào cách suy nghĩ mà có thể trở nên vui vẻ hay khổ sở."),
                ],
                "note": "Khác hoàn toàn với Bài 03 (`V-ます + 次第` = ngay sau khi)! Ở Bài 09 là `N + 次第だ` = tùy thuộc vào N."
            },
            {
                "name": "4. 〜に応（おう）じて",
                "meaning": "Ứng với / Tùy theo / Phù hợp tương ứng với (nhu cầu, năng lực, hoàn cảnh, tuổi tác...).",
                "connection": "N + に応（おう）じて / に応（おう）じた + N",
                "examples": [
                    ("体力（たいりょく）**に応（おう）じて**、無理（むり）のない運動（うんどう）を続（つづ）けましょう。", "Hãy duy trì vận động vừa sức tương ứng với thể lực của bản thân."),
                    ("時代（じだい）の変化（へんか）**に応（おう）じた**教育（きょういく）が求（もと）められている。", "Một nền giáo dục phù hợp tương ứng với sự thay đổi của thời đại đang được đòi hỏi."),
                ],
                "note": "Khác `〜につれて` (biến đổi tự nhiên liên tục); `に応じて` là điều chỉnh linh hoạt cho phù hợp với từng mức/đối tượng khác nhau."
            },
            {
                "name": "5. 〜につけて（は・も）",
                "meaning": "Mỗi khi (nhìn thấy, nghe thấy, nghĩ đến...) A thì tự nhiên lại nảy sinh cảm xúc B.",
                "connection": "V-る / N + につけて（は・も）",
                "examples": [
                    ("この写真（しゃしん）を見（み）る**につけて**、ふるさとを思（おも）い出（だ）す。", "Mỗi khi ngắm nhìn bức ảnh này, tôi lại bồi hồi nhớ về quê hương."),
                    ("何（なに）か**につけて**、母（はは）は私（わたし）のことを心配（しんぱい）してくれる。", "Hễ có chuyện gì đi nữa, mẹ cũng luôn lo lắng cho tôi."),
                ],
                "note": "Vế trước hay là `見る・聞く・読む・思い出す` hoặc các cụm cố định `何かにつけて`, `につけ〜につけ` (`良いにつけ悪いにつけ` = dù tốt hay xấu)."
            },
        ],
        "comparison": [
            ("〜につれて", "A biến đổi -> B biến đổi liên tục (chỉ sự thay đổi dần dần).", "Không dùng với ý chí/mệnh lệnh ở vế sau."),
            ("〜に伴って", "Biến động kéo theo tác động/hệ quả (văn viết).", "Bổ nghĩa danh từ dùng `に伴う N`."),
            ("〜に応じて", "Thay đổi/lựa chọn sao cho phù hợp từng điều kiện, cấp độ.", "Hay đi với `能力・年齢・季節・要望`."),
            ("〜次第だ (N)", "Tùy thuộc vào N (`あなた次第`).", "Phân biệt với `V-ます + 次第` (ngay sau khi — Bài 03)."),
        ],
        "pitfalls": [
            "⚠️ Cặp dễ nhầm số 1: `V-ます + 次第` (ngay khi — Bài 03) vs `N + 次第だ` (tùy thuộc vào — Bài 09).",
            "⚠️ `〜につれて` không đi được với câu rủ rê/mệnh lệnh ở vế sau (nếu vế sau có ý chí, dùng `にしたがって` ở nghĩa \"làm theo\" hoặc chọn cấu trúc khác)."
        ],
        "quiz": [
            ("秋（あき）が深（ふか）まる（　　）、朝晩（あさばん）の冷（ひ）え込（こ）みが厳（きび）しくなってきた。", ["につれて", "に応（おう）じて", "につけて", "次第（しだい）で"], 1, "Mùa thu vào sâu kéo theo trời lạnh dần -> につれて."),
            ("参加（さんか）者（しゃ）のレベル（　　）、クラスを3つに分（わ）けました。", ["に応（おう）じて", "につれて", "に伴（ともな）って", "につけて"], 1, "Chia lớp tương ứng với trình độ từng người -> に応じて."),
            ("成功（せいこう）するかどうかは、リーダーの判断（はんだん）（　　）だ。", ["次第（しだい）", "につれて", "につけて", "に応（おう）じて"], 1, "Tùy thuộc vào phán đoán của trưởng nhóm -> N + 次第だ."),
            ("この曲（きょく）を聞（き）く（　　）、学生（がくせい）時代（じだい）の思い出（おもいで）がよみがえる。", ["につけて", "に応（おう）じて", "次第（しだい）で", "に伴（ともな）って"], 1, "Mỗi khi nghe bản nhạc lại gợi nhớ kỷ niệm -> V-る + につけて."),
            ("都市（とし）の再開発（さいかいはつ）（　　）、周辺（しゅうへん）の交通（こうつう）量（りょう）が増加（ぞうか）した。", ["に伴（ともな）い", "につけて", "次第（しだい）で", "に応（おう）じて"], 1, "Tái phát triển đô thị kéo theo lượng giao thông tăng -> に伴い."),
        ]
    },
    10: {
        "title_jp": "〜や〜など",
        "title_vi": "Liệt Kê & Nêu Ví Dụ",
        "section": "I. ことがらを説明する",
        "intro": "Bài 10 trong **Shinkanzen Master Ngữ pháp N2** gom các cấu trúc **liệt kê, đưa ra nhiều ví dụ hoặc cân nhắc giữa các khả năng** (`〜やら〜やら`, `〜というか〜というか`, `〜にしても〜にしても / 〜にしろ / 〜にせよ`, `〜といった`).",
        "patterns": [
            {
                "name": "1. 〜やら〜やら",
                "meaning": "Nào là A, nào là B... (Liệt kê nhiều thứ/việc xảy ra cùng lúc khiến người nói thấy rối bời, bận rộn, vất vả).",
                "connection": "V-る / Aい / N + やら + ... + やら",
                "examples": [
                    ("引（ひ）っ越（こ）しの前（まえ）は、荷造（にづ）り**やら**手続き（てつづき）**やら**で本当（ほんとう）に忙（いそが）しい。", "Trước khi chuyển nhà, nào là đóng gói đồ đạc nào là làm thủ tục, bận tối mắt tối mũi."),
                    ("合格（ごうかく）が決（き）まって、嬉（うれ）しい**やら**ホッとした**やら**で涙（なみだ）が出（で）た。", "Nhận tin đỗ, nào là mừng rỡ nào là nhẹ nhõm làm tôi bật khóc."),
                ],
                "note": "Thường đi kèm với trạng thái hỗn độn, quá nhiều việc dồn dập hoặc cảm xúc lẫn lộn."
            },
            {
                "name": "2. 〜というか〜というか",
                "meaning": "Không biết nên gọi là A hay là B... (Diễn tả sự phân vân khi chọn từ mô tả chính xác sắc thái).",
                "connection": "Thể thông thường（Na-な/だ, N-だ/bỏ だ）+ というか + ... + というか",
                "examples": [
                    ("彼（かれ）の態度（たいど）は、自信（じしん）がある**というか**生意気（なまいき）**というか**、ちょっと複雑（ふくざつ）だ。", "Thái độ của anh ta, nói là tự tin hay nói là xấc xược đây nhỉ, hơi khó diễn tả."),
                    ("あの映画（えいが）は、感動的（かんどうてき）**というか**切（せつ）ない**というか**、心（こころ）に残（のこ）る作品（さくひん）だった。", "Bộ phim đó nói là cảm động hay day dứt đây, thực sự là tác phẩm đọng lại sâu sắc."),
                ],
                "note": "Hai vế có thể là 2 mặt tương tự hoặc hơi trái ngược làm người nói cân nhắc cách diễn đạt."
            },
            {
                "name": "3. 〜にしても〜にしても / 〜にしろ〜にしろ / 〜にせよ〜にせよ",
                "meaning": "Dù là A hay là B thì cũng đều... (Cả hai trường hợp đối lập hoặc ví dụ đưa ra đều dẫn đến cùng kết luận).",
                "connection": "N / Thể thông thường + にしても〜にしても（にしろ〜にしろ / にせよ〜にせよ）",
                "examples": [
                    ("仕事（しごと）**にしても**勉強（べんきょう）**にしても**、毎日（まいにち）コツコツ続（つづ）けることが大切（たいせつ）だ。", "Dù là công việc hay học tập đi nữa, việc kiên trì từng chút mỗi ngày đều rất quan trọng."),
                    ("行（い）く**にしろ**行（い）かない**にしろ**、早（はや）めに連絡（れんらく）してください。", "Dù đi hay không đi, xin hãy liên lạc báo sớm giúp tôi."),
                ],
                "note": "Thứ tự trang trọng tăng dần: `にしても` -> `にしろ` -> `にせよ` (trang trọng, văn viết)."
            },
            {
                "name": "4. 〜といった",
                "meaning": "Những thứ như là A, B... (Liệt kê ví dụ tiêu biểu để bổ nghĩa cho danh từ tổng quát phía sau).",
                "connection": "N（や N）+ といった + N",
                "examples": [
                    ("京都（きょうと）や奈良（なら）**といった**古都（こと）には、歴史的（れきしてき）な建造物（けんぞうぶつ）が多（おお）い。", "Ở những cố đô như là Kyoto hay Nara có rất nhiều công trình kiến trúc lịch sử."),
                    ("頭痛（ずつう）や倦怠感（けんたいかん）**といった**症状（しょうじょう）が出（で）たら、早（はや）めに病院（びょういん）へ行（い）きましょう。", "Nếu xuất hiện các triệu chứng như đau đầu hay mệt mỏi rã rời, hãy sớm đi bệnh viện."),
                ],
                "note": "Luôn đứng trước một Danh từ bao quát hơn nhóm danh từ liệt kê ở trước."
            },
        ],
        "comparison": [
            ("〜やら〜やら", "Liệt kê nhiều thứ/cảm giác hỗn độn, bận rộn.", "Chỉ cần liệt kê 2–3 ví dụ gây bận tâm/cảm xúc lẫn lộn."),
            ("〜というか〜というか", "Phân vân diễn đạt \"nên nói là A hay B đây\".", "Dùng để tìm từ mô tả tính chất, cảm giác."),
            ("〜にしても〜にしても", "Dù A hay B thì kết luận chung vẫn không đổi.", "Rất hay đi với cặp trái ngược (`行くにしろ行かないにしろ`)."),
            ("〜といった", "Nêu ví dụ cụ thể rồi khép lại bằng danh từ chung.", "Bắt buộc phải có Danh từ đứng ngay sau `といった`."),
        ],
        "pitfalls": [
            "⚠️ Đừng nhầm `〜といった` (những thứ như là + N — Bài 10) với `〜といったら` (nói về mức độ — Bài 13).",
            "⚠️ Trong `〜にしても〜にしても`, vế sau phải mang nghĩa bao quát chung cho cả hai vế A và B."
        ],
        "quiz": [
            ("年末（ねんまつ）は大掃除（おおそうじ）（　　）年賀状（ねんがじょう）の準備（じゅんび）（　　）で忙（いそが）しい。", ["やら／やら", "というか／というか", "といった／といった", "にしろ／にしろ"], 1, "Nhiều việc dồn dập cuối năm gây bận rộn -> やら〜やら."),
            ("あの店（みせ）の雰囲気（ふんいき）は、素朴（そぼく）（　　）古（ふる）めかしい（　　）、独特（どくとく）の空気（くうき）がある。", ["というか／というか", "やら／やら", "にしても／にしても", "といった／といった"], 1, "Cân nhắc lựa chọn từ mô tả không khí quán -> というか〜というか."),
            ("賛成（さんせい）する（　　）反対（はんたい）する（　　）、まずは意見（いけん）を聞（き）かせてほしい。", ["にしろ／にしろ", "やら／やら", "というか／というか", "といった／といった"], 1, "Dù tán thành hay phản đối thì cũng muốn nghe ý kiến -> にしろ〜にしろ."),
            ("リンゴやバナナ（　　）果物（くだもの）は、ビタミンが豊富（ほうふ）だ。", ["といった", "やら", "にしても", "というか"], 1, "Nêu ví dụ cụ thể bổ nghĩa cho danh từ chung 果物 -> といった."),
            ("仕事（しごと）（　　）趣味（しゅみ）（　　）、無理（むり）をしすぎないことが大切（たいせつ）だ。", ["にしても／にしても", "やら／やら", "というか／というか", "といった／といった"], 1, "Dù là công việc hay sở thích đều cần tránh quá sức -> にしても〜にしても."),
        ]
    },
    11: {
        "title_jp": "〜に関係なく・無視して",
        "title_vi": "Bất Kể, Phớt Lờ & Tạm Gác Lại",
        "section": "II. 主観を含めて説明する",
        "intro": "Bài 11 trong **Shinkanzen Master Ngữ pháp N2** mở đầu phần II (diễn giải kèm chủ quan người nói) với 5 cấu trúc biểu thị **không liên quan/bất chấp** và **tạm gác sang một bên** (`〜を問わず`, `〜にかかわりなく・〜にかかわらず`, `〜もかまわず`, `〜はともかく（として）`, `〜はさておき`).",
        "patterns": [
            {
                "name": "1. 〜を問（と）わず",
                "meaning": "Bất kể / Không phân biệt (tuổi tác, giới tính, quốc tịch, kinh nghiệm, ngày đêm...).",
                "connection": "N + を問（と）わず",
                "examples": [
                    ("このアルバイトは、経験（けいけん）の有無（うむ）**を問（と）わず**応募（おうぼ）できます。", "Công việc làm thêm này không đòi hỏi có kinh nghiệm hay chưa, ai cũng ứng tuyển được."),
                    ("この店（みせ）は昼夜（ちゅうや）**を問（と）わず**お客（きゃく）さんでにぎわっている。", "Quán này bất kể ngày đêm lúc nào cũng đông khách."),
                ],
                "note": "Rất hay dùng trong văn bản tuyển dụng, thông báo quy định. Thường đi với danh từ bao hàm cặp đối lập (`男女・年齢・国籍・昼夜・晴雨`)."
            },
            {
                "name": "2. 〜にかかわりなく / 〜にかかわらず",
                "meaning": "Bất kể / Không phụ thuộc vào việc... (Dù thế nào kết quả cũng như nhau).",
                "connection": "N / V-る + V-ない / Aい + Aくない + にかかわりなく / にかかわらず",
                "examples": [
                    ("天候（てんこう）**にかかわらず**、明日（あす）の運動会（うんどうかい）は予定（よてい）通（どお）り行（おこな）います。", "Bất kể thời tiết thế nào, hội thao ngày mai vẫn tiến hành đúng kế hoạch."),
                    ("参加（さんか）するしない**にかかわりなく**、返事（へんじ）を出（だ）してください。", "Dù có tham gia hay không tham gia, xin hãy gửi phản hồi."),
                ],
                "note": "Linh hoạt hơn `を問わず` vì ghép được trực tiếp với cặp khẳng định–phủ định (`あるなしにかかわらず`, `好き嫌いにかかわらず`)."
            },
            {
                "name": "3. 〜も構（かま）わず",
                "meaning": "Mặc kệ / Chẳng thèm bận tâm đến... (Thường mang sắc thái phê phán hành động thiếu ý tứ, bất chấp làm người khác ngạc nhiên).",
                "connection": "N / Thể thông thường（+ の）+ も構（かま）わず",
                "examples": [
                    ("彼女（かのじょ）は人目（ひとめ）**も構（かま）わず**、駅（えき）のホームで大声（おおごえ）で泣（な）いた。", "Cô ấy mặc kệ ánh mắt mọi người xung quanh, khóc nức nở ngay trên sân ga."),
                    ("服（ふく）が汚（よご）れるの**も構（かま）わず**、子どもたちは泥（どろ）だらけになって遊（あそ）んでいる。", "Chẳng màng quần áo lấm bẩn, lũ trẻ cứ lấm lem bùn đất chơi đùa."),
                ],
                "note": "Khác `を問わず / にかかわらず` ở chỗ mang cảm xúc bất ngờ hoặc chê trách hành động bất chấp thiếu kiềm chế."
            },
            {
                "name": "4. 〜はともかく（として）",
                "meaning": "A thì tạm khoan bàn tới (A cũng đáng cân nhắc đấy nhưng tạm gác lại), điều B mới quan trọng/nổi bật hơn.",
                "connection": "N / Câu nghi vấn + はともかく（として）",
                "examples": [
                    ("味（あじ）**はともかく**、このレストランの雰囲気（ふんいき）は最高（さいこう）だ。", "Hương vị thì khoan bàn tới, nhưng bầu không khí của nhà hàng này thì tuyệt vời nhất."),
                    ("勝敗（しょうはい）**はともかくとして**、全力を出し切（き）ったことに意味（いみ）がある。", "Thắng thua tạm gác qua một bên, việc dốc hết toàn lực mới là điều có ý nghĩa."),
                ],
                "note": "Hay dùng khi muốn đánh giá vế B tốt hơn hoặc đáng ưu tiên hơn vế A."
            },
            {
                "name": "5. 〜はさておき",
                "meaning": "Tạm gác chuyện A sang một bên (để bước ngay vào vấn đề chính B).",
                "connection": "N + はさておき",
                "examples": [
                    ("冗談（じょうだん）**はさておき**、そろそろ本題（ほんだい）に入（はい）りましょう。", "Chuyện đùa tạm gác lại nhé, chúng ta mau bước vào vấn đề chính thôi."),
                    ("詳（くわ）しい説明（せつめい）**はさておき**、まずは結論（けつろん）から伝（つた）えます。", "Tạm gác phần giải thích chi tiết lại, trước hết tôi xin báo ngay kết luận."),
                ],
                "note": "Thường dùng để **chuyển mạch hội thoại/bài viết** từ chuyện phụ sang chuyện cốt lõi."
            },
        ],
        "comparison": [
            ("〜を問わず", "Quy định/tuyển dụng mang tính trang trọng.", "Chỉ đi với N phân loại/đối lập (`年齢`, `国籍`, `昼夜`)."),
            ("〜にかかわらず", "Kết quả không đổi bất chấp điều kiện.", "Đi được cả với cặp `V-る V-ない` (`行く行かない`)."),
            ("〜も構わず", "Phớt lờ lễ nghi/hệ lụy (sắc thái chê).", "Hay đi với `人目・時間・周囲・汚れ`."),
            ("〜はともかく / 〜はさておき", "Đều là \"gác A sang một bên\".", "`はともかく` nhấn mạnh B đáng chú ý hơn; `はさておき` nhấn mạnh chuyển sang chủ đề chính."),
        ],
        "pitfalls": [
            "⚠️ Không dùng `〜も構わず` trong thông báo tuyển dụng trang trọng (✗ `経験も構わず募集します` -> phải là `経験を問わず`).",
            "⚠️ `〜はともかく` thường có chút đánh giá về A (như \"dù A chưa tốt lắm nhưng B...\"), còn `〜はさておき` dùng để bỏ qua chuyện râu ria để vào việc chính."
        ],
        "quiz": [
            ("プロ・アマ（　　）、誰（だれ）でも自由（じゆう）に参加（さんか）できるコンテストだ。", ["を問（と）わず", "も構（かま）わず", "はさておき", "はともかく"], 1, "Thể lệ cuộc thi không phân biệt chuyên nghiệp hay nghiệp dư -> を問わず."),
            ("靴（くつ）が濡（ぬ）れるの（　　）、彼（かれ）は水（みず）たまりの中（なか）を走（はし）っていった。", ["も構（かま）わず", "を問（と）わず", "にかかわらず", "はさておき"], 1, "Mặc kệ giày ướt (động từ + の + も構わず) -> も構わず."),
            ("合格（ごうかく）するしない（　　）、試験（しけん）を受（う）けること自体（じたい）が良（よ）い経験（けいけん）になる。", ["にかかわらず", "を問（と）わず", "も構（かま）わず", "はさておき"], 1, "Đi sau cặp V-る V-ない (đỗ hay không đỗ) -> にかかわらず."),
            ("結果（けっか）（　　）、彼（かれ）が毎日（まいにち）努力（どりょく）していたことは事実（じじつ）だ。", ["はともかく", "も構（かま）わず", "を問（と）わず", "にかかわらず"], 1, "Kết quả tạm khoan xét, nhưng nỗ lực của anh ấy là sự thật -> はともかく."),
            ("雑談（ざつだん）（　　）、今日（きょう）の会議（かいぎ）の本題（ほんだい）に移（うつ）りましょう。", ["はさておき", "も構（かま）わず", "を問（と）わず", "にかかわらず"], 1, "Gác chuyện phiếm để chuyển sang nội dung chính -> はさておき."),
        ]
    },
    12: {
        "title_jp": "強く否定する・強く否定しない",
        "title_vi": "Phủ Định Mạnh & Phủ Định Một Phần",
        "section": "II. 主観を含めて説明する",
        "intro": "Bài 12 trong **Shinkanzen Master Ngữ pháp N2** xử lý sự khác biệt sống còn giữa **phủ định 100% (chắc chắn không thể)** và **phủ định một phần (không hẳn là)** (`〜わけがない`, `〜どころではない・〜どころか`, `〜ものか`, `〜わけではない`, `〜というものではない`).",
        "patterns": [
            {
                "name": "1. 〜わけがない",
                "meaning": "Tuyệt đối không thể nào / Làm gì có lý nào mà... (Phủ định 100% dựa trên lý lẽ thông thường).",
                "connection": "V-thông thường / Aい / Na-な（である） / N-の（である） + わけがない（わけはない）",
                "examples": [
                    ("漢字（かんじ）の読（よ）めない彼（かれ）に、こんな難（むずか）しい小説（しょうせつ）が読（よ）める**わけがない**。", "Cậu ta đến Kanji còn chẳng đọc được thì làm gì có chuyện đọc nổi cuốn tiểu thuyết khó thế này."),
                    ("まだ一度（いちど）も練習（れんしゅう）していないのに、試合（しあい）に勝（か）てる**わけがない**。", "Chưa luyện tập lấy một lần mà đòi thắng trận đấu thì đời nào có chuyện đó."),
                ],
                "note": "Phủ định hoàn toàn khả năng xảy ra (100% không)."
            },
            {
                "name": "2. 〜どころではない / 〜どころか",
                "meaning": "1) `どころではない`: Đang trong hoàn cảnh bận rộn/nguy cấp, chẳng còn tâm trí hay điều kiện đâu mà làm A; 2) `どころか`: Nói gì đến A, sự thật còn tệ/khác xa gấp bội (hoặc tốt hơn nhiều).",
                "connection": "V-る・V-ている / N + どころではない ｜ Thể thông thường / N + どころか",
                "examples": [
                    ("テスト前（まえ）で忙（いそが）しく、遊（あそ）ぶ**どころではない**。", "Sắp thi rồi bận túi bụi, chẳng còn tâm trí đâu mà chơi bời."),
                    ("給料（きゅうりょう）が上（あ）がる**どころか**、ボーナスまで減（へ）らされてしまった。", "Nói gì đến tăng lương, đến cả tiền thưởng cũng bị cắt giảm luôn rồi."),
                ],
                "note": "`どころではない` luôn nói về sự thiếu điều kiện/thời gian/tâm trí cho vế A; `どころか` so sánh thực tế vế B hoàn toàn trái ngược hoặc vượt xa vế A."
            },
            {
                "name": "3. 〜ものか",
                "meaning": "Làm gì có chuyện... / Đời nào mà... (Phủ định cảm tính, phản bác mạnh mẽ trong khẩu ngữ).",
                "connection": "V-thông thường / Aい / Na-な / N-な + ものか（もんか）",
                "examples": [
                    ("あんな失礼（しつれい）な店（みせ）へ、二度（にど）と行（い）く**ものか**。", "Cái quán bất lịch sự như thế, đời nào tôi thèm quay lại lần thứ hai chứ!"),
                    ("あいつが約束（やくそく）を守（まも）る**ものか**。いつも遅刻（ちこく）ばかりしているんだから。", "Làm gì có chuyện tên đó giữ lời hứa. Lần nào chẳng đi trễ."),
                ],
                "note": "Dạng văn nói thân mật hơn là `もんか`; thể hiện ý chí quyết không làm hoặc phủ định gay gắt."
            },
            {
                "name": "4. 〜わけではない / 〜というわけではない",
                "meaning": "Không hẳn là... / Không có nghĩa là... (Phủ định một phần, thanh minh tránh hiểu lầm).",
                "connection": "V-thông thường / Aい / Na-な（である） / N-という + わけではない",
                "examples": [
                    ("日本（にほん）料理（りょうり）が嫌（きら）いな**わけではない**が、毎日（まいにち）だと飽（あ）きてしまう。", "Không hẳn là tôi ghét món Nhật đâu, nhưng ngày nào cũng ăn thì ngán lắm."),
                    ("安（やす）ければ何でもいい**というわけではない**。品質（ひんしつ）も大切（たいせつ）だ。", "Không phải cứ rẻ là cái gì cũng được đâu. Chất lượng cũng quan trọng lắm chứ."),
                ],
                "note": "Rất hay dùng kèm `〜が、〜` để giải thích lý do thật sự đằng sau, tránh đối phương hiểu nhầm cực đoan."
            },
            {
                "name": "5. 〜というものではない / 〜というものでもない",
                "meaning": "Không phải hễ cứ... là được / Không thể đánh đồng cho rằng cứ... là đúng.",
                "connection": "Thể thông thường + というものではない / というものでもない",
                "examples": [
                    ("謝（あやま）ればそれで許（ゆる）される**というものではない**。", "Không phải cứ xin lỗi một tiếng là mọi chuyện đều được tha thứ đâu."),
                    ("お金（かね）さえあれば幸せになれる**というものでもない**。", "Cũng không thể khẳng định rằng hễ cứ có tiền là sẽ hạnh phúc."),
                ],
                "note": "Mang tính triết lý, nêu nhận định chung về quy luật cuộc sống chứ không chỉ chuyện cá nhân như `わけではない`."
            },
        ],
        "comparison": [
            ("〜わけがない", "Không đời nào (phủ định 100% logic).", "Không thể nào xảy ra."),
            ("〜わけではない", "Không hẳn là (phủ định một phần, đính chính).", "Trái ngược hoàn toàn về mức độ với `わけがない`!"),
            ("〜というものではない", "Không thể nói cứ thế là đúng (chân lý chung).", "Hay đi với câu điều kiện `〜ばいいというものではない`."),
            ("〜どころではない vs 〜どころか", "`どころではない`: không có tâm trí/điều kiện; `どころか`: trái lại hoàn toàn.", "Khác nhau hoàn toàn về cấu trúc vế sau."),
        ],
        "pitfalls": [
            "⚠️ BẪY KINH ĐIỂN NHẤT N2: Đừng bao giờ nhầm `〜わけがない` (tuyệt đối không thể) với `〜わけではない` (không hẳn là)!",
            "⚠️ Sau `〜というものではない` thường là nhận xét mang tính đạo lý/xã hội, hay ghép với cụm `〜ばいいというものではない`."
        ],
        "quiz": [
            ("甘いものが嫌（きら）いな（　　）が、ダイエット中（ちゅう）なので我慢（がまん）している。", ["わけがない", "わけではない", "どころか", "ものか"], 2, "Không hẳn là ghét đồ ngọt, chỉ là đang ăn kiêng -> わけではない."),
            ("昨日（きのう）まで元気（げんき）だった彼（かれ）が、そんな重病（じゅうびょう）である（　　）。", ["わけがない", "わけではない", "というものではない", "どころではない"], 1, "Phủ định hoàn toàn khả năng vô lý -> わけがない."),
            ("明後日（あさって）が締（し）め切（き）りなので、今（いま）は映画（えいが）を見（み）ている（　　）。", ["どころではない", "どころか", "わけではない", "わけがない"], 1, "Đang sát deadline không còn tâm trí/thời gian xem phim -> どころではない."),
            ("勉強（べんきょう）時間（じかん）が長（なが）ければいい（　　）。質（しつ）も重要（じゅうよう）だ。", ["というものではない", "わけがない", "ものか", "どころか"], 1, "Không phải cứ học thời gian dài là tốt -> というものではない."),
            ("日本語（にほんご）が上手（じょうず）になる（　　）、むしろ前（まえ）より話（はな）せなくなった気（き）がする。", ["どころか", "どころではない", "わけではない", "ものか"], 1, "Nói gì đến giỏi lên, ngược lại còn thấy nói kém hơn trước -> どころか."),
        ]
    },
    13: {
        "title_jp": "〜（話題）は",
        "title_vi": "Đưa Ra Chủ Đề & Liên Tưởng Cảm Xúc",
        "section": "II. 主観を含めて説明する",
        "intro": "Bài 13 trong **Shinkanzen Master Ngữ pháp N2** gồm 5 mẫu chuyên dùng để **đưa ra chủ đề bình luận, định nghĩa hoặc cảm thán ấn tượng mạnh về chủ đề đó** (`〜とは`, `〜といえば`, `〜というと・〜といったら`, `〜（のこと）となると`, `〜といったら`).",
        "patterns": [
            {
                "name": "1. 〜とは",
                "meaning": "1) Định nghĩa \"cái gọi là... chính là...\"; 2) Bày tỏ sự ngạc nhiên/cảm thán \"không ngờ lại có chuyện...\".",
                "connection": "N / Thể thông thường + とは",
                "examples": [
                    ("「幸福（こうふく）」**とは**、人（ひと）それぞれ感（かん）じ方（かた）が異（こと）なるものだ。", "Cái gọi là \"hạnh phúc\" là thứ mà mỗi người có cách cảm nhận khác nhau."),
                    ("あの無口（むくち）な彼（かれ）が、人前（ひとまえ）で歌（うた）う**とは**驚（おどろ）いた。", "Thật không ngờ một người ít nói như anh ấy lại hát trước đám đông."),
                ],
                "note": "Ở nghĩa (1) vế sau hay kết thúc bằng `〜のことだ`, `〜を意味する`; ở nghĩa (2) vế sau hay đi với `思わなかった`, `驚いた`, `信じられない`."
            },
            {
                "name": "2. 〜といえば",
                "meaning": "1) Nhắc đến... thì sực nhớ ra; 2) Nếu nói là... thì cũng đúng thật đấy nhưng... (nhượng bộ đồng tình một phần).",
                "connection": "N / Thể thông thường + といえば",
                "examples": [
                    ("京都（きょうと）**といえば**、来月（らいげつ）から友達（ともだち）が京都（きょうと）に転勤（てんきん）するんですよ。", "Nhắc tới Kyoto mới nhớ, tháng sau bạn tôi chuyển công tác về Kyoto đấy."),
                    ("便利（べんり）**といえば**便利（べんり）だが、値段（ねだん）が高（たか）すぎる。", "Nói tiện thì cũng đúng là tiện thật, nhưng giá đắt quá."),
                ],
                "note": "Trong cấu trúc lặp `AといえばAが...` có sắc thái \"nếu nói A thì cũng có phần đúng, nhưng...\"."
            },
            {
                "name": "3. 〜というと / 〜といえば / 〜といったら",
                "meaning": "Hễ nói tới A là liên tưởng ngay đến hình ảnh đặc trưng tiêu biểu B.",
                "connection": "N + というと / といえば / といったら",
                "examples": [
                    ("日本（にほん）の夏（なつ）の風物詩（ふうぶつし）**というと**、やはり花火（はなび）大会（たいかい）ですね。", "Nói tới nét đặc trưng mùa hè Nhật Bản thì hẳn là lễ hội pháo hoa nhỉ."),
                    ("北海道（ほっかいどう）**といえば**、広大（こうだい）な自然（しぜん）とおいしい海鮮（かいせん）料理（りょうり）が思（おも）い浮（う）かぶ。", "Hễ nhắc tới Hokkaido là liên tưởng ngay đến thiên nhiên bao la và hải sản tươi ngon."),
                ],
                "note": "Dùng để nêu đặc trưng nổi bật nhất khi nhắc đến một địa danh, khái niệm hoặc mùa trong năm."
            },
            {
                "name": "4. 〜（のこと）となると",
                "meaning": "Hễ cứ đụng đến chuyện của A là thái độ/hành động thay đổi hẳn (hăng hái hơn hoặc nghiêm túc khác thường).",
                "connection": "N（+ のこと） / V-る + となると",
                "examples": [
                    ("普段（ふだん）はおとなしい父（ちち）も、サッカーの試合（しあい）**となると**別人のように熱狂（ねっきょう）する。", "Bố tôi bình thường điềm đạm là thế, mà hễ cứ đụng tới trận bóng đá là cuồng nhiệt như người khác hẳn."),
                    ("自分（じぶん）の将来（しょうらい）**のこととなると**、誰（だれ）でも真剣（しんけん）に考（かんが）えざるを得（え）ない。", "Hễ liên quan tới tương lai của chính mình thì ai cũng buộc phải suy nghĩ nghiêm túc."),
                ],
                "note": "Nhấn mạnh sự thay đổi thái độ rõ rệt của một người khi chạm đúng chủ đề quan trọng/đam mê của họ."
            },
            {
                "name": "5. 〜といったら",
                "meaning": "Nói về mức độ của A thì thật không sao tả xiết (cảm thán kinh ngạc — có thể khen cực độ hoặc chê hết lời).",
                "connection": "N + といったら（ない）",
                "examples": [
                    ("テストに落（お）ちた時（とき）のショック**といったら**、言葉（ことば）では表（あらわ）せないほどだった。", "Nói về cú sốc lúc trượt kỳ thi thì quả thật không lời nào tả xiết."),
                    ("この部屋（へや）の汚（きたな）さ**といったら**、まるでゴミ箱（ばこ）のようだ。", "Cái sự bừa bộn của căn phòng này thật hết chỗ nói, trông chẳng khác nào bãi rác."),
                ],
                "note": "Cảm xúc dâng cao về mức độ; hay dùng trong dạng `名詞 + といったらない` hoặc đi với tính từ danh từ hóa (`〜さ`)."
            },
        ],
        "comparison": [
            ("〜とは", "Định nghĩa khái niệm hoặc ngạc nhiên trước điều khó tin.", "Vế sau thường là `〜のことだ` hoặc `〜とは思わなかった`."),
            ("〜といえば", "Mở liên tưởng hoặc chuyển chủ đề trong hội thoại.", "Cũng dùng kiểu lặp `〜といえば〜が` để công nhận một phần."),
            ("〜（のこと）となると", "Thay đổi thái độ hẳn khi nhắc tới đúng chủ đề đó.", "Luôn thể hiện sự chuyển biến thái độ khác ngày thường."),
            ("〜といったら", "Cảm thán mức độ cực lớn của N.", "Khác `〜といった` (liệt kê ví dụ — Bài 10)."),
        ],
        "pitfalls": [
            "⚠️ Chú ý phân biệt `〜といった + N` (ví dụ như — Bài 10) với `〜といったら` (cảm thán về mức độ — Bài 13).",
            "⚠️ Với `〜（のこと）となると`, vế sau thường phải thấy sự khác biệt rõ với bình thường (`別人のように`, `急に`, `目が輝く`)."
        ],
        "quiz": [
            ("あの穏（おだ）やかな田中（たなか）さんが人（ひと）を怒鳴（どな）りつける（　　）、よほどのことがあったのだろう。", ["とは", "といったら", "といえば", "となると"], 1, "Ngạc nhiên \"không ngờ người như vậy lại...\" -> とは."),
            ("彼女（かのじょ）は普段（ふだん）ケチなのに、推（お）しのアイドルのグッズ（　　）お金（かね）を惜（お）しまない。", ["となると", "とは", "といった", "といったら"], 1, "Hễ đụng tới đồ của thần tượng là thay đổi hẳn thái độ -> となると."),
            ("真夏（まなつ）の炎天下（えんてんか）で2時間（にじかん）待（ま）たされた時（とき）の暑（あつ）さ（　　）なかった。", ["といったら", "とは", "というと", "となると"], 1, "Cảm thán mức độ nóng không tả xiết: 暑さといったらなかった."),
            ("日本（にほん）の伝統（でんとう）スポーツ（　　）、まず相撲（すもう）を思い浮（う）かべる人（ひと）が多（おお）い。", ["というと", "とは", "となると", "といった"], 1, "Liên tưởng tiêu biểu nhất khi nhắc tới chủ đề -> というと."),
            ("「ボランティア」（　　）、見返（みかえ）りを求（もと）めずに社会（しゃかい）に貢献（こうけん）する活動（かつどう）のことだ。", ["とは", "といったら", "となると", "といえば"], 1, "Định nghĩa khái niệm -> とは."),
        ]
    },
}
