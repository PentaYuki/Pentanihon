# -*- coding: utf-8 -*-
"""
Tiểu thuyết 2 — YANDERE ROMANCE (Tình Yêu Độc Chiếm & Tâm Lý): Phần A (Chương 01 - 06)
『君だけの檻に咲く紅の約束』— Lời Hứa Đỏ Thắm Trong Chiếc Lồng Chỉ Dành Riêng Cho Anh
"""

YANDERE_META = {
    "id": "yandere",
    "slug": "yandere",
    "genre_badge": "🖤🌹 YANDERE ROMANCE • TÌNH YÊU ĐỘC CHIẾM",
    "theme_color": "#86194f",
    "theme_soft": "#fdf2f8",
    "title_jp": "君（きみ）だけの檻（おり）に咲（さ）く紅（くれない）の約束（やくそく）",
    "title_vi": "Lời Hứa Đỏ Thắm Trong Chiếc Lồng Chỉ Dành Riêng Cho Anh",
    "tagline": "Nụ cười hoàn hảo, sự quan tâm nghẹt thở, những tin nhắn bị kiểm soát và tình yêu độc chiếm chỉ thuộc về duy nhất một người — gói trọn 12 bài Shinkanzen (233 từ)!",
    "yuki_intro": "Hít một hơi thật sâu nào em~ Bộ truyện thứ hai là thể loại **Yandere chuyên về tình cảm tâm lý**: dịu dàng đến rùng mình, ngọt ngào mà đầy chiếm hữu! Mỗi câu chữ đều lồng ghép các từ cảm xúc, bệnh tật, công nghệ theo dõi và động từ đa nghĩa Shinkanzen N2. Đọc thấy tim đập nhanh quá thì nhớ uống ngụm trà ấm cùng chị nha 🌹✨",
    "characters": [
        {"name": "海斗（かいと / Kaito）", "role": "Nam chính (24 tuổi)", "desc": "Chàng thiết kế đồ họa hiền lành, sống khép kín, dần phát hiện thế giới xung quanh mình đang bị cô đồng nghiệp dịu dàng bao bọc chặt kín."},
        {"name": "小百合（さゆり / Sayuri）", "role": "Nữ chính Yandere (23 tuổi)", "desc": "Bề ngoài là cô gái dịu dàng, đảm đang, ngưỡng mộ Kaito hết mực, nhưng bên trong lại khao khát độc chiếm Kaito hoàn toàn chỉ cho riêng mình."},
        {"name": "玲奈（れいな / Reina）", "role": "Đồng nghiệp cũ (24 tuổi)", "desc": "Người bạn thân từng giúp đỡ Kaito ở công ty nhưng bỗng dưng đột ngột xin chuyển công tác sau khi đụng độ Sayuri."},
    ],
}

