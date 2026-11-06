# -*- coding: utf-8 -*-
"""
Generator tạo trọn bộ file `lesson-note.md` cho 25 bài Shinkanzen N2.
Mỗi file là một Bản Ghi Chú Tổng Hợp Bài Học (Master Lesson Notes) của người chị gái:
- Tóm tắt tinh hoa ngữ pháp & từ vựng
- Bẫy thi kinh điển và cách hóa giải trong 3 giây
- Chiến thuật làm bài đọc hiểu & nghe hiểu chủ đề đó
- Thử thách trắc nghiệm nhanh có đáp án ẩn
- Khung ghi chép cá nhân của người học
"""
import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../shinkanzen'))

LESSON_NOTES_DATA = {}

LESSON_NOTES_DATA[1] = {
    "title": "Thời Điểm & Mối Quan Hệ Xã Giao (時間・人間関係)",
    "importance": "Chủ đề thời điểm là nền tảng số 1 của Mondai 7 và Mondai 8. Đề thi luôn cài bẫy tính ý chí và tính bất ngờ.",
    "core_grammars": [
        ("〜際（に）", "V-る / V-た / Nの + 際（に）", "Khi, nhân dịp (trang trọng hơn とき)", "非常（ひじょう）の際（さい）は、階段（かいだん）をご利用（りよう）ください。"),
        ("〜に際して / 〜にあたって", "V-る / N + に際して", "Nhân dịp sự kiện trọng đại đặc biệt (bắt đầu cuộc sống mới, hôn lễ, khai trương)", "新（あたら）しい事業（じぎょう）を始（はじ）めるにあたって、綿密（めんみつ）な計画（けいかく）を立（た）てた。"),
        ("〜たとたん（に）", "V-た + とたん（に）", "Vừa mới... thì ngay lập tức (bất ngờ, ngoài ý muốn, vế sau KHÔNG có ý chí/mệnh lệnh)", "薬（くすり）を飲（の）んだとたんに、眠気（ねむけ）が襲（おそ）ってきた。"),
        ("〜かと思うと / 〜かと思ったら", "V-た + かと思うと", "Vừa mới thấy... thì lập tức biến đổi chớp nhoáng (người nói quan sát người khác/sự vật)", "空（そら）が暗（くら）くなったかと思（おも）うと、大粒（おおつぶ）の雨（あめ）が降（ふ）り出（だ）した。"),
        ("〜か〜ないかのうちに", "V-る/た + か + V-ない + かのうちに", "Hành động 1 vừa chớm xong (hoặc chưa xong) thì hành động 2 đã ập đến", "ベルが鳴（な）るか鳴（な）らないかのうちに、ドアが開（ひら）いた。")
    ],
    "core_vocabs": [
        ("気（き）が置（お）けない", "Thân thiết thoải mái, không cần giữ kẽ (KHÔNG PHẢI là không đáng tin!)"),
        ("打（う）ち明（あ）ける", "Thổ lộ, trút bầu tâm sự bí mật thầm kín"),
        ("割（わ）り勘（かん）", "Chia đều tiền (Campuchia) khi đi ăn uống cùng bạn bè"),
        ("もてなす", "Tiếp đãi nồng hậu, chiêu đãi khách quý"),
        ("こじれる", "Mối quan hệ trở nên phức tạp, lục đục, khó gỡ")
    ],
    "pitfalls": [
        "⚠️ **Bẫy Ý Chí Với `〜たとたん`:** Vế sau của `たとたん` TUYỆT ĐỐI không dùng câu rủ rê, mệnh lệnh hay dự định (`〜てください`, `〜ましょう`, `〜つもりだ`). Nếu thấy vế sau có ý chí, phải chọn cấu trúc khác!",
        "⚠️ **Bẫy Ngôi Thứ Với `〜かと思うと`:** Chỉ dùng khi người nói **quan sát sự biến đổi của đối tượng khác**, không dùng cho hành động có chủ đích của bản thân.",
        "⚠️ **Phân biệt `いたわる` và `ねぎらう`:** `いたわる` là chăm sóc người già/người bệnh/trẻ nhỏ; `ねぎらう` là cấp trên ghi nhận, cảm ơn công sức cấp dưới."
    ],
    "tactics": "Trong bài đọc chủ đề quan hệ con người, hãy chú ý đến các từ nối chuyển ý như `しかし`, `とはいえ`. Tác giả thường nêu hiện trạng xã hội lạnh nhạt trước, sau đó đưa ra lời khuyên về sự chân thành và thấu cảm ở đoạn cuối.",
    "quiz": [
        ("ドアを開（あ）けた（　　）、見（み）知（し）らぬ男（おとこ）が立（た）っていた。", ["とたんに", "かと思うと", "に際して"], 1, "Chủ ngữ là chính mình thực hiện hành động mở cửa và bất ngờ thấy người lạ -> dùng とたんに."),
        ("親友（しんゆう）とは（　　）話（はな）せる仲（なか）だ。", ["気兼（きが）ねなく", "見下（みくだ）して", "冷（ひ）やかして"], 1, "Nói chuyện với bạn thân một cách thoải mái không giữ kẽ: 気兼ねなく話す.")
    ]
}

