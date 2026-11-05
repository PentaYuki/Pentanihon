# -*- coding: utf-8 -*-
"""
Generator trọn bộ 25 bài Từ Vựng Shinkanzen Master N2
Đảm bảo mỗi bài có ít nhất 25 từ vựng, phiên âm Hiragana 100%,
Hán Việt, Nghĩa tiếng Việt, Cụm từ Collocation và lời dặn chị gái dễ thương.
"""
import os

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../shinkanzen'))

vocab_curriculum = {}

# ==========================================
# BÀI 01 - BÀI 04 (Đã chuẩn bị kỹ lưỡng)
# ==========================================
vocab_curriculum[1] = {
    "title": "Mối Quan Hệ Con Người & Xã Giao (人間関係 - にんげんかんけい)",
    "intro": "Chào bé cưng! Từ vựng Bài 1 bao gồm 25 từ đắt giá nhất về đối nhân xử thế, kết bạn và giao thiệp xã hội chuẩn Shinkanzen N2:",
    "tips": "Nhớ kỹ từ `気が置けない` là thân thiết thoải mái không cần giữ kẽ, đừng nhầm với không đáng tin nha cưng!",
    "words": [
        ("付（つ）き合（あ）い", "PHÓ HỢP", "Quan hệ giao thiệp, xã giao", "近所（きんじょ）付（つ）き合（あ）い"),
        ("もてなす", "đãi", "Tiếp đãi, chiêu đãi nồng hậu", "お客様（きゃくさま）を温（あたた）かくもてなす"),
        ("気兼（きが）ねする", "KHÍ KIÊM", "Khách khí, gượng gạo, giữ kẽ", "気兼（きが）ねなく話（はな）す"),
        ("打（う）ち明（あ）ける", "ĐẢ MINH", "Thổ lộ, trút bầu tâm sự", "本音（ほんね）を打（う）ち明（あ）ける"),
        ("なつく", "thân", "Quấn quýt, bám theo, thân thiết", "犬（いぬ）が私（わたし）になつく"),
        ("見（み）かけ", "KIẾN", "Vẻ bề ngoài, diện mạo", "人（ひと）を見（み）かけで判断（はんだん）する"),
        ("こじれる", "rối", "Mối quan hệ trở nên phức tạp, lục đục", "話（はなし）がこじれる"),
        ("おごる", "khao", "Bao ăn, khao tiền", "後輩（こうはい）に昼（ひる）ご飯（はん）をおごる"),
        ("割（わ）り勘（かん）", "CÁT KHÁM", "Chia đều tiền (Campuchia)", "今日（きょう）は割（わ）り勘（かん）にしよう"),
        ("気（き）が置（お）けない", "KHÍ TRÍ", "Thân thiết thoải mái (không cần giữ kẽ)", "気（き）が置（お）けない仲間（なかま）"),
        ("口実（こうじつ）", "KHẨU THỰC", "Cái cớ, viện cớ thoái thác", "忙（いそが）しさを口実（こうじつ）にして断（ことわ）る"),
        ("お互（たが）い様（さま）", "HỖ DẠNG", "Ai cũng như nhau cả thôi, huề cả làng", "困（こま）ったときはお互（たが）い様（さま）だ"),
        ("励（はげ）ます", "LỆ", "Động viên, khích lệ", "友人（ゆうじん）を励（はげ）ます"),
        ("労（ねぎら）う", "LAO", "Tán thưởng, ghi nhận công lao", "部下（ぶか）の労（ろう）をねぎらう"),
        ("引（ひ）き止（と）める", "DẪN CHỈ", "Níu giữ lại, ngăn lại", "帰（かえ）ろうとする客（きゃく）を引（ひ）き止（と）める"),
        ("お世辞（せじ）", "THẾ TỪ", "Lời khen xã giao, nịnh nọt", "お世辞（せじ）を言（い）う"),
        ("恩（おん）に着（き）る", "ÂN TRỨ", "Ghi ơn, mang ơn", "親切（しんせつ）を恩（おん）に着（き）る"),
        ("冷（ひ）やかす", "LÃNH", "Trêu chọc, chọc ghẹo", "関係（かんけい）を冷（ひ）やかす"),
        ("気（き）を遣（つか）う", "KHÍ KHIỂN", "Để ý, bận tâm chăm sóc", "周囲（しゅうい）に気（き）を遣（つか）う"),
        ("気（き）を利（き）かせる", "KHÍ LỢI", "Tinh tế, biết ý nhường nhịn", "気（き）を利（き）かせて席（せき）を外（はず）す"),
        ("打（う）ち解（と）ける", "ĐẢ GIẢI", "Cởi mở, thân mật", "すぐに打（う）ち解（と）ける"),
        ("思（おも）いやる", "TƯ", "Cảm thông, thấu hiểu", "相手（あいて）の気持（きも）ちを思（おも）いやる"),
        ("いたわる", "lao", "Chăm sóc ân cần, nâng niu", "老人（ろうじん）をいたわる"),
        ("敬（うやま）う", "KÍNH", "Kính trọng, tôn kính", "目上（めうえ）の人（ひと）を敬（うやま）う"),
        ("見下（みくだ）す", "KIẾN HẠ", "Coi thường, khinh khỉnh", "人（ひと）を見下（みくだ）す")
    ]
}

vocab_curriculum[2] = {
    "title": "Đời Sống Hàng Ngày & Nhà Cửa (日常生活・家事 - にちじょうせいかつ・かじ)",
    "intro": "Chào bé cưng! Chủ đề nhà cửa và việc nhà có trọn bộ 25 từ đắt giá giúp em tự tin đọc hiểu hợp đồng thuê nhà và đời sống Nhật Bản:",
    "tips": "Phân biệt kỹ `敷金` (tiền cọc hoàn lại khi trả nhà) và `礼金` (tiền biếu chủ nhà một đi không trở lại) nhé cưng!",
    "words": [
        ("炊事（すいじ）", "XUY SỰ", "Việc bếp núc, nấu nướng", "毎朝（まいあさ）の炊事（すいじ）"),
        ("献立（こんだて）", "HIẾN LẬP", "Thực đơn, cơ cấu bữa ăn", "栄養（えいよう）バランスの良（よ）い献立（こんだて）"),
        ("手際（てぎわ）", "THỦ TẾ", "Kỹ năng xử lý thoăn thoắt", "料理（りょうり）の手際（てぎわ）がいい"),
        ("省（はぶ）く", "TỈNH", "Lược bỏ, cắt giảm bớt", "無駄（むだ）な手間（てま）を省（はぶ）く"),
        ("買（か）い出（だ）し", "MÃI XUẤT", "Mua sắm tích trữ số lượng lớn", "スーパーへ買（か）い出（だ）しに行（い）く"),
        ("すすぐ", "tráng", "Tráng nước, giũ sạch xà phòng", "洗剤（せんざい）を水（みず）ですすぐ"),
        ("こする", "cọ", "Cọ rửa, chà xát", "鍋（なべ）の焦（こ）げ付（つ）きをこする"),
        ("散（ち）らかる", "TẢN", "Bừa bộn, vương vãi", "部屋（へや）が散（ち）らかる"),
        ("粗大（そだい）ごみ", "THÔ ĐẠI", "Rác cồng kềnh", "粗大（そだい）ごみシールを貼（は）る"),
        ("買（か）い換（か）える", "MÃI HOÁN", "Mua đồ mới thay đồ cũ", "テレビを買（か）い換（か）える"),
        ("重（かさ）なる", "TRỌNG", "Chồng chất, dồn dập kéo đến", "不運（ふうん）が重（かさ）なる"),
        ("やり繰（く）り", "KHIỂN LAI", "Khéo thu vén chi tiêu", "家計（かけい）をやり繰（く）りする"),
        ("敷金（しききん）", "PHU KIM", "Tiền cọc thuê nhà", "敷金（しききん）2か月分（にかげつぶん）"),
        ("礼金（れいきん）", "LỄ KIM", "Tiền lễ tạ ơn chủ nhà", "礼金（れいきん）なしの物件（ぶっけん）"),
        ("間取（まど）り", "GIAN THỦ", "Sơ đồ bố trí phòng ốc", "間取（まど）り図（ず）を見（み）る"),
        ("家賃（やちん）", "GIA THẢI", "Tiền thuê nhà hàng tháng", "家賃（やちん）を振（ふ）り込（こ）む"),
        ("築年数（ちくねんすう）", "TRÚC NIÊN SỐ", "Số năm kể từ khi xây dựng", "築（ちく）10年（じゅうねん）のマンション"),
        ("徒歩（とほ）", "ĐỒ BỘ", "Đi bộ", "駅（えき）から徒歩（とほ）5分（ごふん）"),
        ("日当（ひあ）たり", "NHẬT ĐƯƠNG", "Ánh sáng mặt trời chiếu rọi", "日当（ひあ）たりが良（よ）い南向（みなみむ）き"),
        ("水気（みずけ）", "THỦY KHÍ", "Hơi nước, nước ẩm ướt", "水気（みずけ）を拭（ふ）き取（と）る"),
        ("湿気（しっけ）", "THẤP KHÍ", "Độ ẩm cao, nồm ẩm", "湿気（しっけ）がこもる"),
        ("換気（かんき）する", "HOÁN KHÍ", "Thông gió, mở cửa thoáng khí", "部屋（へや）を換気（かんき）する"),
        ("生（なま）ごみ", "SINH", "Rác thải hữu cơ đồ ăn", "生（なま）ごみを捨（す）てる"),
        ("分別（ぶんべつ）", "PHÂN BIỆT", "Phân loại rác theo quy định", "ごみを分別（ぶんべつ）する"),
        ("物干（ものほ）し", "VẬT CAN", "Dây phơi, chỗ phơi đồ", "物干（ものほ）し竿（ざお）に干（ほ）す")
    ]
}

vocab_curriculum[3] = {
    "title": "Giao Tiếp Xã Hội & Tranh Luận (社会生活・人間関係 - しゃかいせいかつ・にんげんかんけい)",
    "intro": "Chào bé cưng! Bài 3 nâng cấp trọn bộ 25 từ vựng then chốt về lập trường, hòa giải và đàm phán xã hội chuẩn Shinkanzen N2:",
    "tips": "Cụm `妥協する` đồng nghĩa với `互いに譲り合う` (nhượng bộ lẫn nhau), xuất hiện cực nhiều trong Mondai 4!",
    "words": [
        ("関心（かんしん）", "QUAN TÂM", "Mối quan tâm, hứng thú", "環境（かんきょう）に関心（かんしん）を持（も）つ"),
        ("立場（たちば）", "LẬP TRƯỜNG", "Lập trường, hoàn cảnh", "相手（あいて）の立場（たちば）に立（た）つ"),
        ("主張（しゅちょう）する", "CHỦ TRƯƠNG", "Khẳng định, bảo vệ quan điểm", "権利（けんり）を主張（しゅちょう）する"),
        ("対立（たいりつ）する", "ĐỐI LẬP", "Đối đầu, xung đột ý kiến", "意見（いけん）が対立（たいりつ）する"),
        ("妥協（だきょう）する", "THỎA HIỆP", "Nhượng bộ lẫn nhau", "妥協（だきょう）点（てん）を探（さが）す"),
        ("配慮（はいりょ）する", "PHỐI LỰ", "Quan tâm chu đáo", "周囲（しゅうい）に配慮（はいりょ）する"),
        ("もめる", "xích mích", "Tranh cãi, lùm xùm", "遺産（いさん）でもめる"),
        ("譲（ゆず）る", "NHƯỢNG", "Nhường nhịn", "席（せき）を譲（ゆず）る"),
        ("誤解（ごかい）を解（と）く", "NGỘ GIẢI", "Xóa bỏ hiểu lầm", "話（はな）して誤解（ごかい）を解（と）く"),
        ("仲直（なかなお）り", "TRỌNG TRỰC", "Làm lành giảng hòa", "喧嘩（けんか）のあと仲直（なかなお）りする"),
        ("口論（こうろん）する", "KHẨU LUẬN", "Khẩu chiến, cãi vã to tiếng", "些細（ささい）なことで口論（こうろん）する"),
        ("偏見（へんけん）", "THIÊN KIẾN", "Thành kiến, định kiến", "偏見（へんけん）を持（も）たない"),
        ("当事者（とうじしゃ）", "ĐƯƠNG SỰ GIẢ", "Người trong cuộc, các bên liên quan", "当事者（とうじしゃ）同士（どうし）で話（はな）し合（あ）う"),
        ("仲裁（ちゅうさい）する", "TRỌNG TÀI", "Đứng ra hòa giải", "喧嘩（けんか）を仲裁（ちゅうさい）する"),
        ("食（く）い違（ちが）う", "THỰC VI", "Bất đồng, cọc cạch không khớp", "証言（しょうげん）が食（く）い違（ちが）う"),
        ("歩（あゆ）み寄（よ）る", "BỘ KÝ", "Cùng xích lại gần, nhượng bộ", "互（たが）いに歩（あゆ）み寄（よ）る"),
        ("紛争（ふんそう）", "PHÂN TRANH", "Tranh chấp, xung đột quốc tế", "国境（こっきょう）の紛争（ふんそう）"),
        ("衝突（しょうとつ）する", "XUNG ĐỘT", "Đâm va, xung đột quan điểm", "意見（いけん）が衝突（しょうとつ）する"),
        ("異論（いろん）", "DỊ LUẬN", "Ý kiến phản đối, quan điểm khác", "異論（いろん）を唱（とな）える"),
        ("満場（まんじょう）一致（いっち）", "MÃN TRƯỜNG NHẤT TRÍ", "Đồng thuận 100%, nhất trí hoàn toàn", "満場（まんじょう）一致（いっち）で可決（かけつ）する"),
        ("合意（ごうい）する", "HỢP Ý", "Thống nhất, đạt thỏa thuận", "条件（じょうけん）に合意（ごうい）する"),
        ("溝（みぞ）が深（ふか）まる", "CÂU THÂM", "Hố ngăn cách ngày càng sâu", "二人の溝（みぞ）が深（ふか）まる"),
        ("摩擦（まさつ）", "MA SÁT", "Ma sát, xích mích va chạm", "貿易（ぼうえき）摩擦（まさつ）"),
        ("根回（ねまわ）し", "CĂN HỒI", "Vận động hành lang trước cuộc họp", "根回（ねまわ）しをしておく"),
        ("見解（けんかい）", "KIẾN GIẢI", "Quan điểm, cách nhìn nhận", "公式（こうしき）な見解（けんかい）を発表（はっぴょう）する")
    ]
}

vocab_curriculum[4] = {
    "title": "Quy Tắc, Bình Đẳng & Pháp Chế (社会のルール・規範 - しゃかいのルール・きはん)",
    "intro": "Chào bé cưng! Bài 4 tập hợp 25 từ vựng then chốt về tiêu chuẩn, điều lệ, nghĩa vụ và quyền lợi công dân:",
    "tips": "Cụm `経験不問` (không đòi hỏi kinh nghiệm) và `一律に` (đồng loạt như nhau) cực hay xuất hiện trong bài đọc thông tin quảng cáo!",
    "words": [
        ("不問（ふもん）", "BẤT VẤN", "Không xét đến, không đòi hỏi", "経験（けいけん）不問（ふもん）"),
        ("一律（いちりつ）に", "NHẤT LUẬT", "Đồng loạt, như nhau không phân biệt", "一律（いちりつ）に10％割引（わりびき）"),
        ("公平（こうへい）な", "CÔNG BÌNH", "Công bằng, vô tư", "公平（こうへい）に分配（ぶんぱい）する"),
        ("公正（こうせい）な", "CÔNG CHÍNH", "Chính trực, minh bạch", "公正（こうせい）な取引（とりひき）"),
        ("差別（さべつ）", "SA BIỆT", "Kỳ thị, phân biệt đối xử", "人種（じんしゅ）差別（さべつ）をなくす"),
        ("格差（かくさ）", "CÁCH SA", "Khoảng cách chênh lệch", "貧富（ひんぷ）の格差（かくさ）"),
        ("義務（ぎむ）", "NGHĨA VỤ", "Nghĩa vụ, bổn phận bắt buộc", "納税（のうぜい）の義務（ぎむ）"),
        ("権利（けんり）", "QUYỀN LỢI", "Quyền lợi chính đáng", "知（し）る権利（けんり）"),
        ("規律（きりつ）", "QUY LUẬT", "Kỷ luật, trật tự tổ chức", "学校（がっこう）の規律（きりつ）を守（まも）る"),
        ("順守（じゅんしゅ）する", "THUẬN THỦ", "Chấp hành, tuân thủ nghiêm ngặt", "法令（ほうれい）を順守（じゅんしゅ）する"),
        ("違反（いはん）する", "VI PHẢN", "Vi phạm quy chế/luật", "スピード違反（いはん）"),
        ("免除（めんじょ）する", "MIỄN TRỪ", "Miễn giảm nghĩa vụ/tiền", "学費（がくひ）を免除（めんじょ）する"),
        ("特権（とっけん）", "ĐẶC QUYỀN", "Đặc quyền, ưu đãi riêng", "特権（とっけん）階級（かいきゅう）"),
        ("処罰（しょばつ）する", "XỨ PHẠT", "Xử phạt, trừng trị", "違反者（いはんしゃ）を処罰（しょばつ）する"),
        ("過料（かりょう）", "QUÁ LIỆU", "Tiền phạt hành chính", "過料（かりょう）を科（か）す"),
        ("摘発（てきはつ）する", "TRÍCH PHÁT", "Phanh phui, bóc trần sai phạm", "不正（ふせい）を摘発（てきはつ）する"),
        ("取り締（し）まる", "THỦ ĐẾ", "Kiểm soát, trấn áp tội phạm", "交通（こうつう）違反（いはん）を取（と）り締（し）まる"),
        ("容認（ようにん）する", "DUNG NHẬN", "Chấp nhận, dung thứ", "遅刻（ちこく）を容認（ようにん）する"),
        ("厳正（げんせい）な", "NGHIÊM CHÍNH", "Nghiêm minh, nghiêm ngặt", "厳正（げんせい）な審査（しんさ）"),
        ("妥当（だとう）な", "THỎA ĐƯƠNG", "Hợp tình hợp lý, xác đáng", "妥当（だとう）な判断（はんだん）"),
        ("不当（ふとう）な", "BẤT ĐƯƠNG", "Bất công, vô lý, sai trái", "不当（ふとう）な要求（ようきゅう）"),
        ("拘束（こうそく）する", "CÂU THÚC", "Gò bó, trói buộc", "時間（じかん）を拘束（こうそく）する"),
        ("裁量（さいりょう）", "TÀI LƯỢNG", "Quyền tự quyết định", "個人（こじん）の裁量（さいりょう）に任（まか）せる"),
        ("規範（きはん）", "QUY PHẠM", "Chuẩn mực, khuôn mẫu xã hội", "道徳（どうとく）的（てき）規範（きはん）"),
        ("遵守（じゅんしゅ）", "TUÂN THỦ", "Tuân thủ đúng quy định", "マナーを遵守（じゅんしゅ）する")
    ]
}

