#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pentanihon Daily Story Generator - Series Engine
Bộ máy tự động xuất bản câu chuyện dài tập Nhật ngữ:
「東京（とうきょう）あおぞら物語（ものがたり）〜レンと姉（あね）ユキの夢（ゆめ）ノート〜」
"""
import os
import glob
import re

WORKSPACE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STORY_DIR = os.path.join(WORKSPACE_DIR, 'story')

# Ngân hàng các tập tiếp theo của Series cốt truyện liên hoàn
SERIES_EPISODES = {
    8: {
        "filename": "series-01_tap-08_phong_van_ban_giam_doc.md",
        "title_jp": "役員（やくいん）面接（めんせつ）と青空（あおぞら）の誓（ちか）い",
        "title_vi": "Phỏng Vấn Ban Giám Đốc & Lời Thề Dưới Bầu Trời Xanh",
        "summary_prev": "Sau khi dốc toàn bộ sức lực hoàn thành kỳ thi JLPT N2 vào đầu tháng 12, Ren nhận được cuộc gọi đặc cách bước vào vòng phỏng vấn Ban Điều Hành cuối cùng tại tập đoàn Mirai Technology.",
        "grammar_points": ["〜を込めて", "〜に相違ない", "〜のみならず", "〜かねない"],
        "content_jp": """冷（つめ）たい冬（ふゆ）の風（かぜ）が吹き抜（ふきぬ）ける秋葉原（あきはばら）。ミライ・テクノロジー本社（ほんしゃ）の最上階（さいじょうかい）の役員（やくいん）室（しつ）で、レンは最終（さいしゅう）決戦（けっせん）の椅子（いす）に座（すわ）っていた。

正面（しょうめん）に座（すわ）るのは、創業者（そうぎょうしゃ）であり現社長（げんしゃちょう）の佐藤（さとう）氏（し）だ。彼（かれ）の鋭（するど）い視線（しせん）は、レンの内面（ないめん）の深（ふか）いところまで見透（みす）かしているかのようだった。

「レンさん、君（きみ）が技術（ぎじゅつ）に優（すぐ）れていることは、松田（まつだ）部長（ぶちょう）からも聞（き）いている。だが、プロのエンジニアにとって技術（ぎじゅつ）は基礎（きそ）**のみならず**、お客様（きゃくさま）の心（こころ）に寄（よ）り添（そ）う人間性（にんげんせい）こそが命（いのち）だ。自分（じぶん）の技術（ぎじゅつ）に過信（かしん）すれば、重大（じゅうだい）な事故（じこ）を引（ひ）き起（お）こし**かねない**」

佐藤（さとう）社長（しゃちょう）の重厚（じゅうこう）な言葉（ことば）に、レンは神保町（じんぼうちょう）で学（まな）んだ全（すべ）てを思（おも）い出（だ）した。

「社長（しゃちょう）、おっしゃる通（とお）りです。私（わたし）にとってコードを書（か）くことは、単（たん）なる仕事（しごと）ではなく、使（つか）う人（ひと）への感謝（かんしゃ）と願（ねが）い**を込（こ）めて**届（とど）ける手紙（てがみ）のようなものです。言葉（ことば）や文化（ぶんか）の違（ちが）いを超（こ）えて、人々（ひとびと）の暮（く）らしを温（あたた）かく支（ささ）えるシステムを作（つく）りたいのです」

その言葉（ことば）を聞（き）いた瞬間（しゅんかん）、佐藤（さとう）社長（しゃちょう）の厳（きび）しい表情（ひょうじょう）が和（やわ）らぎ、静（しず）かに笑（え）みが浮（う）かんだ。

「その情熱（じょうねつ）があれば、君（きみ）が素晴（すば）らしいエンジニアへと成長（せいちょう）することは間違（まちが）いなく、成功（せいこう）するに**相違（そうい）ない**。良（よ）い返事（へんじ）を待（ま）っていてください」

応接室（おうせつしつ）を出（で）たレンの目（め）の前（まえ）には、雲（くも）ひとつない澄（す）み渡（わた）った東京（とうきょう）の青空（あおぞら）がどこまでも広（ひろ）がっていた。""",
        "content_vi": """Những cơn gió đông buốt giá lùa qua các góc phố Akihabara. Tại phòng Ban Điều Hành trên tầng cao nhất của tập đoàn Mirai Technology, Ren đang ngồi trước chiếc bàn phỏng vấn quyết định số phận.

Ngồi đối diện cậu là ngài Sato — người sáng lập kiêm Tổng Giám Đốc tập đoàn. Ánh mắt sâu thẳm của vị thuyền trưởng dường như thấu suốt mọi ngóc ngách trong suy nghĩ của chàng trai trẻ.

"Anh Ren này, kỹ năng lập trình của cậu xuất sắc ra sao, tôi đã nghe Trưởng phòng Matsuda báo cáo lại rồi. Thế nhưng đối với một kỹ sư chuyên nghiệp, kỹ thuật không chỉ là nền tảng duy nhất, mà cốt lõi sinh mệnh chính là nhân cách và sự thấu cảm nỗi đau của khách hàng. Nếu chỉ tự mãn vào chuyên môn của mình, ta rất có thể sẽ gây ra những thảm họa hệ thống nghiêm trọng."