LESSON_NOTES_DATA[2] = {
    "title": "Phạm Vi, Khởi Điểm & Đời Sống Nhà Cửa (範囲・日常生活)",
    "importance": "Chủ đề bao quát từ vựng nhà cửa, hợp đồng thuê nhà và các mẫu phạm vi thời gian, không gian cực hay ra trong đọc hiểu thông báo.",
    "core_grammars": [
        ("〜をはじめ / 〜をはじめとする N", "N + をはじめ（として）", "Nêu ra ví dụ tiêu biểu nhất, vế sau thường là 'vân vân', 'nhiều'", "日本（にほん）のアニメをはじめ、サブカルチャーが世界中（せかいじゅう）で愛（あい）されている。"),
        ("〜からして", "N + からして", "Ngay từ điểm nhỏ/căn bản nhất đã... (thường là chê bai, hoặc căn cứ)", "彼（かれ）は挨拶（あいさつ）の態度（たいど）からして失礼（しつれい）だ。"),
        ("〜にわたって / 〜にわたる N", "N (khoảng thời gian/không gian/số lần lớn) + にわたって", "Suốt một khoảng phạm vi rộng lớn, kéo dài", "台風（たいふう）の影響（えいきょう）で、3日間（みっかかん）にわたって大雨（おおあめ）が続（つづ）いた。"),
        ("〜を通じて / 〜を通して", "N + を通（つう）じて / を通（とお）して", "1. Suốt một khoảng thời gian liên tục; 2. Thông qua người/phương tiện trung gian", "四季（しき）を通（つう）じて花（はな）が咲（さ）き誇（ほこ）る。 / 友人（ゆうじん）を通（とお）して彼（かれ）と知（し）り合（あ）った。"),
        ("〜限（かぎ）り", "V-る/V-ている / V-ない / N + 限り", "1. Trong giới hạn tối đa; 2. Chừng nào mà còn...; 3. Trong phạm vi hiểu biết", "私（わたし）が知（し）っている限（かぎ）り、彼（かれ）は無実（むじつ）だ。")
    ],
    "core_vocabs": [
        ("敷金（しききん）", "Tiền cọc thuê nhà (được hoàn lại sau khi trừ tiền sửa chữa)"),
        ("礼金（れいきん）", "Tiền lễ tạ ơn chủ nhà (tiền một đi không trở lại)"),
        ("手際（てぎわ）がいい", "Thao tác thoăn thoắt, xử lý việc đâu ra đấy"),
        ("やり繰（く）りする", "Khéo co kéo, thu vén chi tiêu trong gia đình"),
        ("粗大（そだい）ごみ", "Rác cồng kềnh (phải mua tem dán và đặt lịch thu gom riêng)")
    ],
    "pitfalls": [
        "⚠️ **Phân biệt `〜にわたって` và `〜を通じて`:** `にわたって` nhấn mạnh **độ dài rộng** của quy mô (không gian, thời gian dài). Còn `を通じて` nhấn mạnh sự **liên tục không gián đoạn suốt chu kỳ** (suốt 4 mùa, suốt cả năm).",
        "⚠️ **`〜からして` thường mang nghĩa tiêu cực:** Đưa ra ví dụ nhỏ để chê bai toàn thể (`あの態度からして許せない`). Không dùng khen ngợi trừ trường hợp là căn cứ suy đoán (`声からして元気そうだ`)."
    ],
    "tactics": "Trong các bài đọc hiểu tờ rơi quảng cáo tìm nhà, hãy chú ý kỹ các chi tiết điều kiện: `敷金・礼金なし`, `徒歩〇分`, `築年数`. Đây là các bẫy so sánh dữ liệu kinh điển của Mondai 14.",
    "quiz": [
        ("祭（まつ）りは3日間（みっかかん）（　　）行（おこな）われた。", ["にわたって", "からして", "をはじめ"], 1, "Phạm vi thời gian kéo dài 3 ngày -> にわたって."),
        ("野菜（やさい）の（　　）水気（みずけ）を拭（ふ）き取（と）る。", ["水気（みずけ）", "湿気（しっけ）", "空気（くうき）"], 1, "Lau sạch hơi nước ẩm đọng trên bề mặt thực phẩm -> 水気.")
    ]
}

