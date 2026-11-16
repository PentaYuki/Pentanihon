# -*- coding: utf-8 -*-
"""
Dữ liệu Ngữ Pháp Shinkanzen Master N2 (新完全マスター文法 N2)
Phần 2: 文の文法 2 (3 bài dấu sao ★)
Phần 3: 文章の文法 (12 bài ngữ pháp đoạn văn)
Phụ lục: Kính ngữ trọng tâm N2
"""

BUNPOU_PART2 = {
    1: {
        "title_jp": "文の組み立て―1 決まった形",
        "title_vi": "Lắp Ghép Câu (★) — 1. Khung Cấu Trúc Cố Định",
        "intro": "Phần 2 của **Shinkanzen Master Ngữ pháp N2** chuyên trị **Mondai 8 (bài tập dấu sao ★)**. Ở Bài 01, chúng ta nắm chắc bí quyết ghép các **khung cặp hô ứng cố định** (`〜だけでなく〜も`, `たとえ〜ても`, `〜か〜ないかのうちに`, `〜ほど〜はない`, `〜かというと〜そうではない`).",
        "strategies": [
            ("Khung cặp hô ứng phó từ", "`たとえ` … `ても` / `どんなに` … `ても` / `もし` … `なら` / `決して` … `ない` / `まさか` … `とは`", "Mỗi khi nhìn thấy phó từ ở vế đầu trong đề, tìm ngay mảnh ghép kết thúc tương ứng ở 4 lựa chọn!"),
            ("Khung so sánh & lựa chọn", "`〜というより〜` / `〜ほど〜はない` / `〜ば〜ほど` / `〜か〜ないかのうちに`", "Kiểm tra cặp động từ lặp lại hoặc cấu trúc định lượng để khóa chặt vị trí 2 mảnh."),
            ("Khung `〜だけでなく〜も` & `〜ばかりか〜まで`", "Xác định vế có `も / まで / さえ` nằm SAU vế `だけでなく / ばかりか`.", "Tuyệt đối không đảo ngược hai vế làm gãy logic tăng tiến.")
        ],
        "star_exercises": [
            (
                "どんなに ______  ______  __★__  ______ ならない。",
                ["こと", "があっても", "大変（たいへん）な", "諦（あきら）めては"],
                [3, 1, 2, 4],
                2,
                "どんなに **大変（たいへん）な(3)** **こと(1)★** **があっても(2)** **諦（あきら）めては(4)** ならない。",
                "`どんなに + Naな + N + があっても` là khung cố định hô ứng với `〜てはならない`."
            ),
            (
                "彼（かれ）は英語（えいご） ______  ______  __★__  ______ いる。",
                ["日本語（にほんご）", "ばかりか", "まで流暢（りゅうちょう）に", "話（はな）せて"],
                [2, 1, 3, 4],
                3,
                "彼（かれ）は英語（えいご） **ばかりか(2)**、**日本語（にほんご）(1)** **まで流暢（りゅうちょう）に(3)★** **話（はな）せて(4)** いる。",
                "Khung tăng tiến `N1 + ばかりか + N2 + まで`."
            ),
            (
                "仕事（しごと） ______  ______  __★__  ______ に限（かぎ）る。",
                ["でも", "に関（かん）して", "迷（まよ）ったら", "先輩（せんぱい）に相談（そうだん）する"],
                [2, 3, 4, 1],
                4,
                "仕事（しごと） **に関（かん）して(2)** **迷（まよ）ったら(3)**、**先輩（せんぱい）に相談（そうだん）する(4)★** **でも(1)**（※Wait: hãy chỉnh lại thành phương án chuẩn tự nhiên: `誰（だれ）かに相談（そうだん）する` hoặc `早く聞く`）"
            ),
        ]
    },
    2: {
        "title_jp": "文の組み立て―2 名詞を説明する形式",
        "title_vi": "Lắp Ghép Câu (★) — 2. Mệnh Đề Bổ Nghĩa Danh Từ",
        "intro": "Bài 02 Phần 2 tập trung vào bẫy lớn nhất của bài dấu sao ★: **xác định danh từ trung tâm và chuỗi định ngữ đứng trước bổ nghĩa cho danh từ đó** (các cụm `〜に関する N`, `〜をめぐる N`, `〜に基づく N`, `〜という N`, `〜といった N`).",
        "strategies": [
            ("Quy tắc 'Đuôi từ chỉ hình thái đứng trước N'", "Các mẫu có dạng liên thể (`〜に関する`, `〜をめぐる`, `〜に基づく`, `〜にあたっての`, `〜としての`, `〜における`) LUÔN phải đứng ngay trước Danh từ.", "Nếu thấy `〜に関する` hoặc `〜をめぐる` ở lựa chọn, tìm ngay Danh từ mà nó bổ nghĩa để khóa thành 1 cặp dính liền!"),
            ("Phân biệt trợ từ `の` và `が` trong mệnh đề định ngữ", "Chủ ngữ của mệnh đề bổ nghĩa danh từ có thể dùng `が` hoặc `の` (`私の書いた本` = `私が書いた本`).", "Cẩn thận đừng tách nhầm `N1 の N2` khi thực chất `N1 の` là chủ ngữ của động từ phía sau."),
            ("Nhóm `〜という N`", "`という` đứng giữa nội dung giải thích/tên gọi và Danh từ (`〜という噂`, `〜という意味`, `〜という意見`).", "Luôn kiểm tra mệnh đề trước `という` phải ở thể thông thường.")
        ],
        "star_exercises": [
            (
                "駅前（えきまえ）の ______  ______  __★__  ______ 行（おこな）われた。",
                ["再開発（さいかいはつ）", "会議（かいぎ）が", "をめぐる", "住民（じゅうみん）たちの"],
                [1, 3, 4, 2],
                4,
                "駅前（えきまえ）の **再開発（さいかいはつ）(1)** **をめぐる(3)** **住民（じゅうみん）たちの(4)★** **会議（かいぎ）が(2)** 行（おこな）われた。",
                "`N + をめぐる` phải đứng trước danh từ chỉ cuộc họp/tranh luận (`住民たちの会議`)."
            ),
            (
                "実際（じっさい）の ______  ______  __★__  ______ 書（か）かれた本（ほん）だ。",
                ["調査（ちょうさ）データ", "詳（くわ）しく", "に基（もと）づいて", "日本（にほん）の経済（けいざい）について"],
                [1, 3, 4, 2],
                4,
                "実際（じっさい）の **調査（ちょうさ）データ(1)** **に基（もと）づいて(3)** **日本（にほん）の経済（けいざい）について(4)★** **詳（くわ）しく(2)** 書（か）かれた本（ほん）だ。",
                "Cụm phương tiện căn cứ `データに基づいて` bổ nghĩa cho động từ bị động `書かれた`."
            ),
            (
                "この問題（もんだい）を ______  ______  __★__  ______ 必要（ひつよう）がある。",
                ["解決（かいけつ）する", "工夫（くふう）をする", "ための", "さまざまな"],
                [1, 3, 4, 2],
                4,
                "この問題（もんだい）を **解決（かいけつ）する(1)** **ための(3)** **さまざまな(4)★** **工夫（くふう）をする(2)** 必要（ひつよう）がある。",
                "`解決するための` + tính từ `さまざまな` + danh từ `工夫をする` + `必要がある`."
            ),
        ]
    },
    3: {
        "title_jp": "文の組み立て―3 「〜ない」がつく文法形式",
        "title_vi": "Lắp Ghép Câu (★) — 3. Cụm Ngữ Pháp Chứa 「〜ない」",
        "intro": "Bài 03 Phần 2 giải mã các câu dấu sao ★ có chứa `ない`, `ず`, `まい` (`〜ないことには`, `〜ないわけにはいかない`, `〜ざるを得ない`, `〜ずにはいられない`, `〜ことはない`, `〜わけではない`). Đây là dạng câu thí sinh hay xếp ngược vị trí nhất!",
        "strategies": [
            ("Nhận diện khung 2 phần chứa `ない`", "`〜ないことには〜ない` (vế đầu phủ định, vế cuối cũng phủ định); `〜てからでないと〜ない`.", "Nếu đề đã in sẵn động từ phủ định ở cuối câu, đặt `〜ないことには` hoặc `〜てからでないと` ở giữa."),
            ("Cẩn thận phủ định kép `ないわけにはいかない`", "`V-ない + わけにはいかない` (= buộc phải làm) hay tách mảnh `わけ` và `にはいかない` thành 2 ô riêng.", "Luôn kiểm tra xem câu muốn nói \"không thể làm\" (`V-る + わけにはいかない`) hay \"buộc phải làm\" (`V-ない + わけにはいかない`)."),
            ("Các mẫu kết thúc bằng `〜ない` đứng cuối", "`〜にすぎない`, `〜にほかならない`, `〜かもしれない`, `〜ざるを得ない`, `〜に違いない`.", "Ghép đúng phần nối trước chúng: `V-ます` hay `V-ない (bỏ ない)` hay `N`.")
        ],
        "star_exercises": [
            (
                "実際（じっさい）に ______  ______  __★__  ______ 分（わ）からない。",
                ["良（よ）さは", "使（つか）って", "ことには", "みない"],
                [2, 4, 3, 1],
                3,
                "実際（じっさい）に **使（つか）って(2)** **みない(4)** **ことには(3)★** **良（よ）さは(1)** 分（わ）からない。",
                "`V-て + みない + ことには + ... + 分からない`."
            ),
            (
                "先輩（せんぱい）から ______  ______  __★__  ______ いかない。",
                ["仕事（しごと）なので", "わけには", "引（ひ）き受（う）けない", "頼（たの）まれた"],
                [4, 1, 3, 2],
                3,
                "先輩（せんぱい）から **頼（たの）まれた(4)** **仕事（しごと）なので(1)** **引（ひ）き受（う）けない(3)★** **わけには(2)** いかない。",
                "Phủ định kép: được tiền bối nhờ nên không thể không nhận (`引き受けない + わけには + いかない`)."
            ),
            (
                "台風（たいふう）が ______  ______  __★__  ______ 得（え）ない。",
                ["ため", "中止（ちゅうし）せ", "ざるを", "近（ちか）づいている"],
                [4, 1, 2, 3],
                2,
                "台風（たいふう）が **近（ちか）づいている(4)** **ため(1)** **中止（ちゅうし）せ(2)★** **ざるを(3)** 得（え）ない。",
                "`する + ざるを得ない` -> `せざるを得ない` tách thành `中止せ` + `ざるを` + `得ない`."
            ),
        ]
    },
}

