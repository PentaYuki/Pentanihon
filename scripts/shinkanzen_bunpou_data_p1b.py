# -*- coding: utf-8 -*-
"""
Dữ liệu Ngữ Pháp Shinkanzen Master N2 (新完全マスター文法 N2)
Phần 1: 文の文法 1 — Bài 14 đến Bài 26
"""

BUNPOU_PART1_B = {
    14: {
        "title_jp": "〜けれど",
        "title_vi": "Nhượng Bộ & Tương Phản (Tuy... Nhưng...)",
        "section": "II. 主観を含めて説明する",
        "intro": "Bài 14 trong **Shinkanzen Master Ngữ pháp N2** gom 6 cấu trúc **nhượng bộ và đối lập nghịch lý** (`〜にもかかわらず`, `〜ものの`, `〜ながら（も）`, `〜つつ（も）`, `〜といっても`, `〜からといって`). Đề thi hay gài bẫy sự khác biệt về cách chia `Na / N` và ngôi chủ ngữ!",
        "patterns": [
            {
                "name": "1. 〜にもかかわらず",
                "meaning": "Mặc dù... thế nhưng... / Bất chấp (Kết quả vế sau đi ngược lại với điều dự đoán thông thường từ vế trước).",
                "connection": "V-thông thường / Aい / Na（bỏ だ・である） / N（bỏ だ・である） + にもかかわらず",
                "examples": [
                    ("大雨（おおあめ）**にもかかわらず**、会場（かいじょう）には多（おお）くのファンが集（あつ）まった。", "Mặc dù trời mưa to, rất đông người hâm mộ vẫn tập trung tại hội trường."),
                    ("何度（なんど）も注意（ちゅうい）した**にもかかわらず**、彼（かれ）は同（おな）じミスを繰（く）り返（かえ）す。", "Dù đã nhắc nhở bao nhiêu lần nhưng cậu ta vẫn lặp lại đúng lỗi đó."),
                ],
                "note": "Thường dùng trong văn viết trang trọng, mang sắc thái bất ngờ hoặc trách nhẹ. Chú ý: sau Na và N KHÔNG thêm な hay の (nhưng có thể dùng である)."
            },
            {
                "name": "2. 〜ものの / 〜とはいうものの",
                "meaning": "Tuy nói là đã... nhưng thực tế thì... (Công nhận sự thật ở vế 1 nhưng vế 2 không suôn sẻ như kỳ vọng).",
                "connection": "V-thông thường / Aい / Na-な（である） / N-である + ものの",
                "examples": [
                    ("車（くるま）の免許（めんきょ）は取（と）った**ものの**、まだ一度（いちど）も運転（うんてん）していない。", "Tuy đã lấy bằng lái xe rồi đấy nhưng tôi vẫn chưa lái thử lần nào."),
                    ("春（はる）になった**とはいうものの**、朝晩（あさばん）はまだ肌寒（はだざむ）い日（ひ）が続（つづ）く。", "Tuy nói là đã sang xuân nhưng sáng tối trời vẫn còn se lạnh."),
                ],
                "note": "Vế trước hay chia `V-た`, vế sau hay mang nội dung chưa thỏa mãn kỳ vọng."
            },
            {
                "name": "3. 〜ながら（も）",
                "meaning": "Tuy rằng... nhưng vẫn... (Hai trạng thái mâu thuẫn tồn tại song song ở cùng một chủ thể).",
                "connection": "V-ます（bỏ ます） / V-ている / Aい / Na（bỏ だ） / N（bỏ だ） + ながら（も）",
                "examples": [
                    ("彼（かれ）は小柄（こがら）**ながらも**、力強（ちからづよ）いプレーを見（み）せる。", "Tuy dáng người nhỏ bé nhưng cậu ấy lại thể hiện lối chơi đầy mạnh mẽ."),
                    ("残念（ざんねん）**ながら**、今回（こんかい）の企画（きかく）は採用（さいよう）を見送（みおく）ることになりました。", "Tuy rất đáng tiếc, nhưng chúng tôi đành phải gác lại dự án lần này."),
                ],
                "note": "Thường đi với tính từ, danh từ hoặc động từ trạng thái (`知る`, `思う`, `持つ`), dùng cho CÙNG một chủ ngữ."
            },
            {
                "name": "4. 〜つつ（も）",
                "meaning": "Dẫu biết là / Dẫu nghĩ là... nhưng vẫn cứ... (Diễn tả sự giằng xé giữa lý trí và hành động thực tế).",
                "connection": "V-ます（bỏ ます） + つつ（も）",
                "examples": [
                    ("体（からだ）に悪（わる）いと知（し）り**つつも**、つい夜食（やしょく）を食（た）べてしまう。", "Dẫu biết là có hại cho sức khỏe nhưng tôi vẫn cứ lỡ ăn khuya."),
                    ("早（はや）く寝（ね）なければと思（おも）い**つつ**、深夜（しんや）までスマホを見（み）てしまった。", "Dẫu tự nhủ phải ngủ sớm nhưng tôi vẫn xem điện thoại đến tận nửa đêm."),
                ],
                "note": "Chỉ nối với **động từ** (thường là động từ tâm lý `知る・思う・分かる`) và hai vế cùng một chủ thể."
            },
            {
                "name": "5. 〜といっても",
                "meaning": "Tuy gọi là A đấy, nhưng thực tế mức độ/tính chất không lớn như người ta tưởng đâu.",
                "connection": "V-thông thường / Aい / Na（bỏ だ） / N + といっても",
                "examples": [
                    ("料理（りょうり）ができる**といっても**、目玉焼（めだまや）きが作（つく）れる程度（ていど）です。", "Nói là biết nấu ăn thôi chứ chỉ ở mức rán được trứng ốp la thôi ạ."),
                    ("残業（ざんぎょう）**といっても**、毎日（まいにち）30分（さんじゅっぷん）くらいのものだ。", "Tuy nói là tăng ca nhưng mỗi ngày chỉ tầm 30 phút thôi."),
                ],
                "note": "Chức năng **đính chính giảm nhẹ** kỳ vọng của người nghe."
            },
            {
                "name": "6. 〜からといって",
                "meaning": "Không phải cứ vì lý do A mà có thể kết luận/làm B được đâu.",
                "connection": "Thể thông thường + からといって + （vế sau phủ định: 〜わけではない / 〜とは限らない / 〜てはいけない）",
                "examples": [
                    ("値段（ねだん）が高（たか）い**からといって**、必（かなら）ずしも品質（ひんしつ）がいいとは限（かぎ）らない。", "Không phải cứ giá đắt thì chắc chắn chất lượng sẽ tốt."),
                    ("疲（つか）れている**からといって**、仕事（しごと）を放（ほう）り出（だ）すわけにはいかない。", "Không thể chỉ vì mệt mà bỏ ngang công việc được."),
                ],
                "note": "Vế sau LUÔN là dạng phủ định một phần hoặc ngăn cấm (`〜わけではない`, `〜とは限らない`, `〜てはいけない`)."
            },
        ],
        "comparison": [
            ("〜にもかかわらず", "Bất chấp điều kiện ngược chiều (văn viết).", "Nối trực tiếp `N / Na` không cần `な / の`."),
            ("〜ものの", "Công nhận vế 1 nhưng vế 2 không như ý.", "Dùng `Naな / Nである` trước `ものの`."),
            ("〜つつ（も）", "Giằng xé giữa nhận thức và hành động.", "Chỉ đi sau `V-ます` (hay gặp `知りつつも`, `思いつつ`)."),
            ("〜といっても", "Đính chính thực tế nhỏ hơn tên gọi.", "Vế sau hay có `ほんの〜`, `〜程度`, `〜だけ`."),
        ],
        "pitfalls": [
            "⚠️ Chú ý cách nối danh từ/tính từ Na: `雨にもかかわらず` (không の/な), `狭いながらも` (không な/だ), `合格したものの`, `健康であるものの`.",
            "⚠️ `〜からといって` bắt buộc vế sau phải có dạng phủ định (`わけではない`, `とは限らない`, `ない`)."
        ],
        "quiz": [
            ("試験（しけん）に合格（ごうかく）した（　　）、まだ会話（かいわ）には自信（じしん）がない。", ["ものの", "つつ", "からといって", "ながらも"], 1, "Tuy đã đỗ kỳ thi nhưng thực tế vẫn chưa tự tin -> V-た + ものの."),
            ("悪天候（あくてんこう）（　　）、多（おお）くのボランティアが作業（さぎょう）に参加（さんか）した。", ["にもかかわらず", "ものの", "からといって", "といっても"], 1, "Bất chấp thời tiết xấu (danh từ trực tiếp) -> にもかかわらず."),
            ("タバコは健康（けんこう）に良（よ）くないと分（わ）かり（　　）、なかなかやめられない。", ["つつも", "ものの", "にもかかわらず", "といっても"], 1, "Giằng xé nội tâm sau V-ます -> つつも."),
            ("日本（にほん）に留学（りゅうがく）していた（　　）、期間（きかん）はわずか1か月（いっかげつ）だ。", ["といっても", "つつも", "からといって", "にもかかわらず"], 1, "Đính chính mức độ thực tế nhỏ hơn tưởng tượng -> といっても."),
            ("お金（かね）がある（　　）、好（す）き勝手（かって）にしていいというわけではない。", ["からといって", "ものの", "ながらも", "つつ"], 1, "Đi với というわけではない ở vế sau -> からといって."),
        ]
    },
    15: {
        "title_jp": "もしそうなら・たとえそうでも",
        "title_vi": "Điều Kiện Giả Định & Giả Sử Nhượng Bộ",
        "section": "II. 主観を含めて説明する",
        "intro": "Bài 15 trong **Shinkanzen Master Ngữ pháp N2** tập hợp các mẫu **giả định điều kiện đặc biệt, điều kiện tiên quyết và nhượng bộ giả sử** (`〜としたら・〜とすれば`, `〜ものなら`, `〜（よ）うものなら`, `〜ないことには`, `〜を抜きにしては`, `〜としても`).",
        "patterns": [
            {
                "name": "1. 〜としたら / 〜とすれば / 〜とすると / 〜となったら / 〜となれば / 〜となると",
                "meaning": "Nếu giả sử rằng... / Một khi đặt trong tình huống là... thì...",
                "connection": "Thể thông thường（Na-だ/bỏ だ, N-だ/bỏ だ）+ としたら / とすれば / とすると / となったら",
                "examples": [
                    ("もし1億円（いちおくえん）当（あ）たった**としたら**、まず両親（りょうしん）に家（いえ）を買（か）ってあげたい。", "Nếu giả sử trúng 100 triệu yên, trước hết tôi muốn mua tặng bố mẹ một căn nhà."),
                    ("来週（らいしゅう）から出張（しゅっちょう）**となれば**、今日中（きょうじゅう）に準備（じゅんび）を済（す）ませなければならない。", "Nếu từ tuần sau phải đi công tác thật thì ngay trong hôm nay tôi phải chuẩn bị xong."),
                ],
                "note": "`としたら / とすれば` mang tính giả thuyết thuần túy; `となったら / となれば` nhấn mạnh chuyển sang tình huống thực tế sắp/đã xảy ra."
            },
            {
                "name": "2. 〜ものなら",
                "meaning": "Giá mà có thể... thì... (Ước muốn làm một việc thực tế rất khó hoặc bất khả thi).",
                "connection": "V-khả năng（thường dùng `〜られる`, `できる`）+ ものなら",
                "examples": [
                    ("タイムマシンで過去（かこ）に戻（もど）れる**ものなら**、もう一度（いちど）やり直（なお）したい。", "Nếu mà có thể quay ngược thời gian về quá khứ, tôi muốn làm lại từ đầu."),
                    ("できる**ものなら**、今（いま）すぐ仕事（しごと）を休（やす）んで旅（たび）に出（で）たい。", "Nếu được thì ngay lúc này tôi muốn nghỉ làm để đi du lịch một chuyến."),
                ],
                "note": "Vế trước đi với **động từ khả năng**, vế sau thường là nguyện vọng (`〜たい`)."
            },
            {
                "name": "3. 〜（よ）うものなら",
                "meaning": "Lỡ mà / Dại dột mà làm A thì chắc chắn chuốc lấy hậu quả nghiêm trọng B.",
                "connection": "V-よう（thể ý chí）+ ものなら",
                "examples": [
                    ("こんな大雨（おおあめ）の日（ひ）に山（やま）に登（のぼ）ろう**ものなら**、遭難（そうなん）する危険（きけん）がある。", "Nếu liều lĩnh leo núi vào ngày mưa bão thế này thì có nguy cơ gặp nạn đấy."),
                    ("社長（しゃちょう）の意見（いけん）に反対（はんたい）しよう**ものなら**、すぐに左遷（させん）されかねない。", "Nếu cả gan phản đối ý kiến giám đốc thì rất có thể bị giáng chức ngay lập tức."),
                ],
                "note": "Phân biệt cực kỹ với mẫu 2! Cùng là `ものなら` nhưng đi sau `V-よう` thì vế sau LUÔN là **hậu quả tồi tệ**."
            },
            {
                "name": "4. 〜ないことには",
                "meaning": "Nếu không làm A thì không thể nào làm/biết được B (Điều kiện bắt buộc).",
                "connection": "V-ない / Aくない / Naでない / Nでない + ことには + (vế sau phủ định)",
                "examples": [
                    ("実際（じっさい）にやってみ**ないことには**、できるかどうか分（わ）からない。", "Nếu không thử làm thực tế thì không thể biết có làm được hay không."),
                    ("資金（しきん）が集（あつ）まら**ないことには**、新（あたら）しい事業（じぎょう）は始（はじ）められない。", "Nếu không gom đủ vốn thì không thể khởi động dự án mới được."),
                ],
                "note": "Vế sau luôn mang nghĩa phủ định hoặc không thể (`分からない`, `始まらない`, `無理だ`)."
            },
            {
                "name": "5. 〜を抜（ぬ）きにしては",
                "meaning": "Nếu gạt bỏ / thiếu vắng A đi thì không thể thực hiện/bàn luận đến B (A là nhân tố không thể thiếu).",
                "connection": "N + を抜（ぬ）きにしては + (vế sau phủ định)",
                "examples": [
                    ("田中（たなか）さんの協力（きょうりょく）**を抜（ぬ）きにしては**、このプロジェクトの成功（せいこう）はあり得（え）ない。", "Nếu thiếu đi sự hợp tác của anh Tanaka thì dự án này không thể nào thành công được."),
                    ("環境（かんきょう）への配慮（はいりょ）**を抜（ぬ）きにしては**、現代（げんだい）の経済（けいざい）発展（はってん）は語（かた）れない。", "Nếu bỏ qua yếu tố môi trường thì không thể bàn tới phát triển kinh tế hiện đại."),
                ],
                "note": "Cũng có dạng `N を抜きにして` = gạt bỏ N sang một bên (`冗談は抜きにして`)."
            },
            {
                "name": "6. 〜としても / 〜にしても / 〜にしろ / 〜にせよ",
                "meaning": "Cho dù giả sử là A đi chăng nữa thì vẫn B (Nhượng bộ trước điều giả định).",
                "connection": "Thể thông thường + としても / にしても / にしろ / にせよ",
                "examples": [
                    ("たとえ失敗（しっぱい）した**としても**、チャレンジした経験（けいけん）は無駄（むだ）にならない。", "Cho dù có thất bại đi chăng nữa thì kinh nghiệm dám thử thách cũng không uổng phí."),
                    ("冗談（じょうだん）だった**にせよ**、相手（あいて）を傷（きず）つけるような言（い）い方（かた）はよくない。", "Dù chỉ là nói đùa đi nữa thì cách nói làm tổn thương người khác cũng không hay chút nào."),
                ],
                "note": "Hay kết hợp với phó từ `たとえ〜` ở đầu câu."
            },
        ],
        "comparison": [
            ("V- khả năng + ものなら", "Giá mà có thể (ước muốn khó thành).", "Vế sau là mong muốn (`〜たい`)."),
            ("V- ý chí (〜よう) + ものなら", "Lỡ mà làm thế thì chết chắc.", "Vế sau là hậu quả nghiêm trọng."),
            ("〜ないことには", "Nếu không làm A thì không thể B.", "Vế sau luôn mang ý phủ định/bất khả."),
            ("〜を抜きにしては", "Nếu thiếu N thì không thể B.", "Chỉ đi với Danh từ."),
        ],
        "pitfalls": [
            "⚠️ Bẫy sống còn giữa 2 cách chia `ものなら`: `戻れるものなら` (ước muốn) vs `遅刻しようものなら` (hậu quả xấu)!",
            "⚠️ Sau `〜ないことには` và `〜を抜きにしては`, vế sau hầu như bắt buộc phải có ý nghĩa phủ định."
        ],
        "quiz": [
                    ("もしタイムマシンを作（つく）れる（　　）、未来（みらい）の日本（にほん）を見（み）てみたい。", ["ものなら", "ないことには", "としても", "を抜きにしては"], 1, "Sau động từ khả năng 作れる bày tỏ ước muốn -> ものなら."),
                    ("この秘密（ひみつ）を他人（たにん）に漏（も）らそう（　　）、信頼（しんらい）を一気（いっき）に失（うしな）うだろう。", ["ものなら", "としたら", "にしても", "ことには"], 1, "Sau thể ý chí 漏らそう dẫn tới hậu quả xấu -> ものなら."),
                    ("まず本人（ほんにん）の意見（いけん）を聞（き）いてみ（　　）、何（なに）も判断（はんだん）できない。", ["ないことには", "ものなら", "としても", "を抜きにしては"], 1, "Nếu không hỏi thử trước thì không thể phán đoán -> ないことには."),
                    ("チーム全員（ぜんいん）の努力（どりょく）（　　）、優勝（ゆうしょう）は実現（じつげん）しなかったはずだ。", ["を抜（ぬ）きにしては", "ないことには", "ものなら", "とすれば"], 1, "Thiếu đi yếu tố N thì không thể thành công -> を抜きにしては."),
                    ("たとえ明日（あした）が雨（あめ）だった（　　）、私（わたし）は予定（よてい）通（どお）り出発（しゅっぱつ）する。", ["としても", "ないことには", "ようものなら", "を抜きにしては"], 1, "Cho dù giả sử ngày mai mưa đi nữa -> としても."),
        ]
    },
    16: {
        "title_jp": "〜だから（理由）— 1",
        "title_vi": "Nguyên Nhân & Lý Do — Phần 1",
        "section": "II. 主観を含めて説明する",
        "intro": "Bài 16 trong **Shinkanzen Master Ngữ pháp N2** phân biệt 5 cách diễn đạt **nguyên nhân, nguồn cơn và lý do** trong nhiều ngữ cảnh từ thân mật đến thông báo công cộng (`〜によって`, `〜ものだから`, `〜おかげだ・〜せいだ`, `〜あまり`, `〜につき`).",
        "patterns": [
            {
                "name": "1. 〜によって / 〜による",
                "meaning": "Bởi / Do nguyên nhân... (Nguyên nhân khách quan mang tính sự kiện, thiên tai, nghiên cứu... — văn viết).",
                "connection": "N + によって / により / による + N",
                "examples": [
                    ("地震（じしん）**によって**、新幹線の運転（うんてん）が一時（いちじ）停止（ていし）した。", "Do trận động đất, tàu Shinkansen đã tạm ngừng vận hành."),
                    ("不注意（ふちゅうい）**による**事故（じこ）が毎年（まいとし）後（あと）を絶（た）たない。", "Tai nạn do bất cẩn năm nào cũng không dứt."),
                ],
                "note": "Rất trang trọng, dùng nêu nguyên nhân trong bản tin, báo cáo; không dùng cho lý do mang tính cảm xúc cá nhân."
            },
            {
                "name": "2. 〜ものだから / 〜もので / 〜もの",
                "meaning": "Tại vì... mà... (Nêu lý do cá nhân mang tính biện minh, giải thích cho sự việc đã xảy ra).",
                "connection": "V-thông thường / Aい / Na-な / N-な（だった） + ものだから（もので / もんだから）",
                "examples": [
                    ("電車（でんしゃ）が遅（おく）れた**ものだから**、会議（かいぎ）に遅刻（ちこく）してしまいました。", "Tại vì tàu điện đến trễ nên em đã lỡ trễ giờ họp mất rồi ạ."),
                    ("あまりにおいしかった**もので**、つい食（た）べすぎてしまった。", "Tại vì ngon quá trời nên lỡ ăn quá đà mất rồi."),
                ],
                "note": "Thiên về văn nói thanh minh/biện hộ (`もので` nhẹ nhàng lịch sự hơn; `もの` đặt ở cuối câu khi giải thích với người thân)."
            },
            {
                "name": "3. 〜おかげだ / 〜せいだ",
                "meaning": "`〜おかげだ`: Nhờ có... mà được kết quả TỐT; `〜せいだ`: Tại vì... mà ra kết quả XẤU (đổ lỗi).",
                "connection": "V-thông thường / Aい / Na-な / Nの + おかげで（おかげだ） / せいで（せいだ）",
                "examples": [
                    ("先生（せんせい）のご指導（しどう）の**おかげで**、N2に合格（ごうかく）することができました。", "Nhờ có sự chỉ dạy tận tình của thầy cô mà em đã đỗ được N2."),
                    ("昨夜（さくや）遅（おそ）くまでゲームをした**せいで**、今日（きょう）は頭（あたま）が痛（いた）い。", "Tại hôm qua chơi game tới khuya nên hôm nay đầu đau như búa bổ."),
                ],
                "note": "Đôi khi `おかげで` dùng kiểu mỉa mai hài hước nhưng trong thi chuẩn N2 luôn phân định rõ: Tốt -> `おかげ`, Xấu -> `せい`."
            },
            {
                "name": "4. 〜あまり / あまりの〜に",
                "meaning": "Vì quá mức... đến độ dẫn đến một hành động/trạng thái mất kiểm soát hoặc bất thường.",
                "connection": "V-る・V-た / Aい（thường danh từ hóa 〜さ） / Na-な / Nの + あまり ｜ あまりの + N + に",
                "examples": [
                    ("合格（ごうかく）が嬉（うれ）しい**あまり**、思（おも）わず涙（なみだ）があふれ出（で）た。", "Vì quá đỗi vui mừng khi đỗ nên nước mắt cứ thế bất giác tuôn trào."),
                    ("**あまりの**驚（おどろ）き**に**、しばらく言葉（ことば）が出（で）なかった。", "Vì quá kinh ngạc nên một lúc lâu tôi không thốt nên lời."),
                ],
                "note": "Diễn tả cảm xúc hoặc trạng thái vượt ngưỡng bình thường dẫn tới phản ứng ngoài ý muốn (`緊張のあまり`, `忙しさのあまり`)."
            },
            {
                "name": "5. 〜につき",
                "meaning": "Do / Vì lý do... (Chỉ dùng trên biển báo, thông báo công cộng, hóa đơn).",
                "connection": "N + につき",
                "examples": [
                    ("ただいま店内（てんない）改装（かいそう）中（ちゅう）**につき**、臨時（りんじ）休業（きゅうぎょう）いたします。", "Hiện tại do đang sửa chữa cửa hàng nên chúng tôi xin tạm nghỉ."),
                    ("工事（こうじ）**につき**、関係者（かんけいしゃ）以外（いがい）の立（た）ち入（い）りを禁止（きんし）いたします。", "Do đang thi công nên cấm người không có phận sự đi vào."),
                ],
                "note": "Chỉ đứng trực tiếp sau **Danh từ** trong thông báo chính thức (`定休日につき`, `悪天候につき`), không dùng trong hội thoại thường."
            },
        ],
        "comparison": [
            ("〜によって", "Nguyên nhân khách quan trong tin tức/báo cáo (`台風によって`).", "Đứng sau Danh từ."),
            ("〜ものだから", "Lý do cá nhân biện minh khi nói chuyện.", "Không dùng trong thông báo chính thức."),
            ("〜あまり", "Vì quá mức cảm xúc/trạng thái dẫn tới phản ứng bất thường.", "Không dùng cho nguyên nhân vật lý thông thường."),
            ("〜につき", "Lý do trên biển báo/thông báo (`工事中につき`).", "Chỉ đi sau Danh từ ngắn gọn."),
        ],
        "pitfalls": [
            "⚠️ Chú ý kết hợp từ trước `〜あまり`: dùng `Nのあまり` (`心配のあまり`), `V-る/たあまり` (`考えすぎたあまり`), nhưng với tính từ đuôi い thường danh từ hóa thành `〜さのあまり` (`嬉しさのあまり`, `悔しさのあまり`) hoặc `あまりの〜さに`.",
            "⚠️ `〜につき` KHÔNG BAO GIỜ nối với động từ hay tính từ (chỉ `N + につき`)."
        ],
        "quiz": [
            ("本日（ほんじつ）は社員（しゃいん）研修（けんしゅう）（　　）、午後（ごご）3時（さんじ）にて閉店（へいてん）いたします。", ["につき", "ものだから", "あまり", "せいで"], 1, "Thông báo cửa hàng sau danh từ ngắn -> につき."),
            ("緊張（きんちょう）の（　　）、スピーチで言（い）うべきことをすっかり忘（わす）れてしまった。", ["あまり", "せいで", "につき", "によって"], 1, "Quá căng thẳng đến độ quên sạch lời: 緊張のあまり."),
            ("道路（どうろ）が渋滞（じゅうたい）していた（　　）、約束（やくそく）の時間（じかん）に遅（おく）れてすみません。", ["ものだから", "につき", "あまり", "によって"], 1, "Xin lỗi và biện minh lý do cá nhân trong giao tiếp -> ものだから."),
            ("悪天候（あくてんこう）（　　）フェリーの欠航（けっこう）が相次（あいつ）いだ。", ["による", "ものだから", "おかげで", "につき"], 1, "Bổ nghĩa danh từ phía sau chỉ nguyên nhân khách quan -> による."),
            ("友人（ゆうじん）たちが温（あたた）かく励（はげ）ましてくれた（　　）、立（た）ち直（なお）ることができた。", ["おかげで", "せいで", "つき", "あまり"], 1, "Nhờ bạn bè động viên nên vực dậy được (kết quả tốt) -> おかげで."),
        ]
    },
    17: {
        "title_jp": "〜だから（理由）— 2",
        "title_vi": "Nguyên Nhân, Căn Cứ & Trách Nhiệm — Phần 2",
        "section": "II. 主観を含めて説明する",
        "intro": "Bài 17 trong **Shinkanzen Master Ngữ pháp N2** tiếp nối nhóm nguyên nhân bằng 5 mẫu mang sắc thái **suy luận từ tính cách, lý do dẫn tới quyết định, hệ quả tương xứng hoặc trách nhiệm một khi đã...** (`〜ことだし`, `〜のことだから`, `〜だけに`, `〜ばかりに`, `〜からには・〜以上は・〜上は`).",
        "patterns": [
            {
                "name": "1. 〜ことだし",
                "meaning": "Cũng vì (tình huống hiện tại như vậy, cộng thêm mấy lý do khác nữa) nên thôi thì làm B đi...",
                "connection": "V-thông thường / Aい / Na-な（である） / N-な（の） + ことだし",
                "examples": [
                    ("雨（あめ）もやんだ**ことだし**、そろそろ買（か）い物（もの）に出（で）かけようか。", "Mưa cũng tạnh rồi đấy, hay là mình ra ngoài đi mua sắm thôi nhỉ."),
                    ("せっかく京都（きょうと）まで来（き）た**ことだし**、有名（ゆうめい）なお寺（てら）を巡（めぐ）ってみよう。", "Nhân tiện cất công tới tận Kyoto rồi, thử đi thăm mấy ngôi chùa nổi tiếng xem sao."),
                ],
                "note": "Thường dùng để rủ rê, đề xuất hoặc đưa ra quyết định nhẹ nhàng dựa trên một tình huống thuận lợi/rõ ràng."
            },
            {
                "name": "2. 〜のことだから",
                "meaning": "Vì là tính cách/đặc thù vốn có của người/vật A mà tôi biết rõ nên chắc chắn sẽ...",
                "connection": "N（chỉ người, tổ chức quen biết）+ のことだから",
                "examples": [
                    ("まじめな佐藤（さとう）さん**のことだから**、きっと時間（じかん）通（どお）りに来（く）るに違（ちが）いない。", "Vì là tính cách nghiêm túc của anh Sato nên chắc chắn anh ấy sẽ đến đúng giờ thôi."),
                    ("おしゃべりな彼（かれ）**のことだから**、もうみんなに話（はな）してしまったかもしれない。", "Vì cái tính hay buôn chuyện của cậu ta nên có khi đã kể cho cả làng biết rồi cũng nên."),
                ],
                "note": "Vế sau LUÔN là suy đoán của người nói (`きっと〜だろう`, `〜に違いない`, `〜はずだ`). Không dùng cho người lạ hoặc sự thật đã khẳng định 100% không cần đoán."
            },
            {
                "name": "3. 〜だけに",
                "meaning": "Chính vì A nên càng... hơn nữa (Kết quả B tương xứng ở mức độ cao — có thể tốt hoặc xấu).",
                "connection": "V-thông thường / Aい / Na（な・である） / N（bỏ だ・である） + だけに",
                "examples": [
                    ("大（おお）きな期待（きたい）をしていた**だけに**、落（お）ちた時（とき）のショックは大きかった。", "Chính vì đã kỳ vọng lớn lao đến thế nên cú sốc khi trượt lại càng lớn."),
                    ("彼（かれ）はプロ**だけに**、仕事（しごと）のスピードも質（しつ）も並外（なみはず）れている。", "Chính vì anh ấy là dân chuyên nghiệp nên tốc độ lẫn chất lượng công việc đều vượt trội."),
                ],
                "note": "Vế sau thể hiện mức độ mạnh mẽ hơn bình thường (`なおさら`, `いっそう`, `〜大きい`) tương xứng với điều kiện vế trước."
            },
            {
                "name": "4. 〜ばかりに",
                "meaning": "Chỉ vì một lý do nhỏ/lỗi lầm A mà dẫn đến kết quả tồi tệ B (mang đầy hối tiếc, ân hận).",
                "connection": "V-thông thường / Aい / Na-な / N-な（である） + ばかりに",
                "examples": [
                    ("たった一言（ひとこと）余計（よけい）なことを言（い）った**ばかりに**、親友（しんゆう）を傷（きず）つけてしまった。", "Chỉ vì lỡ thốt ra một câu thừa thãi mà tôi đã làm tổn thương người bạn thân nhất."),
                    ("免許（めんきょ）を持（も）っていない**ばかりに**、希望（きぼう）の会社（かいしゃ）に応募（おうぼ）できなかった。", "Chỉ tại không có bằng lái mà tôi đành ngậm ngùi không nộp đơn được vào công ty mơ ước."),
                ],
                "note": "Vế sau **100% là kết quả tiêu cực / bất mãn / hối hận**! Không bao giờ dùng cho kết quả vui."
            },
            {
                "name": "5. 〜からには / 〜以上（いじょう）（は） / 〜上（うえ）は",
                "meaning": "Một khi đã... thì đương nhiên phải / nhất định sẽ... (Nhấn mạnh trách nhiệm, nghĩa vụ hoặc quyết tâm tất yếu).",
                "connection": "V-thông thường（`N + である`）+ からには / 以上（は） / 上（うえ）は",
                "examples": [
                    ("自分（じぶん）で引（ひ）き受（う）けた**からには**、最後（さいご）まで責任（せきにん）を持（も）ってやり遂（と）げるべきだ。", "Một khi đã tự mình nhận lời thì phải chịu trách nhiệm làm cho đến cùng."),
                    ("日本（にほん）へ留学（りゅうがく）する**以上（いじょう）は**、必（かなら）ず目標（もくひょう）を達成（たっせい）したい。", "Một khi đã sang Nhật du học thì tôi nhất định muốn hoàn thành mục tiêu."),
                ],
                "note": "Vế sau luôn là biểu hiện ý chí, nghĩa vụ, lời khuyên hoặc phán đoán đương nhiên (`〜べきだ`, `〜なければならない`, `〜つもりだ`)."
            },
        ],
        "comparison": [
            ("〜だけに", "Chính vì A nên càng B (tốt hoặc xấu đều được).", "Vế sau tương xứng tăng cường độ."),
            ("〜ばかりに", "Chỉ tại A mà chuốc lấy hậu quả xấu B.", "100% kết quả tiêu cực + hối tiếc."),
            ("〜のことだから", "Suy đoán dựa trên tính cách quen biết của N.", "Vế sau luôn có phỏng đoán (`だろう`, `に違いない`)."),
            ("〜からには / 〜以上は", "Một khi đã làm A thì buộc phải/quyết tâm làm B.", "Vế sau chứa ý chí, nghĩa vụ hoặc mệnh lệnh."),
        ],
        "pitfalls": [
            "⚠️ Không nhầm `〜だけに` (kết quả 2 chiều) với `〜ばかりに` (chỉ kết quả xấu, tiếc nuối).",
            "⚠️ Với `〜上（うえ）は`, chú ý chữ `上` ở đây đọc là **うえは** (với nghĩa \"một khi đã...\"), khác với `〜上（じょう）` (trên phương diện `歴史上`)."
        ],
        "quiz": [
            ("慌（あわ）てて家（いえ）を出（で）た（　　）、大切（たいせつ）な財布（さいふ）を忘（わす）れてしまった。", ["ばかりに", "だけに", "ことだし", "からには"], 1, "Chỉ vì vội mà dẫn tới kết quả xấu hối tiếc -> ばかりに."),
            ("約束（やくそく）した（　　）、どんなに忙（いそが）しくても守（まも）らなければならない。", ["以上（いじょう）は", "ばかりに", "ことだし", "のことだから"], 1, "Một khi đã hứa thì bắt buộc phải giữ lời -> 以上は."),
            ("一生懸命（いっしょうけんめい）練習（れんしゅう）した（　　）、負（ま）けた悔（くや）しさはひとしおだった。", ["だけに", "ことだし", "からには", "ばかりに"], 1, "Chính vì luyện tập hết mình nên nỗi tiếc nuối càng sâu -> だけに."),
            ("準備（じゅんび）も整（ととの）った（　　）、さっそくイベントを始めましょう。", ["ことだし", "ばかりに", "のことだから", "だけに"], 1, "Chuẩn bị cũng xong xuôi rồi, thôi mình bắt đầu ngay nhé -> ことだし."),
            ("時間（じかん）に厳（きび）しい鈴木（すずき）部長（ぶちょう）（　　）、もう会議室（かいぎしつ）に着（つ）いているはずだ。", ["のことだから", "ばかりに", "ことだし", "上（うえ）は"], 1, "Suy đoán dựa trên tính cách quen biết của sếp Suzuki -> のことだから."),
        ]
    },
    18: {
        "title_jp": "〜できない・困難だ・〜できる",
        "title_vi": "Không Thể, Khó Khăn & Có Thể",
        "section": "III. 評価・判断する",
        "intro": "Bài 18 trong **Shinkanzen Master Ngữ pháp N2** tổng hợp 6 cấu trúc diễn tả **sự bất khả kháng, khó khăn về mặt tâm lý/đạo đức/phương pháp, hoặc khả năng xảy ra về mặt lý thuyết** (`〜がたい`, `〜わけにはいかない`, `〜かねる`, `〜ようがない`, `〜どころではない`, `〜得る / 〜得ない`).",
        "patterns": [
            {
                "name": "1. 〜がたい",
                "meaning": "Khó mà... được (Về mặt tâm lý, cảm xúc hoặc tình trạng thấy khó thực hiện, dù xét về năng lực vật lý không phải không làm được).",
                "connection": "V-ます（bỏ ます）+ がたい",
                "examples": [
                    ("長年（ながねん）信（しん）じていた友（とも）に裏切（うらぎ）られたことは、許（ゆる）し**がたい**。", "Việc bị người bạn tin tưởng nhiều năm phản bội thật khó mà tha thứ nổi."),
                    ("こんな不思議（ふしぎ）な現象（げんしょう）は、にわかには信（しん）じ**がたい**。", "Hiện tượng kỳ lạ thế này thật khó mà tin ngay được."),
                ],
                "note": "Thường đi với động từ nhận thức, cảm xúc hoặc biểu đạt (`信じる・理解する・想像する・許す・言う・認める`). Không dùng cho hành động thể chất thông thường (✗ `食べがたい`)."
            },
            {
                "name": "2. 〜わけにはいかない / 〜わけにもいかない",
                "meaning": "1) `V-る + わけにはいかない`: Không thể làm thế được (vì rào cản đạo đức, quy tắc, trách nhiệm, thể diện); 2) `V-ない + わけにはいかない`: Không thể không làm (= buộc phải làm).",
                "connection": "V-る / V-ない + わけにはいかない",
                "examples": [
                    ("大切（たいせつ）な会議（かいぎ）の発表（はっぴょう）担当（たんとう）なので、風邪（かぜ）でも休（やす）む**わけにはいかない**。", "Vì là người phụ trách thuyết trình cuộc họp quan trọng nên dù cảm tôi cũng không thể nghỉ được."),
                    ("上司（じょうし）に頼（たの）まれた仕事（しごと）だから、引（ひ）き受（う）けない**わけにはいかない**。", "Vì là việc sếp giao nên tôi không thể không nhận."),
                ],
                "note": "Cẩn thận bẫy phủ định kép `V-ないわけにはいかない` = BẮT BUỘC phải làm!"
            },
            {
                "name": "3. 〜かねる",
                "meaning": "Khó lòng mà... / Xin phép không thể... (Cách từ chối cực kỳ lịch sự trong công sở/dịch vụ, hoặc e ngại làm sẽ bất tiện).",
                "connection": "V-ます（bỏ ます）+ かねる",
                "examples": [
                    ("その件（けん）につきましては、私（わたし）の一存（いちぞん）ではお答（こた）えし**かねます**。", "Về vấn đề đó, chỉ riêng cá nhân tôi thì xin phép khó lòng trả lời được ạ."),
                    ("この規則（きそく）の改正（かいせい）には、どうしても賛成（さんせい）し**かねる**。", "Tôi thực sự khó lòng mà tán thành việc sửa đổi quy tắc này."),
                ],
                "note": "PHÂN BIỆT SỐNG CÒN: `〜かねる` (khó lòng làm — Bài 18) khác hoàn toàn `〜かねない` (rất có thể dẫn tới điều xấu — Bài 22)!"
            },
            {
                "name": "4. 〜ようがない / 〜ようもない",
                "meaning": "Chẳng có cách nào để làm... (Bó tay vì thiếu phương tiện/công cụ/đầu mối).",
                "connection": "V-ます（bỏ ます）+ ようがない / ようもない",
                "examples": [
                    ("連絡先（れんらくさき）が全（まった）く分（わ）からないので、連絡（れんらく）のし**ようがない**。", "Chẳng hề biết thông tin liên lạc nên không có cách nào để liên hệ được."),
                    ("ここまで壊（こわ）れてしまっては、もう直（なお）し**ようがない**。", "Đã hỏng đến mức này rồi thì chẳng còn cách nào sửa chữa nữa."),
                ],
                "note": "Với động từ nhóm III `する` -> `しようがない` hoặc `のしようがない`."
            },
            {
                "name": "5. 〜どころではない",
                "meaning": "Không còn tâm trí / điều kiện / thời gian đâu mà nghĩ tới việc đó.",
                "connection": "V-る / V-ている / N + どころではない",
                "examples": [
                    ("熱（ねつ）が39度（ど）もあって、食事（しょくじ）**どころではない**。", "Sốt tới 39 độ rồi, chẳng thiết tha ăn uống gì nữa đâu."),
                ],
                "note": "Đã gặp ở Bài 12 ở góc độ phủ định mạnh; trong Bài 18 nhìn ở góc độ trạng thái bất khả thi vì tình huống gấp gáp."
            },
            {
                "name": "6. 〜得（う）る / 〜得（え）ない",
                "meaning": "Có khả năng xảy ra / Hoàn toàn có thể (`うる / える`); Không thể nào có khả năng đó (`えない`).",
                "connection": "V-ます（bỏ ます）+ 得（う）る / 得（え）る / 得（え）ない",
                "examples": [
                    ("人間（にんげん）である以上（いじょう）、誰（だれ）にでもミスは起（お）こり**得（う）る**。", "Đã là con người thì sai sót có thể xảy ra với bất kỳ ai."),
                    ("そんな馬鹿（ばか）げたことは、現実（げんじつ）にはあり**得（え）ない**。", "Chuyện ngớ ngẩn như thế ngoài đời thực tuyệt đối không thể có."),
                ],
                "note": "Chú ý cách đọc: thể khẳng định đọc là **うる** hoặc **える** (khi đứng trước danh từ `あり得る話` chỉ đọc là `うる` hoặc `える`, khi chia quá khứ `あり得た` đọc `えた`); thể phủ định CHỈ đọc là **えない**!"
            },
        ],
        "comparison": [
            ("〜がたい", "Khó về mặt tâm lý/tình cảm (`許しがたい`, `信じがたい`).", "Không dùng cho khả năng thể chất."),
            ("〜わけにはいかない", "Không thể về mặt đạo đức/trách nhiệm.", "`V-ないわけにはいかない` = buộc phải làm."),
            ("〜かねる", "Khó lòng (từ chối lịch sự trong công việc).", "KHÔNG nhầm với `〜かねない` (có nguy cơ xấu — Bài 22)."),
            ("〜ようがない", "Bó tay không có phương tiện/cách thức.", "Nối sau `V-ます` (hay thêm `の`: `しようがない`)."),
        ],
        "pitfalls": [
            "⚠️ Bẫy đọc chữ `得る`: `あり得ない` luôn đọc là `ありえない` (KHÔNG đọc `ありうない`!).",
            "⚠️ `〜かねる` (từ chối lịch sự: `お受けしかねます`) trái ngược hoàn toàn với `〜かねない` (có nguy cơ: `事故を起こしかねない`)."
        ],
        "quiz": [
            ("電話番号（でんわばんごう）を消（け）してしまったので、彼女（かのじょ）に連絡（れんらく）のし（　　）。", ["ようがない", "がたい", "かねる", "得（え）ない"], 1, "Không có cách nào để liên lạc -> V-ます + ようがない."),
            ("誠（まこと）に申（もう）し訳（わけ）ございませんが、そのご要望（ようぼう）にはお応（こた）えし（　　）。", ["かねます", "かねません", "がたいです", "ようがありません"], 1, "Từ chối khách hàng lịch sự -> V-ます + かねます."),
            ("どれほど科学（かがく）が進歩（しんぽ）しても、災害（さいがい）のリスクがゼロになることはあり（　　）。", ["得（え）ない", "がたい", "かねない", "ようがない"], 1, "Về mặt lý thuyết hoàn toàn không thể có -> あり得ない."),
            ("友人（ゆうじん）と約束（やくそく）した以上（いじょう）、今（いま）さら行（い）かない（　　）。", ["わけにはいかない", "がたい", "ようがない", "得（え）ない"], 1, "Không thể không đi (trách nhiệm với lời hứa) -> V-ない + わけにはいかない."),
            ("彼（かれ）がそんな冷酷（れいこく）な発言（はつげん）をするとは、にわかには信（しん）じ（　　）。", ["がたい", "かねない", "ようがない", "わけにはいかない"], 1, "Khó mà tin được về mặt cảm xúc -> 信じがたい."),
        ]
    },
    19: {
        "title_jp": "〜を見て評価すると・〜の立場で評価すると",
        "title_vi": "Đánh Giá & Góc Nhìn Lập Trường",
        "section": "III. 評価・判断する",
        "intro": "Bài 19 trong **Shinkanzen Master Ngữ pháp N2** gom 6 cấu trúc chuyên dùng để **so sánh đánh giá so với tiêu chuẩn/kỳ vọng** và **đặt vào lập trường/góc nhìn của một đối tượng** (`〜わりに（は）`, `〜にしては`, `〜だけ（のことは）ある`, `〜として`, `〜にとって`, `〜にしたら・〜にすれば`).",
        "patterns": [
            {
                "name": "1. 〜わりに（は）",
                "meaning": "So với mức độ/giá cả/công sức... thì kết quả lại vượt hoặc kém hơn hẳn mong đợi (khá bất ngờ).",
                "connection": "V-thông thường / Aい / Na-な / N-の + わりに（は）",
                "examples": [
                    ("このレストランは値段（ねだん）の**わりに**、味（あじ）がとてもおいしい。", "Nhà hàng này so với mức giá thì hương vị ngon ngoài mong đợi."),
                    ("あまり勉強（べんきょう）していない**わりには**、テストの点（てん）が良（よ）かった。", "So với mức độ chẳng học hành mấy thì điểm kiểm tra lại cao bất ngờ."),
                ],
                "note": "Thường dùng với danh từ chỉ **mức độ, thang đo** (`値段・年・広さ・努力`) hoặc động/tính từ."
            },
            {
                "name": "2. 〜にしては",
                "meaning": "Xét theo tiêu chuẩn của đối tượng/con số cụ thể A mà nói thì... (thật bất ngờ khác thường).",
                "connection": "V-thông thường / N + にしては",
                "examples": [
                    ("日本（にほん）へ来（き）てまだ半年（はんとし）**にしては**、日本語（にほんご）がとても上手（じょうず）だ。", "Mới sang Nhật có nửa năm mà tiếng Nhật giỏi thật đấy."),
                    ("初心者（しょしんしゃ）**にしては**、なかなか堂々（どうどう）とした演奏（えんそう）だった。", "Xét ở tư cách người mới bắt đầu thì màn trình diễn khá đĩnh đạc."),
                ],
                "note": "KHÔNG đi sau tính từ; thường đứng sau **danh từ cụ thể hoặc con số/danh xưng** (`子ども`, `プロ`, `70歳`, `初心者`)."
            },
            {
                "name": "3. 〜だけ（のことは）ある",
                "meaning": "Quả không hổ danh là... / Đúng là xứng đáng với... (Đánh giá tích cực, hợp lý với danh tiếng/nỗ lực).",
                "connection": "V-thông thường / Aい / Na-な / N + だけある / だけのことはある",
                "examples": [
                    ("五（いつ）つ星（ぼし）ホテル**だけのことはあって**、サービスが実（じつ）にきめ細（こま）やかだ。", "Quả đúng danh khách sạn 5 sao, dịch vụ thực sự chu đáo từng li từng tí."),
                    ("毎日（まいにち）欠（か）かさず練習（れんしゅう）した**だけあって**、見事（みごと）に優勝（ゆうしょう）した。", "Đúng là bõ công luyện tập không nghỉ ngày nào, cậu ấy đã vô địch ngoạn mục."),
                ],
                "note": "Ngược với `わりに / にしては` (bất ngờ trái chuẩn); `だけある` là **đúng chuẩn xứng đáng với công sức/đẳng cấp**."
            },
            {
                "name": "4. 〜として",
                "meaning": "Với tư cách là / Ở vị trí, vai trò là...",
                "connection": "N + として（は / も / の + N）",
                "examples": [
                    ("私（わたし）は留学生（りゅうがくせい）代表（だいひょう）**として**、スピーチを行（おこな）った。", "Tôi đã phát biểu với tư cách đại diện du học sinh."),
                    ("この地方（ちほう）は、米（こめ）の産地（さんち）**として**有名（ゆうめい）だ。", "Vùng này nổi tiếng với vai trò là vùng sản xuất gạo."),
                ],
                "note": "Phân biệt rõ với `にとって` (góc độ đánh giá của người/tổ chức)!"
            },
            {
                "name": "5. 〜にとって",
                "meaning": "Đối với (xét theo góc nhìn, tầm quan trọng hoặc giá trị đối với đối tượng A thì...)",
                "connection": "N（người, tổ chức, tập thể...）+ にとって（は / も / の + N）",
                "examples": [
                    ("私（わたし）**にとって**、家族（かぞく）の存在（そんざい）は何（なに）よりも大切（たいせつ）だ。", "Đối với tôi, sự hiện diện của gia đình quan trọng hơn bất cứ thứ gì."),
                    ("高齢者（こうれいしゃ）**にとって**、駅（えき）にエレベーターがあることは非常（ひじょう）に助（たす）かる。", "Đối với người cao tuổi, việc nhà ga có thang máy giúp ích rất nhiều."),
                ],
                "note": "Vế sau là tính chất, đánh giá giá trị (`大切だ`, `難しい`, `便利だ`, `負担だ`) nhìn từ phía N; KHÔNG dùng cho hành động tác động trực tiếp vào N (khi đó dùng `に対して`)."
            },
            {
                "name": "6. 〜にしたら / 〜にすれば / 〜にしてみれば / 〜にしても",
                "meaning": "Nếu đứng ở lập trường / đặt mình vào vị trí cảm nhận của A mà xét thì...",
                "connection": "N（chỉ người, đối tượng có cảm xúc）+ にしたら / にすれば / にしてみれば / にしても",
                "examples": [
                    ("親（おや）**にすれば**、いくつになっても子（こ）どもは心配（しんぱい）なものだ。", "Đứng ở góc độ làm cha mẹ mà nói, dù con cái bao nhiêu tuổi vẫn luôn là nỗi lo lắng."),
                    ("本人（ほんにん）**にしてみれば**、悪気（わるぎ）があって言（い）ったわけではないのだろう。", "Đứng từ phía bản thân cậu ấy mà nghĩ thì chắc không phải cố ý nói ác đâu."),
                ],
                "note": "Thường dùng để đồng cảm hoặc suy đoán tâm trạng của một người khác khi đặt mình vào hoàn cảnh của họ."
            },
        ],
        "comparison": [
            ("〜わりに（は）", "So với thang đo/mức độ (giá, tuổi, công sức).", "Nối được cả với `Aい`, `Naな`, `Nの`."),
            ("〜にしては", "So với tiêu chuẩn cụ thể (`プロ`, `70歳`).", "KHÔNG nối với tính từ."),
            ("〜だけある", "Quả xứng đáng với (hợp kỳ vọng, khen).", "Trái ngược về tính bất ngờ với `わりに / にしては`."),
            ("〜にとって vs 〜として", "`にとって`: giá trị đối với ai; `として`: với tư cách/vai trò gì.", "`親にとって大切な子` vs `親としてすべきこと`."),
        ],
        "pitfalls": [
            "⚠️ Bẫy lớn nhất: `年のわりに` (mức độ tuổi tác -> `わりに`) vs `80歳にしては` (con số/đối tượng cụ thể -> `にしては`).",
            "⚠️ Phân biệt `〜に対して` (hướng hành động tới N: `先生に対して失礼だ`) với `〜にとって` (đánh giá đối với N: `私にとって大切な先生だ`)."
        ],
        "quiz": [
            ("このコートは軽（かる）い（　　）、とても暖（あたた）かい。", ["わりに", "にしては", "だけあって", "にとって"], 1, "Sau tính từ đuôi い 軽い chỉ dùng được わりに (にしては không đi sau tính từ)."),
            ("フランス人（じん）（　　）、漢字（かんじ）の知識（ちしき）がかなり豊富（ほうふ）だ。", ["にしては", "だけあって", "にすれば", "にとって"], 1, "Đánh giá bất ngờ dựa trên danh xưng cụ thể フランス人 -> にしては."),
            ("さすが一流（いちりゅう）ホテル（　　）、ロビーからすでに高級感（こうきゅうかん）があふれている。", ["だけあって", "にしては", "のわりに", "にとって"], 1, "Quả xứng danh khách sạn hàng đầu (đúng kỳ vọng) -> だけあって."),
            ("初心者（しょしんしゃ）（　　）、この専門書（せんもんしょ）の内容（ないよう）は理解（りかい）しにくい。", ["にとって", "として", "だけあって", "にしては"], 1, "Đánh giá mức độ khó đối với đối tượng 初心者 -> にとって."),
            ("厳（きび）しく叱（しか）ったものの、親（おや）（　　）子どもの将来（しょうらい）を思（おも）ってのことだった。", ["にしてみれば", "だけあって", "のわりに", "として"], 1, "Đứng trên lập trường tâm trạng của cha mẹ -> にしてみれば."),
        ]
    },
    20: {
        "title_jp": "結果はどうなったか",
        "title_vi": "Diễn Biến & Kết Cục Sau Cùng",
        "section": "III. 評価・判断する",
        "intro": "Bài 20 trong **Shinkanzen Master Ngữ pháp N2** tập trung vào 6 mẫu miêu tả **kết cục sau khi thực hiện một quá trình hoặc hành động** (`〜たところ`, `〜きり`, `〜あげく`, `〜末（に）`, `〜ところだった`, `〜ずじまいだ`).",
        "patterns": [
            {
                "name": "1. 〜たところ",
                "meaning": "Sau khi thử làm A thì nhận được kết quả/phát hiện là B (kết quả thực tế ngay sau khi thử).",
                "connection": "V-た + ところ",
                "examples": [
                    ("先生（せんせい）に相談（そうだん）した**ところ**、快（こころよ）く引（ひ）き受（う）けてくださった。", "Sau khi trao đổi thử với thầy, thầy đã vui vẻ nhận lời giúp."),
                    ("病院（びょういん）で検査（けんさ）を受（う）けた**ところ**、どこも悪（わる）くないと言（い）われた。", "Sau khi đi kiểm tra ở bệnh viện, bác sĩ bảo không có chỗ nào bị sao cả."),
                ],
                "note": "Thường đi với vế sau là sự việc đã xảy ra ở thì quá khứ (`〜た`), mang tính tường thuật khách quan hoặc phát hiện bất ngờ."
            },
            {
                "name": "2. 〜きり",
                "meaning": "Từ sau lần đó trở đi là... (giữ nguyên trạng thái đó mãi / bặt vô âm tín không làm lại nữa).",
                "connection": "V-た / N + きり",
                "examples": [
                    ("彼（かれ）とは卒業式（そつぎょうしき）の日（ひ）に会（あ）った**きり**、一度（いちど）も連絡（れんらく）を取（と）っていない。", "Từ sau hôm lễ tốt nghiệp gặp nhau đó đến nay, tôi chưa hề liên lạc lại với cậu ấy."),
                    ("息子（むすこ）は部屋（へや）に閉じこもった**きり**、出（で）てこない。", "Con trai cứ nhốt mình trong phòng từ nãy đến giờ mãi chẳng chịu ra."),
                ],
                "note": "Có dạng `これっきり`, `一度きり` = chỉ một lần duy nhất rồi thôi."
            },
            {
                "name": "3. 〜あげく",
                "meaning": "Sau bao nhiêu suy nghĩ/vất vả/cãi vã... cuối cùng lại ra kết quả KHÔNG TỐT (thường mang nghĩa tiêu cực).",
                "connection": "V-た / N（danh động từ）+ の + あげく（に）",
                "examples": [
                    ("長時間（ちょうじかん）迷（まよ）った**あげく**、結局（けっきょく）何（なに）も買（か）わずに帰（かえ）った。", "Sau một hồi lâu đắn đo suy nghĩ, rốt cuộc tôi lại về tay không chẳng mua gì."),
                    ("激（はげ）しい口論（こうろん）**のあげく**、二人（ふたり）は絶交（ぜっこう）してしまった。", "Sau hồi cãi vã nảy lửa, hai người đã cắt đứt quan hệ luôn."),
                ],
                "note": "Kết quả vế sau hầu như **luôn tiêu cực, thất vọng hoặc không như ý**."
            },
            {
                "name": "4. 〜末（すえ）（に）",
                "meaning": "Sau một quá trình dài nỗ lực/trăn trở/thử nghiệm... cuối cùng cũng đi tới kết cục B.",
                "connection": "V-た / N（danh động từ）+ の + 末（すえ）（に）",
                "examples": [
                    ("何度（なんど）も試行（しこう）錯誤（さくご）を重（かさ）ねた**末（すえ）に**、ついに新薬（しんやく）が完成（かんせい）した。", "Sau biết bao lần thử và sai lặp đi lặp lại, cuối cùng thuốc mới cũng hoàn thành."),
                    ("苦労（くろう）**の末（すえ）**、念願（ねんがん）の自分（じぶん）の店（みせ）を持（も）つことができた。", "Sau bao gian khổ, cuối cùng tôi đã có được cửa hàng mơ ước của riêng mình."),
                ],
                "note": "Dùng được cho cả kết quả **tích cực** (thành công sau gian lao) lẫn **tiêu cực** (kết cục đáng buồn)."
            },
            {
                "name": "5. 〜ところだった",
                "meaning": "Suýt chút nữa thì đã... rồi (may mà thực tế không xảy ra!).",
                "connection": "V-る / V-ない + ところだった",
                "examples": [
                    ("あと少（すこ）しで終電（しゅうでん）に乗（の）り遅（おく）れる**ところだった**。", "Chỉ chút xíu nữa thôi là tôi đã trễ chuyến tàu cuối rồi."),
                    ("鍵（かぎ）を閉（し）め忘（わす）れて、泥棒（どろぼう）に入（はい）られるところだった。", "Quên khóa cửa làm suýt chút nữa bị trộm lẻn vào nhà."),
                ],
                "note": "Hay đi kèm với các phó từ `もうちょっとで`, `あと少しで`, `危うく` (suýt nữa)."
            },
            {
                "name": "6. 〜ずじまいだ",
                "meaning": "Định bụng làm thế mà rốt cuộc vẫn chưa kịp làm / bỏ lỡ luôn đến lúc kết thúc.",
                "connection": "V-ない（bỏ ない, riêng する -> せず）+ じまいだ（じまいだった）",
                "examples": [
                    ("北海道（ほっかいどう）へ行（い）きたいと思（おも）いながら、忙（いそが）しくて行（い）か**ずじまいだった**。", "Trong lòng vẫn muốn đi Hokkaido mà bận quá cuối cùng vẫn chẳng đi được."),
                    ("感謝（かんしゃ）の気持（きも）ちを伝（つた）えたいと思いながら、とうとう言（い）え**ずじまいだった**。", "Định bụng nói lời cảm ơn mà rốt cuộc cứ chần chừ mãi không nói ra được."),
                ],
                "note": "Mang sắc thái tiếc nuối nhẹ vì dự định ban đầu cuối cùng không thực hiện được. Chú ý `する` chia thành `せずじまい`."
            },
        ],
        "comparison": [
            ("〜あげく", "Kết quả sau quá trình dài thường **TIÊU CỰC** (`迷ったあげく`, `口論のあげく`).", "Gần như luôn kết thúc bằng chuyện không hay."),
            ("〜末（に）", "Kết quả sau quá trình dài vất vả, trung tính (tốt hoặc xấu).", "Hay dùng cho thành tựu gian nan (`努力の末に`)."),
            ("〜たところ", "Làm thử A và thấy ngay kết quả B.", "Không đòi hỏi quá trình gian nan kéo dài."),
            ("〜ずじまいだ", "Cuối cùng vẫn chưa làm được việc định làm.", "Cấu trúc chia `V-ない (bỏ ない) + ずじまい`."),
        ],
        "pitfalls": [
            "⚠️ Bẫy chia `する`: `せずじまいだ` (KHÔNG phải `しずじまい`!).",
            "⚠️ Không dùng `〜あげく` cho thành tích vui vẻ như ✗ `努力したあげく、試験に合格した` -> phải dùng `努力の末に`."
        ],
        "quiz": [
            ("大雪（おおゆき）の道（みち）で滑（すべ）って、あと少（すこ）しで転（ころ）ぶ（　　）。", ["ところだった", "きりだった", "あげくだった", "ずじまいだった"], 1, "Suýt nữa thì ngã (nhưng may không ngã) -> ところだった."),
            ("長（なが）い研究（けんきゅう）の（　　）、画期的（かっきてき）な治療法（ちりょうほう）が開発（かいはつ）された。", ["末（すえ）に", "あげく", "きり", "ところ"], 1, "Kết quả tích cực sau quá trình nghiên cứu dài -> 末に."),
            ("何時間（なんじかん）も悩（なや）んだ（　　）、間違（まちが）った方（ほう）を選（えら）んでしまった。", ["あげく", "ところだった", "きり", "ずじまい"], 1, "Suy nghĩ mãi rồi lại chọn nhầm (kết quả xấu) -> あげく."),
            ("借（か）りた本（ほん）を返（かえ）そうと思（おも）いつつ、忙（いそが）しくて返（かえ）さ（　　）になっている。", ["ずじまい", "きり", "あげく", "ところ"], 1, "Định trả mà cuối cùng vẫn chưa trả được -> V-ずじまい."),
            ("メールを送（おく）った（　　）、すぐに相手（あいて）から丁寧（ていねい）な返信（へんしん）が来（き）た。", ["ところ", "きり", "あげく", "末（すえ）に"], 1, "Làm hành động A và nhận kết quả B ngay sau đó -> たところ."),
        ]
    },
    21: {
        "title_jp": "強く言う・軽く言う",
        "title_vi": "Nhấn Mạnh Cực Đoan & Xem Nhẹ Mức Độ",
        "section": "IV. 気持ちを表現する",
        "intro": "Bài 21 trong **Shinkanzen Master Ngữ pháp N2** mở đầu Phần IV (biểu đạt cảm xúc và thái độ của người nói) với các cấu trúc **coi nhẹ mức độ tối thiểu** hoặc **nhấn mạnh thái quá đến mức cực đoan** (`〜くらい / 〜ぐらい`, `〜など / 〜なんか / 〜なんて`, `〜まで / 〜までして / 〜てまで`, `〜（一）〜ない`, `〜さえ`).",
        "patterns": [
            {
                "name": "1. 〜くらい / 〜ぐらい",
                "meaning": "Ít ra cỡ chuyện nhỏ nhặt như... thì (nên làm / cũng không đáng kể).",
                "connection": "N / Thể thông thường + くらい / ぐらい",
                "examples": [
                    ("忙（いそが）しくても、自分の部屋（へや）を片付（かたづ）ける**くらい**の時間はあるはずだ。", "Dù có bận thì ít nhất cũng phải có chút thời gian dọn phòng mình chứ."),
                    ("お礼（れい）の電話（でんわ）**ぐらい**かけてきてもいいのに。", "Ít ra cũng gọi lấy một cuộc điện thoại cảm ơn thì tốt biết mấy."),
                ],
                "note": "Thường đi với sắc thái coi đó là mức tối thiểu đương nhiên, hoặc hơi chê trách ai không làm nổi mức tối thiểu."
            },
            {
                "name": "2. 〜など / 〜なんか / 〜なんて",
                "meaning": "Những thứ như... (xem nhẹ, hạ thấp giá trị, hoặc ngạc nhiên vì không ngờ).",
                "connection": "N（+ trợ từ）/ Thể thông thường + など / なんか / なんて",
                "examples": [
                    ("他人（たにん）の噂（うわさ）話（ばなし）**など**、気（き）にする必要（ひつよう）はありません。", "Mấy chuyện đồn thổi của người ngoài thì việc gì phải bận tâm."),
                    ("自分（じぶん）**なんか**にできるだろうか、と不安（ふあん）になることもある。", "Đôi lúc tôi cũng bất an tự hỏi kẻ tầm thường như mình liệu có làm nổi không."),
                ],
                "note": "`など` dùng trong văn viết/trang trọng; `なんか` và `なんて` mang sắc thái khẩu ngữ mạnh hơn (khiêm tốn hạ mình hoặc coi thường/ngạc nhiên)."
            },
            {
                "name": "3. 〜まで / 〜までして / 〜てまで",
                "meaning": "Đến mức làm cả việc cực đoan như... / Bất chấp làm đến độ... (ngạc nhiên, phê phán sự thái quá).",
                "connection": "N + まで（して） / V-て + まで",
                "examples": [
                    ("借金（しゃっきん）をし**てまで**、高級（こうきゅう）車（しゃ）を買（か）う必要（ひつよう）があるのだろうか。", "Liệu có cần thiết phải vay nợ để bằng được mua xe sang như thế không?"),
                    ("睡眠（すいみん）時間（じかん）を削（けず）って**まで**仕事（しごと）をするのは体（からだ）によくない。", "Làm việc đến mức cắt xén cả giờ ngủ thì không tốt cho sức khỏe đâu."),
                ],
                "note": "Diễn tả mức độ hành động vượt quá giới hạn thông thường khiến người nói bất ngờ hoặc phản đối."
            },
            {
                "name": "4. 〜（一）〜ない / 〜として〜ない",
                "meaning": "Đến cả một (đơn vị nhỏ nhất) cũng không... (Phủ định tuyệt đối 100%, không chừa ngoại lệ nào).",
                "connection": "一（いち・ひと）+ lượng từ + も + phủ định ｜ từ nghi vấn + として + phủ định",
                "examples": [
                    ("昨日（きのう）のテストは難（むずか）しくて、一問（いちもん）**も**解（と）け**なかった**。", "Bài kiểm tra hôm qua khó đến mức tôi không giải nổi lấy một câu."),
                    ("会議（かいぎ）では誰（だれ）一人（ひとり）**として**反対（はんたい）する者（もの）はい**なかった**。", "Trong cuộc họp chẳng có lấy một ai phản đối cả."),
                ],
                "note": "Các cụm hay gặp: `一つとして〜ない`, `誰一人〜ない`, `一滴も〜ない`, `一時として〜ない`."
            },
            {
                "name": "5. 〜さえ",
                "meaning": "Ngay cả đến... cũng... (Lấy ví dụ cực đoan nhất để ngụ ý mọi cái bình thường khác đương nhiên đều như vậy).",
                "connection": "N（+ trợ từ） / V-ます + さえ / V-て + さえ",
                "examples": [
                    ("忙（いそが）しすぎて、昼（ひる）ご飯（はん）を食べる時間（じかん）**さえ**ない。", "Bận tối mắt tới mức ngay cả thời gian ăn trưa cũng không có."),
                    ("こんな簡単（かんたん）な問題（もんだい）は、小学生（しょうがくせい）**さえ**解（と）ける。", "Bài toán dễ thế này thì ngay cả học sinh tiểu học cũng giải được."),
                ],
                "note": "Phân biệt `さえ` (ngay cả... — nhấn mạnh) vs `さえ〜ば` (chỉ cần... là đủ — điều kiện)."
            },
        ],
        "comparison": [
            ("〜くらい", "Xem nhẹ mức tối thiểu (`挨拶くらいする`).", "Hàm ý \"chỉ mức nhỏ thế thôi mà...\"."),
            ("〜など / なんか / なんて", "Coi nhẹ, hạ thấp giá trị đối tượng hoặc khiêm nhường.", "`など` văn viết; `なんか/なんて` khẩu ngữ."),
            ("〜てまで / 〜までして", "Bất chấp làm tới mức cực đoan thái quá.", "Thường thể hiện ngạc nhiên hoặc phê phán."),
            ("〜さえ", "Ngay cả trường hợp ít ngờ nhất cũng...", "Khác `〜さえ〜ば` (chỉ cần A là đủ)."),
        ],
        "pitfalls": [
            "⚠️ Chú ý vị trí trợ từ với `〜など / 〜なんか`: thường đứng thay `を・が` (`お金などいらない`), nhưng đứng sau `に・へ・と・から` (`そんな人になんか頼まない`).",
            "⚠️ Trong `〜てまで`, vế sau thường mang đánh giá tiêu cực/hoài nghi hoặc câu hỏi tu từ (`〜必要があるのか`, `〜べきではない`)."
        ],
        "quiz": [
            ("家（いえ）に帰（かえ）ったら、自分の靴（くつ）（　　）ちゃんと揃（そろ）えなさい。", ["くらい", "てまで", "さえ", "として"], 1, "Mức tối thiểu nhỏ nhất (xếp giày mình) -> くらい."),
            ("嘘（うそ）をつい（　　）、試験（しけん）に合格（ごうかく）したいとは思（おも）わない。", ["てまで", "くらい", "など", "さえ"], 1, "Bất chấp làm điều cực đoan sai trái -> V-て + まで."),
            ("台風（たいふう）が接近（せっきん）しているせいか、町（まち）には人（ひと）の気配（けはい）が一人（ひとり）（　　）ない。", ["として", "くらい", "など", "てまで"], 1, "Phủ định tuyệt đối không có lấy một bóng người -> 一人として〜ない."),
            ("私（わたし）（　　）にこんな大役（たいやく）が務（つと）まるかどうか心配（しんぱい）だ。", ["なんか", "てまで", "くらい", "として"], 1, "Khiêm nhường hạ thấp bản thân -> なんか."),
            ("今日（きょう）は喉（のど）が痛（いた）くて、水（みず）（　　）飲（の）むのが辛（つら）い。", ["さえ", "てまで", "として", "など"], 1, "Ngay cả thứ dễ nhất là uống nước cũng khổ -> さえ."),
        ]
    },
    22: {
        "title_jp": "〜だろうと思う",
        "title_vi": "Phỏng Đoán & Khẳng Định Chắc Chắn",
        "section": "IV. 気持ちを表現する",
        "intro": "Bài 22 trong **Shinkanzen Master Ngữ pháp N2** gom 6 cấu trúc diễn đạt **suy đoán theo mức độ chắc chắn và nguy cơ dự báo** (`〜とみえる`, `〜かねない`, `〜おそれがある`, `〜まい・〜ではあるまいか`, `〜に違いない・〜に相違ない`, `〜にきまっている`).",
        "patterns": [
            {
                "name": "1. 〜とみえる / 〜とみえて",
                "meaning": "Trông có vẻ như là... / Nhìn biểu hiện bên ngoài có lẽ là...",
                "connection": "Thể thông thường（Na-bỏ だ / N-bỏ だ）+ とみえる / とみえて",
                "examples": [
                    ("田中（たなか）さんは傘（かさ）を差（さ）さずに帰（かえ）っていった。雨（あめ）はもう止（や）んだ**とみえる**。", "Anh Tanaka không che ô mà về luôn rồi. Có vẻ trời đã tạnh mưa rồi đấy."),
                    ("昨夜（さくや）よく眠（ねむ）れなかった**とみえて**、彼女（かのじょ）は朝からあくびばかりしている。", "Trông có vẻ đêm qua ngủ không ngon nên sáng giờ cô ấy cứ ngáp suốt."),
                ],
                "note": "Suy đoán khách quan dựa trên **dấu hiệu nhìn thấy bằng mắt thường** ở người khác/sự vật (không dùng cho chính mình)."
            },
            {
                "name": "2. 〜かねない",
                "meaning": "Rất có thể sẽ xảy ra (nguy cơ, hậu quả xấu không mong muốn).",
                "connection": "V-ます（bỏ ます）+ かねない",
                "examples": [
                    ("そんな無茶（むちゃ）な運転（うんてん）をしていたら、大事故（だいじこ）を起（お）こし**かねない**。", "Cứ lái xe ẩu tả như thế thì rất có thể sẽ gây ra tai nạn lớn đấy."),
                    ("睡眠（すいみん）不足（ぶそく）が続（つづ）くと、体（からだ）を壊（こわ）し**かねない**。", "Nếu thiếu ngủ kéo dài, rất có nguy cơ đổ bệnh đấy."),
                ],
                "note": "Vế sau LUÔN là **tình huống tiêu cực**! Đừng bao giờ nhầm với `〜かねる` (khó lòng — Bài 18)!"
            },
            {
                "name": "3. 〜おそれがある",
                "meaning": "Có nguy cơ / E rằng có khả năng xảy ra (chỉ cảnh báo rủi ro, thiên tai, bệnh tật — văn phong tin tức/báo chí).",
                "connection": "V-る / N + の + おそれがある",
                "examples": [
                    ("この台風（たいふう）は明日（あす）の朝（あさ）、関東（かんとう）地方（ちほう）に上陸（じょうりく）する**おそれがある**。", "Cơn bão này có nguy cơ đổ bộ vào vùng Kanto vào sáng mai."),
                    ("個人情報（こじんじょうほう）が外部（がいぶ）に流出（りゅうしゅつ）する**おそれがある**ため、対策（たいさく）を強化（きょうか）した。", "Vì có nguy cơ rò rỉ thông tin cá nhân ra bên ngoài nên chúng tôi đã tăng cường biện pháp."),
                ],
                "note": "Trang trọng, khách quan hơn `かねない`; chuyên dùng trong dự báo thời tiết, cảnh báo y tế, thông báo công ty."
            },
            {
                "name": "4. 〜まい / 〜ではあるまいか",
                "meaning": "1) `〜まい`: Chắc sẽ không... đâu (phỏng đoán phủ định — văn viết); 2) `〜ではあるまいか`: Chẳng phải là... hay sao?",
                "connection": "V-る（nhóm II/III có thể bỏ る: 見まい・すまい）+ まい ｜ Thể thông thường（Na・N）+ ではあるまいか",
                "examples": [
                    ("こんなに曇（くも）っているのだから、今日（きょう）は星（ほし）は見（み）え**まい**。", "Trời nhiều mây thế này thì hôm nay chắc sẽ không nhìn thấy sao đâu."),
                    ("この問題（もんだい）の本当（ほんとう）の原因（げんいん）は、コミュニケーション不足（ぶそく）**ではあるまいか**。", "Nguyên nhân thực sự của vấn đề này chẳng phải chính là do thiếu giao tiếp hay sao?"),
                ],
                "note": "Phân biệt: `〜まい` trong Bài 22 là phỏng đoán cho người/sự việc khác (\"chắc là không\"); ở Bài 24 `〜まい` ngôi 1 là ý chí (\"tôi quyết không\")."
            },
            {
                "name": "5. 〜に違（ちが）いない / 〜に相違（そうい）ない",
                "meaning": "Chắc chắn là... / Không còn nghi ngờ gì nữa (Suy luận đầy tự tin của người nói).",
                "connection": "Thể thông thường（Na-bỏ だ / N-bỏ だ）+ に違（ちが）いない / に相違（そうい）ない",
                "examples": [
                    ("鍵（かぎ）がかかっているから、誰（だれ）もいない**に違（ちが）いない**。", "Cửa khóa thế này thì chắc chắn không có ai ở nhà rồi."),
                    ("この証拠（しょうこ）から考（かんが）えると、犯人（はんにん）は彼（かれ）**に相違（そうい）ない**。", "Xét từ bằng chứng này thì thủ phạm chắc chắn không sai là hắn ta."),
                ],
                "note": "`に相違ない` là dạng văn viết trang trọng, cứng hơn `に違いない`."
            },
            {
                "name": "6. 〜にきまっている",
                "meaning": "Chắc chắn mười mươi là... rồi / Kiểu gì chẳng... (Khẳng định chủ quan mạnh mẽ, đôi khi hơi áp đặt).",
                "connection": "Thể thông thường（Na-bỏ だ / N-bỏ だ）+ にきまっている",
                "examples": [
                    ("あんなに練習（れんしゅう）したのだから、今回（こんかい）の試合（しあい）は勝（か）つ**にきまっている**。", "Đã luyện tập đến thế rồi thì trận đấu lần này kiểu gì chẳng thắng."),
                    ("彼（かれ）のことだから、どうせ遅刻（ちこく）する**にきまっている**。", "Tính cậu ta thì đằng nào cũng đi muộn cho mà xem."),
                ],
                "note": "Khẩu ngữ, mang tính chủ quan cao hơn `に違いない`."
            },
        ],
        "comparison": [
            ("〜かねない", "Có nguy cơ xấu xảy ra (`事故を起こしかねない`).", "Vế sau luôn tiêu cực; khác `かねる` (Bài 18)."),
            ("〜おそれがある", "Cảnh báo nguy cơ khách quan (bản tin, thông báo).", "Dùng với `V-る` hoặc `Nの`."),
            ("〜に違いない / 相違ない", "Khẳng định chắc chắn gần 100%.", "`相違ない` là văn viết trang trọng."),
            ("〜にきまっている", "Khẳng định chủ quan kiểu \"kiểu gì chẳng thế\".", "Thường dùng trong văn nói."),
        ],
        "pitfalls": [
            "⚠️ Bẫy lớn nhất: `〜かねる` (từ chối/khó lòng) vs `〜かねない` (rất có thể gây ra điều xấu).",
            "⚠️ Trước `に違いない / にきまっている / とみえる` không thêm `だ` sau danh từ và tính từ đuôi な (`学生に違いない`, `静かに違いない`)."
        ],
        "quiz": [
            ("この川（かわ）は台風（たいふう）の大雨（おおあめ）で氾濫（はんらん）する（　　）。", ["おそれがある", "とみえる", "にきまっている", "まい"], 1, "Cảnh báo rủi ro thiên tai trong bản tin -> おそれがある."),
            ("疲（つか）れたまま運転（うんてん）を続（つづ）けると、大事故（だいじこ）を引（ひ）き起（お）こし（　　）。", ["かねない", "かねる", "とみえる", "にきまっている"], 1, "Nguy cơ xảy ra tai nạn xấu -> V-ます + かねない."),
            ("玄関（げんかん）に靴（くつ）がたくさん並（なら）んでいる。もうお客（きゃく）さんが来（き）ている（　　）。", ["とみえる", "かねない", "おそれがある", "まい"], 1, "Suy đoán dựa trên dấu hiệu nhìn thấy -> とみえる."),
            ("防犯（ぼうはん）カメラに映（うつ）っていた以上（いじょう）、彼が関与（かんよ）している（　　）。", ["に相違（そうい）ない", "おそれがある", "かねない", "とみえる"], 1, "Khẳng định chắc chắn dựa trên chứng cứ -> に相違ない."),
            ("こんな悪条件（あくじょうけん）では、成功（せいこう）など望（のぞ）め（　　）。", ["まい", "かねない", "にきまっている", "おそれがある"], 1, "Phỏng đoán phủ định văn viết \"chắc chẳng thể hy vọng\" -> 望めまい."),
        ]
    },
    23: {
        "title_jp": "感想を言う・主張する",
        "title_vi": "Cảm Nhận Quy Luật & Chủ Trương Bản Chất",
        "section": "IV. 気持ちを表現する",
        "intro": "Bài 23 trong **Shinkanzen Master Ngữ pháp N2** tổng hợp 7 mẫu biểu đạt **quy luật chung, nhận xét đánh giá bản chất, sự lựa chọn tối ưu/duy nhất và lời khuyên nghĩa vụ** (`〜ものだ`, `〜というものだ`, `〜にすぎない`, `〜にほかならない`, `〜に越したことはない`, `〜しかない・〜よりほかない`, `〜べきだ`).",
        "patterns": [
            {
                "name": "1. 〜ものだ",
                "meaning": "Vốn dĩ thường là như thế / Quy luật tự nhiên là vậy (nêu chân lý, bản chất phổ quát).",
                "connection": "V-る・V-ない / Aい / Na-な + ものだ",
                "examples": [
                    ("人間（にんげん）は誰（だれ）でも、年（とし）をとると体力（たいりょく）が衰（おとろ）える**ものだ**。", "Con người ai rồi cũng vậy, khi có tuổi thì thể lực vốn dĩ sẽ suy giảm."),
                    ("自分（じぶん）の欠点（けってん）にはなかなか気（き）づきにくい**ものだ**。", "Thường thì người ta rất khó tự nhận ra khuyết điểm của chính bản thân mình."),
                ],
                "note": "Trong Bài 23 diễn tả bản chất/chân lý phổ biến (với từ khái quát như `人は`, `誰でも`, `本来`)."
            },
            {
                "name": "2. 〜というものだ",
                "meaning": "Đúng là... thật đấy / Quả thực là điều đương nhiên như vậy (khẳng định cảm nhận đánh giá sự việc).",
                "connection": "Thể thông thường（Na-だ/な, N-だ/bỏ だ）+ というものだ",
                "examples": [
                    ("練習（れんしゅう）もせずに勝（か）とうとするなんて、虫（むし）がよすぎる**というものだ**。", "Chưa luyện tập gì mà đòi thắng thì đúng là quá khôn lỏi/mơ mộng rồi còn gì."),
                    ("相手（あいて）の苦労（くろう）が分（わ）かってこそ、本当（ほんとう）の友人（ゆうじん）**というものだ**。", "Phải thấu hiểu nỗi vất vả của nhau mới thực sự gọi là bạn bè đúng nghĩa."),
                ],
                "note": "Thường nhận xét đánh giá sau khi chứng kiến một sự việc cụ thể."
            },
            {
                "name": "3. 〜にすぎない",
                "meaning": "Chẳng qua chỉ là... mà thôi (đánh giá thấp giá trị/quy mô).",
                "connection": "Thể thông thường（Na・N bỏ だ）+ にすぎない",
                "examples": [
                    ("それは単（たん）なる噂（うわさ）**にすぎない**ので、信（しん）じる必要（ひつよう）はない。", "Đó chẳng qua chỉ là tin đồn nhảm thôi nên chẳng cần tin làm gì."),
                    ("私（わたし）はただ自分（じぶん）のやるべきことをやった**にすぎません**。", "Tôi chẳng qua chỉ làm đúng phận sự mình cần làm mà thôi."),
                ],
                "note": "Hay đi kèm với các từ giảm nhẹ `ただ`, `単なる`, `ほんの`."
            },
            {
                "name": "4. 〜にほかならない",
                "meaning": "Chính là... chứ không gì khác / Không ngoài nguyên nhân nào khác chính là...",
                "connection": "N + にほかならない",
                "examples": [
                    ("今回（こんかい）の成功（せいこう）は、皆様（みなさま）のご協力（きょうりょく）の賜物（たまもの）**にほかならない**。", "Thành công lần này chính là thành quả từ sự hợp tác của quý vị chứ không gì khác."),
                    ("彼女（かのじょ）が厳（きび）しく言（い）うのは、あなたを思（おも）う愛情（あいじょう）の表（あらわ）れ**にほかならない**。", "Cô ấy nói nghiêm khắc như vậy chính là biểu hiện của tình thương dành cho bạn đấy."),
                ],
                "note": "Khẳng định mạnh mẽ bản chất hoặc nguyên nhân cốt lõi; thường mở đầu bằng `〜のは〜にほかならない`."
            },
            {
                "name": "5. 〜に越（こ）したことはない",
                "meaning": "Tốt nhất vẫn là... / Không gì bằng việc... (nêu phương án lý tưởng, an toàn nhất).",
                "connection": "V-る・V-ない / Aい / Na-である / N-である + に越（こ）したことはない",
                "examples": [
                    ("病気（びょうき）になったら治（なお）せばいいが、予防（よぼう）できる**に越（こ）したことはない**。", "Bị bệnh thì chữa cũng được, nhưng tốt nhất vẫn là phòng ngừa được từ trước."),
                    ("準備（じゅんび）は早（はや）めにする**に越（こ）したことはない**。", "Việc chuẩn bị thì làm sớm vẫn là tốt nhất."),
                ],
                "note": "Dù không bắt buộc tuyệt đối nhưng khuyên rằng làm vậy là an toàn/tối ưu nhất."
            },
            {
                "name": "6. 〜しかない / 〜よりほかない",
                "meaning": "Chỉ còn cách... / Đành phải... (không còn phương án nào khác).",
                "connection": "V-る + しかない / ほかない / よりほか（は）ない",
                "examples": [
                    ("終電（しゅうでん）を逃（のが）したからには、タクシーで帰（かえ）る**しかない**。", "Một khi đã lỡ chuyến tàu cuối thì chỉ còn cách đi taxi về thôi."),
                    ("みんなが賛成（さんせい）している以上（いじょう）、従（したが）う**よりほかない**。", "Một khi mọi người đã đồng thuận cả rồi thì đành phải làm theo chứ sao."),
                ],
                "note": "`〜よりほかない` và `〜ほかしかたがない` mang sắc thái trang trọng hơn `しかない`."
            },
            {
                "name": "7. 〜べきだ / 〜べきではない",
                "meaning": "Nên / Phải làm... (theo đạo lý, trách nhiệm, lẽ phải chung); Không nên...",
                "connection": "V-る + べきだ / べきではない（する -> すべきだ / するべきだ）",
                "examples": [
                    ("約束（やくそく）したことは、必（かなら）ず守（まも）る**べきだ**。", "Đã hứa thì nhất định nên giữ lời."),
                    ("どんな理由（りゆう）があっても、他人（たにん）の秘密（ひみつ）を勝手（かって）に話（はな）す**べきではない**。", "Dù có lý do gì đi nữa, không nên tự tiện kể bí mật của người khác."),
                ],
                "note": "Không dùng `べきだ` để sai khiến trực tiếp bề trên (khi khuyên nhẹ hãy dùng `〜たほうがいい`). Chú ý `する -> すべき`."
            },
        ],
        "comparison": [
            ("〜にすぎない", "Đánh giá thấp (\"chẳng qua chỉ là\").", "Hay đi với `ただ`, `単なる`."),
            ("〜にほかならない", "Khẳng định cốt lõi (\"chính là, không gì khác\").", "Ngược sắc thái coi nhẹ của `にすぎない`."),
            ("〜に越したことはない", "Tốt nhất vẫn là (an toàn, tối ưu).", "Không mang nghĩa ép buộc khắt khe như `べきだ`."),
            ("〜しかない", "Không còn phương án nào khác -> đành làm.", "Nối sau `V-る`."),
        ],
        "pitfalls": [
            "⚠️ Động từ `する` trước `べきだ` thường chia thành `すべきだ` (cũng chấp nhận `するべきだ`).",
            "⚠️ Không nhầm `〜にすぎない` (chỉ là chuyện nhỏ) với `〜にほかならない` (chính là bản chất)."
        ],
        "quiz": [
            ("この企画（きかく）が成功（せいこう）したのは、全員（ぜんいん）の努力（どりょく）の結果（けっか）（　　）。", ["にほかならない", "にすぎない", "に越（こ）したことはない", "しかない"], 1, "Khẳng định bản chất nguyên nhân thành công -> にほかならない."),
            ("旅行（りょこう）の荷物（にもつ）は軽（かる）い（　　）が、必要（ひつよう）な薬（くすり）は忘（わす）れないようにしよう。", ["に越（こ）したことはない", "にすぎない", "べきではない", "というものだ"], 1, "Tốt nhất vẫn là nhẹ gọn -> に越したことはない."),
            ("それは個人（こじん）の感想（かんそう）（　　）、全体（ぜんたい）の意見（いけん）ではない。", ["にすぎず", "にほかならず", "べきで", "ものだ"], 1, "Chẳng qua chỉ là cảm nhận cá nhân (kết nối dạng liên dụng) -> にすぎず."),
            ("時間（じかん）がないのだから、今（いま）はタクシーを使（つか）う（　　）。", ["よりほかない", "にほかならない", "にすぎない", "に越したことはない"], 1, "Không còn lựa chọn khác -> よりほかない."),
            ("公共（こうきょう）の場（ば）では、周囲（しゅうい）の人（ひと）へのマナーを守（まも）る（　　）。", ["べきだ", "にすぎない", "よりほかない", "ものか"], 1, "Nghĩa vụ chuẩn mực chung -> べきだ."),
        ]
    },
    24: {
        "title_jp": "提案する・意志を表す",
        "title_vi": "Đề Xuất, Khuyên Bảo & Ý Chí",
        "section": "IV. 気持ちを表現する",
        "intro": "Bài 24 trong **Shinkanzen Master Ngữ pháp N2** tập hợp các mẫu **kêu gọi đề xuất, khuyên răn theo đạo lý hoặc cá nhân, không cần thiết, và ý chí phủ định/do dự** (`〜（よ）うではないか`, `〜ことだ`, `〜ものだ・〜ものではない`, `〜ことはない`, `〜まい・〜（よ）うか〜まいか`, `〜ものか`).",
        "patterns": [
            {
                "name": "1. 〜（よ）うではないか",
                "meaning": "Hãy cùng nhau làm... đi nào! (Lời kêu gọi trang trọng trong diễn văn, hội nghị, bài viết cổ vũ).",
                "connection": "V-よう（thể ý chí）+ ではないか / じゃないか",
                "examples": [
                    ("みんなで力（ちから）を合（あ）わせて、この困難（こんなん）を乗（の）り越（こ）え**ようではないか**。", "Chúng ta hãy cùng nhau hợp sức để vượt qua khó khăn này đi nào!"),
                    ("もう一度（いちど）、生活（せいかつ）習慣（しゅうかん）を見直（みなお）してみ**ようじゃないか**。", "Hãy thử xem xét lại thói quen sinh hoạt một lần nữa xem sao nhé."),
                ],
                "note": "`〜ようではないか` rất trang trọng (phát biểu trước tập thể); `〜ようじゃないか` thân mật hơn."
            },
            {
                "name": "2. 〜ことだ",
                "meaning": "Nên làm... (Lời khuyên trực tiếp, cụ thể giải quyết một tình huống nhất định).",
                "connection": "V-る / V-ない + ことだ",
                "examples": [
                    ("日本語（にほんご）が上手（じょうず）になりたければ、毎日（まいにち）声（こえ）に出（だ）して読（よ）む**ことだ**。", "Nếu muốn giỏi tiếng Nhật thì cách tốt nhất là mỗi ngày đọc to thành tiếng."),
                    ("健康（けんこう）のためには、あまり夜更（よふ）かしをしない**ことだ**。", "Vì sức khỏe thì không nên thức khuya quá nhiều."),
                ],
                "note": "Thường dùng với câu điều kiện (`〜たければ〜ことだ`, `〜ためには〜ことだ`) đưa ra lời khuyên trực tiếp cụ thể."
            },
            {
                "name": "3. 〜ものだ / 〜ものではない",
                "meaning": "Theo lẽ thường/đạo lý chung thì nên... / tuyệt đối không nên...",
                "connection": "V-る + ものだ / ものではない",
                "examples": [
                    ("困（こま）っている人（ひと）を見（み）たら、助（たす）けてあげる**ものだ**。", "Thấy người gặp khó khăn thì lẽ thường là nên giúp đỡ họ."),
                    ("陰（かげ）で人（ひと）の悪口（わるくち）を言（い）う**ものではない**。", "Không được nói xấu sau lưng người khác đâu nhé."),
                ],
                "note": "Khác `〜ことだ` (khuyên cụ thể để đạt mục tiêu cá nhân); `〜ものだ / ものではない` khuyên răn mang tính **đạo đức, chuẩn mực xã hội chung**."
            },
            {
                "name": "4. 〜ことはない",
                "meaning": "Không cần thiết phải... đâu (trấn an, khuyên đối phương đừng làm việc thừa).",
                "connection": "V-る + ことはない",
                "examples": [
                    ("大丈夫（だいじょうぶ）だよ。そんなに心配（しんぱい）する**ことはない**。", "Không sao đâu mà. Cậu chẳng việc gì phải lo lắng đến thế đâu."),
                    ("明日（あした）は休（やす）みなのだから、早起（はやお）きする**ことはない**。", "Ngày mai được nghỉ mà, không cần phải dậy sớm làm gì."),
                ],
                "note": "Chỉ có nghĩa **không cần thiết** (`必要がない`), KHÔNG phải \"chưa từng làm\" (`V-たことがない`)."
            },
            {
                "name": "5. 〜まい / 〜（よ）うか〜まいか",
                "meaning": "1) `V-る + まい` (ngôi 1): Quyết tâm không đời nào làm nữa; 2) `V-ようか V-まいか`: Phân vân không biết nên làm hay không nên làm.",
                "connection": "V-る（nhóm II/III: 見まい・すまい）+ まい ｜ V-ようか + V-まいか",
                "examples": [
                    ("あんな失敗（しっぱい）は二度（にど）とする**まい**と心（こころ）に誓（ちか）った。", "Tôi thề trong lòng sẽ không bao giờ lặp lại sai lầm như thế lần thứ hai."),
                    ("留学（りゅうがく）し**ようか**する**まいか**、ずっと迷（まよ）っている。", "Tôi cứ phân vân mãi không biết nên đi du học hay không."),
                ],
                "note": "Rất hay ra thi dạng lưỡng lự: `V-ようか + V-まいか` (cùng 1 động từ!)."
            },
            {
                "name": "6. 〜ものか",
                "meaning": "Đời nào tôi chịu làm... / Tuyệt đối không đời nào! (Ý chí phủ định quyết liệt).",
                "connection": "V-る + ものか（もんか）",
                "examples": [
                    ("ここで諦（あきら）める**ものか**。最後（さいご）まで戦（たたか）ってみせる。", "Đời nào tôi chịu bỏ cuộc ở đây chứ! Nhất định sẽ chiến đấu đến cùng."),
                ],
                "note": "Khẩu ngữ mạnh mẽ, biểu lộ quyết tâm không khuất phục."
            },
        ],
        "comparison": [
            ("〜ことだ", "Lời khuyên cụ thể cho vấn đề trước mắt (`毎日練習することだ`).", "Không mang nghĩa đạo lý chung bằng `ものだ`."),
            ("〜ものだ / ものではない", "Khuyên theo đạo đức xã hội chung (`悪口を言うものではない`).", "Dạng phủ định khuyên răn rất hay thi."),
            ("〜ことはない", "Không cần thiết phải làm (`心配することはない`).", "Khác `V-たことがない` (chưa từng)."),
            ("〜ようか〜まいか", "Do dự nên làm hay không nên làm.", "Cặp song hành thể ý chí + まい."),
        ],
        "pitfalls": [
            "⚠️ Đừng nhầm `〜ことはない` (không cần phải) với `〜ことがない` (không có chuyện / chưa từng).",
            "⚠️ Chú ý phân biệt `〜ことだ` (khuyên thực tiễn) và `〜ものではない` (răn đe đạo lý)."
        ],
        "quiz": [
            ("大学（だいがく）卒業後（そつぎょうご）、就職（しゅうしょく）（　　）迷（まよ）っている。", ["しようかするまいか", "するまいか", "ことだ", "ことはない"], 1, "Cấu trúc `Vようか + V（る）まいか`: phân vân không biết có nên làm V hay không -> 就職しようかするまいか."),
            ("ほんの些細（ささい）なミスなのだから、そんなに落（お）ち込（こ）む（　　）。", ["ことはない", "ことだ", "まいか", "ものではない"], 1, "`Vる + ことはない`: không việc gì / không cần thiết phải (rầu rĩ quá mức như vậy)."),
        ]
    },
    25: {
        "title_jp": "強くそう感じる・思いが強いられる",
        "title_vi": "Cảm Xúc Dâng Trào & Bị Thôi Thúc / Bắt Buộc",
        "section": "IV. 気持ちを表現する",
        "intro": "Bài 25 trong **Shinkanzen Master Ngữ pháp N2** tập hợp 5 cấu trúc cực hay thi trong Mondai 7 về **cảm xúc mãnh liệt không kìm nổi** và **cảm giác bị bắt buộc phải làm** (`〜てしかたがない / しょうがない / たまらない`, `〜てならない`, `〜ないではいられない / ずにはいられない`, `〜ないわけにはいかない`, `〜ざるを得ない`).",
        "patterns": [
            {
                "name": "1. 〜てしかたがない / 〜てしょうがない / 〜てたまらない",
                "meaning": "Vô cùng... / Quá đỗi... đến mức không chịu nổi (cảm giác cơ thể, ham muốn, cảm xúc ngôi thứ nhất).",
                "connection": "V-て / A-くて / Na-で + しかたがない / しょうがない / たまらない",
                "examples": [
                    ("ふるさとを離（はな）れて半年（はんとし）、家族（かぞく）に会（あ）いたくて**たまらない**。", "Xa quê nửa năm rồi, tôi nhớ muốn gặp gia đình đến cồn cào không chịu nổi."),
                    ("結果（けっか）発表（はっぴょう）が気（き）になって**しかたがない**。", "Tôi cứ nôn nao tò mò kết quả công bố đến đứng ngồi không yên."),
                ],
                "note": "`しょうがない` thiên về khẩu ngữ; `たまらない` hay đi với cảm giác thể chất (`眠くてたまらない`, `暑くてたまらない`) hoặc khát khao (`〜たくてたまらない`)."
            },
            {
                "name": "2. 〜てならない",
                "meaning": "Tự nhiên trào dâng cảm xúc/linh cảm... không ngăn lại được.",
                "connection": "V-て / A-くて / Na-で + ならない",
                "examples": [
                    ("何（なに）か悪（わる）いことが起（お）きるような気（き）がして**ならない**。", "Tôi cứ có linh cảm bất an như sắp có chuyện xấu gì xảy ra không ngừng."),
                    ("留学（りゅうがく）する娘（むすめ）のことが心配（しんぱい）で**ならない**。", "Tôi không sao ngừng lo lắng cho cô con gái sắp đi du học."),
                ],
                "note": "Thường đi với **cảm xúc nội tâm tự nhiên hoặc suy nghĩ** (`気がする`, `思える`, `残念だ`, `心配だ`, `不思議だ`), KHÔNG dùng cho cảm giác thể chất như ✗ `おなかが空いてならない`!"
            },
            {
                "name": "3. 〜ないではいられない / 〜ずにはいられない",
                "meaning": "Không thể kìm lòng mà cứ thế làm... / Không nhịn được mà phải... (bộc phát tự nhiên).",
                "connection": "V-ない + ではいられない ｜ V-ない（bỏ ない, riêng する -> せず）+ ずにはいられない",
                "examples": [
                    ("あんなに悲（かな）しい映画（えいが）を見（み）たら、誰（だれ）でも泣（な）か**ずにはいられない**。", "Xem bộ phim buồn đến thế thì ai cũng không thể kìm được nước mắt."),
                    ("目の前（まえ）でおいしそうなケーキを見（み）ると、つい手（て）を伸（の）ばさ**ないではいられない**。", "Hễ thấy chiếc bánh ngon lành trước mặt là không sao kìm được mà vươn tay ra lấy."),
                ],
                "note": "Khác `〜ないわけにはいかない` (làm vì nghĩa vụ/xã hội); `ずにはいられない` là **tự nhiên bộc phát không kìm chế nổi**."
            },
            {
                "name": "4. 〜ないわけにはいかない",
                "meaning": "Không thể không làm (= bắt buộc phải làm vì phép tắc, đạo đức, hoàn cảnh xã hội).",
                "connection": "V-ない + わけに（は）いかない",
                "examples": [
                    ("上司（じょうし）からの誘（さそ）いなので、行（い）か**ないわけにはいかない**。", "Vì là lời mời từ cấp trên nên tôi không thể không đi được."),
                    ("自分（じぶん）が責任者（せきにんしゃ）だから、謝（あやま）ら**ないわけにはいかない**。", "Vì mình là người chịu trách nhiệm nên không thể không xin lỗi."),
                ],
                "note": "Xuất phát từ **trách nhiệm xã hội hoặc tâm lý**."
            },
            {
                "name": "5. 〜ざるを得（え）ない",
                "meaning": "Buộc lòng phải / Đành phải làm... (trong lòng không muốn nhưng không còn lựa chọn nào khác).",
                "connection": "V-ない（bỏ ない, riêng する -> せ）+ ざるを得（え）ない",
                "examples": [
                    ("台風（たいふう）が接近（せっきん）しているため、明日（あした）のイベントは中止（ちゅうし）**せざるを得（え）ない**。", "Vì bão đang tiến gần nên ngày mai đành buộc phải hủy sự kiện."),
                    ("これだけの証拠（しょうこ）がある以上（いじょう）、事実（じじつ）を認（みと）め**ざるを得（え）ない**。", "Đã có từng này bằng chứng thì đành phải thừa nhận sự thật thôi."),
                ],
                "note": "Văn viết trang trọng hơn `ないわけにはいかない`, nhấn mạnh tính **bất đắc dĩ không còn lối thoát**. Nhớ đặc biệt: `する -> せざるを得ない`!"
            },
        ],
        "comparison": [
            ("〜てたまらない", "Cảm giác cơ thể/ham muốn mãnh liệt (`痛くてたまらない`, `会いたくてたまらない`).", "Dùng nhiều cho giác quan cơ thể."),
            ("〜てならない", "Cảm xúc nội tâm/linh cảm tự trào (`気がしてならない`, `思えてならない`).", "KHÔNG dùng cho cảm giác đói/khát/buồn ngủ."),
            ("〜ずにはいられない", "Không nhịn được, bộc phát tự nhiên (`笑わずにはいられない`).", "Xuất phát từ phản xạ/tâm lý tự nhiên."),
            ("〜ざるを得ない", "Đành phải làm (bất đắc dĩ không còn cách nào).", "Văn viết; `する -> せざるを得ない`."),
        ],
        "pitfalls": [
            "⚠️ Phân biệt `〜ずにはいられない` (tự nhiên không kìm được -> `笑う`, `泣く`, `言わずに`) vs `〜ざるを得ない` (bất đắc dĩ phải -> `認める`, `中止する`, `変更する`).",
            "⚠️ Chia đúng động từ `する`: `せずにはいられない` nhưng `せざるを得ない`!"
        ],
        "quiz": [
            ("お笑い番組（ばんぐみ）があまりにも面白（おもしろ）くて、笑（わら）わ（　　）。", ["ずにはいられない", "ざるを得（え）ない", "てならない", "てたまらない"], 1, "Không kìm được bật cười tự nhiên -> 笑わずにはいられない."),
            ("予算（よさん）が大幅（おおはば）に不足（ふそく）しているため、計画（けいかく）を縮小（しゅくしょう）（　　）。", ["せざるを得（え）ない", "せずにはいられない", "してならない", "てしかたがない"], 1, "Bất đắc dĩ buộc phải thu hẹp kế hoạch -> せざるを得ない."),
            ("あんなに頑張（がんば）っていた彼（かれ）が落（お）ちたとは、残念（ざんねん）（　　）。", ["でならない", "にしかたがない", "ざるを得（え）ない", "ずにはいられない"], 1, "Cảm xúc tiếc nuối tự nhiên trào dâng sau Na -> でならない."),
            ("夏休（なつやす）みの旅行（りょこう）が楽（たの）しみ（　　）。", ["でたまらない", "ざるを得（え）ない", "ないわけにはいかない", "てならない"], 1, "Háo hức vui sướng không chịu nổi -> でたまらない."),
            ("友だちの結婚（けっこん）式（しき）に招待（しょうたい）されたので、出席（しゅっせき）し（　　）。", ["ないわけにはいかない", "てならない", "てたまらない", "ざるを得ない"], 1, "Không thể không tham dự vì phép lịch sự/tình cảm -> ないわけにはいかない."),
        ]
    },
    26: {
        "title_jp": "願う・感動する",
        "title_vi": "Ước Nguyện, Hồi Tưởng & Cảm Động",
        "section": "IV. 気持ちを表現する",
        "intro": "Bài 26 — bài cuối cùng của Phần 1 trong **Shinkanzen Master Ngữ pháp N2** — tổng hợp 6 mẫu biểu cảm sâu lắng về **ước mong thiết tha, hồi tưởng ký ức và sự cảm động sâu sắc** (`〜たいものだ・〜てほしいものだ`, `〜ものだ`, `〜ないもの（だろう）か`, `〜ものがある`, `〜ことだ`, `〜ことだろう・〜ことか`).",
        "patterns": [
            {
                "name": "1. 〜たいものだ / 〜てほしいものだ",
                "meaning": "Thực lòng mong muốn / Rất hy vọng rằng... (ước nguyện chung hoặc kỳ vọng dài lâu).",
                "connection": "V-ます + たいものだ / V-て + ほしいものだ",
                "examples": [
                    ("いつか世界中（せかいじゅう）をゆっくり旅（たび）してみたい**ものだ**。", "Ước gì một ngày nào đó tôi được thong dong du lịch vòng quanh thế giới."),
                    ("若（わか）い人（ひと）たちには、もっと本（ほん）を読（よ）んでほしい**ものだ**。", "Thật lòng mong các bạn trẻ hãy đọc sách nhiều hơn nữa."),
                ],
                "note": "Thể hiện ước vọng chân thành nhưng không quá gấp gáp tức thì (`ぜひ〜たいものだ`)."
            },
            {
                "name": "2. 〜ものだ（回想・感嘆）",
                "meaning": "1) `V-た + ものだ`: Ngày xưa thường hay... (hồi tưởng đầy hoài niệm); 2) `A・V + ものだ`: Thật là... biết bao (cảm thán sâu sắc).",
                "connection": "V-た / V-る / Aい / Na-な + ものだ",
                "examples": [
                    ("子（こ）どもの頃（ころ）は、よくこの川（かわ）で泳（およ）いだ**ものだ**。", "Hồi nhỏ tôi thường hay bơi ở con sông này lắm đấy."),
                    ("月日（つきひ）が経（た）つのは、本当（ほんとう）に早（はや）い**ものだ**。", "Thời gian trôi đi thật sự nhanh biết bao!"),
                ],
                "note": "Hồi tưởng quá khứ chỉ dùng cho **thói quen lặp đi lặp lại trong quá khứ** (KHÔNG dùng cho việc xảy ra đúng 1 lần như ✗ `昨日東京へ行ったものだ`)."
            },
            {
                "name": "3. 〜ないもの（だろう）か",
                "meaning": "Liệu có cách nào... được không nhỉ? (Mong mỏi tha thiết một điều khó thực hiện, không biết làm sao).",
                "connection": "V-ない（thường là dạng khả năng phủ định: できない・ならない）+ もの（だろう）か",
                "examples": [
                    ("この渋滞（じゅうたい）をなんとか解消（かいしょう）でき**ないものだろうか**。", "Liệu có cách nào giải quyết được tình trạng kẹt xe này không nhỉ?"),
                    ("もっと安（やす）くて質（しつ）のいい製品（せいひん）は作（つく）れ**ないものか**。", "Không biết có thể tạo ra sản phẩm rẻ mà chất lượng tốt hơn không nhỉ."),
                ],
                "note": "Hay đi kèm với từ `なんとか`, `どうにか` (bằng cách nào đó)."
            },
            {
                "name": "4. 〜ものがある",
                "meaning": "Cảm thấy có điều gì đó thật... (một cảm nhận sâu sắc trào dâng trong lòng khi chứng kiến việc gì).",
                "connection": "V-る / Aい / Na-な + ものがある",
                "examples": [
                    ("彼（かれ）の演奏（えんそう）には、聴（き）く人（ひと）の心（こころ）を打（う）つ**ものがある**。", "Tiếng đàn của anh ấy thực sự có sức lay động lòng người nghe."),
                    ("この古い街並（まちな）みには、言葉（ことば）にできない美（うつく）しい**ものがある**。", "Khu phố cổ này có nét đẹp sâu lắng khó diễn tả thành lời."),
                ],
                "note": "Thường đi với các từ diễn tả cảm nhận tinh thần (`心惹かれる`, `感心させられる`, `胸に迫る`, `信じがたい`)."
            },
            {
                "name": "5. 〜ことだ（感嘆）",
                "meaning": "Thật là... làm sao! / Biết bao! (Thán phục, ngạc nhiên hoặc mỉa mai về một việc cụ thể).",
                "connection": "Aい / Na-な + ことだ（ことか）",
                "examples": [
                    ("一人（ひとり）旅（たび）はなんと自由（じゆう）で楽（たの）しい**ことだ**。", "Du lịch một mình thật tự do và vui biết bao!"),
                ],
                "note": "Phân biệt với Bài 24 (`V-る + ことだ` = lời khuyên nên làm)."
            },
            {
                "name": "6. 〜ことだろう / 〜ことか",
                "meaning": "Biết bao nhiêu / Nhường nào! (Nhấn mạnh mức độ cảm xúc quá lớn không sao đong đếm được).",
                "connection": "Thể thông thường（Na-な・である / N-である）+ ことだろう / ことか",
                "examples": [
                    ("無事（ぶじ）に合格（ごうかく）したと知（し）ったら、両親（りょうしん）は**どれほど**喜（よろこ）ぶ**ことだろう**。", "Nếu biết tin đỗ bình an, bố mẹ sẽ vui mừng biết nhường nào!"),
                    ("この日（ひ）を迎（むか）えるために、彼女（かのじょ）は**どんなに**努力（どりょく）した**ことか**。", "Để đón được ngày hôm nay, cô ấy đã nỗ lực biết bao nhiêu mà kể!"),
                ],
                "note": "HẦU NHƯ LUÔN đi kèm từ nghi vấn nhấn mạnh mức độ ở trước (`どんなに`, `どれほど`, `どれくらい`, `何度`)."
            },
        ],
        "comparison": [
            ("V-た + ものだ", "Hồi tưởng thói quen xưa (`よく遊んだものだ`).", "Chỉ dùng cho việc lặp lại thời gian dài."),
            ("〜ないものだろうか", "Ước gì có cách nào đó... (`何とかできないものか`).", "Thường đi với V khả năng phủ định + `なんとか`."),
            ("〜ものがある", "Cảm nhận sâu sắc trong tâm khảm (`心を打つものがある`).", "Diễn tả ấn tượng/sức hút tinh thần."),
            ("〜ことだろう / ことか", "Biết bao nhiêu (đi với `どんなに`, `どれほど`).", "Cảm thán mức độ cực lớn."),
        ],
        "pitfalls": [
            "⚠️ Hồi tưởng `V-たものだ` KHÔNG dùng cho hành động chỉ xảy ra một lần (✗ `去年初めて日本へ来たものだ`).",
            "⚠️ Câu hỏi chứa `どんなに〜` hoặc `どれほど〜` ở vế trước gần như chắc chắn chốt đuôi bằng `〜ことだろう` hoặc `〜ことか`!"
        ],
        "quiz": [
            ("学生（がくせい）の頃（ころ）は、夜（よる）遅（おそ）くまで友達（ともだち）と語（かた）り合（あ）った（　　）。", ["ものだ", "ことだ", "ものがある", "ことだろう"], 1, "Hồi tưởng kỷ niệm lặp lại thời sinh viên -> V-た + ものだ."),
            ("異国（いこく）での生活（せいかつ）が（　　）不安（ふあん）だったことか。", ["どれほど", "なんとか", "まさか", "ぜひ"], 1, "Từ hô ứng đi kèm đuôi câu cảm thán ~ことか -> どれほど."),
            ("ゴミ問題（もんだい）をどうにか解決（かいけつ）でき（　　）と常（つね）に考（かんが）えている。", ["ないものだろうか", "たいものだ", "ものがある", "ことだろう"], 1, "Mong mỏi tìm cách giải quyết (kèm どうにか) -> ないものだろうか."),
            ("彼女（かのじょ）の直筆（じきひつ）の手紙（てがみ）には、胸（むね）に迫（せま）る（　　）。", ["ものがある", "ことか", "ものか", "ことはない"], 1, "Cảm nhận sâu sắc lay động lòng người -> ものがある."),
            ("災害（さいがい）で家（いえ）を失（うしな）った人（ひと）たちが、一日（いちにち）も早（はや）く安心（あんしん）して暮（く）らせるようになってほしい（　　）。", ["ものだ", "ことか", "ものがある", "ことだ"], 1, "Mong mỏi chân thành -> てほしいものだ."),
        ]
    },
}