Lắng nghe những lời tâm huyết sâu sắc của vị Tổng Giám Đốc, Ren nhớ lại tất cả những gì cậu đã chắt chiu tại khu phố sách Jimbocho:

"Thưa Tổng Giám Đốc, đúng như những gì ngài vừa răn dạy ạ. Đối với cháu, việc viết mã phần mềm không đơn thuần là một công việc kiếm sống, mà giống như một lá thư mang theo trọn vẹn sự biết ơn và mong ước tốt đẹp gửi gắm đến người dùng. Cháu muốn vượt qua rào cản ngôn ngữ và sự khác biệt văn hóa để kiến tạo nên những hệ thống nâng đỡ và sưởi ấm cuộc sống con người."

Khoảnh khắc lắng nghe những lời tự đáy lòng ấy, nét mặt nghiêm nghị của Tổng Giám Đốc Sato bỗng giãn ra, một nụ cười ấm áp xuất hiện:

"Với ngọn lửa đam mê chân chính ấy, tôi tin chắc rằng cậu sẽ trưởng thành thành một kỹ sư xuất chúng, điều đó chắc chắn không còn nghi ngờ gì nữa. Hãy đợi tin mừng từ chúng tôi nhé."

Rời khỏi phòng phỏng vấn, hiện ra trước mắt Ren là một bầu trời Tokyo xanh ngắt không một gợn mây, trải dài bất tận như tương lai đang vẫy gọi.""",
        "grammar_analysis": """### 1. `〜を込（こ）めて`
- **Câu trong tập:** `感謝（かんしゃ）と願（ねが）いを込（こ）めて届（とど）ける`
- **Ý nghĩa:** "Gửi gắm trọn vẹn tấm lòng / tình cảm / ước nguyện vào trong hành động".

### 2. `〜に相違（そうい）ない`
- **Câu trong tập:** `成功（せいこう）するに相違（そうい）ない`
- **Ý nghĩa:** "Chắc chắn là... không còn nghi ngờ gì nữa" (Cách nói trang trọng, khẳng định tuyệt đối).

### 3. `〜のみならず`
- **Câu trong tập:** `技術（ぎじゅつ）は基礎（きそ）のみならず...`
- **Ý nghĩa:** "Không chỉ A mà còn cả B nữa" (Văn viết trang trọng, tương đương với `だけでなく`).

### 4. `〜かねない`
- **Câu trong tập:** `事故（じこ）を引（ひ）き起（お）こしかねない`
- **Ý nghĩa:** "Rất có thể sẽ dẫn tới hậu quả tiêu cực" (Cảnh báo nguy cơ xấu có thể xảy ra).""",
        "vocab_notes": """- **見透（みす）かす (KIẾN THẤU):** Nhìn thấu tâm can, nhìn xuyên qua vẻ bề ngoài.
- **過信（かしん - QUÁ TÍN):** Quá tự tin, kiêu ngạo vào năng lực bản thân.
- **寄（よ）り添（そ）う (KÝ THIÊM):** Ở bên cạnh đồng cảm, thấu hiểu và sẻ chia.
- **澄（す）み渡（わた）る (TRỪNG ĐỘ):** Trong veo, xanh ngắt không một gợn mây.""",
        "questions": [
            ("佐藤社長がプロのエンジニアにとって最も重要だと考えている要素は何か。",
             ["誰よりも速くコードを書くスピード。",
              "技術力だけでなく、使う人の心に寄り添う温かい人間性。",
              "海外の有名大学の卒業資格。",
              "競合他社の欠点を見つけ出す能力。"], 2),
            ("レンが「コードを書くこと」を何に例えて社長に伝えたか。",
             ["お金を稼ぐための単なる作業道具。",
              "使い手への感謝と願いを込めて届ける手紙のようなもの。",
              "誰にも負けない自分だけの武器。",
              "大学の卒業証書。"], 2)
        ],
        "sister_message": "Chân thành chính là vũ khí mạnh nhất trong mọi cuộc phỏng vấn bé cưng nhé! Hãy luôn giữ trái tim ấm áp khi làm việc nha! 🌸",
        "next_preview": "Một tuần sau buổi phỏng vấn định mệnh, hòm thư của Ren đồng loạt nhận được 2 phong bì thư đặc biệt: một từ Hiệp hội JLPT và một từ Tập đoàn Mirai Technology! Liệu điều kỳ diệu có đến? Đón đọc Tập 09 nhé!"
    },
    9: {
        "filename": "series-01_tap-09_giay_bao_do_va_naitei.md",
        "title_jp": "合格（ごうかく）通知（つうち）と涙（なみだ）の内定（ないてい）",
        "title_vi": "Giấy Báo Đỗ & Nước Mắt Ngày Nhận Naitei",
        "summary_prev": "Sau buổi phỏng vấn đầy xúc động với Tổng Giám Đốc Sato, Ren hồi hộp đếm từng ngày chờ đợi kết quả kép: điểm thi JLPT N2 và thông báo tuyển dụng.",
        "grammar_points": ["〜にほかならない", "〜やまない", "〜からには", "〜に違いない"],
        "content_jp": """郵便（ゆうびん）配達（はいたつ）のバイクの音（おと）が神保町（じんぼうちょう）の路地（ろじ）に響（ひび）いた。

「レン君（くん）！ 届（とど）いたよ！」