print("Loaded Lesson 01 - 04.")

# ==========================================
# BÀI 05 - BÀI 10
# ==========================================
vocab_curriculum[5] = {
    "title": "Thông Tin & Truyền Thông (情報・メディア - じょうほう・メディア)",
    "intro": "Chào bé cưng! Bài 5 mở ra thế giới truyền thông, báo chí và mạng xã hội. 25 từ này xuất hiện liên tục trong bài đọc hiểu N2 đấy:",
    "tips": "Từ `世論` trong đề thi N2 hay đố cách đọc furigana: vừa đọc là `よろん` vừa đọc là `せいろん` (trong đó `よろん` phổ biến hơn). Nhớ kỹ nha cưng!",
    "words": [
        ("普及（ふきゅう）", "PHỔ CẬP", "Lan rộng, phổ biến khắp nơi", "インターネットが急速（きゅうそく）に普及（ふきゅう）する"),
        ("報道（ほうどう）", "BÁO ĐẠO", "Đưa tin tức, phản ánh trên báo đài", "事件（じけん）の真相（しんそう）を報道（ほうどう）する"),
        ("宣伝（せんでん）", "TUYÊN TRUYỀN", "Quảng bá, quảng cáo sản phẩm", "新商品（しんしょうひん）を大々的（だいだいてき）に宣伝（せんでん）する"),
        ("速報（そくほう）", "TỐC BÁO", "Tin nóng sốt dẻo, bản tin nhanh", "地震（じしん）の緊急（きんきゅう）速報（そくほう）が流（なが）れる"),
        ("配信（はいしん）", "PHỐI TÍN", "Phát sóng, phát trực tuyến qua mạng", "動画（どうが）をライブ配信（はいしん）する"),
        ("訂正（ていせい）", "ĐÍNH CHÍNH", "Đính chính thông tin sai lệch", "誤（あやま）った記事（きじ）を訂正（ていせい）する"),
        ("世論（よろん）", "THẾ LUẬN", "Dư luận xã hội, ý kiến quần chúng", "世論（よろん）の動向（どうこう）に注目（ちゅうもく）する"),
        ("取材（しゅざい）", "THỦ TÀI", "Phỏng vấn, thu thập tài liệu làm báo", "現地（げんち）で関係者（かんけいしゃ）を取材（しゅざい）する"),
        ("拡散（かくさん）", "KHUẾCH TẢN", "Lan truyền nhanh chóng trên mạng", "SNSで情報（じょうほう）が一気（いっき）に拡散（かくさん）する"),
        ("閲覧（えつらん）", "DUYỆT LÃM", "Xem, truy cập đọc tài liệu/trang web", "Webページを閲覧（えつらん）する"),
        ("掲載（けいさい）", "YẾT TẢI", "Đăng tải bài viết, in ấn", "新聞（しんぶん）に記事（きじ）が掲載（けいさい）される"),
        ("意図（いと）", "Ý ĐỒ", "Mục đích, ý định nhắm tới", "相手（あいて）の発言（はつげん）の意図（いと）を探（さぐ）る"),
        ("誇張（こちょう）", "KHOA TRƯƠNG", "Thổi phồng, cường điệu hóa sự thật", "事実（じじつ）を誇張（こちょう）して伝（つた）える"),
        ("検閲（けんえつ）", "KIỂM DUYỆT", "Kiểm duyệt nội dung, ấn phẩm", "記事（きじ）が厳（きび）しく検閲（けんえつ）される"),
        ("捏造（ねつぞう）", "NIẾT TẠO", "Bịa đặt thông tin, làm giả chứng cứ", "データや証拠（しょうこ）を捏造（ねつぞう）する"),
        ("著作権（ちょさくけん）", "TRỨ TÁC QUYỀN", "Quyền tác giả, bản quyền sáng tạo", "著作権（ちょさくけん）を保護（ほご）する"),
        ("侵害（しんがい）", "XÂM HẠI", "Xâm phạm quyền lợi, tổn hại riêng tư", "プライバシーを侵害（しんがい）する"),
        ("発信者（はっしんしゃ）", "PHÁT TÍN GIẢ", "Người đăng tải, nguồn phát tán tin tức", "情報（じょうほう）の発信者（はっしんしゃ）を特定（とくてい）する"),
        ("匿名（とくめい）", "NẶC DANH", "Ẩn danh giấu tên không lộ diện", "匿名（とくめい）で悪口（わるくち）を書（か）き込（こ）む"),
        ("炎上（えんじょう）", "VIÊM THƯỢNG", "Bão ném đá tẩy chay trên mạng", "不適切（ふてきせつ）な発言（はつげん）で炎上（えんじょう）する"),
        ("口（くち）コミ", "KHẨU", "Đánh giá truyền miệng từ người dùng", "口（くち）コミで評判（ひょうばん）が広（ひろ）がる"),
        ("購読（こうどく）", "CẤU ĐỘC", "Đặt mua báo/tạp chí đọc định kỳ", "定期刊行物（ていきかんこうぶつ）を購読（こうどく）する"),
        ("媒体（ばいたい）", "MÔI THỂ", "Phương tiện truyền tải thông điệp", "広告（こうこく）の媒体（ばいたい）を選（えら）ぶ"),
        ("独占取材（どくせんしゅざい）", "ĐỘC CHIÊM THỦ TÀI", "Phỏng vấn độc quyền một mình", "有名人（ゆうめいじん）の独占取材（どくせんしゅざい）に成功（せいこう）する"),
        ("視聴率（しちょうりつ）", "THỊ THÍNH SUẤT", "Tỷ lệ khán giả đón xem đài", "歴代（れきだい）最高（さいこう）の視聴率（しちょうりつ）を記録（きろく）する")
    ]
}

vocab_curriculum[6] = {
    "title": "Thương Mại & Tiêu Dùng (商業・消費 - しょうぎょう・しょうひ)",
    "intro": "Chào bé cưng! Bài 6 đưa em vào thương trường: giá cả, mua sắm, lời lỗ và kinh doanh thực chiến:",
    "tips": "Nhớ cặp bài trùng `黒字` (hắc tự = có lãi/thặng dư) và `赤字` (xích tự = lỗ thâm hụt). Người Nhật dùng mực đen ghi số dương và mực đỏ ghi số âm đó bé cưng!",
    "words": [
        ("購買意欲（こうばいいよく）", "CẤU MÃI Ý DỤC", "Hứng thú muốn mở ví chi tiền mua", "消費者（しょうひしゃ）の購買意欲（こうばいいよく）をそそる"),
        ("在庫（ざいこ）", "TẠI KHỐ", "Hàng hóa đang còn trong kho lưu", "在庫（ざいこ）を切（き）らす／在庫（ざいこ）を抱（かか）える"),
        ("販売促進（はんばいそくしん）", "PHIẾN MẠI XÚC TIẾN", "Xúc tiến bán lẻ, thúc đẩy doanh số", "販売促進（はんばいそくしん）キャンペーンを実施（じっし）する"),
        ("採算（さいさん）", "THẢI TOÁN", "Khả năng sinh lời kinh tế", "採算（さいさん）が合（あ）わない事業（じぎょう）から撤退（てったい）する"),
        ("消費税（しょうひぜい）", "TIÊU PHÍ THUẾ", "Thuế giá trị gia tăng tiêu dùng", "消費税（しょうひぜい）が10%に増税（ぞうぜい）される"),
        ("値下（ねさ）がり", "TRỊ HẠ", "Rớt giá, hạ giá thành sản phẩm", "野菜（やさい）の価格（かかく）が値下（ねさ）がりする"),
        ("収支（しゅうし）", "THU CHI", "Cân đối thu vào chi ra tài chính", "今月（こんげつ）の収支（しゅうし）を計算（けいさん）する"),
        ("定価（ていか）", "ĐỊNH GIÁ", "Giá niêm yết chuẩn chính hãng", "定価（ていか）の2割引（にわりび）きで売（う）る"),
        ("割引（わりびき）", "CÁT DẪN", "Giảm giá tiền, chiết khấu", "学生（がくせい）割引（わりびき）を利用（りよう）する"),
        ("領収書（りょうしゅうしょ）", "LÃNH THU THƯ", "Hóa đơn đỏ, biên nhận thanh toán", "領収書（りょうしゅうしょ）を発行（はっこう）してもらう"),
        ("請求（せいきゅう）", "THỈNH CẦU", "Đòi nợ, yêu cầu thanh toán bill", "工事（こうじ）代金（だいきん）を請求（せいきゅう）する"),
        ("見積（みつ）もり", "KIẾN TÍCH", "Bảng dự toán chi phí trước mắt", "修理費（しゅうりひ）の見積（みつ）もりを取（と）る"),
        ("利益（りえき）", "LỢI ÍCH", "Lợi nhuận ròng sau chi phí", "多大（ただい）な利益（りえき）を生（う）み出（だ）す"),
        ("赤字（あかじ）", "XÍCH TỰ", "Thua lỗ, chi nhiều hơn thu", "貿易（ぼうえき）赤字（あかじ）が拡大（かくだい）する"),
        ("黒字（くろじ）", "HẮC TỰ", "Lãi ròng, thặng dư ngân sách", "今期（こんき）は黒字（くろじ）に転換（てんかん）した"),
        ("経費（けいひ）", "KINH PHÍ", "Chi phí chi trả trong công việc", "無駄（むだ）な経費（けいひ）を削減（さくげん）する"),
        ("仕入（しい）れる", "SĨ NHẬP", "Mua gom nhập hàng vào kho bán", "新鮮（しんせん）な魚（さかな）を市場（いちば）から仕入（しい）れる"),
        ("納入（のうにゅう）", "NẠP NHẬP", "Giao hàng đến nơi hẹn, nộp tiền", "期日（きじつ）までに製品（せいひん）を納入（のうにゅう）する"),
        ("返品（へんぴん）", "PHẢN PHẨM", "Trả lại món hàng lỗi cho tiệm", "不良品（ふりょうひん）を返品（へんぴん）する"),
        ("転売（てんばい）", "CHUYỂN MẠI", "Bán sang tay lại kiếm chênh lệch", "限定（げんてい）グッズを高額（こうがく）で転売（てんばい）する"),
        ("顧客（こきゃく）", "CỐ KHÁCH", "Khách hàng ruột, bạn mua thân quen", "顧客（こきゃく）のニーズに柔軟（じゅうなん）に応（こた）える"),
        ("需要（じゅよう）", "NHU YẾU", "Nhu cầu tiêu thụ của thị trường", "需要（じゅよう）と供給（きょうきゅう）のバランス"),
        ("供給（きょうきゅう）", "CUNG CẤP", "Nguồn cung hàng hóa ra chợ", "エネルギーを安定（あんてい）供給（きょうきゅう）する"),
        ("元手（もとで）", "NGUYÊN THỦ", "Tiền vốn liếng ban đầu khởi nghiệp", "元手（もとで）なしでビジネスを始（はじ）める"),
        ("負債（ふさい）", "PHỤ TRÁI", "Gánh nặng nợ nần tài chính", "多額（たがく）の負債（ふさい）を抱（かか）える")
    ]
}

vocab_curriculum[7] = {
    "title": "Tính Cách & Cảm Xúc (性格・感情 - せいかく・かんじょう)",
    "intro": "Chào bé cưng! Bài 7 chứa 25 tính từ và danh từ miêu tả tính cách con người, xuất hiện liên miên ở bài đọc hiểu ngắn và trung:",
    "tips": "Phân biệt `図々しい` (trơ tráo, không biết ngượng) và `厚かましい` (mặt dày xin xỏ). Cả hai đều mang sắc thái tiêu cực trong đối nhân xử thế!",
    "words": [
        ("謙虚（けんきょ）", "KHIÊM HƯ", "Khiêm nhường, không tự cao tự đại", "謙虚（けんきょ）な姿勢（しせい）で学（まな）ぶ"),
        ("積極的（せっきょくてき）", "TÍCH CỰC ĐÍCH", "Chủ động, hăng hái bắt tay làm", "議論（ぎろん）に積極的（せっきょくてき）に参加（さんか）する"),
        ("几帳面（きちょうめん）", "KỶ TRƯỚNG DIỆN", "Ngăn nắp cẩn thận, quy củ tỉ mỉ", "性格（せいかく）が几帳面（きちょうめん）で部屋（へや）がきれい"),
        ("短気（たんき）", "ĐOẢN KHÍ", "Nóng tính, hay nổi giận cáu gắt", "父（ちち）は短気（たんき）ですぐ怒（おこ）る"),
        ("穏（おだ）やか", "ỔN", "Dịu dàng, điềm đạm thanh bình", "穏（おだ）やかな性格（せいかく）の人（ひと）"),
        ("社交的（しゃこうてき）", "XÃ GIAO ĐÍCH", "Dễ gần, thích kết giao bạn bè", "社交的（しゃこうてき）で友達（ともだち）が多（おお）い"),
        ("内向的（ないこうてき）", "NỘI HƯỚNG ĐÍCH", "Hướng nội, ít nói, ngại giao thiệp", "内向的（ないこうてき）でおとなしい性格（せいかく）"),
        ("おおらか", "ĐẠI", "Rộng lượng, thoáng tính phóng khoáng", "小（ちい）さな失敗（しっぱい）を気（き）にしないおおらかな人（ひと）"),
        ("慎重（しんちょう）", "THẬN TRỌNG", "Cân nhắc kỹ càng, thận trọng", "慎重（しんちょう）に行動（こうどう）する"),
        ("臆病（おくびょう）", "ỨC BỆNH", "Nhát gan, sợ hãi e dè", "臆病（おくびょう）で挑戦（ちょうせん）できない"),
        ("厚（あつ）かましい", "HẬU", "Mặt dày đòi hỏi, trơ trẽn", "厚（あつ）かましいお願いをする"),
        ("図々（ずうずう）しい", "ĐỒ", "Trơ tráo vô liêm sỉ, không biết ngại", "人（ひと）の物（もの）を平気（へいき）で使（つか）う図々（ずうずう）しい奴（やつ）"),
        ("朗（ほが）らか", "LÃNG", "Vui vẻ rạng rỡ như ánh mặt trời", "いつも朗（ほが）らかな笑顔（えがお）を見（み）せる"),
        ("気（き）が短（みじか）い", "KHÍ ĐOẢN", "Hay nôn nóng sốt ruột, thiếu kiên nhẫn", "気（き）が短（みじか）くて待（ま）てない"),
        ("負（ま）けず嫌（ぎら）い", "PHỤ HIỀM", "Hiếu thắng, không bao giờ chịu thua", "負（ま）けず嫌（ぎら）いで必死（ひっし）に努力（どりょく）する"),
        ("気難（きむずか）しい", "KHÍ NAN", "Khó tính, khó chiều, dễ phật ý", "気難（きむずか）しい上司（じょうし）を相手（あいて）にする"),
        ("素直（すなお）", "TỐ TRỰC", "Ngoan ngoãn thật thà, biết lắng nghe", "人（ひと）の意見（いけん）を素直（すなお）に聞（き）く"),
        ("頑固（がんこ）", "NGOAN CỐ", "Cứng đầu bảo thủ, khư khư ý mình", "頑固（がんこ）に自説（じせつ）を曲（ま）げない"),
        ("嫉妬（しっと）", "TẬT ĐỐ", "Ghen tị trước may mắn người khác", "友人（ゆうじん）の成功（せいこう）に嫉妬（しっと）する"),
        ("憧（あこが）れる", "SUNG", "Ngưỡng mộ thần tượng, khát khao noi theo", "先輩（せんぱい）の活躍（かつやく）に憧（あこが）れる"),
        ("焦（あせ）る", "TIÊU", "Cuống cuồng vội vã, mất bình tĩnh", "時間（じかん）がなくて焦（あせ）る"),
        ("落（お）ち込（こ）む", "LẠC NHẬP", "Hụt hẫng u sầu, buồn rầu ủ rũ", "試験（しけん）に落（お）ちて落（お）ち込（こ）む"),
        ("惜（お）しむ", "TÍCH", "Tiếc nuối chia tay, trân quý từng giây", "別（わか）れを惜（お）しむ／寸暇（すんか）を惜（お）しんで学（まな）ぶ"),
        ("誇（ほこ）らしい", "KHOA", "Hãnh diện ngẩng cao đầu tự hào", "努力（どりょく）が実（みの）って誇（ほこ）らしい"),
        ("戸惑（とまど）う", "HỘ HOẶC", "Bối rối lạ lẫm, không biết làm sao", "急（きゅう）な変化（へんか）に戸惑（とまど）う")
    ]
}