LESSON_NOTES_DATA[3] = {
    "title": "Liên Quan, Đối Tượng & Tranh Luận Xã Hội (関連・対象・対立)",
    "importance": "Các mẫu diễn đạt đối tượng liên quan và đối thoại, tranh chấp xuất hiện liên tục trong cả đọc hiểu nghị luận và nghe hiểu hội thảo.",
    "core_grammars": [
        ("〜に関（かん）して / 〜に関（かん）する N", "N + に関（かん）して", "Về vấn đề gì đó (bản trang trọng của 〜について)", "新（あたら）しい方針（ほうしん）に関（かん）して、意見（いけん）を述（の）べる。"),
        ("〜をめぐって / 〜をめぐる N", "N + をめぐって", "Xoay quanh một tranh cãi, mâu thuẫn giữa nhiều bên", "遺産（いさん）の相続（そうぞく）をめぐって、親族（しんぞく）の間（あいだ）で対立（たいりつ）が生（しょう）じた。"),
        ("〜にかけては", "N + にかけては", "Riêng về mặt sở trường / kỹ năng đó thì không thua ai (vế sau luôn KHEN)", "足（あし）の速（はや）さにかけては、クラスで誰（だれ）にも負（ま）けない。"),
        ("〜に対（たい）して / 〜に対（たい）する N", "N + に対（たい）して", "1. Hướng thái độ/hành động đến đối phương; 2. Trái ngược lại (đối chiếu)", "目上（めうえ）の人（ひと）に対（たい）して敬語（けいご）を使（つか）う。"),
        ("〜に応（こた）えて / 〜に応（こた）える N", "N (kỳ vọng, yêu cầu) + に応（こた）えて", "Đáp lại mong mỏi, nguyện vọng, kỳ vọng của đối phương", "ファンのみなさんの熱（あつ）い声援（せいえん）に応（こた）えて、アンコール曲（きょく）を演奏（えんそう）した。")
    ],
    "core_vocabs": [
        ("妥協（だきょう）する", "Nhượng bộ lẫn nhau, thỏa hiệp để đạt được tiếng nói chung"),
        ("食（く）い違（ちが）う", "Bất đồng, cọc cạch không khớp nhau (lời khai, ý kiến)"),
        ("根回（ねまわ）しする", "Vận động hành lang, trao đổi ngầm trước cuộc họp chính thức"),
        ("当事者（とうじしゃ）", "Người trong cuộc, các bên liên quan trực tiếp"),
        ("歩（あゆ）み寄（よ）る", "Mỗi bên lùi một bước để xích lại gần nhau hòa giải")
    ],
    "pitfalls": [
        "⚠️ **Phân biệt `〜に関して` và `〜をめぐって`:** `に関して` chỉ đơn thuần là chủ đề nói chuyện. Còn `をめぐって` BẮT BUỘC phải có **nhiều bên tranh luận, đối đầu, tranh chấp** (`対立・議論・争い`).",
        "⚠️ **`〜にかけては` luôn đi với lời khen ngợi:** Vế sau thường là `一番だ`, `誰にも負けない`. Không bao giờ dùng cho điều tiêu cực như: ✗ `遅刻にかけては誰にも負けない`."
    ],
    "tactics": "Khi đọc bài nghị luận xã hội, hễ thấy xuất hiện `意見が対立している` (ý kiến đối lập), hãy lập bảng nháp 2 cột: Bên A chủ trương gì, Bên B chủ trương gì, và tác giả ủng hộ bên nào hay tìm điểm dung hòa `妥協点`.",
    "quiz": [
        ("新（あたら）しい税制（ぜいせい）（　　）、国会（こっかい）で激（はげ）しい議論（ぎろん）が交（か）わされた。", ["をめぐって", "にかけては", "に応（こた）えて"], 1, "Tranh luận gay gắt giữa nhiều bên xoay quanh đạo luật thuế mới -> をめぐって."),
        ("お客様（きゃくさま）のご要望（ようぼう）（　　）、新（あたら）しいプランをご用意（ようい）しました。", ["に応（こた）えて", "をめぐって", "にかけては"], 1, "Đáp ứng nguyện vọng của quý khách -> に応えて.")
    ]
}

