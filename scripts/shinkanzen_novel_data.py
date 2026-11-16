# -*- coding: utf-8 -*-
"""
Cuốn Tiểu Thuyết Ngắn Tương Tác JLPT N2:
『東京（とうきょう）の小さな書斎（しょさい）』— Căn Phòng Đọc Nhỏ Giữa Lòng Tokyo (6 Chương)
Vận dụng trực tiếp hệ thống Từ Vựng & Ngữ Pháp chuẩn 5 cuốn Shinkanzen Master N2.
Mọi chữ Hán đều có Hiragana kế bên: 漢字（かんじ）.
Cú pháp đánh dấu từ Shinkanzen tự động phát sáng & mở bảng hướng dẫn khi click:
  [[từ_hiển_thị_có_hiragana|khoá_tra_Shinkanzen]]
  hoặc [[Từ（ひらがな）]] nếu phần chữ Hán trùng khớp khoá gốc.
"""

NOVEL_META = {
    "title_jp": "東京（とうきょう）の小さな書斎（しょさい）",
    "title_vi": "Căn Phòng Đọc Nhỏ Giữa Lòng Tokyo",
    "subtitle": "Tiểu thuyết ngắn 6 chương thực chiến JLPT N2 • Bấm vào từ vựng Shinkanzen trong truyện để bật sáng & xem bảng hướng dẫn chi tiết",
    "author_note": "Chào em, đây là cuốn tiểu thuyết nhỏ gồm 6 chương chị viết riêng cho em để ôn lại hàng loạt từ vựng và ngữ pháp vừa học trong bộ Shinkanzen Master N2. Toàn bộ chữ Hán đều có sẵn Hiragana đứng kế bên để em đọc trôi chảy không bị vấp. Khi bắt gặp bất kỳ từ nào nằm trong giáo trình Shinkanzen, em chỉ cần bấm vào từ đó — nó sẽ phát sáng rực lên và mở ra Bảng Hướng Dẫn chi tiết kèm âm Hán Việt, Collocation và đường dẫn tới đúng bài học gốc!",
}