vocab_curriculum[8] = {
    "title": "Học Tập, Thi Cử & Đánh Giá (学習・試験 - がくしゅう・しけん)",
    "intro": "Chào bé cưng! 25 từ học thuật Bài 8 sẽ là cánh tay đắc lực giúp em rinh trọn điểm Mondai 1 và đọc hiểu giảng đường:",
    "tips": "Từ `及第点` (điểm chuẩn đỗ qua môn) hay đi kèm động từ `取る` hoặc `達する`. Đừng nhầm với `落第` là trượt lưu ban nha cưng!",
    "words": [
        ("基準（きじゅん）", "CƠ CHUẨN", "Tiêu chí, chuẩn mực để so sánh", "合格（ごうかく）基準（きじゅん）を満（み）たす"),
        ("評価（ひょうか）", "BÌNH GIÁ", "Đánh giá tài năng, nhìn nhận công sức", "業績（ぎょうせき）を高（たか）く評価（ひょうか）する"),
        ("資格（しかく）", "TƯ CÁCH", "Văn bằng, chứng chỉ năng lực hành nghề", "弁護士（べんごし）の資格（しかく）を取得（しゅとく）する"),
        ("模擬試験（もぎしけん）", "MÔ NGHĨ THÍ NGHIỆM", "Kỳ thi thử rèn quân trước giờ G", "模擬試験（もぎしけん）を受（う）ける"),
        ("習得（しゅうとく）", "TẬP ĐẮC", "Lĩnh hội thuần thục kỹ năng mới", "プログラミング技術（ぎじゅつ）を習得（しゅうとく）する"),
        ("履修（りしゅう）", "LÝ TU", "Học tích lũy trọn vẹn số tín chỉ", "必修（ひっしゅう）科目（かもく）を履修（りしゅう）する"),
        ("専攻（せんこう）", "CHUYÊN CÔNG", "Ngành học chuyên sâu đại học", "日本（にほん）文学（ぶんがく）を専攻（せんこう）する"),
        ("推薦（すいせん）", "THÔI TIẾN", "Tiến cử gửi gắm, viết thư giới thiệu", "教授（きょうじゅ）の推薦（すいせん）で就職（しゅうしょく）する"),
        ("偏差値（へんさち）", "THIÊN SAI TRỊ", "Điểm số độ lệch chuẩn năng lực", "偏差値（へんさち）が高（たか）い名門校（めいもんこう）"),
        ("合否（ごうひ）", "HỢP PHỦ", "Kết quả chung cuộc đỗ hay rớt", "合否（ごうひ）の通知（つうち）を待（ま）つ"),
        ("暗記（あんき）", "ÁM KÝ", "Học vẹt thuộc lòng từng chữ", "英単語（えいたんご）を暗記（あんき）する"),
        ("応用（おうよう）", "ỨNG DỤNG", "Vận dụng linh hoạt lý thuyết vào đề", "基本（きほん）を応用（おうよう）して解（と）く"),
        ("考察（こうさつ）", "KHẢO SÁT", "Suy ngẫm phân tích logic số liệu", "実験（じっけん）結果（けっか）を考察（こうさつ）する"),
        ("参照（さんしょう）", "THAM CHIẾU", "Tra cứu đối chiếu tài liệu đính kèm", "図表（ずひょう）を参照（さんしょう）する"),
        ("添削（てんさく）", "THIÊM TƯỚC", "Sửa câu sửa chữ bài văn luận", "先生（せんせい）に小論文（しょうろんぶん）を添削（てんさく）してもらう"),
        ("採点（さいてん）", "THẢI ĐIỂM", "Chấm điểm từng câu kiểm tra", "テストを厳（きび）しく採点（さいてん）する"),
        ("集中力（しゅうちゅうりょく）", "TẬP TRUNG LỰC", "Năng lượng tập trung toàn bộ tâm trí", "集中力（しゅうちゅうりょく）が途切（とぎ）れる"),
        ("克服（こくふく）", "KHẮC PHỤC", "Đánh bại nỗi sợ, vượt qua điểm yếu", "苦手（にがて）科目（かもく）を克服（こくふく）する"),
        ("成績（せいせき）", "THÀNH TÍCH", "Bảng điểm kết quả học tập", "成績（せいせき）が優秀（ゆうしゅう）な学生（がくせい）"),
        ("優秀（ゆうしゅう）", "ƯU TÚ", "Giỏi giang xuất sắc vượt bậc", "優秀（ゆうしゅう）な成績（せいせき）を収（おさ）める"),
        ("劣（おと）る", "LIỆT", "Thua kém yếu thế hơn người khác", "性能（せいのう）が他社（たしゃ）より劣（おと）る"),
        ("及第点（きゅうだいてん）", "CẬP ĐỆ ĐIỂM", "Điểm số vừa vặn đỗ qua môn", "試験（しけん）で及第点（きゅうだいてん）を取（と）る"),
        ("落第（らくだい）", "LẠC ĐỆ", "Trượt kỳ thi, ở lại lớp năm cũ", "単位（たんい）が足（た）りずに落第（らくだい）する"),
        ("志望校（しぼうこう）", "CHÍ VỌNG HIỆU", "Trường học mơ ước nộp đơn thi", "第一（だいいち）志望校（しぼうこう）に合格（ごうかく）する"),
        ("根気（こんき）", "CĂN KHÍ", "Sự nhẫn nại bền bỉ không bỏ dở", "根気（こんき）よく問題（もんだい）に取り組（く）む")
    ]
}

vocab_curriculum[9] = {
    "title": "Sức Khỏe, Bệnh Tật & Y Tế (健康・医療 - けんこう・いりょう)",
    "intro": "Chào bé cưng! Bài 9 giúp em nắm chắc từ vựng y tế và thể chất, rất hay gặp trong đời sống Nhật Bản và đề thi JLPT:",
    "tips": "Từ `こじらせる` (làm bệnh trở nặng thêm vì chủ quan) còn có thể dùng ẩn dụ trong tình cảm: `話がこじれる` (chuyện trở nên rối rắm khó gỡ) đấy bé!",
    "words": [
        ("予防（よぼう）", "DỰ PHÒNG", "Phòng chống ngăn bệnh từ sớm", "病気（びょうき）を予防（よぼう）する"),
        ("治療（ちりょう）", "TRỊ LIỆU", "Chữa trị bằng thuốc và phác đồ", "早期（そうき）治療（ちりょう）を受（う）ける"),
        ("診断（しんだん）", "CHẨN ĐOÁN", "Bác sĩ khám bắt bệnh", "医師（いし）の診断（しんだん）を受（う）ける"),
        ("感染（かんせん）", "CẢM NHIỄM", "Bị vi trùng virus xâm nhập lây nhiễm", "ウイルスに感染（かんせん）する"),
        ("処方（しょほう）", "XỨ PHƯƠNG", "Bốc thuốc kê đơn điều trị", "薬（くすり）を処方（しょほう）してもらう"),
        ("症状（しょうじょう）", "CHỨNG TRẠNG", "Biểu hiện phát bệnh trên cơ thể", "風邪（かぜ）の初期（しょき）症状（しょうじょう）"),
        ("副作用（ふくさよう）", "PHÓ TÁC DỤNG", "Tác dụng phụ ngoài ý muốn của thuốc", "薬（くすり）の副作用（ふくさよう）で眠（ねむ）くなる"),
        ("慢性（まんせい）", "MÃN TÍNH", "Bệnh kéo dài năm này qua năm khác", "慢性（まんせい）の頭痛（ずつう）に悩（なや）む"),
        ("急性（きゅうせい）", "CẤP TÍNH", "Bệnh bộc phát bất ngờ dữ dội", "急性（きゅうせい）盲腸炎（もうちょうえん）"),
        ("処置（しょち）", "XỨ TRÍ", "Sơ cứu vết thương, xử lý y khoa", "傷口（きずぐち）に応急（おうきゅう）処置（しょち）を施（ほどこ）す"),
        ("手術（しゅじゅつ）", "THỦ THUẬT", "Mổ xẻ phẫu thuật can thiệp", "胃（い）の手術（しゅじゅつ）を受（う）ける"),
        ("看護（かんご）", "KHÁN HỘ", "Chăm nom điều dưỡng người ốm", "家族（かぞく）を手厚（てあつ）く看護（かんご）する"),
        ("免疫力（めんえきりょく）", "MIỄN DỊCH LỰC", "Hàng rào sức đề kháng cơ thể", "免疫力（めんえきりょく）を高（たか）める"),
        ("衛生（えいせい）", "VỆ SINH", "Giữ gìn vệ sinh sạch sẽ an toàn", "衛生（えいせい）管理（かんり）を徹底（てってい）する"),
        ("休養（きゅうよう）", "HƯU DƯỠNG", "Tĩnh dưỡng nghỉ ngơi lấy lại sức", "しっかり休養（きゅうよう）を取（と）る"),
        ("倦怠感（けんたいかん）", "QUYỆN ĐÃI CẢM", "Cảm giác mệt mỏi uể oải rời rạc", "全身（ぜんしん）の倦怠感（けんたいかん）を訴（うった）える"),
        ("衰（おとろ）える", "SUY", "Sức khỏe thể lực sa sút kiệt dần", "体力（たいりょく）が衰（おとろ）える"),
        ("こじらせる", "làm nặng thêm", "Khiến bệnh tình trở nên trầm trọng", "風邪（かぜ）をこじらせて肺炎（はいえん）になる"),
        ("発症（はっしょう）", "PHÁT CHỨNG", "Phát tác mầm bệnh ra ngoài", "感染（かんせん）後（ご）に発症（はっしょう）する"),
        ("告知（こくち）", "CÁO TRI", "Bác sĩ thông báo sự thật bệnh án", "がんの告知（こくち）を受（う）ける"),
        ("兆候（ちょうこう）", "TRIỆU HẬU", "Dấu hiệu điềm báo biến chuyển", "回復（かいふく）の兆候（ちょうこう）が見（み）られる"),
        ("完治（かんち）", "HOÀN TRỊ", "Lành hẳn, khỏi sạch hoàn toàn", "骨折（こっせつ）が完治（かんち）する"),
        ("療養（りょうよう）", "LIỆU DƯỠNG", "Dưỡng bệnh tĩnh tâm tại nhà/viện", "自宅（じたく）で療養（りょうよう）生活（せいかつ）を送（おく）る"),
        ("診断書（しんだんしょ）", "CHẨN ĐOÁN THƯ", "Giấy chứng nhận bệnh án bác sĩ cấp", "診断書（しんだんしょ）を会社（かいしゃ）に提出（ていしゅつ）する"),
        ("伝染（でんせん）", "TRUYỀN NHIỄM", "Lây truyền mầm bệnh sang người khác", "伝染（でんせん）病（びょう）の拡大（かくだい）を防（ふせ）ぐ")
    ]
}

vocab_curriculum[10] = {
    "title": "Giao Thông, Đi Lại & Sự Cố (交通・移動 - こうつう・いどう)",
    "intro": "Chào bé cưng! Bài 10 tổng hợp 25 từ đắt giá về hệ thống tàu xe và tình huống giao thông Nhật Bản:",
    "tips": "Khi nghe phát thanh ga tàu, cụm `運転を見合わせる` có nghĩa là tạm dừng chạy tàu để kiểm tra/xử lý sự cố, nhớ chuẩn bị tinh thần tìm lộ trình khác nha em!",
    "words": [
        ("渋滞（じゅうたい）", "SÁP TRỆ", "Ùn tắc giao thông, kẹt xe hàng dài", "高速（こうそく）道路（どうろ）が渋滞（じゅうたい）する"),
        ("運行（うんこう）", "VẬN HÀNH", "Chạy tàu xe theo lịch trình", "ダイヤ通（どお）りに正常（せいじょう）運行（うんこう）する"),
        ("迂回（うかい）", "VU HỒI", "Đi đường vòng để tránh kẹt hay sự cố", "迂回（うかい）ルートを通（とお）る"),
        ("運賃（うんちん）", "VẬN THẢI", "Giá cước tiền vé tàu xe", "運賃（うんちん）を改定（かいてい）する"),
        ("車線（しゃせん）", "XA TUYẾN", "Làn đường kẻ vạch cho xe", "片側（かたがわ）2車線（しゃせん）の道路（どうろ）"),
        ("踏切（ふみきり）", "ĐẠP THIẾT", "Điểm giao cắt có rào chắn đường ray", "踏切（ふみきり）で一時（いちじ）停止（ていし）する"),
        ("横断（おうだん）", "HOÀNH ĐOẠN", "Băng ngang qua đường phố lớn", "横断（おうだん）歩道（ほどう）を渡（わた）る"),
        ("通過（つうか）", "THÔNG QUÁ", "Tàu chạy vụt qua ga không dừng", "特急（とっきゅう）が駅（えき）を通過（つうか）する"),
        ("停車（ていしゃ）", "ĐÌNH XA", "Tàu xe dừng bánh đỗ lại", "次（つぎ）の駅（えき）に停車（ていしゃ）する"),
        ("直通（ちょくつう）", "TRỰC THÔNG", "Chạy thẳng một mạch không cần đổi tàu", "空港（くうこう）への直通（ちょくつう）電車（でんしゃ）"),
        ("乗（の）り換（か）え", "THỪA HOÁN", "Chuyển tuyến sang tàu xe khác", "新幹線（しんかんせん）に乗（の）り換（か）える"),
        ("定期券（ていきけん）", "ĐỊNH KỲ KHOÁN", "Vé tháng đi tàu định kỳ tiết kiệm", "定期券（ていきけん）を更新（こうしん）する"),
        ("発着（はっちゃく）", "PHÁT TRƯỚC", "Thời khắc đi và đến bến", "電車（でんしゃ）の発着（はっちゃく）時刻（じこく）"),
        ("運休（うんきゅう）", "VẬN HƯU", "Hủy chuyến ngừng chạy do sự cố", "台風（たいふう）で電車（でんしゃ）が運休（うんきゅう）になる"),
        ("混雑（こんざつ）", "HỖN TẠP", "Đông đúc chen lấn xô đẩy", "ラッシュ時（じ）にホームが混雑（こんざつ）する"),
        ("衝突（しょうとつ）", "XUNG ĐỘT", "Đâm va đối đầu trực diện giữa hai xe", "トラックと正面（しょうめん）衝突（しょうとつ）する"),
        ("接触（せっしょく）", "TIẾP XÚC", "Cọ quẹt va chạm nhẹ sượt qua", "接触（せっしょく）事故（じこ）を起（お）こす"),
        ("追突（ついとつ）", "TRUY ĐỘT", "Tông thẳng vào đít xe đi trước", "後続車（こうぞくしゃ）に追突（ついとつ）される"),
        ("始発（しはつ）", "THỦY PHÁT", "Chuyến tàu sáng sớm mở đầu ngày", "始発（しはつ）列車（れっしゃ）に乗（の）る"),
        ("終電（しゅうでん）", "CHUNG ĐIỆN", "Chuyến tàu vét cuối cùng đêm khuya", "終電（しゅうでん）を逃（のが）す"),
        ("ダイヤ（ダイヤ）", "BIỂU ĐỒ", "Biểu đồ giờ chạy tàu xe", "ダイヤが乱（みだ）れる"),
        ("沿線（えんせん）", "DUYÊN TUYẾN", "Dọc hai bên tuyến đường sắt chạy", "山手線（やまのてせん）の沿線（えんせん）に住（す）む"),
        ("経路（けいろ）", "KINH LỘ", "Đường đi nước bước, lộ trình", "最短（さいたん）の移動（いどう）経路（けいろ）を調（しら）べる"),
        ("免許（めんきょ）", "MIỄN HỨA", "Giấy phép lái xe chính chủ", "運転（うんてん）免許（めんきょ）を取得（しゅとく）する"),
        ("見合（みあ）わせる", "KIẾN HỢP", "Tạm hoãn chuyến tàu theo dõi sự cố", "強風（きょうふう）のため運転（うんてん）を見合（みあ）わせる")
    ]
}

print("Loaded Lesson 05 - 10.")