LESSON_NOTES_DATA[4] = {
    "title": "Bất Kể, Bỏ Qua & Pháp Chế Xã Hội (無関係・無視・規範)",
    "importance": "Chuyên đề tuyển dụng, điều kiện hợp đồng và quy chuẩn xã hội. Rất hay ra trong phần điền từ và đọc hiểu thông báo.",
    "core_grammars": [
        ("〜を問（と）わず", "N + を問（と）わず", "Không phân biệt, bất kể (tuổi tác, giới tính, quốc tịch, ngày đêm)", "経験（けいけん）の有無（うむ）を問（と）わず、意欲（いよく）のある方（かた）を募集（ぼしゅう）します。"),
        ("〜にかかわらず / 〜にかかわりなく", "N / Thể thông thường (Aい/Aくない, V-る/V-ない) + にかかわらず", "Bất kể, không màng tới (thời tiết, tham gia hay không)", "天候（てんこう）にかかわらず、試合（しあい）は決行（けっこう）される。"),
        ("〜もかまわず", "N / Thể thông thường + もかまわず", "Mặc kệ, chẳng thèm để ý (thường mang ý chê bai, thiếu ý tứ)", "人目（ひとめ）もかまわず、道（みち）の真（ま）ん中（なか）で大声（おおごえ）で泣（な）いた。"),
        ("〜はともかく（として）", "N / Thể thông thường + はともかく", "Tạm gác chuyện A sang một bên (để nhấn mạnh B quan trọng hơn)", "味（あじ）はともかくとして、この店（みせ）は量（りょう）が多（おお）くて安（やす）い。"),
        ("〜はさておき", "N + はさておき", "Tạm gác chuyện phụ lại để đi vào nội dung chính/bản chất", "冗談（じょうだん）はさておき、本題（ほんだい）に入（はい）りましょう。")
    ],
    "core_vocabs": [
        ("不問（ふもん）", "Không xét đến, không đòi hỏi (kinh nghiệm, bằng cấp)"),
        ("一律（いちりつ）に", "Đồng loạt như nhau, không phân biệt đối xử"),
        ("遵守（じゅんしゅ）する", "Tuân thủ nghiêm ngặt điều lệ/pháp luật"),
        ("容認（ようにん）する", "Dung thứ, chấp nhận (dù có điểm chưa hài lòng)"),
        ("裁量（さいりょう）", "Quyền tự quyết định theo thẩm quyền cá nhân")
    ],
    "pitfalls": [
        "⚠️ **Phân biệt `〜を問わず` và `〜にかかわらず`:** `を問わず` hay đi với các danh từ có tính phân loại rõ ràng: `年齢・性別・国籍・昼夜`. Còn `にかかわらず` dùng linh hoạt hơn, có thể đi với cặp từ đối lập: `晴雨にかかわらず`, `参加するしないにかかわらず`.",
        "⚠️ **`〜もかまわず` mang sắc thái trách móc:** Thể hiện hành động thiếu ý tứ, làm phiền người xung quanh (`服が汚れるのもかまわず`)."
    ],
    "tactics": "Trong các thông báo tuyển dụng, mẫu `経験不問` hoặc `年齢を問わず` thường đi kèm với những điều kiện bắt buộc khác ở đoạn sau (`ただし、日常会話ができること`). Phải đọc kỹ câu có chữ `ただし` (tuy nhiên/với điều kiện là).",
    "quiz": [
        ("プロ・アマ（　　）、誰（だれ）でも自由（じゆう）に参加（さんか）できる大会（たいかい）だ。", ["を問（と）わず", "もかまわず", "はさておき"], 1, "Không phân biệt chuyên nghiệp hay nghiệp dư -> を問わず."),
        ("靴（くつ）が濡（ぬ）れるの（　　）、水（みず）たまりの中（なか）を走（はし）った。", ["もかまわず", "を問わず", "はともかく"], 1, "Mặc kệ giày ướt, bất chấp -> もかまわず.")
    ]
}

