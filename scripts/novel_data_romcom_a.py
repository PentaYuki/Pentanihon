# -*- coding: utf-8 -*-
"""
Tiểu thuyết 1 — ROMCOM (Hài Lãng Mạn): Phần A (Chương 01 - 07)
『桜坂シェアハウスの恋は計算外！』— Tình Yêu Ngoài Dự Tính Ở Nhà Trọ Chung Sakurazaka
"""

ROMCOM_META = {
    "id": "romcom",
    "slug": "romcom",
    "genre_badge": "💕 ROMCOM • HÀI LÃNG MẠN",
    "theme_color": "#c92a5a",
    "theme_soft": "#fff0f5",
    "title_jp": "桜坂（さくらざか）シェアハウスの恋（こい）は計算外（けいさんがい）！",
    "title_vi": "Tình Yêu Ngoài Dự Tính Ở Nhà Trọ Chung Sakurazaka",
    "tagline": "Thanh mai trúc mã tsundere, những bữa cơm ấm áp, chuyến du lịch suối nước nóng dở khóc dở cười và 314 từ vựng Shinkanzen N2 ngọt lịm!",
    "yuki_intro": "Chào em yêu~ Chào mừng em đến với bộ Romcom mở màn đầy tiếng cười và rung động nhẹ nhàng ở ngôi nhà trọ chung Sakurazaka! Em cứ vừa đọc truyện như xem anime tình cảm hài, vừa bấm vào các từ phát sáng để thuộc lòng tự nhiên trọn 13 bài Shinkanzen trong bộ này nha. Đọc chậm thôi cũng được, chị Yuki luôn ngồi bên cạnh cổ vũ em nè 🌸",
    "characters": [
        {"name": "陽翔（はると / Haruto）", "role": "Nam chính (21 tuổi)", "desc": "Sinh viên năm ba chuyển lên Tokyo ở trọ, hơi hậu đậu nhưng ấm áp và biết giữ lời hứa."},
        {"name": "美咲（みさき / Misaki）", "role": "Nữ chính Tsundere (21 tuổi)", "desc": "Bạn thanh mai trúc mã cùng tuổi, nấu ăn siêu ngon, ngoài miệng hay cằn nhằn nhưng bên trong cực kỳ quan tâm."},
        {"name": "蓮（れん / Ren）", "role": "Bạn thân cùng nhà trọ (23 tuổi)", "desc": "Tiền bối vui tính, cây hài của cả nhà, luôn bày trò ghép đôi hai đứa."},
        {"name": "ひなた（Hinata）", "role": "Cô em khóa dưới (19 tuổi)", "desc": "Năng động, thích viết báo tường và mê đồ ngọt."},
    ],
}