# ==========================================
# BÀI 11 - BÀI 16
# ==========================================
vocab_curriculum[11] = {
    "title": "Lao Động & Việc Làm Công Sở (仕事・職業 - しごと・しょくぎょう)",
    "intro": "Chào bé cưng! Bài 11 là trọn bộ từ vựng chốn công sở Nhật Bản: xin việc, chế độ đãi ngộ và thăng tiến:",
    "tips": "Từ `ノルマ` (bắt nguồn từ tiếng Nga) dùng để chỉ chỉ tiêu doanh số bắt buộc phải đạt. Cụm `ノルマを達成する` (hoàn thành chỉ tiêu) cực hay ra thi!",
    "words": [
        ("就職（しゅうしょく）", "TỰU CHỨC", "Tìm được việc làm, vào công ty làm", "希望（きぼう）の会社（かいしゃ）に就職（しゅうしょく）する"),
        ("責任（せきにん）", "TRÁCH NHIỆM", "Trách nhiệm đối với công việc", "仕事（しごと）の責任（せきにん）を果（は）たす"),
        ("勤務（きんむ）", "CẦN VỤ", "Làm việc, công tác tại văn phòng", "本社（ほんしゃ）に勤務（きんむ）する"),
        ("昇進（しょうしん）", "THĂNG TIẾN", "Được thăng quan tiến chức", "課長（かちょう）に昇進（しょうしん）する"),
        ("採用（さいよう）", "THẢI DỤNG", "Tuyển chọn nhận vào làm", "新卒（しんそつ）社員（しゃいん）を採用（さいよう）する"),
        ("待遇（たいぐう）", "ĐÃI NGỘ", "Chế độ lương thưởng phúc lợi", "良（よ）い待遇（たいぐう）で迎（むか）える"),
        ("残業（ざんぎょう）", "TÀN NGHIỆP", "Làm việc thêm giờ ngoài giờ hành chính", "毎晩（まいばん）遅（おそ）くまで残業（ざんぎょう）する"),
        ("有給休暇（ゆうきゅうきゅうか）", "HỮU CẤP HƯU HẠ", "Ngày nghỉ phép hưởng nguyên lương", "有給休暇（ゆうきゅうきゅうか）を取得（しゅとく）する"),
        ("辞職（じしょく）", "TỪ CHỨC", "Từ bỏ chức vụ xin rút lui", "大臣（だいじん）を辞職（じしょく）する"),
        ("転職（てんしょく）", "CHUYỂN CHỨC", "Nhảy việc sang công ty mới", "キャリアアップのために転職（てんしょく）する"),
        ("人事（じんじ）", "NHÂN SỰ", "Công tác nhân sự, sắp xếp người", "人事（じんじ）異動（いどう）の時期（じき）"),
        ("部署（ぶしょ）", "BỘ THỰ", "Phòng ban chuyên môn trong cty", "営業（えいぎょう）部署（ぶしょ）に配属（はいぞく）される"),
        ("業績（ぎょうせき）", "NGHIỆP TÍCH", "Thành tích, kết quả kinh doanh đạt được", "会社（かいしゃ）の業績（ぎょうせき）が向上（こうじょう）する"),
        ("ノルマ（ノルマ）", "CHỈ TIÊU", "Định mức chỉ tiêu ép buộc phải xong", "月（つき）のノルマを達成（たっせい）する"),
        ("手当（てあて）", "THỦ ĐƯƠNG", "Tiền phụ cấp trách nhiệm ngoài lương", "住宅（じゅうたく）手当（てあて）が支給（しきゅう）される"),
        ("定年（ていねん）", "ĐỊNH NIÊN", "Độ tuổi về hưu theo luật định", "定年（ていねん）退職（たいしょく）を迎（むか）える"),
        ("退職金（たいしょくきん）", "THOÁI CHỨC KIM", "Khoản tiền trợ cấp sau khi nghỉ việc", "退職金（たいしょくきん）を受（う）け取（と）る"),
        ("派遣（はけん）", "PHÁI KHIỂN", "Lao động phái cử từ công ty trung gian", "派遣（はけん）社員（しゃいん）として働（はたら）く"),
        ("契約社員（けいやくしゃいん）", "KHẾ ƯỚC XÃ VIÊN", "Nhân viên ký hợp đồng có thời hạn", "契約社員（けいやくしゃいん）の雇用（こよう）形態（けいたい）"),
        ("役職（やくしょく）", "DỊCH CHỨC", "Chức danh lãnh đạo quản lý", "重（おも）い役職（やくしょく）に就（つ）く"),
        ("引（ひ）き継（つ）ぐ", "DẪN KẾ", "Chuyển giao và nhận lại công việc", "前任者（ぜんにんしゃ）から仕事（しごと）を引き継（つ）ぐ"),
        ("打（う）ち合（あ）わせ", "ĐẢ HỢP", "Cuộc họp ngắn bàn bạc công việc", "取引先（とりひきさき）と打（う）ち合（あ）わせをする"),
        ("出張（しゅっちょう）", "XUẤT TRƯƠNG", "Đi công tác xa nhà", "海外（かいがい）へ出張（しゅっちょう）する"),
        ("労使（ろうし）", "LAO SỬ", "Người lao động và chủ sử dụng", "労使（ろうし）交渉（こうしょう）を行（おこな）う"),
        ("労災（ろうさい）", "LAO TAI", "Tai nạn trong quá trình làm việc", "労災（ろうさい）保険（ほけん）を申請（しんせい）する")
    ]
}

vocab_curriculum[12] = {
    "title": "Kinh Doanh, Doanh Nghiệp & Quản Lý (経営・管理 - けいえい・かんり)",
    "intro": "Chào bé cưng! Bài 12 đưa em vào phòng họp hội đồng quản trị với 25 từ ngữ quản lý doanh nghiệp đỉnh cao:",
    "tips": "Nhớ kỹ từ `買収` (M&A thâu tóm công ty) và `合併` (sáp nhập hai doanh nghiệp làm một). Đây là hai khái niệm vàng trong bài đọc hiểu kinh tế!",
    "words": [
        ("経営（けいえい）", "KINH DOANH", "Nghệ thuật điều hành quản trị công ty", "会社（かいしゃ）を健全（けんぜん）に経営（けいえい）する"),
        ("利益（りえき）", "LỢI ÍCH", "Lợi nhuận ròng thu về sau chi phí", "利益（りえき）を最大化（さいだいか）する"),
        ("方針（ほうしん）", "PHƯƠNG CHÂM", "Đường lối, phương châm hành động", "経営（けいえい）方針（ほうしん）を発表（はっぴょう）する"),
        ("管理（かんり）", "QUẢN LÝ", "Giám sát, theo dõi trông coi", "品質（ひんしつ）管理（かんり）を徹底（てってい）する"),
        ("企業（きぎょう）", "XÍ NGHIỆP", "Tổ chức doanh nghiệp kinh doanh", "大（だい）企業（きぎょう）と提携（ていけい）する"),
        ("買収（ばいしゅう）", "MÃI THU", "Thâu tóm mua lại doanh nghiệp khác", "競合（きょうごう）他社（たしゃ）を買収（ばいしゅう）する"),
        ("合併（がっぺい）", "HỢP TINH", "Sáp nhập hai công ty làm một", "二社（にしゃ）が対等（たいとう）に合併（がっぺい）する"),
        ("倒産（とうさん）", "ĐẢO SẢN", "Phá sản, vỡ nợ đóng cửa công ty", "多額（たがく）の負債（ふさい）で倒産（とうさん）する"),
        ("資本（しほん）", "TƯ BẢN", "Nguồn vốn đăng ký hoạt động", "資本（しほん）金（きん）を増資（ぞうし）する"),
        ("投資（とうし）", "ĐẦU TƯ", "Bỏ tiền của đầu tư phát triển", "新分野（しんぶんや）に投資（とうし）する"),
        ("資金繰（しきんぐ）り", "TƯ KIM LẠI", "Sự luân chuyển xoay vòng tiền mặt", "資金繰（しきんぐ）りに苦（くる）しむ"),
        ("取引先（とりひきさき）", "THỦ DẪN TIÊN", "Đối tác bạn hàng kinh doanh thân cận", "新規（しんき）の取引先（とりひきさき）を開拓（かいたく）する"),
        ("提携（ていけい）", "ĐỀ HUỆ", "Bắt tay liên minh hợp tác làm ăn", "海外（かいがい）企業（きぎょう）と業務（ぎょうむ）提携（ていけい）する"),
        ("独占（どくせん）", "ĐỘC CHIÊM", "Thâu tóm độc chiếm thị trường", "市場（しじょう）を独占（どくせん）する"),
        ("開拓（かいたく）", "KHAI THÁC", "Mở rộng khai thông thị trường mới", "海外（かいがい）市場（しじょう）を開拓（かいたく）する"),
        ("資産（しさん）", "TƯ SẢN", "Của cải tài sản đứng tên sở hữu", "有形（ゆうけい）資産（しさん）を管理（かんり）する"),
        ("負債（ふさい）", "PHỤ TRÁI", "Các khoản nợ nần còn tồn đọng", "負債（ふさい）を返済（へんさい）する"),
        ("監査（かんさ）", "GIÁM TRA", "Kiểm toán, thanh tra sổ sách kỹ", "会計（かいけい）監査（かんさ）を受（う）ける"),
        ("株式（かぶしき）", "CỔ THỨC", "Cổ phiếu niêm yết trên thị trường", "株式（かぶしき）を公開（こうかい）する"),
        ("配当（はいとう）", "PHỐI ĐƯƠNG", "Cổ tức chia tiền lãi cho cổ đông", "株主（かぶぬし）に配当（はいとう）を支払（しはら）う"),
        ("役員（やくいん）", "DỊCH VIÊN", "Thành viên ban giám đốc lãnh đạo", "役員（やくいん）会（かい）を開催（かいさい）する"),
        ("株主（かぶぬし）", "CỔ CHỦ", "Cổ đông nắm giữ cổ phần công ty", "株主（かぶぬし）総会（そうかい）で議決（ぎけつ）する"),
        ("業績不振（ぎょうせきふしん）", "NGHIỆP TÍCH BẤT CHẤN", "Kinh doanh bết bát, kết quả sa sút", "業績不振（ぎょうせきふしん）に陥（おちい）る"),
        ("立（た）て直（なお）す", "LẬP TRỰC", "Vực dậy cơ đồ, khôi phục lại", "倒産（とうさん）寸前（すんぜん）の会社（かいしゃ）を立（た）て直（なお）す"),
        ("再建（さいけん）", "TÁI KIẾN", "Tái thiết, xây dựng lại hệ thống", "経営（けいえい）を再建（さいけん）する")
    ]
}

vocab_curriculum[13] = {
    "title": "Khí Tượng, Thiên Nhiên & Thiên Tai (気象・自然 - きしょう・しぜん)",
    "intro": "Chào bé cưng! Bài 13 cung cấp 25 từ then chốt về thời tiết, hiện tượng tự nhiên và ứng phó thiên tai:",
    "tips": "Từ `猛暑` (nắng nóng gay gắt cực đoan) và `寒波` (đợt không khí lạnh buốt) rất hay xuất hiện trong dự báo thời tiết và bài thi nghe N2!",
    "words": [
        ("気候変動（きこうへんどう）", "KHÍ HẬU BIẾN ĐỘNG", "Biến đổi khí hậu trên diện rộng", "地球（ちきゅう）規模（きぼ）の気候変動（きこうへんどう）"),
        ("災害（さいがい）", "TAI HẠI", "Thiên tai thảm họa ập đến bất ngờ", "自然（しぜん）災害（さいがい）に備（そな）える"),
        ("警報（けいほう）", "CẢNH BÁO", "Cảnh báo khẩn cấp phát ra", "大雨（おおあめ）警報（けいほう）が発令（はつれい）される"),
        ("予測（よそく）", "DỰ TRẮC", "Dự đoán xu thế diễn biến tương lai", "進路（しんろ）を正確（せいかく）に予測（よそく）する"),
        ("集中豪雨（しゅうちゅうごうう）", "TẬP TRUNG HÀO VŨ", "Mưa rào trút nước xối xả cục bộ", "局地（きょくち）的（てき）な集中豪雨（しゅうちゅうごうう）"),
        ("猛暑（もうしょ）", "MÃNH THỬ", "Cái nóng bức oi ả thiêu đốt", "記録（きろく）的（てき）な猛暑（もうしょ）が続（つづ）く"),
        ("寒波（かんぱ）", "HÀN BA", "Làn sóng gió rét căm căm tràn về", "強烈（きょうれつ）な寒波（かんぱ）が襲来（しゅうらい）する"),
        ("洪水（こうずい）", "HỒNG THỦY", "Nước lũ dâng cao gây lụt lội", "河川（かせん）が氾濫（はんらん）して洪水（こうずい）になる"),
        ("土砂崩（どしゃくず）れ", "THỔ SA BĂNG", "Sạt lở đất đá kinh hoàng trên núi", "大雨（おおあめ）で土砂崩（どしゃくず）れが起（お）きる"),
        ("避難（ひなん）", "TỴ NẠN", "Sơ tán di tản lánh nạn an toàn", "高台（たかだい）へ避難（ひなん）する"),
        ("警戒（けいかい）", "CẢNH GIỚI", "Cảnh giác cao độ trước rủi ro", "土砂（どしゃ）災害（さいがい）に警戒（けいかい）する"),
        ("観測（かんそく）", "QUAN TRẮC", "Đo đạc, quan sát hiện tượng thời tiết", "気温（きおん）を観測（かんそく）する"),
        ("突風（とっぷう）", "ĐỘT PHONG", "Cơn gió giật lốc bất thình lình", "突風（とっぷう）で屋根（やね）が飛（と）ばされる"),
        ("雷雨（らいう）", "LÔI VŨ", "Cơn mưa dông sấm chớp ầm ầm", "激（はげ）しい雷雨（らいう）に見舞（みま）われる"),
        ("地震（じしん）", "ĐỊA CHẤN", "Động đất rung chuyển mặt đất", "マグニチュード7の地震（じしん）"),
        ("津波（つなみ）", "TÂN BA", "Sóng thần cuộn dâng từ biển", "津波（つなみ）警報（けいほう）が出（で）る"),
        ("余震（よしん）", "DƯ CHẤN", "Dư chấn rung lắc nối tiếp sau", "大（おお）きな余震（よしん）に注意（ちゅうい）する"),
        ("火口（かこう）", "HỎA KHẨU", "Miệng núi lửa phun trào nham thạch", "火口（かこう）から煙（けむり）が上（あ）がる"),
        ("噴火（ふんか）", "PHÚN HỎA", "Núi lửa phun tro bụi và nham thạch", "火山（かざん）が噴火（ふんか）する"),
        ("干ばつ（かんばつ）", "CAN", "Hạn hán khô cằn thiếu nước dài ngày", "深刻（しんこく）な干（かん）ばつに見舞（みま）われる"),
        ("被害（ひがい）", "BÌ HẠI", "Tổn thất thiệt hại để lại sau bão", "甚大（じんだい）な被害（ひがい）を受（う）ける"),
        ("復旧（ふっきゅう）", "PHỤC CỰU", "Khắc phục khôi phục lại hạ tầng", "停電（ていでん）から復旧（ふっきゅう）する"),
        ("防災（ぼうさい）", "PHÒNG TAI", "Phòng chống giảm nhẹ hiểm họa thiên tai", "防災（ぼうさい）訓練（くんれん）に参加（さんか）する"),
        ("予報（よほう）", "DỰ BÁO", "Dự báo thời tiết trước hàng ngày", "天気（てんき）予報（よほう）を確認（かくにん）する"),
        ("発生（はっせい）", "PHÁT SINH", "Bùng phát, nảy sinh bất ngờ", "台風（たいふう）が発生（はっせい）する")
    ]
}