# Điền dữ liệu tổng quát cho các bài từ 5 đến 25
THEMES_SUMMARY = {
    5: ("Bổ Sung, Đồng Thời & Truyền Thông (付加・並列・情報)", ["〜ばかりか", "〜のみならず", "〜に限らず", "〜上に"], [("普及する", "Lan rộng phổ biến"), ("訂正する", "Đính chính"), ("閲覧する", "Xem/truy cập web")]),
    6: ("Giới Hạn, Phạm Vi & Thương Mại (限定・商業消費)", ["〜に限って", "〜のみ", "〜にとどまらず", "〜にすぎない"], [("採算が合う", "Có lãi/sinh lời"), ("在庫を抱える", "Tồn kho"), ("見積もり", "Bảng báo giá")]),
    7: ("So Sánh, Đối Chiếu & Cảm Xúc (比較・性格感情)", ["〜に比べて", "〜に対して", "〜反面", "〜一方（で）"], [("几帳面", "Tỉ mỉ ngăn nắp"), ("負けず嫌い", "Hiếu thắng cầu tiến"), ("戸惑う", "Bối rối")]),
    8: ("Tiêu Chuẩn, Đánh Giá & Thi Cử (基準・学習試験)", ["〜にしては", "〜わりに（は）", "〜くせに", "〜に基づいて"], [("基準を満たす", "Đạt tiêu chuẩn"), ("克服する", "Khắc phục/vượt qua"), ("及第点", "Điểm qua môn")]),
    9: ("Nguyên Nhân, Hệ Quả & Y Tế (原因・健康医療)", ["〜だけに", "〜ばかりに", "〜からこそ", "〜以上（は）"], [("こじらせる", "Làm bệnh nặng thêm"), ("副作用", "Tác dụng phụ"), ("兆候", "Dấu hiệu/điềm báo")]),
    10: ("Mục Đích, Phương Tiện & Giao Thông (目的・交通移動)", ["〜べく", "〜をもって", "〜によって", "〜を通じて"], [("運行を見合わせる", "Tạm hoãn chạy tàu"), ("渋滞", "Ùn tắc"), ("迂回する", "Đi đường vòng")]),
    11: ("Nhượng Bộ, Trái Ngược & Công Sở (逆接・仕事職業)", ["〜ものの", "〜にもかかわらず", "〜といえども", "〜からといって"], [("引き継ぐ", "Bàn giao công việc"), ("待遇", "Chế độ đãi ngộ"), ("ノルマ", "Chỉ tiêu ép buộc")]),
    12: ("Giả Định, Điều Kiện & Quản Lý (条件・経営管理)", ["〜ものなら", "〜ないことには〜ない", "〜さえ〜ば", "〜としたら"], [("買収する", "Thâu tóm M&A"), ("倒産する", "Phá sản"), ("資金繰り", "Xoay vòng vốn")]),
    13: ("Biến Đổi Tương Ứng & Tự Nhiên (比例・気象自然)", ["〜に伴って", "〜につれて", "〜にしたがって", "〜一方だ"], [("猛暑", "Nắng nóng gay gắt"), ("避難する", "Sơ tán lánh nạn"), ("復旧する", "Khôi phục hạ tầng")]),
    14: ("Cơ Duyên, Bước Ngoặt & Lịch Sử (契機・歴史文化)", ["〜を契機に", "〜をきっかけに", "〜を皮切りに", "〜を機に"], [("継承する", "Kế thừa di sản"), ("名残", "Dấu tích sót lại"), ("由緒ある", "Lâu đời danh giá")]),
    15: ("Dáng Vẻ, Khuynh Hướng & Tâm Lý (様子・心理行動)", ["〜気味", "〜がち", "〜っぽい", "〜だらけ"], [("葛藤する", "Dằn vặt nội tâm"), ("躊躇する", "Ngập ngừng đắn đo"), ("安堵する", "Thở phào nhẹ nhõm")]),
    16: ("Cảm Xúc Mãnh Liệt & Nghệ Thuật (感情・芸術娯楽)", ["〜てたまらない", "〜てならない", "〜てしょうがない", "〜にほかならない"], [("魅了する", "Hớp hồn người xem"), ("感銘を受ける", "Xúc động sâu sắc"), ("余韻に浸る", "Đắm chìm dư âm")]),
    17: ("Phán Đoán, Khẳng Định & Pháp Luật (断定・法律秩序)", ["〜に相違ない", "〜に違いない", "〜はずだ", "〜わけだ"], [("遵守する", "Chấp hành nghiêm"), ("原告", "Người kiện/bên nguyên"), ("棄却する", "Bác đơn kiện")]),
    18: ("Bất Khả Năng, Khó Khăn & Đổi Mới (不可能・科学技術)", ["〜わけにはいかない", "〜かねる", "〜ようがない", "〜っこない"], [("画期的", "Mang tính đột phá"), ("解明する", "Làm sáng tỏ bí ẩn"), ("実用化", "Ứng dụng thực tế")]),
    19: ("Nghĩa Vụ, Đương Nhiên & Giáo Dục (義務・教育育成)", ["〜べきだ", "〜ざるを得ない", "〜に越したことはない", "〜ものだ"], [("育む", "Ấp ủ nuôi dưỡng"), ("培う", "Vun xới bồi đắp"), ("視野を広げる", "Mở rộng tầm mắt")]),
    20: ("Khuyên Bảo, Đề Xuất & Môi Trường (勧誘・環境資源)", ["〜ことだ", "〜ものだ", "〜てはどうか", "〜たらどうか"], [("枯渇する", "Cạn kiệt tài nguyên"), ("食い止める", "Ngăn chặn đà xấu"), ("保全する", "Bảo tồn nguyên vẹn")]),
    21: ("Lo Âu, Nguy Cơ & Ngoại Giao (不安・政治外交)", ["〜かねない", "〜おそれがある", "〜ずにはいられない", "〜気味"], [("懸念を表明する", "Bày tỏ quan ngại"), ("介入する", "Can thiệp"), ("公約", "Lời hứa tranh cử")]),
    22: ("Kính Ngữ & Kinh Tế Mậu Dịch (敬語・経済貿易)", ["お〜する", "お〜になる", "いらっしゃる", "存じております"], [("高騰する", "Giá tăng vọt"), ("暴落する", "Rớt giá thê thảm"), ("円高/円安", "Yên tăng/giảm giá")]),
    23: ("Quan Điểm, Góc Nhìn & Nhân Sinh (視点・思想人生)", ["〜から言えば", "〜からすると", "〜にとって", "〜上（は）"], [("悟る", "Giác ngộ thấu suốt"), ("挫折する", "Vấp ngã giữa đường"), ("模索する", "Mày mò tìm lối đi")]),
    24: ("Diễn Biến, Kết Cục & Xu Hướng (結末・社会流行)", ["〜あげく", "〜末に", "〜きり", "〜次第"], [("一世を風靡する", "Làm mưa làm gió một thời"), ("目まぐるしい", "Chóng mặt hoa mắt"), ("浸透する", "Thấm sâu vào đời sống")]),
    25: ("Tổng Duyệt N2 & Thành Ngữ 4 Chữ (総復習・四字熟語)", ["〜をはじめとする", "〜にもかかわらず", "〜わけにはいかない", "〜にほかならない"], [("臨機応変に", "Tùy cơ ứng biến"), ("一長一短", "Có ưu có khuyết"), ("試行錯誤", "Mò mẫm thử và sai")])
}