ユキ姉（ねえ）が息（いき）を切（き）らして二通（につう）の封筒（ふうとう）をカフェのテーブルに並（なら）べた。一通（いっつう）は日本（にほん）国際（こくさい）教育（きょういく）支援（しえん）協会（きょうかい）からの合否（ごうひ）結果（けっか）通知（つうち）書（しょ）。そしてもう一通（いっつう）は、ミライ・テクノロジーからの親展（しんてん）郵便（ゆうびん）だった。

奥（おく）の席（せき）から田中（たなか）さんも眼鏡（めがね）を外（はず）して見守（みまも）り、スマホの通話（つうわ）の向（む）こうではアオイも固唾（かたず）を呑（の）んでいた。

震（ふる）える指先（ゆびさき）で、まずはJLPTの封（ふう）を切（き）る。

【判定：合格（ごうかく）　得点：168／180点】

「……受（う）かった……！ 合格（ごうかく）だ！」

レンの叫（さけ）び声（ごえ）に、ユキ姉（ねえ）が両手（りょうて）を叩（たた）いて喜（よろこ）んだ。  
そして、二通（につう）目（め）の封筒（ふうとう）を慎重（しんちょう）に開（ひら）く。中（なか）から現（あらわ）れたのは、重（おも）みのある『採用（さいよう）内定（ないてい）通知（つうち）書（しょ）』だった。

『貴殿（きでん）の熱意（ねつい）と誠実（せいじつ）な姿勢（しせい）を高（たか）く評価（ひょうか）し、正社員（せいしゃいん）として採用（さいよう）内定（ないてい）いたします』

その文字（もじ）を読（よ）んだ瞬間（しゅんかん）、レンの目（め）から大粒（おおつぶ）の涙（なみだ）が机（つくえ）の夢（ゆめ）ノートへとこぼれ落（お）ちた。

「おめでとう、レン……！本当（ほんとう）によく頑張（がんば）ったわね！」

ユキ姉（ねえ）がレンの背中（せなか）を抱（だ）きしめ、田中（たなか）さんも目頭（めがしら）を押（お）さえている。

「この結果（けっか）はね、君（きみ）が流（なが）した汗（あせ）と涙（なみだ）の結晶（けっしょう）**にほかならない**よ。日本（にほん）でプロとして歩（あゆ）む**からには**、これからが本当（ほんとう）の勝負（しょうぶ）だが、君（きみ）の未来（みらい）の成功（せいこう）を祈（いの）って**やまない**よ」

田中（たなか）さんの言葉（ことば）に、レンは涙（なみだ）を拭（ぬぐ）って力強（ちからづよ）く頷（うなず）いた。東京（とうきょう）の街（まち）に、彼（かれ）の夢（ゆめ）の花（はな）が確（たし）かに咲（さ）き誇（ほこ）った瞬間（しゅんかん）だった。""",
        "content_vi": """Tiếng xe máy của nhân viên bưu điện vang lên rộn rã đầu con ngõ phố Jimbocho.

"Ren ơi! Thư đến rồi này em!"

Chị Yuki thở hổn hển đặt hai phong bì thư trang trọng lên bàn cà phê. Một chiếc là giấy báo kết quả thi từ Hiệp hội Hỗ trợ Giáo dục Quốc tế Nhật Bản (JLPT). Và chiếc còn lại là thư bảo mật gửi từ Tập đoàn Mirai Technology.

Từ phía góc quán, bác Tanaka cũng tháo kính chăm chú dõi theo, đầu dây bên kia điện thoại cô bạn Aoi cũng đang nín thở chờ đợi.

Đầu ngón tay run run xé chiếc phong bì đầu tiên:

【Kết quả: ĐỖ (合格) — Điểm số: 168 / 180 điểm】

"...Đỗ rồi...! Em đỗ N2 rồi chị ơi!"

Tiếng reo hò của Ren làm chị Yuki vỡ òa vỗ tay mừng rỡ.  
Tiếp đó, cậu cẩn thận bóc chiếc phong bì thứ hai. Tấm giấy bên trong hiện ra dòng chữ dập nổi: 'THÔNG BÁO TRÚNG TUYỂN CHÍNH THỨC (採用内定通知書)'.

'Chúng tôi đánh giá rất cao nhiệt huyết và sự chân thành của anh, trân trọng thông báo tiếp nhận anh làm nhân viên chính thức của tập đoàn'.

Khoảnh khắc đọc từng dòng chữ ấy, những giọt nước mắt nóng hổi lăn dài trên má Ren, rơi xuống trang giấy của 'Quyển Sổ Ước Mơ'.

"Chúc mừng em, Ren...! Em đã nỗ lực tuyệt vời lắm rồi!"

Chị Yuki ôm chầm lấy cậu em trai, bác Tanaka bên cạnh cũng khẽ chấm khóe mắt rưng rưng:

"Trái ngọt ngày hôm nay chính là kết tinh từ mồ hôi và những đêm thức trắng của cháu chứ không đâu khác. Một khi đã dấn thân bước đi như một kỹ sư chuyên nghiệp tại Nhật Bản, phía trước mới là chiến trường thực thụ, nhưng bác luôn cầu chúc không ngừng cho tương lai rực rỡ của cháu!"