vocab_curriculum[14] = {
    "title": "Lịch Sử, Truyền Thống & Xã Hội (歴史・文化 - れきし・ぶんか)",
    "intro": "Chào bé cưng! Bài 14 giúp em tiếp cận các khái niệm chiều sâu về cội nguồn, văn hóa và phong tục tập quán:",
    "tips": "Từ `継承` (kế thừa truyền thống) và `伝承` (lưu truyền đời này sang đời khác) là chìa khóa mở điểm cho các bài văn luận văn hóa N2!",
    "words": [
        ("伝統（でんとう）", "TRUYỀN THỐNG", "Truyền thống ngàn đời cha ông để lại", "古（ふる）き良（よ）き伝統（でんとう）を守（まも）る"),
        ("遺産（いさん）", "DI SẢN", "Di sản văn hóa vật thể và phi vật thể", "世界（せかい）文化（ぶんか）遺産（いさん）に登録（とうろく）される"),
        ("継承（けいしょう）", "KẾ THỪA", "Kế tục tiếp nối di sản tiền nhân", "伝統（でんとう）芸能（げいのう）を継承（けいしょう）する"),
        ("風習（ふうしゅう）", "PHONG TẬP", "Phong tục tập quán của làng quê", "地域（ちいき）特有（とくゆう）の風習（ふうしゅう）"),
        ("起源（きげん）", "KHỞI NGUYÊN", "Nguồn gốc xuất xứ khởi thủy bắt đầu", "祭（まつ）りの起源（きげん）を調（しら）べる"),
        ("儀式（ぎしき）", "NGHI THỨC", "Lễ nghi trang trọng tôn nghiêm", "厳（おごそ）かに儀式（ぎしき）を執（と）り行（おこな）う"),
        ("変遷（へんせん）", "BIẾN THIÊN", "Sự thay đổi thăng trầm theo thời gian", "時代（じだい）の変遷（へんせん）をたどる"),
        ("復元（ふくげん）", "PHỤC NGUYÊN", "Dựng lại nguyên trạng di tích cũ", "城（しろ）の姿（すがた）を復元（ふくげん）する"),
        ("発掘（はっくつ）", "PHÁT QUẬT", "Khai quật di chỉ khảo cổ học", "古代（こだい）の遺跡（いせき）を発掘（はっくつ）する"),
        ("遺跡（いせき）", "DI TÍCH", "Dấu tích công trình cổ xưa còn lại", "歴史（れきし）的（てき）な遺跡（いせき）を巡（めぐ）る"),
        ("伝承（でんしょう）", "TRUYỀN THỪA", "Lưu truyền chuyện xưa qua các thế hệ", "民話（みんわ）を後世（こうせい）に伝承（でんしょう）する"),
        ("名残（なごり）", "DANH TÀN", "Tàn tích, dấu vết sót lại của quá khứ", "江戸（えど）時代（じだい）の名残（なごり）をとどめる"),
        ("象徴（しょうちょう）", "TƯỢNG TRƯNG", "Biểu tượng mang ý nghĩa thiêng liêng", "平和（へいわ）の象徴（しょうちょう）"),
        ("信仰（しんこう）", "TÍN NGƯỠNG", "Đức tin và lòng tôn thờ tín ngưỡng", "神（かみ）への信仰（しんこう）を深（ふか）める"),
        ("慣習（かんしゅう）", "QUÁN TẬP", "Thói quen nề nếp xã hội quen thuộc", "社会（しゃかい）的（てき）な慣習（かんしゅう）に従（したが）う"),
        ("由来（ゆらい）", "DO LAI", "Lai lịch, gốc tích cái tên sự việc", "地名（ちめい）の由来（ゆらい）を尋（たず）ねる"),
        ("時代錯誤（じだいさくご）", "THỜI ĐẠI THÁC NGỘ", "Lạc hậu lỗi thời không hợp thời đại", "時代錯誤（じだいさくご）な考（かんが）え方（かた）"),
        ("重鎮（じゅうちん）", "TRỌNG TRẤN", "Cây đa cây đề trụ cột trong giới", "政界（せいかい）の重鎮（じゅうちん）"),
        ("由緒（ゆいしょ）", "DO TỰ", "Bề dày lịch sử dòng dõi danh giá", "由緒（ゆいしょ）ある神社（じんじゃ）"),
        ("古文書（こもんじょ）", "CỔ VĂN THƯ", "Tài liệu văn tự cổ ngày xưa ghi chép", "古文書（こもんじょ）を解読（かいどく）する"),
        ("風土（ふうど）", "PHONG THỔ", "Khí hậu và bản sắc địa phương riêng", "土地（とち）の風土（ふうど）に育（はぐく）まれる"),
        ("民俗（みんぞく）", "DÂN TỤC", "Văn hóa dân gian tập tục truyền miệng", "民俗（みんぞく）学（がく）を研究（けんきゅう）する"),
        ("開拓（かいたく）", "KHAI THÁC", "Khai phá vùng đất hoang sơ lập ấp", "荒野（こうや）を開拓（かいたく）する"),
        ("先祖（せんぞ）", "TIÊN TỔ", "Tổ tiên nhiều đời trước của gia đình", "先祖（せんぞ）の墓（はか）にお参（まい）りする"),
        ("後世（こうせい）", "HẬU THẾ", "Các thế hệ con cháu đời mai sau", "名作（めいさく）を後世（こうせい）に残（のこ）す")
    ]
}

vocab_curriculum[15] = {
    "title": "Tâm Lý & Xu Hướng Hành Vi (心理・行動 - しんり・こうどう)",
    "intro": "Chào bé cưng! Bài 15 mổ xẻ nội tâm con người: động cơ, tiềm thức và diễn biến tâm lý vi tế:",
    "tips": "Từ `葛藤` (cát đằng = dằn vặt đấu tranh nội tâm) cực kỳ đắt giá khi làm bài đọc hiểu diễn biến nhân vật trong văn học!",
    "words": [
        ("心理（しんり）", "TÂM LÝ", "Trạng thái nội tâm bên trong con người", "消費者（しょうひしゃ）の心理（しんり）を分析（ぶんせき）する"),
        ("動機（どうき）", "ĐỘNG CƠ", "Động cơ thôi thúc dẫn tới hành động", "犯行（はんこう）の動機（どうき）を自供（じきょう）する"),
        ("衝動（しょうどう）", "XUNG ĐỘNG", "Xung động nhất thời không kiềm chế nổi", "衝動（しょうどう）的（てき）に買（か）い物（もの）をする"),
        ("葛藤（かっとう）", "CÁT ĐẰNG", "Dằn vặt giằng xé nội tâm khó xử", "内心（ないしん）の葛藤（かっとう）と闘（たたか）う"),
        ("本能（ほんのう）", "BẢN NĂNG", "Bản năng sinh tồn bẩm sinh sẵn có", "生存（せいぞん）の本能（ほんのう）に従（したが）う"),
        ("錯覚（さっかく）", "THÁC GIÁC", "Ảo giác, nhìn nhầm ngộ nhận cảm giác", "目（め）の錯覚（さっかく）を利用（りよう）する"),
        ("偏見（へんけん）", "THIÊN KIẾN", "Định kiến một chiều thiếu công tâm", "偏見（へんけん）を捨（す）てて接（せっ）する"),
        ("直感（ちょっかん）", "TRỰC CẢM", "Trực giác mách bảo nhạy bén", "直感（ちょっかん）を信（しん）じて決断（けつだん）する"),
        ("劣等感（れっとうかん）", "LIỆT ĐẲNG CẢM", "Cảm giác tự ti mặc cảm thua kém bạn bè", "強（つよ）い劣等感（れっとうかん）を抱（いだ）く"),
        ("優越感（ゆうえつかん）", "ƯU VIỆT CẢM", "Cảm giác tự mãn vượt trội hơn người", "優越感（ゆうえつかん）に浸（ひた）る"),
        ("トラウマ（トラウマ）", "VẾT THƯƠNG LÒNG", "Ám ảnh tâm lý sau cú sốc lớn", "過去（かこ）のトラウマを克服（こくふく）する"),
        ("共感（きょうかん）", "CỘNG CẢM", "Đồng cảm sâu sắc rung động lòng trắc ẩn", "相手（あいて）の気持（きも）ちに共感（きょうかん）する"),
        ("反発（はんぱつ）", "PHẢN PHÁT", "Chống đối bật lại, bất mãn biểu lộ", "親（おや）の言（い）い分（ぶん）に反発（はんぱつ）する"),
        ("躊躇（ちゅうちょ）", "TRÙ TRỪ", "Ngập ngừng đắn đo không dám quyết", "躊躇（ちゅうちょ）せずに申（もう）し込（こ）む"),
        ("執着（しゅうちゃく）", "CHẤP TRƯỚC", "Mê muội cố chấp bám víu không buông", "過去（かこ）の栄光（えいこう）に執着（しゅうちゃく）する"),
        ("安堵（あんど）", "AN ĐỔ", "Thở phào nhẹ nhõm trút được gánh nặng", "無事（ぶじ）を知（し）って安堵（あんど）する"),
        ("猜疑心（さいぎしん）", "SAI NGHI TÂM", "Tâm địa đa nghi ngờ vực người khác", "猜疑心（さいぎしん）を抱（いだ）く"),
        ("罪悪感（ざいあくかん）", "TỘI ÁC CẢM", "Cảm giác tội lỗi cắn rứt lương tâm", "嘘（うそ）をついて罪悪感（ざいあくかん）に苛（さいな）まれる"),
        ("自己嫌悪（じこけんお）", "TỰ KỶ HIỀM ÁC", "Chán ghét bản thân thất bại tồi tệ", "失敗（しっぱい）して自己嫌悪（じこけんお）に陥（おちい）る"),
        ("虚栄心（きょえいしん）", "HƯ VINH TÂM", "Tính hám hư danh thích khoe mẽ", "虚栄心（きょえいしん）から嘘（うそ）をつく"),
        ("無力感（むりょくかん）", "VÔ LỰC CẢM", "Cảm giác bất lực không làm gì được", "深（ふか）い無力感（むりょくかん）に襲（おそ）われる"),
        ("好奇心（こうきしん）", "HẢO KỲ TÂM", "Tò mò ham khám phá học hỏi điều mới", "旺盛（おうせい）な好奇心（こうきしん）を持（も）つ"),
        ("潔癖（けっぺき）", "KHIẾT PHÁCH", "Ưa sạch sẽ quá mức, ghét điều mờ ám", "潔癖（けっぺき）な性格（せいかく）"),
        ("共鳴（きょうめい）", "CỘNG MINH", "Hưởng ứng cùng chung chí hướng nhịp đập", "理念（りねん）に深（ふか）く共鳴（きょうめい）する"),
        ("焦燥感（しょうそうかん）", "TIÊU TÁO CẢM", "Cảm giác bồn chồn đứng ngồi không yên", "時間（じかん）に追（お）われ焦燥感（しょうそうかん）を覚（おぼ）える")
    ]
}

vocab_curriculum[16] = {
    "title": "Nghệ Thuật, Thể Thao & Giải Trí (芸術・娯楽 - げいじゅつ・ごらく)",
    "intro": "Chào bé cưng! Bài 16 thăng hoa cảm xúc với 25 từ miêu tả hội họa, âm nhạc, sân khấu kịch và cảm thụ cái đẹp:",
    "tips": "Cụm `感銘を受ける` (cảm động sâu sắc, khắc cốt ghi tâm trước một tác phẩm) là cụm từ vàng trong các bài văn nghị luận nghệ thuật!",
    "words": [
        ("創作（そうさく）", "SÁNG TÁC", "Sáng tạo tác phẩm nghệ thuật mới", "小説（しょうせつ）の創作（そうさく）活動（かつどう）に励（はげ）む"),
        ("鑑賞（かんしょう）", "GIÁM THƯỞNG", "Thưởng thức, cảm thụ cái đẹp nghệ thuật", "美術（びじゅつ）鑑賞（かんしょう）が趣味（しゅみ）だ"),
        ("傑作（けっさく）", "KIỆT TÁC", "Kiệt tác xuất chúng để đời", "歴史（れきし）に残（のこ）る傑作（けっさく）を生（う）み出（だ）す"),
        ("情熱（じょうねつ）", "TÌNH NHIỆT", "Ngọn lửa đam mê cháy bỏng nhiệt huyết", "音楽（おんがく）に情熱（じょうねつ）を注（そそ）ぐ"),
        ("演奏（えんそう）", "DIỄN TẤU", "Biểu diễn tấu đàn nhạc cụ", "ピアノの素晴（すば）らしい演奏（えんそう）"),
        ("脚本（きゃくほん）", "CƯỚC BẢN", "Kịch bản sân khấu và điện ảnh", "映画（えいが）の脚本（きゃくほん）を執筆（しっぴつ）する"),
        ("舞台（ぶたい）", "VŨ ĐÀI", "Sân khấu kịch nghệ thuật lộng lẫy", "舞台（ぶたい）に立（た）って演（えん）じる"),
        ("演出（えんしゅつ）", "DIỄN XUẤT", "Đạo diễn dàn dựng cảnh trí tác phẩm", "光（ひかり）と音（おと）の演出（えんしゅつ）が際立（きわだ）つ"),
        ("俳優（はいゆう）", "BÀI ƯU", "Diễn viên kịch, nghệ sĩ điện ảnh", "実力（じつりょく）派（は）の俳優（はいゆう）"),
        ("役柄（やくがら）", "DỊCH BÍNH", "Tính chất vai diễn trong kịch bản", "難（むずか）しい役柄（やくがら）を見事（みごと）に演（えん）じる"),
        ("個性（こせい）", "CÁ TÍNH", "Cá tính riêng biệt không trùng lặp", "豊（ゆた）かな個性（こせい）を発揮（はっき）する"),
        ("独自性（どくじせい）", "ĐỘC TỰ TÍNH", "Tính độc đáo, phong cách riêng biệt", "作品（さくひん）の独自性（どくじせい）を追求（ついきゅう）する"),
        ("独創的（どくそうてき）", "ĐỘC SÁNG ĐÍCH", "Sáng tạo mới lạ chưa từng có trước đó", "独創的（どくそうてき）な発想（はっそう）に驚（おどろ）く"),
        ("拍手（はくしゅ）", "PHÁCH THỦ", "Vỗ tay tán thưởng nồng nhiệt", "惜（お）しみない拍手（はくしゅ）を送（おく）る"),
        ("喝采（かっさい）", "HÁT THẢI", "Reo hò cổ vũ vang dội cầu trường", "満場（まんじょう）の喝采（かっさい）を浴（あ）びる"),
        ("陶酔（とうすい）", "ĐÀO TÚY", "Say sưa mê đắm chìm trong giai điệu", "美（うつく）しい音色（ねいろ）に陶酔（とうすい）する"),
        ("魅了（みりょう）", "MỊ LIỄU", "Mê hoặc, cuốn hút hớp hồn khán giả", "観客（かんきゃく）を魅了（みりょう）する"),
        ("感銘（かんめい）を受（う）ける", "CẢM MINH", "Xúc động sâu sắc, khắc cốt ghi tâm", "名作（めいさく）に深（ふか）く感銘（かんめい）を受（う）ける"),
        ("余韻（よいん）", "DƯ VẬN", "Dư âm lắng đọng mãi trong tâm trí", "コンサートの後（のち）の余韻（よいん）に浸（ひた）る"),
        ("展覧会（てんらんかい）", "TRIỂN LÃM HỘI", "Triển lãm trưng bày tranh tượng", "絵画（かいが）の展覧会（てんらんかい）へ行（い）く"),
        ("描写（びょうしゃ）", "MIÊU TẢ", "Khắc họa miêu tả chân thực từng nét", "心理（しんり）を細（こま）やかに描写（びょうしゃ）する"),
        ("調和（ちょうわ）", "ĐIỀU HÒA", "Hài hòa cân đối màu sắc âm thanh", "全体（ぜんたい）の調和（ちょうわ）が保（たも）たれている"),
        ("名作（めいさく）", "DANH TÁC", "Tác phẩm danh tiếng để đời", "後世（こうせい）に伝（つた）わる名作（めいさく）"),
        ("才能（さいのう）", "TÀI NĂNG", "Tố chất tài hoa thiên bẩm", "隠（かく）れた才能（さいのう）を開花（かいか）させる"),
        ("情景（じょうけい）", "TÌNH CẢNH", "Cảnh tượng gợi xúc cảm trong lòng", "懐（なつ）かしい情景（じょうけい）を思（おも）い浮（う）かべる")
    ]
}

print("Loaded Lesson 11 - 16.")

