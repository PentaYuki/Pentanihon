# -*- coding: utf-8 -*-
"""
Tiểu thuyết 3 — ISEKAI FANTASY (Chuyển Sinh Kiến Quốc & Phép Thuật): Phần A (Chương 01 - 06)
『異世界の落ちこぼれ領主、現代知識で最強王国を創る！』— Lãnh Chúa Phế Vật Ở Dị Giới Dùng Kiến Thức Hiện Đại Kiến Tạo Vương Quốc Mạnh Nhất!
"""

ISEKAI_META = {
    "id": "isekai",
    "slug": "isekai",
    "genre_badge": "⚔️✨ ISEKAI FANTASY • CHUYỂN SINH KIẾN QUỐC",
    "theme_color": "#4338ca",
    "theme_soft": "#eef2ff",
    "title_jp": "異世界（いせかい）の落ちこぼれ領主（りょうしゅ）、現代（げんだい）知識（ちしき）で最強（さいきょう）王国（おうこく）を創（つく）る！",
    "title_vi": "Lãnh Chúa Phế Vật Ở Dị Giới Dùng Kiến Thức Hiện Đại Kiến Tạo Vương Quốc Mạnh Nhất!",
    "tagline": "Đánh thức phép thuật tri thức, cải cách kinh tế, bảo vệ sinh thái, chế tạo ma cụ và dẫn dắt quân đoàn vượt ải ma vương — trọn vẹn 12 bài Shinkanzen còn lại (233 từ)!",
    "yuki_intro": "Chào mừng em bước qua cánh cổng dịch chuyển tới bộ tiểu thuyết thứ ba: **Isekai Chuyển Sinh Kiến Quốc**!! ⚔️✨ Ở thế giới phép thuật rực rỡ này, chúng mình sẽ cùng lãnh chúa trẻ Yūma chinh phục 12 bài cuối cùng của Shinkanzen N2: từ thiên nhiên du lịch, kinh tế vĩ mô, chính trị luật pháp, khoa học sinh thái, số lượng không gian, cho tới toàn bộ **Từ tượng thanh/tượng hình (オノマトペ)** và **Quy tắc cấu tạo từ (語形成)** cực kỳ hay thi N2 nha~ Lên đường thám hiểm cùng chị nào! 🌸",
    "characters": [
        {"name": "悠真（ゆうま / Yūma）", "role": "Nam chính (25 tuổi)", "desc": "Kỹ sư quy hoạch & chuyên gia kinh tế hiện đại bất ngờ chuyển sinh vào thân xác vị nam tước trẻ cai quản vùng biên ải nghèo nàn Eldia."},
        {"name": "セレス（Celes）", "role": "Nữ kỵ sĩ pháp sư (20 tuổi)", "desc": "Phó quan nghiêm khắc nhưng tận tâm của gia tộc Eldia, ban đầu hoài nghi Yūma nhưng dần bị chinh phục bởi tầm nhìn và sự ấm áp của cậu."},
        {"name": "ルナ（Luna）", "role": "Thiên tài giả kim (17 tuổi)", "desc": "Cô gái phụ trách phòng nghiên cứu ma thạch và thảo dược, luôn say mê những công thức khoa học kỳ diệu từ thế giới của Yūma."},
    ],
}