YANDERE_CHAPTERS_A = [
    {
        "num": 1,
        "slug": "chuong-01",
        "lesson_id": "p1_c01_b03",
        "title_jp": "第1章：[[憧（あこが）れる|3]]笑顔（えがお）の裏（うら）と[[嫉妬（しっと）|16]]の吐息（といき）",
        "title_vi": "Chương 01: Phía Sau Nụ Cười Ngưỡng Mộ & Hơi Thở Của Sự Ghen Tuông",
        "yuki_reminder_top": "Chương mở màn bộ Yandere chứa trọn 32 từ **Bài 3 (Cảm xúc & Hành động đối với người khác)**! Cực hợp chất tình cảm tâm lý luôn: từ `慕う・憧れる・甘える` (quý mến, ngưỡng mộ, làm nũng) cho tới `嫉妬する・恨む・疑う・裏切る` (ghen tuông, oán hận, nghi ngờ, phản bội)! 🖤🌹",
        "yuki_reminder_bottom": "Chà, cô nàng Sayuri mới chương 1 đã lộ chút ánh mắt ghen tuông rồi đó em... Nhớ phân biệt `うらやましい` (ngưỡng mộ muốn được như thế) với `嫉妬する` (ghen tuông đố kỵ) và `労う` vs `いたわる` khi làm 5 câu quiz bên dưới nhé! 💌",
        "soft_notes": [
            (2, "Nhắc nhẹ từ chị Yuki 🌹", "Phân biệt `労（ねぎら）う` (cảm ơn, tán thưởng công sức đồng nghiệp/cấp dưới) với `いたわる` (chăm sóc ân cần người già/người ốm/người yếu). Trong đề hay tráo 2 từ này lắm nha em!"),
            (5, "Sắc thái Ghen tị vs Ghen tuông 💔", "`うらやましい` là ghen tị nhẹ nhàng tích cực, còn `嫉妬（しっと）する` là ghen tuông đố kỵ rực lửa — đúng chất Yandere luôn đó! Còn `気（き）が置（お）けない` nghĩa là *thoải mái không cần giữ kẽ* (đừng hiểu nhầm là 'không để ý' nhé em!)."),
        ],
        "paragraphs": [
            (
                "デザイン事務所（じむしょ）で働（はたら）く海斗（かいと）にとって、一つ後輩（こうはい）の小百合（さゆり）は、いつも礼儀（れいぎ）正（ただ）しく先輩（せんぱい）を[[敬（うやま）い|1]]、兄（あに）のように[[慕（した）っ|2]]てくれる可憐（かれん）な女性（じょせい）だった。「海斗（かいと）先輩（せんぱい）の才能（さいのう）にずっと[[憧（あこが）れて|3]]いたんです！」と小百合（さゆり）は目を輝（かがや）かせる。",
                "Đối với Kaito đang làm việc tại văn phòng thiết kế, cô hậu bối kém một tuổi Sayuri luôn là một cô gái khả ái biết kính trọng tiền bối và quý mến quấn quýt cậu như anh trai. 'Em luôn ngưỡng mộ tài năng của tiền bối Kaito lắm ạ!' — Sayuri nói với đôi mắt sáng lấp lánh."
            ),
            (
                "仕事（しごと）で疲（つか）れた海斗（かいと）を気遣（きづか）い、小百合（さゆり）はいつも手作り（てづくり）のクッキーで温（あたた）かく[[もてなして|9]]くれた。「今日（きょう）もお疲れ（つかれ）さまでした」と優しく[[労（ねぎら）い|8]]ながら、体調（たいちょう）を崩（くず）したお年寄（としよ）りまで[[いたわる|7]]ように、毛布（もうふ）までそっと掛（か）けてくれる。ペットの子猫（こねこ）が飼い主（かいぬし）に[[なつく|11]]みたいに無邪気（むじゃき）に[[かわいがり|10]]たくなる笑顔（えがお）で[[甘（あま）えて|27]]くるので、海斗（かいと）もすっかり[[信用（しんよう）する|12]]ようになっていた。",
                "Quan tâm Kaito mỗi lúc mệt mỏi vì công việc, Sayuri luôn tiếp đón cậu nồng hậu bằng bánh quy tự làm. Vừa dịu dàng tán thưởng động viên 'Hôm nay anh vất vả rồi', cô còn ân cần chăm nom đắp thêm cả chiếc chăn mỏng như chăm sóc người yếu. Vì cô ấy hay làm nũng với nụ cười ngây thơ quấn quýt như mèo con khiến người ta chỉ muốn yêu chiều, Kaito đã hoàn toàn tin tưởng cô."
            ),
            (
                "ところが、ある金曜日（きんようび）の夜（よる）から空気（くうき）が変（か）わった。同期（どうき）の玲奈（れいな）と二人（ふたり）が[[気（き）が置（お）けない|32]]仲（なか）でカフェに寄（よ）り、会計（かいけい）を[[割（わ）り勘（かん）|31]]にしようとしたとき、海斗（かいと）が「今日（きょう）は俺（おれ）が[[おごる|30]]よ」と笑（わら）った瞬間（しゅんかん）を、窓（まど）の外（そと）から小百合（さゆり）が見（み）ていたのだ。",
                "Thế nhưng từ một tối thứ Sáu nọ, bầu không khí bỗng thay đổi. Khi Kaito ghé quán cà phê cùng cô bạn đồng khóa thân thiết không cần giữ kẽ là Reina, lúc chuẩn bị chia đều tiền thì cậu cười bảo 'Hôm nay để anh bao nhé' — đúng khoảnh khắc ấy đã bị Sayuri đứng ngoài cửa sổ nhìn thấy hết."
            ),
            (
                "翌日（よくじつ）の給湯室（きゅうとうしつ）で、小百合（さゆり）は冷（つめ）たい声（こえ）で呟（つぶや）いた。「ねえ、海斗（かいと）先輩（せんぱい）。昨日（きのう）の女性（じょせい）、ただの[[お世辞（せじ）|25]]で笑（わら）ってただけじゃないんですか？　あんな軽（かる）い人（ひと）に[[頼（たよ）る|28]]だなんて、先輩（せんぱい）が[[だまされ|20]]てしまわないか心配（しんぱい）です」",
                "Ngày hôm sau trong phòng pha trà, Sayuri khẽ thì thầm bằng chất giọng lạnh băng: 'Này tiền bối Kaito. Người phụ nữ hôm qua chẳng qua chỉ cười nói lời xã giao tâng bốc thôi đúng không ạ? Dựa dẫm vào một người nhẹ dạ như thế, em lo anh sẽ bị cô ta lừa mất thôi'."
            ),
            (
                "「玲奈（れいな）はそんな人（ひと）じゃないよ。仕事（しごと）でミスして落（お）ち込（こ）んでいた僕（ぼく）をいつも[[慰（なぐさ）め|5]]て[[励（はげ）まし|6]]てくれたんだ」と海斗（かいと）が庇（かば）うと、小百合（さゆり）の瞳（ひとみ）から温度（おんど）が消（き）えた。「へえ……私（わたし）は先輩（せんぱい）に一番（いちばん）好（す）かれていると思って[[うらやましい|15]]くらいだったのに、彼女（かのじょ）の方（ほう）に[[同情（どうじょう）して|4]]るんですか？」",
                "'Reina không phải người như vậy đâu. Mỗi lúc anh mắc lỗi buồn bã, chính cậu ấy luôn an ủi và động viên anh đấy' — Kaito vừa bênh vực, ánh mắt Sayuri lập tức tắt hẳn hơi ấm: 'Ra vậy... Em cứ tưởng em mới là người được anh quý nhất, thậm chí từng ngưỡng mộ tình bạn của hai người, hóa ra anh lại đồng cảm với cô ta hơn à?'."
            ),
            (
                "海斗（かいと）が「まさか、小百合（さゆり）が[[嫉妬（しっと）する|16]]なんてことある？」と冗談（じょうだん）めかして[[からかう|21]]ように笑（わら）うと、小百合（さゆり）はふっと口元（くちもと）を歪（ゆが）めた。「ええ、先輩（せんぱい）の隣（となり）に他（ほか）の女（おんな）がいると、その人（ひと）を[[恨（うら）み|13]]そうなくらい[[憎（にく）く|14]]なるんです。私（わたし）の気持（きも）ちを[[無視（むし）して|23]]、私（わたし）を[[見下（みくだ）し|17]]て笑（わら）うつもりなら、[[避（さ）け|22]]られても絶対（ぜったい）に追（お）いかけますから」",
                "Kaito định cười trêu chọc cho qua chuyện 'Đâu có chuyện Sayuri đi ghen tuông thế đâu nhỉ?', thì Sayuri khẽ nhếch môi: 'Có chứ ạ. Hễ có người con gái khác đứng cạnh tiền bối là em ghét cay ghét đắng đến mức muốn oán hận cô ta luôn đấy. Nếu anh phớt lờ cảm xúc của em, coi thường mà cười nhạo em thì dù anh có trốn tránh em cũng nhất định đuổi theo tới cùng'."
            ),
            (
                "海斗（かいと）は一瞬（いっしゅん）背筋（せすじ）が凍（こお）り、自分（じぶん）に[[反抗（はんこう）する|29]]ような目（め）つきを[[疑（うたが）った|18]]。「そんな、[[言（い）い訳（わけ）|26]]するわけじゃないけど……」と言いかけた瞬間（しゅんかん）、小百合（さゆり）は再び（ふたたび）花（はな）のように微笑（ほほえ）み、胸（むね）の奥（おく）の秘密（ひみつ）を[[打（う）ち明（あ）けた|24]]。「先輩（せんぱい）が私（わたし）の優（やさ）しさを[[裏切（うらぎ）る|19]]ことはないって信（しん）じてますよ。だって、私（わたし）の世界（せかい）には先輩（せんぱい）しかいないんですから」",
                "Trong tích tắc sống lưng Kaito lạnh toát, cậu nghi ngờ không hiểu ánh mắt như đang chống đối đầy chiếm hữu vừa rồi có phải thật không. 'Đâu có, không phải anh định kiếm cớ đâu...' — cậu vừa định nói thì Sayuri bỗng mỉm cười rạng rỡ như hoa trở lại, thổ lộ bí mật tận đáy lòng: 'Em tin tiền bối sẽ không bao giờ phản bội tình cảm dịu dàng của em đâu. Vì trong thế giới của em, chỉ tồn tại duy nhất mình anh thôi mà'."
            ),
        ],
        "quiz": [
            {
                "prompt": "ずっと一人（ひとり）で悩（なや）んでいた秘密（ひみつ）の本音（ほんね）を、信（しん）じる人（ひと）に（　　）。",
                "options": ["打（う）ち明（あ）けた", "裏切（うらぎ）った", "からかった", "見下（みくだ）した"],
                "ans": 1,
                "right_exp": "💖 Chính xác! Thổ lộ tâm sự thầm kín từ đáy lòng cho người mình tin tưởng là `打ち明ける`.",
                "wrong_exps": [
                    "Chính xác: `打ち明ける` = thổ lộ tâm tình, thú nhận bí mật.",
                    "`裏切る` là phản bội lòng tin.",
                    "`からかう` là trêu chọc đùa giỡn.",
                    "`見下す` là coi thường khinh miệt người khác."
                ]
            },
            {
                "prompt": "プロジェクトを終（お）えた部下（ぶか）の苦労（くろう）に感謝（かんしゃ）して、言葉（ことば）をかけて（　　）。",
                "options": ["労（ねぎら）った", "恨（うら）んだ", "だました", "反抗（はんこう）した"],
                "ans": 1,
                "right_exp": "💖 Quá chuẩn! Ghi nhận và cảm ơn công sức vất vả của cấp dưới/đồng nghiệp là `労（ねぎら）う`.",
                "wrong_exps": [
                    "Chính xác: `労う` = tán thưởng, cảm ơn công lao vất vả.",
                    "`恨む` là oán hận.",
                    "`だます` là lừa dối.",
                    "`反抗する` là chống đối lại."
                ]
            },
            {
                "prompt": "「遠慮（えんりょ）しないで気楽（きらく）に話（はな）せる親（した）しい友達（ともだち）」を表（あらわ）す表現（ひょうげん）はどれか。",
                "options": ["気（き）が置（お）けない仲間（なかま）", "お世辞（せじ）を言（い）う人（ひと）", "目上（めうえ）の人（ひと）", "無視（むし）する相手（あいて）"],
                "ans": 1,
                "right_exp": "💖 Tuyệt vời! Đây là bẫy siêu kinh điển của N2: `気が置けない` KHÔNG mang nghĩa xấu mà có nghĩa là **thoải mái, thân thiết không cần giữ kẽ**!",
                "wrong_exps": [
                    "Chính xác: `気が置けない仲間` = bạn bè thân thiết không cần khách sáo.",
                    "`お世辞を言う人` là người hay khen xã giao tâng bốc.",
                    "`目上の人` là người bề trên (thường phải dùng kính ngữ giữ lễ chứ không hẳn thoải mái tùy tiện).",
                    "`無視する相手` là người phớt lờ làm ngơ."
                ]
            },
            {
                "prompt": "友達（ともだち）と食事（しょくじ）に行（い）って、一人（ひとり）ずつ同（おな）じ金額（きんがく）を払（はら）うことを何（なん）と言（い）うか。",
                "options": ["割（わ）り勘（かん）", "おごる", "言（い）い訳（わけ）", "お世辞（せじ）"],
                "ans": 1,
                "right_exp": "💖 Chuẩn rồi em! Chia đều hóa đơn mỗi người trả phần mình là `割り勘（わりかん）`.",
                "wrong_exps": [
                    "Chính xác: `割り勘` = chia đều tiền thanh toán.",
                    "`おごる` là mình đứng ra bao trả hết tiền cho người khác.",
                    "`言い訳` là lời biện minh, kiếm cớ.",
                    "`お世辞` là lời khen xã giao."
                ]
            },
            {
                "prompt": "小百合（さゆり）が海斗（かいと）に「私（わたし）の世界（せかい）には先輩（せんぱい）しかいない」と打（う）ち明（あ）けた裏（うら）には、どんな感情（かんじょう）があるか。",
                "options": [
                    "海斗（かいと）が他（ほか）の女性（じょせい）と親（した）しくするのを許（ゆる）せない強（つよ）い嫉妬（しっと）と独占欲（どくせんよく）",
                    "玲奈（れいな）とカフェで割（わ）り勘（かん）したかったという羨（うらや）ましさ",
                    "会社（かいしゃ）の先輩（せんぱい）として給料（きゅうりょう）をおごってほしいという願（ねが）い",
                    "海斗（かいと）を会社（かいしゃ）から避（さ）けたいという気持（きも）ち"
                ],
                "ans": 1,
                "right_exp": "💖 Nắm trúng tâm lý nhân vật rồi nè! Đằng sau nụ cười dịu dàng của Sayuri là sự ghen tuông mãnh liệt (`嫉妬`) và khát khao độc chiếm chỉ riêng mình Kaito thuộc về cô ấy.",
                "wrong_exps": [
                    "Chính xác: Tình cảm chiếm hữu và ghen tuông cực độ với bất kỳ cô gái nào lại gần Kaito.",
                    "Sayuri không hề muốn đi cà phê chia tiền với Reina mà cực kỳ ghét việc Kaito thân thiết với Reina.",
                    "Cô ấy không hề đòi tiền hay nhờ bao ăn nhé.",
                    "Ngược lại hoàn toàn: cô ấy khẳng định dù Kaito có trốn tránh cô cũng sẽ đuổi theo!"
                ]
            },
        ]
    },
    {
        "num": 2,
        "slug": "chuong-02",
        "lesson_id": "p1_c02_b03",
        "title_jp": "第2章：高熱（こうねつ）の夜（よる）と、甘（あま）すぎる[[看病（かんびょう）|17]]",
        "title_vi": "Chương 02: Đêm Sốt Cao & Sự Chăm Sóc Ngọt Ngào Đến Nghẹt Thở",
        "yuki_reminder_top": "Chương 2 lồng trọn 27 từ **Bài 6 (Sức khỏe, Bệnh tật & Y tế)**! Chàng Kaito bị cảm nặng đến mức suýt ngất, thế là nàng Yandere Sayuri tận dụng cơ hội tới tận phòng riêng chăm sóc cậu. Học kỹ cặp `診察・診断`, `感染・伝染` và phản xạ cơ thể `しびれる・震える・もたれる・しゃがむ` nha em 🤒💊",
        "yuki_reminder_bottom": "Ấy chà, viên thuốc làm cậu buồn ngủ vì `副作用` (tác dụng phụ) hay là kế giữ chân cậu ở lại đây? Nhớ phân biệt `診察する` (bác sĩ khám) vs `診断する` (chẩn đoán tên bệnh) trước khi làm 5 câu quiz nha! 🌸",
        "soft_notes": [
            (2, "Phân biệt khám & chẩn đoán 🏥", "`診察（しんさつ）する` = bác sĩ trực tiếp thăm khám (nghe phổi, soi họng); `診断（しんだん）する` = kết luận tên bệnh sau khi khám/xét nghiệm (`胃炎と診断された`). Rất hay ra cặp đối chiếu ở N2 nha!"),
            (5, "Từ cơ thể hay nhầm 💊", "`しびれる` (tê bì chân tay), `震（ふる）える` (run rẩy), `青白（あおじろ）い` (sắc mặt xanh xao tái nhợt), `こじらせる` (để bệnh kéo dài biến chứng nặng thêm). Đọc đoạn Sayuri chăm bệnh nhớ liền tay luôn!"),
        ],
        "paragraphs": [
            (
                "連日（れんじつ）の納期（のうき）による[[睡眠不足（すいみんぶそく）|23]]がたたったのか、海斗（かいと）は週明（しゅうあ）けからすっかり[[体調（たいちょう）|1]]を崩（くず）してしまった。軽（かる）い風邪（かぜ）だと思（おも）って無理（むり）をしたせいで、かえって[[症状（しょうじょう）|2]]を[[こじらせて|25]]しまったのだ。",
                "Chắc do thiếu ngủ liên tục vì chạy kịp hạn giao dự án, đầu tuần Kaito bỗng suy sụp sức khỏe hẳn. Nghĩ chỉ là cảm nhẹ nên cậu cố làm tiếp, ai ngờ lại khiến triệu chứng trở nặng kéo dài hơn."
            ),
            (
                "「うっ……寒気（さむけ）がして全身（ぜんしん）が[[震（ふる）える|8]]……」。朝（あさ）、[[血圧（けつあつ）|3]]を測（はか）る力（ちから）もなく玄関（げんかん）で靴（くつ）を履（は）こうと[[しゃがむ|27]]んだ瞬間（しゅんかん）、めまいで足（あし）が[[しびれて|7]]しまい、壁（かべ）に[[もたれて|26]]動（うご）けなくなった。鏡（かがみ）に映（うつ）った顔色（かおいろ）は[[青白（あおじろ）い|9]]、立（た）っているだけで強（つよ）い[[苦痛（くつう）|10]]を感（かん）じる。",
                "'Hic... lạnh buốt khiến toàn thân run rẩy...' — Buổi sáng, đến sức đo huyết áp cũng không còn; khoảnh khắc ngồi xổm xuống định xỏ giày trước cửa, cơn chóng mặt làm chân cậu tê dại đi, phải tựa lưng vào tường bất động. Khuôn mặt phản chiếu trong gương xanh xao nhợt nhạt, chỉ đứng thôi cũng cảm thấy đau đớn rã rời."
            ),
            (
                "なんとか近所（きんじょ）のクリニックへたどり着（つ）き、医師（いし）の[[診察（しんさつ）|11]]を受（う）けると、「過労（かろう）とウイルスに[[感染（かんせん）した|4]]発熱（はつねつ）ですね。他（ほか）の人（ひと）に[[伝染（でんせん）|5]]するおそれもありますから、十分（じゅうぶん）な[[休養（きゅうよう）|22]]をとってください」と[[診断（しんだん）|12]]された。",
                "Lê bước tới phòng khám gần nhà, sau khi được bác sĩ thăm khám, cậu nhận kết luận chẩn đoán: 'Cậu bị sốt do làm việc quá sức và nhiễm virus đấy. Còn có nguy cơ lây truyền sang người khác nên hãy nghỉ ngơi đầy đủ nhé'."
            ),
            (
                "さらに昨日（きのう）駅（えき）の階段（かいだん）で転（ころ）んで手首（てくび）を痛（いた）めたところも確認（かくにん）してもらった。「[[骨折（こっせつ）|6]]はしていませんし[[手術（しゅじゅつ）|18]]も不要（ふよう）ですが、[[治療（ちりょう）|13]]として擦（す）り傷（きず）を[[消毒（しょうどく）して|21]][[包帯（ほうたい）|19]]を巻（ま）いておきますね」。先生（せんせい）は解熱剤（げねつざい）を[[処方（しょほう）して|14]]くれた。",
                "Cậu cũng nhờ bác sĩ kiểm tra luôn cổ tay bị đau do ngã cầu thang ga hôm qua. 'Không bị gãy xương và cũng không cần phẫu thuật đâu, nhưng để điều trị ta sát trùng vết xước rồi quấn băng gạc lại cho chắc nhé'. Bác sĩ kê đơn thuốc hạ sốt cho cậu."
            ),
            (
                "部屋（へや）へ戻（もど）ってベッドに倒（たお）れ込（こ）んだ夜（よる）、チャイムが鳴（な）った。「海斗（かいと）先輩（せんぱい）、[[予防（よぼう）|20]]のためにマスクをしてお粥（かゆ）と薬（くすり）を持（も）ってきましたよ」。合鍵（あいかぎ）でも持（も）っているかのように、いつの間（ま）にか部屋（へや）の中（なか）で[[衛生的（えいせいてき）|24]]にキッチンを整（ととの）えている小百合（さゆり）の姿（すがた）に、海斗（かいと）は驚（おどろ）いた。",
                "Đêm đó khi vừa về phòng đổ gục xuống giường thì chuông cửa reo lên. 'Tiền bối Kaito ơi, để phòng ngừa lây nhiễm em đeo khẩu trang rồi mang cháo và thuốc tới cho anh nè'. Thấy Sayuri thoắt cái đã đứng trong nhà thu dọn căn bếp sạch sẽ hợp vệ sinh như thể cô ấy nắm sẵn chìa khóa dự phòng, Kaito giật mình kinh ngạc."
            ),
            (
                "「ありがとう……でもうつったら悪（わる）いから、もう帰（かえ）っていいよ」と言う海斗（かいと）の額（ひたい）に、小百合（さゆり）は冷（つめ）たい手（て）をそっと載（の）せた。「ダメですよ。先輩（せんぱい）が弱（よわ）っているときくらい、私（わたし）だけに[[看病（かんびょう）して|17]]させてください。ほら、この薬（くすり）はとてもよく[[効（き）く|16]]んです。ただし少し眠（ねむ）くなる[[副作用（ふくさよう）|15]]があるので……今夜（こんや）はずっとおそばにいてあげますね」――小百合（さゆり）の唇（くちびる）が、闇（やみ）の中（なか）で甘（あま）く微笑（ほほえ）んだ。",
                "'Cảm ơn em... nhưng lây sang em thì ngại lắm, em về đi cũng được' — vừa dứt lời, Sayuri khẽ đặt bàn tay mát lạnh lên trán Kaito: 'Không được đâu ạ. Ít nhất những lúc anh yếu đuối thế này, hãy để một mình em chăm sóc cho anh đi. Nào, thuốc này công hiệu lắm đấy. Chỉ có điều nó có chút tác dụng phụ gây buồn ngủ nên... tối nay em sẽ ở bên cạnh anh suốt đêm nhé' — đôi môi Sayuri mỉm cười ngọt ngào đầy bí ẩn trong bóng tối."
            ),
        ],
        "quiz": [
            {
                "prompt": "軽（かる）い風邪（かぜ）だと思（おも）って休（やす）まずに働（はたら）いていたら、かえって（　　）しまった。",
                "options": ["こじらせて", "消毒（しょうどく）して", "予防（よぼう）して", "処方（しょほう）して"],
                "ans": 1,
                "right_exp": "💖 Chính xác! Không chịu nghỉ ngơi làm bệnh kéo dài và nặng thêm là `こじらせる` (`風邪をこじらせる`).",
                "wrong_exps": [
                    "Chính xác: `こじらせる` = làm bệnh trở nặng, biến chứng kéo dài.",
                    "`消毒する` là khử trùng, sát khuẩn vết thương.",
                    "`予防する` là phòng ngừa bệnh trước khi mắc.",
                    "`処方する` là bác sĩ kê đơn thuốc."
                ]
            },
            {
                "prompt": "医師（いし）の診察（しんさつ）の結果（けっか）、ストレスによる胃炎（いえん）だと（　　）された。",
                "options": ["診断（しんだん）", "感染（かんせん）", "伝染（でんせん）", "看病（かんびょう）"],
                "ans": 1,
                "right_exp": "💖 Chuẩn rồi em! Sau bước khám (`診察`), bác sĩ kết luận bệnh gì gọi là `診断（しんだん）する`.",
                "wrong_exps": [
                    "Chính xác: `診断する` = chẩn đoán, kết luận tên bệnh.",
                    "`感染する` là bị nhiễm virus/vi khuẩn.",
                    "`伝染する` là lây lan bệnh từ người này sang người khác.",
                    "`看病する` là chăm sóc người bệnh."
                ]
            },
            {
                "prompt": "この薬（くすり）を飲（の）むと、とても眠（ねむ）くなるという（　　）があるそうだ。",
                "options": ["副作用（ふくさよう）", "症状（しょうじょう）", "苦痛（くつう）", "休養（きゅうよう）"],
                "ans": 1,
                "right_exp": "💖 Quá giỏi! Tác dụng ngoài ý muốn của thuốc (như buồn ngủ, khô miệng) gọi là `副作用（ふくさよう）`.",
                "wrong_exps": [
                    "Chính xác: `副作用` = tác dụng phụ của thuốc.",
                    "`症状` là triệu chứng của bệnh tật.",
                    "`苦痛` là nỗi đau đớn thể xác hoặc tinh thần.",
                    "`休養` là nghỉ ngơi hồi phục sức khỏe."
                ]
            },
            {
                "prompt": "床（ゆか）に（　　）で、落（お）とした鍵（かぎ）を拾（ひろ）った。",
                "options": ["しゃがん", "もたれ", "しびれ", "震（ふる）え"],
                "ans": 1,
                "right_exp": "💖 Đúng rồi em! Ngồi xổm xuống đất nhặt đồ dùng `しゃがむ` (chia thể て -> `しゃがんで`).",
                "wrong_exps": [
                    "Chính xác: `しゃがんで` = ngồi xổm xuống.",
                    "`もたれて` nghĩa là tựa lưng vào tường/ghế.",
                    "`しびれて` là bị tê bì tay chân.",
                    "`震えて` là run rẩy vì lạnh hoặc sợ."
                ]
            },
            {
                "prompt": "海斗（かいと）が風邪（かぜ）で寝込（ねこ）んだ夜（よる）、小百合（さゆり）が見（み）せた不気味（ぶきみ）で甘い行動（こうどう）とは何（なに）か。",
                "options": [
                    "まるで合鍵（あいかぎ）を持（も）っているかのように部屋（へや）に入（はい）り、今夜（こんや）ずっとそばにいると笑（ほほえ）んだこと",
                    "病院（びょういん）の診察（しんさつ）を無断（むだん）でキャンセルしたこと",
                    "玲奈（れいな）を部屋（へや）に呼（よ）んで二人（ふたり）で看病（かんびょう）したこと",
                    "海斗（かいと）に冷（つめ）たい氷（こおり）水（みず）を飲（の）ませて帰（かえ）ったこと"
                ],
                "ans": 1,
                "right_exp": "💖 Chuẩn không khí Yandere luôn! Cô ấy vào phòng tự nhiên như có chìa khóa riêng, dọn bếp sạch sẽ rồi cười bí ẩn bảo tối nay sẽ ở bên cạnh suốt đêm vì thuốc có tác dụng phụ gây buồn ngủ~",
                "wrong_exps": [
                    "Chính xác: Tự nhiên vào phòng như có chìa khóa riêng và tuyên bố ở bên suốt đêm.",
                    "Kaito đã tự đi khám bác sĩ từ ban ngày trước khi về nhà rồi nè.",
                    "Sayuri ghét cay ghét đắng Reina, tuyệt đối không bao giờ gọi Reina tới đâu!",
                    "Cô ấy mang cháo ấm và thuốc tới chăm sóc rồi ở lại luôn chứ không về đâu."
                ]
            },
        ]
    },
    {
        "num": 3,
        "slug": "chuong-03",
        "lesson_id": "p1_c06_b02",
        "title_jp": "第3章：[[消去（しょうきょ）|4]]された履歴（りれき）と、画面（がめん）越（ご）しの瞳（ひとみ）",
        "title_vi": "Chương 03: Lịch Sử Bị Xóa Sạch & Đôi Mắt Sau Màn Hình Máy Tính",
        "yuki_reminder_top": "Chương 3 cực kỳ gay cấn với trọn 24 từ **Bài 13 (Máy tính, Internet & Thao tác số)**! Kaito bắt đầu nghi ngờ chiếc laptop ở văn phòng của mình bị ai đó âm thầm theo dõi, kiểm tra từng file đã lưu (`保存`), xóa (`削除・消去`), gửi nhận (`送信・受信`), đính kèm (`添付`) và cài phần mềm (`インストール`)... 🖤💻",
        "yuki_reminder_bottom": "Ghê thật đó em, hóa ra cô nàng theo dõi cả email công việc để không cho ai tiếp cận Kaito! Nhớ phân biệt `削除（さくじょ）` (xóa file/dòng) với `消去（しょうきょ）` (xóa sạch dấu vết lịch sử) nha~ 🌸",
        "soft_notes": [
            (2, "Nhắc nhẹ thao tác máy tính 💻", "`起動（きどう）する` = mở máy/app; `立（た）ち上（あ）げる` = mở trình duyệt/khởi tạo phần mềm; `再起動（さいきどう）する` = khởi động lại (Restart). Ba từ hay đi cùng nhau cực kỳ dễ nhầm!"),
            (5, "Cặp phóng to – thu nhỏ & gửi mail 📎", "`拡大（かくだい）` (phóng to) ⇄ `縮小（しゅくしょう）` (thu nhỏ), `挿入（そうにゅう）` (chèn hình/bảng), `添付（てんぷ）する` (đính kèm tệp vào email), `閲覧（えつらん）する` (xem duyệt web/tài liệu)."),
        ],
        "paragraphs": [
            (
                "翌週（よくしゅう）、仕事（しごと）に復帰（ふっき）した海斗（かいと）が朝（あさ）デスクのパソコンを[[起動（きどう）する|21]]と、妙（みょう）な違和感（いわかん）を覚（おぼ）えた。いつも[[立（た）ち上（あ）げる|24]]ブラウザの[[設定（せってい）|8]]が勝手（かって）に変（か）わっており、昨夜（さくや）のアクセス履歴（りれき）まで誰（だれ）かにきれいに[[消去（しょうきょ）|4]]されていたのだ。",
                "Tuần sau quay lại làm việc, vừa khởi động máy tính trên bàn vào buổi sáng, Kaito đã cảm thấy một sự kỳ lạ khó tả. Cài đặt của trình duyệt cậu vẫn hay mở đã bị ai đó tự ý thay đổi, thậm chí toàn bộ lịch sử truy cập tối qua cũng bị xóa sạch hoàn toàn không còn dấu vết."
            ),
            (
                "「おかしいな……[[通信（つうしん）速度（そくど）|17]]も急（きゅう）に遅（おそ）いし」。[[ウイルス対策（たいさく）|20]]ソフトを開（ひら）いてチェックしても異常（いじょう）はない。念（ねん）のため一度（いちど）[[再起動（さいきどう）|22]]してから、Wi-Fiに[[接続（せつぞく）して|14]]メールボックスを確認（かくにん）してみた。",
                "'Lạ thật đấy... tốc độ đường truyền mạng tự dưng cũng chậm hẳn lại'. Cậu mở phần mềm chống virus ra quét thử nhưng chẳng báo lỗi gì. Để chắc ăn, cậu khởi động lại máy một lần rồi kết nối Wi-Fi để kiểm tra hộp thư điện tử."
            ),
            (
                "すると、[[受信（じゅしん）|12]]トレイにあったはずの玲奈（れいな）からの連絡（れんらく）メールが[[削除（さくじょ）|3]]されているではないか。それどころか、自分が企画（きかく）書（しょ）を[[作成（さくせい）|1]]して[[保存（ほぞん）した|2]]フォルダの中身（なかみ）を[[検索（けんさく）|15]]してみると、見知（みし）らぬPDFが[[添付（てんぷ）|13]]された下書（したが）きが残（のこ）っていた。",
                "Thế nhưng, email liên lạc từ Reina vốn nằm trong hộp thư đến lại biến mất như bị xóa bỏ mất rồi. Không chỉ vậy, khi tìm kiếm trong thư mục chứa bản kế hoạch cậu vừa tạo lập và lưu hôm qua, cậu phát hiện một bản nháp lạ hoắc có đính kèm file PDF không rõ nguồn gốc."
            ),
            (
                "「誰（だれ）がこんなことを……」。慌（あわ）ててファイルを[[ダウンロード|18]]し、[[操作（そうさ）|23]]して開（ひら）いてみる。資料（しょるい）は読みやすい[[フォント|10]]で組（く）まれ、本文（ほんぶん）の最後（さいご）に小さな画像（がぞう）が[[挿入（そうにゅう）|5]]されていた。サイズを[[縮小（しゅくしょう）|7]]してあったその画像（がぞう）を、海斗（かいと）は[[拡大（かくだい）して|6]]見（み）た瞬間（しゅんかん）、息（いき）が止（と）まった。",
                "'Ai đã làm trò này vậy trời...' — Cậu vội tải tệp đó về máy rồi thao tác mở ra xem. Tài liệu được trình bày bằng phông chữ cực kỳ dễ nhìn, và cuối văn bản có chèn một bức ảnh nhỏ xíu. Khoảnh khắc phóng to bức ảnh vốn đã bị thu nhỏ kích thước ấy lên, Kaito như chết lặng nín thở."
            ),
            (
                "それは、昨夜（さくや）のレストランで玲奈（れいな）と海斗（かいと）が話（はな）していた写真（しゃしん）を[[プリントアウト|9]]して、赤いペンで玲奈（れいな）の顔（かお）だけ塗り（ぬり）つぶしたものだった。ファイルの作成者（さくせいしゃ）名（めい）を[[閲覧（えつらん）する|16]]と、そこには『Sayuri』の文字（もじ）が静（しず）かに光（ひか）っていた。",
                "Đó là bức ảnh chụp Kaito và Reina nói chuyện ở nhà hàng tối qua được in ra giấy rồi bị tô kín khuôn mặt của Reina bằng mực đỏ. Khi xem phần tên tác giả tạo tệp, dòng chữ 'Sayuri' lặng lẽ hiện lên sáng rực trước mắt cậu."
            ),
            (
                "「先輩（せんぱい）、コーヒーお待（ま）ちしました♪」。背（せ）後（ご）から囁（ささや）く声（こえ）に振（ふ）り向（む）くと、小百合（さゆり）が天使（てんし）のように笑（わら）っていた。「あの……昨日（きのう）新（あたら）しい管理（かんり）アプリを[[インストール|19]]しておきましたから、これからは変（へん）なメールは自動（じどう）で消（き）えるようになりますよ。これで私（わたし）以外（いがい）の雑音（ざつおん）は、もう[[送信（そうしん）|11]]されてきませんから安心（あんしん）してくださいね？」",
                "'Tiền bối ơi, cà phê của anh tới rồi đây♪'. Giật mình quay lại trước giọng thì thầm ngay sau lưng, cậu thấy Sayuri đang mỉm cười hiền như thiên thần. 'À... hôm qua em cài đặt sẵn ứng dụng quản lý mới vào máy cho anh rồi đó, từ giờ mấy email kỳ quặc sẽ tự động biến mất hết. Như vậy sẽ chẳng còn tạp âm nào ngoài em gửi tới được nữa, anh cứ yên tâm nha?'"
            ),
        ],
        "quiz": [
            {
                "prompt": "履歴書（りれきしょ）のPDFファイルをメールに（　　）して送信（そうしん）した。",
                "options": ["添付（てんぷ）", "挿入（そうにゅう）", "閲覧（えつらん）", "消去（しょうきょ）"],
                "ans": 1,
                "right_exp": "💖 Chính xác! Đính kèm file vào email gửi đi dùng `添付（てんぷ）する`.",
                "wrong_exps": [
                    "Chính xác: `添付する` = đính kèm tệp vào thư/hồ sơ.",
                    "`挿入する` là chèn ảnh/biểu đồ vào giữa nội dung văn bản (Word/tài liệu).",
                    "`閲覧する` là xem/duyệt trang web hoặc tài liệu.",
                    "`消去する` là xóa sạch dữ liệu."
                ]
            },
            {
                "prompt": "パソコンの画面（がめん）が固（かた）まって動（うご）かないので、一度（いちど）（　　）することにした。",
                "options": ["再起動（さいきどう）", "保存（ほぞん）", "検索（けんさく）", "拡大（かくだい）"],
                "ans": 1,
                "right_exp": "💖 Quá chuẩn! Máy bị treo đơ cần khởi động lại (Restart) dùng `再起動（さいきどう）`.",
                "wrong_exps": [
                    "Chính xác: `再起動` = khởi động lại máy.",
                    "`保存` là lưu dữ liệu.",
                    "`検索` là tìm kiếm thông tin.",
                    "`拡大` là phóng to ảnh/màn hình."
                ]
            },
            {
                "prompt": "細（こま）かい文字（もじ）がよく見（み）えないので、画面（がめん）を（　　）して読（よ）んだ。",
                "options": ["拡大（かくだい）", "縮小（しゅくしょう）", "削除（さくじょ）", "受信（じゅしん）"],
                "ans": 1,
                "right_exp": "💖 Chuẩn rồi em! Phóng to chữ nhỏ cho dễ đọc là `拡大（かくだい）する` (trái nghĩa là `縮小` = thu nhỏ).",
                "wrong_exps": [
                    "Chính xác: `拡大する` = phóng to.",
                    "`縮小する` là thu nhỏ lại — ngược nghĩa rồi nè!",
                    "`削除する` là xóa bỏ file/dòng.",
                    "`受信する` là nhận email/tín hiệu."
                ]
            },
            {
                "prompt": "重要（じゅうよう）なファイルが消（き）えないように、USBメモリにもデータを（　　）しておこう。",
                "options": ["保存（ほぞん）", "接続（せつぞく）", "操作（そうさ）", "送信（そうしん）"],
                "ans": 1,
                "right_exp": "💖 Tuyệt vời! Lưu trữ dữ liệu an toàn dùng `保存（ほぞん）する`.",
                "wrong_exps": [
                    "Chính xác: `保存する` = lưu dữ liệu.",
                    "`接続する` là kết nối mạng/thiết bị.",
                    "`操作する` là thao tác điều khiển thiết bị.",
                    "`送信する` là gửi tin/email đi."
                ]
            },
            {
                "prompt": "小百合（さゆり）が海斗（かいと）のパソコンに勝手（かって）にアプリをインストールした本当（ほんとう）の目的（もくてき）は何（なに）か。",
                "options": [
                    "海斗（かいと）と玲奈（れいな）など他（ほか）の女性（じょせい）との連絡（れんらく）を遮断（しゃだん）し、自分（じぶん）だけのものにするため",
                    "通信（つうしん）速度（そくど）を速（はや）くして仕事（しごと）を手伝（てつだ）うため",
                    "ウイルス対策（たいさく）をしてお礼（れい）をもらうため",
                    "きれいなフォントを増（ふ）やしてあげるため"
                ],
                "ans": 1,
                "right_exp": "💖 Rợn nhẹ sống lưng luôn ha~ Cô ấy cài phần mềm theo dõi để tự động xóa email từ người khác (đặc biệt là Reina), cô lập Kaito chỉ còn nghe thấy tiếng của mình thôi!",
                "wrong_exps": [
                    "Chính xác: Kiểm soát và chặn liên lạc của Kaito với những phụ nữ khác.",
                    "Không phải giúp tăng tốc mạng đâu, thậm chí máy còn chạy chậm hẳn đi vì phần mềm theo dõi đó!",
                    "Phần mềm chống virus của Kaito không báo lỗi, đây là app quản lý theo dõi riêng của Sayuri.",
                    "Cô ấy không hề cài phông chữ mà là xóa lịch sử và chặn email đấy."
                ]
            },
        ]
    },
    {
        "num": 4,
        "slug": "chuong-04",
        "lesson_id": "p1_c07_b02",
        "title_jp": "第4章：停電（ていでん）の[[災害（さいがい）|14]]と、密室（みっしつ）の[[警戒（けいかい）|21]]",
        "title_vi": "Chương 04: Đêm Mất Điện Vì Thiên Tai & Sự Cảnh Giác Trong Căn Phòng Kín",
        "yuki_reminder_top": "Chương 4 đưa hai người mắc kẹt cùng nhau trong đêm mưa bão mất điện với trọn 24 từ **Bài 15 (Sự kiện hình sự, Tai nạn & Thiên tai)**! Từ tội phạm (`事件・犯人・逮捕・取り調べる・盗難・詐欺`), tai nạn (`負傷・人身事故・転落・故障・救助`) đến động đất – sóng thần – lũ lụt (`地震・津波・洪水・土砂崩れ・火災・避難・復旧`)! ⚡🌧️",
        "yuki_reminder_bottom": "Kaito vừa phát hiện ra bí mật rợn người ngay trong cơn bão luôn rồi! Chú ý cặp đồng âm cực hay thi `避難（ひなん）` (sơ tán lánh nạn) vs `非難（ひなん）` (chỉ trích phê phán) nhé em! 🌸",
        "soft_notes": [
            (2, "Nhắc nhẹ từ bản tin sự cố 🚨", "`盗難（とうなん）に遭（あ）う` (bị mất trộm), `被害（ひがい）に遭（あ）う` (chịu thiệt hại), `詐欺（さぎ）` (lừa đảo), `目撃（もくげき）する` (tận mắt chứng kiến). Cả cụm `〜に遭う` đều mang nghĩa gặp chuyện xui xẻo nhé em!"),
            (5, "Bộ thiên tai hay thi JLPT 🌪️", "`地震（じしん）` (động đất), `津波（つなみ）` (sóng thần), `洪水（こうずい）` (lũ lụt), `土砂崩（どしゃくず）れ` (sạt lở đất), `火災（かさい）` (hỏa hoạn), `復旧（ふっきゅう）する` (khôi phục lại điện/tàu). Nhớ cả bộ phòng khi đọc tin Nhật nữa nha~"),
        ],
        "paragraphs": [
            (
                "玲奈（れいな）が突然（とつぜん）会社（かいしゃ）を辞（や）めて引（ひ）っ越（こ）した直後（ちょくご）、海斗（かいと）は部屋（へや）の合鍵（あいかぎ）が一本（いっぽん）なくなっている[[盗難（とうなん）|5]]に気づ（きづ）いた。まるでミステリーの[[事件（じけん）|1]]のようで、[[犯人（はんにん）|2]]は誰（だれ）なのか頭（あたま）を巡（めぐ）らせていた夕方（ゆうがた）、街（まち）を巨大（きょだい）な台風（たいふう）が襲（おそ）った。",
                "Ngay sau khi Reina đột ngột nghỉ việc và chuyển nhà, Kaito phát hiện một chiếc chìa khóa dự phòng trong phòng mình đã bị mất trộm. Chẳng khác gì một vụ án trinh thám, đúng buổi chiều cậu đang vắt óc suy nghĩ xem thủ phạm là ai thì một cơn bão khổng lồ đổ bộ xuống thành phố."
            ),
            (
                "スマホに緊急（きんきゅう）[[警報（けいほう）|22]]が鳴（な）り響（ひび）く。「今夜（こんや）は[[災害（さいがい）|14]]への[[防災（ぼうさい）|24]]準備（じゅんび）を！　川（かわ）が氾濫（はんらん）すれば[[洪水（こうずい）|17]]、山側（やまがわ）では[[土砂崩（どしゃくず）れ|18]]のおそれがあり、湾岸（わんがん）部（ぶ）では[[地震（じしん）|15]]や[[津波（つなみ）|16]]並（な）みの高潮（たかしお）に[[警戒（けいかい）して|21]]ください！」",
                "Điện thoại reo vang cảnh báo khẩn cấp: 'Tối nay xin hãy chuẩn bị phòng chống thiên tai! Có nguy cơ lũ lụt do sông tràn bờ và sạt lở đất ở vùng núi; khu vực ven vịnh xin cảnh giác cao độ trước triều cường dữ dội như động đất và sóng thần!'."
            ),
            (
                "帰り道（かえりみち）、海斗（かいと）の乗（の）った電車（でんしゃ）が[[人身事故（じんしんじこ）|10]]と踏切（ふみきり）の信号（しんごう）[[故障（こしょう）|12]]で止（と）まってしまった。駅前（えきまえ）でホームから人が[[転落（てんらく）して|11]][[負傷（ふしょう）する|9]]瞬間（しゅんかん）を[[目撃（もくげき）し|7]]た海斗（かいと）が、駅員（えきいん）と一緒（いっしょ）に[[救助（きゅうじょ）する|13]]手伝（てつだ）いをしていると、突然（とつぜん）街（まち）全体（ぜんたい）が停電（ていでん）した。",
                "Trên đường về, chuyến tàu Kaito đi phải dừng lại vì tai nạn có người gặp nạn và sự cố hỏng đèn tín hiệu. Vừa chứng kiến cảnh một hành khách trượt chân ngã xuống đường ray bị thương, Kaito liền cùng nhân viên nhà ga chạy tới cứu hộ, đúng lúc ấy cả thành phố bất ngờ mất điện tối om."
            ),
            (
                "「避難所（ひなんじょ）へ[[避難（ひなん）しよう|20]]……」と雨（あめ）の中（なか）を歩（ある）き出（だ）した海斗（かいと）の腕（うで）を、傘（かさ）を差（さ）した小百合（さゆり）がぎゅっと掴（つか）んだ。「先輩（せんぱい）！　外（そと）は近所（きんじょ）で[[火災（かさい）|19]]も起（お）きているし、こんな嵐（あらし）の中（なか）を歩（ある）いたら[[被害（ひがい）に遭（あ）います|8]]よ。電気（でんき）が[[復旧（ふっきゅう）する|23]]まで、私（わたし）のマンションへ来（き）てください！」",
                "'Phải đi sơ tán tới nơi trú ẩn thôi...' — Kaito vừa định dầm mưa bước đi thì bị Sayuri che ô chạy tới nắm chặt lấy cánh tay: 'Tiền bối ơi! Ngoài kia gần đây còn xảy ra cả hỏa hoạn nữa đấy, đi giữa bão thế này anh sẽ gặp tai họa mất. Cho đến khi có điện khôi phục trở lại, hãy sang căn hộ của em lánh tạm đi!'."
            ),
            (
                "半（はん）ば強引（ごういん）に部屋（へや）へ招（まね）かれた海斗（かいと）は、小百合（さゆり）が淹（い）れてくれた紅茶（こうちゃ）を飲（の）みながら、ふとリビングのガラスケースに目（め）が留（と）まった。そこには見覚（みおぼ）えのある銀色（ぎんいろ）の鍵（かぎ）と、海斗（かいと）のマグカップやペンが並（なら）んでいた。",
                "Bị kéo nửa ép nửa dỗ vào căn hộ, Kaito vừa nhấp ngụm hồng trà Sayuri pha cho thì ánh mắt chợt khựng lại trước chiếc tủ kính ở phòng khách. Bên trong đó bày ngay ngắn một chiếc chìa khóa bạc quen thuộc cùng chiếc cốc và cây bút cậu từng làm mất."
            ),
            (
                "「これ……俺（おれ）の合鍵（あいかぎ）じゃないか！？　詐欺（さぎ）というか、まさか犯人（はんにん）は……」と言（い）いかけて振り返（ふりかえ）ると、小百合（さゆり）が窓（まど）の鍵（かぎ）をカチャリと閉（し）めた。「ええ、警察（けいさつ）に[[逮捕（たいほ）され|3]]て[[取（と）り調（しら）べられ|4]]ても構（かま）いません。それに[[詐欺（さぎ）|6]]なんかじゃありませんよ――私（わたし）が先輩（せんぱい）を愛（あい）しているのは本当（ほんとう）なんですから。嵐（あらし）が止（や）むまで、二人（ふたり）きりでいましょうね？」",
                "'Cái này... chẳng phải chìa khóa dự phòng của anh sao?! Lừa đảo hay thủ phạm chẳng lẽ là...' — Kaito vừa định quay lại thì nghe tiếng Sayuri bấm khóa cửa sổ cái tách. 'Vâng, dù có bị cảnh sát bắt giữ và thẩm vấn em cũng chẳng ngại đâu. Với lại chẳng phải lừa đảo gì hết — chuyện em yêu tiền bối là thật lòng trăm phần trăm mà. Cho đến khi cơn bão tan, hai ta cứ ở riêng bên nhau nhé?'"
            ),
        ],
        "quiz": [
            {
                "prompt": "台風（たいふう）で停電（ていでん）していたが、作業（さぎょう）のおかげでようやく電気（でんき）が（　　）した。",
                "options": ["復旧（ふっきゅう）", "避難（ひなん）", "転落（てんらく）", "故障（こしょう）"],
                "ans": 1,
                "right_exp": "💖 Chính xác! Điện, nước, tàu xe hoạt động trở lại bình thường sau sự cố là `復旧（ふっきゅう）する`.",
                "wrong_exps": [
                    "Chính xác: `復旧する` = khôi phục hạ tầng hoạt động lại bình thường.",
                    "`避難する` là sơ tán lánh nạn tới nơi an toàn.",
                    "`転落する` là rơi ngã từ trên cao xuống.",
                    "`故障する` là bị hỏng hóc thiết bị máy móc."
                ]
            },
            {
                "prompt": "電車（でんしゃ）や電話（でんわ）でお金（かね）をだまし取（と）る（　　）事件（じけん）に気（き）をつけよう。",
                "options": ["詐欺（さぎ）", "盗難（とうなん）", "火災（かさい）", "洪水（こうずい）"],
                "ans": 1,
                "right_exp": "💖 Chuẩn rồi em! Lừa đảo chiếm đoạt tài sản qua điện thoại/mạng là `詐欺（さぎ）`.",
                "wrong_exps": [
                    "Chính xác: `詐欺` = trò lừa đảo.",
                    "`盗難` là mất trộm lén lút khi chủ không biết.",
                    "`火災` là vụ cháy hỏa hoạn.",
                    "`洪水` là lũ lụt."
                ]
            },
            {
                "prompt": "津波（つなみ）警報（けいほう）が出（で）たら、すぐに高（たか）い場所（ばしょ）へ（　　）してください。",
                "options": ["避難（ひなん）", "逮捕（たいほ）", "目撃（もくげき）", "負傷（ふしょう）"],
                "ans": 1,
                "right_exp": "💖 Tuyệt vời! Sơ tán lánh nạn lên nơi cao an toàn là `避難（ひなん）する`.",
                "wrong_exps": [
                    "Chính xác: `避難する` = sơ tán, lánh nạn.",
                    "`逮捕する` là cảnh sát bắt giữ tội phạm.",
                    "`目撃する` là chứng kiến tận mắt.",
                    "`負傷する` là bị thương."
                ]
            },
            {
                "prompt": "山（やま）の近（ちか）くでは、大雨（おおあめ）による（　　）に警戒（けいかい）する必要（ひつよう）がある。",
                "options": ["土砂崩（どしゃくず）れ", "人身事故（じんしんじこ）", "盗難（とうなん）", "救助（きゅうじょ）"],
                "ans": 1,
                "right_exp": "💖 Quá giỏi! Mưa lớn vùng núi hay gây ra sạt lở đất đá `土砂崩れ`.",
                "wrong_exps": [
                    "Chính xác: `土砂崩れ` = sạt lở đất đá.",
                    "`人身事故` là tai nạn giao thông có thương vong người (thường hay báo trên tàu điện).",
                    "`盗難` là mất trộm.",
                    "`救助` là công tác cứu hộ."
                ]
            },
            {
                "prompt": "小百合（さゆり）のマンションのガラスケースを見（み）て、海斗（かいと）は何（なに）に気づ（きづ）いたのか。",
                "options": [
                    "なくしたはずの自分（じぶん）の合鍵（あいかぎ）や私物（しぶつ）を、小百合（さゆり）が密（ひそ）かに集（あつ）めていたこと",
                    "小百合（さゆり）が防災（ぼうさい）訓練（くんれん）の賞状（しょうじょう）を飾（かざ）っていたこと",
                    "玲奈（れいな）が部屋（へや）の中に隠（かく）れていたこと",
                    "電気（でんき）がすでに復旧（ふっきゅう）していたこと"
                ],
                "ans": 1,
                "right_exp": "💖 Căng thẳng tột độ luôn! Chiếc chìa khóa dự phòng bị mất trộm cùng cốc và bút của Kaito được Sayuri trưng bày gọn gàng trong tủ kính nhà cô ấy đó!",
                "wrong_exps": [
                    "Chính xác: Phát hiện bộ sưu tập chìa khóa và đồ dùng cá nhân của mình trong tủ kính.",
                    "Không phải bằng khen phòng chống thiên tai nào cả nhé.",
                    "Reina đã nghỉ việc chuyển đi từ đầu chương rồi nè.",
                    "Cả khu phố vẫn đang mất điện giữa cơn bão."
                ]
            },
        ]
    },
    {
        "num": 5,
        "slug": "chuong-05",
        "lesson_id": "p2_c01_b01",
        "title_jp": "第5章：[[鍵（かぎ）がかかる|7]]部屋（へや）と、震（ふる）える[[ため息（いき）|10]]",
        "title_vi": "Chương 05: Căn Phòng Bị Khóa Trái & Tiếng Thở Dài Run Rẩy",
        "yuki_reminder_top": "Chương 5 bước vào thế giới từ đa nghĩa siêu quan trọng của **Bài 22 (Từ đa nghĩa — Động từ Phần 1)**! Lưu ý chương này có đủ cả **hai nghĩa (1) và (2)** của `上がる`, `受ける`, `かかる`, `つく`, `取る`, `乗る` luôn nha em! Bấm vào từng từ để thấy sự khác biệt giữa nghĩa đen và nghĩa bóng nhé 🔑🖤",
        "yuki_reminder_bottom": "Vượt qua 16 sắc thái động từ đa nghĩa rồi đó em~ Đừng quên: `相談に乗る` = lắng nghe tư vấn, `嘘をつく` = nói dối, `期限が切れる` = hết hạn, `ステージで上がる` = bị run khớp trên sân khấu! 🌸",
        "soft_notes": [
            (2, "Nhắc nhẹ từ đa nghĩa (1) vs (2) 🔑", "Để ý kỹ nè em: `雨（あめ）が上（あ）がる` (tạnh mưa) là `上がる(1)`, còn `緊張（きんちょう）して上（あ）がる` (bị run mất bình tĩnh) là `上がる(2)`! Bấm vào từng chữ trong truyện để xem nghĩa đúng ngữ cảnh nha!"),
            (5, "Cặp đa nghĩa siêu hay thi ✨", "`嘘（うそ）をつく` (nói dối) / `ため息（いき）をつく` (thở dài) vs `しみ・癖（くせ）がつく` (dính vết / thành thói quen); `期限（きげん）が切（き）れる` (hết hạn); `気（き）が利（き）く` (tinh tế biết ý). Toàn câu chốt điểm Mondai 5!"),
        ],
        "paragraphs": [
            (
                "朝（あさ）になると、ようやく激しい[[雨（あめ）が上（あ）がった|1]]。だが、海斗（かいと）の心（こころ）には重苦（おもくる）しい不安（ふあん）が拭（ぬぐ）えなかった。リビングのドアにしっかり[[鍵（かぎ）がかかって|7]]おり、勝手（かって）に出（で）られない気配（けはい）がしたからだ。",
                "Sáng hôm sau, cơn mưa dữ dội cuối cùng cũng tạnh. Thế nhưng trong lòng Kaito vẫn chẳng xua tan nổi nỗi bất an nặng nề, bởi cậu cảm nhận rõ cánh cửa phòng khách đã bị khóa chặt từ bên trong không thể tùy ý bước ra."
            ),
            (
                "「おはよう、海斗（かいと）先輩（せんぱい）。昨日（きのう）の緊張（きんちょう）で頭（あたま）が[[上（あ）がって|2]]いませんか？　ほら、朝（あさ）ご飯（はん）ができたら[[席（せき）を空（あ）けて|3]]待（ま）ってますからね」。小百合（さゆり）はエプロン姿（すがた）で微笑（ほほえ）み、スープの湯気（ゆげ）が立（た）つテーブルを指（ゆび）さした。",
                "'Chào buổi sáng, tiền bối Kaito. Hôm qua căng thẳng quá có làm anh bị run mệt không ạ? Nào, nấu xong bữa sáng rồi em chừa sẵn chỗ ngồi chờ anh đấy nhé'. Sayuri mỉm cười trong bộ tạp dề, chỉ về phía bàn ăn đang bốc khói nghi ngút."
            ),
            (
                "海斗（かいと）は[[ため息（いき）をつき|10]]ながら椅子（いす）に座（すわ）った。「小百合（さゆり）、どうしてこんなことをするんだ。もし僕（ぼく）が警察（けいさつ）に[[連絡（れんらく）をとっ|12]]たらどうなるか……」と言（い）う海斗（かいと）に、小百合（さゆり）は静（しず）かに首（くび）を振（ふ）った。",
                "Kaito vừa thở dài vừa ngồi xuống ghế: 'Sayuri này, tại sao em lại làm như vậy? Nếu anh giữ liên lạc với cảnh sát thì chuyện gì sẽ xảy ra...' — nghe Kaito nói vậy, Sayuri khẽ lắc đầu."
            ),
            (
                "「私（わたし）、[[嘘（うそ）をつく|10]]のが嫌（きら）いなんです。ただ、あのまま玲奈（れいな）さんに[[影響（えいきょう）を受（う）け|4]]て先輩（せんぱい）が離（はな）れていくのを見（み）ていられなかっただけ。だって昔（むかし）、先輩（せんぱい）が冗談（じょうだん）でみんなに[[受（う）けて|5]]笑（わら）っていたときも、本当（ほんとう）はずっと寂（さび）しそうだったじゃないですか」",
                "'Em ghét nói dối lắm ạ. Chỉ là em không thể ngồi yên nhìn anh chịu ảnh hưởng từ chị Reina rồi rời xa em dần thôi. Vì ngày xưa lúc anh đùa vui khiến mọi người hưởng ứng cười rộ lên, thực ra trông anh vẫn luôn cô đơn lắm mà đúng không?'"
            ),
            (
                "「それは……」。図星（ずぼし）を突（つ）かれて言葉（ことば）に詰（つ）まる海斗（かいと）の手（て）を、小百合（さゆり）がそっと[[取（と）り|11]]、熱（あつ）い紅茶（こうちゃ）を差し出（さしだ）した。「ほら、[[気（き）が利（き）く|8]]と言（い）われる私（わたし）のお手製（てせい）ハーブティー。風邪（かぜ）によく[[効（き）く|8]]し、心（こころ）に[[癖（くせ）がつく|9]]ほど温（あたた）まりますよ」",
                "'Cái đó...' — bị nói trúng tim đen khiến Kaito nghẹn lời. Sayuri dịu dàng nắm lấy tay cậu rồi đưa tách trà thảo mộc nóng hổi: 'Nào, trà do em tự pha vốn được khen là tinh tế lắm đấy. Thuốc công hiệu cho bệnh cảm mà trà này cũng ấm đến mức dễ thành thói quen luôn nha'."
            ),
            (
                "「でも、僕（ぼく）は部屋（へや）の家賃（やちん）や契約（けいやく）の[[期限（きげん）が切（き）れる|16]]前（まえ）に帰（かえ）らなきゃいけないんだ。それに、この先（さき）ずっとここには住（す）めない。時間（じかん）も[[手間（てま）もかかる|6]]し、僕（ぼく）なんか小百合（さゆり）に[[向（む）いて|15]]いないよ」",
                "'Nhưng anh phải về trước khi hợp đồng thuê nhà hết hạn nữa. Với lại anh không thể ở đây mãi thế này được. Tốn thời gian và công sức lắm, một người như anh đâu có hợp với em'."
            ),
            (
                "小百合（さゆり）は少（すこ）しも動（どう）じず、海斗（かいと）の隣（となり）に腰（こし）を下（お）ろした。「大丈夫（だいじょうぶ）です。今（いま）は時代（じだい）の[[流（なが）れに乗（の）って|13]]在宅（ざいたく）ワークだってできますし、先輩（せんぱい）の[[相談（そうだん）に乗（の）って|14]]あげられるのも、この世（よ）で私（わたし）だけなんですから。もう少しだけ、二人（ふたり）で休（やす）みましょうね？」",
                "Sayuri chẳng hề nao núng, nhẹ nhàng ngồi xuống sát bên Kaito: 'Không sao đâu ạ. Giờ bắt kịp xu thế thời đại làm việc từ xa tại nhà cũng được mà, với lại người duy nhất trên đời này sẵn sàng lắng nghe tư vấn cho anh chỉ có mình em thôi. Mình nghỉ ngơi riêng hai đứa thêm chút nữa nhé?'."
            ),
        ],
        "quiz": [
            {
                "prompt": "みんなの視線（しせん）が気（き）になって、スピーチの舞台（ぶたい）で緊張（きんちょう）して（　　）しまった。",
                "options": ["上（あ）がって", "切（き）れて", "向（む）いて", "空（あ）けて"],
                "ans": 1,
                "right_exp": "💖 Chính xác! Nghĩa bóng (2) của `上がる`: bị run lúng túng mất bình tĩnh trước đám đông (`緊張して上がる`).",
                "wrong_exps": [
                    "Chính xác: `上がる（2）` = hồi hộp run đến cứng người trước đám đông.",
                    "`切れる` là đứt, hết hạn (`期限が切れる`).",
                    "`向く` là hướng về hoặc phù hợp năng khiếu (`私に向いている`).",
                    "`空ける` là để trống chỗ (`席を空ける`)."
                ]
            },
            {
                "prompt": "進路（しんろ）について悩（なや）んでいたら、親切（しんせつ）な先輩（せんぱい）が親身（しんみ）に（　　）くれた。",
                "options": ["相談（そうだん）に乗（の）って", "嘘（うそ）をついて", "癖（くせ）がついて", "手間（てま）がかかって"],
                "ans": 1,
                "right_exp": "💖 Quá giỏi! Cụm đa nghĩa cố định: `相談に乗る` = lắng nghe và tư vấn giúp ai đó.",
                "wrong_exps": [
                    "Chính xác: `相談に乗る` = nhiệt tình lắng nghe tư vấn.",
                    "`嘘をつく` là nói dối.",
                    "`癖がつく` là hình thành thói quen/tật.",
                    "`手間がかかる` là tốn nhiều công sức thời gian."
                ]
            },
            {
                "prompt": "図書館（としょかん）から借（か）りた本（ほん）の返却（へんきゃく）（　　）ので、急（いそ）いで返（かえ）しに行（い）った。",
                "options": ["期限（きげん）が切（き）れた", "雨（あめ）が上（あ）がった", "鍵（かぎ）がかかった", "ため息（いき）をついた"],
                "ans": 1,
                "right_exp": "💖 Chuẩn rồi em! Hết hạn trả sách / hợp đồng dùng `期限が切れる`.",
                "wrong_exps": [
                    "Chính xác: `期限が切れる` = hết thời hạn.",
                    "`雨が上がる` là trời tạnh mưa.",
                    "`鍵がかかる` là cửa bị khóa.",
                    "`ため息をつく` là thở dài."
                ]
            },
            {
                "prompt": "新（あたら）しく開発（かいはつ）したコメディ企画（きかく）は、若いお客（きゃく）さんにすごく（　　）大好評（だいこうひょう）だった。",
                "options": ["受（う）けて", "かかって", "取（と）って", "向（む）いて"],
                "ans": 1,
                "right_exp": "💖 Đúng rồi! Nghĩa mở rộng (2) của `受ける`: được khán giả hưởng ứng nồng nhiệt, gây cười (`観客に受ける`).",
                "wrong_exps": [
                    "Chính xác: `受ける（2）` = được đón nhận, gây cười hưởng ứng.",
                    "`かかる` nghĩa là mắc bệnh / tốn công / bị khóa.",
                    "`取る` là cầm lấy / lấy chứng chỉ / giữ liên lạc.",
                    "`向く` là hợp với bản thân (`仕事に向いている`)."
                ]
            },
            {
                "prompt": "小百合（さゆり）の優（やさ）しい言葉（ことば）を聞（き）いても、なぜ海斗（かいと）は不安（ふあん）を感じたのか。",
                "options": [
                    "ドアに鍵（かぎ）がかかっていて外（そと）に出（で）られず、外部（がいぶ）との連絡（れんらく）も遮断（しゃだん）されそうだったから",
                    "朝（あさ）ご飯（はん）のハーブティーの味（あじ）が苦（にが）すぎたから",
                    "家賃（やちん）が高（たか）すぎて払（はら）えなかったから",
                    "雨（あめ）がまだ止（や）まずに雷（かみなり）が鳴（な）っていたから"
                ],
                "ans": 1,
                "right_exp": "💖 Chính xác! Dù ngoài mặt Sayuri pha trà nấu sáng dịu dàng hết nấc, nhưng cánh cửa bị khóa và ý định giữ Kaito làm việc tại nhà tách biệt hoàn toàn với thế giới bên ngoài khiến cậu lạnh người.",
                "wrong_exps": [
                    "Chính xác: Cảm giác bị giam lỏng trong căn phòng khóa trái.",
                    "Trà thảo mộc còn được khen dịu ấm, không phải vì vị đắng đâu nè.",
                    "Hợp đồng nhà là lý do Kaito viện ra để xin về chứ không phải vì tiền thuê đắt.",
                    "Trời đã tạnh mưa ngay từ câu mở đầu chương (`雨が上がった`) rồi nhé!"
                ]
            },
        ]
    },
    {
        "num": 6,
        "slug": "chuong-06",
        "lesson_id": "p2_c01_b02",
        "title_jp": "第6章：[[心（こころ）に残（のこ）る|10]]言葉（ことば）と、[[手（て）を引（ひ）く|14]]ことのできない罠（わな）",
        "title_vi": "Chương 06: Lời Nói Đọng Lại Trong Tim & Cái Bẫy Không Thể Rút Lui",
        "yuki_reminder_top": "Chương 6 tiếp tục chinh phục 15 mục **Bài 23 (Từ đa nghĩa — Động từ Phần 2)**! Chú ý đủ các nghĩa mở rộng siêu hay gặp của `落ちる`, `変える・換える`, `過ぎる`, `進む`, `通る`, `直す・治す`, `払う`, `引く`, `抜く` nha! ⚡🖤",
        "yuki_reminder_bottom": "Kịch tính quá trời luôn! Em nhớ khắc sâu hai cụm hay xuất hiện nhất ở Mondai 5: `注意（ちゅうい）を払（はら）う` (hết sức chú ý) và `筋（すじ）が通（とお）る` (có lý, logic) trước khi giải 5 câu quiz nhé! 🌸",
        "soft_notes": [
            (2, "Đa nghĩa hay thi nhất JLPT 🎯", "`時計（とけい）が5分（ごふん）進（すす）む` (đồng hồ chạy nhanh 5 phút), `色（いろ）や味（あじ）が落（お）ちる` (phai màu / hương vị giảm sút), `主張（しゅちょう）に筋（すじ）が通（とお）る` (lập luận hợp lý). Toàn ví dụ kinh điển sách Shinkanzen luôn!"),
            (5, "Phân biệt 払う & 引く ✨", "`払（はら）う` vừa là trả tiền (`代金を払う`), vừa là dành sự chú ý (`注意を払う`). Còn `引（ひ）く` vừa là bị cảm (`風邪を引く`), tra từ điển (`辞書を引く`), vừa là rút lui không làm nữa (`手を引く`)!"),
        ],
        "paragraphs": [
            (
                "部屋（へや）の壁（かべ）にかかった時計（とけい）が実際（じっさい）より五分（ごふん）[[進（すす）んで|5]]いることに気づ（きづ）いたとき、海斗（かいと）は外（そと）の[[道（みち）へ続（つづ）く|6]]廊下（ろうか）を見（み）つめて考えた。「締（し）め切（き）りが[[過（す）ぎる|4]]ほどここで長居（ながい）したら、仕事（しごと）の評価（ひょうか）も[[落（お）ちて|1]]しまう。それに昨日（きのう）の紅茶（こうちゃ）を飲（の）んでから、どうにも体力（たいりょく）のスピードが[[落（お）ちた|2]]気がするんだ」",
                "Khi nhận ra chiếc đồng hồ treo tường chạy nhanh hơn giờ thực 5 phút, Kaito nhìn chằm chằm hành lang dẫn ra con đường bên ngoài mà suy nghĩ: 'Nếu ở lại đây quá hạn chót thì đánh giá công việc cũng rớt mất. Với lại từ hôm qua uống tách trà xong, cứ thấy tốc độ hồi phục thể lực suy giảm hẳn đi'."
            ),
            (
                "「でも……」。海斗（かいと）が机（つくえ）の端（はし）に[[残（のこ）った|10]]小さなメモを見（み）つけた瞬間（しゅんかん）、胸（むね）がざわついた。そこには海斗（かいと）が過去に[[落（お）ちた|1]]試験（しけん）のことや、[[風邪（かぜ）を治（なお）す|9]]ために通（かよ）った病院（びょういん）、[[外貨（がいか）を円（えん）に換（か）えた|3]]日付（ひづけ）まで、自分の日記（にっき）を丸ごと[[直（なお）し|9]]たかのように細（こま）かく記録（きろく）されていたのだ。",
                "'Nhưng mà...' — Khoảnh khắc Kaito nhìn thấy tờ ghi chú nhỏ còn sót lại ở mép bàn, ngực cậu bỗng thắt lại. Trên đó ghi chép tỉ mỉ như thể chép lại nguyên cuốn nhật ký của cậu: từ chuyện ngày xưa cậu từng trượt kỳ thi nào, phòng khám cậu tới để chữa cảm, cho tới cả ngày tháng cậu đi đổi ngoại tệ sang Yên."
            ),
            (
                "「いつからこんな調査（ちょうさ）に[[手（て）を出し|15]]たんだ……まさか、わざと[[手（て）を抜（ぬ）か|15]]ずにずっと僕（ぼく）の後（あと）をつけていたのか？」と海斗（かいと）が叫（さけ）ぶと、キッチンから戻（もど）ってきた小百合（さゆり）は静（しず）かにうなずいた。",
                "'Em nhúng tay vào điều tra anh từ bao giờ vậy... chẳng lẽ suốt thời gian qua em không bỏ qua một chi tiết nào mà bám theo anh mãi sao?!' — Kaito thốt lên. Sayuri từ bếp bước ra chỉ lặng lẽ gật đầu."
            ),
            (
                "「ええ。先輩（せんぱい）の安全（あんぜん）には細心（さいしん）の[[注意（ちゅうい）を払（はら）って|12]]きましたから。カフェで[[代金（だいきん）を払（はら）う|11]]姿（すがた）も、本屋（ほんや）で[[辞書（じしょ）を引（ひ）く|13]]横顔（よこがお）も、全部（ぜんぶ）見守（みまも）っていたんです。私（わたし）の愛（あい）にはちゃんと[[筋（すじ）が通（とお）って|8]]いるでしょう？」",
                "'Vâng. Em luôn dành sự chú ý hết sức cẩn trọng cho sự an toàn của anh mà. Dáng vẻ anh thanh toán tiền ở quán cà phê, hay góc nghiêng lúc anh tra từ điển trong hiệu sách, em đều dõi theo hết cả đấy. Tình yêu của em rõ ràng rất có lý mạch lạc đúng không ạ?'"
            ),
            (
                "海斗（かいと）は[[企画（きかく）が会議（かいぎ）を通（とお）る|7]]とかいう日常（にちじょう）が遠く（とおく）霞（かす）むのを感じ（かんじ）た。「そんなの愛（あい）じゃない！　今すぐこんな監視（かんし）から[[手（て）を引（ひ）く|14]]んだ！」",
                "Kaito cảm thấy cuộc sống thường ngày như chuyện dự án được thông qua ở cuộc họp bỗng trôi xa mờ mịt. 'Đó không phải tình yêu! Em rút tay khỏi trò giám sát này ngay lập tức cho anh!'"
            ),
            (
                "「無理（むり）ですよ」と小百合（さゆり）は微笑（ほほえ）んで、海斗（かいと）のスマホを[[変（か）え|3]]たばかりのロック画面（がめん）に向（む）けてかざした。「だって昨日（きのう）の夜（よる）、先輩（せんぱい）は寝言（ねごと）で『小百合（さゆり）……どこにも行（い）くな』って言（い）ったんですよ？　その[[心（こころ）に残（のこ）る|10]]言葉（ことば）を忘（わす）れることなんて、もう二度（にど）とできません」",
                "'Không thể đâu anh à' — Sayuri mỉm cười, giơ chiếc điện thoại Kaito vừa đổi màn hình khóa lên trước mặt cậu: 'Bởi vì đêm qua khi ngủ, anh đã nói mớ rằng: Sayuri... đừng đi đâu hết nhé? Những lời đọng sâu trong tim ấy, em không thể nào quên được nữa đâu'."
            ),
        ],
        "quiz": [
            {
                "prompt": "事故（じこ）が起（お）きないように、細心（さいしん）の注意（ちゅうい）を（　　）作業（さぎょう）しよう。",
                "options": ["払（はら）って", "引（ひ）いて", "抜（ぬ）いて", "過（す）ぎて"],
                "ans": 1,
                "right_exp": "💖 Chính xác! Thành ngữ công việc rất hay ra thi JLPT: `細心の注意を払う` = hết sức chú ý cẩn thận.",
                "wrong_exps": [
                    "Chính xác: `注意を払う` = dành sự chú ý cẩn trọng.",
                    "`引く` không đi với `注意を〜` (mà đi với `注意を引く` = thu hút sự chú ý của người khác).",
                    "`抜く` là nhổ ra hoặc bỏ qua công đoạn (`手を抜く`).",
                    "`過ぎる` là trôi qua hoặc quá trớn."
                ]
            },
            {
                "prompt": "彼（かれ）の意見（いけん）にはしっかり（　　）が通（とお）っているので、みんなが納得（なっとく）した。",
                "options": ["筋（すじ）", "手（て）", "色（いろ）", "辞書（じしょ）"],
                "ans": 1,
                "right_exp": "💖 Quá giỏi! `筋（すじ）が通（とお）っている` = lập luận hợp lý, có trước có sau mạch lạc.",
                "wrong_exps": [
                    "Chính xác: `筋が通る` = có lý, hợp logic.",
                    "`手` đi với `手を引く` / `手を抜く`, không dùng `手が通る`.",
                    "`色` đi với `色が落ちる` (phai màu).",
                    "`辞書` đi với `辞書を引く` (tra từ điển)."
                ]
            },
            {
                "prompt": "この時計（とけい）は実際（じっさい）の時間（じかん）より5分（ごふん）（　　）いる。",
                "options": ["進（すす）んで", "残（のこ）って", "治（なお）って", "続（つづ）いて"],
                "ans": 1,
                "right_exp": "💖 Chuẩn xác! Đồng hồ chạy nhanh hơn giờ thật là `時計が進んでいる` (còn chạy chậm là `遅れている`).",
                "wrong_exps": [
                    "Chính xác: `進む` = đồng hồ chạy nhanh hơn giờ chuẩn.",
                    "`残る` là còn sót lại.",
                    "`治る` là khỏi bệnh.",
                    "`続く` là kéo dài hoặc dẫn tới nơi nào."
                ]
            },
            {
                "prompt": "違法（いほう）な仕事（しごと）だと気づ（きづ）いたので、すぐその会社（かいしゃ）から（　　）ことにした。",
                "options": ["手（て）を引（ひ）く", "手（て）を抜（ぬ）く", "代金（だいきん）を払（はら）う", "風邪（かぜ）を引（ひ）く"],
                "ans": 1,
                "right_exp": "💖 Đúng rồi em! Rút lui, chấm dứt không dính dáng tới việc gì nữa là `手を引く` (`引（ひ）く` nghĩa 2).",
                "wrong_exps": [
                    "Chính xác: `手を引く` = rút tay khỏi việc gì đó, chấm dứt tham gia.",
                    "`手を抜く` là làm ẩu, ăn bớt công đoạn.",
                    "`代金を払う` là trả tiền hàng.",
                    "`風邪を引く` là bị cảm lạnh."
                ]
            },
            {
                "prompt": "海斗（かいと）は机（つくえ）のメモを見（み）て、なぜ激（はげ）しく驚（おどろ）いたのか。",
                "options": [
                    "海斗（かいと）の過去の試験（しけん）や病院（びょういん）、銀行（ぎんこう）の両替（りょうがえ）まで小百合（さゆり）がすべて記録（きろく）していたから",
                    "会社（かいしゃ）の企画（きかく）が会議（かいぎ）を通（とお）らなかったから",
                    "時計（とけい）が五分（ごふん）遅（おく）れて壊（こわ）れていたから",
                    "小百合（さゆり）が明日（あした）外国（がいこく）へ帰（かえ）ると書（か）いてあったから"
                ],
                "ans": 1,
                "right_exp": "💖 Chuẩn không khí trinh thám tình cảm luôn! Sayuri theo dõi và ghi chép từng dấu chân nhỏ nhất trong đời Kaito từ quá khứ tới hiện tại mà không hề chừa chi tiết nào!",
                "wrong_exps": [
                    "Chính xác: Toàn bộ lịch sử cá nhân của Kaito bị Sayuri ghi chép chi tiết.",
                    "Không có kết quả họp công ty nào được báo trong chương này.",
                    "Đồng hồ chạy nhanh 5 phút (`進んでいる`) chứ không phải bị chậm hỏng.",
                    "Sayuri tuyệt đối không đi đâu hết, cô ấy còn muốn giữ Kaito lại mãi cơ!"
                ]
            },
        ]
    },
]