# Fix Exercise 3 of Part 2 Lesson 1 cleanly
BUNPOU_PART2[1]["star_exercises"][2] = (
    "どんな ______  ______  __★__  ______ の大切（たいせつ）なルールだ。",
    ["仕事（しごと）", "でも", "守（まも）るべき", "において"],
    [1, 4, 2, 3],
    2,
    "どんな **仕事（しごと）(1)** **において(4)★** **でも(2)** **守（まも）るべき(3)** の大切（たいせつ）なルールだ。",
    "Wait—`守るべき` trước `の` phải có danh từ! Hãy chỉnh lại thành câu thật mượt chuẩn JLPT N2:"
)
BUNPOU_PART2[1]["star_exercises"][2] = (
    "失敗（しっぱい）を ______  ______  __★__  ______ ことが重要（じゅうよう）だ。",
    ["次（つぎ）に", "恐（おそ）れる", "のではなく", "生（い）かす"],
    [2, 3, 1, 4],
    1,
    "失敗（しっぱい）を **恐（おそ）れる(2)** **のではなく(3)** **次（つぎ）に(1)★** **生（い）かす(4)** ことが重要（じゅうよう）だ。",
    "Khung tương phản `AのではなくB`: Không phải sợ thất bại mà là tận dụng cho lần sau."
)