ROMCOM_CHAPTERS_A = [
    {
        "num": 1,
        "slug": "chuong-01",
        "lesson_id": "p1_c01_b01",
        "title_jp": "第1章：桜坂（さくらざか）の[[お辞儀（じぎ）|37]]と再会（さいかい）の朝（あさ）",
        "title_vi": "Chương 01: Cúi Chào Ở Dốc Hoa Anh Đào & Buổi Sáng Tái Ngộ",
        "yuki_reminder_top": "Chương mở đầu chứa trọn 41 từ của **Bài 1 (Người thân, bạn bè & kính xưng công sở)** — bài nhiều từ nhất cuốn sách luôn đó! Đừng hoảng nha em, cứ đọc từng đoạn ngắn và chú ý cách gọi người nhà người khác (`奥様・ご主人・ご夫妻`) để không bị nhầm với nhà mình nhé 💕",
        "yuki_reminder_bottom": "Chúc mừng em đã vượt qua 41 từ của chương đầu tiên siêu mượt mà! Uống một ngụm nước mát rồi thử làm 5 câu trắc nghiệm nhỏ bên dưới để khóa chặt kiến thức nha~ 🌸",
        "soft_notes": [
            (2, "Nhắc nhẹ từ chị Yuki 🌸", "Chú ý cặp `実家（じっか）` (nhà bố mẹ đẻ) và bộ ba thế hệ `祖先（そせん）` — `祖父母（そふぼ）` — `孫（まご）` — `子孫（しそん）`. Cả 4 từ đều liên hoàn theo dòng thời gian gia đình nên nhớ một lần là nhớ cả chùm luôn đó em!"),
            (5, "Mẹo nhỏ dễ thương 💕", "Khi nói chuyện với hàng xóm hay sếp người Nhật: vợ người ta gọi là `奥様（おくさま）`, chồng là `ご主人（しゅじん）`, hai vợ chồng là `ご夫妻（ふさい）` nhé! Đừng gọi nhầm sang nhà mình nha~"),
            (8, "Phân biệt chuẩn N2 ✨", "`同（おな）い年（どし）` đọc là **おないどし** (cẩn thận bẫy đọc おなじとし trong đề thi nha em!), còn `言葉遣（ことばづか）い` nhớ biến âm `づ` nhé!"),
        ],
        "paragraphs": [
            (
                "春（はる）の桜（さくら）が舞（ま）う朝（あさ）、大学（だいがく）三年生（さんねんせい）の陽翔（はると）は[[実家（じっか）|11]]の駅（えき）を出発（しゅっぱつ）して、東京（とうきょう）の桜坂（さくらざか）シェアハウスへ引（ひ）っ越（こ）してきた。",
                "Vào một buổi sáng mùa xuân hoa anh đào bay lả tả, chàng sinh viên năm ba Haruto rời nhà ga quê nhà bố mẹ đẻ để chuyển tới nhà trọ chung Sakurazaka ở Tokyo."
            ),
            (
                "見送（みおく）りに来（き）た[[祖父母（そふぼ）|3]]は「いつか可愛い[[孫（まご）|4]]の顔（かお）を見（み）せてね。先祖（せんぞ）というか、[[祖先（そせん）|1]]から[[子孫（しそん）|2]]まで仲良（なかよ）くね」と笑（わら）った。陽翔（はると）は[[三世代（さんせだい）|5]]で暮（く）らした温（あたた）かい[[一家（いっか）|6]]や、近所（きんじょ）の[[親類（しんるい）|7]]・[[親戚（しんせき）|8]]を思（おも）い出（だ）し、「[[親不孝（おやふこう）|10]]ばかりだったけど、今年（ことし）こそバイトも勉強（べんきょう）も頑張（がんば）って[[親孝行（おやこうこう）|9]]しよう」と決意（けつい）した。",
                "Ông bà ra tiễn cậu cười hiền: 'Bao giờ nhớ đưa cháu dâu đáng yêu về thăm nhé, từ đời tổ tiên cho tới con cháu sau này phải luôn hòa thuận đấy'. Haruto nhớ lại gia đình ba thế hệ ấm áp cùng họ hàng thân thích gần xa nơi quê nhà, thầm nhủ: 'Trước giờ mình toàn làm bố mẹ phiền lòng, năm nay nhất định phải cố gắng vừa làm thêm vừa học để báo hiếu mới được'."
            ),
            (
                "陽翔（はると）は兄弟（きょうだい）がいない[[一人（ひとり）っ子（こ）|12]]だが、このシェアハウスには賑（にぎ）やかな仲間（なかま）がいる。[[双子（ふたご）|13]]の兄（あに）たちと違（ちが）って甘（あま）え上手（じょうず）な[[末（すえ）っ子（こ）|14]]のひなた、大学（だいがく）の[[先輩（せんぱい）|28]]である蓮（れん）、そして昔（むかし）からの[[友人（ゆうじん）|15]]で[[仲良（なかよ）し|16]]グループの中心（ちゅうしん）だった美咲（みさき）だ。",
                "Haruto vốn là con một không có anh chị em, nhưng ở nhà trọ chung này lại có những người bạn vô cùng náo nhiệt: cô em út Hinata khéo làm nũng (trái ngược hẳn với hai anh sinh đôi của cô bé), tiền bối đại học Ren, và Misaki — người bạn thân thiết lâu năm từng là trung tâm nhóm bạn chơi thân hồi xưa."
            ),
            (
                "玄関（げんかん）で荷物（にもつ）を下（お）ろすと、エプロン姿（すがた）の美咲（みさき）が「遅（お）いわよ、[[同（おな）い年（どし）|34]]のよしみで部屋（へや）を片付（かたづ）けておいたのに！」と頬（ほほ）を膨（ふく）らませた。隣（となり）ではひなたが「あ、陽翔（はると）さん！　[[年上（としうえ）|32]]のお兄（にい）さんが来（き）て嬉（うれ）しいです！　[[年下（としした）|33]]の私（わたし）と[[後輩（こうはい）|29]]の面倒（めんどう）も見（み）てくださいね」と笑（わら）う。",
                "Vừa đặt hành lý xuống sảnh, Misaki trong bộ tạp dề đã phồng má trách yêu: 'Cậu đến muộn quá đấy, nể tình bằng tuổi nhau tớ đã dọn sẵn phòng cho rồi mà!'. Bên cạnh, Hinata cười tươi: 'A, anh Haruto! Em vui quá vì có anh lớn tuổi hơn chuyển tới, nhớ chăm sóc đứa em nhỏ tuổi hơn kiêm hậu bối là em nhé!'."
            ),
            (
                "そこへオーナーの田中（たなか）[[ご夫妻（ふさい）|24]]が挨拶（あいさつ）に現（あらわ）れた。「[[ご主人（しゅじん）|21]]、陽翔（はると）くんが着（つ）きましたよ」と[[奥様（おくさま）|20]]が優（やさ）しく言（い）い、[[夫人（ふじん）|25]]の隣（となり）で田中（たなか）さんが[[握手（あくしゅ）|38]]を求（もと）めてきた。「よく来（き）たね。うちの可愛い[[お嬢（じょう）ちゃん|22]]みたいな美咲（みさき）と、ちょっと調子（ちょうし）に乗（の）りやすい[[お坊（ぼっ）ちゃん|23]]みたいな蓮（れん）をよろしく頼（たの）むよ」",
                "Đúng lúc ấy, vợ chồng bác Tanaka chủ nhà bước ra chào hỏi. Bác gái dịu dàng nói với bác trai: 'Mình ơi, cậu Haruto tới rồi kìa', còn bác Tanaka bên cạnh phu nhân chìa tay ra bắt tay cậu: 'Chào mừng cháu. Nhờ cháu trông chừng cô con gái cưng Misaki và cậu ấm hơi hay cao hứng là thằng Ren hộ bác nhé'."
            ),
            (
                "陽翔（はると）は[[目上（めうえ）|30]]の人（ひと）への礼儀（れいぎ）として深（ふか）く[[お辞儀（じぎ）|37]]をし、丁寧（ていねい）な[[言葉遣（ことばづか）い|36]]と誠実（せいじつ）な[[態度（たいど）|41]]で答（こた）えた。「はい、[[目下（めした）|31]]の私（わたし）ですが、近所（きんじょ）[[付（つ）き合（あ）い|35]]も大切（たいせつ）にして頑張（がんば）ります！」",
                "Để giữ lễ phép với người bề trên, Haruto cúi đầu chào thật sâu, đáp lại bằng lời ăn tiếng nói lịch sự và thái độ chân thành: 'Dạ vâng, tuy cháu là người bề dưới nhưng cháu sẽ trân trọng cả quan hệ hàng xóm xung quanh và cố gắng hết mình ạ!'."
            ),
            (
                "「おっ、さすが新入（しんにゅう）バイト先（さき）でも好（す）かれそうだな！　今度（こんど）、俺（おれ）の[[知人（ちじん）|18]]や近所（きんじょ）の[[知（し）り合（あ）い|19]]も紹介（しょうかい）するよ。カフェの[[仕事（しごと）仲間（なかま）|17]]もみんな気（き）さくだし、[[上司（じょうし）|26]]の佐藤（さとう）店長（てんちょう）も[[部下（ぶか）|27]]想（おも）いで優（やさ）しいんだ」と蓮（れん）が肩（かた）を叩（たた）いた。",
                "'Ồ, đúng chuẩn chàng trai đi làm thêm đâu cũng được quý! Hôm nào anh giới thiệu thêm người quen của anh và bà con hàng xóm quen biết cho. Đồng nghiệp ở quán cà phê toàn người xởi lởi, sếp trưởng tiệm Sato cũng cực kỳ thương cấp dưới nữa đấy' — Ren vỗ vai cậu."
            ),
            (
                "「ねえ陽翔（はると）、引っ越し祝（いわ）いに今夜（こんや）はカレー作（つく）るから、七時（しちじ）までに帰（かえ）ってくるっていう[[約束（やくそく）を守（まも）る|39]]こと！　もし[[約束（やくそく）を破（やぶ）る|40]]ようなことがあったら、お前（まえ）の分（ぶん）は辛口（からくち）十倍（じゅうばい）にするからね！」――美咲（みさき）の照（て）れ隠（かく）しの笑顔（えがお）に、陽翔（はると）の胸（むね）がふわりと温（あたた）かくなった。",
                "'Này Haruto, tối nay tớ nấu cà ri mừng cậu chuyển nhà nên phải giữ đúng lời hứa về trước 7 giờ đấy! Nếu mà thất hứa thì phần của cậu tớ cho cay gấp 10 lần luôn cho biết mặt!' — Trước nụ cười che giấu sự ngượng ngùng của Misaki, lồng ngực Haruto bỗng thấy ấm áp lạ thường."
            ),
        ],
        "quiz": [
            {
                "prompt": "田中（たなか）さんの奥（おく）さんのことを、近所（きんじょ）の人（ひと）が丁寧（ていねい）に呼（よ）ぶとき、どの言葉（ことば）を使（つか）うか。",
                "options": ["奥様（おくさま）", "ご主人（しゅじん）", "実家（じっか）", "末（すえ）っ子（こ）"],
                "ans": 1,
                "right_exp": "💖 Chính xác luôn bé ơi! `奥様（おくさま）` là cách gọi kính trọng vợ của người khác (tương ứng `ご主人` là chồng người khác).",
                "wrong_exps": [
                    "Chính xác: `奥様（おくさま）` là kính xưng dành cho vợ người khác.",
                    "Úi, `ご主人（ごしゅじん）` là cách gọi **chồng** của người khác nha em, không phải vợ nhé! 🌸",
                    "Nhầm xíu rồi nè~ `実家（じっか）` nghĩa là **nhà bố mẹ đẻ** chứ không phải danh xưng vợ người khác.",
                    "Chưa đúng rùi~ `末（すえ）っ子（こ）` nghĩa là **con út trong gia đình** thôi nha em."
                ]
            },
            {
                "prompt": "本文（ほんぶん）で、陽翔（はると）と美咲（みさき）は「同（おな）い年（どし）」と書（か）かれている。「同い年」の正（ただ）しい読（よ）み方（かた）はどれか。",
                "options": ["おなじとし", "おないどし", "どうねん", "どうし"],
                "ans": 2,
                "right_exp": "💖 Tuyệt vời! `同（おな）い年（どし）` là từ cực hay gài bẫy ở Mondai 1, đọc chuẩn là **おないどし** (biến âm ở `どし`).",
                "wrong_exps": [
                    "Cẩn thận bẫy kinh điển nha em! Nhìn chữ 同 và 年 rất dễ đọc nhầm thành `おなじとし`, nhưng cách đọc chuẩn tiếng Nhật của `同い年` là **おないどし** đấy 🌸",
                    "Chính xác: `同（おな）い年（どし）` đọc là **おないどし**.",
                    "Hơi sai âm rồi nè~ Nếu là Hán-Nhật `同年` mới đọc `どうねん`, còn có chữ い ở giữa (`同い年`) phải đọc thuần Nhật là **おないどし**.",
                    "`どうし` là cách đọc của `同士` (những người cùng nhóm), không phải `同い年` nha em."
                ]
            },
            {
                "prompt": "目上（めうえ）の人（ひと）に対（たい）して話（はな）すとき、丁寧（ていねい）な（　　）に気（き）をつけるべきだ。",
                "options": ["親不孝（おやふこう）", "お坊（ぼっ）ちゃん", "言葉遣（ことばづか）い", "双子（ふたご）"],
                "ans": 3,
                "right_exp": "💖 Chuẩn không cần chỉnh! `言葉遣（ことばづか）い` là cách dùng từ ngữ, lời ăn tiếng nói (nhớ viết hiragana là `づかい`).",
                "wrong_exps": [
                    "`親不孝（おやふこう）` là **bất hiếu với cha mẹ**, không ghép với `丁寧な〜` khi nói chuyện với người bề trên được nha.",
                    "`お坊（ぼっ）ちゃん` là **cậu ấm / con trai nhà người ta**, không hợp nghĩa rồi nè.",
                    "Chính xác: `丁寧な言葉遣い` = cách dùng ngôn từ lịch sự.",
                    "`双子（ふたご）` nghĩa là **sinh đôi**, không đúng ngữ cảnh câu này nhé em."
                ]
            },
            {
                "prompt": "「時間（じかん）の約束（やくそく）を（　　）」と、友達（ともだち）の信用（しんよう）を失（うしな）ってしまう。",
                "options": ["守（まも）る", "破（やぶ）る", "お辞儀（じぎ）する", "握手（あくしゅ）する"],
                "ans": 2,
                "right_exp": "💖 Quá giỏi! Vế sau nói \"sẽ đánh mất lòng tin của bạn bè\" nên vế trước phải là **thất hứa / phá vỡ hẹn**: `約束を破る`.",
                "wrong_exps": [
                    "Đọc kỹ vế sau một chút nhé em: `信用を失う` là **đánh mất lòng tin**! Nếu giữ lời hứa (`約束を守る`) thì phải tạo được uy tín chứ không mất lòng tin đâu nha 🌸",
                    "Chính xác: `約束を破る` (phá vỡ lời hẹn) dẫn đến mất lòng tin.",
                    "`お辞儀する` là cúi đầu chào, không đi với trợ từ を sau `約束`.",
                    "`握手する` là bắt tay, không mang nghĩa thất hứa."
                ]
            },
            {
                "prompt": "美咲（みさき）はなぜ「約束（やくそく）を破（やぶ）ったら辛口（からくち）十倍（じゅうばい）にする」と言（い）ったのか。",
                "options": [
                    "陽翔（はると）が激辛（げきから）料理（りょうり）の大好物（だいこうぶつ）だから",
                    "照（て）れながら、陽翔（はると）と一緒（いっしょ）に晩（ばん）ご飯（はん）を食（た）べたいから",
                    "シェアハウスの掃除（そうじ）をサボった罰（ばつ）だから",
                    "陽翔（はると）を追い出（おいだ）したいから"
                ],
                "ans": 2,
                "right_exp": "💖 Đúng tâm lý Romcom rồi nè! Misaki vốn tsundere nên ngoài miệng dọa cho cay gấp 10, thực chất là muốn chắc chắn Haruto về ăn tối cùng mình đó~",
                "wrong_exps": [
                    "Không phải vì Haruto thích ăn cay đâu, đó chỉ là lời dọa kiểu tsundere thôi nè 💕",
                    "Chính xác: Misaki vừa ngượng vừa mong Haruto giữ hẹn về ăn tối chung.",
                    "Đoạn truyện không hề nhắc tới việc cậu trốn quét dọn nhé.",
                    "Ngược lại hoàn toàn luôn: Misaki còn dọn sẵn phòng và nấu cà ri chào mừng Haruto đó!"
                ]
            },
        ]
    },
    {
        "num": 2,
        "slug": "chuong-02",
        "lesson_id": "p1_c01_b02",
        "title_jp": "第2章：[[几帳面（きちょうめん）|6]]な彼女（かのじょ）と[[そそっかしい|9]]僕（ぼく）の[[性格（せいかく）|1]]",
        "title_vi": "Chương 02: Cô Nàng Tỉ Mỉ & Chàng Trai Hấp Tấp",
        "yuki_reminder_top": "Chương 2 gói trọn 30 từ **Bài 2 (Tính cách & Đặc điểm con người)**! Toàn những cặp tính từ trái nghĩa cực thú vị để miêu tả cặp đôi oan gia nhà Sakurazaka luôn. Chú ý đuôi `〜っぽい` (`怒りっぽい`, `飽きっぽい`) nữa nha em ✨",
        "yuki_reminder_bottom": "Hiểu tính cách đối phương rồi thấy hai bạn dễ thương ghê chưa~ Nhớ đừng nhầm `器用` (khéo léo) với `謙虚` (khiêm tốn) khi làm quiz bên dưới nhé! 🎀",
        "soft_notes": [
            (2, "Cặp trái nghĩa đắt giá 💡", "`几帳面（きちょうめん）` (ngăn nắp tỉ mỉ) ⇄ `だらしない` (luộm thuộm bừa bãi), `積極的（せっきょくてき）` (chủ động) ⇄ `消極的（しょうきょくてき）` (thụ động rụt rè). Nhớ theo cặp đối nghịch cực nhanh thuộc!"),
            (5, "Nhắc nhỏ về đuôi 〜っぽい 🌸", "Thấy `V-ます + っぽい` là biết ngay nghĩa \"dễ/hay...\": `怒（おこ）りっぽい` (hay nổi cáu), `飽（あ）きっぽい` (cả thèm chóng chán). Quá dễ nhớ đúng không nào~"),
        ],
        "paragraphs": [
            (
                "シェアハウス生活（せいかつ）が始（はじ）まって三日（みっか）。陽翔（はると）は住人（じゅうにん）たちの[[性格（せいかく）|1]]の違い（ちがい）に驚（おどろ）くばかりだった。",
                "Ba ngày trôi qua kể từ khi cuộc sống nhà trọ chung bắt đầu, Haruto chỉ biết ngạc nhiên trước sự khác biệt tính cách của từng thành viên."
            ),
            (
                "美咲（みさき）はノートも調味料（ちょうみりょう）も定規（じょうぎ）で測（はか）ったように並（なら）べる[[几帳面（きちょうめん）|6]]なタイプで、いつも[[慎重（しんちょう）|8]]に計画（けいかく）を立（た）てる。手先（てさき）も[[器用（きよう）|10]]で、折り紙（おりがみ）や裁縫（さいほう）まで完璧（かんぺき）だ。一方（いっぽう）、陽翔（はると）は[[そそっかしい|9]]上に[[不器用（ぶきよう）|11]]で、靴下（くつした）を片方（かたほう）だけ履（は）いて玄関（げんかん）に出（で）るほど[[だらしない|7]]ところがあった。",
                "Misaki là tuýp người ngăn nắp tỉ mỉ đến mức xếp cả vở lẫn lọ gia vị thẳng như đo bằng thước, lúc nào cũng cân nhắc thận trọng. Đôi tay cô ấy còn khéo léo, gấp giấy hay khâu vá đều hoàn hảo. Ngược lại, Haruto vừa hấp tấp lại vừa vụng về, có lúc luộm thuộm đến mức đi mỗi một chiếc tất đã bước ra cửa."
            ),
            (
                "「ちょっと陽翔（はると）！　また鍵（かぎ）を忘（わす）れたの？　[[わがまま|20]]で[[図々（ずうずう）しい|21]]蓮（れん）先輩（せんぱい）とは違（ちが）って、陽翔（はると）は[[素直（すなお）|14]]なのが[[長所（ちょうしょ）|2]]なんだから、[[短所（たんしょ）|3]]も直（なお）しなさいよ」",
                "'Này Haruto! Lại quên chìa khóa nữa hả? Không giống anh Ren vừa ích kỷ vừa mặt dày, ưu điểm của cậu là thật thà biết lắng nghe, nên hãy sửa luôn cả khuyết điểm đi nhé!'"
            ),
            (
                "そう言（い）われてリビングを見（み）ると、蓮（れん）がソファーでポテチを食（た）べながら「おいおい、[[厚（あつ）かましい|22]]なあ。俺（おれ）は[[気（き）さくな|16]]人気者（にんきもの）で、いつも[[陽気（ようき）|18]]にみんなを笑（わら）わせてるだろ？」と笑（わら）った。確かに蓮（れん）は[[要領（ようりょう）がいい|29]]し、後輩（こうはい）が困（こま）ったときは[[頼（たの）もしい|17]]先輩（せんぱい）になる。",
                "Nghe vậy quay sang nhìn phòng khách, thấy Ren đang ngồi trên sofa nhai snack cười khà khà: 'Ấy dà, nói anh mặt dày là oan quá nha. Anh là người cởi mở dễ gần, lúc nào cũng vui vẻ hoạt bát khuấy động cả nhà còn gì?'. Quả thực Ren biết xoay xở nhanh nhạy hiệu quả, và khi đàn em gặp khó khăn anh cũng là tiền bối rất đáng tin cậy."
            ),
            (
                "そこへ[[派手（はで）|27]]なピンクのニットを着（き）たひなたが帰（かえ）ってきた。「美咲（みさき）先輩（せんぱい）は[[地味（じみ）|28]]な色の服（ふく）が多（おお）いですけど、とても[[穏（おだ）やか|15]]で優（やさ）しいから大好きです！　でも、陽翔（はると）さんには少（すこ）し[[怒（おこ）りっぽい|25]]ですよね？」",
                "Đúng lúc đó Hinata mặc chiếc áo len hồng rực rỡ đi về: 'Chị Misaki hay mặc đồ màu sắc giản dị trầm lắng, nhưng chị ôn hòa dịu dàng nên em thích nhất luôn! Cơ mà với anh Haruto thì chị có vẻ hơi dễ nổi nóng nhỉ?'."
            ),
            (
                "「べ、別（べつ）に！　陽翔（はると）が[[飽（あ）きっぽい|26]]せいで、部屋（へや）の整理（せいり）も三日（みっか）坊主（ぼうず）だから注意（ちゅうい）してるだけよ！」と美咲（みさき）が赤（あか）くなる。ひなたは[[勘（かん）が鋭（するど）い|30]]ので、「ふふっ、先輩（せんぱい）ったら本当（ほんとう）は陽翔（はると）さんのことが…」とにやにやした。",
                "'Đ-đâu có! Tại Haruto cả thèm chóng chán, dọn phòng được ba bữa lại bỏ nên tớ mới nhắc nhở thôi!' — Misaki đỏ bừng mặt. Hinata vốn trực giác sắc bén nhìn thấu ngay, cười tủm tỉm: 'Hì hì, chị ơi thực ra chị thích anh Haruto...'."
            ),
            (
                "「こら、[[生意気（なまいき）|13]]な口（くち）をきくな！」と美咲（みさき）が[[強引（ごういん）|23]]に話題（わだい）を変（か）えようとする。「陽翔（はると）、[[消極的（しょうきょくてき）|5]]に黙（だま）ってないで、もっと[[積極的（せっきょくてき）|4]]に家事（かじ）に参加（さんか）してよ。しかも最近（さいきん）、自分のコーヒー代（だい）には[[けち|24]]なくせに、美咲（みさき）へのプリンだけ[[頑固（がんこ）|19]]に高級（こうきゅう）なのを買（か）ってくるって本当（ほんとう）？」と蓮（れん）が追（お）い討（う）ちをかけた。",
                "'Này, đừng có nói năng xấc xược thế!' — Misaki định ép chuyển chủ đề ngay. Ren còn bồi thêm: 'Haruto, đừng có thụ động im lặng thế, chủ động tham gia việc nhà hơn đi chứ. Mà nghe đồn dạo này với tiền cà phê của bản thân thì keo kiệt từng xu, thế mà mua bánh pudding cho Misaki lại khăng khăng cứng đầu chọn loại cao cấp nhất hả?'."
            ),
            (
                "「そ、それは…美咲（みさき）がいつも[[謙虚（けんきょ）|12]]で自分（じぶん）の分（ぶん）を遠慮（えんりょ）するから…」と陽翔（はると）が小声（こごえ）で答（こた）えると、ダイニングが甘（あま）い沈黙（ちんもく）に包（つつ）まれた。",
                "'Đ-đó là tại... Misaki lúc nào cũng khiêm tốn nhường nhịn chẳng chịu mua phần cho mình nên...' — Haruto khẽ đáp nhỏ, khiến cả gian bếp bỗng chìm vào một khoảng lặng ngọt ngào."
            ),
        ],
        "quiz": [
            {
                "prompt": "美咲（みさき）はノートも調味料（ちょうみりょう）もきれいに並（なら）べる（　　）な性格（せいかく）だ。",
                "options": ["几帳面（きちょうめん）", "だらしない", "そそっかしい", "飽（あ）きっぽい"],
                "ans": 1,
                "right_exp": "💖 Chuẩn rồi! `几帳面（きちょうめん）` nghĩa là ngăn nắp, chỉn chu, tỉ mỉ từng li từng tí.",
                "wrong_exps": [
                    "Chính xác: `几帳面（きちょうめん）` mô tả tính cách gọn gàng, ngăn nắp.",
                    "`だらしない` nghĩa là luộm thuộm, bừa bãi — trái nghĩa hoàn toàn với việc sắp xếp gọn gàng nhé em 🌸",
                    "`そそっかしい` là tính hấp tấp bộp chộp hay quên trước quên sau.",
                    "`飽きっぽい` là cả thèm chóng chán, không liên quan đến việc sắp xếp ngăn nắp."
                ]
            },
            {
                "prompt": "少（すこ）しのヒントで人（ひと）の本音（ほんね）をすぐ見抜（みぬ）くひなたは、（　　）。",
                "options": ["勘（かん）が鋭（するど）い", "要領（ようりょう）が悪い", "不器用（ぶきよう）だ", "地味（じみ）だ"],
                "ans": 1,
                "right_exp": "💖 Xuất sắc! `勘（かん）が鋭（するど）い` nghĩa là trực giác nhạy bén, nhìn thấu suy nghĩ người khác rất nhanh.",
                "wrong_exps": [
                    "Chính xác: `勘が鋭い` = trực giác sắc bén.",
                    "`要領が悪い` là làm việc không biết cách nắm trọng tâm, lề mề kém hiệu quả — ngược ý rồi nha.",
                    "`不器用だ` là vụng về tay chân hoặc giao tiếp, không phải nhạy bén.",
                    "`地味だ` là giản dị, mờ nhạt."
                ]
            },
            {
                "prompt": "「何事（なにごと）も三日（みっか）でやめてしまう」という性格（せいかく）を表（あらわ）す言葉（ことば）はどれか。",
                "options": ["怒（おこ）りっぽい", "飽（あ）きっぽい", "図々（ずうずう）しい", "頑固（がんこ）"],
                "ans": 2,
                "right_exp": "💖 Đúng rồi em! Làm gì cũng được ba bữa rồi bỏ (ba ngày rưỡi) chính là `飽きっぽい` (cả thèm chóng chán).",
                "wrong_exps": [
                    "`怒りっぽい` nghĩa là **dễ nổi cáu**, không phải mau chán nhé.",
                    "Chính xác: `飽（あ）きっぽい` = mau chán, không bền.",
                    "`図々しい` là trơ tráo, mặt dày.",
                    "`頑固` là cứng đầu bảo thủ."
                ]
            },
            {
                "prompt": "「積極的（せっきょくてき）」の反対（はんたい）の意味（いみ）の言葉（ことば）はどれか。",
                "options": ["消極的（しょうきょくてき）", "素直（すなお）", "謙虚（けんきょ）", "慎重（しんちょう）"],
                "ans": 1,
                "right_exp": "💖 Quá chuẩn! Cặp trái nghĩa kinh điển Shinkanzen: `積極的（せっきょくてき）` (tích cực, chủ động) ⇄ `消極的（しょうきょくてき）` (tiêu cực, thụ động).",
                "wrong_exps": [
                    "Chính xác: `消極的` đối lập trực tiếp với `積極的`.",
                    "`素直` là thật thà ngoan ngoãn, không phải trái nghĩa của chủ động.",
                    "`謙虚` là khiêm tốn, không đối lập với `積極的`.",
                    "`慎重` là thận trọng cân nhắc kỹ."
                ]
            },
            {
                "prompt": "なぜ陽翔（はると）は自分のコーヒー代（だい）を節約（せつやく）しても、美咲（みさき）には高級（こうきゅう）なプリンを買（か）ったのか。",
                "options": [
                    "お坊（ぼっ）ちゃんでお金（かね）が余（あま）っていたから",
                    "美咲（みさき）がいつも謙虚（けんきょ）で自分（じぶん）の分（ぶん）を遠慮（えんりょ）するのを気遣（きづか）ったから",
                    "美咲（みさき）に強引（ごういん）に頼（たの）まれたから",
                    "賞味期限（しょうみきげん）が切（き）れそうだったから"
                ],
                "ans": 2,
                "right_exp": "💖 Ngọt xỉu luôn! Đoạn cuối nói rõ Haruto để ý thấy Misaki hay khiêm tốn nhường phần cho mọi người nên cậu âm thầm mua loại ngon cho riêng cô ấy.",
                "wrong_exps": [
                    "Chàng ta còn tiết kiệm cả tiền cà phê của mình nữa mà, đâu có dư dả đâu nè!",
                    "Chính xác: Vì thương Misaki luôn nhún nhường phần mình.",
                    "Misaki không hề đòi mua nhé, Haruto tự nguyện mua cho cô ấy đấy.",
                    "Trong bài không hề nhắc tới hạn sử dụng của bánh pudding nha."
                ]
            },
        ]
    },
    {
        "num": 3,
        "slug": "chuong-03",
        "lesson_id": "p1_c02_b01",
        "title_jp": "第3章：焦（こ）げたオムライスと[[香（こう）ばしい|23]]恋（こい）の[[味付け（あじつけ）|19]]",
        "title_vi": "Chương 03: Món Cơm Cuộn Trứng Cháy & Gia Vị Tình Yêu Thơm Lừng",
        "yuki_reminder_top": "Chương 3 đưa em vào căn bếp nhộn nhịp của nhà trọ để học trọn 27 từ **Bài 4 (Ẩm thực & Chế biến món ăn)**! Từ gọt vỏ (`皮をむく`), thái nhỏ (`刻む`), ninh (`煮る`), xào (`炒める`) đến chiên hấp... đọc xong khéo đói bụng mất thôi 😋",
        "yuki_reminder_bottom": "Vượt qua bài nấu ăn rồi nha! Mẹo nhỏ cho em: nhớ phân biệt cặp `お湯を沸かす` (đun sôi nước) và `料理を煮る` (kho/ninh đồ ăn) để không bị đánh lừa ở bài trắc nghiệm nhé 🍳",
        "soft_notes": [
            (2, "Từ bếp núc siêu dễ nhầm 🍳", "`刻（きざ）む` là băm/thái nhỏ rau hành, `皮（かわ）をむく` là gọt vỏ táo khoai, `混（ま）ぜる` là trộn đều, `加（くわ）える` là nêm thêm. Học theo trình tự nấu một món ăn rất dễ nhớ!"),
            (5, "Cặp hương vị hay thi 🍋", "`酸（す）っぱい` (chua như chanh), `渋（しぶ）い` (chát như trà đặc/hồng xanh), `香（こう）ばしい` (thơm nức mùi nướng/rang). Đừng nhầm `香ばしい` với thơm nước hoa nha em!"),
        ],
        "paragraphs": [
            (
                "土曜日（どようび）の昼（ひる）、いつも[[外食（がいしょく）|4]]ばかりだった陽翔（はると）は、[[栄養（えいよう）|2]]と[[食生活（しょくせいかつ）|1]]を整（ととの）えるために[[自炊（じすい）|3]]へ挑戦（ちょうせん）することにした。「今日（きょう）は俺（おれ）が昼（ひる）ご飯（はん）を作（つく）るよ！」",
                "Trưa thứ Bảy, Haruto vốn trước nay toàn đi ăn hàng quyết định thử tự nấu ăn để cải thiện dinh dưỡng và chế độ ăn uống sinh hoạt. 'Hôm nay tớ sẽ nấu bữa trưa cho cả nhà!'"
            ),
            (
                "「へえ、[[献立（こんだて）|7]]は何（なに）？」と美咲（みさき）が覗（のぞ）き込（こ）む。陽翔（はると）は冷蔵庫（れいぞうこ）から[[新鮮（しんせん）|24]]な鶏肉（とりにく）と野菜（やさい）、卵（たまご）などの[[材料（ざいりょう）|5]]を取（と）り出（だ）し、棚（たな）から[[調味料（ちょうみりょう）|6]]を並（なら）べた。「特製（とくせい）オムライスと、唐（から）揚（あ）げと、野菜（やさい）スープだ！」",
                "'Ồ, thực đơn gồm món gì thế?' — Misaki ngó vào xem. Haruto lấy từ tủ lạnh ra các nguyên liệu như thịt gà tươi ngon, rau củ, trứng rồi bày hàng gia vị trên kệ: 'Cơm cuộn trứng đặc biệt, gà rán và súp rau củ!'."
            ),
            (
                "まずはじゃがいもの[[皮（かわ）をむく|9]]ところから始（はじ）めたが、包丁（ほうちょう）が危（あぶ）なっかしい。たまねぎを[[刻（きざ）む|10]]ときには涙（なみだ）が止（と）まらず、ボウルで卵（たまご）を[[混（ま）ぜる|11]]つもりが机（つくえ）にこぼしてしまった。見（み）かねた美咲（みさき）が「貸（か）して！」と隣（となり）に並（なら）ぶ。",
                "Cậu bắt đầu từ việc gọt vỏ khoai tây nhưng cầm dao cứ loạng choạng đến phát sợ. Lúc băm nhỏ hành tây thì nước mắt giàn giụa, định trộn trứng trong bát thì lại làm đổ ra bàn. Misaki đứng nhìn không đành lòng bèn tiến lại đứng sát bên: 'Đưa đây cho tớ!'."
            ),
            (
                "「いい？　スープの鍋（なべ）はお湯（ゆ）を[[沸（わ）かして|17]]準備（じゅんび）してから、野菜（やさい）を弱火（よわび）で[[煮（に）る|13]]の。チキンライスはフライパンで手早（てばや）く[[炒（いた）める|14]]こと！　唐（から）揚（あ）げは高温（こうおん）の油（あぶら）でカリッと[[揚（あ）げる|15]]わよ。ブロッコリーは[[蒸（む）す|16]]と甘（あま）くなるの」",
                "'Nghe rõ nhé: nồi súp thì phải đun sôi nước chuẩn bị trước rồi mới ninh rau củ bằng lửa nhỏ. Cơm gà thì đảo xào nhanh tay trên chảo! Còn gà rán phải chiên ngập dầu nóng cho giòn rụm, bông cải xanh đem hấp lên sẽ ngọt tự nhiên đấy'."
            ),
            (
                "肩（かた）が触（ふ）れ合（あ）う近（ちか）さで料理（りょうり）を教（おし）えてもらい、陽翔（はると）は塩（しお）と醤油（しょうゆ）を[[加（くわ）える|12]]手（て）まで震（ふる）えた。その横（よこ）では、ひなたが「レモンの[[酸（す）っぱい|21]]ドレッシングも作（つく）りました！　お茶（ちゃ）は少し[[渋（しぶ）い|22]]玉露（ぎょくろ）を冷蔵庫（れいぞうこ）で[[冷（ひ）やして|18]]おきましたよ」と準備（じゅんび）万端（ばんたん）だ。",
                "Được Misaki chỉ bảo ở khoảng cách gần tới mức vai chạm vai, tay Haruto cầm muối và nước tương cho thêm vào mà run bần bật. Bên cạnh, Hinata cũng chuẩn bị đâu vào đấy: 'Em làm xong cả nước sốt chanh chua dịu rồi ạ! Trà xanh hơi chát đậm em cũng ướp lạnh trong tủ lạnh rồi nè!'."
            ),
            (
                "「あ！　バターが焦（こ）げて[[香（こう）ばしい|23]]匂（にお）いが…って焦（こ）げすぎた！」――陽翔（はると）のオムライスは少し黒（くろ）くなったが、美咲（みさき）がケチャップで可愛（かわい）くハートを描（か）いて[[味付（あじつ）け|19]]を整（ととの）えてくれた。「ほら、みんなで[[味（あじ）わって|20]]みよう！」",
                "'Á! Bơ cháy tỏa mùi thơm lừng... ôi thôi cháy đen quá rồi!' — Chiếc cơm cuộn trứng của Haruto hơi sém đen một góc, nhưng Misaki đã dùng tương cà vẽ một hình trái tim xinh xắn rồi nêm nếm lại cho vừa vặn: 'Nào, mọi người cùng nếm thưởng thức xem sao nhé!'."
            ),
            (
                "「[[生（なま）|8]]のキャベツのシャキシャキ感（かん）も最高（さいこう）！　これだけ上手（じょうず）なら、残（のこ）ったおかずはタッパーで[[保存（ほぞん）して|25]]おけば明日（あした）も食（た）べられるね」と蓮（れん）が大絶賛（だいぜっさん）。ただし冷蔵庫（れいぞうこ）の奥（おく）から「これ、[[賞味期限（しょうみきげん）|27]]が切（き）れて[[腐（くさ）り|26]]かけてる牛乳（ぎゅうにゅう）誰（だれ）の!?」と美咲（みさき）の雷（かみなり）が落（お）ちたのは、蓮（れん）のせいであった。",
                "'Bắp cải ăn sống giòn sần sật ngon tuyệt! Ngon thế này thì đồ ăn thừa cứ bảo quản vào hộp kín mai ăn tiếp được đấy' — Ren tấm tắc khen. Chỉ có điều từ góc tủ lạnh bỗng vang lên tiếng sấm sét của Misaki: 'Hộp sữa hết hạn dùng ngon nhất mà sắp thiu hỏng này là của ai đây hả?!' — thủ phạm thì chẳng ai khác ngoài ông anh Ren."
            ),
        ],
        "quiz": [
            {
                "prompt": "じゃがいもを切（き）る前（まえ）に、まずピーラーで（　　）。",
                "options": ["皮（かわ）をむく", "湯（ゆ）を沸（わ）かす", "刻（きざ）む", "腐（くさ）る"],
                "ans": 1,
                "right_exp": "💖 Chính xác! Trước khi thái khoai tây phải dùng dao bào để **gọt vỏ** (`皮をむく`).",
                "wrong_exps": [
                    "Chính xác: `皮をむく` = gọt vỏ củ quả.",
                    "`湯を沸かす` là đun sôi nước, không dùng với công cụ gọt vỏ (ピーラー) nhé.",
                    "`刻む` là băm nhỏ sau khi đã gọt vỏ rồi nè.",
                    "`腐る` nghĩa là bị thiu hỏng (tự động từ), không hợp nghĩa."
                ]
            },
            {
                "prompt": "焼（や）きたてのパンから、とても（　　）いい匂（にお）いが漂（ただよ）ってきた。",
                "options": ["香（こう）ばしい", "酸（す）っぱい", "渋（しぶ）い", "生（なま）な"],
                "ans": 1,
                "right_exp": "💖 Chuẩn rồi bé! Mùi thơm lừng đặc trưng của đồ nướng/rang/cà phê/bánh mì là `香ばしい`.",
                "wrong_exps": [
                    "Chính xác: `香（こう）ばしい` = thơm lừng mùi nướng/rang.",
                    "`酸っぱい` là vị chua (chanh, giấm), không diễn tả mùi thơm bánh nướng.",
                    "`渋い` là vị chát (trà, quả hồng xanh).",
                    "`生（なま）` là đồ sống chưa chế biến, không đi với mùi thơm bánh vừa nướng xong."
                ]
            },
            {
                "prompt": "夏場（なつば）は食（た）べ物（もの）が（　　）やすいので、冷蔵庫（れいぞうこ）に保存（ほぞん）しましょう。",
                "options": ["腐（くさ）り", "冷（ひ）やし", "蒸（む）し", "混（ま）ぜ"],
                "ans": 1,
                "right_exp": "💖 Tuyệt vời! Mùa hè đồ ăn rất dễ bị thiu hỏng nên phải cho vào tủ lạnh: `腐りやすい`.",
                "wrong_exps": [
                    "Chính xác: `腐（くさ）る` chia bỏ ます + やすい = `腐りやすい` (dễ thiu hỏng).",
                    "`冷やす` là làm lạnh (tha động từ), không nói đồ ăn dễ tự làm lạnh nhé.",
                    "`蒸す` là hấp đồ ăn.",
                    "`混ぜる` là trộn đều nguyên liệu."
                ]
            },
            {
                "prompt": "フライパンで肉（にく）とたまねぎを強火（つよび）で（　　）。",
                "options": ["炒（いた）める", "煮（に）る", "揚（あ）げる", "沸（わ）かす"],
                "ans": 1,
                "right_exp": "💖 Chuẩn xác! Xào thịt và hành tây trên chảo bằng lửa lớn là `炒（いた）める`.",
                "wrong_exps": [
                    "Chính xác: `炒（いた）める` = xào trên chảo.",
                    "`煮（に）る` là ninh/kho/hầm trong nồi có nước chứ không dùng chảo lửa to.",
                    "`揚（あ）げる` là chiên ngập dầu.",
                    "`沸（わ）かす` là đun sôi nước."
                ]
            },
            {
                "prompt": "陽翔（はると）が作（つく）ったオムライスは少（すこ）し焦（こ）げたのに、なぜみんな喜（よろこ）んで食（た）べたのか。",
                "options": [
                    "陽翔（はると）がお金（かね）を払（はら）って買（か）ってきた外食（がいしょく）だったから",
                    "美咲（みさき）がフォローして味付（あじつ）けを整（ととの）え、みんなで一緒（いっしょ）に楽（たの）しく料理（りょうり）したから",
                    "賞味期限（しょうみきげん）が近（ちか）くて急（いそ）いで片付（かたづ）ける必要（ひつよう）があったから",
                    "ほかに食（た）べる材料（ざいりょう）が一切（いっさい）なかったから"
                ],
                "ans": 2,
                "right_exp": "💖 Chính xác! Dù trứng hơi sém một chút nhưng nhờ Misaki đứng cạnh giúp nêm lại và vẽ trái tim tương cà, cả nhà đều vui vẻ thưởng thức bữa cơm tự nấu ấm áp.",
                "wrong_exps": [
                    "Chương này cậu tự nấu (`自炊`) chứ không mua đồ ăn ngoài (`外食`) nha.",
                    "Chính xác: Nhờ Misaki khéo léo cứu nguy và tình cảm ấm áp của cả nhà.",
                    "Hộp sữa gần hết hạn là câu chuyện hài phía cuối bữa về ông anh Ren thôi nè.",
                    "Trên bàn còn có gà rán, súp rau củ, salad bắp cải và trà lạnh nữa cơ!"
                ]
            },
        ]
    },
    {
        "num": 4,
        "slug": "chuong-04",
        "lesson_id": "p1_c02_b02",
        "title_jp": "第4章：洗濯物（せんたくもの）と[[片付（かたづ）ける|11]]心（こころ）の隙間（すきま）",
        "title_vi": "Chương 04: Đống Quần Áo Phơi & Khoảng Trống Trái Tim Được Thu Gọn",
        "yuki_reminder_top": "Chương 4 ôm trọn 24 từ **Bài 5 (Việc nhà, dọn dẹp & sinh hoạt gia đình)**! Em sẽ thấy đủ quy trình dọn phòng (`掃く・拭く・片付ける・換気する`) và giặt giũ (`洗剤・すすぐ・干す・取り込む・畳む`) ngay trong màn cãi nhau đáng yêu của Haruto và Misaki~",
        "yuki_reminder_bottom": "Xong việc nhà sạch bóng rồi đó em! Hãy nhớ kỹ cặp `部屋が散らかる` (tự động từ: căn phòng bề bộn) và `部屋を片付ける` (tha động từ: dọn gọn phòng) nhé 🧹",
        "soft_notes": [
            (2, "Nhắc nhẹ từ chị Yuki 🧹", "`掃（は）く` là quét bằng chổi, `拭（ふ）く` là lau bằng khăn ẩm, `こする` là chà cọ mạnh vết bẩn cứng đầu! Ba động từ làm sạch hay xuất hiện chung trong câu hỏi chọn từ lắm nha~"),
            (5, "Quy trình giặt phơi chuẩn Nhật 👕", "Cho `洗剤（せんざい）` -> `すすぐ` (giũ nước) -> `干（ほ）す` (phơi ngoài ban công) -> trời mưa thì vội `取（と）り込（こ）む` (thu vào) -> khô rồi `畳（たた）む` (gấp gọn). Quá trực quan luôn!"),
        ],
        "paragraphs": [
            (
                "梅雨（つゆ）入（い）り前（まえ）の週末（しゅうまつ）、シェアハウスは[[湿気（しっけ）|15]]対策（たいさく）の大掃除（おおそうじ）デーになった。しかし蓮（れん）が「[[家事（かじ）|1]]とか[[炊事（すいじ）|2]]って[[面倒（めんどう）くさい|24]]よなあ」と寝転（ねころ）がったせいで、陽翔（はると）と美咲（みさき）が二人（ふたり）で担当（たんとう）することになった。",
                "Cuối tuần trước khi vào mùa mưa, nhà trọ chung tổ chức ngày tổng vệ sinh chống ẩm mốc. Thế nhưng vì Ren cứ nằm ườn ra kêu 'Việc nhà với bếp núc phiền phức chết đi được', cuối cùng chỉ còn Haruto và Misaki phụ trách."
            ),
            (
                "「ほら、陽翔（はると）の机（つくえ）の上（うえ）、プリントで[[散（ち）らかり|10]]っぱなしよ！　まず窓（まど）を開（あ）けて[[換気（かんき）|14]]しながら、資料（しょるい）を[[整理（せいり）して|12]][[片付（かたづ）け|11]]なさい」と美咲（みさき）が指揮（しき）をとる。陽翔（はると）はほうきで廊下（ろうか）を[[掃（は）き|7]]、雑巾（ぞうきん）で床（ゆか）を丁寧（ていねい）に[[拭（ふ）き|8]]、さらにはキッチンの焦（こ）げ跡（あと）までスポンジで力（ちから）いっぱい[[こすり|9]]落（お）とした。",
                "'Nhìn kìa, trên bàn của Haruto toàn giấy tờ bày bừa khắp nơi! Trước tiên vừa mở cửa sổ thông gió, vừa sắp xếp phân loại giấy tờ rồi dọn gọn lại ngay!' — Misaki chỉ huy. Haruto cầm chổi quét hành lang, lấy giẻ lau sạch sàn nhà, rồi cọ rửa mạnh tay sạch bong cả vết cháy trong bếp."
            ),
            (
                "「おっ、やるじゃん陽翔（はると）！　作業（さぎょう）の[[手際（てぎわ）|3]]が良（よ）くなってきたね」と美咲（みさき）が感心（かんしん）する。「ごみも燃（も）えるごみとプラスチックにきちんと[[分別（ぶんべつ）した|13]]し、無駄（むだ）な動（うご）きを[[省（はぶ）け|4]]ば早（はや）いよ。あとでスーパーへ[[買（か）い出（だ）し|5]]に行（い）こうか。今月（こんげつ）の食費（しょくひ）の[[やり繰（く）り|6]]も計算（けいさん）しておいたんだ」",
                "'Ồ, khá lắm Haruto! Thao tác tay chân dọn dẹp khéo hẳn ra rồi đấy' — Misaki gật gù khen. 'Rác cũng phân loại gọn gàng rác cháy được và nhựa rồi nè, bỏ bớt mấy bước thừa đi thì làm nhanh lắm. Lát nữa hai đứa đi siêu thị mua trữ đồ ăn nhé, tớ tính sẵn cả cách thu vén tiền ăn tháng này rồi đấy'."
            ),
            (
                "そう話（はな）している間（あいだ）に洗濯（せんたく）機（き）が止（と）まった。陽翔（はると）が優（やさ）しい香（かお）りの[[洗剤（せんざい）|16]]で洗（あら）い、しっかり水（みず）で[[すすぎ|17]]終（お）えたシーツを、二人（ふたり）でベランダに[[干（ほ）した|18]]。「わっ、青空（あおぞら）に映（は）えてきれい！」",
                "Vừa nói chuyện thì máy giặt dừng lại. Hai đứa cùng mang tấm ga trải giường vừa được Haruto giặt bằng nước giặt thơm dịu và giũ sạch nước ra phơi ngoài ban công. 'Oa, bay phấp phới dưới trời xanh đẹp quá!'"
            ),
            (
                "ところが午後（ごご）三時（さんじ）、急（きゅう）に黒（くろ）い雲（くも）が広（ひろ）がり雨（あめ）がポツリと降（ふ）ってきた。「大変（たいへん）！　急（いそ）いで洗濯物（せんたくもの）を[[取（と）り込（こ）む|19]]よ！」――二人（ふたり）は慌（あわ）ててベランダへ飛（と）び出（だ）し、濡（ぬ）れる前（まえ）に無事（ぶじ）回収（かいしゅう）した。",
                "Ấy thế mà ba giờ chiều, mây đen bất ngờ kéo tới và những hạt mưa bắt đầu rơi lác đác. 'Nguy rồi! Mau thu quần áo vào nhà thôi!' — cả hai hốt hoảng lao ra ban công, kịp thu gọn lại trước khi bị ướt."
            ),
            (
                "リビングに戻（もど）って二人（ふたり）向（む）かい合（あ）い、乾（かわ）いたタオルやシャツを一緒（いっしょ）に[[畳（たた）む|20]]。陽翔（はると）がポケットから破（やぶ）れた靴下（くつした）を出（だ）すと、美咲（みさき）は「もう、仕方（しかた）ないなあ」と言いながら針（はり）と糸（いと）を取（と）り出（だ）して小さな穴（あな）を[[繕（つくろ）って|21]]くれた。",
                "Quay lại phòng khách ngồi đối diện nhau, hai đứa cùng gấp gọn khăn tắm và áo sơ mi đã khô. Thấy Haruto lôi ra chiếc tất bị rách, Misaki khẽ thở dài 'Đúng là hết cách với cậu' rồi lấy kim chỉ khâu vá lại lỗ thủng nhỏ giúp cậu."
            ),
            (
                "「ありがとう、美咲（みさき）。将来（しょうらい）こんなふうに、古（ふる）い家電（かでん）を一緒（いっしょ）に[[買（か）い換（か）え|22]]たり、二人（ふたり）で協力（きょうりょく）して[[育児（いくじ）|23]]をしたりできたら素敵（すてき）だろうな……」と陽翔（はると）がつい口（くち）を滑（すべ）らせた瞬間（しゅんかん）、美咲（みさき）の指先（ゆびさき）がぴたりと止（と）まり、耳（みみ）まで真っ赤（まっか）になった。",
                "'Cảm ơn nhé, Misaki. Sau này mà cũng có thể cùng nhau đi mua máy móc mới thay đồ cũ, rồi hai đứa cùng hợp lực nuôi dạy con cái như thế này chắc tuyệt lắm nhỉ...' — Khoảnh khắc Haruto lỡ miệng buột ra câu đó, đầu ngón tay Misaki khựng hẳn lại, gương mặt đỏ lựng lan tận mang tai."
            ),
        ],
        "quiz": [
            {
                "prompt": "朝（あさ）起（お）きたら、新鮮（しんせん）な空気（くうき）を入（い）れるために窓（まど）を開（あ）けて部屋（へや）を（　　）。",
                "options": ["換気（かんき）する", "分別（ぶんべつ）する", "散（ち）らかる", "繕（つくろ）う"],
                "ans": 1,
                "right_exp": "💖 Đúng rồi em! Mở cửa sổ đón không khí mới cho thoáng phòng là `換気する` (HOÁN KHÍ).",
                "wrong_exps": [
                    "Chính xác: `換気する` = thông gió cho căn phòng.",
                    "`分別する` là phân loại rác thải nhé em.",
                    "`散らかる` là tự động từ chỉ sự bừa bộn.",
                    "`繕う` là khâu vá chỗ rách trên quần áo/tất."
                ]
            },
            {
                "prompt": "雨（あめ）が降（ふ）り始（はじ）めたので、ベランダに干（ほ）してあった洗濯物（せんたくもの）を急（いそ）いで（　　）。",
                "options": ["取（と）り込（こ）んだ", "すすいだ", "掃（は）いた", "こすった"],
                "ans": 1,
                "right_exp": "💖 Chuẩn không cần chỉnh! Thấy trời đổ mưa vội chạy ra thu quần áo vào nhà dùng `取り込む`.",
                "wrong_exps": [
                    "Chính xác: `取り込む` = thu đồ đang phơi vào nhà.",
                    "`すすぐ` là giũ sạch xà phòng bằng nước.",
                    "`掃く` là dùng chổi quét sàn.",
                    "`こする` là chà xát cọ rửa."
                ]
            },
            {
                "prompt": "限（かぎ）られたお小遣（こづか）いの中（なか）で、毎月の生活費（せいかつひ）をうまく（　　）している。",
                "options": ["やり繰（く）り", "買い出（かいだ）し", "買（か）い換（か）え", "手際（てぎわ）"],
                "ans": 1,
                "right_exp": "💖 Quá giỏi! Thu vén, xoay xở cân đối chi tiêu trong khoản tiền hạn hẹp là `やり繰りする`.",
                "wrong_exps": [
                    "Chính xác: `やり繰り` = khéo léo thu vén, xoay xở chi tiêu.",
                    "`買い出し` là đi mua đồ tích trữ ở siêu thị.",
                    "`買い換え` là mua đồ mới thay thế đồ cũ.",
                    "`手際` là sự khéo tay nhanh nhẹn trong thao tác."
                ]
            },
            {
                "prompt": "靴下（くつした）の親指（おやゆび）のあたりに小さ（ちいさ）な穴（あな）が開（あ）いたので、針（はり）と糸（いと）で（　　）。",
                "options": ["繕（つくろ）った", "畳（たた）んだ", "拭（ふ）いた", "省（はぶ）いた"],
                "ans": 1,
                "right_exp": "💖 Tuyệt vời! Vá lại chỗ rách trên áo hay tất dùng `繕（つくろ）う`.",
                "wrong_exps": [
                    "Chính xác: `繕う` = khâu vá chỗ rách.",
                    "`畳む` là gấp quần áo cho gọn.",
                    "`拭く` là lau chùi bề mặt bằng khăn.",
                    "`省く` là cắt giảm bớt công đoạn."
                ]
            },
            {
                "prompt": "陽翔（はると）のどんな言葉（ことば）を聞（き）いて、美咲（みさき）は耳（みみ）まで真っ赤（まっか）になったのか。",
                "options": [
                    "蓮（れん）先輩（せんぱい）が家事（かじ）をサボって寝（ね）ていたこと",
                    "将来（しょうらい）も二人（ふたり）で暮（く）らして買（か）い換（か）えや育児（いくじ）ができたら素敵（すてき）だと言（い）ったこと",
                    "スーパーの割引（わりびき）時間（じかん）を忘（わす）れてしまったこと",
                    "靴下（くつした）をまだ洗（あら）っていなかったこと"
                ],
                "ans": 2,
                "right_exp": "💖 Chuẩn rồi! Tự nhiên anh chàng lại mơ màng chuyện tương lai hai người cùng sống, cùng mua sắm và nuôi con nên nàng tsundere ngượng chín mặt luôn~",
                "wrong_exps": [
                    "Chuyện anh Ren lười xảy ra ngay từ đầu chương, không làm Misaki đỏ mặt đâu nè.",
                    "Chính xác: Lời buột miệng ngọt ngào về tương lai chung đôi của Haruto!",
                    "Trong chương hai bạn chỉ tính toán chi tiêu chứ không quên giờ giảm giá nha.",
                    "Chiếc tất là đã giặt khô rồi đem ra khâu vá chỗ rách chứ không phải chưa giặt nhé."
                ]
            },
        ]
    },
    {
        "num": 5,
        "slug": "chuong-05",
        "lesson_id": "p1_c03_b01",
        "title_jp": "第5章：学園祭（がくえんさい）の[[舞台（ぶたい）|6]]と鳴（な）り止（や）まない[[拍手（はくしゅ）|13]]",
        "title_vi": "Chương 05: Sân Khấu Lễ Hội Trường & Tràng Pháo Tay Không Dứt",
        "yuki_reminder_top": "Chương 5 chứa đủ 22 từ **Bài 7 (Sở thích, Nghệ thuật, Thể thao & Giải trí)**! Nào là kịch bản (`脚本`), kiệt tác (`傑作`), thưởng thức (`鑑賞`), vỡ òa xúc động (`感銘を受ける`), lẫn cả thi đấu thể thao hòa (`引き分け`) và cổ vũ (`応援する`) — chuẩn bị tinh thần đi hội trường cổ vũ cặp đôi nhé 🎭✨",
        "yuki_reminder_bottom": "Cháy hết mình cùng lễ hội trường rồi ha~ Nhớ phân biệt `鑑賞（かんしょう）` (thưởng thức nghệ thuật như nhạc/tranh/kịch) với `観賞（かんしょう）` (ngắm hoa/cá cảnh) kẻo bị lừa ở đề JLPT đó em! 🌸",
        "soft_notes": [
            (2, "Nhắc nhẹ từ chị Yuki 🎭", "Cặp động từ say mê: `〜に夢中（むちゅう）になる` và `〜に熱中（ねっちゅう）する` đều đi với trợ từ `に` nha em! Đừng nhầm với `〜を` nhé~"),
            (5, "Từ vựng thi đấu hay gặp ⚽", "`勝負（しょうぶ）` (trận đấu thắng thua), `引（ひ）き分（わ）け` (kết quả hòa), `敗（やぶ）れる` (thua trận), `記録（きろく）を更新（こうしん）する` (phá kỷ lục). Đi chung một trận đấu cực dễ nhớ!"),
        ],
        "paragraphs": [
            (
                "秋（あき）の学園祭（がくえんさい）が近（ちか）づき、桜坂（さくらざか）シェアハウスのメンバーもそれぞれ準備（じゅんび）に大忙（おおいそが）しだ。普段（ふだん）はテレビやゲームといった[[娯楽（ごらく）|1]]ばかりの蓮（れん）も、演劇（えんげき）サークルの[[脚本（きゃくほん）|12]]書（か）きに[[熱中（ねっちゅう）|3]]し、ひなたは美術部（びじゅつぶ）の[[展覧会（てんらんかい）|8]]に飾（かざ）る油絵（あぶらえ）の[[創作（そうさく）|10]]に[[夢中（むちゅう）になって|2]]いた。",
                "Lễ hội trường mùa thu cận kề, các thành viên nhà Sakurazaka ai nấy đều tất bật chuẩn bị. Ngay cả anh Ren bình thường chỉ mê giải trí như tivi hay game giờ cũng say mê cuồng nhiệt viết kịch bản cho câu lạc bộ kịch, còn Hinata thì mải mê quên ăn quên ngủ sáng tác bức tranh sơn dầu trưng bày ở triển lãm câu lạc bộ mỹ thuật."
            ),
            (
                "「ねえ陽翔（はると）、勉強（べんきょう）の[[気分転換（きぶんてんかん）|22]]に、今度（こんど）の日曜日（にちようび）、演劇（えんげき）の[[会場（かいじょう）|19]]へ一緒（いっしょ）にリハーサルを見（み）に行（い）かない？」と美咲（みさき）が[[あらすじ|11]]のプリントを渡（わた）してくれた。美咲（みさき）はピアノ部（ぶ）として、劇（げき）の[[舞台（ぶたい）|6]]裏（うら）でBGMを[[演奏（えんそう）|5]]することになったのだ。",
                "'Này Haruto, để giải khuây thay đổi tâm trạng khỏi đống bài vở, Chủ nhật tới cậu có muốn cùng tới hội trường xem buổi tổng duyệt kịch không?' — Misaki đưa cho cậu tờ tóm tắt cốt truyện. Hóa ra Misaki thuộc câu lạc bộ piano và sẽ biểu diễn nhạc nền ngay trên sân khấu vở kịch."
            ),
            (
                "迎（むか）えた学園祭（がくえんさい）初日（しょにち）。午前中（ごぜんちゅう）は体育館（たいいくかん）でバスケ部の親善（しんぜん）試合（しあい）が行（おこな）われた。陽翔（はると）は[[応援（おうえん）|18]]席（せき）の最前列（さいぜんれつ）で声（こえ）を枯（か）らし、チームは次々（つぎつぎ）と[[得点（とくてん）|20]]を重（かさ）ねて大会（たいかい）新（しん）[[記録（きろく）を更新（こうしん）する|21]]勢（いきお）いだった。",
                "Ngày đầu tiên của lễ hội trường cuối cùng cũng đến. Buổi sáng diễn ra trận giao hữu bóng rổ tại nhà thi đấu. Haruto ngồi hàng đầu khu cổ vũ hét đến khản cả cổ, đội nhà ghi liên tiếp nhiều điểm số với khí thế như sắp phá kỷ lục giải đấu."
            ),
            (
                "最後（さいご）まで白熱（はくねつ）した[[勝負（しょうぶ）|15]]だったが、あと一歩（いっぽ）及（およ）ばず昨年（さくねん）の王者（おうじゃ）に惜（お）しくも[[敗（やぶ）れる|17]]かと思（おも）いきや、終了（しゅうりょう）ブザー直前（ちょくぜん）のシュートが決（き）まり、奇跡的（きせきてき）な[[引（ひ）き分（わ）け|16]]に終（お）わった！",
                "Đó là một trận đấu thắng thua nghẹt thở đến giây cuối cùng; tưởng chừng thiếu một chút nữa sẽ thua đương kim vô địch năm ngoái, thì cú ném sát giờ còi kết thúc lại vào rổ, khép lại trận đấu bằng tỷ số hòa đầy kỳ tích!"
            ),
            (
                "午後（ごご）は講堂（こうどう）でクラシック音楽（おんがく）の[[鑑賞（かんしょう）|4]]と演劇（えんげき）の本番（ほんばん）だ。ひなたの絵（え）も「これは学生（がくせい）レベルの域（いき）を超（こ）えた[[傑作（けっさく）|9]]だ！」と評判（ひょうばん）になった。幕（まく）が上（あ）がると、美咲（みさき）の繊細（せんさい）なピアノの音色（ねいろ）が響（ひび）き渡（わた）り、満員（まんいん）の[[観客（かんきゃく）|7]]が息（いき）を呑（の）んだ。",
                "Buổi chiều tại hội trường lớn là phần thưởng thức nhạc cổ điển và buổi diễn chính thức của vở kịch. Bức tranh của Hinata cũng được khen ngợi là 'kiệt tác vượt xa tầm sinh viên'. Khi bức màn nhung kéo lên, tiếng đàn piano tinh tế của Misaki vang vọng khắp khán phòng khiến khán giả chật kín như nín thở."
            ),
            (
                "エンディングの瞬間（しゅんかん）、割（わ）れんばかりの[[拍手（はくしゅ）|13]]が湧（わ）き起（お）こった。陽翔（はると）は彼女（かのじょ）の真剣（しんけん）な横顔（よこがお）に深（ふか）く[[感銘（かんめい）を受（う）け|14]]、ロビーで花束（はなたば）を渡（わた）しながら「美咲（みさき）のピアノ、世界一（せかいいち）きれいだったよ」とまっすぐ伝（つた）えたのだった。",
                "Khoảnh khắc kết thúc vở diễn, những tràng pháo tay vang dội như vỡ òa. Haruto xúc động sâu sắc trước góc nghiêng đầy tập trung của cô ấy, liền đón ở sảnh trao bó hoa và nói thẳng từ đáy lòng: 'Tiếng đàn của Misaki đẹp nhất thế giới luôn đấy'."
            ),
        ],
        "quiz": [
            {
                "prompt": "美術（びじゅつ）博物館（はくぶつかん）で、有名（ゆうめい）な画家（がか）の絵画（かいが）をゆっくり（　　）した。",
                "options": ["鑑賞（かんしょう）", "応援（おうえん）", "演奏（えんそう）", "創作（そうさく）"],
                "ans": 1,
                "right_exp": "💖 Chính xác! Thưởng thức tác phẩm nghệ thuật (tranh, nhạc, phim, kịch) dùng `鑑賞する`.",
                "wrong_exps": [
                    "Chính xác: `鑑賞（かんしょう）する` = thưởng thức nghệ thuật.",
                    "`応援する` là cổ vũ, ủng hộ đội thi đấu hay bạn bè.",
                    "`演奏する` là tự mình biểu diễn nhạc cụ chứ không phải đi xem tranh.",
                    "`創作する` là tự tay sáng tác ra tác phẩm."
                ]
            },
            {
                "prompt": "長（なが）い映画（えいが）を見（み）る時間（じかん）がないので、まずパンフレットで（　　）だけ読（よ）んだ。",
                "options": ["あらすじ", "脚本（きゃくほん）", "拍手（はくしゅ）", "記録（きろく）"],
                "ans": 1,
                "right_exp": "💖 Chuẩn rồi! Phần tóm tắt nội dung chính / cốt truyện là `あらすじ`.",
                "wrong_exps": [
                    "Chính xác: `あらすじ` = tóm tắt cốt truyện.",
                    "`脚本` là kịch bản chi tiết từng lời thoại cho diễn viên đóng, không phải bản tóm tắt ngắn.",
                    "`拍手` là tiếng vỗ tay tán thưởng.",
                    "`記録` là kỷ lục hoặc ghi chép."
                ]
            },
            {
                "prompt": "テスト勉強（べんきょう）ばかりで頭（あたま）が疲（つか）れたから、散歩（さんぽ）して（　　）しよう。",
                "options": ["気分転換（きぶんてんかん）", "引（ひ）き分（わ）け", "展覧会（てんらんかい）", "得点（とくてん）"],
                "ans": 1,
                "right_exp": "💖 Đúng rồi em! Làm việc nhẹ nhàng để thay đổi tâm trạng cho thư thái là `気分転換`!",
                "wrong_exps": [
                    "Chính xác: `気分転換` = giải khuây, đổi gió cho đỡ mệt đầu.",
                    "`引き分け` là tỷ số hòa trong trận đấu.",
                    "`展覧会` là buổi triển lãm nghệ thuật.",
                    "`得点` là điểm số đạt được."
                ]
            },
            {
                "prompt": "接戦（せっせん）の末（すえ）、両（りょう）チームとも同点（どうてん）で（　　）に終（お）わった。",
                "options": ["引（ひ）き分（わ）け", "傑作（けっさく）", "勝負（しょうぶ）", "敗（やぶ）れ"],
                "ans": 1,
                "right_exp": "💖 Quá chuẩn! Hai đội bằng điểm (`同点`) thì trận đấu kết thúc với kết quả hòa `引き分け`.",
                "wrong_exps": [
                    "Chính xác: `引き分け` = trận hòa.",
                    "`傑作` là kiệt tác nghệ thuật.",
                    "`勝負` chỉ cuộc đấu phân thắng bại nói chung, không mang nghĩa hòa nhau.",
                    "`敗れ` (từ động từ 敗れる) nghĩa là bị đánh bại, thua trận."
                ]
            },
            {
                "prompt": "学園祭（がくえんさい）の演劇（えんげき）の後（あと）、陽翔（はると）はなぜ美咲（みさき）に花束（はなたば）を渡（わた）したのか。",
                "options": [
                    "ピアノ演奏（えんそう）に深（ふか）く感銘（かんめい）を受（う）け、素敵（すてき）だったと素直（すなお）に伝（つた）えたかったから",
                    "美咲（みさき）が舞台（ぶたい）で失敗（しっぱい）して泣（な）いていたから",
                    "蓮（れん）に頼（たの）まれて借（か）りたお金（かね）を返（かえ）すため",
                    "バスケの試合（しあい）で勝（か）ったお祝（いわ）いのため"
                ],
                "ans": 1,
                "right_exp": "💖 Đáng yêu quá trời! Haruto thật sự xúc động sâu sắc (`感銘を受ける`) trước tiếng đàn của Misaki nên tặng hoa và khen hết lời đó~",
                "wrong_exps": [
                    "Chính xác: Vì xúc động trước màn biểu diễn tuyệt đẹp của Misaki.",
                    "Màn biểu diễn thành công vang dội với tràng pháo tay không dứt chứ không hề thất bại nhé.",
                    "Không có vụ trả nợ hộ Ren đâu nè.",
                    "Bó hoa tặng sau buổi diễn kịch và piano buổi chiều, không phải cho trận bóng rổ buổi sáng nhé."
                ]
            },
        ]
    },
    {
        "num": 6,
        "slug": "chuong-06",
        "lesson_id": "p1_c04_b01",
        "title_jp": "第6章：[[往復（おうふく）|4]]切符（きっぷ）と温泉（おんせん）旅館（りょかん）の一夜（いちや）",
        "title_vi": "Chương 06: Tấm Vé Khứ Hồi & Một Đêm Ở Lữ Quán Suối Nước Nóng",
        "yuki_reminder_top": "Chương 6 dẫn cả nhóm đi du lịch suối nước nóng cùng 26 từ **Bài 8 (Du lịch, Lưu trú & Giao thông)**! Từ quầy vé (`窓口`), tàu chạy thẳng (`直通`) vs đổi tàu (`乗り換え`), thông báo ga tàu (`運休・見合わせる・通過・停車`) cho đến tắc đường (`渋滞・迂回`) — toàn từ cực thực tế khi sang Nhật đó em! 🚄♨️",
        "yuki_reminder_bottom": "Chuyến đi bão táp nhưng tình cảm lại nở hoa ngọt ngào rồi nè~ Chú ý cụm `運転を見合わせる` (tạm hoãn chạy tàu vì thời tiết) và `払い戻し` (hoàn tiền vé) vì rất hay thi JLPT nha em! 🌸",
        "soft_notes": [
            (2, "Nhắc nhẹ nhà ga Nhật Bản 🚄", "Ở Nhật khi đi tàu nhớ nhìn kỹ bảng điện tử: `直通（ちょくつう）` là chạy thẳng không phải đổi tuyến, còn nếu có đổi tuyến là `乗（の）り換（か）え`; tàu nhanh `通過（つうか）する` sẽ vụt qua ga nhỏ, còn tàu thường sẽ `停車（ていしゃ）する` ở mọi ga nhé!"),
            (5, "Bẫy thông báo sự cố ⚠️", "`運休（うんきゅう）` = hủy chuyến hẳn luôn, còn `運転（うんてん）を見合（みあ）わせる` = tạm ngừng chạy chờ xem xét tình hình (ví dụ chờ gió bão ngớt). Trong trắc nghiệm hay hỏi phân biệt sắc thái này lắm đó em!"),
        ],
        "paragraphs": [
            (
                "冬休（ふゆやす）み、四人（よにん）は箱根（はこね）の温泉（おんせん）旅館（りょかん）に[[宿泊（しゅくはく）する|1]]旅行（りょこう）を計画（けいかく）した。陽翔（はると）は駅（えき）のみどりの[[窓口（まどぐち）|6]]へ並（なら）び、[[片道（かたみち）|3]]ではなくお得な[[往復（おうふく）|4]]チケットを購入（こうにゅう）した。いつも学校（がっこう）で使（つか）う[[定期券（ていきけん）|19]]とは別（べつ）に、[[運賃（うんちん）|18]]もきちんと計算（けいさん）済みだ。",
                "Kỳ nghỉ đông, bốn người lên kế hoạch đi du lịch nghỉ qua đêm tại một lữ quán suối nước nóng ở Hakone. Haruto xếp hàng tại quầy vé Midori của nhà ga, mua vé khứ hồi ưu đãi thay vì vé một chiều. Ngoài chiếc vé tháng vẫn dùng đi học hàng ngày, cậu còn tính kỹ cả giá cước tàu xe."
            ),
            (
                "「いい？　新宿（しんじゅく）から[[直通（ちょくつう）|14]]のロマンスカーに乗（の）れば、途中（とちゅう）の[[乗（の）り換（か）え|15]]なしよ！　途中の小（ちい）さな駅（えき）は全部（ぜんぶ）[[通過（つうか）して|16]]、箱根湯本（はこねゆもと）駅（えき）にだけ[[停車（ていしゃ）|17]]するから早（はや）いわ」と美咲（みさき）が[[発着（はっちゃく）|13]]時刻（じこく）表（ひょう）を指（ゆび）さした。",
                "'Nghe này: nếu lên tàu Romancecar chạy thẳng từ Shinjuku thì giữa đường không cần chuyển tuyến đâu! Các ga nhỏ dọc đường tàu chạy vụt qua hết và chỉ dừng đỗ ở ga Hakone-Yumoto nên nhanh lắm' — Misaki chỉ vào bảng giờ tàu khởi hành và đến bến."
            ),
            (
                "ところが出発（しゅっぱつ）当朝（とうちょう）、ひなたから電話（でんわ）が入（はい）った。「ごめんなさい、バイト先（さき）で急（きゅう）なシフトが入（はい）って行（い）けなくなりました…」。蓮（れん）も「俺（おれ）も風邪（かぜ）っぽいから[[払（はら）い戻（もど）し|5]]手続き（てつづき）だけ頼（たの）むわ（ニヤリ）」と、わざとらしく二人（ふたり）だけにしてくれた。",
                "Thế nhưng sáng ngày khởi hành, Hinata gọi điện báo: 'Em xin lỗi, chỗ làm thêm đột xuất bị thiếu người nên em không đi được rồi...'. Ông anh Ren cũng hùa theo: 'Anh hơi cảm cúm nên nhờ hai đứa làm thủ tục hoàn tiền vé hộ anh nha (cười nham hiểm)', cố tình để lại chuyến đi cho riêng hai người."
            ),
            (
                "結局（けっきょく）、陽翔（はると）と美咲（みさき）の二人（ふたり）旅（たび）になった。車内（しゃない）は[[観光（かんこう）客（きゃく）|7]]でかなり[[混雑（こんざつ）|26]]していたが、隣（となり）同士（どうし）の席（せき）に座（すわ）れて胸（むね）が高鳴（たかな）る。ところが山間部（さんかんぶ）で大雪（おおゆき）が降（ふ）り、鉄道（てつどう）の[[運行（うんこう）|10]]が乱（みだ）れて後続（こうぞく）の列車（れっしゃ）は[[見合（みあ）わせる|12]]ことになり、夕方（ゆうがた）の便（びん）は[[運休（うんきゅう）|11]]とアナウンスされた。",
                "Cuối cùng chuyến đi biến thành hành trình của riêng Haruto và Misaki. Trên tàu khá đông đúc khách du lịch nhưng hai đứa vẫn được ngồi cạnh nhau khiến tim đập rộn ràng. Ấy thế mà khi vào vùng núi, tuyết rơi dày đặc khiến việc vận hành tàu bị gián đoạn; loa thông báo các chuyến sau phải tạm hoãn chạy để theo dõi và chuyến chiều bị hủy hoàn toàn."
            ),
            (
                "「仕方（しかた）ない、バスに乗（の）ろう」と駅（えき）を出（で）たものの、道路（どうろ）も大（だい）[[渋滞（じゅうたい）|20]]。「前（まえ）の方（ほう）でトラックと乗用車（じょうようしゃ）が[[追突（ついとつ）|23]]したのか、いや正面（しょうめん）[[衝突（しょうとつ）|22]]らしいぞ。先（さき）の[[踏切（ふみきり）|24]]を渡（わた）って別（べつ）の道（みち）へ[[迂回（うかい）|21]]しよう」と運転手（うんてんしゅ）さんが機転（きてん）を利（き）かせた。",
                "'Đành bắt xe buýt vậy' — bước ra khỏi ga nhưng đường bộ cũng ùn tắc kéo dài. Bác tài xế nhanh trí nói: 'Chắc phía trước có xe tải húc đuôi hay đâm trực diện nhau gì đó rồi. Ta vượt qua chỗ chắn đường sắt phía trước rồi đi đường vòng tránh tắc nhé'."
            ),
            (
                "ようやく[[現地（げんち）|2]]へ着（つ）き、[[横断（おうだん）|25]]歩道（ほどう）を渡（わた）って旅館（りょかん）へ。翌日（よくじつ）は雪見（ゆきみ）の[[名所（めいしょ）|8]]を巡（めぐ）り、シェアハウスのみんなへ温泉（おんせん）饅頭（まんじゅう）のお[[土産（みやげ）|9]]をたくさん買（か）った。夜（よる）、浴衣（ゆかた）姿（すがた）で星空（ほしぞら）を見上（みあ）げながら「二人（ふたり）きりも悪（わる）くないね」と笑（わら）った美咲（みさき）の横顔（よこがお）を、陽翔（はると）は忘（わす）れられなかった。",
                "Cuối cùng cũng tới được nơi, hai đứa băng qua vạch kẻ đường để vào lữ quán. Hôm sau, cả hai dạo thăm các danh lam thắng cảnh ngắm tuyết rơi và mua thật nhiều bánh bao suối nóng làm quà lưu niệm cho mọi người ở nhà trọ. Đêm hôm ấy, khoảnh khắc Misaki trong bộ yukata ngước nhìn bầu trời sao rồi khẽ cười: 'Đi riêng hai đứa thế này cũng đâu tệ nhỉ', Haruto biết mình mãi mãi không thể nào quên."
            ),
        ],
        "quiz": [
            {
                "prompt": "台風（たいふう）の強風（きょうふう）のため、安全（あんぜん）を確認（かくにん）するまで電車（でんしゃ）の運転（うんてん）を一時的（いちじてき）に（　　）います。",
                "options": ["見合（みあ）わせて", "通過（つうか）して", "追突（ついとつ）して", "宿泊（しゅくはく）して"],
                "ans": 1,
                "right_exp": "💖 Chính xác tuyệt đối! Tạm ngừng chạy tàu chờ kiểm tra an toàn là `運転を見合わせる`.",
                "wrong_exps": [
                    "Chính xác: `見合わせる` = tạm hoãn lại để theo dõi tình hình.",
                    "`通過する` là chạy thẳng qua ga không dừng.",
                    "`追突する` là đâm vào đuôi xe phía trước.",
                    "`宿泊する` là nghỉ trọ qua đêm tại khách sạn/lữ quán."
                ]
            },
            {
                "prompt": "急（きゅう）に旅行（りょこう）が中止（ちゅうし）になったので、みどりの窓口（まどぐち）で切符（きっぷ）の（　　）をした。",
                "options": ["払（はら）い戻（もど）し", "乗（の）り換（か）え", "定期券（ていきけん）", "運賃（うんちん）"],
                "ans": 1,
                "right_exp": "💖 Quá giỏi! Trả lại vé để nhận tiền hoàn lại là `払い戻し`.",
                "wrong_exps": [
                    "Chính xác: `払い戻し` = thủ tục hoàn tiền vé.",
                    "`乗り換え` là chuyển tuyến tàu xe.",
                    "`定期券` là thẻ vé tháng đi học/đi làm.",
                    "`運賃` là tiền cước vé đi lại nói chung."
                ]
            },
            {
                "prompt": "工事（こうじ）で通行（つうこう）止（ど）めになっているので、少（すこ）し遠回（とおまわ）りして別（べつ）の道（みち）へ（　　）しよう。",
                "options": ["迂回（うかい）", "直通（ちょくつう）", "発着（はっちゃく）", "横断（おうだん）"],
                "ans": 1,
                "right_exp": "💖 Đúng rồi em! Đi đường vòng tránh đoạn tắc/cấm đường là `迂回（うかい）する`.",
                "wrong_exps": [
                    "Chính xác: `迂回する` = đi đường vòng.",
                    "`直通` là chạy thẳng một mạch không đổi tuyến.",
                    "`発着` là giờ khởi hành và đến bến.",
                    "`横断する` là băng ngang qua đường/lục địa."
                ]
            },
            {
                "prompt": "行（い）きと帰（かえ）りの両方（りょうほう）がセットになったチケットを何（なん）と言（い）うか。",
                "options": ["往復（おうふく）切符（きっぷ）", "片道（かたみち）切符（きっぷ）", "運休（うんきゅう）", "混雑（こんざつ）"],
                "ans": 1,
                "right_exp": "💖 Chính xác! Cả đi lẫn về là `往復（おうふく）` (VÃNG PHỤC), còn một chiều là `片道（かたみち）`.",
                "wrong_exps": [
                    "Chính xác: `往復` = khứ hồi hai chiều.",
                    "`片道` chỉ là vé một chiều đi thôi nha em.",
                    "`運休` là ngừng chạy hủy chuyến.",
                    "`混雑` là tình trạng đông đúc chen chúc."
                ]
            },
            {
                "prompt": "なぜ陽翔（はると）と美咲（みさき）の二人（ふたり）きりの旅行（りょこう）になったのか。",
                "options": [
                    "電車（でんしゃ）が混雑（こんざつ）していて蓮（れん）たちが乗（の）れなかったから",
                    "ひなたは急（きゅう）なアルバイトが入（はい）り、蓮（れん）は二人のためにわざと欠席（けっせき）したから",
                    "旅館（りょかん）の部屋（へや）が二人分（ふたりぶん）しか予約（よやく）できなかったから",
                    "二人が相談（そうだん）して蓮（れん）たちを置いていったから"
                ],
                "ans": 2,
                "right_exp": "💖 Quá tinh ý! Hinata bận ca làm đột xuất, còn anh Ren cố tình giả vờ cảm (`ニヤリ`) để tạo cơ hội cho đôi bạn trẻ đi riêng với nhau đó!",
                "wrong_exps": [
                    "Ren và Hinata báo không đi từ sáng ở nhà trước khi lên tàu nha em.",
                    "Chính xác: Hinata kẹt việc làm thêm còn Ren cố tình nhường không gian cho hai người.",
                    "Ban đầu đã mua vé cho cả 4 người rồi sau đó mới nhờ hoàn vé cho Ren và Hinata.",
                    "Hai đứa không hề cố tình bỏ rơi bạn đâu nè."
                ]
            },
        ]
    },
    {
        "num": 7,
        "slug": "chuong-07",
        "lesson_id": "p1_c05_b01",
        "title_jp": "第7章：図書館（としょかん）の隣（となり）席（せき）と[[模擬試験（もぎしけん）|11]]の[[合否（ごうひ）|12]]",
        "title_vi": "Chương 07: Chiếc Ghế Kế Bên Ở Thư Viện & Kết Quả Kỳ Thi Thử",
        "yuki_reminder_top": "Chương 7 bước vào giảng đường đại học với trọn 25 từ **Bài 10 (Trường học, Học tập & Thi cử)**! Có từ vựng học bổng (`奨学金`), tín chỉ (`単位`), bài tiểu luận (`提出・添削`), thi thử (`模擬試験`) và sự kiên trì (`根気`) — đọc là thấy có động lực ôn JLPT cùng hai bạn liền nè 📚✨",
        "yuki_reminder_bottom": "Kiên trì (`根気よく`) như Haruto rồi chắc chắn tụi mình cũng sẽ vượt qua điểm yếu (`克服する`) và đạt thành tích xuất sắc (`優秀な成績`) thôi! Cùng check 5 câu hỏi bài này nha 🌸",
        "soft_notes": [
            (2, "Nhắc nhẹ từ chị Yuki 🎓", "Phân biệt chuẩn 2 từ hay nhầm ở trường: `講義（こうぎ）` (giờ giảng lý thuyết đông người) vs `ゼミ` (nhóm thảo luận chuyên sâu với giáo sư), và `添削（てんさく）` (sửa câu chữ bài viết) vs `採点（さいてん）` (chấm điểm)!"),
            (5, "Cụm vàng mùa thi 🌟", "`単位（たんい）を取（と）る` (lấy tín chỉ), `基準（きじゅん）を満（み）たす` (đạt chuẩn), `苦手（にがて）を克服（こくふく）する` (khắc phục điểm yếu), `根気（こんき）よく続（つづ）ける` (kiên trì theo đuổi). Câu nào cũng cực hay xuất hiện trong đề N2!"),
        ],
        "paragraphs": [
            (
                "冬（ふゆ）が明（あ）けて新学期（しんがっき）。陽翔（はると）は将来（しょうらい）のため、大学院（だいがくいん）へ[[進学（しんがく）|1]]して専門（せんもん）の経済（けいざい）をもっと[[専攻（せんこう）|2]]しようか悩み（なやみ）ながら、[[奨学金（しょうがくきん）|10]]の申請（しんせい）書類（しょるい）を準備（じゅんび）していた。",
                "Mùa đông qua đi nhường chỗ cho học kỳ mới. Nghĩ cho tương lai, Haruto vừa phân vân có nên học lên cao học để học chuyên sâu thêm về kinh tế hay không, vừa chuẩn bị hồ sơ xin học bổng."
            ),
            (
                "「今学期（こんがっき）は卒業（そつぎょう）に必要な[[単位（たんい）|5]]がぎりぎりなんだから、必修（ひっしゅう）科目（かもく）をしっかり[[履修（りしゅう）|6]]しなきゃダメよ！」と美咲（みさき）がスケジュール帳（ちょう）を覗（のぞ）き込（こ）む。大学（だいがく）の厳しい[[校則（こうそく）|8]]や[[講義（こうぎ）|3]]の出席（しゅっせき）チェックに加えて、[[ゼミ|4]]の教授（きょうじゅ）から[[推薦（すいせん）|9]]状（じょう）をもらうには、まず課題（かだい）レポートを期限（きげん）までに[[提出（ていしゅつ）する|7]]ことが絶対（ぜったい）条件（じょうけん）だ。",
                "'Học kỳ này số tín chỉ cần để tốt nghiệp của cậu sát nút lắm rồi đấy, phải đăng ký học đầy đủ các môn bắt buộc đi chứ!' — Misaki ghé sát xem sổ kế hoạch của cậu. Ngoài nội quy nghiêm khắc của trường và điểm danh giờ giảng lý thuyết, để xin được thư tiến cử từ giáo sư nhóm seminar, điều kiện tiên quyết là phải nộp báo cáo bài tập đúng hạn."
            ),
            (
                "「でも僕（ぼく）、データ分析（ぶんせき）や理論（りろん）の[[考察（こうさつ）|23]]が苦手（にがて）でさ。専門書（せんもんしょ）を[[参照（さんしょう）|24]]しても、公式（こうしき）を[[暗記（あんき）|19]]するだけで精一杯（せいいっぱい）なんだ。美咲（みさき）みたいに[[優秀（ゆうしゅう）|15]]で、習（なら）った知識（ちしき）をすぐ問題（もんだい）に[[応用（おうよう）する|20]]力（ちから）があればなあ」",
                "'Nhưng mà tớ kém khoản phân tích số liệu và khảo sát suy luận lý thuyết lắm. Dù có tham khảo sách chuyên ngành, học thuộc lòng công thức thôi đã hết hơi rồi. Giá mà được xuất sắc như Misaki, vừa học xong đã vận dụng ngay kiến thức vào bài tập thì tốt biết mấy'."
            ),
            (
                "「[[成績（せいせき）|14]]が他（ほか）の人（ひと）より少（すこ）し[[劣（おと）る|16]]からって腐（くさ）らないで！　ほら、毎日（まいにち）図書館（としょかん）で一緒（いっしょ）に勉強（べんきょう）すれば、苦手（にがて）もきっと[[克服（こくふく）|22]]できるし、合格（ごうかく）[[基準（きじゅん）|13]]だって超（こ）えられるよ。英語（えいご）もビジネス会話（かいわ）まで[[習得（しゅうとく）|21]]するまで、私（わたし）が[[根気（こんき）|25]]よく付（つ）き合（あ）ってあげる」",
                "'Đừng có nản chỉ vì bảng điểm hơi kém hơn người khác một chút chứ! Nào, mỗi ngày cùng học ở thư viện với tớ, cậu nhất định sẽ khắc phục được môn yếu và vượt qua tiêu chuẩn đỗ cho xem. Ngay cả tiếng Anh thương mại tớ cũng sẽ kiên nhẫn kèm cậu đến khi thành thạo thì thôi!'"
            ),
            (
                "それからの一ヶ月（いっかげつ）、美咲（みさき）は毎日（まいにち）陽翔（はると）の小論文（しょうろんぶん）を赤ペンで丁寧に[[添削（てんさく）|17]]し、[[模擬試験（もぎしけん）|11]]の答案（とうあん）を厳（きび）しく[[採点（さいてん）|18]]してくれた。疲（つか）れて机（つくえ）に伏（ふ）せた陽翔（はると）の横（よこ）で、そっと温（あたた）かいココアを置（お）いてくれる優（やさ）しさに、何度（なんど）励（はげ）まされたことだろう。",
                "Suốt một tháng sau đó, ngày nào Misaki cũng cầm bút đỏ sửa câu chữ cẩn thận cho bài tiểu luận của Haruto và chấm điểm khắt khe từng bài thi thử. Biết bao lần cậu được tiếp thêm sức mạnh bởi sự dịu dàng khi cô lặng lẽ đặt ly cacao nóng bên cạnh mỗi lúc cậu mệt rũ gục xuống bàn."
            ),
            (
                "そしてついに[[合否（ごうひ）|12]]発表（はっぴょう）の日（ひ）。スマホの画面（がめん）を見（み）た陽翔（はると）がガッツポーズをして叫（さけ）んだ。「受（う）かった！　美咲（みさき）、全部（ぜんぶ）合格（ごうかく）だ！」。「やったね！」と抱（だ）き合（あ）いそうになった瞬間（しゅんかん）、二人はハッとして顔（かお）を離（はな）し、図書館（としょかん）の静（しず）けさの中（なか）で照（て）れ臭（くさ）そうに笑（わら）い合（あ）った。",
                "Và cuối cùng ngày công bố kết quả đỗ trượt cũng tới. Nhìn màn hình điện thoại, Haruto giơ nắm đấm reo lên: 'Đỗ rồi! Misaki ơi, tớ đỗ hết cả rồi!'. 'Tuyệt quá!' — đúng khoảnh khắc hai đứa suýt ôm chầm lấy nhau, cả hai chợt giật mình lùi lại, nhìn nhau cười ngượng ngùng giữa không gian tĩnh lặng của thư viện."
            ),
        ],
        "quiz": [
            {
                "prompt": "提出（ていしゅつ）した小論文（しょうろんぶん）の表現（ひょうげん）を、先生（せんせい）に赤ペンで丁寧（ていねい）に（　　）してもらった。",
                "options": ["添削（てんさく）", "採点（さいてん）", "暗記（あんき）", "履修（りしゅう）"],
                "ans": 1,
                "right_exp": "💖 Chuẩn rồi em! Chỉnh sửa, góp ý câu chữ cho bài viết/tiểu luận là `添削（てんさく）`.",
                "wrong_exps": [
                    "Chính xác: `添削（てんさく）` = sửa bài viết, biên tập lại câu chữ.",
                    "`採点（さいてん）` là chấm điểm số (như chấm 80/100 điểm), không phải sửa câu chữ nhé.",
                    "`暗記（あんき）` là học thuộc lòng.",
                    "`履修（りしゅう）` là đăng ký theo học một môn học."
                ]
            },
            {
                "prompt": "大学（だいがく）を卒業（そつぎょう）するためには、必修（ひっしゅう）科目（かもく）の（　　）を全部（ぜんぶ）取（と）らなければならない。",
                "options": ["単位（たんい）", "校則（こうそく）", "講義（こうぎ）", "奨学金（しょうがくきん）"],
                "ans": 1,
                "right_exp": "💖 Quá chuẩn! Tín chỉ môn học đại học là `単位（たんい）` (`単位を取る`).",
                "wrong_exps": [
                    "Chính xác: `単位` = tín chỉ môn học.",
                    "`校則` là nội quy nhà trường.",
                    "`講義` là giờ giảng bài trên giảng đường.",
                    "`奨学金` là tiền học bổng."
                ]
            },
            {
                "prompt": "苦手（にがて）だったリスニングを、毎日（まいにち）（　　）よく練習（れんしゅう）して克服（こくふく）した。",
                "options": ["根気（こんき）", "推薦（すいせん）", "合否（ごうひ）", "基準（きじゅん）"],
                "ans": 1,
                "right_exp": "💖 Chuẩn xác! Cụm cố định `根気（こんき）よく` nghĩa là kiên trì nhẫn nại không bỏ cuộc.",
                "wrong_exps": [
                    "Chính xác: `根気よく` = kiên trì bền bỉ.",
                    "`推薦` là tiến cử giới thiệu.",
                    "`合否` là kết quả đỗ hay trượt.",
                    "`基準` là tiêu chuẩn, mức chuẩn."
                ]
            },
            {
                "prompt": "去年（きょねん）と比（くら）べると、今年（ことし）の成績（せいせき）は少（すこ）し（　　）いる。",
                "options": ["劣（おと）って", "専攻（せんこう）して", "参照（さんしょう）して", "応用（おうよう）して"],
                "ans": 1,
                "right_exp": "💖 Đúng rồi em! Kém hơn so với mức trước/người khác dùng `〜より劣（おと）る`.",
                "wrong_exps": [
                    "Chính xác: `劣（おと）る` = thua kém hơn.",
                    "`専攻する` là học chuyên ngành gì.",
                    "`参照する` là tham khảo tài liệu.",
                    "`応用する` là ứng dụng vào thực tế."
                ]
            },
            {
                "prompt": "陽翔（はると）が苦手（にがて）科目（かもく）を克服（こくふく）して合格（ごうかく）できた一番（いちばん）の支（ささ）えは何（なに）だったか。",
                "options": [
                    "美咲（みさき）が毎日（まいにち）添削（てんさく）や採点（さいてん）をしてくれ、温（あたた）かく励（はげ）まし続（つづ）けてくれたこと",
                    "蓮（れん）が代（か）わりにレポートを書（か）いて提出（ていしゅつ）してくれたこと",
                    "テストの問題（もんだい）がすべて暗記（あんき）だけで解（と）ける簡単（かんたん）なものだったこと",
                    "教授（きょうじゅ）の推薦（すいせん）で試験（しけん）を免除（めんじょ）されたこと"
                ],
                "ans": 1,
                "right_exp": "💖 Ấm áp ghê luôn! Nhờ có Misaki kiên nhẫn kèm cặp, chấm thi thử và động viên bằng ly cacao nóng mỗi ngày mà Haruto đã vượt qua chính mình đó!",
                "wrong_exps": [
                    "Chính xác: Sự đồng hành kiên nhẫn và dịu dàng của Misaki.",
                    "Không có chuyện nhờ người viết hộ bài đâu nha!",
                    "Haruto từng than rằng chỉ học thuộc lòng công thức thôi không đủ giải quyết phần suy luận.",
                    "Cậu vẫn phải tự ôn tập, thi thử và xem kết quả đỗ trượt trực tiếp trên điện thoại."
                ]
            },
        ]
    },
]