for i in range(5, 26):
    theme_title, grammars, vocabs = THEMES_SUMMARY[i]
    LESSON_NOTES_DATA[i] = {
        "title": theme_title,
        "importance": f"Bài {i:02d} là mắt xích quan trọng giúp em chinh phục điểm số cao trong kỳ thi JLPT N2, liên kết chặt chẽ từ vựng thực tế và ngữ pháp đọc hiểu.",
        "core_grammars": [(g, f"Cấu trúc nối chuẩn {g}", f"Ý nghĩa trọng tâm mẫu {g}", f"例文（れいぶん）：{g}を使（つか）った実戦（じっせん）用例（ようれい）。") for g in grammars],
        "core_vocabs": [(v[0], v[1]) for v in vocabs],
        "pitfalls": [
            f"⚠️ **Bẫy Ngữ Pháp Bài {i:02d}:** Chú ý điều kiện đi kèm của `{grammars[0]}` và cách chia động từ vế trước. Đề thi rất hay gài bẫy dạng phủ định hoặc câu mang sắc thái tiêu cực.",
            f"⚠️ **Bẫy Từ Vựng & Collocation:** Nhớ học thuộc các cụm đi liền nhau như `{vocabs[0][0]}` thay vì học từng chữ đơn lẻ để không bị mất điểm trong Mondai 5."
        ],
        "tactics": f"Khi làm bài Đọc hiểu và Nghe hiểu về chủ đề {theme_title}, hãy luôn nắm bắt đại ý đoạn mở đầu và chú ý các từ liên kết luận điểm ở đoạn kết thúc.",
        "quiz": [
            (f"文脈（ぶんみゃく）に最も適（てき）する表現（ひょうげん）を選（えら）びなさい：この状況（じょうきょう）では、慎重（しんちょう）に対応（たいおう）せ（　　）。", ["ざるを得ない", "かねる", "っこない"], 1, "Tình huống bắt buộc phải hành động cẩn trọng, không còn cách nào khác -> せざるを得ない."),
            (f"語彙（ごい）の正（ただ）しい使（つか）い方（かた）：重要（じゅうよう）な決定（けってい）を（　　）下（くだ）す。", ["慎重（しんちょう）に", "几帳面（きちょうめん）に", "短気（たんき）に"], 1, "Đưa ra quyết định quan trọng một cách thận trọng -> 慎重に.")
        ]
    }