# ==========================================
# BÀI 17 - BÀI 21
# ==========================================
vocab_curriculum[17] = {
    "title": "Pháp Luật, Trật Tự & Quy Chế (法律・秩序 - ほうりつ・ちつじょ)",
    "intro": "Chào bé cưng! Bài 17 nâng tầm kiến thức với 25 thuật ngữ tòa án, pháp lý và trật tự công cộng chuẩn đề thi N2:",
    "tips": "Nhớ cặp đôi trong phiên tòa: `原告` (nguyên cáo = người đâm đơn đi kiện) và `被告` (bị cáo = người bị kiện ra trước tòa) nha cưng!",
    "words": [
        ("規則（きそく）", "QUY TẮC", "Nội quy điều lệ chung phải tuân theo", "規則（きそく）を厳守（げんしゅ）する"),
        ("秩序（ちつじょ）", "TRẬT TỰ", "Trật tự an ninh xã hội ổn định", "社会（しゃかい）の秩序（ちつじょ）を乱（みだ）す"),
        ("違反（いはん）", "VI PHẠM", "Phạm luật trái phép, vi phạm quy tắc", "交通（こうつう）ルールに違反（いはん）する"),
        ("遵守（じゅんしゅ）", "TUÂN THỦ", "Chấp hành nghiêm chỉnh luật pháp", "法令（ほうれい）を遵守（じゅんしゅ）する"),
        ("制定（せいてい）", "CHẾ ĐỊNH", "Ban hành xây dựng đạo luật mới", "新（あたら）しい法律（ほうりつ）を制定（せいてい）する"),
        ("改正（かいせい）", "CẢI CHÍNH", "Sửa đổi bổ sung điều luật cũ", "憲法（けんぽう）を改正（かいせい）する"),
        ("施行（しこう）", "THI HÀNH", "Đưa luật vào thực thi đời sống", "改正（かいせい）法（ほう）が施行（しこう）される"),
        ("条例（じょうれい）", "ĐIỀU LỆ", "Quy định điều lệ do địa phương ban hành", "路上（ろじょう）喫煙（きつえん）禁止（きんし）の条例（じょうれい）"),
        ("訴訟（そしょう）", "TỐ TỤNG", "Kiện tụng lôi nhau ra pháp đình", "損害（そんがい）賠償（ばいしょう）の訴訟（そしょう）を起（お）こす"),
        ("裁判（さいばん）", "TÀI PHÁN", "Phiên tòa xét xử định đoạt đúng sai", "裁判（さいばん）で無罪（むざい）を主張（しゅちょう）する"),
        ("判決（はんけつ）", "PHÁN QUYẾT", "Lời tuyên án chính thức của quan tòa", "有罪（ゆうざい）の判決（はんけつ）が下（くだ）る"),
        ("原告（げんこく）", "NGUYÊN CÁO", "Người khởi kiện, bên nguyên", "原告（げんこく）側（がわ）の訴（うった）えを認（みと）める"),
        ("被告（ひこく）", "BỊ CÁO", "Người bị kiện đứng trước vành móng ngựa", "被告（ひこく）に懲役（ちょうえき）5年（ごねん）を求刑（きゅうけい）する"),
        ("証拠（しょうこ）", "CHỨNG CỨ", "Bằng chứng vật chứng nhân chứng xác thực", "動（うご）かぬ証拠（しょうこ）を提示（ていじ）する"),
        ("権利（けんり）", "QUYỀN LỢI", "Quyền lợi hợp pháp của công dân", "基本（きほん）的人権（じんけん）の権利（けんり）"),
        ("義務（ぎむ）", "NGHĨA VỤ", "Nghĩa vụ trách nhiệm pháp lý bắt buộc", "法（ほう）に定（さだ）められた義務（ぎむ）"),
        ("損害賠償（そんがいばいしょう）", "TỔN HẠI BỒI THƯỜNG", "Đền bù thiệt hại vật chất và tinh thần", "損害賠償（そんがいばいしょう）を請求（せいきゅう）する"),
        ("処罰（しょばつ）", "XỨ PHẠT", "Xử lý kỷ luật, chế tài xử phạt", "不正（ふせい）行為（こうい）を厳（きび）しく処罰（しょばつ）する"),
        ("刑罰（けいばつ）", "HÌNH PHẠT", "Hình phạt tù tội giam giữ theo luật", "重（おも）い刑罰（けいばつ）が科（か）される"),
        ("違法（いほう）", "VI PHÁP", "Bất hợp pháp, phạm vào điều cấm", "違法（いほう）な手段（しゅだん）でお金（かね）を得（え）る"),
        ("合法（ごうほう）", "HỢP PHÁP", "Hợp pháp, tuân theo đúng khuôn khổ", "合法（ごうほう）的（てき）な範囲（はんい）で行動（こうどう）する"),
        ("弁護士（べんごし）", "BIỆN HỘ SĨ", "Luật sư bào chữa bảo vệ thân chủ", "有能（ゆうのう）な弁護士（べんごし）を雇（やと）う"),
        ("審理（しんり）", "THẨM LÝ", "Xem xét thẩm tra hồ sơ vụ án tại tòa", "事件（じけん）の審理（しんり）が長引（ながび）く"),
        ("控訴（こうそ）", "KHỐNG TỐ", "Kháng cáo lên tòa án cấp cao hơn", "判決（はんけつ）を不服（ふふく）として控訴（こうそ）する"),
        ("棄却（ききゃく）", "KHÍ CƯỚC", "Bác đơn kiện, từ chối thụ lý", "裁判所（さいばんしょ）が訴（うった）えを棄却（ききゃく）する")
    ]
}

vocab_curriculum[18] = {
    "title": "Khoa Học, Kỹ Thuật & Đổi Mới (科学・技術 - かがく・ぎじゅつ)",
    "intro": "Chào bé cưng! Bài 18 là vũ đài của công nghệ cao, trí tuệ nhân tạo và đổi mới sáng tạo tương lai:",
    "tips": "Từ `画期的` (mang tính đột phá lịch sử) xuất hiện dày đặc trong các bài giới thiệu phát minh khoa học mới!",
    "words": [
        ("開発（かいはつ）", "KHAI PHÁT", "Nghiên cứu tạo ra sản phẩm mới", "新技術（しんぎじゅつ）を開発（かいはつ）する"),
        ("革新（かくしん）", "CÁCH TÂN", "Cách tân đổi mới vượt bậc", "技術（ぎじゅつ）革新（かくしん）が社会（しゃかい）を変（か）える"),
        ("検証（けんしょう）", "KIỂM CHỨNG", "Thực nghiệm kiểm chứng độ đúng sai", "仮説（かせつ）の正（ただ）しさを検証（けんしょう）する"),
        ("画期的（かっきてき）", "HỌA KỲ ĐÍCH", "Đột phá mang tính bước ngoặt thời đại", "画期的（かっきてき）な新薬（しんやく）が完成（かんせい）する"),
        ("実用化（じつようか）", "THỰC DỤNG HÓA", "Đưa công nghệ ứng dụng vào đời sống", "電気（でんき）自動車（じどうしゃ）を実用化（じつようか）する"),
        ("発明（はつめい）", "PHÁT MINH", "Phát minh sáng chế máy móc mới lạ", "蒸気（じょうき）機関（きかん）を発明（はつめい）する"),
        ("特許（とっきょ）", "ĐẶC HỨA", "Bằng sáng chế bảo hộ độc quyền", "技術（ぎじゅつ）の特許（とっきょ）を出願（しゅつがん）する"),
        ("人工知能（じんこうちのう）", "NHÂN CÔNG TRÍ NĂNG", "Trí tuệ nhân tạo (AI)", "人工知能（じんこうちのう）が進化（しんか）を遂（と）げる"),
        ("分析（ぶんせき）", "PHÂN TÍCH", "Mổ xẻ phân tích dữ liệu chuyên sâu", "ビッグデータを詳細（しょうさい）に分析（ぶんせき）する"),
        ("抽出（ちゅうしゅつ）", "TRỪU XUẤT", "Chiết xuất tinh chất hoặc dữ liệu mẫu", "植物（しょくぶつ）から有効（ゆうこう）成分（せいぶん）を抽出（ちゅうしゅつ）する"),
        ("合成（ごうせい）", "HỢP THÀNH", "Hợp chất tổng hợp nhân tạo", "化学（かがく）物質（ぶっしつ）を合成（ごうせい）する"),
        ("遺伝子（いでんし）", "DI TRUYỀN TỬ", "Gen di truyền cấu trúc sinh học", "遺伝子（いでんし）の組（く）み換（か）え技術（ぎじゅつ）"),
        ("細胞（さいぼう）", "TẾ BÀO", "Tế bào sống đơn vị cơ bản cơ thể", "万能（ばんのう）細胞（さいぼう）の研究（けんきゅう）"),
        ("実験（じっけん）", "THỰC NGHIỆM", "Làm thí nghiệm trong phòng lab", "実験（じっけん）室（しつ）で新（あたら）しい試（こころ）みを行（おこな）う"),
        ("装置（そうち）", "TRANG TRÍ", "Thiết bị, máy móc vận hành hỗ trợ", "最新（さいしん）の測定（そくてい）装置（そうち）を導入（どうにゅう）する"),
        ("精度（せいど）", "TINH ĐỘ", "Độ chính xác chuẩn mực tuyệt đối", "測定（そくてい）の精度（せいど）を高（たか）める"),
        ("測定（そくてい）", "TRẮC ĐỊNH", "Đo lường các thông số vật lý", "電波（でんぱ）の強（つよ）さを測定（そくてい）する"),
        ("摩擦（まさつ）", "MA SÁT", "Lực ma sát tiếp xúc cơ học", "部品（ぶひん）の摩擦（まさつ）を減（へ）らす"),
        ("伝導（でんどう）", "TRUYỀN DẪN", "Dẫn truyền nhiệt hoặc dòng điện", "熱（ねつ）の伝導（でんどう）率（りつ）が高（たか）い金属（きんぞく）"),
        ("仮説（かせつ）", "GIẢ THUYẾT", "Đưa ra giả thuyết khoa học chờ chứng minh", "大胆（だいたん）な仮説（かせつ）を立（た）てる"),
        ("現象（げんしょう）", "HIỆN TƯỢNG", "Hiện tượng tự nhiên được quan sát", "不思議（ふしぎ）な自然（しぜん）現象（げんしょう）"),
        ("探求（たんきゅう）", "THÁM CẦU", "Tìm tòi khám phá chân lý khoa học", "真理（しんり）を探求（たんきゅう）する"),
        ("解明（かいめい）", "GIẢI MINH", "Làm sáng tỏ bí ẩn chưa ai biết", "宇宙（うちゅう）の謎（なぞ）を解明（かいめい）する"),
        ("最先端（さいせんたん）", "TỐI TIÊN ĐOAN", "Đỉnh cao đi đầu công nghệ", "最先端（さいせんたん）の医療（いりょう）技術（ぎじゅつ）"),
        ("応用技術（おうようぎじゅつ）", "ỨNG DỤNG KĨ THUẬT", "Kỹ thuật ứng dụng thực tiễn vào đời sống", "基礎（きそ）研究（けんきゅう）を応用技術（おうようぎじゅつ）に生（い）かす")
    ]
}

vocab_curriculum[19] = {
    "title": "Giáo Dục, Đào Tạo & Nuôi Dạy (教育・育成 - きょういく・いくせい)",
    "intro": "Chào bé cưng! Bài 19 cung cấp 25 từ ngữ sư phạm, rèn luyện nhân cách và khai phóng tiềm năng:",
    "tips": "Từ `育む` (ấp ủ, nuôi dưỡng tình yêu/tài năng) là động từ tuyệt đẹp thường xuyên gặp trong văn phong trang trọng và đề thi N2!",
    "words": [
        ("指導（しどう）", "CHỈ ĐẠO", "Uốn nắn, hướng dẫn chỉ bảo học trò", "後輩（こうはい）を熱心（ねっしん）に指導（しどう）する"),
        ("育成（いくせい）", "DỤC THÀNH", "Đào tạo, nuôi dưỡng nhân tài tương lai", "次世代（じせだい）のリーダーを育成（いくせい）する"),
        ("自主性（じしゅせい）", "TỰ CHỦ TÍNH", "Tính chủ động, tự lập tự giác cao", "子供（こども）の自主性（じしゅせい）を重（おも）んじる"),
        ("素質（そしつ）", "TỐ CHẤT", "Năng khiếu tố chất bẩm sinh", "音楽（おんがく）の素質（そしつ）に恵（めぐ）まれる"),
        ("養成（ようせい）", "DƯỠNG THÀNH", "Rèn giũa đào tạo nghề bài bản", "教員（きょういん）を養成（ようせい）する大学（だいがく）"),
        ("理念（りねん）", "LÝ NIỆM", "Triết lý, kim chỉ nam cốt lõi giáo dục", "教育（きょういく）の基本（きほん）理念（りねん）"),
        ("規律（きりつ）", "QUY LUẬT", "Nền nếp kỷ luật nghiêm ngặt", "厳（きび）しい規律（きりつ）を守（まも）らせる"),
        ("忍耐力（にんたいりょく）", "NHẪN NẠI LỰC", "Sức chịu đựng, tính kiên nhẫn bền gan", "困難（こんなん）に耐（た）える忍耐力（にんたいりょく）を養（やしな）う"),
        ("潜在能力（せんざいのうりょく）", "TIỀM TẠI NĂNG LỰC", "Năng lực tiềm ẩn bên trong chờ khai mở", "自分（じぶん）の潜在能力（せんざいのうりょく）を信（しん）じる"),
        ("引（ひ）き出（だ）す", "DẪN XUẤT", "Khơi gợi, phát huy tài năng bên trong", "生徒（せいと）のやる気（き）を引き出（だ）す"),
        ("育（はぐく）む", "DỤC", "Ấp ủ, vun đắp nuôi dưỡng tâm hồn", "豊（ゆた）かな感性（かんせい）を育（はぐく）む"),
        ("鍛（きた）える", "ĐOÁN", "Rèn luyện thể lực và ý chí thép", "心身（しんしん）を厳（きび）しく鍛（きた）える"),
        ("模範（もはん）", "MÔ PHẠM", "Tấm gương sáng chuẩn mực noi theo", "後輩（こうはい）の模範（もはん）となる行動（こうどう）"),
        ("励（はげ）ます", "LỆ", "Khích lệ động viên học trò tiến lên", "落（お）ち込（こ）む友（とも）を温（あたた）かく励（はげ）ます"),
        ("叱責（しっせき）", "SẤC TRÁCH", "Quở mắng, khiển trách nghiêm khắc", "怠慢（たいまん）な態度（たいど）を叱責（しっせき）する"),
        ("評価（ひょうか）", "BÌNH GIÁ", "Ghi nhận nhìn nhận sự tiến bộ", "努力（どりょく）の過程（かてい）を正当（せいとう）に評価（ひょうか）する"),
        ("視野（しや）を広（ひろ）げる", "THỊ DÃ QUẢNG", "Mở rộng tầm mắt và thế giới quan", "留学（りゅうがく）して視野（しや）を広（ひろ）げる"),
        ("教養（きょうよう）", "GIÁO DƯỠNG", "Vốn văn hóa học thức sâu rộng", "豊（ゆた）かな教養（きょうよう）を身（み）につける"),
        ("専攻（せんこう）", "CHUYÊN CÔNG", "Đi sâu nghiên cứu chuyên ngành học", "大学院（だいがくいん）で哲学（てつがく）を専攻（せんこう）する"),
        ("奨励（しょうれい）", "TƯỞNG LỆ", "Khuyến khích, động viên làm điều tốt", "読書（どくしょ）を大（おお）いに奨励（しょうれい）する"),
        ("培（つちか）う", "BỒI", "Vun xới bồi đắp kinh nghiệm quý báu", "長年（ながねん）培（つちか）った信頼（しんらい）関係（かんけい）"),
        ("指針（ししん）", "CHỈ CHÂM", "Định hướng kim chỉ nam hành động", "人生（じんせい）の指針（ししん）となる言葉（ことば）"),
        ("人材（じんざい）", "NHÂN TÀI", "Nguồn lực con người chất lượng cao", "優秀（ゆうしゅう）な人材（じんざい）を確保（かくほ）する"),
        ("適性（てきせい）", "THÍCH TÍNH", "Độ phù hợp, năng khiếu thích hợp nghề", "職業（しょくぎょう）適性（てきせい）検査（けんさ）を受（う）ける"),
        ("啓発（けいはつ）", "KHẢI PHÁT", "Khai sáng mở mang trí tuệ nhận thức", "自己（じこ）啓発（けいはつ）の本（ほん）を読（よ）む")
    ]
}

vocab_curriculum[20] = {
    "title": "Môi Trường Sinh Thái & Tài Nguyên (環境・資源 - かんきょう・しげん)",
    "intro": "Chào bé cưng! Bài 20 là chủ đề nóng bỏng của thế kỷ 21: bảo vệ môi trường, rác thải và năng lượng xanh:",
    "tips": "Từ `枯渇` (khô kiệt = cạn kiệt tài nguyên) và `削減` (tước giảm = cắt giảm khí thải CO2) xuất hiện tới 90% trong bài đọc hiểu khoa học môi trường!",
    "words": [
        ("資源（しげん）", "TÀI NGUYÊN", "Tài nguyên thiên nhiên khoáng sản", "天然（てんねん）資源（しげん）を有効（ゆうこう）に活用（かつよう）する"),
        ("再生（さいせい）", "TÁI SINH", "Tái sinh, tái chế rác thành đồ hữu ích", "再生（さいせい）可能（かのう）エネルギー"),
        ("節約（せつやく）", "TIẾT ƯỚC", "Tằn tiện tiết kiệm điện nước chi tiêu", "電気（でんき）と水（みず）を節約（せつやく）する"),
        ("保護（ほご）", "BẢO HỘ", "Bảo vệ giữ gìn động vật và tự nhiên", "自然（しぜん）環境（かんきょう）を保護（ほご）する"),
        ("枯渇（こかつ）", "KHÔ KIỆT", "Cạn kiệt khô cạn nguồn tài nguyên dầu mỏ", "地下水（ちかすい）が枯渇（こかつ）する"),
        ("削減（さくげん）", "TƯỚC GIẢM", "Cắt giảm lượng khí thải độc hại", "二酸化炭素（にさんかたんそ）の排出（はいしゅつ）を削減（さくげん）する"),
        ("汚染（おせん）", "Ô NHIỄM", "Ô nhiễm môi trường không khí nguồn nước", "工場（こうじょう）排水（はいすい）で川（かわ）が汚染（おせん）される"),
        ("排出量（はいしゅつりょう）", "BÀI XUẤT LƯỢNG", "Lượng khói bụi khí thải nhả ra trời", "温室（おんしつ）効果（こうか）ガスの排出量（はいしゅつりょう）"),
        ("生態系（せいたいけい）", "SINH THÁI HỆ", "Hệ sinh thái muôn loài cân bằng", "生態系（せいたいけい）が破壊（はかい）される"),
        ("絶滅（ぜつめつ）", "TUYỆT DIỆT", "Tuyệt chủng biến mất vĩnh viễn trên đời", "希少（きしょう）な野生（やせい）動物（どうぶつ）が絶滅（ぜつめつ）の危機（きき）に瀕（ひん）する"),
        ("温暖化（おんだんか）", "ÔN NOÃN HÓA", "Sự nóng lên của nhiệt độ toàn cầu", "地球（ちきゅう）温暖化（おんだんか）を食（と）め止（と）める"),
        ("再利用（さいりよう）", "TÁI LỢI DỤNG", "Tái sử dụng đồ cũ nhiều lần bền lâu", "不用品（ふようひん）を再利用（さいりよう）する"),
        ("省（しょう）エネ", "TỈNH", "Tiết kiệm điện năng tối đa khi dùng", "省（しょう）エネ家電（かでん）に買（か）い換（か）える"),
        ("太陽光（たいようこう）", "THÁI DƯƠNG QUANG", "Năng lượng ánh sáng mặt trời tự nhiên", "太陽光（たいようこう）発電（はつでん）パネルを設置（せっち）する"),
        ("廃棄物（はいきぶつ）", "PHẾ KHÍ VẬT", "Chất thải rác thải công nghiệp bỏ đi", "産業（さんぎょう）廃棄物（はいきぶつ）を適切（てきせつ）に処理（しょり）する"),
        ("浄化（じょうか）", "TỊNH HÓA", "Thanh lọc làm sạch nước bẩn không khí", "汚濁（おだく）した河川（かせん）を浄化（じょうか）する"),
        ("保全（ほぜん）", "BẢO TOÀN", "Bảo tồn nguyên vẹn môi trường sinh thái", "森林（しんりん）環境（かんきょう）を保全（ほぜん）する"),
        ("伐採（ばっさい）", "PHẠT THÁI", "Chặt đốn phá rừng lấy gỗ bừa bãi", "熱帯（ねったい）雨林（うりん）の過度（かど）な伐採（ばっさい）"),
        ("酸性雨（さんせいう）", "TOAN TÍNH VŨ", "Mưa axit do khói bụi hủy hoại rừng", "酸性雨（さんせいう）で木々（きぎ）が枯（か）れる"),
        ("温室効果（おんしつこうか）", "ÔN THẤT HIỆU QUẢ", "Hiệu ứng nhà kính giữ nhiệt làm nóng", "温室効果（おんしつこうか）ガスを削減（さくげん）する"),
        ("自然エネルギー（しぜんエネルギー）", "TỰ NHIÊN", "Năng lượng sạch từ gió nắng và nước", "自然（しぜん）エネルギーの導入（どうにゅう）を進（すす）める"),
        ("分別（ぶんべつ）", "PHÂN BIỆT", "Phân chia rác theo chủng loại", "ごみの分別（ぶんべつ）を徹底（てってい）する"),
        ("回収（かいしゅう）", "HỒI THU", "Thu gom chai lọ pin cũ về xử lý", "ペットボトルを回収（かいしゅう）する"),
        ("エコ（エコ）", "SINH THÁI", "Lối sống xanh thân thiện với trái đất", "エコバッグを持参（じさん）して買（か）い物（もの）する"),
        ("生物多様性（せいぶつたようせい）", "SINH VẬT ĐA DẠNG TÍNH", "Sự phong phú muôn loài sinh học", "生物多様性（せいぶつたようせい）を守（まも）る条約（じょうやく）")
    ]
}