NOVEL_CHAPTERS = [
    {
        "num": 1,
        "slug": "chuong-01",
        "title_jp": "第1章：旅立（たびだ）ちと最初（さいしょ）の言葉遣（ことばづか）い",
        "title_vi": "Chương 01: Chuyến Khởi Hành & Bài Học Về Ngôn Từ Đầu Tiên",
        "yuki_tip": "Chương mở đầu đưa em theo chân Haruto rời quê lên Tokyo nhận việc tại một nhà xuất bản nhỏ ở phố sách Jimbocho. Hãy chú ý các từ thuộc **Chương 1 (Con người, Tính cách, Lễ nghi)** và **Chương 5 (Công việc)** của Shinkanzen N2 nhé!",
        "paragraphs": [
            (
                "十月（じゅうがつ）の晴（は）れた朝（あさ）、陽翔（はると）は[[実家（じっか）]]の玄関（げんかん）で荷造（にづく）りを終（お）え、深（ふか）く息（いき）を吸（す）い込（こ）んだ。",
                "Vào một buổi sáng tháng Mười trời quang mây tạnh, Haruto đóng gói hành lý xong xuôi ngay trước tiền sảnh nhà bố mẹ đẻ rồi hít một hơi thật sâu."
            ),
            (
                "地方（ちほう）の大学（だいがく）を卒業（そつぎょう）して、ようやく念願（ねんがん）の出版社（しゅっぱんしゃ）に[[就職（しゅうしょく）する|就職する]]ことになったのだ。しかし、一人（ひとり）で都会（とかい）に出（で）る[[に際（さい）して|に際して]]、胸（むね）の奥（おく）が緊張（きんちょう）でどきどきし[[てたまらなかった|てしかたがない]]。",
                "Tốt nghiệp đại học ở tỉnh lẻ, cậu cuối cùng cũng vào làm tại một nhà xuất bản đúng như ước nguyện. Thế nhưng, nhân dịp một mình lên thành phố lớn, tận sâu trong lồng ngực cậu hồi hộp căng thẳng không sao kìm nổi."
            ),
            (
                "「陽翔（はると）、体（からだ）に気（き）をつけて。立派（りっぱ）に働（はたら）いて、たまには顔（かお）を見（み）せなさいよ」",
                "\"Haruto này, nhớ giữ gìn sức khỏe nhé. Làm việc cho thật chững chạc rồi thỉnh thoảng về thăm bố mẹ đấy.\""
            ),
            (
                "両親（りょうしん）の見送（みおく）りを受（う）けながら、陽翔（はると）は「いつかきっと[[親孝行（おやこうこう）]]をしよう」と心（こころ）に誓（ちか）った。駅（えき）へ急（いそ）ぐ途中（とちゅう）、以前（いぜん）から親（した）しい[[友人（ゆうじん）]]や、近所（きんじょ）の[[知（し）り合（あ）い|知り合い]]たちにも優（やさ）しく[[励（はげ）まされた|励ます]]。",
                "Nhận lời tiễn chân của cha mẹ, Haruto tự nhủ trong lòng nhất định có ngày sẽ báo hiếu. Trên đường vội ra ga, cậu cũng được người bạn thân từ trước và cả những người quen hàng xóm dịu dàng động viên."
            ),
            (
                "東京（とうきょう）の神保町（じんぼうちょう）にある小（ちい）さな出版社（しゅっぱんしゃ）へ着（つ）くと、そこには[[先（さき）に入（はい）った|先輩]]の梨花（りか）[[先輩（せんぱい）|先輩]]が待（ま）っていた。彼女（かのじょ）は仕事（しごと）に対してとても[[積極的（せっきょくてき）]]で、頼（たよ）りになる存在（そんざい）だ。",
                "Khi tới nhà xuất bản nhỏ nằm ở phố Jimbocho, Tokyo, tiền bối Rika đã chờ sẵn ở đó. Chị ấy là một người rất tích cực với công việc và vô cùng đáng tin cậy."
            ),
            (
                "「ようこそ！ この職場（しょくば）では、お客様（きゃくさま）や取引先（とりひきさき）に対する丁寧（ていねい）な[[言葉遣（ことばづか）い]]と[[態度（たいど）]]がとても大切（たいせつ）なのよ。それに、どんな小（ちい）さな[[約束（やくそく）を守（まも）る|約束を守る]]ことが信用（しんよう）につながるわ」",
                "\"Chào mừng em! Ở nơi làm việc này, cách dùng từ lịch sự và thái độ đối với khách hàng hay đối tác quan trọng lắm đấy. Hơn nữa, giữ đúng dù chỉ một lời hứa nhỏ xíu thôi cũng sẽ xây dựng nên lòng tin.\""
            ),
            (
                "「はい！ まだ[[不器用（ぶきよう）]]ですが、一日（いちにち）も早（はや）く慣（な）れるよう精一杯（せいいっぱい）努力（どりょく）します」",
                "\"Dạ vâng! Em vẫn còn hơi vụng về, nhưng em sẽ nỗ lực hết sức để làm quen nhanh nhất có thể ạ.\""
            ),
            (
                "[[緊張（きんちょう）]]のあまり少（すこ）し硬（かた）くなっていた陽翔（はると）を見て、[[上司（じょうし）]]である高橋（たかはし）[[部長（ぶちょう）|上司]]も笑顔（えがお）で迎（むか）えてくれた。「東京（とうきょう）での生活（せいかつ）が陽翔（はると）くんを大きく成長（せいちょう）させてくれる[[に違（ちが）いない|に違いない]]」と声をかけてもらい、不安（ふあん）だった気持ちが少（すこ）し[[ほっとした|ほっとする]]のだった。",
                "Nhìn Haruto căng thẳng đến mức hơi cứng người lại, sếp trực tiếp là trưởng phòng Takahashi cũng mỉm cười chào đón cậu. Được sếp nhắn nhủ 'Cuộc sống ở Tokyo chắc chắn sẽ giúp cậu trưởng thành vượt bậc', tâm trạng lo âu ban đầu của cậu chợt thấy nhẹ nhõm hẳn đi."
            ),
        ],
        "quiz": [
            (
                "陽翔（はると）が実家（じっか）を出発（しゅっぱつ）するとき、なぜ緊張（きんちょう）していたのか。",
                [
                    "両親（りょうしん）に反対（はんたい）されて家（いえ）を出（で）たから",
                    "初（はじ）めて一人（ひとり）で都会（とかい）の出版社（しゅっぱんしゃ）で働（はたら）く新生活（しんせいかつ）に際（さい）して不安（ふあん）と期待（きたい）があったから",
                    "大学（だいがく）の単位（たんい）が足（た）りなくて卒業（そつぎょう）できなかったから",
                    "知（し）り合（あ）いが誰（だれ）も応援（おうえん）してくれなかったから"
                ],
                2,
                "Đoạn 2 nói rõ cậu vừa tốt nghiệp ĐH và vào làm ở NXB mơ ước nhưng `一人で都会に出るに際して、緊張でどきどきしてたまらなかった`."
            ),
            (
                "梨花（りか）先輩（せんぱい）は職場（しょくば）で何（なに）がいちばん大切（たいせつ）だと教（おし）えたか。",
                [
                    "毎日（まいにち）残業（ざんぎょう）して早（はや）く昇進（しょうしん）すること",
                    "丁寧（ていねい）な言葉遣（ことばづか）い・態度（たいど）と、小（ちい）さな約束（やくそく）を守（まも）ること",
                    "上司（じょうし）とはあまり話（はな）さず消極的（しょうきょくてき）に作業（さぎょう）すること",
                    "友人（ゆうじん）とだけ仕事（しごと）の相談（そうだん）をすること"
                ],
                2,
                "Lời khuyên trực tiếp của Rika ở đoạn 6: nhấn mạnh `丁寧な言葉遣いと態度` và `小さな約束を守ることが信用につながる`."
            ),
            (
                "本文（ほんぶん）の「[[親孝行（おやこうこう）]]」の意味（いみ）として最（もっと）も適切（てきせつ）なものはどれか。",
                [
                    "親（おや）に迷惑（めいわく）をかけること",
                    "両親（りょうしん）を大切（たいせつ）にして喜（よろこ）ばせること",
                    "遠（とお）い親戚（しんせき）の家（いえ）に引（ひ）っ越（こ）すこと",
                    "先輩（せんぱい）にお辞儀（じぎ）をすること"
                ],
                2,
                "親孝行（おやこうこう — THÂN HIẾU HÀNH）: hiếu thảo, chăm sóc làm cha mẹ vui lòng (Shinkanzen 1章1課)."
            ),
        ]
    },
    {
        "num": 2,
        "slug": "chuong-02",
        "title_jp": "第2章：[[几帳面（きちょうめん）]]な先輩（せんぱい）と[[頑固（がんこ）]]な店主（てんしゅ）",
        "title_vi": "Chương 02: Tiền Bối Tỉ Mỉ & Ông Chủ Tiệm Sách Bảo Thủ",
        "yuki_tip": "Sang Chương 2, Haruto đối mặt với công việc biên tập thực tế (`編集する・打ち合わせ`) và các tính cách trái ngược (`几帳面` ⇄ `そそっかしい`, `頑固`, `謙虚`) cùng động từ đa nghĩa ở Phần 2 Shinkanzen!",
        "paragraphs": [
            (
                "入社（にゅうしゃ）から一週間（いっしゅうかん）。陽翔（はると）は毎日（まいにち）記事（きじ）の[[編集（へんしゅう）する|編集する]]作業（さぎょう）や先輩（せんぱい）との[[打（う）ち合（あ）わせ|打ち合わせ]]に追（お）われていた。",
                "Một tuần sau khi vào công ty. Haruto ngày nào cũng quay cuồng với việc biên tập bài viết và các buổi họp trao đổi cùng tiền bối."
            ),
            (
                "梨花（りか）先輩（せんぱい）はとても[[几帳面（きちょうめん）]]な性格（せいかく）で、漢字（かんじ）の間違（まちが）いや誤字（ごじ）を一つも許（ゆる）さない。一方（いっぽう）、[[そそっかしい]]ところがある陽翔（はると）は、[[うっかり]]句読点（くとうてん）を抜（ぬ）かしてしまい、何度も[[書（か）き直（なお）す|書き直す]]ことになった。",
                "Chị tiền bối Rika có tính cách rất ngăn nắp tỉ mỉ, không bỏ sót dù chỉ một lỗi chính tả hay sai chữ Hán. Ngược lại, Haruto vốn có chút hấp tấp nên lỡ quên mất dấu chấm câu, đành phải viết lại bao nhiêu lần."
            ),
            (
                "「ほら、また誤字（ごじ）！ 読者（どくしゃ）に誤解（ごかい）を与（あた）えないよう、細（こま）かい点（てん）にも[[注意（ちゅうい）を払（はら）う|払う]]べきよ。原稿（げんこう）を丁寧（ていねい）に[[見直（みなお）す|見直す]]習慣（しゅうかん）をつけなさい」",
                "\"Đây này, lại sai chữ rồi! Để không gây hiểu lầm cho độc giả, em phải hết sức chú ý tới cả những chi tiết nhỏ nhất chứ. Hãy tập thói quen rà soát lại bản thảo cẩn thận nhé.\""
            ),
            (
                "その日（ひ）の午後（ごご）、陽翔（はると）は街（まち）で長年（ながねん）古本屋（ふるほんや）を営（いとな）む黒沢（くろさわ）さんの店（みせ）へ[[取材（しゅざい）する|取材する]]ために[[足（あし）を運（はこ）んだ|足を運ぶ]]。しかし、黒沢（くろさわ）さんは[[頑固（がんこ）]]な職人気質（しょくにんかたぎ）で、最初（さいしょ）はインタビュ—を断（ことわ）ろうとした。",
                "Chiều hôm đó, Haruto cất công ghé tới tiệm sách cổ lâu năm của ông Kurosawa để lấy tin phỏng vấn. Tuy nhiên, ông Kurosawa mang khí chất nghệ nhân rất cứng đầu bảo thủ, ban đầu định từ chối cuộc phỏng vấn."
            ),
            (
                "「雑誌（ざっし）に載（の）せるなんざ、わしは興味（きょうみ）ないね。ネットの時代（じだい）に本（ほん）の良（よ）さなんて伝（つた）わるわけがない」",
                "\"Đăng lên tạp chí gì đó thì lão không hứng thú đâu. Thời đại internet thế này làm sao truyền tải hết được cái hay của sách chứ.\""
            ),
            (
                "陽翔（はると）は落（お）ち込（こ）んだが、ここで諦（あきら）め[[ざるを得（え）ない|〜ざるを得ない]]とは思（おも）いたくなかった。店（みせ）を回（まわ）って古書（こしょ）の手触（てざわ）りや店主（てんしゅ）の並（なら）べ方（かた）の工夫（くふう）を[[謙虚（けんきょ）]]な姿勢（しせい）で学（まな）び[[つつ|〜つつ]]、毎日（まいにち）店（みせ）へ通（かよ）って店主（てんしゅ）の話（はなし）に耳（みみ）を傾（かたむ）けた。",
                "Haruto hụt hẫng lắm, nhưng cậu không muốn đành phải bỏ cuộc ngay lúc này. Vừa học hỏi cách bài trí tinh tế và chất giấy sách cổ với thái độ khiêm nhường, cậu vừa ghé tiệm mỗi ngày để lắng nghe câu chuyện của ông chủ."
            ),
            (
                "「君（きみ）は若（わか）いのに[[話（はなし）の筋（すじ）が通（とお）っている|通る]]し、本当（ほんとう）に本（ほん）を愛（あい）しているんだな。いいだろう、明日（あした）正式（せいしき）にインタビューに応（おう）じよう」",
                "\"Cậu tuy trẻ nhưng lập luận rất rành mạch có lý, lại thực sự yêu sách đấy nhỉ. Được rồi, ngày mai ta sẽ chính thức nhận lời phỏng vấn.\""
            ),
            (
                "予想外（よそうがい）の承諾（しょうだく）に、陽翔（はると）は驚（おどろ）いて[[目（め）を丸（まる）くした|目を丸くする]]。帰（かえ）って梨花（りか）先輩（せんぱい）に報告（ほうこく）すると、「粘（ねば）り強（づよ）く熱意（ねつい）を伝（つた）えた結果（けっか）ね。[[頭（あたま）が下（さ）がる|頭が下がる]]わ」と心（こころ）から褒（ほ）めてくれたのだった。",
                "Trước sự đồng ý ngoài dự đoán, Haruto kinh ngạc mở to tròn đôi mắt. Về kể lại với chị Rika, chị ấy khen hết lời: 'Đó là kết quả của việc em kiên trì truyền đạt nhiệt huyết đấy. Chị thực sự khâm phục em luôn'."
            ),
        ],
        "quiz": [
            (
                "黒沢（くろさわ）さんが最初（さいしょ）、雑誌（ざっし）の取材（しゅざい）を断（ことわ）った理由（りゆう）は何（なに）か。",
                [
                    "陽翔（はると）の言葉遣（ことばづか）いが悪（わる）かったから",
                    "ネットの時代（じだい）に本（ほん）の良（よ）さは簡単（かんたん）には伝（つた）わらないと思（おも）っていたから",
                    "店（みせ）の掃除（そうじ）で忙（いそが）しくて時間（じかん）がなかったから",
                    "梨花（りか）先輩（せんぱい）と以前（いぜん）けんかをしたことがあったから"
                ],
                2,
                "Đoạn 5: `ネットの時代に本の良さなんて伝わるわけがない`."
            ),
            (
                "陽翔（はると）はどうやって黒沢（くろさわ）さんの心（こころ）を動（うご）かしたか。",
                [
                    "高い（たかい）お金（かね）を払（はら）ってインタビューを買（か）った",
                    "古本屋（ふるほんや）の工夫（くふう）を謙虚（けんきょ）に学（まな）びつつ毎日（まいにち）通（かよ）って話（はなし）を聞（き）いた",
                    "他の店（みせ）と比較（ひかく）して黒沢（くろさわ）さんを非難（ひなん）した",
                    "上司（じょうし）を連（つ）れて無理（むり）やり頼（たの）み込（こ）んだ"
                ],
                2,
                "Đoạn 6: Cậu giữ thái độ `謙虚な姿勢で学びつつ` và kiên trì tới lắng nghe hàng ngày."
            ),
            (
                "「[[目（め）を丸（まる）くする|目を丸くする]]」と同じ意味（いみ）の表現（ひょうげん）はどれか。",
                [
                    "とても眠（ねむ）くなる",
                    "ひどく驚（おどろ）く",
                    "怒（おこ）って泣（な）き出（だ）す",
                    "わざと見（み）ないふりをする"
                ],
                2,
                "Thành ngữ cơ thể Shinkanzen `第2部 6章 1課`: 目を丸くする = Tròn mắt kinh ngạc sửng sốt."
            ),
        ]
    },
    {
        "num": 3,
        "slug": "chuong-03",
        "title_jp": "第3章：雨（あめ）の夜（よる）、[[肩（かた）の荷（に）が下（お）りる|肩の荷が下りる]]瞬間（しゅんかん）",
        "title_vi": "Chương 03: Đêm Mưa & Khoảnh Khắc Trút Bỏ Gánh Nặng",
        "yuki_tip": "Chương 3 tập trung vào nhóm thành ngữ **慣用表現 (第2部 6章)**, **từ tượng thanh オノマトペ (第2部 5章)** và từ vựng xử lý sự cố (`渋滞`・`実施する`・`助け合う`・`考え抜く`)!",
        "paragraphs": [
            (
                "いよいよ書店（しょてん）イベントの前日（ぜんじつ）になった。しかし、[[生憎（あいにく）|生憎]]の大雨（おおあめ）で配送（はいそう）トラックが高速道路（こうそくどうろ）の[[渋滞（じゅうたい）|渋滞]]に巻（ま）き込（こ）まれ、新刊（しんかん）の到着（とうちゃく）が遅（おく）れるという連絡（れんらく）が入（はい）ったのだ。",
                "Cuối cùng cũng tới ngày trước sự kiện hội sách. Ấy thế mà trớ trêu thay trời lại đổ mưa lớn khiến xe tải giao hàng kẹt cứng trên cao tốc, văn phòng nhận được tin báo lô sách mới sẽ bị giao trễ."
            ),
            (
                "もし明朝（みょうちょう）までに届（とど）かなければ、イベントを[[延期（えんき）する|延期する]]ことになり[[かねない|〜かねない]]。陽翔（はると）は[[気（き）が気（き）じゃない|気が気じゃない]]状態（じょうたい）で、[[頭（あたま）を抱（かか）えて|頭を抱える]]いた。",
                "Nếu không tới kịp trước sáng mai, e rằng sự kiện sẽ có nguy cơ phải hoãn lại mất. Haruto đứng ngồi không yên, ôm đầu lo lắng tột độ."
            ),
            (
                "「落（お）ち着（つ）いて、陽翔（はると）くん！ こんな時（とき）こそ[[仕事（しごと）仲間（なかま）|仕事仲間]]で[[助（たす）け合（あ）う|助け合う]]番（ばん）よ」",
                "\"Bình tĩnh nào Haruto! Chính những lúc thế này mới là lúc đồng nghiệp chúng ta hỗ trợ lẫn nhau đấy.\""
            ),
            (
                "梨花（りか）先輩（せんぱい）は[[直（ただ）ちに|直ちに]]印刷所（いんさつじょ）の[[顔（かお）が広（ひろ）い|顔が広い]]知人（ちじん）に連絡（れんらく）を取（と）って代替（だいたい）便（びん）を手配（てはい）してくれた。また、会場（かいじょう）スタッフの美咲（みさき）さんは[[気（き）が利（き）く|気が利く]]女性（じょせい）で、濡（ぬ）れた社員（しゃいん）のために素早（すばや）くタオルと温（あたた）かいお茶（ちゃ）を用意（ようい）してくれた。",
                "Chị Rika lập tức liên hệ với một người quen có mối quan hệ rộng bên xưởng in để điều phối chuyến xe thay thế. Còn chị Misaki bên tổ hậu cần là người vô cùng tinh tế biết ý, đã nhanh chóng chuẩn bị sẵn khăn khô và trà nóng cho mọi người đang ướt mưa."
            ),
            (
                "みんなで解決策（かいけつさく）を[[考（かんが）え抜（ぬ）いた|考え抜く]][[末（すえ）に|〜末に]]、真夜中（まよなか）の二時（にじ）、ようやく荷物（にもつ）が無事（ぶじ）に会場（かいじょう）へ運（はこ）び込（こ）まれた。",
                "Sau khi mọi người vắt óc suy nghĩ tìm giải pháp, vào lúc hai giờ sáng, cuối cùng thùng sách cũng được chuyển an toàn vào hội trường."
            ),
            (
                "翌日（よくじつ）、青空（あおぞら）の下（もと）でブックイベントは無事（ぶじ）に[[実施（じっし）され|実施する]]、予想（よそう）を大きく[[上回（うわまわ）る|上回る]]来場者（らいじょうしゃ）で賑（にぎ）わった。大成功（だいせいこう）に終（お）わった帰り道（かえりみち）、みんな大きな仕事（しごと）を終（お）えて[[肩（かた）の荷（に）が下（お）りた|肩の荷が下りる]]ように[[ほっとした|ほっとする]]表情（ひょうじょう）を浮（う）かべていた。",
                "Hôm sau, dưới bầu trời xanh ngắt, sự kiện sách diễn ra suôn sẻ và tấp nập khách ghé thăm vượt xa mức dự đoán ban đầu. Trên đường về sau thành công rực rỡ, gương mặt ai nấy đều ánh lên vẻ nhẹ nhõm như vừa trút được gánh nặng lớn trên vai."
            ),
            (
                "「みんなと[[協力（きょうりょく）|労働・協力]]した[[おかげで|〜おかげで]]、最高（さいこう）の一日（いちにち）になった[[ばかりでなく|〜ばかりでなく]]、チームワークの大切（たいせつ）さも心（こころ）から学（まな）ぶことができた」――陽翔（はると）は帰宅後（きたくご）、安心（あんしん）して[[ぐっすり]]眠（ねむ）りについた。",
                "\"Nhờ hợp tác cùng mọi người, hôm nay không chỉ trở thành một ngày tuyệt vời nhất, mà mình còn học được từ tận đáy lòng giá trị của tinh thần đồng đội.\" Sau khi về nhà, Haruto yên tâm chìm vào giấc ngủ thật say."
            ),
        ],
        "quiz": [
            (
                "トラックが遅（おく）れたトラブルを、陽翔（はると）たちはどうやって乗り越（のりこ）えたか。",
                [
                    "イベントを来週（らいしゅう）に延期（えんき）して対応（たいおう）した",
                    "全員（ぜんいん）で役割（やくわり）を分担（ぶんたん）し、代替（だいたい）便（びん）の手配（てはい）などで協力（きょうりょく）し合った",
                    "陽翔（はると）一人（ひとり）で夜中（よなか）まで荷物（にもつ）を取り（とり）に行（い）った",
                    "印刷（いんさつ）会社（がいしゃ）に苦情（くじょう）の電話（でんわ）をして諦（あきら）めた"
                ],
                2,
                "Chị Rika nhờ người quen điều xe thay thế, Misaki chăm sóc hậu cần, mọi người cùng nghĩ cách và hợp lực (`助け合う`)."
            ),
            (
                "本文中（ほんぶんちゅう）の「[[気（き）が利（き）く|気が利く]]」は美咲（みさき）さんのどんな行動（こうどう）を指（さ）しているか。",
                [
                    "計算（けいさん）を間違（まちが）えずに速（はや）く終（お）わらせたこと",
                    "雨（あめ）に濡（ぬ）れた仲間（なかま）を思（おも）いやり、言（い）われる前（まえ）にタオルとお茶（ちゃ）を用意（ようい）したこと",
                    "トラックの運転手（うんてんしゅ）と交渉（こうしょう）したこと",
                    "たくさんの雑誌（ざっし）を棚（たな）に並（なら）べたこと"
                ],
                2,
                "気が利く (Shinkanzen 第2部6章2課): tinh ý, nhanh nhạy thấu hiểu để giúp trước khi người khác kịp nhờ."
            ),
            (
                "次（つぎ）のうち、イベントの結果（けっか）と合（あ）っているものはどれか。",
                [
                    "来場者（らいじょうしゃ）は予定（よてい）を下回（したまわ）った",
                    "新刊（しんかん）はイベント終了後（しゅうりょうご）に届（とど）いた",
                    "来場者（らいじょうしゃ）が予想（よそう）を上回（うわまわ）り、大成功（だいせいこう）だった",
                    "陽翔（はると）は疲れ（つか）て夜（よる）もろくに眠（ねむ）れなかった"
                ],
                3,
                "`予想を大きく上回る来場者で賑わった` và tối về cậu ngủ say `ぐっすり眠りについた`."
            ),
        ]
    },
    {
        "num": 4,
        "slug": "chuong-04",
        "title_jp": "第4章：新（あたら）しい[[食生活（しょくせいかつ）]]とやり繰（く）りの知恵（ちえ）",
        "title_vi": "Chương 04: Nếp Sống Tự Lập & Bí Quyết Cân Bằng Ở Tokyo",
        "yuki_tip": "Chương 4 ôn lại toàn bộ từ vựng **Chương 2 (Ăn uống, Việc nhà, Sức khỏe)** và các **Phó từ (`第2部 4章`: 漸く, すっかり, 却って, 思い切って, さっぱり)** rất hay gặp trong bài đục lỗ JLPT!",
        "paragraphs": [
            (
                "イベントを終（お）えた翌月（よくげつ）、陽翔（はると）は会社（かいしゃ）の近（ちか）くへ引（ひ）っ越（こ）すことにした。毎朝（まいあさ）の満員（まんいん）電車（でんしゃ）から解放（かいほう）され、時間（じかん）が経（た）つ[[につれて|〜につれて]]東京（とうきょう）の暮（く）らしにも[[すっかり]]慣（な）れてきた。",
                "Sang tháng sau khi sự kiện khép lại, Haruto quyết định chuyển nhà đến gần công ty hơn. Giải thoát khỏi cảnh tàu điện đông đúc mỗi sáng, càng theo thời gian cậu càng quen hẳn với cuộc sống Tokyo."
            ),
            (
                "ただ、一人（ひとり）暮（ぐ）らしを始（はじ）めた[[当初（とうしょ）]]は、[[外食（がいしょく）]]ばかり続（つづ）けていたせいで[[栄養（えいよう）]]バランスが偏（かたよ）り、[[体調（たいちょう）]]を崩（くず）しかけたことがあった。お財布（さいふ）の[[やり繰（く）り|やり繰り]]も楽（らく）ではなかった。",
                "Chỉ là thời gian đầu mới sống một mình, do suốt ngày ăn ngoài hàng nên cân bằng dinh dưỡng bị lệch và cậu suýt thì đổ bệnh. Việc xoay xở chi tiêu ví tiền cũng chẳng dễ dàng chút nào."
            ),
            (
                "「毎日（まいにち）コンビニ弁当（べんとう）じゃお金（かね）がかかるし、[[却（かえ）って|却って]]疲（つか）れが取（と）れないわよ。簡単（かんたん）な[[自炊（じすい）]]から始（はじ）めてみたら？」と梨花（りか）先輩（せんぱい）が勧（すす）めてくれた。",
                "\"Ngày nào cũng cơm hộp cửa hàng tiện lợi vừa tốn tiền, trái lại còn chẳng tan hết mệt đâu. Hay em thử bắt đầu tự nấu mấy món đơn giản xem?\" — chị Rika khuyên cậu."
            ),
            (
                "そこで陽翔（はると）は[[思（おも）い切（き）って|思い切って]]休（やす）みの日（ひ）にフライパンと[[調味料（ちょうみりょう）]]を一式（いっしき）買（か）い揃（そろ）えた。スーパーで安（やす）い食材（しょくざい）を[[買（か）い出（だ）し|買い出し]]し、皮（かわ）をむいて[[刻（きざ）む|刻む]]ことから挑戦（ちょうせん）した。",
                "Thế là Haruto quyết định dứt khoát mua trọn bộ chảo rán và gia vị vào ngày nghỉ. Cậu đi siêu thị mua sắm thực phẩm giá rẻ, tập tành từ việc gọt vỏ đến thái nhỏ rau củ."
            ),
            (
                "最初（さいしょ）は[[手際（てぎわ）]]が悪（わる）くてキッチンが[[散（ち）らかった|散らかる]]ばかりだったが、週末（しゅうまつ）ごとに部屋（へや）を[[片付（かたづ）けて|片付ける]][[整理（せいり）する|整理する]]うちに、[[漸（ようや）く|漸く]]手際（てぎわ）よく[[献立（こんだて）]]を作（つく）れるようになった。",
                "Lúc đầu thao tác còn lóng ngóng khiến căn bếp chỉ toàn bày bừa, nhưng nhờ mỗi cuối tuần dọn dẹp sắp xếp lại phòng, dần dần rốt cuộc cậu cũng biết lên thực đơn gọn gàng nhanh tay hơn hẳn."
            ),
            (
                "自分（じぶん）で作（つく）った野菜（やさい）たっぷりの味噌汁（みそしる）を飲（の）むと、体（からだ）が温（あたた）まって気分（きぶん）も[[すっきり]]する。[[外食（がいしょく）]]を減（へ）らして健康（けんこう）を[[維持（いじ）する|維持する]][[一方（いっぽう）で|〜一方で]]、食費（しょくひ）も[[大幅（おおはば）に|減少・増加]]抑（おさ）えられるようになったのである。",
                "Uống bát canh miso đầy rau củ do chính tay mình nấu, cơ thể ấm áp lên mà tinh thần cũng sảng khoái hẳn. Một mặt giảm ăn ngoài để duy trì sức khỏe, mặt khác cậu còn tiết giảm được đáng kể tiền ăn uống."
            ),
        ],
        "quiz": [
            (
                "陽翔（はると）が自炊（じすい）を始（はじ）めようと決意（けつい）した直接（ちょくせつ）のきっかけは何（なに）か。",
                [
                    "料理（りょうり）番組（ばんぐみ）を見（み）てシェフになりたくなったから",
                    "外食（がいしょく）ばかりで栄養（えいよう）バランスとお金（かね）に困（こま）り、先輩（せんぱい）に勧（すす）められたから",
                    "近所（きんじょ）にレストランが1軒（いっけん）もなくなったから",
                    "会社（かいしゃ）の食堂（しょくどう）が休（やす）みになったから"
                ],
                2,
                "Đoạn 2 & 3: Do ăn ngoài (`外食`) làm hỏng `栄養バランス` và tốn tiền (`やり繰り`), cộng thêm lời khuyên của Rika."
            ),
            (
                "自炊（じすい）を続（つづ）けたことで、陽翔（はると）の生活（せいかつ）はどう変化（へんか）したか。",
                [
                    "食費（しょくひ）は増（ふ）えたが、料理（りょうり）の手際（てぎわ）は良（よ）くなった",
                    "キッチンがさらに散（ち）らかるようになった",
                    "健康（けんこう）を維持（いじ）できる一方で、食費（しょくひ）の節約（せつやく）にもなった",
                    "体調（たいちょう）を崩（くず）して休（やす）むことが増（ふ）えた"
                ],
                3,
                "Đoạn cuối sử dụng `〜一方で` nối 2 mặt lợi song hành: giữ sức khỏe & tiết kiệm chi tiêu."
            ),
            (
                "「[[漸（ようや）く|漸く]]作（つく）れるようになった」の「漸く（ようやく）」と近（ちか）い意味（いみ）はどれか。",
                [
                    "まったく〜ない",
                    "苦労（くろう）の末（すえ）にとうとう",
                    "思（おも）わずうっかり",
                    "あらかじめ前（まえ）もって"
                ],
                2,
                "漸く（ようやく）: cuối cùng thì cũng / phải vất vả mãi mới... (Shinkanzen 第2部 4章 1課)."
            ),
        ]
    },
    {
        "num": 5,
        "slug": "chuong-05",
        "title_jp": "第5章：デジタルの波（なみ）と[[伝統（でんとう）]]の[[価値（かち）|価値・構造]]",
        "title_vi": "Chương 05: Làn Sóng Số Hóa & Giá Trị Truyền Thống",
        "yuki_tip": "Chương 5 bước vào thế giới **Xã hội & Truyền thông (Chương 6 & 7 Shinkanzen)** — chủ đề tranh luận `紙の本 vs 電子書籍` siêu kinh điển trong cả phần Đọc hiểu lẫn Nghe hiểu JLPT N2!",
        "paragraphs": [
            (
                "半年後（はんとしご）、社内（しゃない）会議（かいぎ）である大（おお）きな企画（きかく）が持（も）ち上（あ）がった。コストを[[削減（さくげん）する|削減する]]ため、紙（かみ）の本（ほん）の[[出版（しゅっぱん）する|出版する]]をやめて、すべて電子（でんし）版（ばん）へ移行（いこう）しようという案（あん）だった。",
                "Nửa năm sau, một dự án lớn được đưa ra trong cuộc họp công ty. Đó là phương án ngừng xuất bản sách giấy để chuyển toàn bộ sang bản điện tử nhằm cắt giảm chi phí."
            ),
            (
                "「今（いま）は若者（わかもの）を中心（ちゅうしん）にスマートフォンが[[普及（ふきゅう）|開発する]]し、情報（じょうほう）もすぐ画面（がめん）で見（み）られる。時代（じだい）の流れ（ながれ）に[[乗（の）る|乗る]]べきだ」という意見（いけん）が多（おお）かった。",
                "Nhiều ý kiến cho rằng hiện nay smartphone đã phổ cập trong giới trẻ, thông tin cũng xem ngay được trên màn hình nên cần bắt kịp dòng chảy thời đại."
            ),
            (
                "しかし、陽翔（はると）は黒沢（くろさわ）さんの古本屋（ふるほんや）で触（ふ）れた紙（かみ）の本（ほん）の温（ぬく）もりを思（おも）い出（だ）した。コストが[[厳しい（きび）しい|厳しい]]現状（げんじょう）[[にもかかわらず|〜にもかかわらず]]、老舗（しにせ）の[[伝統（でんとう）]]を守（まも）りながら新（あたら）しい[[技術革新（ぎじゅつかくしん）]]を取り入（とりい）れる方法（ほうほう）があるはずだと[[考（かんが）え抜（ぬ）いた|考え抜く]]。",
                "Thế nhưng Haruto nhớ lại hơi ấm của những cuốn sách giấy từng chạm vào tại tiệm sách cổ ông Kurosawa. Dù thực trạng chi phí đang khắc nghiệt, cậu vắt óc suy nghĩ rằng chắc chắn phải có cách vừa giữ gìn truyền thống vừa kết hợp đổi mới công nghệ."
            ),
            (
                "陽翔（はると）は徹夜（てつや）で[[資料（しりょう）|提出する]]を[[作成（さくせい）する|作成する]]し、翌日（よくじつ）の会議（かいぎ）で堂々（どうどう）とプレゼンを行（おこな）った。",
                "Haruto thức trắng đêm lập tài liệu và tự tin thuyết trình đàng hoàng trước cuộc họp ngày hôm sau."
            ),
            (
                "「電子版（でんしばん）の便利（べんり）さは[[極（きわ）めて|極めて]]大き（おお）いが、紙（かみ）の本（ほん）にはページをめくる歓（よろこ）びと[[深（ふか）い|深い・浅い]]思索（しさく）の時間（じかん）があります。そこで、少部数（しょうぶすう）の美（うつく）しい紙（かみ）の書籍（しょせき）に、学習（がくしゅう）用（よう）のQRコード付（つ）き電子（でんし）ガイドを組み合わせるハイブリッド企画（きかく）を[[提案（ていあん）|選択する]]します！」",
                "\"Sự tiện lợi của bản điện tử vô cùng to lớn, nhưng sách giấy có niềm vui lật trang và khoảng thời gian suy tư sâu lắng. Vì vậy, tôi xin đề xuất dự án kết hợp: sách giấy in đẹp số lượng giới hạn đi kèm hướng dẫn điện tử qua mã QR!\""
            ),
            (
                "会議室（かいぎしつ）が静（しず）まり返（かえ）ったあと、いつも厳（きび）しい高橋（たかはし）部長（ぶちょう）が「よく[[調（しら）べ抜（ぬ）いた|走り抜く]]な。これならデジタル派（は）も紙（かみ）派（は）も[[納得（なっとく）|一致する]]できる画期的（かっきてき）なアイデアだ！」と賛成（さんせい）してくれた。",
                "Sau giây phút phòng họp im phăng phắc, trưởng phòng Takahashi vốn hay nghiêm khắc lại gật đầu tán thành: 'Cậu tìm hiểu thấu đáo lắm! Như thế này thì cả phe kỹ thuật số lẫn phe yêu sách giấy đều có thể tâm phục khẩu phục. Đúng là ý tưởng mang tính bước ngoặt!'."
            ),
        ],
        "quiz": [
            (
                "会社（かいしゃ）の会議（かいぎ）で最初（さいしょ）に出（だ）された案（あん）はどのようなものだったか。",
                [
                    "すべての本（ほん）を伝統的（でんとうてき）な和紙（わし）で印刷（いんさつ）する案（あん）",
                    "コスト削減（さくげん）のため、紙（かみ）の本（ほん）をやめて電子版（でんしばん）のみにする案（あん）",
                    "黒沢（くろさわ）さんの古本屋（ふるほんや）を買収（ばいしゅう）する案（あん）",
                    "海外（かいがい）への輸出（ゆしゅつ）を完全に停止（ていし）する案（あん）"
                ],
                2,
                "Đoạn 1: `コストを削減するため、紙の本の出版をやめて、すべて電子版へ移行しようという案だった`."
            ),
            (
                "陽翔（はると）が会議（かいぎ）で提案（ていあん）した新（あたら）しいアイデアの特徴（とくちょう）はどれか。",
                [
                    "紙（かみ）の本（ほん）を無料（むりょう）で全員（ぜんいん）に配（くば）ること",
                    "電子版（でんしばん）の便利（べんり）さを否定（ひてい）し、インターネットを使（つか）わないこと",
                    "高品質（こうひんしつ）な紙（かみ）の本（ほん）と、学習（がくしゅう）をサポートする電子（でんし）ガイドを組み合わせること",
                    "社員（しゃいん）の給料（きゅうりょう）を下（さ）げて出版（しゅっぱん）を続（つづ）けること"
                ],
                3,
                "Đoạn 5: Hybrid kết hợp sách giấy in đẹp + hướng dẫn điện tử qua QR."
            ),
            (
                "「厳しい現状（げんじょう）[[にもかかわらず|〜にもかかわらず]]」の使い方（つかいかた）として正（ただ）しい説明（せつめい）はどれか。",
                [
                    "「〜だから当然（とうぜん）」という順接（じゅんせつ）の意味（いみ）を表（あらわ）す",
                    "「厳しい現状（げんじょう）ではあるが、それに負（ま）けず〜」という逆接（ぎゃくせつ）を表（あらわ）す",
                    "「〜のおかげで助（たす）かった」という感謝（かんしゃ）を表（あらわ）す",
                    "「〜するたびにお金（かね）がかかる」という回数（かいすう）を表（あらわ）す"
                ],
                2,
                "`N + にもかかわらず`: Mặc dù... nhưng vẫn... (mang sắc thái bất ngờ/ngược dự đoán — Shinkanzen Ngữ pháp Bài 13)."
            ),
        ]
    },
    {
        "num": 6,
        "slug": "chuong-06",
        "title_jp": "第6章：青空（あおぞら）の下（した）、次（つぎ）なる夢（ゆめ）への出発（しゅっぱつ）",
        "title_vi": "Chương 06: Dưới Bầu Trời Xanh — Hành Trình Mới Rộng Mở",
        "yuki_tip": "Chương kết tổng hợp tinh hoa từ vựng **Cấu tạo từ (第2部 7章: 〜的, 〜性, 〜化, 〜感, 高まる, 深まる)** và ngữ pháp trọng điểm (`〜を契機に`, `〜にほかならない`, `やり抜く`) — cùng thông điệp chúc em chinh phục JLPT N2!",
        "paragraphs": [
            (
                "あの日（ひ）の企画（きかく）が成功（せいこう）した[[のを契機（けいき）に|を契機に]]、陽翔（はると）は編集部（へんしゅうぶ）の大切な[[一員（いちいん）|部署]]として認（みと）められるようになった。",
                "Lấy thành công của dự án ngày hôm ấy làm bước ngoặt, Haruto đã được công nhận là một thành viên quan trọng trong ban biên tập."
            ),
            (
                "一年（いちねん）前（まえ）、駅（えき）で切符（きっぷ）すら迷（まよ）っていた頃（ころ）を[[振（ふ）り返（かえ）る|振り返る]]と、毎日（まいにち）の細（こま）かな積（つ）み重（かさ）ねが自分（じぶん）の[[可能性（かのうせい）|〜性]]をこれほどまでに広（ひろ）げてくれたのだと実感（じっかん）する。",
                "Nhìn lại khoảng thời gian một năm trước ngay cả việc mua vé tàu ở ga cũng còn lúng túng, cậu thấm thía rằng chính sự tích lũy từng chút mỗi ngày đã mở rộng khả năng của bản thân đến nhường này."
            ),
            (
                "ある穏（おだ）やかな日曜日（にちようび）、陽翔（はると）は黒沢（くろさわ）さんの店（みせ）の前（まえ）のブックカフェで梨花（りか）先輩（せんぱい）と並（なら）んで座（すわ）り、出来上（できあ）がったばかりの新刊（しんかん）を手（て）に取（と）った。そこには、一年前（いちねんまえ）の自分（じぶん）が悩（なや）みながら[[やり抜（ぬ）いた|走り抜く]]経験（けいけん）がすべて詰（つ）まっていた。",
                "Vào một ngày Chủ nhật êm ả, Haruto ngồi cạnh chị tiền bối Rika tại quán cà phê sách trước tiệm ông Kurosawa, cầm trên tay cuốn sách mới vừa ra lò. Trong đó chứa đựng trọn vẹn những trải nghiệm cậu đã trăn trở và kiên trì đi tới cùng suốt một năm qua."
            ),
            (
                "「最初（さいしょ）は自信（じしん）がなくて[[消極的（しょうきょくてき）]]だったけれど、ここまで来（こ）られたのは優（やさ）しい仲間（なかま）と両親（りょうしん）の支（ささ）えがあったから[[にほかならない|にほかならない]]」",
                "\"Ban đầu em từng thiếu tự tin và rụt rè đến thế, nhưng việc đi được tới chặng đường hôm nay chính là nhờ sự nâng đỡ của đồng đội dịu dàng và cha mẹ chứ chẳng phải điều gì khác.\""
            ),
            (
                "「陽翔（はると）くん自身（じしん）が毎日（まいにち）の困難（こんなん）から逃（に）げずに[[向（む）き合（あ）い|話し合う]]、[[成長（せいちょう）|〜化]]し続（つづ）けた証（あかし）よ。これから先（さき）も、もっと[[高（たか）まる|高まる・高める]]知識欲（ちしきよく）と仲間（なかま）との[[深（ふか）まる|深まる・深める]]絆（きずな）を大切（たいせつ）にしてね」",
                "\"Đó còn là minh chứng cho việc chính em đã không trốn chạy khó khăn mỗi ngày mà luôn đối diện và không ngừng trưởng thành đấy. Từ nay về sau, hãy luôn trân trọng khát khao tri thức ngày càng dâng cao và tình gắn kết ngày càng sâu sắc với mọi người nhé.\""
            ),
            (
                "ページを開（ひら）けば、そこには言葉（ことば）のひとつひとつに込（こ）められた物語（ものがたり）がある。[[充実（じゅうじつ）した|充実]]日々（ひび）への達成感（たっせいかん）と感謝（かんしゃ）を胸（むね）に、陽翔（はると）は見上（みあ）げた東京（とうきょう）の青空（あおぞら）の下（した）で、[[遥（はる）かに|遥かに]]遠（とお）い次（つぎ）の夢（ゆめ）へと歩（あゆ）み出（だ）した。",
                "Mỗi lần mở trang sách là một câu chuyện gửi gắm trong từng con chữ. Mang trong tim cảm giác viên mãn về những ngày tháng đã qua cùng lòng biết ơn sâu sắc, dưới bầu trời xanh Tokyo ngước nhìn lên, Haruto bước tiếp về phía ước mơ còn vươn xa hơn nữa."
            ),
        ],
        "quiz": [
            (
                "一年前（いちねんまえ）の自分（じぶん）と比（くら）べて、陽翔（はると）はどう成長（せいちょう）したか。",
                [
                    "他人（たにん）の意見（いけん）を聞（き）かずに一人（ひとり）で決（き）めるようになった",
                    "消極的（しょうきょくてき）だった自分（じぶん）を乗り越（のりこ）え、出版社（しゅっぱんしゃ）の大切（たいせつ）な一員（いちいん）として新刊（しんかん）を世（よ）に出（だ）した",
                    "都会（とかい）の生活（せいかつ）に疲（つか）れて実家（じっか）へ帰（かえ）ることにした",
                    "電子（でんし）書籍（しょせき）だけを作（つく）る専門（せんもん）会社（がいしゃ）へ転職（てんしょく）した"
                ],
                2,
                "Từ cậu sinh viên thiếu tự tin hay bối rối trước máy bán vé, sau 1 năm cậu thành biên tập viên chủ chốt cho ra mắt cuốn sách mới."
            ),
            (
                "「あの日（ひ）の企画（きかく）が成功（せいこう）した[[のを契機（けいき）に|を契機に]]」の意味（いみ）として正（ただ）しいのはどれか。",
                [
                    "その出来事（できごと）が原因（げんいん）で失敗（しっぱい）したこと",
                    "その出来事（できごと）をきっかけ・転機（てんき）として、新しい変化（へんか）が始（はじ）まったこと",
                    "その出来事（できごと）の間（あいだ）だけ一時的（いちじてき）に行（おこな）われたこと",
                    "その出来事（できごと）を完全（かんぜん）に忘（わす）れてしまったこと"
                ],
                2,
                "`Vる / N + を契機に（して）`: Lấy N/sự kiện đó làm bước ngoặt để khởi đầu giai đoạn mới (Shinkanzen Ngữ pháp Bài 3)."
            ),
            (
                "梨花（りか）先輩（せんぱい）が陽翔（はると）に贈（おく）った最後（さいご）のメッセージの趣旨（しゅし）はどれか。",
                [
                    "これから難（むずか）しい仕事（しごと）は全部（ぜんぶ）後輩（こうはい）に任（まか）せるべきだ",
                    "自分（じぶん）の努力（どりょく）による成長（せいちょう）を誇（ほこ）りに思（おも）い、知識（ちしき）と仲間（なかま）との絆（きずな）をこれからも大切（たいせつ）にしてほしい",
                    "今（いま）の仕事（しごと）に満足（まんぞく）してもう勉強（べんきょう）しなくていい",
                    "黒沢（くろさわ）さんの店（みせ）の掃除（そうじ）を毎日（まいにち）手伝（てつだ）ってほしい"
                ],
                2,
                "Đoạn 5: Chị Rika khẳng định thành quả đó là minh chứng cho sự nỗ lực của cậu và dặn giữ vững ham học hỏi + tình đồng đội."
            ),
        ]
    }
]