BUNPOU_PART3 = {
    1: {
        "title_jp": "始めと終わりが正しく対応した文",
        "title_vi": "Tương Ứng Đầu – Cuối Trong Câu Văn",
        "summary": "Mondai 9 thường kiểm tra lỗi **đầu voi đuôi chuột** trong câu dài: chủ ngữ và vị ngữ không khớp nhau, hoặc phó từ mở đầu không tương thích với kết thúc câu.",
        "points": [
            "**Chủ ngữ – Vị ngữ khớp nhau:** Nếu đầu câu là `〜理由は...` (Lý do là...), cuối câu PHẢI là `〜からだ` hoặc `〜ためだ` (vì...). Nếu đầu câu là `〜特徴は...` (Đặc trưng là...), cuối câu là `〜ことだ`.",
            "**Phó từ hô ứng bắt buộc:** `なぜなら〜からだ`, `もし〜たら/ば`, `たとえ〜ても`, `決して〜ない`, `おそらく〜だろう`, `まるで〜ようだ`.",
            "**Tránh gãy cấu trúc liệt kê:** Khi liệt kê nhiều cụm `〜たり〜たり`, `〜し〜し`, kiểm tra đuôi tổng kết phải khớp (`〜たりする`, `〜のだ`)."
        ],
        "passage_jp": """日本（にほん）で一人（ひとり）暮（ぐ）らしを始（はじ）める人（ひと）が増（ふ）えている理由（りゆう）は、進学（しんがく）や就職（しゅうしょく）を機（き）に親元（おやもと）を離（はな）れる若者（わかもの）が多（おお）い（　1　）。また、高齢者（こうれいしゃ）の単独（たんどく）世帯（せたい）が増加（ぞうか）していることも大きな要因（よういん）だ。""",
        "question": "Chỗ trống (1) chọn đáp án nào để khớp đúng với chủ ngữ `理由は` ở đầu câu?",
        "options": ["からだ", "ことだ", "わけだ", "ものだ"],
        "answer": 1,
        "explanation": "Đầu câu mở bằng `〜理由は` (Lý do là...), nên cuối câu bắt buộc chốt bằng `〜からだ` (là bởi vì...)."
    },
    2: {
        "title_jp": "時制",
        "title_vi": "Sự Thống Nhất Về Thì (Thời Gian) Trong Đoạn Văn",
        "summary": "Bài 02 Phần 3 giúp em phân biệt cách chuyển đổi giữa thì quá khứ (`〜た`, `〜ていた`) và thì hiện tại/tương lai (`〜る`, `〜ている`) trong bài tường thuật và bài nghị luận.",
        "points": [
            "**Bài tường thuật trải nghiệm (quá khứ):** Các sự kiện đã xảy ra dùng `〜た / 〜ていた`, nhưng khi chuyển sang **nhận xét chung, chân lý hoặc cảm nghĩ hiện tại của người viết** phải chuyển về `〜る / 〜ている / 〜のだ`.",
            "**Thì trong mệnh đề bổ nghĩa:** `駅（えき）に着（つ）いた時（とき）` (lúc đã tới ga) vs `駅（えき）に着（つ）く前（まえ）に` (trước khi tới ga — kể cả chuyện đã qua vẫn dùng `V-る + 前に`!).",
            "**Lưu ý `〜てきた` vs `〜ていく`:** Kể diễn biến từ quá khứ đến nay dùng `〜てきた`, dự đoán tương lai dùng `〜ていくだろう`."
        ],
        "passage_jp": """昨日（きのう）、初（はじ）めて京都（きょうと）の古本（ふるほん）屋（や）を訪（おとず）れた。店（みせ）に入（はい）る（　1　）、古（ふる）い紙（かみ）と墨（すみ）の懐（なつ）かしい匂（にお）いがした。""",
        "question": "Chỗ trống (1) điền hình thức thì nào cho tự nhiên?",
        "options": ["と", "たところ", "前に", "ので"],
        "answer": 1,
        "explanation": "Kể khoảnh khắc bước vào tiệm và ngay sau đó cảm nhận mùi hương -> `入る + と` (hoặc nếu dùng `た` thì là `入ったところ`). Ở đây 4 lựa chọn chỉ có `と` nối sau `V-る`."
    },
    3: {
        "title_jp": "条件を表す文",
        "title_vi": "Câu Điều Kiện Trong Mạch Đoạn Văn (と・ば・たら・なら)",
        "summary": "Trong đoạn văn dài, đề thi Mondai 9 thường đánh vào sự khác biệt giữa 4 dạng điều kiện `と`, `ば`, `たら`, `なら` và ý nghĩa ngữ cảnh phía sau.",
        "points": [
            "**`〜と`:** Kết quả tất yếu tự nhiên hoặc phát hiện bất ngờ ở quá khứ (`窓を開けると雪だった`). KHÔNG dùng với ý chí/mệnh lệnh ở vế sau.",
            "**`〜ば`:** Điều kiện giả định chung, chân lý hoặc câu tục ngữ (`練習すれば上手になる`).",
            "**`〜たら`:** Linh hoạt nhất, dùng được cho giả định 1 lần cụ thể và cả câu mệnh lệnh/nhờ vả (`家に着いたら電話して`).",
            "**`〜なら`:** Dựa trên tiền đề lời nói/dự định của đối phương để đưa lời khuyên (`日本へ行くなら京都がおすすめだ`)."
        ],
        "passage_jp": """もし日本（にほん）の伝統（でんとう）文化（ぶんか）に興味（きょうみ）がある（　1　）、一度（いちど）金沢（かなざわ）を訪（おとず）れてみるといい。古（ふる）い街並（まちな）みがそのまま残（のこ）っている。""",
        "question": "Chỗ trống (1) dùng mẫu điều kiện nào để đưa lời khuyên dựa trên giả định sở thích người đọc?",
        "options": ["なら", "と", "たり", "ものの"],
        "answer": 1,
        "explanation": "Đưa ra gợi ý/lời khuyên dựa trên điều kiện giả định \"Nếu như có hứng thú...\" -> `なら` (hoặc `のなら`)."
    },
    4: {
        "title_jp": "視点を動かさない手段―1 動詞の使い方（自動詞・他動詞）",
        "title_vi": "Giữ Vững Điểm Nhìn — 1. Tự Động Từ & Tha Động Từ",
        "summary": "Văn phong Nhật Bản rất coi trọng **tính nhất quán của chủ ngữ/điểm nhìn (視点の一貫性)**. Việc chọn Tự động từ hay Tha động từ quyết định chủ thể hành động có đồng nhất xuyên suốt đoạn văn hay không.",
        "points": [
            "**Giữ cùng chủ ngữ làm trục chính:** Nếu cả đoạn đang nói về \"cửa hàng / máy móc / sự vật\", hãy dùng Tự động từ (`店が開く`, `システムが動く`) thay vì đột ngột chuyển sang Tha động từ.",
            "**Nếu chủ ngữ là người tác động:** Dùng Tha động từ (`店員がドアを開ける`) để mạch câu không nhảy chủ ngữ đột ngột.",
            "**Thể trạng thái kết quả:** `〜ている` (tự động từ: trạng thái đang còn `電気がついている`) vs `〜てある` (tha động từ: đã được ai chuẩn bị sẵn `電気がつけてある`)."
        ],
        "passage_jp": """最近（さいきん）、スマートフォンを使（つか）う時間（じかん）が長（なが）くなりすぎて、視力（しりょく）が（　1　）人（ひと）が増（ふ）えているそうだ。""",
        "question": "Chỗ trống (1) chọn Tự động từ hay Tha động từ cho khớp chủ ngữ `視力が`?",
        "options": ["落（お）ちる", "落（お）とす", "落（お）とした", "落（お）とさせる"],
        "answer": 1,
        "explanation": "Trợ từ `が` đi với `視力` (thị lực tự suy giảm) -> phải dùng Tự động từ `落ちる` (không dùng tha động từ `落とす`)."
    },
    5: {
        "title_jp": "視点を動かさない手段―2 「〜てくる・〜ていく」",
        "title_vi": "Giữ Vững Điểm Nhìn — 2. Hướng Chuyển Động 「〜てくる・〜ていく」",
        "summary": "Bài 05 Phần 3 giúp em phân biệt hướng không gian và dòng thời gian của `〜てくる` (hướng về phía người nói / từ quá khứ tới hiện tại) và `〜ていく` (đi ra xa người nói / từ hiện tại hướng tới tương lai).",
        "points": [
            "**Dòng thời gian:** Từ quá khứ kéo dài đến hiện tại dùng `〜てきた` (`これまで努力してきた`). Từ hiện tại tiếp diễn ra tương lai dùng `〜ていく` (`これからも続けていく`).",
            "**Sự xuất hiện / bắt đầu:** Hiện tượng mới xuất hiện, cảm xúc nảy sinh hướng vào nhận thức người nói dùng `〜てくる` (`雨が降ってきた`, `見えてきた`).",
            "**Sự biến mất / xa dần:** Hiện tượng mờ dần, biến mất khỏi tầm mắt dùng `〜ていく` (`消えていった`)."
        ],
        "passage_jp": """今後（こんご）、少子（しょうし）高齢化（こうれいか）はますます進（すす）んで（　1　）だろう。私（わたし）たちは早（はや）めに対策（たいさく）を考（かんが）えなければならない。""",
        "question": "Chỗ trống (1) nói về diễn biến từ nay về tương lai (`今後`) nên chọn đáp án nào?",
        "options": ["いく", "くる", "いた", "きた"],
        "answer": 1,
        "explanation": "Có từ chỉ tương lai `今後` và `〜だろう` -> diễn biến tiến tới tương lai dùng `〜ていく`."
    },
    6: {
        "title_jp": "視点を動かさない手段―3 受身・使役・使役受身",
        "title_vi": "Giữ Vững Điểm Nhìn — 3. Bị Động, Sai Khiến & Sai Khiến Bị Động",
        "summary": "Để không phải đổi chủ ngữ giữa chừng từ \"Tôi\" sang \"Người khác\", tiếng Nhật ưu tiên giữ \"Tôi / nhân vật chính\" làm chủ ngữ xuyên suốt bằng cách dùng **Thể Bị Động (受身)** hoặc **Sai khiến bị động (使役受身)**.",
        "points": [
            "**Giữ nhân vật chính làm chủ ngữ:** Thay vì `私は友だちに会った。友だちが私をほめた`, viết mượt thành `私は友だちにほめられた`.",
            "**Bị động gián tiếp (bị làm phiền):** `雨に降られた`, `隣の人にタバコを吸われて困った`.",
            "**Sai khiến bị động (`〜させられる`):** Diễn tả việc bị ép buộc làm, hoặc tự nhiên bị thôi thúc (`深く考えさせられた` = bị thôi thúc phải suy ngẫm sâu sắc)."
        ],
        "passage_jp": """昨日（きのう）はせっかく新（あたら）しい靴（くつ）をはいて出（で）かけたのに、途中（とちゅう）で急（きゅう）な雨（あめ）に（　1　）、びしょ濡（ぬ）れになってしまった。""",
        "question": "Chỗ trống (1) giữ chủ ngữ là người đi ra ngoài và thể hiện bị mưa làm phiền -> chọn gì?",
        "options": ["降（ふ）られて", "降（ふ）って", "降（ふ）らせて", "降（ふ）られさせて"],
        "answer": 1,
        "explanation": "Bị động gây phiền toái với chủ thể `私`: `雨に降られて`."
    },
    7: {
        "title_jp": "視点を動かさない手段―4 「〜てあげる・〜てもらう・〜てくれる」",
        "title_vi": "Giữ Vững Điểm Nhìn — 4. Cho Nhận Hành Động (授受表現)",
        "summary": "Bài 07 Phần 3 là trọng tâm hay sai nhất trong Mondai 9: phân biệt ai làm cho ai và kính ngữ của 3 động từ cho-nhận (`てさしあげる・ていただく・てくださる`).",
        "points": [
            "**`〜てあげる / さしあげる`:** Chủ ngữ (mình/người thân) làm ơn cho người khác. Chú ý không dùng `さしあげる` trực tiếp với cấp trên khi tự khoe mình làm gì; lịch sự hãy nói `〜ましょうか`.",
            "**`〜てもらう / いただく`:** Chủ ngữ (mình/người nhận ơn) nhận được hành động từ người khác (`先生に添削していただいた`).",
            "**`〜てくれる / くださる`:** Chủ ngữ là người khác (tốt bụng làm cho mình/phe mình) (`先生が丁寧に教えてくださった`)."
        ],
        "passage_jp": """進路（しんろ）について悩（なや）んでいた時（とき）、担任（たんにん）の先生（せんせい）が親身（しんみ）になって相談（そうだん）に乗（の）って（　1　）。""",
        "question": "Chủ ngữ là `担任の先生` (người bề trên thực hiện hành động giúp mình) -> chọn?",
        "options": ["くださった", "いただいた", "さしあげた", "あげた"],
        "answer": 1,
        "explanation": "Thầy giáo chủ nhiệm (`先生 + が`) làm cho mình -> tôn kính ngữ của `てくれた` là `てくださった`."
    },
    8: {
        "title_jp": "指示表現「こ・そ・あ」の使い分け",
        "title_vi": "Cách Dùng Từ Chỉ Định 「こ・そ・あ」 Trong Văn Bản",
        "summary": "Trong bài đọc và Mondai 9, **こ・そ・あ** không chỉ chỉ khoảng cách vật lý mà tuân theo quy tắc chỉ định mạch văn bản (文脈指示) chặt chẽ!",
        "points": [
            "**`こ〜` (これ・この・こう):** Chỉ sự việc ngay trước đó mà **tác giả muốn nhấn mạnh, đưa ra làm trọng tâm thảo luận tiếp** hoặc điều vừa tự mình trình bày.",
            "**`そ〜` (それ・その・そう):** Chỉ điều vừa được nhắc đến ở câu trước một cách **trung tính, khách quan** (hoặc điều chỉ bên người nghe biết, người nói không trải nghiệm trực tiếp).",
            "**`あ〜` (あれ・あの):** Chỉ ký ức, kiến thức chung mà cả người nói và người nghe đều từng cùng biết/trải nghiệm (hầu như không dùng để chỉ đoạn văn vừa viết trong văn nghị luận trừ hồi ức)."
        ],
        "passage_jp": """「失敗（しっぱい）は成功（せいこう）のもと」という言葉（ことば）がある。しかし、（　1　）は単（たん）に失敗（しっぱい）をすればいいという意味（いみ）ではない。""",
        "question": "Chỗ trống (1) quy chiếu lại câu tục ngữ vừa nêu ở câu ngay trước -> chọn?",
        "options": ["それ", "あれ", "どれ", "どこ"],
        "answer": 1,
        "explanation": "Quy chiếu lại câu trích dẫn vừa xuất hiện trước đó một cách khách quan để giải thích tiếp -> `それ` (trong câu văn viết không dùng `あれ` cho trích dẫn vừa nêu)."
    },
    9: {
        "title_jp": "「は・が」の使い分け",
        "title_vi": "Phân Biệt Trợ Từ 「は」 Và 「が」 Trong Đoạn Văn",
        "summary": "Nắm rõ quy luật thông tin cũ (`は`) – thông tin mới (`が`) giúp em chọn đúng 100% các câu kiểm tra trợ từ trong Mondai 9.",
        "points": [
            "**Giới thiệu nhân vật/thông tin MỚI lần đầu:** dùng `が` (`昔々、ある所におじいさんが住んでいた`). Khi nhắc lại từ câu thứ 2 trở đi thành **chủ đề đã biết**: chuyển sang `は` (`おじいさんは毎日山へ行った`).",
            "**Miêu tả hiện tượng trước mắt / mệnh đề phụ:** Hiện tượng tự nhiên dùng `が` (`雨が降ってきた`); mệnh đề phụ bổ nghĩa danh từ hoặc mệnh đề thời gian `〜と / 〜たら / 〜とき` ưu tiên `が` (`私が作った料理`).",
            "**Đối chiếu hai vế:** Dùng `は` để đối chiếu (`肉は食べるが、魚は食べない`)."
        ],
        "passage_jp": """公園（こうえん）のベンチに一匹（いっぴき）の猫（ねこ）が座（すわ）っていた。その猫（ねこ）（　1　）とても人懐（ひとなつ）っこく、私（わたし）の足元（あしもと）に近（ちか）づいてきた。""",
        "question": "Câu 1 đã giới thiệu `一匹の猫が`. Sang câu 2 nhắc lại `その猫` làm chủ đề -> dùng?",
        "options": ["は", "を", "に", "で"],
        "answer": 1,
        "explanation": "Chủ thể đã được giới thiệu ở câu trước (`その猫`) trở thành chủ đề đã biết -> dùng `は`."
    },
    10: {
        "title_jp": "接続表現",
        "title_vi": "Từ Nối & Liên Từ Chuyển Mạch Đoạn Văn",
        "summary": "Bài 10 Phần 3 tổng hợp toàn bộ nhóm từ nối kinh điển thường ra trong cả **Mondai 9 (Ngữ pháp đoạn văn)** lẫn **Đọc hiểu**!",
        "points": [
            "**Nghịch lý / Chuyển hướng:** `しかし`, `だが`, `ところが` (bất ngờ trái dự đoán), `けれども`, `それにしても` (dẫu vậy nhưng...).",
            "**Nhân quả:** `したがって` (do đó — văn viết), `そのため` (vì thế), `それゆえ` (chính vì vậy), `なぜなら〜からだ` (bởi vì...).",
            "**Tóm tắt / Diễn giải:** `つまり` (tóm lại), `すなわち` (tức là), `言い換えれば` (nói cách khác).",
            "**Bổ sung / Khác biệt:** `また`, `さらに` (hơn thế nữa), `ただし` (tuy nhiên kèm điều kiện ngoại lệ), `なお` (xin lưu ý thêm), `もっとも` (tuy nhiên nói thêm cho công bằng)."
        ],
        "passage_jp": """インターネットでいつでも情報（じょうほう）が調（しら）べられるようになり、生活（せいかつ）は大変（たいへん）便利（べんり）になった。（　1　）、誤（あやま）った情報（じょうほう）に惑（まど）わされる危険（きけん）も増（ふ）えている。""",
        "question": "Chỗ trống (1) chuyển từ mặt tích cực sang mặt tiêu cực đối lập -> chọn từ nối nào?",
        "options": ["しかし", "したがって", "つまり", "なぜなら"],
        "answer": 1,
        "explanation": "Mở đầu bằng sự tiện lợi, sau đó nêu nguy cơ trái chiều -> từ nối chuyển ý nghịch đảo `しかし` (hoặc `一方で`)."
    },
    11: {
        "title_jp": "省略・繰り返し・言い換え",
        "title_vi": "Lược Bỏ, Lặp Lại & Diễn Đạt Tương Đương",
        "summary": "Trong tiếng Nhật, một câu văn tự nhiên sẽ tránh lặp danh từ thô cứng bằng cách lược bỏ hợp lý hoặc dùng từ đồng nghĩa/chỉ thị (`こうした`, `このような`) và danh từ hóa (`〜こと`, `〜の`).",
        "points": [
            "**Lược bỏ chủ ngữ quen thuộc:** Nếu chủ ngữ vẫn là người/vật đang bàn ở câu trước, không cần lặp lại `私は〜` ở mọi câu.",
            "**Danh từ hóa để nối ý:** Dùng `こうした取り組み`, `このような状況` thay vì chép nguyên lại cả mệnh đề dài.",
            "**Dùng cặp `〜のだ` / `〜のである`:** Kết nối câu sau làm lời giải thích nguyên nhân/ý nghĩa cho câu trước."
        ],
        "passage_jp": """環境（かんきょう）を守るために、ごみ分別（ぶんべつ）の徹底（てってい）やマイバッグの持参（じさん）などができる。（　1　）地道（じみち）な取（と）り組（く）みの積（つ）み重（かさ）ねが大切（たいせつ）だ。""",
        "question": "Chỗ trống (1) tóm gọn các hành động vừa liệt kê ở câu trước -> chọn?",
        "options": ["こうした", "ああした", "どちらの", "どうした"],
        "answer": 1,
        "explanation": "`こうした + N` (Những nỗ lực như thế này) dùng để tóm tắt lại chuỗi hành động vừa nêu ngay trước đó."
    },
    12: {
        "title_jp": "文体の一貫性",
        "title_vi": "Sự Thống Nhất Văn Phong (だ・である vs です・ます)",
        "summary": "Bài 12 Phần 3 giúp em nhận ra bẫy cuối cùng của Mondai 9: **toàn bộ một đoạn văn phải đồng nhất văn phong** (Thể thông thường `だ・である` hoặc Thể lịch sự `です・ます`), và phân biệt văn viết với văn nói.",
        "points": [
            "**Bài luận, báo chí, bình luận:** Thống nhất dùng thể `だ・である` (không tự nhiên xen lẫn `〜ます` vào câu cuối trừ câu trích dẫn hội thoại trong ngoặc `「〜」`).",
            "**Thư từ, thông báo hướng tới người đọc, email:** Thống nhất dùng `です・ます`.",
            "**Tránh lẫn văn nói vào văn viết trang trọng:** Không dùng `〜ちゃう`, `〜てる`, `〜けど`, `〜なんか` trong đoạn văn viết kiểu `〜である` (phải dùng `〜てしまう`, `〜ている`, `〜が`, `〜など`)."
        ],
        "passage_jp": """近年（きんねん）、電子（でんし）書籍（しょせき）を利用（りよう）する人が増（ふ）えている。紙（かみ）の本（ほん）と違（ちが）い、何百（なんびゃく）冊（さつ）もの本（ほん）を気軽（きがる）に持（も）ち歩（ある）ける点が魅力（みりょく）（　1　）。""",
        "question": "Đoạn văn đang viết theo thể `〜ている` (thể thường/văn viết). Chỗ trống (1) điền gì cho nhất quán văn phong?",
        "options": ["である", "であります", "ですね", "だよね"],
        "answer": 1,
        "explanation": "Toàn bài sử dụng văn phong luận văn `だ・である` nên câu kết phải thống nhất dùng `である` (không dùng `ですね` hay `であります`)."
    },
}