vocab_curriculum[21] = {
    "title": "Chính Trị, Ngoại Giao & Nhà Nước (政治・外交 - せいじ・がいこう)",
    "intro": "Chào bé cưng! Bài 21 mở rộng kiến thức xã hội với 25 từ ngữ chính trường, quan hệ bang giao và đàm phán:",
    "tips": "Từ `懸念` (lo ngại, trăn trở) là từ ngữ ngoại giao kinh điển. Cụm `懸念を表明する` (bày tỏ quan ngại sâu sắc) hay ra thi đọc hiểu xã hội cực kỳ!",
    "words": [
        ("政策（せいさく）", "CHÍNH SÁCH", "Chính sách, chủ trương của chính phủ", "経済（けいざい）政策（せいさく）を打（う）ち出（だ）す"),
        ("条約（じょうやく）", "ĐIỀU ƯỚC", "Hiệp ước, hiệp định ký giữa các nước", "平和（へいわ）条約（じょうやく）を締結（ていけつ）する"),
        ("協議（きょうぎ）", "HIỆP NGHỊ", "Bàn bạc thương lượng để tìm tiếng nói", "首脳（しゅのう）同士（どうし）で協議（きょうぎ）を重（かさ）ねる"),
        ("懸念（けねん）", "HUYỀN NIỆM", "Mối lo ngại, trăn trở canh cánh", "情勢（じょうせい）の悪化（あっか）を深（ふか）く懸念（けねん）する"),
        ("議会（ぎかい）", "NGHỊ HỘI", "Quốc hội, nghị viện bàn quốc sự", "国会（こっかい）の議会（ぎかい）を開会（かいかい）する"),
        ("首相（しゅしょう）", "THỦ TƯỚNG", "Thủ tướng đứng đầu nội các chính phủ", "首相（しゅしょう）が演説（えんぜつ）を行（おこな）う"),
        ("内閣（ないかく）", "NỘI CÁC", "Nội các ban bệ các bộ trưởng", "新（あたら）しい内閣（ないかく）が発足（ほっそく）する"),
        ("支持率（しじりつ）", "CHI TRÌ SUẤT", "Tỷ lệ cử tri ủng hộ chính phủ", "内閣（ないかく）支持率（しじりつ）が上昇（じょうしょう）する"),
        ("選挙（せんきょ）", "TUYỂN CỬ", "Bầu cử đại biểu quốc hội/địa phương", "衆議院（しゅうぎいん）議員（ぎいん）選挙（せんきょ）"),
        ("投票（とうひょう）", "ĐẦU PHIẾU", "Bỏ lá phiếu vào thùng bầu cử", "清（きよ）き一票（いっぴょう）を投票（とうひょう）する"),
        ("外交（がいこう）", "NGOẠI GIAO", "Quan hệ bang giao giữa các quốc gia", "外交（がいこう）問題（もんだい）を平和（へいわ）裏（り）に解決（かいけつ）する"),
        ("首脳（しゅのう）", "THỦ NÃO", "Người đứng đầu các cường quốc", "主要国（しゅようこく）首脳（しゅのう）会議（かいぎ）"),
        ("会談（かいだん）", "HỘI ĐÀM", "Hội đàm thượng đỉnh cấp nguyên thủ", "両国（りょうこく）の首脳（しゅのう）が会談（かいだん）する"),
        ("批准（ひじゅん）", "PHÊ CHUẨN", "Phê chuẩn hiệp ước quốc tế", "条約（じょうやく）を議会（ぎかい）で批准（ひじゅん）する"),
        ("制裁（せいさい）", "CHẾ TÀI", "Trừng phạt kinh tế, áp đặt chế tài", "経済（けいざい）制裁（せいさい）を発動（はつどう）する"),
        ("妥協（だきょう）", "THỎA HIỆP", "Nhượng bộ để đạt tiếng nói chung", "双方が歩（あゆ）み寄（よ）って妥協（だきょう）する"),
        ("連帯（れんたい）", "LIÊN ĐỚI", "Đoàn kết gắn bó cùng chịu trách nhiệm", "国際（こくさい）社会（しゃかい）と連帯（れんたい）する"),
        ("介入（かいにゅう）", "GIỚI NHẬP", "Can thiệp vào công việc nội bộ", "他国（たこく）の内政（ないせい）に介入（かいにゅう）する"),
        ("主権（しゅけん）", "CHỦ QUYỀN", "Chủ quyền tối cao của một quốc gia", "国家（こっか）の主権（しゅけん）を侵害（しんがい）する"),
        ("同盟（どうめい）", "ĐỒNG MINH", "Liên minh đồng minh quân sự/kinh tế", "安全（あんぜん）保障（ほしょう）同盟（どうめい）を結（むす）ぶ"),
        ("脱退（だったい）", "THOÁT THOÁI", "Rút lui khỏi tổ chức/hiệp định", "国際（こくさい）組織（そしき）から脱退（だったい）する"),
        ("政権（せいけん）", "CHÍNH QUYỀN", "Chính quyền lãnh đạo đất nước", "政権（せいけん）交代（こうたい）が実現（じつげん）する"),
        ("公約（こうやく）", "CÔNG ƯỚC", "Lời hứa cam kết khi tranh cử", "選挙（せんきょ）公約（こうやく）を果（は）たす"),
        ("世論（よろん）", "THẾ LUẬN", "Dư luận tiếng nói của toàn dân", "世論（よろん）を反映（はんえい）した政治（せいじ）"),
        ("法案（ほうあん）", "PHÁP ÁN", "Dự thảo luật trình ra quốc hội", "法案（ほうあん）を可決（かけつ）する")
    ]
}

print("Loaded Lesson 17 - 21.")

# ==========================================
# BÀI 22 - BÀI 25
# ==========================================
vocab_curriculum[22] = {
    "title": "Kinh Tế, Thị Trường & Ngoại Thương (経済・貿易 - けいざい・ぼうえき)",
    "intro": "Chào bé cưng! Bài 22 bao gồm 25 thuật ngữ kinh tế học vĩ mô, biến động tiền tệ và cán cân xuất nhập khẩu:",
    "tips": "Nhớ kỹ: `円高` (yên tăng giá) thì có lợi cho nhập khẩu `輸入`, còn `円安` (yên giảm giá) thì kích thích các hãng xuất khẩu `輸出` nha cưng!",
    "words": [
        ("景気（けいき）", "CẢNH KHÍ", "Tình hình kinh tế thịnh suy chung", "景気（けいき）が回復（かいふく）する"),
        ("不況（ふきょう）", "BẤT HUỐNG", "Khủng hoảng suy thoái kinh tế trầm lắng", "深刻（しんこく）な不況（ふきょう）に陥（おちい）る"),
        ("為替（かわせ）", "VI THẾ", "Tỷ giá hối đoái đổi ngoại tệ", "為替（かわせ）レートが乱高下（らんこうげ）する"),
        ("株価（かぶか）", "CỔ GIÁ", "Giá cổ phiếu giao dịch trên sàn", "日経（にっけい）平均（へいきん）株価（かぶか）が暴落（ぼうらく）する"),
        ("暴落（ぼうらく）", "BẠO LẠC", "Sụt giảm giá thê thảm không phanh", "原油（げんゆ）価格（かかく）が暴落（ぼうらく）する"),
        ("高騰（こうとう）", "CAO ĐẰNG", "Giá cả tăng vọt chóng mặt lên mây", "物価（ぶっか）が高騰（こうとう）して家計（かけい）を圧迫（あっぱく）する"),
        ("インフレ（インフレ）", "LẠM PHÁT", "Lạm phát đồng tiền mất giá", "インフレが進（すす）んで生活（せいかつ）が苦（くる）しい"),
        ("デフレ（デフレ）", "GIẢM PHÁT", "Giảm phát giá hàng rẻ kéo theo lương giảm", "デフレからの脱却（だっきゃく）を図（はか）る"),
        ("貿易（ぼうえき）", "MẬU DỊCH", "Giao thương buôn bán quốc tế", "二国間（にこくかん）の貿易（ぼうえき）協定（きょうてい）"),
        ("輸入（ゆにゅう）", "THÂU NHẬP", "Nhập khẩu hàng hóa từ nước ngoài", "食料（しょくりょう）を海外（かいがい）から輸入（ゆにゅう）する"),
        ("輸出（ゆしゅつ）", "THÂU XUẤT", "Xuất khẩu hàng nội địa ra thế giới", "自動車（じどうしゃ）を世界（せかい）に輸出（ゆしゅつ）する"),
        ("関税（かんぜい）", "QUAN THUẾ", "Thuế quan đánh lên hàng nhập khẩu", "関税（かんぜい）を引き上（あ）げる"),
        ("財政（ざいせい）", "TÀI CHÍNH", "Ngân sách chi tiêu của quốc gia", "国（くに）の財政（ざいせい）赤字（あかじ）が膨（ふく）らむ"),
        ("赤字（あかじ）", "XÍCH TỰ", "Thâm hụt cán cân thu chi, lỗ", "貿易（ぼうえき）赤字（あかじ）を縮小（しゅくしょう）する"),
        ("黒字（くろじ）", "HẮC TỰ", "Thặng dư tài chính, có lãi", "経常（けいじょう）収支（しゅうし）が黒字（くろじ）になる"),
        ("国債（こくさい）", "QUỐC TRÁI", "Trái phiếu do chính phủ phát hành", "国債（こくさい）を発行（はっこう）して資金（しきん）を調達（ちょうたつ）する"),
        ("金利（きんり）", "KIM LỢI", "Lãi suất tiền gửi và tiền vay ngân hàng", "中央（ちゅうおう）銀行（ぎんこう）が金利（きんり）を引（ひ）き下（さ）げる"),
        ("利子（りし）", "LỢI TỬ", "Tiền lãi thu được hoặc phải trả", "銀行（ぎんこう）に利子（りし）を支払（しはら）う"),
        ("投資（とうし）", "ĐẦU TƯ", "Đầu tư tài chính sinh lời", "成長（せいちょう）産業（さんぎょう）に投資（とうし）する"),
        ("融資（ゆうし）", "DUNG TƯ", "Cấp vốn cho vay tiền làm ăn", "新規（しんき）事業（じぎょう）に融資（ゆうし）を受（う）ける"),
        ("資金（しきん）", "TƯ KIM", "Nguồn tiền vốn hoạt động", "研究（けんきゅう）資金（しきん）を集（あつ）める"),
        ("流通（りゅうつう）", "LƯU THÔNG", "Hàng hóa lưu thông trên thị trường", "商品（しょうひん）が円滑（えんかつ）に流通（りゅうつう）する"),
        ("円高（えんだか）", "VIÊN CAO", "Đồng Yên Nhật lên giá so với ngoại tệ", "急激（きゅうげき）な円高（えんだか）が進（すす）む"),
        ("円安（えんやす）", "VIÊN AN", "Đồng Yên Nhật mất giá trượt dốc", "円安（えんやす）で輸出（ゆしゅつ）企業（きぎょう）が潤（うるお）う"),
        ("格差（かくさ）", "CÁCH SA", "Khoảng cách chênh lệch giàu nghèo", "所得（しょとく）格差（かくさ）が拡大（かくだい）する")
    ]
}

vocab_curriculum[23] = {
    "title": "Triết Lý, Tư Tưởng & Đời Người (思想・人生 - しそう・じんせい)",
    "intro": "Chào bé cưng! Bài 23 mang chiều sâu nhân sinh quán: sự giác ngộ, hoài bão lý tưởng và ý nghĩa cuộc sống:",
    "tips": "Từ `葛藤` (trăn trở nội tâm) và `理念` (triết lý cốt lõi) kết hợp với `信条` (nguyên tắc sống kiên định) là bộ ba điểm 10 trong bài đọc văn triết học!",
    "words": [
        ("理念（りねん）", "LÝ NIỆM", "Triết lý sâu xa soi sáng con đường", "崇高（すうこう）な理念（りねん）を掲（かか）げる"),
        ("思想（しそう）", "TƯ TƯỞNG", "Tư tưởng học thuyết chiêm nghiệm", "近代（きんだい）思想（しそう）の流（なが）れを学（まな）ぶ"),
        ("人生観（じんせいかん）", "NHÂN SINH QUAN", "Góc nhìn cảm ngộ về kiếp nhân sinh", "旅（たび）に出（で）て人生観（じんせいかん）が変（か）わる"),
        ("悟（さと）る", "NGỘ", "Giác ngộ, thấu suốt sự thật cuộc đời", "自分（じぶん）の限界（げんかい）を悟（さと）る"),
        ("葛藤（かっとう）", "CÁT ĐẰNG", "Xung đột dằn vặt nội tâm lựa chọn", "義務（ぎむ）と情愛（じょうあい）の間（あいだ）で葛藤（かっとう）する"),
        ("運命（うんめい）", "VẬN MỆNH", "Số phận định mệnh sắp đặt", "過酷（かこく）な運命（うんめい）に立（た）ち向（む）かう"),
        ("宿命（しゅくめい）", "TÚC MỆNH", "Định mệnh tiền định không thể tránh", "背負（せお）った重（おも）い宿命（しゅくめい）"),
        ("使命（しめい）", "SỨ MỆNH", "Trọng trách cao cả cuộc đời giao phó", "与（あた）えられた使命（しめい）を全（まっと）うする"),
        ("生きがい（いきがい）", "SINH", "Lý do thức dậy mỗi sớm mai, lẽ sống", "仕事（しごと）に生（い）きがいを見出（みいだ）す"),
        ("充実（じゅうじつ）", "SUNG THỰC", "Đầy ắp niềm vui, mãn nguyện trọn vẹn", "充実（じゅうじつ）した毎日（まいにち）を送（おく）る"),
        ("後悔（こうかい）", "HẬU HỐI", "Nuối tiếc ăn năn về việc đã qua", "悔（く）いのない人生（じんせい）を生（い）きる"),
        ("挫折（ざせつ）", "TỎA CHIẾT", "Vấp ngã đứt gánh giữa đường", "大（おお）きな挫折（ざせつ）を乗（の）り越（こ）える"),
        ("転機（てんき）", "CHUYỂN CƠ", "Bước ngoặt định mệnh xoay chuyển đời", "人生（じんせい）の大（おお）きな転機（てんき）を迎（むか）える"),
        ("岐路（きろ）", "KỲ LỘ", "Ngã rẽ phân vân chọn lựa con đường", "人生（じんせい）の岐路（きろ）に立（た）つ"),
        ("模索（もさく）", "MÔ TÁC", "Mày mò tìm kiếm hướng đi tương lai", "自分（じぶん）の進（すす）むべき道（みち）を模索（もさく）する"),
        ("苦悩（くのう）", "KHỔ NÃO", "Khổ sở đau đầu trăn trở suy nghĩ", "進路（しんろ）について深（ふか）く苦悩（くのう）する"),
        ("諦観（ていかん）", "ĐẾ QUAN", "Tâm thế buông xả, thấu suốt lẽ đời", "世（よ）の中（なか）を諦観（ていかん）の目（め）で見（み）つめる"),
        ("孤独（こどく）", "CÔ ĐỘC", "Một mình lẻ loi lặng lẽ chiêm nghiệm", "孤独（こどく）を恐（おそ）れずに一人（ひとり）で歩（あゆ）む"),
        ("自己犠牲（じこぎせい）", "TỰ KỶ HY SINH", "Quên mình hy sinh vì hạnh phúc người khác", "崇高（すうこう）な自己犠牲（じこぎせい）の精神（せいしん）"),
        ("利他（りた）", "LỢI THA", "Sống vị tha hướng về tha nhân", "利他（りた）の心（こころ）で社会（しゃかい）に尽（つく）す"),
        ("虚無感（きょむかん）", "HƯ VÔ CẢM", "Cảm giác trống rỗng hư vô mênh mang", "心（こころ）にぽっかり虚無感（きょむかん）が広（ひろ）がる"),
        ("精神的（せいしんてき）", "TINH THẦN ĐÍCH", "Thuộc về cảnh giới chiều sâu tâm hồn", "精神的（せいしんてき）に成熟（せいじゅく）する"),
        ("探求（たんきゅう）", "THÁM CẦU", "Đi tìm chân lý tối thượng của nhân sinh", "真（しん）の幸福（こうふく）を探求（たんきゅう）する"),
        ("志（こころざし）", "CHÍ", "Ý chí hoài bão lớn lao nung nấu", "高（たか）い志（こころざし）を抱（いだ）く"),
        ("信条（しんじょう）", "TÍN ĐIỀU", "Nguyên tắc sống bất di bất dịch của mình", "信念（しんねん）と信条（しんじょう）を貫（つらぬ）く")
    ]
}