Lau khô những giọt nước mắt hạnh phúc, Ren gật đầu kiên định. Dưới bầu trời Tokyo, bông hoa ước mơ đầu tiên của cậu đã kiêu hãnh bung nở rạng ngời.""",
        "grammar_analysis": """### 1. `〜からには`
- **Câu trong tập:** `プロとして歩（あゆ）むからには、これからが本当（ほんとう）の勝負（しょうぶ）だ`
- **Ý nghĩa:** "Một khi đã... thì nhất định phải..." (Biểu thị quyết tâm hoặc trách nhiệm tất yếu một khi đã lựa chọn).

### 2. `〜てやまない`
- **Câu trong tập:** `未来（みらい）の成功（せいこう）を祈（いの）ってやまない`
- **Ý nghĩa:** "Luôn luôn / Không ngừng... từ tận đáy lòng" (Diễn tả tình cảm, lời chúc phúc sâu sắc, thiết tha).

### 3. `〜にほかならない`
- **Câu trong tập:** `汗（あせ）と涙（なみだ）の結晶（けっしょう）にほかならない`
- **Ý nghĩa:** "Chính là / Không gì khác ngoài..." (Khẳng định đanh thép bản chất nguyên nhân thành quả).

### 4. `〜に違（ちが）いない`
- **Câu trong tập:** *(Ôn tập)* `喜（よろこ）んでいるに違（ちが）いない`
- **Ý nghĩa:** "Chắc chắn là đang vui sướng khôn xiết".""",
        "vocab_notes": """- **固唾（かたず）を呑（の）む (CỐ THOA THÔN):** Nín thở hồi hộp theo dõi tình huống gay cấn.
- **結晶（けっしょう - KẾT TINH):** Kết tinh, thành quả ngọt ngào đúc kết sau nỗ lực.
- **目頭（めがしら）を押（お）さえる:** Lấy tay chấm khóe mắt vì quá xúc động rơi lệ.
- **勝負（しょうぶ - THẮNG PHỤ):** Cuộc chiến thực sự, thử thách quyết định.""",
        "questions": [
            ("レンが手に入れた2つの大きな成果は何か。",
             ["JLPT N1合格と大学院の推薦入学。",
              "JLPT N2高得点合格（168点）と志望IT企業からの正社員内定。",
              "カフェの店長就任と日本語学校の奨学金。",
              "アルバイトの時給アップと新しいアパートの契約。"], 2),
            ("田中さんが「〜祈ってやまない」という表現を使って伝えた気持ちはどれか。",
             ["レンが日本を離れて帰国してしまうことへの心配。",
              "プロとして歩み出すレンの輝かしい未来に対する、心からの深い祝福と応援。",
              "カフェの家賃を早く払ってほしいという要求。",
              "もう二度と勉強しなくていいという安堵感。"], 2)
        ],
        "sister_message": "Mọi nỗ lực chân chính đều sẽ nở hoa bé cưng ơi! Cầm trên tay tấm vé Naitei, cánh cửa Tokyo thực sự đã mở ra rồi nhé! 🌸",
        "next_preview": "Mùa xuân gõ cửa. Ren chính thức khoác ba lô bước vào ngày đầu tiên đi làm tại văn phòng Akihabara. Những quy tắc công sở khắt khe như văn hóa trao đổi danh thiếp (名刺交換) và báo cáo Ho-Ren-So sẽ thử thách cậu ra sao? Đón đọc Tập 10 nhé!"
    },
    10: {
        "filename": "series-01_tap-10_ngay_dau_tien_di_lam.md",
        "title_jp": "初（はつ）出社（しゅっしゃ）の緊張（きんちょう）と最初（さいしょ）の壁（かべ）",
        "title_vi": "Ngày Đầu Tiên Đi Làm & Bức Tường Thử Thách",
        "summary_prev": "Nhận được chứng chỉ N2 và giấy trúng tuyển chính thức, Ren chia tay chuỗi ngày hồi hộp xin việc để chuẩn bị bước vào cuộc sống của một nhân viên công sở Nhật Bản thực thụ.",
        "grammar_points": ["〜にあたって", "〜まい", "〜一方（で）", "〜ざるを得ない"],
        "content_jp": """四月（しがつ）の朝（あさ）、満開（まんかい）の桜（さくら）が風（かぜ）に舞（ま）い散（ち）る中（なか）、レンは新（あたら）しいスーツに身（み）を包（つつ）み、秋葉原（あきはばら）のオフィスビルの自動（じどう）ドアをくぐった。

今日（きょう）からミライ・テクノロジーの開発（かいはつ）第（だい）一チームの一員（いちいん）として、社会（しゃかい）人（じん）生活（せいかつ）が始（はじ）まるのだ。

「新（あたら）しい人生（じんせい）のスタートを切（き）る**にあたって**、先輩（せんぱい）への挨拶（あいさつ）と報連相（ほうれんそう）だけは徹底（てってい）しなさいよ」

出（で）がけにユキ姉（ねえ）がネクタイを直（なお）しながら言（い）ってくれた言葉（ことば）が、胸（むね）に響（ひび）いていた。

「おはようございます！ 今日（きょう）から配属（はいぞく）になりましたレンと申（もう）します。よろしくお願（ねが）いいたします！」