ISEKAI_CHAPTERS_A = [
    {
        "num": 1,
        "slug": "chuong-01",
        "lesson_id": "p1_c04_b02",
        "title_jp": "第1章：[[恵（めぐ）まれ|1]]た大地（だいち）と[[山頂（さんちょう）|5]]からの[[眺（なが）め|2]]",
        "title_vi": "Chương 01: Vùng Đất Được Ban Tặng & Tầm Nhìn Từ Đỉnh Núi Biên Ải",
        "yuki_reminder_top": "Chương mở màn thế giới Isekai gói gọn 22 từ **Bài 9 — Phần 1 Chương 4 Bài 2 (Thiên nhiên & Cảnh quan khi du lịch)**! Từ `恵まれる` (được thiên nhiên ưu đãi), `標高・山頂・ふもと` (độ cao, đỉnh núi, chân núi), `川上・川下` (thượng nguồn/hạ lưu), `日当たり・日陰` (chỗ nắng/bóng râm), cho đến `梅雨・紅葉・枯れる・茂る・火山` đều nằm gọn trong chuyến khảo sát biên ải đầu tiên của Yūma đó nha! 🏔️✨",
        "yuki_reminder_bottom": "Vừa nhâm nhi phong cảnh dị giới vừa nhớ cặp đối nghĩa `川上・川下`, `日当たり・日陰`, `上る・沈む` và `枯れる・茂る` trong bài này em nhé! Chị đợi em qua 5 câu trắc nghiệm phía dưới đó~ 🌸",
        "soft_notes": [
            (2, "Cảnh báo phân biệt âm đọc cùng Kanji ✨", "Trong bài có `[[上（のぼ）る|16]]` khi nói mặt trời mọc (`朝日（あさひ）が上（のぼ）る`) hoặc leo dốc, đọc là `のぼる` (KHÔNG phải `あがる` trong trường hợp này nhé!). Ngược lại lặn xuống chân trời/chìm xuống nước là `[[沈（しず）む|15]]`!"),
            (5, "Mẹo nhớ từ ghép cặp đôi dễ thương 🌿", "Chị Yuki gợi ý học theo cặp: `日当（ひあ）たり` (nơi nắng rọi ấm áp) ↔ `日陰（ひかげ）` (bóng râm mát); `川上（かわかみ）` (thượng nguồn) ↔ `川下（かわしも）` (hạ lưu); `山頂（さんちょう）` (đỉnh núi) ↔ `ふもと` (chân núi). Học có đôi có cặp vừa nhanh vừa khó quên lắm luôn!"),
        ],
        "paragraphs": [
            (
                "目（め）を覚（さ）ますと、悠真（ゆうま）は見知（みし）らぬ異世界（いせかい）の辺境（へんきょう）エルディア領（りょう）にいた。案内役（あんないやく）の女（おんな）騎士（きし）セレスは馬（うま）を止（と）め、「ここがあなた様（さま）の領地（りょうち）です。手付（てつ）かずの自然（しぜん）に[[恵（めぐ）まれ|1]]ていますが、財政（ざいせい）は火（ひ）の車（くるま）です」と厳（きび）しく告（つ）げた。",
                "Khi mở mắt tỉnh dậy, Yūma phát hiện mình đang đứng giữa lãnh địa biên ải Eldia ở một thế giới khác. Nữ kỵ sĩ dẫn đường Celes ghìm dây cương ngựa lại và báo cáo nghiêm nghị: 'Đây chính là lãnh địa của ngài. Nơi này được thiên nhiên nguyên sơ ưu đãi, nhưng ngân khố thì đang cháy túi kiệt quệ rồi ạ'."
            ),
            (
                "現状（げんじょう）を確か（たしか）めるため、二人（ふたり）は[[標高（ひょうこう）|4]]三千（さんぜん）メートル級（きゅう）の岩山（いわやま）を登（のぼ）り、風（かぜ）の強（つよ）い[[山頂（さんちょう）|5]]に立（た）った。そこからの[[眺（なが）め|2]]は息（いき）を呑（の）むほど壮大（そうだい）で、見渡（みわた）す限（かぎ）り青い空（そら）と緑（みどり）の大地（だいち）が果（は）てしなく[[広（ひろ）がっ|3]]ていた。",
                "Để kiểm chứng hiện trạng lãnh địa, cả hai leo lên ngọn núi đá cao tầm 3.000 mét và đứng trên đỉnh núi lộng gió. Tầm nhìn từ trên đỉnh hùng vĩ đến nghẹt thở: bầu trời xanh thẳm và mảnh đất xanh mướt trải rộng bát ngát đến tận chân trời."
            ),
            (
                "山（やま）の[[ふもと|6]]には霧（きり）のかかる深（ふか）い[[谷（たに）|9]]が走（はし）り、切り立った崖（がけ）から壮観（そうかん）な[[滝（たき）|10]]が轟音（ごうおん）を立（た）てて落（お）ちていた。「[[川上（かわかみ）|11]]には魔力（まりょく）を含（ふく）む泉（いずみ）があり、その水（みず）が[[川下（かわしも）|12]]の村（むら）の畑（はたけ）を潤（うるお）しています」とセレスが指（ゆび）をさす。",
                "Dưới chân núi là một thung lũng sâu phủ sương mù, và từ vách đá dựng đứng đổ xuống một thác nước hùng vĩ ầm ầm vang dội. 'Ở thượng nguồn có con suối chứa ma lực, dòng nước ấy chảy về tưới tiêu cho ruộng đồng các ngôi làng ở hạ lưu đấy ạ' — Celes chỉ tay giải thích."
            ),
            (
                "遠（とお）くの西（にし）の果（は）てには美（うつく）しい[[海岸（かいがん）|7]]線（せん）が延（の）び、太陽（たいよう）に煌（きら）めく白い[[砂浜（すなはま）|8]]が見（み）えた。さらに北（きた）には煙（けむり）をわずかに上（あ）げる活（かつ）[[火山（かざん）|22]]までそびえ立（た）ち、周辺（しゅうへん）には天然（てんねん）温泉（おんせん）が湧（わ）き出（で）ているという。",
                "Xa xa tận phía tây là đường bờ biển tuyệt đẹp cùng bãi cát trắng lấp lánh dưới ánh mặt trời. Không chỉ vậy, ở phía bắc còn sừng sững một ngọn núi lửa đang còn hoạt động phả làn khói mỏng, nghe nói xung quanh đó còn tuôn trào suối nước nóng tự nhiên nữa."
            ),
            (
                "「冬（ふゆ）には草木（くさき）が[[枯（か）れ|20]]て厳（きび）しいですが、秋（あき）の[[紅葉（こうよう）|19]]は王都（おうと）でも有名（ゆうめい）です。ただ、[[梅雨（つゆ）|18]]のように長雨（ながあめ）が続（つづ）く季節（きせつ）は道（みち）がぬかるみますね」とセレスは言（い）った。けれど春（はる）から夏（なつ）にかけては木々（きぎ）が青々（あおあお）と[[茂（しげ）り|21]]、観光（かんこう）資源（しげん）の宝庫（ほうこ）ではないか！",
                "'Vào mùa đông cây cỏ héo úa thì hơi khắc nghiệt, nhưng mùa thu lá đỏ ở đây nổi tiếng khắp cả kinh đô đấy ạ. Chỉ có điều vào mùa mưa dầm kéo dài giống tháng sáu thì đường sá hay lầy lội lắm.' — Celes nói. Thế nhưng từ xuân sang hè cây cối mọc sum suê xanh rì thế này, chẳng phải đây chính là kho báu tài nguyên du lịch sao!"
            ),
            (
                "悠真（ゆうま）は[[日当（ひあ）たり|13]]の良（よ）い南（みなみ）斜面（しゃめん）にリゾート宿（やど）を建（た）て、夏（なつ）の涼（すず）しい木（き）の[[日陰（ひかげ）|14]]を休憩（きゅうけい）所（じょ）にする構想（こうそう）を描（えが）いた。やがて水平線（すいへいせん）に夕日（ゆうひ）が[[沈（しず）み|15]]、翌朝（よくあさ）また東（ひがし）から朝日（あさひ）が[[上（のぼ）っ|16]]て黄金色（こがねいろ）の光（ひかり）が領地（りょうち）を[[照（て）らし|17]]た時（とき）、新（あたら）しい国（くに）づくりの一歩（いっぽ）が始（はじ）まった。",
                "Yūma phác thảo ý tưởng xây dựng khu nghỉ dưỡng ở sườn núi hướng nam đầy ánh nắng chan hòa, còn bóng râm mát rượi dưới tán cây mùa hè sẽ làm trạm dừng chân. Chẳng bao lâu sau khi mặt trời lặn xuống đường chân trời và rạng sáng hôm sau bình minh lại mọc ở phía đông chiếu sáng rực rỡ lên khắp lãnh địa bằng thứ ánh sáng vàng óng, bước đi đầu tiên kiến tạo vương quốc mới đã chính thức bắt đầu."
            ),
        ],
        "quiz": [
            {
                "prompt": "富士山の（　　）に広がる湖（みずうみ）のまわりで、みんなとキャンプをした。",
                "options": ["ふもと", "山頂", "川上", "砂浜"],
                "ans": 1,
                "right_exp": "Chính xác! `ふもと` (chân núi) kết hợp tự nhiên với `富士山のふもと` (dưới chân núi Phú Sĩ) nơi có hồ nước và khu cắm trại.",
                "wrong_exps": [
                    "Đáp án đúng là `ふもと` (vùng chân núi) nha em.",
                    "`山頂（さんちょう）` là đỉnh núi chót vót trên cao, không hợp với 'hồ trải rộng ở dưới'.",
                    "`川上（かわかみ）` là thượng nguồn dòng sông, không dùng cho chân núi.",
                    "`砂浜（すなはま）` là bãi cát ven biển, không gắn với núi Phú Sĩ."
                ]
            },
            {
                "prompt": "南向きで（　　）が良い部屋（へや）なので、冬でもぽかぽかと暖かい。",
                "options": ["日陰（ひかげ）", "日当（ひあ）たり", "眺め（ながめ）", "標高（ひょうこう）"],
                "ans": 2,
                "right_exp": "Quá chuẩn luôn! `日当たりが良い` nghĩa là đón nắng tốt / nhiều ánh nắng chiếu vào, cực hợp với phòng hướng nam ấm áp vào mùa đông.",
                "wrong_exps": [
                    "`日陰（ひかげ）` là bóng râm, trái nghĩa hoàn toàn với ấm áp nhờ nắng.",
                    "Chính xác! `日当たり（ひあたり）` là độ chiếu nắng.",
                    "`眺め（ながめ）` là tầm nhìn phong cảnh, không trực tiếp khiến phòng ấm lên vào mùa đông như ánh nắng.",
                    "`標高（ひょうこう）` là độ cao so với mực nước biển."
                ]
            },
            {
                "prompt": "秋（あき）になると山全体（やまぜんたい）が赤や黄色に染（そ）まり、（　　）がとても美しい。",
                "options": ["梅雨（つゆ）", "火山（かざん）", "紅葉（こうよう）", "滝（たき）"],
                "ans": 3,
                "right_exp": "Chuẩn không cần chỉnh! `紅葉（こうよう）` là lá đỏ mùa thu (cụ thể là cảnh sắc lá đổi sang đỏ vàng vào thu).",
                "wrong_exps": [
                    "`梅雨（つゆ）` là mùa mưa dầm tháng 6.",
                    "`火山（かざん）` là núi lửa.",
                    "Tuyệt vời! `紅葉（こうよう）` là cảnh lá phong đỏ vàng mùa thu.",
                    "`滝（たき）` là thác nước."
                ]
            },
            {
                "prompt": "森（もり）の奥（おく）では、夏（なつ）の日光（にっこう）を浴（あ）びて木々（きぎ）が青々（あおあお）と（　　）いる。",
                "options": ["枯（か）れて", "茂（しげ）って", "沈（しず）んで", "恵（めぐ）まれて"],
                "ans": 2,
                "right_exp": "Xuất sắc! `茂（しげ）る` là mọc sum suê rậm rạp (`青々と茂っている` = xanh tốt um tùm).",
                "wrong_exps": [
                    "`枯（か）れる` là héo úa khô cạn, ngược với `青々と` (xanh mướt).",
                    "Đúng rồi! `茂（しげ）る` diễn tả cây cối mọc rậm rạp sum suê.",
                    "`沈（しず）む` là chìm xuống hoặc mặt trời lặn.",
                    "`恵（めぐ）まれる` thường đi với danh từ + に (`自然に恵まれる`: được ưu đãi bởi thiên nhiên)."
                ]
            },
            {
                "prompt": "ここは海（うみ）にも山（やま）にも近く、豊（ゆた）かな自然（しぜん）に（　　）土地（とち）だ。",
                "options": ["照（て）らされた", "広がった", "上（のぼ）った", "恵（めぐ）まれた"],
                "ans": 4,
                "right_exp": "Chính xác tuyệt đối! Mẫu cố định `自然に恵まれる` nghĩa là được thiên nhiên ưu đãi ban tặng dồi dào.",
                "wrong_exps": [
                    "`照らす` là chiếu sáng lên bề mặt vật gì.",
                    "`広がる` là trải rộng ra trước mắt (`海が広がる`), không đi với trợ từ に kiểu bị động hưởng lợi.",
                    "`上る` là leo lên / mặt trời mọc.",
                    "Chuẩn rồi! `〜に恵まれる` là cụm kinh điển của N2."
                ]
            },
        ],
    },
    {
        "num": 2,
        "slug": "chuong-02",
        "lesson_id": "p1_c07_b03",
        "title_jp": "第2章：[[赤字（あかじ）|14]]脱出（だっしゅつ）！[[経済（けいき）|1]]と[[貿易（ぼうえき）|7]]の大改革（だいかいかく）",
        "title_vi": "Chương 02: Thoát Khỏi Thâm Hụt! Đại Cải Cách Kinh Tế & Thương Mại",
        "yuki_reminder_top": "Sang Chương 02 là trọn vẹn **25 từ Bài 16 — Phần 1 Chương 7 Bài 3 (Kinh tế, Kinh doanh & Công nghiệp)** siêu hay gặp trong JLPT N2 luôn đó em! Nào là `景気・不況・物価・消費税`, `需要・供給`, `貿易・輸出・輸入・円高・円安`, `株・投資・利益・赤字・黒字・負債`, rồi tới `経費・採算・企業・経営・提携・買収・合併・倒産・在庫`! Cùng Yūma vực dậy kinh tế lãnh địa nhé 💼🪙",
        "yuki_reminder_bottom": "Ôi chao màn giải cứu tài chính của Yūma ngoạn mục quá phải không em? Nhớ phân biệt kỹ `赤字` (thua lỗ/âm) với `黒字` (có lãi/dương), `買収` (mua lại thâu tóm) với `合併` (hai bên sáp nhập ngang hàng) nhé! Làm 5 câu trắc nghiệm củng cố liền tay nào ✨",
        "soft_notes": [
            (2, "Phân biệt `買収` vs `合併` & `赤字` vs `黒字` 🪙", "Ở Nhật sổ sách ngày xưa ghi số lời bằng mực đen `黒字（くろじ）` còn số lỗ bằng mực đỏ `赤字（あかじ）` nên thành từ vựng kinh tế siêu dễ nhớ luôn! Còn trong M&A: `買収（ばいしゅう）` là công ty lớn mua đứt công ty khác, còn `合併（がっぺい）` là sáp nhập 2 công ty thành 1 công ty mới!"),
            (5, "Cặp từ đối lập bắt buộc phải nằm lòng 📊", "1) `需要（じゅよう）` (cầu) ↔ `供給（きょうきゅう）` (cung)\n2) `輸出（ゆしゅつ）` (xuất khẩu - gửi *ra*) ↔ `輸入（ゆにゅう）` (nhập khẩu - đưa *vào*)\n3) `円高（えんだか）` (Yên lên giá - nhập khẩu sướng, du lịch rẻ) ↔ `円安（えんやす）` (Yên mất giá - xuất khẩu thu lợi khi quy đổi). Nắm chắc logic này thì vào đề đọc hiểu kinh tế không sợ câu nào!"),
        ],
        "paragraphs": [
            (
                "領主館（りょうしゅかん）の書庫（しょこ）で帳簿（ちょうぼ）を開（ひら）いた悠真（ゆうま）は、思（おも）わず頭（あたま）を抱（かか）えた。エルディア領（りょう）は長引（ながび）く深刻（しんこく）な[[不況（ふきょう）|2]]に陥（おちい）り、パンの[[物価（ぶっか）|3]]が急上昇（きゅうじょうしょう）する一方（いっぽう）、領民（りょうみん）の暮（く）らしを圧迫（あっぱく）する高（たか）い[[消費税（しょうひぜい）|4]]のせいで市場（しじょう）の[[景気（けいき）|1]]は冷（ひ）え切（き）っていた。",
                "Mở sổ sách trong thư khố dinh thự lãnh chúa ra xem, Yūma bất giác ôm đầu. Lãnh địa Eldia đang rơi vào tình trạng suy thoái nghiêm trọng kéo dài: vật giá bánh mì tăng vọt trong khi thuế tiêu dùng quá cao đè nặng lên đời sống dân chúng khiến tình hình kinh tế ngoài chợ đóng băng lạnh lẽo."
            ),
            (
                "「前年（ぜんねん）の収支（しゅうし）は大幅（おおはば）な[[赤字（あかじ）|14]]で、王立（おうりつ）銀行（ぎんこう）への[[負債（ふさい）|16]]も山積（さんづ）みです。しかも倉庫（そうこ）には売（う）れない鉱石（こうせき）の[[在庫（ざいこ）|25]]が大量（たいりょう）に眠（ねむ）っています」とセレスが肩（かた）を落（お）とす。",
                "'Thu chi năm ngoái thâm hụt thua lỗ nặng nề, khoản nợ đối với Ngân hàng Hoàng gia cũng chất thành núi. Hơn nữa trong kho còn chất đống hàng tồn kho là quặng ma thạch chẳng bán nổi' — Celes rũ vai thở dài."
            ),
            (
                "悠真（ゆうま）は即座（そくざ）に電卓（でんたく）を叩（たた）き始（はじ）めた。「大丈夫（だいじょうぶ）、原因（げんいん）は[[需要（じゅよう）|5]]と[[供給（きょうきゅう）|6]]のバランスが崩（くず）れているだけだ！　まず無駄（むだ）な宮廷（きゅうてい）の[[経費（けいひ）|17]]を削減（さくげん）し、[[採算（さいさん）|18]]の合（あ）わない古い炭鉱（たんこう）事業（じぎょう）から撤退（てったい）しよう。」",
                "Yūma lập tức bấm bảng tính suy luận ngay. 'Không sao cả, nguyên nhân chỉ là do cán cân cung và cầu bị mất cân bằng mà thôi! Trước hết chúng ta cắt giảm mọi chi phí rườm rà trong phủ, rồi rút lui khỏi những mỏ than cũ kỹ không có hiệu quả lời lỗ.'"
            ),
            (
                "次（つぎ）に悠真（ゆうま）が目（め）をつけたのは隣国（りんごく）との[[貿易（ぼうえき）|7]]だった。温泉（おんせん）から採（と）れる希少（きしょう）な硫黄（いおう）や魔法（まほう）薬草（やくそう）を外国（がいこく）へ[[輸出（ゆしゅつ）|8]]し、不足（ふそく）している鉄鉱石（てっこうせき）を安（やす）く[[輸入（ゆにゅう）|9]]するルートを開拓（かいたく）したのだ。前世（ぜんせ）の日本（にほん）で学（まな）んだ[[円高（えんだか）|10]]や[[円安（えんやす）|10]]の為替（かわせ）変動（へんどう）の知識（ちしき）を応用（おうよう）し、自領（じりょう）通貨（つうか）と隣国（りんごく）金貨（きんか）の交換（こうかん）レートを巧（たく）みに管理（かんり）した。",
                "Tiếp đó, thứ Yūma nhắm tới là thương mại giao thương với lân bang. Cậu khai thông tuyến xuất khẩu lưu huỳnh hiếm từ suối nước nóng và thảo dược ma pháp sang nước ngoài, đồng thời nhập khẩu quặng sắt đang thiếu với giá rẻ. Vận dụng kiến thức biến động tỷ giá như đồng Yên tăng giá hay mất giá mà mình học ở kiếp trước tại Nhật, cậu khéo léo điều tiết tỷ giá quy đổi giữa tiền tệ lãnh địa và tiền vàng nước bạn."
            ),
            (
                "さらに町（まち）の商業（しょうぎょう）ギルド改革（かいかく）に挑（いど）んだ。[[経営（けいえい）|20]]悪化（あっか）で[[倒産（とうさん）|24]]しかけていた小規模（しょうきぼ）な工房（こうぼう）を救（すく）うため、大手（おおて）の[[企業（きぎょう）|19]]にあたる王都（おうと）の巨大（きょだい）商会（しょうかい）と業務（ぎょうむ）[[提携（ていけい）|21]]を結（むす）んだ。対立（たいりつ）していた二つの鍛冶（かじ）組合（くみあい）を一つに[[合併（がっぺい）|23]]させ、悪徳（あくとく）商人が進（すす）めていた工房（こうぼう）の無理（むり）な[[買収（ばいしゅう）|22]]計画（けいかく）も見事（みごと）に阻止（そし）した。",
                "Chưa dừng lại, cậu còn dấn thân cải cách Hiệp hội Thương nhân trong thị trấn. Để cứu các xưởng thủ công nhỏ đang đứng bên bờ vực phá sản vì điều hành sa sút, cậu ký kết hợp tác liên minh nghiệp vụ với đại thương đoàn ở kinh đô — tương đương các doanh nghiệp lớn. Cậu cho sáp nhập hai công đoàn thợ rèn từng đối đầu thành một khối thống nhất, và chặn đứng ngoạn mục âm mưu thâu tóm mua lại cưỡng ép của đám gian thương."
            ),
            (
                "最後（さいご）に悠真（ゆうま）は領内（りょうない）初（はつ）となる商会（しょうかい）の出資（しゅっし）証書（しょうしょ）――現代（げんだい）でいう[[株（かぶ）|11]]のような仕組み（しくみ）を発行（はっこう）し、貴族（きぞく）や富豪（ふごう）に「エルディアの観光（かんこう）と薬草（やくそう）産業（さんぎょう）に[[投資（とうし）|12]]しませんか」と呼（よ）びかけた。半年（はんとし）後（ご）、領地（りょうち）の帳簿（ちょうぼ）は巨額（きょがく）の[[利益（りえき）|13]]を生（う）み出（だ）して見事（みごと）な[[黒字（くろじ）|15]]へと転換（てんかん）し、セレスは「信じ（しんじ）られません……まるで経済（けいざい）の魔法（まほう）ですね！」と目（め）を輝（かがや）かせた。",
                "Cuối cùng, Yūma phát hành chứng thư góp vốn thương hội đầu tiên trong lãnh địa — mô hình hệt như cổ phiếu thời hiện đại — kêu gọi giới quý tộc và phú hào hãy đầu tư vào ngành du lịch và dược liệu của Eldia. Nửa năm sau, sổ sách lãnh địa tạo ra lợi nhuận khổng lồ và chuyển mình ngoạn mục sang có lãi thặng dư, khiến Celes sáng rực ánh mắt thốt lên: 'Thần không thể tin nổi… đúng là phép màu của kinh tế học ạ!'."
            ),
        ],
        "quiz": [
            {
                "prompt": "人件費（じんけんひ）などの（　　）を見直（みなお）して削減（さくげん）し、ようやく赤字から抜け出した。",
                "options": ["負債（ふさい）", "在庫（ざいこ）", "経費（けいひ）", "物価（ぶっか）"],
                "ans": 3,
                "right_exp": "Chính xác! `経費（けいひ）` là chi phí vận hành/hoạt động (bao gồm tiền nhân công, vật tư...), thường đi với `削減する` (cắt giảm).",
                "wrong_exps": [
                    "`負債（ふさい）` là khoản nợ nần tồn đọng (đi với `抱える・返済する`).",
                    "`在庫（ざいこ）` là hàng tồn kho trong kho.",
                    "Quá chuẩn! `経費を見直す・削減する` là cụm chuyên dụng N2.",
                    "`物価（ぶっか）` là giá cả thị trường chung."
                ]
            },
            {
                "prompt": "（　　）が合（あ）わない赤字（あかじ）の店舗（てんぽ）は、来月（らいげつ）で閉（し）めることになった。",
                "options": ["採算（さいさん）", "提携（ていけい）", "貿易（ぼうえき）", "需要（じゅよう）"],
                "ans": 1,
                "right_exp": "Tuyệt vời! Quán dụng kinh tế cực hay thi `採算が合う / 合わない` nghĩa là tính toán có lời hay không có lời.",
                "wrong_exps": [
                    "Chuẩn xác! `採算（さいさん）が合わない` = không có lãi / không bù nổi vốn.",
                    "`提携（ていけい）` là sự hợp tác liên minh kinh doanh.",
                    "`貿易（ぼうえき）` là ngoại thương xuất nhập khẩu.",
                    "`需要（じゅよう）` là nhu cầu thị trường."
                ]
            },
            {
                "prompt": "大企業（だいきぎょう）がライバル会社（がいしゃ）を（　　）して、自分のグループに入（い）れた。",
                "options": ["倒産（とうさん）", "買収（ばいしゅう）", "投資（とうし）", "輸入（ゆにゅう）"],
                "ans": 2,
                "right_exp": "Chính xác! `買収（ばいしゅう）` là mua lại, thâu tóm công ty khác đưa về dưới trướng tập đoàn mình.",
                "wrong_exps": [
                    "`倒産（とうさん）` là phá sản vỡ nợ đóng cửa.",
                    "Chuẩn luôn! `買収する` nghĩa là thâu tóm (M&A).",
                    "`投資（とうし）` là đầu tư vốn sinh lời chứ không nhất thiết nuốt trọn cả công ty.",
                    "`輸入（ゆにゅう）` là nhập khẩu hàng hóa."
                ]
            },
            {
                "prompt": "今年度（こんねんど）は新商品（しんしょうひん）が大ヒットし、5年ぶりに（　　）に転換（てんかん）した。",
                "options": ["赤字（あかじ）", "不況（ふきょう）", "黒字（くろじ）", "消費税（しょうひぜい）"],
                "ans": 3,
                "right_exp": "Quá chính xác! Sản phẩm mới hit bùng nổ giúp lần đầu sau 5 năm chuyển từ lỗ sang có lãi: `黒字（くろじ）に転換した`.",
                "wrong_exps": [
                    "`赤字（あかじ）` là thâm hụt thua lỗ, mâu thuẫn với 'sản phẩm bán chạy đại thắng'.",
                    "`不況（ふきょう）` là thời kỳ suy thoái kinh tế chung.",
                    "Đúng rồi! `黒字` = thặng dư, có lãi.",
                    "`消費税（しょうひぜい）` là thuế tiêu dùng."
                ]
            },
            {
                "prompt": "夏（なつ）は気温（きおん）が上（あ）がるため、冷（つめ）たい飲（の）み物（もの）の（　　）が急（きゅう）に高（たか）まる。",
                "options": ["供給（きょうきゅう）", "需要（じゅよう）", "在庫（ざいこ）", "負債（ふさい）"],
                "ans": 2,
                "right_exp": "Chuẩn không cần chỉnh! Mùa hè nóng nên *nhu cầu* (`需要（じゅよう）`) về đồ uống lạnh tăng cao (`需要が高まる`).",
                "wrong_exps": [
                    "`供給（きょうきゅう）` là nguồn cung phía nhà sản xuất đưa ra.",
                    "Tuyệt vời! `需要が高まる` = nhu cầu tăng vọt.",
                    "`在庫（ざいこ）` là lượng hàng còn tồn trong kho.",
                    "`負債（ふさい）` là khoản nợ."
                ]
            },
        ],
    },
    {
        "num": 3,
        "slug": "chuong-03",
        "lesson_id": "p1_c07_b04",
        "title_jp": "第3章：王都（おうと）の[[議会（ぎかい）|4]]と[[条約（じょうやく）|8]]、そして古代（こだい）[[遺跡（いせき）|23]]の秘密（ひみつ）",
        "title_vi": "Chương 03: Nghị Viện Vương Đô, Hiệp Ước Hòa Bình & Bí Mật Di Tích Cổ",
        "yuki_reminder_top": "Chương 03 cực ngầu với **25 từ Bài 17 — Phần 1 Chương 7 Bài 4 (Chính trị, Pháp luật & Lịch sử)**! Từ trường nghị trường (`政治・政策・首相・議会・選挙・投票・外交・条約・懸念`), sang tòa án luật pháp (`法律・制定・改正・施行・遵守・違反・権利・義務・裁判・判決・罰する・証拠`), tới lịch sử hào hùng (`歴史・遺跡・栄える・滅びる`) đều hội tụ trong phiên đối chất của Yūma tại Vương Đô đó em! ⚖️🏛️",
        "yuki_reminder_bottom": "Ôi pha vạch mặt tên công tước tham nhũng giữa công đường đã cái nư ghê em ha~ Nhớ phân biệt cặp `制定する` (ban hành luật hoàn toàn mới), `改正する` (sửa đổi luật cũ), và `施行される` (luật chính thức có hiệu lực thi hành) nhé! Triển liền 5 câu quiz bên dưới nào 🌸",
        "soft_notes": [
            (2, "Nhắc nhẹ phát âm dễ nhầm: `施行（しこう）` vs `判決（はんけつ）` ⚖️", "Từ `[[施行（しこう）される|13]]` đọc là **しこう** (thi hành, có hiệu lực từ ngày...), đừng nhầm với せこう (thi công xây dựng) nhé em! Còn `[[罰（ばっ）する|20]]` đọc âm ngắt `ばっする` (xử phạt) khi gắn thêm `する`!"),
            (5, "Bộ đôi đối nghĩa Lịch Sử: `栄える` ↔ `滅びる` 🏛️", "Nhớ chữ Hán nhé: `栄（さか）える` (VINH — phồn vinh, hưng thịnh, thuộc nhóm 2) và `滅（ほろ）びる` (DIỆT — diệt vong, suy tàn, cũng thuộc nhóm 2, quá khứ là 滅びた)!"),
        ],
        "paragraphs": [
            (
                "エルディアの目覚（めざ）ましい発展（はってん）を妬（ねた）む守旧派（しゅきゅうは）の貴族（きぞく）が王都（おうと）の[[議会（ぎかい）|4]]で妨害（ぼうがい）工作（こうさく）を始（はじ）めた。これまで[[政治（せいじ）|1]]に興味（きょうみ）のなかった領主（りょうしゅ）と侮（あなど）っていた相手（あいて）に対（たい）し、悠真（ゆうま）は堂々（どうどう）と[[首相（しゅしょう）|3]]の前（まえ）へ進（すす）み出（で）た。",
                "Phe quý tộc bảo thủ ghen tức trước sự phát triển vượt bậc của Eldia liền bày trò cản phá trong Nghị viện Vương đô. Đáp trả lại thái độ khinh thường của những kẻ vốn tưởng Yūma là lãnh chúa chẳng màng chính trị, cậu hiên ngang bước lên trước mặt Thủ tướng Vương quốc."
            ),
            (
                "「我々（われわれ）が目指（めざ）す新（あたら）しい[[政策（せいさく）|2]]は、領民（りょうみん）の幸福（こうふく）を第一（だいいち）とするものだ」。悠真（ゆうま）は領民（りょうみん）代表（だいひょう）を選（えら）ぶ公平（こうへい）な[[選挙（せんきょ）|5]]制度（せいど）を提案（ていあん）し、身分（みぶん）を問（と）わず全員（ぜんいん）が一票（いっぴょう）を[[投票（とうひょう）|6]]できる権利（けんり）を訴（うった）えた。「他国（たこく）との戦争（せんそう）への[[懸念（けねん）|9]]を払拭（ふっしょく）するため、誠実（せいじつ）な[[外交（がいこう）|7]]によって隣国（りんごく）と不可侵（ふかしん）の[[条約（じょうやく）|8]]を結（むす）びたいのです！」",
                "'Chính sách mới mà chúng tôi hướng tới đặt hạnh phúc của người dân lên hàng đầu.' Yūma đề xuất chế độ bầu cử công bằng để chọn đại diện nhân dân, kêu gọi mọi người không phân biệt thân phận đều có thể đi bỏ phiếu bầu. 'Để xóa bỏ mọi mối quan ngại về chiến tranh với nước láng giềng, tôi muốn thông qua ngoại giao chân thành ký kết hiệp ước hòa bình bất khả xâm phạm với họ!'"
            ),
            (
                "しかし腐敗（ふはい）したバルド公爵（こうしゃく）は「平民（へいみん）に税（ぜい）を納（おさ）める[[義務（ぎむ）|17]]はあるが、[[政治|1]]に口（くち）を出（だ）す[[権利（けんり）|16]]はない！」と怒鳴（どな）り、密輸（みつゆ）の罪（つみ）を悠真（ゆうま）になすりつけようとした。けれど悠真（ゆうま）は、公爵（こうしゃく）が王国の[[法律（ほうりつ）|10]]に[[違反（いはん）|15]]して闇取引（やみとりひき）をしていた決定的（けっていてき）な[[証拠（しょうこ）|21]]の帳簿（ちょうぼ）を議場（ぎじょう）に叩（たた）きつけた！",
                "Thế nhưng Công tước Baldo thối nát quát tháo: 'Thường dân có nghĩa vụ nộp thuế, chứ không có quyền lợi tham gia chính sự!' rồi toan đổ tội buôn lậu lên đầu Yūma. Nào ngờ Yūma đã đập mạnh lên bàn nghị trường cuốn sổ cái bằng chứng thép chứng minh chính gã công tước đã vi phạm luật pháp vương quốc để giao dịch phi pháp!"
            ),
            (
                "すぐさま王立（おうりつ）法廷（ほうてい）で特別（とくべつ）[[裁判（さいばん）|18]]が開（ひら）かれ、国王（こくおう）自ら（みずから）下（くだ）した厳格（げんかく）な[[判決（はんけつ）|19]]によって公爵（こうしゃく）は厳（きび）しく[[罰（ばっ）せ|20]]られた。これを機（き）に議会（ぎかい）は古びた貴族（きぞく）優遇（ゆうぐう）法（ほう）を[[改正（かいせい）|12]]し、誰（だれ）もが法（ほう）を[[遵守（じゅんしゅ）|14]]する公正（こうせい）な新法（しんぽう）を[[制定（せいてい）|11]]した。新（あたら）しい規則（きそく）は翌月（よくげつ）から正式（せいしき）に[[施行（しこう）され|13]]、王都（おうと）中（じゅう）から喝采（かっさい）が起（お）きた。",
                "Ngay lập tức một phiên tòa đặc biệt được mở tại Tòa án Hoàng gia, và theo bản án phán quyết nghiêm khắc do chính Quốc vương tuyên đọc, gã công tước đã bị trừng phạt đích đáng. Nhân cơ hội đó, Nghị viện sửa đổi bộ luật cũ ưu ái quý tộc, ban hành bộ luật công minh mới bắt buộc mọi người phải tuân thủ pháp luật. Quy định mới chính thức được thi hành từ tháng kế tiếp, nhận được tiếng reo hò vang dội khắp Vương đô."
            ),
            (
                "祝勝（しゅくしょう）の夜（よる）、悠真（ゆうま）とセレスはエルディア森（もり）の奥（おく）で発見（はっけん）された古代（こだい）の[[遺跡（いせき）|23]]を訪（おとず）れた。石碑（せきひ）に刻（きざ）まれた文字（もじ）を解読（かいどく）すると、かつて[[歴史（れきし）|22]]上（じょう）もっとも[[栄（さか）え|24]]た魔法（まほう）文明（ぶんめい）が、傲慢（ごうまん）と環境（かんきょう）破壊（はかい）によって一夜（いちや）にして[[滅（ほろ）び|25]]たという警告（けいこく）が記（しる）されていたのだ――。",
                "Đêm mừng thắng lợi, Yūma và Celes ghé thăm khu di tích cổ đại vừa được phát hiện sâu trong khu rừng Eldia. Khi giải mã những dòng văn tự khắc trên bia đá, cả hai bàng hoàng trước lời cảnh báo trong lịch sử: nền văn minh ma thuật từng phồn vinh hưng thịnh nhất xưa kia đã sụp đổ diệt vong chỉ sau một đêm vì sự ngạo mạn và hủy hoại môi trường..."
            ),
        ],
        "quiz": [
            {
                "prompt": "新しい交通（こうつう）ルールを（　　）し、歩行者（ほこうしゃ）の安全（あんぜん）を守（まも）る。",
                "options": ["違反（いはん）", "制定（せいてい）", "罰（ばっ）する", "滅（ほろ）びる"],
                "ans": 2,
                "right_exp": "Quá chuẩn! `法律・ルールを制定（せいてい）する` là lập ra và ban hành luật lệ mới.",
                "wrong_exps": [
                    "`違反（いはん）する` là làm trái vi phạm luật chứ không phải tạo ra luật.",
                    "Chính xác! `制定する` là ban hành/chế định luật mới.",
                    "`罰（ばっ）する` là xử phạt người có lỗi.",
                    "`滅（ほろ）びる` là diệt vong (tự động từ)."
                ]
            },
            {
                "prompt": "改正（かいせい）された新（あたら）しい法律（ほうりつ）が、来月（らいげつ）1日から正式（せいしき）に（　　）。",
                "options": ["投票（とうひょう）される", "栄（さか）える", "施行（しこう）される", "主張（しゅちょう）される"],
                "ans": 3,
                "right_exp": "Tuyệt vời! `法律が施行（しこう）される` là từ chuyên môn để chỉ luật bắt đầu có hiệu lực thực thi.",
                "wrong_exps": [
                    "`投票される` là được bỏ phiếu bầu.",
                    "`栄える` là phồn vinh hưng thịnh.",
                    "Chuẩn xác! `施行（しこう）される` = chính thức có hiệu lực thi hành.",
                    "`主張される` là được chủ trương khẳng định."
                ]
            },
            {
                "prompt": "どんな企業（きぎょう）も、社会のルールや法律を（　　）義務（ぎむ）がある。",
                "options": ["懸念（けねん）する", "遵守（じゅんしゅ）する", "違反（いはん）する", "改正（かいせい）する"],
                "ans": 2,
                "right_exp": "Chính xác! `法律・規則を遵守（じゅんしゅ）する` là tuân thủ nghiêm chỉnh luật pháp, cụm từ ruột trong đề N2!",
                "wrong_exps": [
                    "`懸念（けねん）する` là lo ngại quan ngại.",
                    "Quá chuẩn! `ルールを遵守（じゅんしゅ）する`.",
                    "`違反（いはん）する` đi với trợ từ に (`ルールに違反する`) và mang nghĩa vi phạm.",
                    "`改正（かいせい）する` chỉ do nhà nước/cơ quan có thẩm quyền thực hiện."
                ]
            },
            {
                "prompt": "住民（じゅうみん）の間（あいだ）に、環境（かんきょう）悪化（あっか）に対（たい）する強（つよ）い（　　）が広（ひろ）がっている。",
                "options": ["判決（はんけつ）", "証拠（しょうこ）", "条約（じょうやく）", "懸念（けねん）"],
                "ans": 4,
                "right_exp": "Đỉnh cao! `懸念（けねん）` là mối lo ngại, quan ngại trước nguy cơ xấu có thể xảy ra.",
                "wrong_exps": [
                    "`判決（はんけつ）` là bản án của tòa án.",
                    "`証拠（しょうこ）` là bằng chứng chứng cứ.",
                    "`条約（じょうやく）` là hiệp ước ký giữa các quốc gia.",
                    "Chính xác! `〜に対する懸念` = mối quan ngại đối với..."
                ]
            },
            {
                "prompt": "数百年（すうひゃくねん）前（まえ）まで大いに（　　）いた巨大（きょだい）な帝国（ていこく）も、やがて滅（ほろ）びた。",
                "options": ["栄（さか）えて", "施行（しこう）して", "罰（ばっ）して", "投票（とうひょう）して"],
                "ans": 1,
                "right_exp": "Xuất sắc! `栄（さか）える` là hưng thịnh phồn vinh, đối lập trực tiếp với vế sau `やがて滅びた` (rồi cũng diệt vong).",
                "wrong_exps": [
                    "Chuẩn rồi! `栄（さか）える` ↔ `滅（ほろ）びる` là cặp đối nghĩa lịch sử hay gặp.",
                    "`施行する` dùng cho luật pháp/quy định.",
                    "`罰する` là trừng phạt.",
                    "`投票する` là bỏ phiếu bầu."
                ]
            },
        ],
    },
    {
        "num": 4,
        "slug": "chuong-04",
        "lesson_id": "p1_c08_b01",
        "title_jp": "第4章：古代（こだい）の警告（けいこく）――[[生態系（せいたいけい）|3]]の危機（きき）と[[再生（さいせい）|13]]の光（ひかり）",
        "title_vi": "Chương 04: Cảnh Báo Từ Cổ Đại — Khủng Hoảng Hệ Sinh Thái & Ánh Sáng Tái Sinh",
        "yuki_reminder_top": "Chương 04 đưa em chạm vào chủ đề hay thi Đọc hiểu N2 cực mạnh: **22 từ Bài 18 — Phần 1 Chương 8 Bài 1 (Môi trường tự nhiên, Sinh thái & Vũ trụ)**! Từ `地球温暖化・気候変動・生態系・絶滅・環境破壊`, đến hành động cứu lấy thế giới của Yūma và cô bé thiên tài giả kim Luna như `汚染・排出・削減・保護・保全・資源・枯渇・再生・再利用・省エネ`, cộng thêm `現象・観測・宇宙・植物・微生物・蒸発・酸素`! 🌍🌱",
        "yuki_reminder_bottom": "Cùng Yūma và Luna vừa cứu rừng thánh vừa thuộc làu 22 từ môi trường-sinh thái rồi nha! Nhớ phân biệt cặp `保護` (bảo vệ cụ thể động thực vật khỏi nguy hiểm) với `保全` (bảo tồn giữ nguyên vẹn cả hệ sinh thái/môi trường) đó em! Làm 5 câu trắc nghiệm nhanh nào 💚",
        "soft_notes": [
            (2, "Nhắc nhẹ 2 từ cực giống nhau: `保護（ほご）` vs `保全（ほぜん）` 🌱", "Trong tiếng Nhật, `保護（ほご）` là bảo vệ (VD: động vật quý hiếm, trẻ em, dữ liệu cá nhân), còn `保全（ほぜん）` là giữ gìn bảo tồn toàn vẹn không để hư hại suy giảm (VD: bảo tồn môi trường tự nhiên `自然環境を保全する`) nha em!"),
            (4, "Combo chữ Hán dễ đọc sai ✨", "Để ý âm đọc của `[[枯渇（こかつ）する|12]]` (cạn kiệt tài nguyên — `こかつ`, nhớ chữ Khô + Khát), `[[微生物（びせいぶつ）|20]]` (`びせいぶつ`, đừng nhầm sang びしょうぶつ!), và `[[蒸発（じょうはつ）する|21]]` (bốc hơi — có âm `つ` khi ghép nhưng đọc là `じょうはつ`) nhé!"),
        ],
        "paragraphs": [
            (
                "遺跡（いせき）の地下（ちか）では、千年（せんねん）前（まえ）の暴走（ぼうそう）した魔石（ませき）炉（ろ）が今（いま）も不気味（ぶきみ）な熱気（ねっき）を放（はな）ち続（つづ）けていた。そのせいで領内（りょうない）では異常（いじょう）な[[気候変動（きこうへんどう）|2]]が起（お）き、現代（げんだい）の[[地球温暖化（ちきゅうおんだんか）|1]]のように気温（きおん）が上昇（じょうしょう）して川（かわ）の水（みず）が急激（きゅうげき）に[[蒸発（じょうはつ）|21]]しつつあった。",
                "Bên dưới lòng đất di tích, lò ma thạch mất kiểm soát từ một nghìn năm trước đến nay vẫn tiếp tục tỏa ra hơi nóng rùng rợn. Chính vì thế, trong lãnh địa đang xảy ra biến đổi khí hậu bất thường: nhiệt độ tăng cao hệt như sự nóng lên toàn cầu ở thời hiện đại khiến nước sông ngòi bốc hơi nhanh chóng."
            ),
            (
                "領内（りょうない）のラボで調査（ちょうさ）に協力（きょうりょく）する天才（てんさい）少女（しょうじょ）ルナは、「このまま魔力（まりょく）の黒煙（こくえん）を[[排出（はいしゅつ）|7]]し続（つづ）けたら、聖域（せいいき）の泉（いずみ）を[[汚染（おせん）|6]]するだけでなく、森（もり）の[[生態系（せいたいけい）|3]]が崩（くず）れて[[絶滅（ぜつめつ）|4]]する精霊獣（せいれいじゅう）も出（で）てしまいます！」と震（ふる）えた。これこそが先人（せんじん）の[[環境破壊（かんきょうはかい）|5]]が招（まね）いた悲劇（ひげき）だったのだ。",
                "Tại phòng nghiên cứu trong lãnh địa, cô bé thiên tài giả kim Luna đang hỗ trợ điều tra run rẩy nói: 'Nếu lò cứ tiếp tục thải ra khói đen ma lực thế này, nó không chỉ gây ô nhiễm con suối thánh mà còn làm hệ sinh thái khu rừng sụp đổ khiến nhiều linh thú có nguy cơ tuyệt chủng mất!' Đây đích thực là bi kịch mà sự phá hủy môi trường của người xưa để lại."
            ),
            (
                "「よし、魔力炉（まりょくろ）を停止（ていし）して熱（ねつ）ガスを大幅（おおはば）に[[削減（さくげん）|8]]しよう！」と悠真（ゆうま）が命（めい）じる。これまで無尽蔵（むじんぞう）だと思（おも）われていた魔結晶（まけっしょう）などの[[資源（しげん）|11]]は有限（ゆうげん）であり、乱獲（らんかく）すればすぐに[[枯渇（こかつ）|12]]してしまうからだ。",
                "'Được rồi, chúng ta hãy dừng lò ma lực và cắt giảm mạnh lượng khí nhiệt thải ra!' Yūma ra lệnh. Bởi vì những tài nguyên như tinh thể ma thạch vốn từng bị tưởng là vô tận thực chất đều có giới hạn, nếu khai thác bừa bãi thì sẽ nhanh chóng cạn kiệt."
            ),
            (
                "悠真（ゆうま）は希少（きしょう）な精霊獣（せいれいじゅう）を森（もり）で手厚（てあつ）く[[保護（ほご）|9]]しつつ、辺境（へんきょう）の豊かな自然（しぜん）環境（かんきょう）を丸（まる）ごと[[保全（ほぜん）|10]]する計画（けいかく）を立（た）てた。魔力（まりょく）の消費（しょうひ）を抑（おさ）える[[省（しょう）エネ|15]]型（がた）の魔法（まほう）ランプを普及（ふきゅう）させ、使（つか）い終（お）わった結晶（けっしょう）のかけらも溶（と）かして[[再利用（さいりよう）|14]]した。すると風力（ふうりょく）と水力（すいりょく）による[[再生（さいせい）|13]]可能（かのう）エネルギーが王都（おうと）の電力（でんりょく）網（もう）に匹敵（ひってき）する明（あか）るさを生（う）み出（だ）した！",
                "Yūma vừa ân cần bảo vệ các linh thú quý hiếm trong rừng, vừa vạch ra kế hoạch bảo tồn nguyên vẹn môi trường tự nhiên trù phú của vùng biên ải. Cậu phổ cập loại đèn ma pháp tiết kiệm năng lượng giúp giảm tiêu hao ma lực, đồng thời nấu chảy những mảnh tinh thể đã dùng xong để tái sử dụng. Thế là nguồn năng lượng tái tạo từ sức gió và sức nước đã tạo nên ánh sáng rực rỡ sánh ngang lưới điện hiện đại!"
            ),
            (
                "ルナの知恵（ちえ）も光（ひか）った。汚染（おせん）された土（つち）を浄化（じょうか）する特殊（とくしゅ）な[[微生物（びせいぶつ）|20]]を培養（ばいよう）し、光を浴（あ）びてたっぷり[[酸素（さんそ）|22]]を作（つく）り出（だ）す魔法（まほう）[[植物（しょくぶつ）|19]]を森（もり）中（じゅう）に植（う）えたのだ。ある夜（よる）、天体（てんたい）望遠鏡（ぼうえんきょう）で[[宇宙（うちゅう）|18]]を[[観測（かんそく）|17]]していた二人は、森（もり）の上（うえ）空（ぞら）で七色（なないろ）の光（ひかり）の柱（はしら）が舞（ま）う神秘的（しんぴてき）な自然（しぜん）[[現象（げんしょう）|16]]を目（ま）の当（あ）たりにして、「自然（しぜん）が息（いき）を吹（ふ）き返（かえ）したんですね！」と手（て）を取り合（とりあ）って喜（よろこ）んだ。",
                "Trí tuệ của Luna cũng tỏa sáng rực rỡ. Cô bé nuôi cấy loài vi sinh vật đặc biệt có khả năng thanh lọc đất ô nhiễm, đồng thời trồng khắp rừng giống thực vật ma pháp hấp thụ ánh sáng để sản sinh dồi dào khí oxy. Một đêm nọ, khi đang dùng kính thiên văn quan sát vũ trụ, cả hai tận mắt chứng kiến hiện tượng tự nhiên thần bí với cột sáng bảy sắc nhảy múa trên bầu trời khu rừng, liền nắm chặt tay reo mừng: 'Thiên nhiên hồi sinh thật rồi anh ơi!'."
            ),
        ],
        "quiz": [
            {
                "prompt": "森林伐採（しんりんばっさい）が進（すす）めば、森（もり）の（　　）が壊（こわ）れて多くの動物が住（す）めなくなる。",
                "options": ["微生物（びせいぶつ）", "生態系（せいたいけい）", "酸素（さんそ）", "宇宙（うちゅう）"],
                "ans": 2,
                "right_exp": "Chính xác! `生態系（せいたいけい）が壊れる` là hệ sinh thái bị phá vỡ, chuẩn đề N2!",
                "wrong_exps": [
                    "`微生物` là vi sinh vật nhỏ bé trong đất/nước.",
                    "Quá chuẩn! `生態系（せいたいけい）` = hệ sinh thái.",
                    "`酸素` là khí oxy.",
                    "`宇宙` là vũ trụ bên ngoài Trái Đất."
                ]
            },
            {
                "prompt": "石油（せきゆ）などの限（かぎ）られたエネルギー（　　）は、いつか枯渇（こかつ）する恐れがある。",
                "options": ["現象（げんしょう）", "資源（しげん）", "変動（へんどう）", "再生（さいせい）"],
                "ans": 2,
                "right_exp": "Tuyệt vời! `エネルギー資源（しげん）が枯渇（こかつ）する` = nguồn tài nguyên năng lượng bị cạn kiệt.",
                "wrong_exps": [
                    "`現象` là hiện tượng tự nhiên/xã hội.",
                    "Chính xác! `資源（しげん）` là tài nguyên thiên nhiên.",
                    "`変動` là sự biến động thay đổi.",
                    "`再生` là tái sinh, phục hồi."
                ]
            },
            {
                "prompt": "プラスチックゴミを減らすため、一度使（つか）った瓶（びん）を洗（あら）って（　　）する取組（とりく）みが広がっている。",
                "options": ["排出（はいしゅつ）", "汚染（おせん）", "蒸発（じょうはつ）", "再利用（さいりよう）"],
                "ans": 4,
                "right_exp": "Chuẩn luôn! Rửa chai lọ đã dùng để sử dụng lại là `再利用（さいりよう）する`.",
                "wrong_exps": [
                    "`排出する` là thải ra ngoài (khí thải, rác).",
                    "`汚染する` là gây ô nhiễm.",
                    "`蒸発する` là bốc hơi nước.",
                    "Đúng rồi! `再利用する` = tái sử dụng."
                ]
            },
            {
                "prompt": "工場（こうじょう）から出（で）るCO2の（　　）量（りょう）を10年後（ねんご）までに半分（はんぶん）に（　　）目標（もくひょう）を立てた。",
                "options": ["排出・削減する", "保護・保全する", "観測・絶滅する", "蒸発・汚染する"],
                "ans": 1,
                "right_exp": "Quá đỉnh! `排出（はいしゅつ）量` (lượng khí thải ra) + `削減（さくげん）する` (cắt giảm bớt đi) là bộ đôi hoàn hảo!",
                "wrong_exps": [
                    "Chính xác tuyệt đối! Lượng phát thải CO2 (`排出量`) + cắt giảm (`削減する`).",
                    "`保護・保全` đều mang nghĩa bảo vệ giữ gìn, không dùng cho khí CO2.",
                    "`観測` là quan sát, `絶滅` là tuyệt chủng.",
                    "`蒸発・汚染` hoàn toàn lệch nghĩa mục tiêu giảm khí thải."
                ]
            },
            {
                "prompt": "石油（せきゆ）などの天然資源（てんねんしげん）は、このまま使（つか）い続（つづ）けると近（ちか）いうちに（　　）してしまう。",
                "options": ["再利用（さいりよう）", "保全（ほぜん）", "枯渇（こかつ）", "観測（かんそく）"],
                "ans": 3,
                "right_exp": "Xuất sắc! `資源が枯渇（こかつ）する` = nguồn tài nguyên cạn kiệt sạch không còn giọt nào.",
                "wrong_exps": [
                    "`再利用` là tái sử dụng (ý tích cực, không hợp với 'nếu cứ tiêu thụ mãi').",
                    "`保全` là bảo tồn giữ gìn.",
                    "Chuẩn rồi! `枯渇（こかつ）する` là từ đinh của bài Môi trường.",
                    "`観測` là đo đạc quan sát thiên văn/khí tượng."
                ]
            },
        ],
    },
    {
        "num": 5,
        "slug": "chuong-05",
        "lesson_id": "p1_c08_b02",
        "title_jp": "第5章：ルナとの[[開発（かいはつ）|1]]と[[画期的（かっきてき）|3]]な[[技術革新（ぎじゅつかくしん）|2]]",
        "title_vi": "Chương 05: Nghiên Cứu Cùng Luna & Cuộc Cách Mạng Công Nghệ Mang Tính Đột Phá",
        "yuki_reminder_top": "Chương 05 siêu bùng nổ với **22 từ Bài 19 — Phần 1 Chương 8 Bài 2 (Khoa học, Nghiên cứu & Công nghệ cao)**! Hãy xem cặp đôi kỹ sư Yūma × nhà giả kim Luna kết hợp phép thuật với khoa học hiện đại bằng `仮説・実験・検証・分析・解明・探求・測定・精度・抽出・合成・装置・効率`, cho tới tạo nên `発明・発見・実用化・特許・人工知能・遺伝子・細胞` nhé! 🔬⚙️✨",
        "yuki_reminder_bottom": "Chà chà, phòng lab ma pháp của Yūma và Luna ngầu hết nấc luôn rồi! Trong bài này đừng quên phân biệt cực gắt giữa `発明（はつめい）` (sáng chế cái CHƯA từng tồn tại như bóng đèn/robot) và `発見（はっけん）` (phát hiện thứ ĐÃ tồn tại sẵn như ngôi sao/loài mới) nha em! Cùng thử tài 5 câu quiz nào 🌸",
        "soft_notes": [
            (1, "Kinh điển JLPT: `発明（はつめい）` vs `発見（はっけん）` 💡", "Cứ nhớ mẹo này từ chị Yuki nè:\n- **発**明 (MINH): tạo ra máy móc, công cụ *chưa từng có* (VD: 電話を発明する).\n- **発**見 (KIẾN): nhìn thấy, tìm ra thứ *vốn đã có sẵn* trong tự nhiên (VD: 新しい星・ウイルスを発見する).\nĐề N2 cực thích tráo hai chữ này trong câu trắc nghiệm đó em!"),
            (4, "Lưu ý cặp âm Hán Việt đọc dễ lộn 🔬", "`精度（せいど）` = độ chính xác (KHÔNG phải chế độ `制度` — cùng đọc せいど nên phải nhìn Kanji!), `効率（こうりつ）` = hiệu suất (đứng cùng `率` ở bài sau sẽ đọc là りつ), còn `仮説（かせつ）` đọc nhẹ là **かせつ** (giả thuyết)!"),
        ],
        "paragraphs": [
            (
                "魔導（まどう）ギルドの妨害（ぼうがい）に対抗（たいこう）するため、悠真（ゆうま）とルナは新（あたら）しい生活（せいかつ）魔道具（まどうぐ）を[[開発（かいはつ）|1]]することにした。「王都（おうと）の贅沢品（ぜいたくひん）に頼（たよ）らない、領民（りょうみん）みんなが使える魔法（まほう）の[[技術革新（ぎじゅつかくしん）|2]]を起こす（おこす）んだ！」――それは貴族（きぞく）独占（どくせん）の常識（じょうしき）を覆（くつがえ）す[[画期的（かっきてき）|3]]な挑戦（ちょうせん）だった。",
                "Để đối đầu với sự chèn ép của Hiệp hội Ma đạo sĩ, Yūma và Luna quyết định phát triển những ma cụ sinh hoạt mới. 'Chúng ta sẽ tạo ra cuộc đổi mới công nghệ ma pháp mà mọi người dân đều dùng được chứ không phụ thuộc vào đồ xa xỉ của Vương đô!' — Đó là thách thức mang tính bước ngoặt lật đổ định kiến độc quyền quý tộc."
            ),
            (
                "二人はまず「薬草（やくそう）の治癒（ちゆ）成分（せいぶん）と魔石（ませき）の熱（ねつ）を反応（はんのう）させれば、安価（あんか）な万能薬（ばんのうやく）ができるはずだ」という[[仮説（かせつ）|8]]を立（た）てた。研究室（けんきゅうしつ）に籠（こ）もり、何百（なんびゃく）回（かい）も[[実験（じっけん）|9]]を繰（く）り返（かえ）して数値を記録（きろく）し、[[仮説|8]]が正（ただ）しいかどうか徹底（てってい）的（てき）に[[検証（けんしょう）|10]]した。",
                "Trước tiên, hai người đặt ra giả thuyết rằng 'nếu cho thành phần trị thương của thảo dược phản ứng với nhiệt của ma thạch thì sẽ tạo ra thuốc vạn năng giá rẻ'. Đóng cửa ở lỳ trong phòng nghiên cứu, họ lặp đi lặp lại hàng trăm cuộc thí nghiệm để ghi lại số liệu và kiểm chứng triệt để xem giả thuyết có đúng hay không."
            ),
            (
                "ルナは植物（しょくぶつ）から有効（ゆうこう）成分（せいぶん）を丁寧（ていねい）に[[抽出（ちゅうしゅつ）|20]]し、魔力（まりょく）触媒（しょくばい）と[[合成（ごうせい）|21]]して試薬（しやく）を作（つく）った。顕微鏡（けんびきょう）を真似（まね）た魔導（まどう）レンズで生体（せいたい）[[細胞（さいぼう）|19]]の動（うご）きを覗（のぞ）き込（こ）み、魔獣（まじゅう）と人間（にんげん）の回復（かいふく）[[遺伝子（いでんし）|18]]の違い（ちがい）まで細（こま）かく[[分析（ぶんせき）|11]]して、長（なが）年（ねん）の病（やまい）の仕組み（しくみ）を次々（つぎつぎ）と[[解明（かいめい）|12]]していく。",
                "Luna cẩn thận chiết xuất hoạt chất từ thảo mộc rồi tổng hợp cùng chất xúc tác ma lực để tạo thuốc thử. Nhìn qua thấu kính ma đạo mô phỏng kính hiển vi để quan sát chuyển động của tế bào sống, phân tích tỉ mỉ sự khác biệt của gen di truyền hồi phục giữa ma thú và con người, cả hai lần lượt làm sáng tỏ cơ chế của nhiều căn bệnh lâu năm."
            ),
            (
                "さらに未知（みち）の真理（しんり）を[[探求（たんきゅう）|13]]する悠真（ゆうま）は、温度（おんど）と圧力（あつりょく）を自動（じどう）で[[測定（そくてい）|14]]する精密（せいみつ）[[装置（そうち）|16]]を[[発明（はつめい）|4]]した。その途中（とちゅう）、地下室（ちかしつ）の古文書（こもんじょ）から「自律（じりつ）思考（しこう）魔導核（まどうかく）」――現代（げんだい）の[[人工知能（じんこうちのう）|17]]にそっくりな古代（こだい）の知性（ちせい）結晶（けっしょう）まで[[発見（はっけん）|5]]したのだ！",
                "Không ngừng tìm tòi khám phá chân lý chưa ai biết tới, Yūma còn phát minh ra một thiết bị chính xác tự động đo đạc nhiệt độ và áp suất. Trong quá trình đó, từ cuộn cổ thư dưới hầm, cậu còn tình cờ phát hiện ra 'Lõi ma đạo tư duy tự hành' — viên tinh thể trí tuệ cổ đại hệt như trí tuệ nhân tạo (AI) ở thế giới hiện đại!"
            ),
            (
                "人工知能（じんこうちのう）並（な）みの計算（けいさん）力で製造（せいぞう）[[精度（せいど）|15]]を極限（きょくげん）まで高（たか）めると、生産（せいさん）[[効率（こうりつ）|22]]は以前（いぜん）の十倍（じゅうばい）に跳（は）ね上（あ）がった。完成（かんせい）した新薬（しんやく）と自動（じどう）灌漑（かんがい）システムはただちに[[実用化（じつようか）|6]]され、悠真（ゆうま）は王室（おうしつ）へ正式（せいしき）に[[特許（とっきょ）|7]]を登録（とうろく）して、他領（たりょう）への違法（いほう）コピーを完全（かんぜん）に防（ふせ）いだのだった。",
                "Nhờ sức tính toán ngang ngửa AI giúp nâng cao độ chính xác chế tạo lên mức tối đa, hiệu suất sản xuất tăng vọt gấp mười lần trước đây. Loại thuốc mới và hệ thống tưới tiêu tự động hoàn thành lập tức được đưa vào ứng dụng thực tế, và Yūma nhanh tay đăng ký bằng sáng chế độc quyền lên Hoàng thất để ngăn chặn triệt để nạn sao chép lậu từ các lãnh địa khác."
            ),
        ],
        "quiz": [
            {
                "prompt": "これまで解（と）けなかった病気（びょうき）の原因（げんいん）が、最新の研究（けんきゅう）によってようやく（　　）。",
                "options": ["発明（はつめい）された", "発見（はっけん）された", "解明（かいめい）された", "抽出（ちゅうしゅつ）された"],
                "ans": 3,
                "right_exp": "Chính xác! `原因・謎を解明（かいめい）する` là làm sáng tỏ, giải đáp được nguyên nhân bí ẩn bấy lâu nay.",
                "wrong_exps": [
                    "`発明` là sáng chế phát minh ra sản phẩm/máy móc mới.",
                    "`発見` là tìm thấy vật thể/sự vật có sẵn (thường dùng là `新種を発見する`, `原因を解明する` tự nhiên hơn nhiều!).",
                    "Quá chuẩn! `原因を解明する` = làm sáng tỏ nguyên nhân.",
                    "`抽出` là chiết xuất tinh chất hoặc lọc dữ liệu."
                ]
            },
            {
                "prompt": "新しい技術（ぎじゅつ）でとても便利な（　　）を作（つく）ったので、国（くに）に特許（とっきょ）を申請（しんせい）した。",
                "options": ["効率（こうりつ）", "装置（そうち）", "仮説（かせつ）", "精度（せいど）"],
                "ans": 2,
                "right_exp": "Tuyệt vời! `便利な装置（そうち）` là thiết bị, máy móc tiện lợi để xin bằng sáng chế (`特許`).",
                "wrong_exps": [
                    "`効率` là hiệu suất.",
                    "Đúng rồi! `装置（そうち）` = thiết bị/máy móc.",
                    "`仮説` là giả thuyết khoa học.",
                    "`精度` là độ chính xác."
                ]
            },
            {
                "prompt": "まず大胆（だいたん）な（　　）を立（た）て、それか正しいかどうか実験（じっけん）で検証（けんしょう）する。",
                "options": ["仮説（かせつ）", "遺伝子（いでんし）", "細胞（さいぼう）", "特許（とっきょ）"],
                "ans": 1,
                "right_exp": "Quá chuẩn! Mẫu kết hợp kinh điển `仮説（かせつ）を立てる` = đặt ra giả thuyết trước khi làm thí nghiệm kiểm chứng.",
                "wrong_exps": [
                    "Chính xác! `仮説を立てる` + `検証する` đi cặp với nhau rất chặt.",
                    "`遺伝子` là gen di truyền.",
                    "`細胞` là tế bào.",
                    "`特許` là bằng sáng chế độc quyền."
                ]
            },
            {
                "prompt": "仕事（しごと）のやり方（かた）を工夫（くふう）して、生産（せいさん）（　　）を二倍（にばい）に高（たか）めた。",
                "options": ["技術革新（ぎじゅつかくしん）", "効率（こうりつ）", "分析（ぶんせき）", "探求（たんきゅう）"],
                "ans": 2,
                "right_exp": "Chuẩn không cần chỉnh! `効率（こうりつ）を高める・効率が良い` = nâng cao hiệu suất công việc.",
                "wrong_exps": [
                    "`技術革新` là sự đổi mới công nghệ (không gắn với 'gấp đôi').",
                    "Tuyệt vời! `生産効率（こうりつ）` = hiệu suất sản xuất.",
                    "`分析` là phân tích dữ liệu.",
                    "`探求` là tìm tòi khám phá."
                ]
            },
            {
                "prompt": "植物（しょくぶつ）の葉（は）から、肌（はだ）にいい天然（てんねん）のオイル成分（せいぶん）を（　　）した。",
                "options": ["測定（そくてい）", "抽出（ちゅうしゅつ）", "実用化（じつようか）", "開発（かいはつ）"],
                "ans": 2,
                "right_exp": "Chính xác! Lấy/tách tinh chất từ thực vật dùng động từ `抽出（ちゅうしゅつ）する` (chiết xuất).",
                "wrong_exps": [
                    "`測定する` là đo đạc số liệu/nhiệt độ/khối lượng.",
                    "Quá chuẩn! `成分を抽出する` = chiết xuất thành phần.",
                    "`実用化する` là đưa sản phẩm vào ứng dụng đại trà.",
                    "`開発する` là nghiên cứu phát triển sản phẩm mới."
                ]
            },
        ],
    },
    {
        "num": 6,
        "slug": "chuong-06",
        "lesson_id": "p1_c09_b01",
        "title_jp": "第6章：魔王軍（まおうぐん）襲来（しゅうらい）！[[膨大（ぼうだい）な|15]]データと[[全体（ぜんたい）|20]]作戦（さくせん）",
        "title_vi": "Chương 06: Ma Vương Quân Tập Kích! Dữ Liệu Khổng Lồ & Chiến Lược Số Học",
        "yuki_reminder_top": "Chương 06 biến toàn bộ chiến trường dị giới thành bài toán chiến lược với **20 từ Bài 20 — Phần 1 Chương 9 Bài 1 (Số lượng, Tỷ lệ & Mức độ)**! Coi đủ hết nha em: `平均・割合・比率・最大・最小・増加・減少・急増・急減・上回る・下回る・半数・過半数・およそ・前後・未満・わずか・膨大な・相当・余り・過剰・不足・全体・一部`! Vừa căng thẳng vừa cực dễ nhớ bảng từ số lượng luôn 🧮⚔️",
        "yuki_reminder_bottom": "Thắng lợi trí tuệ siêu mãn nhãn luôn phải không em? Mẹo thi JLPT N2 của bài này là phân biệt **chốt mốc** của `未満` (dưới mức, KHÔNG tính mốc đó, VD 18歳未満 = từ 17 trở xuống) với `以下` (từ mốc đó trở xuống), và phân biệt `半数` (đúng một nửa 50%) vs `過半数` (quá nửa >50%)! Chinh phục 5 câu trắc nghiệm thôi nào 🌟",
        "soft_notes": [
            (2, "Nhớ kỹ ranh giới chết người: `未満（みまん）` vs `以下（いか）` 🎯", "Rất nhiều bạn thi N2 hay mất điểm ở đây nha em:\n- `[[未満（みまん）|13]]`: **CHƯA ĐẠT MỐC** (`18歳未満` = dưới 18 tuổi, tức 18 tuổi KHÔNG được tính!).\n- `以下（いか）`: **BẰNG HOẶC DƯỚI** (`18歳以下` = từ 18 tuổi trở xuống).\nTương tự `以上（いじょう）` gồm cả mốc, còn `を超（こ）える` là vượt hẳn trên mốc!"),
            (5, "Cặp `上回る` ↔ `下回る` & `わずか` ✨", "`[[上回（うわまわ）る|7]]` (cao hơn dự kiến/năm trước) và `[[下回（したまわ）る|8]]` (thấp hơn, hụt xuống dưới) luôn lấy mốc so sánh bằng trợ từ `を` (`予想を上回る`)! Còn `[[わずか|14]]` (chỉ một chút ít, vỏn vẹn) hay đi với số nhỏ (`あとわずか`, `わずかな時間`)."),
        ],
        "paragraphs": [
            (
                "平和（へいわ）な領地（りょうち）に突如（とつじょ）、魔界（まかい）の将軍（しょうぐん）率（ひき）いる大軍（たいぐん）が進軍（しんぐん）してきたという急報（きゅうほう）が入（はい）った。王都（おうと）の偵察（ていさつ）部隊（ぶたい）から届（とど）いた報告（ほうこく）書（しょ）は[[膨大（ぼうだい）な|15]]量（りょう）に上（のぼ）り、読（よ）み解（と）くだけでも[[相当（そうとう）|16]]な時間（じかん）がかかると思（おも）われた。",
                "Giữa lúc lãnh địa đang thái bình, tin cấp báo bỗng dội về rằng đại quân do một tướng quân ma giới dẫn đầu đang tiến đánh. Báo cáo từ đội trinh sát Vương đô gửi về nhiều đến mức đồ sộ khổng lồ, tưởng chừng chỉ riêng việc đọc giải mã thôi cũng tốn khoảng thời gian đáng kể."
            ),
            (
                "しかし悠真（ゆうま）は古代（こだい）知性（ちせい）核（かく）でデータ分析（ぶんせき）を[[およそ|11]]一時間（いちじかん）[[余（あま）り|17]]で終（お）え、軍議（ぐんぎ）の席（せき）で地図（ちず）を広（ひろ）げた。「敵（てき）の兵力（へいりょく）は一万（いちまん）人（にん）[[前後（ぜんご）|12]]。ただし[[平均（へいきん）|1]]的（てき）な魔族（まぞく）兵（へい）と新兵（しんぺい）の[[比率（ひりつ）|3]]を調（しら）べると、精鋭（せいえい）の[[割合（わりあい）|2]]は[[全体（ぜんたい）|20]]の[[一部（いちぶ）|20]]――せいぜい二割（にわり）に過（す）ぎない！」",
                "Thế nhưng Yūma dùng Lõi trí tuệ cổ đại hoàn tất phân tích dữ liệu chỉ trong khoảng hơn một tiếng đồng hồ một chút, rồi trải bản đồ ra trước hội nghị quân sự. 'Binh lực địch xấp xỉ khoảng trên dưới một vạn quân. Tuy nhiên khi kiểm tra tỷ suất giữa binh sĩ ma tộc trung bình và tân binh, tỷ lệ tinh nhuệ chỉ là một phần nhỏ trong toàn thể đại quân — nhiều lắm cũng chỉ hai mươi phần trăm mà thôi!'"
            ),
            (
                "「しかも先月（せんげつ）から敵（てき）の魔石（ませき）消費（しょうひ）が[[急増（きゅうぞう）|6]]する一方（いっぽう）で、北（きた）の補給（ほきゅう）路（ろ）からの輸送（ゆそう）は[[急減（きゅうげん）|6]]している。つまり敵（てき）は食料（しょくりょう）[[不足（ふそく）|19]]に陥（おちい）っており、長期戦（ちょうきせん）になれば戦力（せんりょく）が大幅（おおはば）に[[減少（げんしょう）|5]]するはずだ」と悠真（ゆうま）が指摘（してき）すると、議場（ぎじょう）の士気（しき）は一気に[[増加（ぞうか）|5]]した。",
                "'Hơn nữa, từ tháng trước lượng tiêu thụ ma thạch của địch tăng vọt trong khi vận chuyển từ tuyến tiếp tế phía bắc lại giảm đột ngột. Nghĩa là địch đang rơi vào cảnh thiếu hụt quân lương; nếu kéo dài thành chiến sự lâu dài thì chiến lực của chúng chắc chắn sẽ sụt giảm mạnh!' Khi Yūma chỉ ra điều đó, nhuệ khí trong nghị trường lập tức gia tăng vùn vụt."
            ),
            (
                "「残（のこ）り時間（じかん）はあと[[わずか|14]]だが、住民（じゅうみん）の避難（ひなん）はどうする？」とセレスが尋（たず）ねる。「二十歳（はたち）[[未満（みまん）|13]]の若者（わかもの）や子どもは地下（ちか）シェルターへ、大人（おとな）の[[半数（はんすう）|9]]以上（いじょう）――できれば[[過半数（かはんすう）|10]]に後方（こうほう）支援（しえん）へ回（まわ）ってもらう。防衛（ぼうえい）線（せん）の犠牲（ぎせい）は[[最小（さいしょう）|4]]限（げん）に抑（おさ）え、ルナの魔導（まどう）砲（ほう）の威力（いりょく）を[[最大（さいだい）|4]]限（げん）に引（ひ）き出（だ）そう！」",
                "'Thời gian còn lại chỉ còn chút ít thôi, việc sơ tán dân cư tính sao đây ạ?' Celes hỏi. 'Thanh thiếu niên dưới 20 tuổi và trẻ em xuống hầm trú ẩn ngầm, còn hơn một nửa người trưởng thành — lý tưởng nhất là quá bán (trên 50%) — nhờ hỗ trợ hậu cần. Chúng ta sẽ kìm hãm thương vong tuyến phòng thủ ở mức tối thiểu, và phát huy uy lực đại bác ma đạo của Luna lên tối đa!'"
            ),
            (
                "敵（てき）の将軍（しょうぐん）は自軍（じぐん）への[[過剰（かじょう）|18]]な自信（じしん）から罠（わな）に突（つ）っ込（こ）み、味方（みかた）の魔法（まほう）陣（じん）が放（はな）った衝撃（しょうげき）波（は）は悠真（ゆうま）の予想（よそう）をはるかに[[上回（うわまわ）る|7]]威力（いりょく）を見（み）せた。逆（ぎゃく）に敵軍（てきぐん）の損害（そんがい）は敵（てき）が想定（そうてい）していた基準（きじゅん）を大きく[[下回（したまわ）る|8]]結果（けっか）となり、前線（ぜんせん）の魔族（まぞく）たちは総崩（そうくず）れになって撤退（てったい）を始（はじ）めたのだった。",
                "Tướng quân phe địch vì tự tin thái quá vào quân mình nên đâm sầm thẳng vào bẫy; làn sóng xung kích từ trận pháp ma thuật phe ta thể hiện uy lực vượt xa dự tính ban đầu của Yūma. Ngược lại, sức chống trả của quân địch tụt xuống thấp hơn hẳn chuẩn mực chúng dự trù, khiến tiền tuyến ma tộc tan rã toàn bộ và buộc phải rút quân."
            ),
        ],
        "quiz": [
            {
                "prompt": "今月（こんげつ）の売上（うりあげ）は、最初（さいしょ）に立（た）てた目標（もくひょう）を大きく（　　）て、社員（しゃいん）全員（ぜんいん）で喜（よろこ）んだ。",
                "options": ["下回（したまわ）っ", "上回（うわまわ）っ", "不足（ふそく）し", "急減（きゅうげん）し"],
                "ans": 2,
                "right_exp": "Chính xác! Cả công ty đều vui mừng vì doanh thu tháng này *vượt xa mục tiêu đề ra*: `目標を上回る`.",
                "wrong_exps": [
                    "`下回る` là thấp hơn mức mục tiêu (đáng buồn chứ không phải vui mừng!).",
                    "Quá chuẩn! `目標を上回（うわまわ）る`.",
                    "`不足する` là thiếu hụt không đủ.",
                    "`急減する` là giảm đột ngột."
                ]
            },
            {
                "prompt": "この映画（えいが）は法律上、18歳（じゅうはっさい）（　　）の人（ひと）は入場（にゅうじょう）できません。",
                "options": ["前後（ぜんご）", "およそ", "未満（みまん）", "過剰（かじょう）"],
                "ans": 3,
                "right_exp": "Chuẩn luôn! `18歳未満（みまん）` là dưới 18 tuổi (từ 17 tuổi trở xuống, không bao gồm 18).",
                "wrong_exps": [
                    "`前後` là xấp xỉ khoảng trên dưới 18 tuổi.",
                    "`およそ` là trạng từ 'khoảng chừng' đứng trước số lượng.",
                    "Tuyệt vời! `〜歳未満` là mẫu quy định độ tuổi siêu phổ biến.",
                    "`過剰` là dư thừa quá mức."
                ]
            },
            {
                "prompt": "住民（じゅうみん）アンケートで、65％という（　　）の賛成（さんせい）を得（え）て新公園（しんこうえん）の建設（けんせつ）が決（き）まった。",
                "options": ["半数（はんすう）", "過半数（かはんすう）", "一部（いちぶ）", "最小（さいしょう）"],
                "ans": 2,
                "right_exp": "Chính xác! 65% là vượt quá 50% (quá bán để thông qua quyết định) -> `過半数（かはんすう）`!",
                "wrong_exps": [
                    "`半数` chỉ là đúng một nửa (50%).",
                    "Tuyệt đối chuẩn! `過半数（かはんすう）` (> 50%).",
                    "`一部` là chỉ một phần nhỏ.",
                    "`最小` là nhỏ nhất."
                ]
            },
            {
                "prompt": "研究（けんきゅう）のために集（あつ）めた（　　）データの中から、必要（ひつよう）な数字（すうじ）だけを探（さが）し出（だ）す。",
                "options": ["わずかな", "全体（ぜんたい）の", "膨大（ぼうだい）な", "過剰（かじょう）な"],
                "ans": 3,
                "right_exp": "Chính xác! Dữ liệu khổng lồ đồ sộ đi chuẩn nhất với tính từ đuôi な `膨大（ぼうだい）なデータ`.",
                "wrong_exps": [
                    "`わずかな` là ít ỏi nhỏ xíu.",
                    "`全体のデータ` không nhấn mạnh độ nhiều để phải lọc tìm từ bên trong như `膨大なデータ`.",
                    "Quá chuẩn! `膨大なデータ・膨大な量` là collocation vàng của N2.",
                    "`過剰な` mang sắc thái tiêu cực 'thái quá không cần thiết' (thường đi với 包装・期待・摂取)."
                ]
            },
            {
                "prompt": "この商品は環境（かんきょう）を守るため、（　　）な包装（ほうそう）をできるだけなくしている。",
                "options": ["相当（そうとう）", "過剰（かじょう）", "不足（ふそく）", "わずか"],
                "ans": 2,
                "right_exp": "Chuẩn không cần chỉnh! Cụm `過剰（かじょう）な包装（ほうそう）` (bao bì đóng gói dư thừa quá mức gây lãng phí) xuất hiện cực kỳ nhiều trong đề N2!",
                "wrong_exps": [
                    "`相当` là khá nhiều/đáng kể.",
                    "Đúng rồi! `過剰な包装` = đóng gói thừa thãi quá mức.",
                    "`不足` là thiếu hụt.",
                    "`わずか` là ít ỏi."
                ]
            },
        ],
    },
]