# Các mẫu bổ sung hoặc ngữ pháp Shinkanzen N2 liên kết trực tiếp về shinkanzen/ngu-phap/
EXTRA_SHINKANZEN_ENTRIES = {
    "就職する": {
        "kind": "vocab",
        "plain": "就職する",
        "furi": "就職（しゅうしょく）する",
        "reading": "しゅうしょくする",
        "hv": "TỰU CHỨC",
        "mean": "Tìm được việc làm chính thức, đi làm tại công ty",
        "collocJp": "希望（きぼう）する出版（しゅっぱん）社（しゃ）に就職（しゅうしょく）する",
        "collocVi": "Vào làm tại nhà xuất bản mơ ước",
        "bookLabel": "Từ vựng N2 — 第1部 5章 2課 (Nghề nghiệp & Công ty)",
        "mdLink": "../shinkanzen/tu-vung/phan-1/c05-b02_nghe-nghiep-cong-viec.md",
        "flashLink": "../shinkanzen/tu-vung/flashcards.html?lesson=p1_c05_b02"
    },
    "編集する": {
        "kind": "vocab",
        "plain": "編集する",
        "furi": "編集（へんしゅう）する",
        "reading": "へんしゅうする",
        "hv": "BIÊN TẬP",
        "mean": "Biên tập, chỉnh sửa nội dung sách báo",
        "collocJp": "記事（きじ）の原稿（げんこう）を丁寧（ていねい）に編集（へんしゅう）する",
        "collocVi": "Biên tập cẩn thận bản thảo bài viết",
        "bookLabel": "Từ vựng N2 — 第1部 6章 1課 (Truyền thông & Xuất bản)",
        "mdLink": "../shinkanzen/tu-vung/phan-1/c06-b01_truyen-thong-xuat-ban.md",
        "flashLink": "../shinkanzen/tu-vung/flashcards.html?lesson=p1_c06_b01"
    },
    "打ち合わせ": {
        "kind": "vocab",
        "plain": "打ち合わせ",
        "furi": "打（う）ち合（あ）わせ",
        "reading": "うちあわせ",
        "hv": "ĐẢ HỢP",
        "mean": "Cuộc họp bàn công việc trước khi thực hiện",
        "collocJp": "先輩（せんぱい）とイベントの打（う）ち合（あ）わせをする",
        "collocVi": "Họp bàn công việc với tiền bối",
        "bookLabel": "Từ vựng N2 — 第1部 5章 2課 (Công việc)",
        "mdLink": "../shinkanzen/tu-vung/phan-1/c05-b02_nghe-nghiep-cong-viec.md",
        "flashLink": "../shinkanzen/tu-vung/flashcards.html?lesson=p1_c05_b02"
    },
    "取材する": {
        "kind": "vocab",
        "plain": "取材する",
        "furi": "取材（しゅざい）する",
        "reading": "しゅざいする",
        "hv": "THỦ TÀI",
        "mean": "Lấy tin, phỏng vấn để viết bài",
        "collocJp": "街（まち）の書店（しょてん）へ取材（しゅざい）に行（い）く",
        "collocVi": "Đi lấy tin phỏng vấn tại hiệu sách",
        "bookLabel": "Từ vựng N2 — 第1部 6章 1課 (Truyền thông & Xuất bản)",
        "mdLink": "../shinkanzen/tu-vung/phan-1/c06-b01_truyen-thong-xuat-ban.md",
        "flashLink": "../shinkanzen/tu-vung/flashcards.html?lesson=p1_c06_b01"
    },
    "渋滞": {
        "kind": "vocab",
        "plain": "渋滞",
        "furi": "渋滞（じゅうたい）",
        "reading": "じゅうたい",
        "hv": "SÁP TRỆ",
        "mean": "Ùn tắc giao thông, kẹt xe kéo dài",
        "collocJp": "大雨（おおあめ）で道路（どうろ）が渋滞（じゅうたい）に巻（ま）き込（こ）まれる",
        "collocVi": "Bị kẹt xe trên đường vì mưa lớn",
        "bookLabel": "Chữ Hán Step 2 Bài 17 & Từ vựng N2",
        "mdLink": "../shinkanzen/kanji/step-2/bai-17.md",
        "flashLink": ""
    },
    "実施する": {
        "kind": "vocab",
        "plain": "実施する",
        "furi": "実施（じっし）する",
        "reading": "じっしする",
        "hv": "THỰC THI",
        "mean": "Triển khai thực hiện chính thức (sự kiện, khảo sát)",
        "collocJp": "イベントを予定（よてい）どおり実施（じっし）する",
        "collocVi": "Tổ chức sự kiện theo đúng lịch trình",
        "bookLabel": "Từ vựng N2 — 第2部 2章 2課 (Từ đồng nghĩa)",
        "mdLink": "../shinkanzen/tu-vung/phan-2/p2-c02-b02_tu-dong-nghia-2.md",
        "flashLink": "../shinkanzen/tu-vung/flashcards.html?lesson=p2_c02_b02"
    },
    "削減する": {
        "kind": "vocab",
        "plain": "削減する",
        "furi": "削減（さくげん）する",
        "reading": "さくげんする",
        "hv": "TƯỚC GIẢM",
        "mean": "Cắt giảm mạnh (chi phí, ngân sách, rác thải)",
        "collocJp": "印刷（いんさつ）コストを大幅（おおはば）に削減（さくげん）する",
        "collocVi": "Cắt giảm mạnh chi phí in ấn",
        "bookLabel": "Từ vựng N2 — 第1部 8章 1課 & Chữ Hán Bài 42",
        "mdLink": "../shinkanzen/tu-vung/phan-1/c08-b01_moi-truong-thien-nhien.md",
        "flashLink": "../shinkanzen/tu-vung/flashcards.html?lesson=p1_c08_b01"
    },
    "出版する": {
        "kind": "vocab",
        "plain": "出版する",
        "furi": "出版（しゅっぱん）する",
        "reading": "しゅっぱんする",
        "hv": "XUẤT BẢN",
        "mean": "Xuất bản phát hành sách",
        "collocJp": "新（あたら）しい本（ほん）を出版（しゅっぱん）する",
        "collocVi": "Xuất bản cuốn sách mới",
        "bookLabel": "Từ vựng N2 — 第1部 6章 1課 (Xuất bản)",
        "mdLink": "../shinkanzen/tu-vung/phan-1/c06-b01_truyen-thong-xuat-ban.md",
        "flashLink": "../shinkanzen/tu-vung/flashcards.html?lesson=p1_c06_b01"
    },
    "作成する": {
        "kind": "vocab",
        "plain": "作成する",
        "furi": "作成（さくせい）する",
        "reading": "さくせいする",
        "hv": "TÁC THÀNH",
        "mean": "Tạo lập, soạn thảo (tài liệu, báo cáo)",
        "collocJp": "プレゼン用（よう）の資料（しりょう）を作成（さくせい）する",
        "collocVi": "Soạn thảo tài liệu dùng cho thuyết trình",
        "bookLabel": "Từ vựng N2 — 第1部 6章 2課 (Máy tính & Tài liệu)",
        "mdLink": "../shinkanzen/tu-vung/phan-1/c06-b02_may-tinh-it.md",
        "flashLink": "../shinkanzen/tu-vung/flashcards.html?lesson=p1_c06_b02"
    },
    "維持する": {
        "kind": "vocab",
        "plain": "維持する",
        "furi": "維持（いじ）する",
        "reading": "いじする",
        "hv": "DUY TRÌ",
        "mean": "Duy trì giữ nguyên trạng thái tốt",
        "collocJp": "食生活（しょくせいかつ）を見直（みなお）して健康（けんこう）を維持（いじ）する",
        "collocVi": "Xem lại thói quen ăn uống để duy trì sức khỏe",
        "bookLabel": "Từ vựng N2 — 第2部 2章 2課",
        "mdLink": "../shinkanzen/tu-vung/phan-2/p2-c02-b02_tu-dong-nghia-2.md",
        "flashLink": "../shinkanzen/tu-vung/flashcards.html?lesson=p2_c02_b02"
    },
    "片付ける": {
        "kind": "vocab",
        "plain": "片付ける",
        "furi": "片付（かたづ）ける",
        "reading": "かたづける",
        "hv": "PHIẾN PHÓ",
        "mean": "Dọn dẹp gọn gàng ngăn nắp",
        "collocJp": "散（ち）らかったキッチンをきれいに片付（かたづ）ける",
        "collocVi": "Dọn dẹp căn bếp bừa bộn cho sạch sẽ",
        "bookLabel": "Từ vựng N2 — 第1部 2章 2課 (Việc nhà)",
        "mdLink": "../shinkanzen/tu-vung/phan-1/c02-b02_viec-nha-do-dac.md",
        "flashLink": "../shinkanzen/tu-vung/flashcards.html?lesson=p1_c02_b02"
    },
    "整理する": {
        "kind": "vocab",
        "plain": "整理する",
        "furi": "整理（せいり）する",
        "reading": "せいりする",
        "hv": "CHỈNH LÝ",
        "mean": "Sắp xếp phân loại gọn gàng",
        "collocJp": "週末（しゅうまつ）に本棚（ほんだな）を整理（せいり）する",
        "collocVi": "Sắp xếp lại giá sách vào cuối tuần",
        "bookLabel": "Từ vựng N2 — 第1部 2章 2課 (Việc nhà)",
        "mdLink": "../shinkanzen/tu-vung/phan-1/c02-b02_viec-nha-do-dac.md",
        "flashLink": "../shinkanzen/tu-vung/flashcards.html?lesson=p1_c02_b02"
    },
    "励ます": {
        "kind": "vocab",
        "plain": "励ます",
        "furi": "励（はげ）ます",
        "reading": "はげます",
        "hv": "LỆ",
        "mean": "Động viên, khích lệ tinh thần",
        "collocJp": "不安（ふあん）な友人（ゆうじん）を温（あたた）かく励（はげ）ます",
        "collocVi": "Động viên ấm áp người bạn đang bất an",
        "bookLabel": "Từ vựng N2 — 第1部 1章 3課 (Tâm trạng & Ứng xử)",
        "mdLink": "../shinkanzen/tu-vung/phan-1/c01-b03_cam-xuc-tam-trang.md",
        "flashLink": "../shinkanzen/tu-vung/flashcards.html?lesson=p1_c01_b03"
    },
    "買い出し": {
        "kind": "vocab",
        "plain": "買い出し",
        "furi": "買（か）い出（だ）し",
        "reading": "かいだし",
        "hv": "MÃI XUẤT",
        "mean": "Đi chợ/siêu thị mua sắm thực phẩm, đồ dùng",
        "collocJp": "日曜日（にちようび）に食材（しょくざい）の買（か）い出（だ）しに行（い）く",
        "collocVi": "Chủ nhật đi mua sắm nguyên liệu nấu ăn",
        "bookLabel": "Từ vựng N2 — 第1部 2章 2課",
        "mdLink": "../shinkanzen/tu-vung/phan-1/c02-b02_viec-nha-do-dac.md",
        "flashLink": "../shinkanzen/tu-vung/flashcards.html?lesson=p1_c02_b02"
    },
    "刻む": {
        "kind": "vocab",
        "plain": "刻む",
        "furi": "刻（きざ）む",
        "reading": "きざむ",
        "hv": "KHẮC",
        "mean": "Thái nhỏ, băm nhỏ (rau/hành) / Khắc ghi",
        "collocJp": "ねぎやニンジンを細（こま）かく刻（きざ）む",
        "collocVi": "Thái nhỏ hành và cà rốt",
        "bookLabel": "Từ vựng N2 — 第1部 2章 1課 (Nấu ăn & Dinh dưỡng)",
        "mdLink": "../shinkanzen/tu-vung/phan-1/c02-b01_thuc-pham-an-uong.md",
        "flashLink": "../shinkanzen/tu-vung/flashcards.html?lesson=p1_c02_b01"
    },
    "見直す": {
        "kind": "vocab",
        "plain": "見直す",
        "furi": "見直（みなお）す",
        "reading": "みなおす",
        "hv": "KIẾN TRỰC",
        "mean": "Kiểm tra xem lại từ đầu / Đánh giá lại tốt hơn",
        "collocJp": "提出（ていしゅつ）の前（まえ）に文章（ぶんしょう）を見直（みなお）す",
        "collocVi": "Kiểm tra lại câu văn trước khi nộp",
        "bookLabel": "Từ vựng N2 — 第2部 7章 1課 (Động từ ghép 〜直す)",
        "mdLink": "../shinkanzen/tu-vung/phan-2/p2-c07-b01_tu-ghep-dong-tu.md",
        "flashLink": "../shinkanzen/tu-vung/flashcards.html?lesson=p2_c07_b01"
    },
    "書き直す": {
        "kind": "vocab",
        "plain": "書き直す",
        "furi": "書（か）き直（なお）す",
        "reading": "かきなおす",
        "hv": "THƯ TRỰC",
        "mean": "Viết sửa lại lần nữa",
        "collocJp": "誤字（ごじ）を見（み）つけて原稿（げんこう）を書（か）き直（なお）す",
        "collocVi": "Tìm thấy lỗi chính tả nên viết sửa lại bản thảo",
        "bookLabel": "Từ vựng N2 — 第2部 7章 1課 (Động từ ghép 〜直す)",
        "mdLink": "../shinkanzen/tu-vung/phan-2/p2-c07-b01_tu-ghep-dong-tu.md",
        "flashLink": "../shinkanzen/tu-vung/flashcards.html?lesson=p2_c07_b01"
    },
    "助け合う": {
        "kind": "vocab",
        "plain": "助け合う",
        "furi": "助（たす）け合（あ）う",
        "reading": "たすけあう",
        "hv": "TRỢ HỢP",
        "mean": "Giúp đỡ lẫn nhau (cùng hợp sức)",
        "collocJp": "困難（こんなん）な時（とき）こそ仲間（なかま）と助（たす）け合（あ）う",
        "collocVi": "Chính lúc khó khăn càng giúp đỡ lẫn nhau",
        "bookLabel": "Từ vựng N2 — 第2部 7章 1課 (Động từ ghép 〜合う)",
        "mdLink": "../shinkanzen/tu-vung/phan-2/p2-c07-b01_tu-ghep-dong-tu.md",
        "flashLink": "../shinkanzen/tu-vung/flashcards.html?lesson=p2_c07_b01"
    },
    "考え抜く": {
        "kind": "vocab",
        "plain": "考え抜く",
        "furi": "考（かんが）え抜（ぬ）く",
        "reading": "かんがえぬく",
        "hv": "KHẢO BẠT",
        "mean": "Suy nghĩ thấu đáo đến cùng không bỏ cuộc",
        "collocJp": "一晩中（ひとばんじゅう）アイデアを考（かんが）え抜（ぬ）く",
        "collocVi": "Vắt óc suy nghĩ ý tưởng suốt đêm",
        "bookLabel": "Từ vựng N2 — 第2部 7章 1課 (Động từ ghép 〜抜く)",
        "mdLink": "../shinkanzen/tu-vung/phan-2/p2-c07-b01_tu-ghep-dong-tu.md",
        "flashLink": "../shinkanzen/tu-vung/flashcards.html?lesson=p2_c07_b01"
    },
    "直ちに": {
        "kind": "vocab",
        "plain": "直ちに",
        "furi": "直（ただ）ちに",
        "reading": "ただちに",
        "hv": "TRỰC",
        "mean": "Ngay lập tức (văn trang trọng)",
        "collocJp": "連絡（れんらく）を受（う）けて直（ただ）ちに対応（たいおう）する",
        "collocVi": "Nhận tin là ứng phó ngay lập tức",
        "bookLabel": "Từ vựng N2 — 第2部 2章 1課",
        "mdLink": "../shinkanzen/tu-vung/phan-2/p2-c02-b01_tu-dong-nghia-1.md",
        "flashLink": "../shinkanzen/tu-vung/flashcards.html?lesson=p2_c02_b01"
    },
    "振り返る": {
        "kind": "vocab",
        "plain": "振り返る",
        "furi": "振（ふ）り返（かえ）る",
        "reading": "ふりかえる",
        "hv": "CHẤN PHẢN",
        "mean": "Ngoái đầu nhìn lại, hồi tưởng lại quá khứ",
        "collocJp": "一年前（いちねんまえ）の自分（じぶん）を振（ふ）り返（かえ）る",
        "collocVi": "Nhìn lại bản thân mình một năm trước",
        "bookLabel": "Từ vựng N2 — 第2部 2章 2課",
        "mdLink": "../shinkanzen/tu-vung/phan-2/p2-c02-b02_tu-dong-nghia-2.md",
        "flashLink": "../shinkanzen/tu-vung/flashcards.html?lesson=p2_c02_b02"
    },
    "散らかる": {
        "kind": "vocab",
        "plain": "散らかる",
        "furi": "散（ち）らかる",
        "reading": "ちらかる",
        "hv": "TÁN",
        "mean": "Bừa bộn, vương vãi lung tung (tự động từ)",
        "collocJp": "部屋（へや）やテーブルの上（うえ）が散（ち）らかっている",
        "collocVi": "Căn phòng và mặt bàn đang bừa bộn",
        "bookLabel": "Từ vựng N2 — 第1部 2章 2課",
        "mdLink": "../shinkanzen/tu-vung/phan-1/c02-b02_viec-nha-do-dac.md",
        "flashLink": "../shinkanzen/tu-vung/flashcards.html?lesson=p1_c02_b02"
    },
    "生憎": {
        "kind": "vocab",
        "plain": "生憎",
        "furi": "生憎（あいにく）",
        "reading": "あいにく",
        "hv": "SINH TĂNG",
        "mean": "Trớ trêu thay, không may là (trái với mong muốn)",
        "collocJp": "イベントの日（ひ）に限（かぎ）って生憎（あいにく）の雨（あめ）だ",
        "collocVi": "Đúng ngày sự kiện thì trớ trêu lại mưa",
        "bookLabel": "Từ vựng N2 — 第2部 4章 3課 (Phó từ)",
        "mdLink": "../shinkanzen/tu-vung/phan-2/p2-c04-b03_pho-tu-3.md",
        "flashLink": "../shinkanzen/tu-vung/flashcards.html?lesson=p2_c04_b03"
    },
    "漸く": {
        "kind": "vocab",
        "plain": "漸く",
        "furi": "漸（ようや）く",
        "reading": "ようやく",
        "hv": "TIỆM",
        "mean": "Cuối cùng thì cũng, rốt cuộc sau bao vất vả",
        "collocJp": "努力（どりょく）の結果（けっか）、漸（ようや）く軌道（きどう）に乗（の）った",
        "collocVi": "Sau bao nỗ lực cuối cùng cũng vào guồng",
        "bookLabel": "Từ vựng N2 — 第2部 4章 1課 (Phó từ)",
        "mdLink": "../shinkanzen/tu-vung/phan-2/p2-c04-b01_pho-tu-1.md",
        "flashLink": "../shinkanzen/tu-vung/flashcards.html?lesson=p2_c04_b01"
    },
    "緊張": {
        "kind": "kanji",
        "plain": "緊張",
        "furi": "緊張（きんちょう）",
        "reading": "きんちょう",
        "hv": "KHẨN TRƯƠNG",
        "mean": "Căng thẳng, hồi hộp",
        "collocJp": "ステージで緊張（きんちょう）して上（あ）がる",
        "collocVi": "Căng thẳng đến mức bị run trên sân khấu",
        "bookLabel": "Chữ Hán Step 3 Bài 37 (緊) & Từ vựng 第2部 1章",
        "mdLink": "../shinkanzen/kanji/step-3/bai-37.md",
        "flashLink": "../shinkanzen/tu-vung/flashcards.html?lesson=p2_c01_b01"
    },
    "労働・協力": {
        "kind": "kanji",
        "plain": "協力",
        "furi": "協力（きょうりょく）",
        "reading": "きょうりょく",
        "hv": "HIỆP LỰC",
        "mean": "Hợp tác, chung sức làm việc",
        "collocJp": "仕事仲間（しごとなかま）と協力（きょうりょく）して乗り越（こ）える",
        "collocVi": "Hợp tác cùng đồng nghiệp vượt qua khó khăn",
        "bookLabel": "Chữ Hán Step 1 Bài 08 (協) & Từ vựng N2",
        "mdLink": "../shinkanzen/kanji/step-1/bai-08.md",
        "flashLink": "../shinkanzen/tu-vung/flashcards.html?lesson=p1_c01_b01"
    },
    "減少・増加": {
        "kind": "kanji",
        "plain": "大幅に",
        "furi": "大幅（おおはば）に",
        "reading": "おおはばに",
        "hv": "ĐẠI PHÚC",
        "mean": "Một cách đáng kể, trên diện rộng / mức lớn",
        "collocJp": "コストや食費（しょくひ）を大幅（おおはば）に削減（さくげん）する",
        "collocVi": "Cắt giảm đáng kể chi phí hoặc tiền ăn",
        "bookLabel": "Chữ Hán Step 3 Bài 47 (幅) & Từ vựng 8章・9章",
        "mdLink": "../shinkanzen/kanji/step-3/bai-47.md",
        "flashLink": "../shinkanzen/tu-vung/flashcards.html?lesson=p1_c09_b01"
    },
    "価値・構造": {
        "kind": "kanji",
        "plain": "価値",
        "furi": "価値（かち）",
        "reading": "かち",
        "hv": "GIÁ TRỊ",
        "mean": "Giá trị, ý nghĩa đáng quý",
        "collocJp": "伝統（でんとう）の大切（たいせつ）な価値（かち）を見直（みなお）す",
        "collocVi": "Nhìn nhận lại giá trị đáng quý của truyền thống",
        "bookLabel": "Chữ Hán Step 1 Bài 04 (価) & Step 2 Bài 24 (値)",
        "mdLink": "../shinkanzen/kanji/step-1/bai-04.md",
        "flashLink": ""
    },
    "充実": {
        "kind": "kanji",
        "plain": "充実",
        "furi": "充実（じゅうじつ）",
        "reading": "じゅうじつ",
        "hv": "SUNG THỰC",
        "mean": "Viên mãn, tràn đầy phong phú, đầy đủ",
        "collocJp": "充実（じゅうじつ）した毎日（まいにち）を送（おく）る",
        "collocVi": "Trải qua những ngày tháng viên mãn trọn vẹn",
        "bookLabel": "Chữ Hán Step 2 Bài 17 (充・実)",
        "mdLink": "../shinkanzen/kanji/step-2/bai-17.md",
        "flashLink": ""
    },
    # Ngữ pháp Shinkanzen N2 nổi bật trong truyện
    "に際して": {
        "kind": "grammar",
        "plain": "〜に際して",
        "furi": "〜に際（さい）して",
        "reading": "〜にさいして",
        "hv": "NGỮ PHÁP BÀI 01",
        "mean": "Nhân dịp..., khi bước vào một sự kiện/cột mốc quan trọng",
        "collocJp": "接続: N / V-る + に際して（の）",
        "collocVi": "Dùng cho khởi đầu mới (nhập học, công tác, khởi hành...)",
        "bookLabel": "Ngữ pháp N2 — 第1部 第1課 (時間・時)",
        "mdLink": "../shinkanzen/ngu-phap/phan-1/bai-01.md",
        "flashLink": ""
    },
    "てしかたがない": {
        "kind": "grammar",
        "plain": "〜てしかたがない / たまらない",
        "furi": "〜てたまらない",
        "reading": "〜てたまらない",
        "hv": "NGỮ PHÁP BÀI 25",
        "mean": "...vô cùng, ...không sao kìm nén nổi",
        "collocJp": "接続: A-くて / Na-で / V-て + たまらない",
        "collocVi": "Diễn tả cảm giác/cảm xúc trào dâng mãnh liệt (lo lắng, nhớ nhung...)",
        "bookLabel": "Ngữ pháp N2 — 第1部 第25課 (強くそう感じる)",
        "mdLink": "../shinkanzen/ngu-phap/phan-1/bai-25.md",
        "flashLink": ""
    },
    "に違いない": {
        "kind": "grammar",
        "plain": "〜に違いない",
        "furi": "〜に違（ちが）いない",
        "reading": "〜にちがいない",
        "hv": "NGỮ PHÁP BÀI 21",
        "mean": "Chắc chắn là..., ắt hẳn là... (suy đoán có cơ sở)",
        "collocJp": "接続: Thể thông thường + に違いない",
        "collocVi": "Thể hiện sự tin chắc gần như tuyệt đối của người nói",
        "bookLabel": "Ngữ pháp N2 — 第1部 第21課 (主張・確信)",
        "mdLink": "../shinkanzen/ngu-phap/phan-1/bai-21.md",
        "flashLink": ""
    },
    "〜ざるを得ない": {
        "kind": "grammar",
        "plain": "〜ざるを得ない",
        "furi": "〜ざるを得（え）ない",
        "reading": "〜ざるをえない",
        "hv": "NGỮ PHÁP BÀI 25",
        "mean": "Đành phải..., buộc lòng phải... (dù không muốn)",
        "collocJp": "接続: V-ない (bỏ ない) + ざるを得ない（※する → せざるを得ない）",
        "collocVi": "Bắt buộc vì hoàn cảnh khách quan không còn lựa chọn nào khác",
        "bookLabel": "Ngữ pháp N2 — 第1部 第25課 (思いが強いられる)",
        "mdLink": "../shinkanzen/ngu-phap/phan-1/bai-25.md",
        "flashLink": ""
    },
    "〜つつ": {
        "kind": "grammar",
        "plain": "〜つつ（も）",
        "furi": "〜つつ",
        "reading": "〜つつ",
        "hv": "NGỮ PHÁP BÀI 02 & 14",
        "mean": "Vừa... vừa... (hai hành động song song) / Mặc dù... nhưng...",
        "collocJp": "接続: V-ます (bỏ ます) + つつ",
        "collocVi": "Văn phong trang nhã hơn 〜ながら rất nhiều",
        "bookLabel": "Ngữ pháp N2 — 第1部 第2課 & 第14課",
        "mdLink": "../shinkanzen/ngu-phap/phan-1/bai-02.md",
        "flashLink": ""
    },
    "〜かねない": {
        "kind": "grammar",
        "plain": "〜かねない",
        "furi": "〜かねない",
        "reading": "〜かねない",
        "hv": "NGỮ PHÁP BÀI 19",
        "mean": "E rằng có nguy cơ..., rất có thể sẽ dẫn đến kết quả xấu...",
        "collocJp": "接続: V-ます (bỏ ます) + かねない",
        "collocVi": "Chỉ dùng cho hệ quả xấu / điều đáng lo ngại có thể xảy ra",
        "bookLabel": "Ngữ pháp N2 — 第1部 第19課 (可能性)",
        "mdLink": "../shinkanzen/ngu-phap/phan-1/bai-19.md",
        "flashLink": ""
    },
    "〜末に": {
        "kind": "grammar",
        "plain": "〜末に",
        "furi": "〜末（すえ）に",
        "reading": "〜すえに",
        "hv": "NGỮ PHÁP BÀI 04",
        "mean": "Sau một quá trình dài vất vả..., cuối cùng thì cũng...",
        "collocJp": "接続: V-た / N-の + 末（に）",
        "collocVi": "Nhấn mạnh quá trình kéo dài đầy nỗ lực trước khi đạt kết quả",
        "bookLabel": "Ngữ pháp N2 — 第1部 第4課 (経過・結末)",
        "mdLink": "../shinkanzen/ngu-phap/phan-1/bai-04.md",
        "flashLink": ""
    },
    "〜おかげで": {
        "kind": "grammar",
        "plain": "〜おかげで",
        "furi": "〜おかげで",
        "reading": "〜おかげで",
        "hv": "NGỮ PHÁP BÀI 09",
        "mean": "Nhờ có... mà (kết quả tốt đẹp)",
        "collocJp": "接続: V-た・普通形 / Na-な / N-の + おかげで",
        "collocVi": "Diễn tả lòng biết ơn đối với nguyên nhân mang lại điều hay",
        "bookLabel": "Ngữ pháp N2 — 第1部 第9課 (原因・理由)",
        "mdLink": "../shinkanzen/ngu-phap/phan-1/bai-09.md",
        "flashLink": ""
    },
    "〜ばかりでなく": {
        "kind": "grammar",
        "plain": "〜ばかりでなく",
        "furi": "〜ばかりでなく",
        "reading": "〜ばかりでなく",
        "hv": "NGỮ PHÁP BÀI 12",
        "mean": "Không chỉ A mà còn cả B nữa...",
        "collocJp": "接続: 普通形 / Na-な(である) / N + ばかりでなく（〜も）",
        "collocVi": "Thường đi kèm vế sau với trợ từ も để bổ sung ý nâng cấp",
        "bookLabel": "Ngữ pháp N2 — 第1部 第12課 (付加・並立)",
        "mdLink": "../shinkanzen/ngu-phap/phan-1/bai-12.md",
        "flashLink": ""
    },
    "〜につれて": {
        "kind": "grammar",
        "plain": "〜につれて",
        "furi": "〜につれて",
        "reading": "〜につれて",
        "hv": "NGỮ PHÁP BÀI 05",
        "mean": "Càng ngày theo đà A thay đổi thì B cũng biến đổi theo",
        "collocJp": "接続: V-る / N + につれて",
        "collocVi": "Thường đi với biến đổi một chiều (thời gian trôi, tuổi tăng...)",
        "bookLabel": "Ngữ pháp N2 — 第1部 第5課 (比例変化)",
        "mdLink": "../shinkanzen/ngu-phap/phan-1/bai-05.md",
        "flashLink": ""
    },
    "〜一方で": {
        "kind": "grammar",
        "plain": "〜一方で",
        "furi": "〜一方（いっぽう）で",
        "reading": "〜いっぽうで",
        "hv": "NGỮ PHÁP BÀI 12",
        "mean": "Một mặt thì..., mặt khác thì... (song hành 2 khía cạnh/đối lập)",
        "collocJp": "接続: 普通形 / Na-な(である) / N-である + 一方で",
        "collocVi": "Rất hay dùng trong Đọc hiểu đối chiếu 対比",
        "bookLabel": "Ngữ pháp N2 — 第1部 第12課 (対比)",
        "mdLink": "../shinkanzen/ngu-phap/phan-1/bai-12.md",
        "flashLink": ""
    },
    "〜にもかかわらず": {
        "kind": "grammar",
        "plain": "〜にもかかわらず",
        "furi": "〜にもかかわらず",
        "reading": "〜にもかかわらず",
        "hv": "NGỮ PHÁP BÀI 13",
        "mean": "Mặc dù..., bất chấp... nhưng vẫn...",
        "collocJp": "接続: 普通形 / Na / N + にもかかわらず",
        "collocVi": "Mức độ trang trọng cao hơn 〜のに rất nhiều trong văn viết",
        "bookLabel": "Ngữ pháp N2 — 第1部 第13課 (逆接)",
        "mdLink": "../shinkanzen/ngu-phap/phan-1/bai-13.md",
        "flashLink": ""
    },
    "を契機に": {
        "kind": "grammar",
        "plain": "〜を契機に",
        "furi": "〜を契機（けいき）に",
        "reading": "〜をけいきに",
        "hv": "NGỮ PHÁP BÀI 03",
        "mean": "Lấy... làm bước ngoặt, cơ hội để đổi mới",
        "collocJp": "接続: N + を契機に（して）",
        "collocVi": "Đánh dấu bước chuyển mình quan trọng (trùng chữ 契機 trong Từ vựng P2-2章2課)",
        "bookLabel": "Ngữ pháp N2 — 第1部 第3課 (きっかけ)",
        "mdLink": "../shinkanzen/ngu-phap/phan-1/bai-03.md",
        "flashLink": ""
    },
    "にほかならない": {
        "kind": "grammar",
        "plain": "〜にほかならない",
        "furi": "〜にほかならない",
        "reading": "〜にほかならない",
        "hv": "NGỮ PHÁP BÀI 21",
        "mean": "Chính là..., chẳng phải điều nào khác ngoài...",
        "collocJp": "接続: N + にほかならない / 〜からにほかならない",
        "collocVi": "Khẳng định nguyên nhân duy nhất mang tính chốt hạ cao",
        "bookLabel": "Ngữ pháp N2 — 第1部 第21課 (主張・断定)",
        "mdLink": "../shinkanzen/ngu-phap/phan-1/bai-21.md",
        "flashLink": ""
    },
}