フロア全員（ぜんいん）に向（む）けて深々（ふかぶか）と一礼（いちれい）すると、迎（むか）えてくれたのは指導（しどう）係（がかり）の先輩（せんぱい）エンジニア・ケンジさんだった。笑顔（えがお）の爽（さわ）やかな頼（たよ）れる先輩（せんぱい）だ。

しかし、歓迎（かんげい）ムードに浸（ひた）っていたのも束（つか）の間（ま）、午後（ごご）から早速（さっそく）実務（じつむ）の洗礼（せんれい）を受（う）けることになった。

渡（わた）されたシステム仕様（しよう）書（しょ）には、難解（なんかい）な業界（ぎょうかい）専門（せんもん）用語（ようご）がびっしりと並（なら）んでいた。教科書（きょうかしょ）通（どお）りの日本語（にほんご）**一方（いっぽう）で**、現場（げんば）で飛（と）び交（か）うリアルな指示（しじ）のスピードに追（お）いつけず、レンは焦（あせ）りを隠（かく）せなかった。

「分（わ）からないことを恥（は）ずかしがって放置（ほうち）する**まい**。聞きづらくても確認（かくにん）し**ざるを得（え）ない**」

レンは深呼吸（しんこきゅう）をし、メモ帳（ちょう）を片手（かたて）にケンジ先輩（せんぱい）のデスクへと向（む）かった。

「ケンジ先輩（せんぱい）、お忙（いそが）しいところ恐（おそ）れ入（い）ります。この仕様（しよう）の認識（にんしき）について、５分（ごふん）だけお時間（じかん）をいただいてもよろしいでしょうか」

ケンジ先輩（せんぱい）は作業（さぎょう）の手（て）を止（と）め、ニッコリと笑（わら）った。

「いい質問（しつもん）のタイミングだね、レン君（くん）。分（わ）からないことをその場（ば）で聞（き）く、それがエンジニアの第一歩（だいいっぽ）だよ」

最初（さいしょ）の壁（かべ）を自（みずか）らの勇気（ゆうき）で乗（の）り越（こ）えたレンの胸（むね）に、新（あたら）しい自信（じしん）の灯（ひ）がともった。""",
        "content_vi": """Một buổi sáng tháng Tư ngập tràn cánh hoa anh đào bay lượn trong gió xuân, khoác lên mình bộ vest mới tinh, Ren tự tin bước qua cánh cửa tự động của tòa cao ốc văn phòng tại Akihabara.

Kể từ hôm nay, cậu chính thức trở thành thành viên của Đội phát triển số 1 thuộc Tập đoàn Mirai Technology, bước vào cuộc đời của một người đi làm (Shakaijin).

"**Nhân thời khắc** bước vào khởi đầu mới của cuộc đời, điều tối quan trọng là phải chào hỏi lễ phép và tuyệt đối tuân thủ nguyên tắc báo cáo Ho-Ren-So (Báo cáo - Liên lạc - Thảo luận) đấy nhé em."

Lời căn dặn ân cần của chị Yuki lúc chỉnh lại cà vạt cho cậu trước khi ra khỏi nhà vẫn còn in đậm trong tâm trí.

"Xin kính chào toàn thể các anh chị! Tôi tên là Ren, từ hôm nay được phân công về phòng mình. Kính mong được các anh chị chỉ bảo và giúp đỡ ạ!"

Cúi chào 90 độ dõng dạc trước toàn thể văn phòng, người tiến tới đón tiếp cậu là anh Kenji — kỹ sư tiền bối chịu trách nhiệm hướng dẫn trực tiếp cho Ren. Một người anh điềm đạm với nụ cười sảng khoái.

Thế nhưng, cảm giác hân hoan vừa chớm nở chẳng kéo dài được bao lâu, ngay buổi chiều cậu đã phải nếm trải 'phép thử rửa tội' thực tế nơi công sở.

Tài liệu đặc tả hệ thống được giao dày đặc những thuật ngữ kỹ thuật chuyên ngành hóc búa. **Một mặt** tiếng Nhật trong sách vở thì cậu nắm chắc, **nhưng mặt khác** tốc độ chỉ đạo công việc dồn dập tại hiện trường lại khiến Ren toát mồ hôi vì không theo kịp.

"**Quyết không đời nào** vì ngại ngùng giấu dốt mà bỏ mặc không hiểu. Dẫu có ngại làm phiền thì lúc này cũng **buộc lòng phải** mở lời hỏi rõ!"

Hít một hơi thật sâu, cầm chắc cuốn sổ tay, Ren dứt khoát bước tới bàn làm việc của đàn anh Kenji:

"Anh Kenji ơi, em xin lỗi vì làm phiền anh lúc đang bận. Về cách hiểu của phần đặc tả này, anh có thể cho em xin 5 phút để xác nhận lại được không ạ?"

Anh Kenji dừng tay gõ bàn phím, quay sang mỉm cười tán thưởng:

"Thời điểm em chọn để hỏi rất chuẩn đấy, Ren à! Không hiểu là hỏi ngay tại chỗ, đó chính là bước đi đầu tiên sống còn của một kỹ sư chuyên nghiệp!"

Vượt qua bức tường bỡ ngỡ đầu tiên bằng chính sự dũng cảm của mình, một ngọn lửa tự tin mới lại bừng sáng trong lồng ngực Ren.""",
        "grammar_analysis": """### 1. `〜にあたって / 〜にあたり`