KEIGO_APPENDIX = {
    "title": "Phụ Lục Ngữ Pháp N2: Hệ Thống Kính Ngữ (敬語) Trọng Tâm",
    "intro": "Ngoài 26 bài Phần 1, 3 bài Phần 2 và 12 bài Phần 3 của **Shinkanzen Master Ngữ pháp N2**, kính ngữ (`敬語`) xuất hiện dày đặc trong cả Phần Ngữ pháp (Mondai 7, 9), Nghe hiểu (Sokuji Outou) và Đọc hiểu email công sở. Dưới đây là bảng tra cứu chuẩn xác nhất!",
    "table": [
        ("する", "なさる / される", "いたす", "Làm"),
        ("行く / 来る", "いらっしゃる / おいでになる", "参（まい）る / 伺（うかが）う", "Đi / Đến"),
        ("いる", "いらっしゃる / おいでになる", "おる", "Có mặt / Ở"),
        ("見る", "ご覧（らん）になる", "拝見（はいけん）する", "Xem / Nhìn"),
        ("聞く / 尋ねる", "お聞（き）きになる", "伺（うかが）う / 拝聴（はいちょう）する", "Nghe / Hỏi"),
        ("言う", "おっしゃる", "申（もう）す / 申（もう）し上（あ）げる", "Nói"),
        ("知る / 思っている", "ご存知（ぞんじ）だ", "存（ぞん）じる / 存（ぞん）じ上（あ）げる", "Biết"),
        ("食べる / 飲む", "召（め）し上（あ）がる", "いただく", "Ăn / Uống"),
        ("あげる", "くださる *(người trên cho mình)*", "差（さ）し上（あ）げる", "Cho / Tặng"),
        ("もらう", "—", "いただく / 頂戴（ちょうだい）する", "Nhận"),
    ],
    "traps": [
        "⚠️ **Tuyệt đối không dùng Tôn kính ngữ cho chính mình / người công ty mình khi nói với khách ngoài:** Phải hạ xuống khiêm nhường hoặc thể lịch sự trung tính (`社長（しゃちょう）はただいま外出（がいしゅつ）しております`, còn với hành động bản thân thì dùng `私（わたし）がご案内（あんない）いたします`).",
        "⚠️ **Tránh lạm dụng Kính ngữ kép (二重敬語):** ✗ `おっしゃられる` (sai vì `おっしゃる` đã là tôn kính) -> đúng là `おっしゃる`; ✗ `ご覧になられる` -> đúng là `ご覧になる`.",
        "⚠️ **Cặp công thức chung:** Tôn kính `お + V-ます + になる` (hoặc `V-(ら)れる`); Khiêm nhường `お + V-ます + する / いたす` (với nhóm III Hán-Nhật dùng `ご + N + する/いたす`)."
    ]
}