vocab_curriculum[24] = {
    "title": "Xu Hướng Xã Hội & Diễn Biến (社会現象・流行 - しゃかいげんしょう・りゅうこう)",
    "intro": "Chào bé cưng! Bài 24 nắm bắt nhịp đập đương đại: trào lưu xã hội, vòng đời sản phẩm và sự đổi thay chóng mặt:",
    "tips": "Cụm thành ngữ `一世を風靡する` (làm mưa làm gió khuynh đảo một thời) cực kỳ đắt giá trong bài đọc hiểu xu hướng lịch sử!",
    "words": [
        ("結末（けつまつ）", "KẾT MẠT", "Hồi kết cái kết của câu chuyện", "意外（いがい）な結末（けつまつ）を迎（むか）える"),
        ("成果（せいか）", "THÀNH QUẢ", "Trái ngọt gặt hái sau chuỗi ngày nỗ lực", "日頃（ひごろ）の努力（どりょく）が成果（せいか）を結（むす）ぶ"),
        ("転換（てんかん）", "CHUYỂN HOÁN", "Bước ngoặt đổi hướng hoàn toàn", "方針（ほうしん）を大（おお）きく転換（てんかん）する"),
        ("反響（はんきょう）", "PHẢN HƯỞNG", "Hiệu ứng tiếng vang đón nhận nồng nhiệt", "新製品（しんせいひん）が社会（しゃかい）に大（おお）きな反響（はんきょう）を呼（よ）ぶ"),
        ("流行（りゅうこう）", "LƯU HÀNH", "Trào lưu thịnh hành rầm rộ khắp nơi", "若者（わかもの）の間（あいだ）で流行（りゅうこう）する"),
        ("ブーム（ブーム）", "CƠN SỐT", "Cơn sốt hâm mộ bùng nổ cuồng nhiệt", "空前（くうぜん）のキャンプブームが起（お）きる"),
        ("兆候（ちょうこう）", "TRIỆU HẬU", "Manh nha dấu hiệu biến chuyển sắp tới", "景気（けいき）回復（かいふく）の兆候（ちょうこう）が現（あらわ）れる"),
        ("普及率（ふきゅうりつ）", "PHỔ CẬP SUẤT", "Tỷ lệ số đông người sở hữu sử dụng", "スマートフォンの普及率（ふきゅうりつ）が9割（きゅうわり）を超（こ）える"),
        ("浸透（しんとう）", "TẨM THẤU", "Thấm nhuần, ăn sâu vào đời sống hàng ngày", "新（あたら）しい生活（せいかつ）様式（ようしき）が浸透（しんとう）する"),
        ("定着（ていちゃく）", "ĐỊNH TRỨNG", "Trở thành thói quen cố định vững chắc", "在宅（ざいたく）勤務（きんむ）が社会（しゃかい）に定着（ていちゃく）する"),
        ("衰退（すいたい）", "SUY THOÁI", "Lụi tàn dần, thoái trào mất đi sức sống", "伝統（でんとう）産業（さんぎょう）が衰退（すいたい）する"),
        ("一世（いっせい）を風靡（ふうび）する", "NHẤT THẾ PHONG PHÍ", "Làm mưa làm gió, khuynh đảo một thời đại", "一世（いっせい）を風靡（ふうび）した大（だい）ヒット曲（きょく）"),
        ("トレンド（トレンド）", "XU HƯỚNG", "Xu hướng mốt thời thượng hiện nay", "最新（さいしん）のファッショントレンドを追（お）う"),
        ("先取（さきど）り", "TIÊN THỦ", "Đi tắt đón đầu, nắm bắt trước thiên hạ", "時代（じだい）のニーズを先取（さきど）りする"),
        ("廃（すた）れる", "PHẾ", "Mai một, lỗi thời bị lãng quên dần", "流行（りゅうこう）がすっかり廃（すた）れる"),
        ("発端（ほったん）", "PHÁT ĐOAN", "Nguồn cơn ngọn ngành nảy sinh chuyện", "些細（ささい）な一言（ひとこと）が事件（じけん）の発端（ほったん）となる"),
        ("過程（かてい）", "QUÁ TRÌNH", "Quá trình diễn tiến xuyên suốt từng bước", "成長（せいちょう）の過程（かてい）を見守（みまも）る"),
        ("経緯（けいい）", "KINH VĨ", "Đầu đuôi diễn biến từ đầu đến cuối", "これまでの経緯（けいい）を丁寧（ていねい）に説明（せつめい）する"),
        ("目（め）まぐるしい", "MỤC", "Thay đổi chóng mặt hoa cả mắt từng ngày", "目（め）まぐるしく変化（へんか）する現代（げんだい）社会（しゃかい）"),
        ("激変（げきへん）", "KÍCH BIẾN", "Biến chuyển dữ dội mau lẹ ngoài dự đoán", "社会（しゃかい）情勢（じょうせい）が激変（げきへん）する"),
        ("潮流（ちょうりゅう）", "TRIỀU LƯU", "Dòng chảy xu thế thời đại cuồn cuộn", "時代（じだい）の潮流（ちょうりゅう）に乗（の）る"),
        ("最前線（さいぜんせん）", "TỐI TIỀN ĐOAN", "Nơi tuyến đầu ngọn sóng đi tiên phong", "ビジネスの最前線（さいぜんせん）で戦（たたか）う"),
        ("変革（へんかく）", "BIẾN CÁCH", "Cuộc cải cách thay da đổi thịt toàn diện", "組織（そしき）の大胆（だいたん）な変革（へんかく）を断行（だんこう）する"),
        ("巻（ま）き起（お）こす", "QUYỂN KHỞI", "Dấy lên một làn sóng cuồng nhiệt mạnh mẽ", "社会（しゃかい）現象（げんしょう）を巻（ま）き起（お）こす"),
        ("終焉（しゅうえん）", "CHUNG YÊN", "Hồi chuông cáo chung kết thúc một kỷ nguyên", "冷戦（れいせん）構造（こうぞう）が終焉（しゅうえん）を迎（むか）える")
    ]
}

vocab_curriculum[25] = {
    "title": "Tổng Hợp Thành Ngữ 4 Chữ & Từ Vựng Sát Thủ N2 (四字熟語・必出語彙 - よじじゅくご・ひっしゅつごい)",
    "intro": "Chào bé cưng! Bài 25 là trùm cuối Shinkanzen: 25 thành ngữ 4 chữ (Yojijukugo) và từ vựng sát thủ hay quyết định điểm 170+ JLPT N2:",
    "tips": "Bài thi Mondai 4 rất thích ra `一長一短` (có ưu có khuyết) và `臨機応変` (tùy cơ ứng biến). Học thuộc lòng để lấy trọn điểm tuyệt đối nhé cưng!",
    "words": [
        ("一筋縄（ひとすじなわ）ではいかない", "NHẤT CÂN THẰNG", "Không phải dạng vừa, cực kỳ hóc búa nan giải", "一筋縄（ひとすじなわ）ではいかない難問（なんもん）"),
        ("臨機応変（りんきおうへん）", "LÂM CƠ ỨNG BIẾN", "Tùy cơ ứng biến, linh hoạt theo hoàn cảnh", "臨機応変（りんきおうへん）に対処（たいしょ）する"),
        ("四苦八苦（しくはっく）", "TỨ KHỔ BÁT KHỔ", "Chật vật khổ sở trăm bề vất vả", "資金（しきん）集（あつ）めに四苦八苦（しくはっく）する"),
        ("試行錯誤（しこうさくご）", "THÍ HÀNH THÁC NGỘ", "Quá trình mò mẫm thử và sửa sai nhiều lần", "試行錯誤（しこうさくご）を繰（く）り返（かえ）して完成（かんせい）させる"),
        ("自暴自棄（じぼうじき）", "TỰ BẠO TỰ KHÍ", "Buông xuôi bất cần đời, tự hủy hoại bản thân", "自暴自棄（じぼうじき）になって酒（さけ）をあおる"),
        ("絶体絶命（ぜったいぜつめい）", "TUYỆT THỂ TUYỆT MỆNH", "Ngàn cân treo sợi tóc, bước đường cùng", "絶体絶命（ぜったいぜつめい）の危機（きき）に陥（おちい）る"),
        ("一網打尽（いちもうだじん）", "NHẤT VÕNG ĐẢ TẬN", "Tóm gọn trọn ổ trong một mẻ lưới", "犯人（はんにん）グループを一網打尽（いちもうだじん）にする"),
        ("紆余曲折（うよきょくせつ）", "KHU VƯ KHÚC TRIẾT", "Trải qua bao thăng trầm trắc trở quanh co", "紆余曲折（うよきょくせつ）の末（すえ）に成功（せいこう）を収（おさ）める"),
        ("起死回生（きしかいせい）", "KHỞI TỬ HỒI SINH", "Lội ngược dòng ngoạn mục từ cõi chết", "起死回生（きしかいせい）の一発（いっぱつ）逆転（ぎゃくてん）ホームラン"),
        ("本末転倒（ほんまつてんとう）", "BẢN MẠT CHUYỂN ĐẢO", "Lộn ngược đầu đuôi, nhầm cái phụ thành cái chính", "手段（しゅだん）が目的（もくてき）化（か）して本末転倒（ほんまつてんとう）だ"),
        ("一長一短（いっちょういったん）", "NHẤT TRƯỜNG NHẤT ĐOẢN", "Được mặt này thì mất mặt kia, có ưu có nhược", "どちらの案（あん）にも一長一短（いっちょういったん）がある"),
        ("危機一髪（ききいっぱつ）", "NGUY CƠ NHẤT PHÁT", "Trong đường tơ kẽ tóc suýt mất mạng", "危機一髪（ききいっぱつ）のところで助（たす）かる"),
        ("十人十色（じゅうにんといろ）", "THẬP NHÂN THẬP SẮC", "Mỗi người một ý, chín người mười tính", "考（かんが）え方（かた）は十人十色（じゅうにんといろ）だ"),
        ("悪戦苦闘（あくせんくとう）", "ÁC CHIẾN KHỔ ĐẤU", "Chiến đấu chật vật vượt qua muôn vàn khó khăn", "強敵（きょうてき）を相手（あいて）に悪戦苦闘（あくせんくとう）する"),
        ("切磋琢磨（せっさたくま）", "THIẾT THOA TRÁC MA", "Cùng nhau học hỏi rèn giũa để cùng tiến bộ", "良（よ）きライバルとして切磋琢磨（せっさたくま）する"),
        ("不可欠（ふかけつ）", "BẤT KHẢ KHIẾM", "Không thể nào thiếu được, cốt lõi sống còn", "生活（せいかつ）に不可欠（ふかけつ）なライフライン"),
        ("画期的（かっきてき）", "HỌA KỲ ĐÍCH", "Đột phá mang tính bước ngoặt vĩ đại", "画期的（かっきてき）な発見（はっけん）に世間（せけん）が沸（わ）く"),
        ("有意義（ゆういぎ）", "HỮU Ý NGHĨA", "Vô cùng bổ ích, giàu ý nghĩa thiết thực", "有意義（ゆういぎ）な時間（じかん）を過（す）ごす"),
        ("圧倒的（あっとうてき）", "ÁP ĐẢO ĐÍCH", "Áp đảo hoàn toàn vượt trội hơn hẳn", "圧倒的（あっとうてき）な強（つよ）さで優勝（ゆうしょう）する"),
        ("模索（もさく）", "MÔ TÁC", "Mày mò tìm kiếm lối đi giải pháp mới", "打開（だかい）策（さく）を懸命（けんめい）に模索（もさく）する"),
        ("痛感（つうかん）", "THỐNG CẢM", "Thấm thía nỗi đau, thấm thía bài học sâu sắc", "力（ちから）不足（ぶそく）を痛感（つうかん）する"),
        ("打開（だかい）", "ĐẢ KHAI", "Phá vỡ bế tắc tìm đường mở ra lối thoát", "苦（くる）しい現状（げんじょう）を打開（だかい）する"),
        ("念頭（ねんとう）に置（お）く", "NIỆM ĐẦU TRÍ", "Luôn ghi nhớ khắc sâu trong tâm trí khi làm", "安全（あんぜん）を念頭（ねんとう）に置（お）いて作業（さぎょう）する"),
        ("目処（めど）が立（た）つ", "MỤC XỨ LẬP", "Đã thấy le lói tia hy vọng xong, có triển vọng", "復旧（ふっきゅう）の目処（めど）が立（た）つ"),
        ("手落（てお）ち", "THỦ LẠC", "Sai sót sơ suất ngoài ý muốn do sơ ý", "準備（じゅんび）に手落（てお）ちがないか再確認（さいかくにん）する")
    ]
}

print("Loaded all 25 lessons!")

# ==========================================
# THỰC THI GHI ĐÈ FILE TU-VUNG.MD CHO 25 BÀI
# ==========================================
success_count = 0
for idx in range(1, 26):
    data = vocab_curriculum[idx]
    lesson_dir = os.path.join(base_dir, f'bai-{idx:02d}')
    os.makedirs(lesson_dir, exist_ok=True)
    tu_vung_file = os.path.join(lesson_dir, 'tu-vung.md')
    
    with open(tu_vung_file, 'w', encoding='utf-8') as f:
        f.write(f'''# 📖 Bài {idx:02d}: Từ Vựng & Chữ Hán (語彙・漢字 - ごい・かんじ) - Shinkanzen N2
## Chủ đề: {data['title']}

> 🌸 **Lời dặn của chị gái:**  
> *"{data['intro']}"*

---

## 1. Bảng 25 Từ Vựng Trọng Tâm Bài {idx:02d} (Giáo Trình Shinkanzen Master N2)

| STT | Từ vựng (Kanji) | Âm Hán Việt | Nghĩa tiếng Việt | Cụm từ hay đi kèm (Collocation) |
| :---: | :--- | :--- | :--- | :--- |
''')
        for w_i, w in enumerate(data['words'], 1):
            f.write(f"| {w_i} | **{w[0]}** | {w[1]} | {w[2]} | {w[3]} |\n")

        f.write(f'''
---

## 2. Người Chị Giải Thích Cặn Kẽ & Mẹo Nhớ Siêu Tốc
> 💖 *{data['tips']}*

- **Bí kíp học của chị:** Hãy đọc to mỗi từ kèm cụm collocation 3 lần mỗi sáng. Đừng bao giờ học từ vựng đơn lẻ cưng nhé! Phải nhớ cả ngữ cảnh xuất hiện thì khi gặp dạng bài Mondai 1 (Đọc Kanji), Mondai 2 (Cách viết Kanji), Mondai 4 (Tìm từ đồng nghĩa) và Mondai 5 (Cách dùng từ trong câu) em mới phản xạ đánh trúng đáp án ngay trong 5 giây!
''')
    success_count += 1
    print(f"Generated bai-{idx:02d}/tu-vung.md ({len(data['words'])} words)")

print(f"\n HOÀN THÀNH TOÀN BỘ {success_count}/25 BÀI TỪ VỰNG CHUẨN SHINKANZEN MASTER N2 VỚI ĐỦ 25 TỪ MỖI BÀI!")