- **Câu trong tập:** `新（あたら）しい人生（じんせい）のスタートを切（き）るにあたって...`
- **Ý nghĩa:** "Nhân thời điểm bước vào một sự kiện / giai đoạn trọng đại..." (Văn phong trang trọng, chuẩn mực).

### 2. `〜まい`
- **Câu trong tập:** `分（わ）からないことを恥（は）ずかしがって放置（ほうち）するまい`
- **Ý nghĩa:** "Quyết không đời nào buông xuôi, tuyệt đối không giấu dốt" (Ý chí phủ định mạnh mẽ).

### 3. `〜一方（で）`
- **Câu trong tập:** `教科書（きょうかしょ）通（どお）りの日本語（にほんご）一方（で）、現場（げんば）のスピード...`
- **Ý nghĩa:** "Một mặt thì nắm lý thuyết, nhưng mặt khác thực tế lại muôn phần khốc liệt" (Đối lập hai mặt).

### 4. `〜ざるを得（え）ない`
- **Câu trong tập:** `確認（かくにん）せざるを得（え）ない`
- **Ý nghĩa:** "Buộc lòng phải hỏi rõ, không còn cách nào khác".""",
        "vocab_notes": """- **報連相（ほうれんそう - BÁO LIÊN TƯƠNG):** Quy tắc vàng công sở Nhật: 報告 (Báo cáo) - 連絡 (Liên lạc) - 相談 (Thảo luận).
- **洗礼（せんれい - TẨY LỄ）を受（う）ける:** Nếm trải thử thách đầu đời, trải qua phép thử cam go.
- **仕様書（しようしょ - SĨ DẠNG THƯ):** Bản đặc tả yêu cầu kỹ thuật phần mềm.
- **放置（ほうち - PHÓNG TRÍ）する:** Bỏ mặc, ngó lơ không thèm giải quyết.""",
        "questions": [
            ("ユキ姉がレンの初出社にあたって最も強調した教えは何か。",
             ["残業代をしっかり請求すること。",
              "先輩への挨拶と報連相（ほうれんそう）を徹底すること。",
              "ランチは必ず高い店に行くこと。",
              "誰とも話さずに黙々とコードを書くこと。"], 2),
            ("レンが仕様書の難しさに直面した時、取った最も適切な行動は何か。",
             ["分からないことを恥ずかしがらず、勇気を出してメモを持って先輩に時間をもらい確認した。",
              "分からないまま適当に想像で作ってしまった。",
              "仕事を投げ出して神保町のカフェへ帰ってしまった。",
              "母親に電話して助けを求めた。"], 1)
        ],
        "sister_message": "Văn hóa Ho-Ren-So (Báo cáo - Liên lạc - Thảo luận) là chìa khóa vàng giúp em thành công ở bất cứ công ty Nhật nào nhé cưng! 🌸",
        "next_preview": "Một lỗi bug nghiêm trọng bất ngờ phát sinh trên hệ thống máy chủ trước giờ bàn giao sản phẩm cho khách hàng lớn. Ren và anh Kenji phải ở lại công ty xuyên đêm giải cứu dự án. Tình đồng đội sẽ được thử thách ra sao? Đón đọc Tập 11 nhé!"
    },
    15: {
        "filename": "series-01_tap-15_quan_he_cong_so_va_loi_hua.md",
        "title_jp": "職場（しょくば）の絆（きずな）と果（は）たすべき約束（やくそく）",
        "title_vi": "Tình Thân Công Sở & Lời Hứa Phải Hoàn Thành — Vận Dụng Từ Vựng Bài 01",
        "summary_prev": "Sau khi chính thức nhận việc tại Tập đoàn Mirai Technology ở Akihabara, Ren đã vượt qua bức tường bỡ ngỡ ban đầu nhờ sự chỉ bảo của đàn anh Kenji. Hôm nay, một thử thách giao tiếp lớn xuất hiện: dự án đầu tiên của cậu phải phối hợp giữa các thế hệ trong công ty và gặp gỡ đối tác quan trọng.",
        "grammar_points": ["〜に際して", "〜一方（で）", "〜に相違ない", "〜を込めて"],
        "sister_message": "Trong môi trường công sở Nhật Bản, từ vựng không chỉ để thi JLPT mà là nghệ thuật đối nhân xử thế. Hãy học thuộc câu thực chiến hôm nay cưng nhé! 🌸",
        "next_preview": "Dự án chính thức bước vào giai đoạn tăng tốc. Liệu Ren và cậu bạn đồng nghiệp bằng tuổi Hayato có phối hợp ăn ý khi đối mặt với sự cố kỹ thuật đầu tiên? Đón đọc Tập 16 nhé!"
    }
}

def generate_dynamic_series_episode(next_ep):
    """
    Tự động sinh tập tiếp theo nếu kịch bản đã vượt quá ngân hàng kịch bản có sẵn.
    Đảm bảo series chạy mãi mãi mỗi ngày mà không bao giờ bị dừng lại!
    """
    arc_number = (next_ep - 1) // 7 + 1
    episode_in_arc = (next_ep - 1) % 7 + 1
    
    # Chủ đề phong phú luân chuyển chuẩn thi N2
    themes = [
        ("チームワークと信頼（しんらい）の絆（きずな）", "Tinh Thần Đồng Đội & Sợi Dây Gắn Kết Niềm Tin", ["〜に相違ない", "〜からこそ", "〜抜く", "〜を契機に"]),
        ("深夜（しんや）の危機（きき）と問題（もんだい）解決（かいけつ）", "Khủng Hoảng Lúc Nửa Đêm & Bản Lĩnh Xử Lý Sự Cố", ["〜ざるを得ない", "〜末に", "〜どころか", "〜一方（で）"]),
        ("顧客（こきゃく）への提案（ていあん）と共感（きょうかん）の力（ちから）", "Đề Xuất Dự Án & Sức Mạnh Thấu Cảm Khách Hàng", ["〜に応えて", "〜を通じて", "〜にほかならない", "〜限り"]),
        ("失敗（しっぱい）から学（まな）ぶプロフェッショナルの誇（ほこ）り", "Học Hỏi Từ Thất Bại & Niềm Tự Hào Chuyên Nghiệp", ["〜まい", "〜てたまらない", "〜のみならず", "〜を込めて"]),
        ("神保町（じんぼうちょう）の週末（しゅうまつ）と未来（みらい）への語（かた）らい", "Cuối Tuần Ở Jimbocho & Cuộc Trò Chuyện Về Tương Lai", ["〜つつある", "〜にすぎない", "〜ものなら", "〜からには"]),
        ("アオイの挑戦（ちょうせん）と仲間（なかま）の温（あたた）かい応援（おうえん）", "Thử Thách Của Aoi & Sự Tiếp Sức Ấm Áp Của Đồng Đội", ["〜に違いない", "〜に際して", "〜やまない", "〜かねない"]),
        ("東京（とうきょう）の青空（あおぞら）と次（つぎ）なる高（たか）みへ", "Bầu Trời Xanh Tokyo & Khát Vọng Chinh Phục Đỉnh Cao Mới", ["〜を契機に", "〜限る", "〜とともに", "〜にほかならない"])
    ]
    
    theme_jp, theme_vi, grammars = themes[episode_in_arc - 1]
    
    return {
        "filename": f"series-01_tap-{next_ep:02d}_aozora_tokyo.md",
        "title_jp": f"{theme_jp}（第{next_ep}話）",
        "title_vi": f"{theme_vi} (Tập {next_ep})",
        "summary_prev": f"Hành trình của Ren và chị Yuki tại Tokyo tiếp tục bước sang chương mới đầy ý nghĩa với những bài học cuộc sống sâu sắc và tinh thần không ngừng vươn lên.",
        "grammar_points": grammars,
        "content_jp": f"""神保町（じんぼうちょう）のカフェ『青空（あおぞら）珈琲館（こーひーかん）』に、今日（きょう）も穏（おだ）やかな時間（じかん）が流（なが）れていた。