# Fix Quiz 1 of Lesson 24 so it has clean, unambiguous options!
BUNPOU_PART1_B[24]["quiz"] = [
    ("このチャンスを逃（のが）すな！みんなで成功（せいこう）を掴（つか）み取（と）ろ（　　）。", ["うではないか", "うか〜まいか", "ことだ", "ものか"], 1, "Lời kêu gọi trang trọng cùng phấn đấu -> 〜ようではないか."),
    ("日本（にほん）で働（はたら）きたいなら、まず敬語（けいご）をしっかり身（み）につける（　　）。", ["ことだ", "ことはない", "まい", "ものか"], 1, "Lời khuyên thực tiễn trực tiếp để đạt mục tiêu -> V-る + ことだ."),
    ("授業（じゅぎょう）中（ちゅう）におしゃべりをする（　　）と先生（せんせい）に注意（ちゅうい）された。", ["ものではない", "ことはない", "ようではないか", "まい"], 1, "Răn đe theo chuẩn mực đạo lý/nội quy chung -> ものではない."),
    ("試験（しけん）は来月（らいげつ）なのだから、今（いま）からそんなに焦（あせ）る（　　）。", ["ことはない", "ことだ", "ものではない", "まい"], 1, "Trấn an không cần thiết phải vội -> V-る + ことはない."),
    ("明日（あした）のテストが気（き）になって、今夜（こんや）は寝（ね）られそうにない。もうゲームなどする（　　）。", ["まい", "ことはない", "ものか", "ことだ"], 1, "Ý chí tự nhủ bản thân quyết không làm -> V-る + まい."),
]