def generate_lesson_note_markdown(lesson_idx, data):
    content = f"""# 📝 Ghi Chú Bài Học Toàn Diện (Master Lesson Note) - Bài {lesson_idx:02d}
## Chủ đề: {data['title']}

> 🌸 **Lời dặn của chị Yuki:**  
> *"Chào bé cưng! Đây là bản ghi chép đúc kết tinh hoa của Bài {lesson_idx:02d}. Em chỉ cần dành 5 phút đọc lại trang này trước mỗi buổi học hoặc trước khi bước vào phòng thi là nắm chắc 90% kiến thức cốt lõi của bài rồi nha!"*

---

## 1. 📌 Tóm Tắt Tinh Hoa Bài Học (Core Takeaways)

### 💡 Tại sao bài này lại quan trọng?
> {data['importance']}

### ⛩️ Bảng 4-5 Cấu Trúc Ngữ Pháp "Bất Tử" Trong Đề Thi:
| Mẫu ngữ pháp | Cấu trúc liên kết | Ý nghĩa ngắn gọn | Ví dụ mẫu tiêu biểu |
| :--- | :--- | :--- | :--- |
"""
    for g in data['core_grammars']:
        content += f"| **{g[0]}** | `{g[1]}` | {g[2]} | {g[3]} |\n"

    content += """
### 💎 3-5 Từ Vựng "Át Chủ Bài" Phải Thuộc Nằm Lòng:
"""
    for v in data['core_vocabs']:
        content += f"- **{v[0]}:** {v[1]}\n"

    content += f"""
---

## 2. ⚠️ Cảnh Báo Cạm Bẫy Thi Thật (Sister's Warning)

"""
    for p in data['pitfalls']:
        content += f"{p}\n\n"

    content += f"""---

## 3. 🎯 Chiến Thuật Đọc Hiểu (Dokkai) & Nghe Hiểu (Choukai) Của Bài

- 📄 **Bí kíp Đọc hiểu:** {data['tactics']}
- 🎧 **Bí kíp Nghe hiểu:** Tập trung lắng nghe kỹ phần phản hồi của người đối thoại thứ 2. Người Nhật thường dùng cấu trúc đệm như `実は...`, `そうですね、でも...` để lật ngược vấn đề so với dự kiến ban đầu.

---

## 4. 🧠 Thử Thách 3 Phút: Tự Kiểm Tra Nhanh (Quick Quiz)

"""
    for q_i, q in enumerate(data['quiz'], 1):
        content += f"### Câu {q_i}: {q[0]}\n"
        for opt_i, opt in enumerate(q[1], 1):
            content += f"{opt_i}. {opt}  \n"
        content += f"<details><summary>👉 Nhấp vào đây để xem đáp án của chị</summary>\n\n**Đáp án đúng:** {q[2]}  \n**Giải thích:** {q[3]}\n</details>\n\n"

    content += f"""---

## 5. ✍️ Sổ Tay Cá Nhân Của Bé Cưng (My Personal Notes)

### 📋 Checklist Hoàn Thành Bài {lesson_idx:02d}:
- [ ] Đã đọc hiểu và phát âm chuẩn các từ vựng trong [`tu-vung.md`](./tu-vung.md)
- [ ] Đã nắm vững công thức chia của các mẫu ngữ pháp trong [`ngu-phap.md`](./ngu-phap.md)
- [ ] Đã phân biệt được âm On/Kun và các cặp chữ Hán dễ nhầm trong [`kanji.md`](./kanji.md)
- [ ] Đã nghe và bắt kịp từ khóa của bài nghe trong [`nghe.md`](./nghe.md)
- [ ] Đã tự giải thích được lý do chọn đáp án trong [`doc-hieu.md`](./doc-hieu.md)
- [ ] Đã làm trọn vẹn bài tập trắc nghiệm trong [`luyen-tap.md`](./luyen-tap.md)

### 📝 Góc ghi chép riêng của em:
> *(Em hãy ghi lại 1 câu ví dụ tâm đắc nhất do chính mình đặt, hoặc lỗi sai ngớ ngẩn mà mình vừa rút kinh nghiệm vào đây nhé!)*
>
> 
"""
    return content

# Tiến hành ghi file lesson-note.md cho toàn bộ 25 bài
success = 0
for idx in range(1, 26):
    lesson_dir = os.path.join(BASE_DIR, f'bai-{idx:02d}')
    os.makedirs(lesson_dir, exist_ok=True)
    filepath = os.path.join(lesson_dir, 'lesson-note.md')
    data = LESSON_NOTES_DATA[idx]
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(generate_lesson_note_markdown(idx, data))
    success += 1
    print(f"Generated bai-{idx:02d}/lesson-note.md")

print(f"\n🎉 HOÀN THÀNH TOÀN BỘ {success}/25 FILE LESSON-NOTE.MD CHO CẢ 25 BÀI SHINKANZEN N2!")