仕事（しごと）の現場（げんば）で様々（さまざま）な経験（けいけん）を積（つ）み重（かさ）ねるレンは、日々（ひび）の課題（かだい）に真摯（しんし）に向（む）き合（あ）っていた。

「壁（かべ）にぶつかった時（とき）**からこそ**、自分（じぶん）の真価（しんか）が問（と）われるのだ」

田中（たなか）さんの教（おし）えとユキ姉（ねえ）の淹（い）れてくれる珈琲（コーヒー）の温（あたた）かさが、彼（かれ）の心（こころ）をいつでも前（まえ）へと押（お）し進（すす）めてくれる。同僚（どうりょう）や仲間（なかま）との対話（たいわ）を通（とお）じて、レンは一歩（いっぽ）ずつ、確実（かくじつ）に成長（せいちょう）を遂（と）げていた。

東京（とうきょう）の青空（あおぞら）は、努力（どりょく）を惜（お）しまない全（すべ）ての人（ひと）を、今日（きょう）も優（やさ）しく見守（みまも）り続（つづ）けている。""",
        "content_vi": f"""Tại quán cà phê 'Aozora' giữa lòng phố sách Jimbocho, nhịp sống bình yên vẫn nhẹ nhàng trôi qua mỗi ngày.

Tích lũy thêm nhiều kinh nghiệm quý báu tại môi trường làm việc thực tế, Ren luôn đối mặt với từng thử thách bằng một thái độ chân thành và cầu thị nhất.

'Chính vì những lúc đối mặt với bức tường khó khăn, giá trị thực sự của bản thân mới được rèn giũa.'

Lời chỉ bảo của bác Tanaka cùng hương cà phê ấm áp của chị Yuki luôn là điểm tựa vững chắc tiếp thêm đôi cánh cho cậu tiến về phía trước. Dưới bầu trời xanh của Tokyo, hành trình trưởng thành của Ren vẫn đang nở rộ từng ngày.""",
        "grammar_analysis": f"""### 1. `{grammars[0]}`
- **Ý nghĩa:** Mẫu ngữ pháp trọng tâm được vận dụng linh hoạt trong đời sống và công việc hàng ngày.
### 2. `{grammars[1]}`
- **Ý nghĩa:** Thể hiện sắc thái biểu cảm phong phú chuẩn phong cách người bản xứ.""",
        "vocab_notes": f"""- **真摯（しんし - CHÂN CHÍ）:** Chân thành, nghiêm túc, hết lòng vì mục tiêu.
- **真価（しんか - CHÂN GIÁ):** Giá trị thực sự, bản lĩnh đích thực bên trong.
- **惜（お）しまない (TÍCH):** Không tiếc công sức, dốc toàn tâm toàn ý.""",
        "questions": [
            ("レンが困難に直面した時に最も支えとなっているものは何か。",
             ["神保町の仲間たちの教えと温かい応援、そして自身の真摯な努力の姿勢。",
              "宝くじに当たること。",
              "仕事を休んでずっと寝ていること。",
              "すぐに諦めて逃げ出すこと。"], 1),
            ("本文が伝えたい最も前向きなメッセージはどれか。",
             ["東京の生活は辛いことばかりだということ。",
              "真面目に努力を重ねる人は、困難を乗り越えて確実に成長していけるということ。",
              "日本語の勉強はすぐにやめるべきだということ。",
              "誰とも関わらず一人で生きるのが一番楽だということ。"], 2)
        ],
        "sister_message": f"Mỗi ngày tiến một bước nhỏ là gom lại thành vạn dặm đường dài rồi cưng nhé! Chị luôn ở đây dõi theo và tự hào về em! 🌸",
        "next_preview": f"Đón đọc tập tiếp theo (Tập {next_ep + 1:02d}) của Series Bầu Trời Xanh Tokyo vào sáng mai nhé!"
    }

def generate_next_series_episode():
    # Quét danh sách các tập series hiện tại
    pattern = os.path.join(STORY_DIR, 'series-01_tap-*.md')
    existing_episodes = glob.glob(pattern)
    
    current_numbers = []
    for ep in existing_episodes:
        match = re.search(r'tap-(\d+)', os.path.basename(ep))
        if match:
            current_numbers.append(int(match.group(1)))
            
    max_ep = max(current_numbers) if current_numbers else 0
    next_ep = max_ep + 1
    
    print(f"Current highest episode: {max_ep}. Next episode to generate: {next_ep}")
    
    if next_ep in SERIES_EPISODES:
        ep_data = SERIES_EPISODES[next_ep]
    else:
        ep_data = generate_dynamic_series_episode(next_ep)
        
    filepath = os.path.join(STORY_DIR, ep_data['filename'])
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(f'''# 🌸 Tập {next_ep:02d}: {ep_data['title_jp']}
## *({ep_data['title_vi']})*

> 🌸 **Lời dặn của chị Yuki:**  
> *"{ep_data['sister_message']}"*

---

## 0. 🎞️ Tóm Tắt Tập Trước (前回のあらすじ)
*{ep_data['summary_prev']}*

---

## 1. 📖 Diễn Biến Câu Chuyện (Có Phiên Âm Hiragana)

{ep_data['content_jp']}

---

## 2. 🇻🇳 Bản Dịch Tiếng Việt

{ep_data['content_vi']}

---

## 3. ⛩️ Phân Tích Ngữ Pháp N2 Trọng Tâm Trong Tập {next_ep:02d}

{ep_data['grammar_analysis']}

---

## 4. 📝 Từ Vựng & Quán Dụng Ngữ Đắt Giá
{ep_data['vocab_notes']}

---

## 5. ✍️ Câu Hỏi Luyện Tập Đọc Hiểu Dokkai

''')
        for q_i, q in enumerate(ep_data['questions'], 1):
            f.write(f"### Câu {q_i}: {q[0]}\n")
            for c_i, choice in enumerate(q[1], 1):
                f.write(f"{c_i}. {choice}  \n")
            f.write(f"\n*(Đáp án đúng: **{q[2]}**)*\n\n")

        f.write(f'''---

## 🔮 Dự Báo Tập Tiếp Theo (次回予告 - Jikai Yokoku)
> *"{ep_data['next_preview']}"*
''')

    # Cập nhật bảng mục lục story/README.md
    readme_path = os.path.join(STORY_DIR, 'README.md')
    if os.path.exists(readme_path):
        with open(readme_path, 'r', encoding='utf-8') as f:
            readme_content = f.read()
            
        new_row = f"| **{next_ep:02d}** | [**{ep_data['title_jp']}**<br>*({ep_data['title_vi']})*](./{ep_data['filename']}) | `{', '.join(ep_data['grammar_points'])}` | ✅ Đã phát hành |\n"
        
        if ep_data['filename'] not in readme_content:
            lines = readme_content.split('\n')
            new_lines = []
            inserted = False
            for line in lines:
                new_lines.append(line)
                if f"| **{max_ep:02d}** |" in line and not inserted:
                    new_lines.append(new_row.strip())
                    inserted = True
            if not inserted:
                # Nếu không tìm thấy dòng max_ep, thêm vào cuối bảng
                for i, line in enumerate(new_lines):
                    if "| **01** |" in line:
                        # Tìm dòng cuối cùng của bảng
                        j = i
                        while j < len(new_lines) and new_lines[j].startswith("|"):
                            j += 1
                        new_lines.insert(j, new_row.strip())
                        break
            with open(readme_path, 'w', encoding='utf-8') as f:
                f.write('\n'.join(new_lines))

    try:
        import build_web_manifest
        build_web_manifest.build_manifest()
    except Exception as e:
        print(f"Warning: Could not build web manifest: {e}")

    print(f" Successfully released Episode {next_ep:02d}: {ep_data['filename']}")
    return ep_data['filename']

if __name__ == '__main__':
    generate_next_series_episode()
