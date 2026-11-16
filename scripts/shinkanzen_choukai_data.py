# -*- coding: utf-8 -*-
"""
Dữ liệu Shinkanzen Master Nghe Hiểu N2 (新完全マスター聴解 N2)
実力養成編 Ⅰ〜Ⅵ (6 chương chuẩn mục lục sách gốc):
- Ⅰ. 音声の特徴に慣れる
- Ⅱ.「即時応答」のスキルを学ぶ (Mondai 4)
- Ⅲ.「課題理解」のスキルを学ぶ (Mondai 1)
- Ⅳ.「ポイント理解」のスキルを学ぶ (Mondai 2)
- Ⅴ.「概要理解」のスキルを学ぶ (Mondai 3)
- Ⅵ.「統合理解」のスキルを学ぶ (Mondai 5)
Mỗi bài nghe có track_id & speakers rõ ràng để sẵn sàng ghép TTS hoặc luyện Shadowing!
"""

CHOUKAI_LESSONS = [
    {
        "filename": "01_am-thanh-dac-trung.md",
        "chapter": "実力養成編 Ⅰ",
        "title_jp": "音声の特徴に慣れる",
        "title_vi": "Chương I — Làm Quen Đặc Trưng Âm Thanh Văn Nói Nhật",
        "intro": "Tại sao đọc chữ thì hiểu hết mà nghe băng người Nhật nói lại trôi tuột không bắt được chữ nào? Đó là vì trong văn nói tự nhiên người Nhật **rút gọn âm (縮約形)**, **lướt âm cuối**, và đổi **ngữ điệu cảm xúc**! Chương I trong **Shinkanzen Master Nghe hiểu N2** giải mã triệt để 6 quy luật biến âm này trước khi vào đề.",
        "theory_table": [
            ("`〜ておく` / `〜でおく`", "`〜とく` / `〜どく`", "Làm sẵn trước: `買（か）っておく → 買（か）っとく` / `読（よ）んでおく → 読（よ）んどく`"),
            ("`〜ている` / `〜ていた`", "`〜てる` / `〜てた`", "Đang/đã: `知（し）っている → 知（し）ってる` / `待（ま）っていた → 待（ま）ってた`"),
            ("`〜てしまう` / `〜でしまう`", "`〜ちゃう` / `〜じゃう`", "Lỡ/xong mất: `忘（わす）れてしまった → 忘（わす）れちゃった` / `飲（の）んでしまった → 飲（の）んじゃった`"),
            ("`〜ては` / `〜では`", "`〜ちゃ` / `〜じゃ`", "Nếu làm thế thì...: `行（い）ってはいけない → 行（い）っちゃいけない` / `それでは → それじゃ`"),
            ("`〜なければならない`", "`〜なきゃ` / `〜なくちゃ`", "Phải làm: `帰（かえ）らなければならない → 帰（かえ）らなきゃ`"),
            ("`〜のではないか` / `〜という`", "`〜んじゃないか` / `〜って（いう）`", "Nhấn mạnh/trích dẫn: `そうではないか → そうじゃないか` / `田中（たなか）という人 → 田中（たなか）って人`"),
        ],
        "strategies": [
            "**Chú ý ngữ điệu lên/xuống giọng (`イントネーション`):** Cùng một câu `行かないの？`, nếu lên giọng cao ở cuối có thể là mời rủ (`Đi cùng chứ?`) hoặc ngạc nhiên (`Ơ cậu không đi à?`); xuống giọng với `〜んじゃないかな` lại mang sắc thái phỏng đoán dè dặt.",
            "**Từ nối nuốt âm hay gặp ở N2:** `だけど` rút từ `だけれども`; `〜てあげようか` -> `〜てやろうか`; `〜に違いない` hay nhấn trọng âm ở âm đầu.",
            "**Luyện Shadowing mỗi ngày 10 phút:** Vừa nhìn dòng Hiragana bên dưới vừa đọc đuổi theo tốc độ tự nhiên để tai quen phản xạ rút gọn âm."
        ],
        "tracks": [
            {
                "track_id": "N2-C1-T01",
                "speakers": "女 (Nữ sinh viên) & 男 (Nam sinh viên)",
                "context": "Đoạn hội thoại ngắn về chuẩn bị tài liệu thuyết trình — chứa 4 dạng rút gọn âm kinh điển.",
                "script_lines": [
                    ("女", "あ、山下（やました）くん。明日（あした）のゼミの資料（しりょう）、もうコピー**しといた**？"),
                    ("男", "えっ、今日（きょう）中（じゅう）に**しなきゃ**いけなかったんだっけ？ すっかり**忘れちゃった**よ。"),
                    ("女", "えー、昨日（きのう）メールで言（い）った**じゃない**！ 今（いま）すぐ**行かなくちゃ**、印刷（いんさつ）室（しつ）閉（し）まっちゃうよ。"),
                    ("男", "わあ、本当（ほんとう）だ。それじゃ、すぐ行（い）ってくる！")
                ],
                "vi": "Nữ: À Yamashita này, tài liệu seminar ngày mai cậu đã photo sẵn chưa?\nNam: Ủa, phải làm trong hôm nay cơ à? Tớ quên khuấy mất rồi.\nNữ: Ơ kìa, hôm qua tớ đã nói qua email rồi còn gì! Không đi ngay bây giờ thì phòng in đóng cửa mất đấy.\nNam: Ôi đúng thật. Vậy tớ đi ngay đây!",
                "question": "Người nam đã quên làm việc gì, và bây giờ phải làm gì?",
                "options": [
                    "Quên gửi email cho người nữ -> giờ phải gửi ngay",
                    "Quên photo sẵn tài liệu seminar -> giờ phải chạy đi in trước khi phòng đóng cửa",
                    "Quên mang tài liệu về nhà -> giờ phải về nhà lấy",
                    "Quên giờ họp seminar ngày hôm nay -> giờ phải vào lớp ngay"
                ],
                "ans": 2,
                "exp": "`コピーしといた` = コピーしておいた (photo sẵn trước). `忘れちゃった` = 忘れてしまった (lỡ quên mất). `閉まっちゃうよ` = 閉まってしまうよ."
            },
            {
                "track_id": "N2-C1-T02",
                "speakers": "女 (Vợ) & 男 (Chồng)",
                "context": "Phân biệt sắc thái ngữ điệu `〜んじゃない` / `〜わけ` / từ phủ định rút gọn.",
                "script_lines": [
                    ("男", "あれ、冷蔵庫（れいぞうこ）に入（い）れておいたケーキ、君（きみ）が**食べちゃった**の？"),
                    ("女", "え、私（わたし）**じゃない**わよ。テーブルの上（うえ）に置（お）きっぱなしに**してた**から、ネコがいたずらした**んじゃない**？"),
                    ("男", "うわ、本当（ほんとう）だ！ 箱（はこ）が床（ゆか）に落（お）ちてる。すぐ片付（かたづ）け**とかなくちゃ**。")
                ],
                "vi": "Nam: Ơ, cái bánh kem anh để trong tủ lạnh em ăn mất rồi à?\nNữ: Ủa không phải em đâu. Vì anh cứ để tơ hơ trên bàn nên chẳng phải con mèo nghịch rồi sao?\nNam: Ôi đúng thật! Cái hộp rơi dưới sàn kìa. Phải dọn sẵn ngay mới được.",
                "question": "Tại sao chiếc bánh bị rơi hỏng?",
                "options": [
                    "Người vợ lỡ ăn hết chiếc bánh trong tủ lạnh",
                    "Người chồng quên mua bánh để vào tủ lạnh",
                    "Người chồng để nguyên trên bàn nên có lẽ con mèo đã làm rơi",
                    "Tủ lạnh bị hỏng nên bánh bị chảy"
                ],
                "ans": 3,
                "exp": "Bẫy văn nói: Nghe chữ `食べちゃったの？` (chồng hỏi nghi ngờ) phải nghe tiếp câu đáp `私じゃないわよ... 置きっぱなしにしてたから` (lúc đầu chồng tưởng để trong tủ nhưng thực ra để nguyên trên bàn)."
            }
        ]
    },
    {
        "filename": "02_sokujitou-outou.md",
        "chapter": "実力養成編 Ⅱ",
        "title_jp": "「即時応答」のスキルを学ぶ（問題4対策）",
        "title_vi": "Chương II — Kỹ Năng Phản Xạ Nhanh (Mondai 4)",
        "intro": "**Mondai 4 — 即時応答 (Phản xạ nhanh)** hoàn toàn KHÔNG có chữ in trên đề thi! Em nghe 1 câu phát biểu ngắn rồi chọn ngay 1 trong 3 câu đáp lại tự nhiên nhất. Bí kíp vàng của **Shinkanzen Master Nghe hiểu N2** là nhận diện ngay **Kính ngữ (`尊敬 vs 謙譲`)**, **Hàm ý từ chối/nhờ vả gián tiếp**, và **Loại bỏ bẫy lặp từ y chang**.",
        "theory_table": [
            ("Bẫy 1: Lặp lại y nguyên từ khóa", "Câu hỏi có `会議の資料`, đáp án sai cũng lặp lại `会議の資料` nhưng sai logic", "Trong tiếng Nhật, câu trả lời tự nhiên hay dùng đại từ/ẩn tân ngữ (`ええ、こちらに`) thay vì lặp lại cộc lốc."),
            ("Bẫy 2: Nhầm Tôn kính ⇄ Khiêm nhường", "Nghe `召し上がる` / `おっしゃる` (người khác làm) lại trả lời `はい、私が召し上がりました`", "Tuyệt đối không tự dùng Tôn kính ngữ cho hành động của bản thân (`×私が拝見します` = đúng phải là Khiêm nhường `拝見します`)."),
            ("Bẫy 3: Từ chối gián tiếp kiểu Nhật", "Đề nghị: `今週の土曜日、手伝っていただけませんか`", "Người Nhật hay nói `ちょっと…` / `あいにく土曜日は用事があって…` = Xin lỗi từ chối, không thể giúp!"),
            ("Bẫy 4: Xác nhận hàm ý ngạc nhiên/khen", "`思ったより難しかったね` / `よく一人でやったね`", "Đáp lại tự nhiên phải đồng cảm hoặc khiêm tốn (`いや、それほどでも` / `本当だね、予想以上だったね`)."),
        ],
        "strategies": [
            "**Tập trung 100% vào chủ ngữ ẩn của câu nói (`だれが誰に`):** Ai là người thực hiện hành động trong câu nói?",
            "**Nghe kỹ 3 chữ cuối câu:** Câu kết thúc bằng `〜てもらえませんか` (nhờ), `〜ましょうか` (đề nghị giúp), `〜たほうがいいですよ` (khuyên) đòi hỏi đuôi đáp hoàn toàn khác nhau!",
            "**Chú ý cụm giao tiếp N2 cố định:** `お先に失礼します`, `おかげさまで`, `こちらこそ`, `あいにくですが`, `恐れ入りますが`."
        ],
        "tracks": [
            {
                "track_id": "N2-C2-T01",
                "speakers": "男 (Đồng nghiệp nam) -> 女 (Đồng nghiệp nữ)",
                "context": "Mondai 4 Mẫu 1 — Khiêm nhường ngữ & Chào đón/Từ chối lịch sự.",
                "script_lines": [
                    ("男", "課長（かちょう）、先（さき）ほどお預（あず）かりした資料（しりょう）、ただいま拝見（はいけん）しました。")
                ],
                "vi": "Nam: Thưa trưởng phòng, tài liệu tôi nhận từ ngài ban nãy tôi vừa mới xem xong ạ.",
                "question": "Câu đáp lại nào của Trưởng phòng là phù hợp nhất?",
                "options": [
                    "1. それは助（たす）かりました。どうでしたか。",
                    "2. ああ、もうお届（とど）けになったんですね。",
                    "3. いいえ、こちらこそ拝見（はいけん）しました。"
                ],
                "ans": 1,
                "exp": "`拝見しました` là Khiêm nhường ngữ của `見ました` (người dưới vừa xem xong tài liệu của sếp). Sếp đáp tự nhiên nhất là `Thế thì đỡ quá / Tốt quá. Cậu thấy thế nào?` (1). Câu (2) sai nghĩa (`gửi` thay vì `đọc`), câu (3) sai kính ngữ (`sếp` lại dùng `拝見` ngược)."
            },
            {
                "track_id": "N2-C2-T02",
                "speakers": "女 (Sếp nữ) -> 男 (Nhân viên nam)",
                "context": "Mondai 4 Mẫu 2 — Hàm ý từ chối khéo / Báo bận (`あいにく`).",
                "script_lines": [
                    ("女", "山田（やまだ）くん、急（きゅう）で悪（わる）いんだけど、今日（きょう）の夕方（ゆうがた）からの会議（かいぎ）、出（で）てもらえないかな。")
                ],
                "vi": "Nữ: Yamada này, gấp quá ngại thật nhưng cuộc họp từ chiều nay cậu tham dự giúp chị được không nhỉ?",
                "question": "Cách đáp tự nhiên và đúng ngữ cảnh nhất của Yamada là gì?",
                "options": [
                    "1. すみません、今日（きょう）はあいにく先約（せんやく）がありまして。",
                    "2. ええ、会議（かいぎ）には絶対（ぜったい）出（だ）さないつもりです。",
                    "3. はい、私（わたし）からもよろしくお伝え（つたえ）ください。"
                ],
                "ans": 1,
                "exp": "`先約（せんやく）がある` (lỡ có hẹn trước rồi) + `あいにく` (tiếc quá/không may là) là cách từ chối khéo chuẩn N2. Câu (2) `出さない` sai tha động từ + vô lễ."
            },
            {
                "track_id": "N2-C2-T03",
                "speakers": "男 -> 女",
                "context": "Mondai 4 Mẫu 3 — Bẫy câu hỏi cảm thán/khẳng định ngược (`〜じゃない`).",
                "script_lines": [
                    ("男", "このレポート、データもしっかりしてるし、とても分かりやすい**じゃない**。")
                ],
                "vi": "Nam: Bản báo cáo này số liệu chắc chắn lại rất dễ hiểu đấy chứ nhỉ (khen ngợi)!",
                "question": "Người nữ đáp lại thế nào cho tự nhiên?",
                "options": [
                    "1. えっ、どこが分（わ）かりにくかったですか。",
                    "2. いやあ、時間（じかん）をかけて調（しら）べた甲斐（かい）がありました。",
                    "3. そうですね、私（わたし）も全然（ぜんぜん）分（わ）かりませんでした。"
                ],
                "ans": 2,
                "exp": "Ngữ điệu lên nhẹ ở `〜じゃない` trong khen ngợi có nghĩa 'tốt quá đấy chứ!'. Đáp lại: `Bõ công bỏ thời gian ra tìm hiểu thật` (2). Bẫy (1) nghe nhầm thành chê!"
            }
        ]
    },
    {
        "filename": "03_kadai-rikai.md",
        "chapter": "実力養成編 Ⅲ",
        "title_jp": "「課題理解」のスキルを学ぶ（問題1対策）",
        "title_vi": "Chương III — Kỹ Năng Hiểu Nhiệm Vụ (Mondai 1 - Hành Động Tiếp Theo)",
        "intro": "**Mondai 1 — 課題理解 (Hiểu nhiệm vụ)** hỏi hành động cụ thể mà nhân vật chính (`男の人` hoặc `女の人`) **PHẢI LÀM NGAY SAU ĐÂY (`このあと、まず何をしますか`)**. Cạm bẫy kinh điển của Shinkanzen là phương án nhắc tới sớm ở đầu băng sẽ bị người kia phủ định hoặc hoán đổi vai cho nhau ở 15 giây cuối!",
        "theory_table": [
            ("Bẫy 1: Nhắc trước rồi gạt đi", "`最初は〜しようと思ったんですが、今は〜のほうがいいですよ`", "Luôn gạch chéo phương án bị chê/hoãn trong giấy nháp, khoanh phương án mới thay thế."),
            ("Bẫy 2: Chia việc A / B giữa 2 người", "`コピーは私がやっておくから、君は予約をお願い`", "Cực kỳ cẩn thận! Đề hỏi **Người Nam** làm gì thì lấy việc giao cho Người Nam; không chọn việc Người Nữ tự nhận làm!"),
            ("Bẫy 3: Từ khóa chốt thứ tự `まず・その前に`", "`提出する前に、課長にハンコをもらわなきゃ`", "Đề hay hỏi `まず何をしますか` (làm việc nào TRƯỚC TIÊN) -> nếu phải xin dấu sếp rồi mới nộp thì đáp án là **xin dấu**, chưa phải nộp!"),
        ],
        "strategies": [
            "**20 giây đầu đọc 4 lựa chọn:** Chia đôi động từ chính ở 4 đáp án và viết tắt tiếng Việt/ký hiệu 1 chữ bên cạnh (vd: 1. Gọi ĐT, 2. Sửa file, 3. Xin dấu, 4. Nộp phòng A).",
            "**Khi băng đọc câu hỏi mở đầu**, gạch dưới xem đề hỏi **男の人 (Nam)** hay **女の人 (Nữ)**!",
            "**Nghe câu chốt ở 10 giây cuối:** Thường có `わかりました。じゃ、そうします。` hoặc `じゃあ、お願いね。`"
        ],
        "tracks": [
            {
                "track_id": "N2-C3-T01",
                "speakers": "女 (Trưởng nhóm) & 男 (Nhân viên mới)",
                "context": "Hội thoại công sở về việc chuẩn bị hội thảo khách hàng chiều nay (Đề hỏi: 男の人 はこのあと、**まず**何をしますか).",
                "script_lines": [
                    ("女", "佐藤（さとう）くん、今日（きょう）の午後（ごご）の説明会（せつめいかい）の準備（じゅんび）、どこまで進（すす）んだ？"),
                    ("男", "はい、会場（かいじょう）のイスは並（なら）べ終（お）わりました。これからマイクのテストをして、そのあと資料（しりょう）を人数分（にんずうぶん）コピーしようと思（おも）っています。"),
                    ("女", "あ、ありがとう。資料（しりょう）のコピーはさっき鈴木（すずき）さんに頼（たの）んでおいたから大丈夫（だいじょうぶ）よ。"),
                    ("男", "そうですか、助（たす）かります。じゃあ、マイクの確認（かくにん）だけすればいいですか。"),
                    ("女", "ううん、その前（まえ）に、入口（いりぐち）に案内（あんない）のポスターを貼（は）ってきてくれる？ お客（きゃく）さんが迷（まよ）わないように早（はや）めに出（だ）しときたいの。マイクはそのあとでいいから。"),
                    ("男", "わかりました。すぐ貼（は）ってきます。")
                ],
                "vi": "Nữ: Sato này, chuẩn bị cho buổi giới thiệu chiều nay làm đến đâu rồi?\nNam: Dạ ghế trong hội trường em xếp xong rồi. Bây giờ em định kiểm tra micro rồi sau đó photo tài liệu đủ số người.\nNữ: À cảm ơn. Photo tài liệu lúc nãy chị nhờ chị Suzuki làm sẵn rồi nên không sao đâu.\nNam: Vậy ạ, đỡ quá. Thế em chỉ cần kiểm tra micro thôi đúng không?\nNữ: Không, TRƯỚC ĐÓ em ra cổng dán tờ áp phích hướng dẫn giúp chị được không? Chị muốn treo sớm kẻo khách bị lạc. Micro để sau cũng được.\nNam: Em hiểu rồi. Em đi dán ngay đây.",
                "question": "男（おとこ）の人（ひと）はこのあと、**まず**何（なに）をしますか。",
                "options": [
                    "1. 会場（かいじょう）のイスを並（なら）べる",
                    "2. 資料（しりょう）を人数分（にんずうぶん）コピーする",
                    "3. 入口（いりぐち）に案内（あんない）のポスターを貼（は）る",
                    "4. マイクのテストをする"
                ],
                "ans": 3,
                "exp": "Bẫy 1: Xếp ghế đã làm xong. Bẫy 2: Photo tài liệu giao cho Suzuki rồi. Bẫy 4: Test mic bị đẩy ra `そのあとでいい` (làm sau). `その前に〜貼ってきて` -> Làm đầu tiên (`まず`) là dán poster (3)!"
            },
            {
                "track_id": "N2-C3-T02",
                "speakers": "男 (Khách hàng) & 女 (Nhân viên cửa hàng sách)",
                "context": "Đặt mua sách chuyên ngành tại hiệu sách (Đề hỏi: 男の人 はこのあと何をしますか).",
                "script_lines": [
                    ("男", "すみません、こちらの経済学（けいざいがく）の本（ほん）、棚（たな）に見当（みあ）たらないんですが。"),
                    ("女", "少々（しょうしょう）お待（ま）ちください……あいにく今（いま）、在庫（ざいこ）を切（き）らしておりまして、取（と）り寄（よ）せになります。来週（らいしゅう）の火曜日（かようび）には届（とど）きますが、いかがなさいますか。"),
                    ("男", "火曜日（かようび）ですか。ちょっと急（いそ）いでいるので、もし隣（となり）の駅前店（えきまえてん）にあれば、そっちで買（か）おうかと思（おも）うんですが。"),
                    ("女", "ただいま駅前店（えきまえてん）に在庫（ざいこ）があるかお調（しら）べしますね。……あ、3冊（さんさつ）残（のこ）っていますよ。お取（と）り置（お）きをお願い（ねが）しましょうか。"),
                    ("男", "はい、ぜひお願いします！ じゃあ、今日（きょう）の夕方（ゆうがた）取り（とり）に行（い）きます。")
                ],
                "vi": "Nam: Xin lỗi, quyển sách kinh tế học này tôi không thấy trên kệ...\nNữ: Xin chờ chút ạ... Tiếc quá hiện cửa hàng đang hết hàng, phải đặt nhập về, thứ Ba tuần sau sẽ tới...\nNam: Thứ Ba cơ à. Tôi đang hơi gấp, nếu chi nhánh trước ga bên cạnh có thì tôi qua đó mua...\nNữ: Để em kiểm tra tồn kho cửa hàng trước ga ngay ạ... À còn 3 cuốn đấy ạ! Em nhờ họ giữ trước cho anh nhé?\nNam: Vâng, nhờ chị nhé! Vậy chiều nay tôi sẽ qua lấy.",
                "question": "男（おとこ）の人（ひと）はこのあとどうしますか。",
                "options": [
                    "1. 来週（らいしゅう）の火曜日（かようび）にもう一度（いちど）この店（みせ）に来（く）る",
                    "2. 駅前店（えきまえてん）に自分（じぶん）で電話（でんわ）をして在庫（ざいこ）を聞（き）く",
                    "3. 今日（きょう）の夕方（ゆうがた）、駅前店（えきまえてん）へ本（ほん）を買（か）いに行（い）く",
                    "4. 本（ほん）の取（と）り寄（よ）せを注文（ちゅうもん）して帰（かえ）る"
                ],
                "ans": 3,
                "exp": "Nhân viên tự gọi kiểm tra & giữ hộ (`お調べしますね・お取り置きをお願いしましょうか`), người nam không cần gọi điện mà chiều nay qua cửa hàng trước ga lấy -> Đáp án 3."
            }
        ]
    },
    {
        "filename": "04_point-rikai.md",
        "chapter": "実力養成編 Ⅳ",
        "title_jp": "「ポイント理解」のスキルを学ぶ（問題2対策）",
        "title_vi": "Chương IV — Kỹ Năng Nắm Bắt Điểm Cốt Lõi (Mondai 2)",
        "intro": "**Mondai 2 — ポイント理解** cho sẵn câu hỏi + 4 đáp án trên giấy thi để đọc trước, sau đó hỏi **Lý do (`なぜですか`)**, **Yếu tố quan trọng nhất**, hoặc **Ý kiến của riêng từng người**. Rất hay đánh lừa bằng cách nhân vật nêu tới 3 lý do nhưng cuối cùng nhấn mạnh cái nào là **quyết định nhất (`一番〜` / `何より〜`)**!",
        "theory_table": [
            ("1. Đọc trước câu hỏi trong lúc băng hướng dẫn", "Nhìn kỹ chủ ngữ câu hỏi (`男の人はなぜ…` hay `女の人は…`)", "Xác định điểm khác biệt giữa 4 đáp án (vd: khác nhau ở Giá tiền / Gần ga / Thời gian / Giảng viên)."),
            ("2. Nhận diện lý do mồi vs lý do thật", "`〜もいいんですが、それよりも〜` / `〜が決め手でした` / `やっぱり〜がいちばんですね`", "Đáp án mồi được khen qua loa trước, nhưng lý do thật đi sau chữ `それよりも`, `結局（けっきょく）`, `いちばん〜`."),
            ("3. Để ý sắc thái do dự trong giao tiếp Nhật", "`そうですねえ…`, `ちょっと迷うんですが…`, `悪くはないんですけど…`", "Nghe `悪くない` đừng tưởng họ đồng ý chọn! Cụm đó thường mở đầu cho một lý do chê/từ chối ngay sau chữ `けど`."),
        ],
        "strategies": [
            "**Chia 2 cột Nam / Nữ trong nháp** nếu hai người tranh luận sở thích đối lập nhau.",
            "**Cảnh giác câu phủ định kép hoặc điều kiện chưa chắc chắn (`かもしれない`)**: Chỉ chốt đáp án nào khớp sự thật được xác nhận cuối cùng."
        ],
        "tracks": [
            {
                "track_id": "N2-C4-T01",
                "speakers": "男 (Đồng nghiệp nam) & 女 (Đồng nghiệp nữ)",
                "context": "Trao đổi về lý do chọn chuyển sang công ty mới hoặc khóa học ngoại ngữ (Đề hỏi: 女の人 は**どうして**今のジムに変えましたか).",
                "script_lines": [
                    ("男", "あれ、田中（たなか）さん、先月（せんげつ）からスポーツジムを変（か）えたんだって？ 前（まえ）のところも駅（えき）から近（ちか）くてよかったじゃない。"),
                    ("女", "うん、立地（りっち）は最高（さいこう）だったんだけどね。ただ、仕事（しごと）帰（かえ）りの夜（よる）7時台（しちじだい）に行（い）くと、いつもマシンがいっぱいで全然（ぜんぜん）待（ま）たされるのよ。"),
                    ("男", "ああ、都会（とかい）のジムは混（こ）むよね。それで、今度（こんど）のところは会費（かいひ）も安（やす）いの？"),
                    ("女", "いや、料金（りょうきん）は前（まえ）より高（たか）いくらいだし、家（いえ）からもちょっと歩（ある）くんだけど、24時間（にじゅうよじかん）開（あ）いてて、しかもアプリで今（いま）どれくらい混（こ）んでるか見（み）られるのが決（き）め手（て）になったんだ。ストレスなく運動（うんどう）できるからね。")
                ],
                "vi": "Nam: Ủa chị Tanaka, nghe bảo từ tháng trước chị đổi phòng gym à? Chỗ cũ gần ga cũng tốt thế còn gì.\nNữ: Ừ vị trí thì tuyệt thật đấy. Có điều cứ đi lúc 7h tối sau giờ làm là máy tập lúc nào cũng kín hết chỗ, phải chờ suốt.\nNam: À gym ở thành phố hay đông nhỉ. Thế chỗ mới phí hội viên cũng rẻ hơn à?\nNữ: Không, giá thậm chí còn đắt hơn chỗ cũ và đi từ nhà cũng phải đi bộ một đoạn, nhưng mở cửa 24h lại xem được độ đông khách qua app chính là điểm quyết định với chị. Tập đỡ bị stress.",
                "question": "女（おんな）の人（ひと）がスポーツジムを変（か）えた理由（りゆう）は何（なん）ですか。",
                "options": [
                    "1. 家（いえ）や駅（えき）からの距離（きょり）が以前（いぜん）より近（ちか）くなったから",
                    "2. 毎月（まいつき）の会費（かいひ）が前（まえ）のジムよりずっと安（やす）いから",
                    "3. 混雑（こんざつ）状況（じょうきょう）を確認（かくにん）でき、時間（じかん）を気（き）にせず快適（かいてき）に使（つか）えるから",
                    "4. 最新（さいしん）のトレーニングマシンがたくさん増（ふ）えたから"
                ],
                "ans": 3,
                "exp": "Bẫy 1 & 2 bị phủ định trực tiếp (`家からもちょっと歩く`, `料金は前より高い`). Bẫy 4 không có trong bài (`マシンがいっぱい` là đông người dùng, không phải thêm máy mới). `24時間開いてて + アプリで混んでるか見られる` -> Đáp án 3!"
            }
        ]
    },
    {
        "filename": "05_gaiyou-rikai.md",
        "chapter": "実力養成編 Ⅴ",
        "title_jp": "「概要理解」のスキルを学ぶ（問題3対策）",
        "title_vi": "Chương V — Kỹ Năng Nắm Bắt Ý Chính (Mondai 3 - Không Nhìn Đề Trước)",
        "intro": "**Mondai 3 — 概要理解** KHÔNG có câu hỏi hay lựa chọn in sẵn trên giấy! Em phải nghe một bài nói/trình bày/ý kiến dài 1–1.5 phút rồi mới nghe câu hỏi (`この人は何について話していますか` / `この人が最も言いたいことは何ですか`). Kỹ thuật cốt lõi của **Shinkanzen Master Nghe hiểu N2** là **ghi chép tóm tắt 3 dòng: Chủ đề — Phản biện — Kết luận**.",
        "theory_table": [
            ("Câu 1–2 đầu băng: Xác định CHỦ ĐỀ (`〜について話しています`)", "Nghe kỹ danh từ lặp đi lặp lại trong 15 giây đầu", "Nếu nói về `睡眠時間`, `プラスチックごみ`, hay `働き方` -> ghi nhanh từ khóa chủ đề."),
            ("Phần giữa băng: Tách `一般論` (Quan điểm chung) ⇄ `しかし・でも` (Ý thật)", "Khi diễn giả nói `最近よく〜と言われますが…` -> chuẩn bị chờ chữ `しかし`!", "Bẫy Mondai 3 cực hay lấy quan điểm `一般論` lúc đầu làm đáp án nhiễu!"),
            ("15 giây cuối băng: Chốt `主張` (Ý người nói muốn nhấn mạnh)", "`大切なのではないでしょうか`, `〜べきだと思います`, `それが本当の〜なんです`", "90% đáp án nằm trọn vẹn ở 2 câu cuối cùng!"),
        ],
        "strategies": [
            "**Không cố nhớ chi tiết số liệu hoặc ví dụ lẻ tẻ:** Quên số phần trăm hay tên riêng dài đi, chỉ tập trung vào **quan điểm tổng quát của người nói**.",
            "**Chú ý câu hỏi cuối băng:** Phân biệt `何についての話か` (Nói về chủ đề gì?) vs `最も伝えたいこと` (Điều muốn truyền đạt nhất là gì?)."
        ],
        "tracks": [
            {
                "track_id": "N2-C5-T01",
                "speakers": "男 (Chuyên gia trên radio)",
                "context": "Bài nói ngắn kiểu phát thanh radio/thuyết trình ~45 giây (Đề hỏi: 男の人 は**何について**話していますか / **最も言いたいこと**は何ですか).",
                "script_lines": [
                    ("男", "最近（さいきん）、街（まち）のスーパーやレストランでロボットが料理（りょうり）を運（はこ）んだり、AIがレジを担当（たんとう）したりする光景（こうけい）をよく見（み）かけるようになりました。"),
                    ("男", "こうした機械化（きかいか）に対（たい）して、『人間（にんげん）の仕事（しごと）が奪（うば）われるのではないか』と心配（しんぱい）する声（こえ）も少（すく）なくありません。"),
                    ("男", "しかし、少子（しょうし）高齢化（こうれいか）で深刻（しんこく）な人手（ひとで）不足（ぶそく）が続（つづ）く日本（にほん）では、単純（たんじゅん）作業（さぎょう）をロボットに任（まか）せることには大（おお）きな意味（いみ）があります。"),
                    ("男", "私（わたし）たちが考（かんが）えるべきなのは、機械（きかい）に負（ま）けないことではなく、人間（にんげん）にしかできない細（こま）やかな気配（きくば）りや創造的（そうぞうてき）な仕事（しごと）にどうやって力（ちから）を注（そそ）ぐか、ということなのです。")
                ],
                "vi": "Gần đây ở siêu thị hay nhà hàng ta hay thấy cảnh robot bưng đồ ăn hay AI phụ trách thu ngân. Trước xu hướng cơ giới hóa này, có không ít tiếng nói lo ngại rằng 'công việc của con người sẽ bị cướp mất sao?'. Thế nhưng ở Nhật Bản đang thiếu nhân lực trầm trọng vì già hóa dân số, việc giao công việc đơn giản cho robot mang lại ý nghĩa rất lớn. Điều chúng ta cần suy nghĩ không phải là ganh đua không thua máy móc, mà là làm sao dồn sức vào những công việc sáng tạo và sự tinh tế quan tâm mà chỉ con người mới làm được.",
                "question": "男（おとこ）の人（ひと）が最（もっと）も言（い）いたいことは何（なに）ですか。",
                "options": [
                    "1. ロボットやAIの導入（どうにゅう）を進（すす）めると人間（にんげん）の仕事（しごと）がなくなるので規制（きせい）すべきだ。",
                    "2. スーパーやレストランではAIよりも人間（にんげん）の店員（てんいん）のほうが正確（せいかく）だ。",
                    "3. 人手不足（ひとでぶそく）の中（なか）で単純（たんじゅん）作業（さぎょう）は機械（きかい）に任（まか）せ、人間（にんげん）ならではの仕事（しごと）に力（ちから）を入（い）れるべきだ。",
                    "4. 機械化（きかいか）に対応（たいおう）するために、すべての人（ひと）がロボットを作（つく）る技術（ぎじゅつ）を学（まな）ぶ必要（ひつよう）がある。"
                ],
                "ans": 3,
                "exp": "Bẫy 1 là `一般論` lo ngại bị cướp việc (bị chữ `しかし` bác bỏ). Bẫy 2 & 4 không nói tới. Câu chốt cuối khẳng định rõ hướng kết hợp máy làm việc đơn giản + người tập trung việc tinh tế/sáng tạo -> Đáp án 3."
            }
        ]
    },
    {
        "filename": "06_tougou-rikai.md",
        "chapter": "実力養成編 Ⅵ",
        "title_jp": "「統合理解」のスキルを学ぶ（問題5対策）",
        "title_vi": "Chương VI — Kỹ Năng Tổng Hợp Thông Tin Dài (Mondai 5)",
        "intro": "Đỉnh cao của phần Nghe hiểu JLPT N2 chính là **Mondai 5 — 統合理解 (Tổng hợp thông tin)**. Thời lượng băng dài ~2 phút, chứa lượng dữ kiện dày đặc gồm **4 phương án (1, 2, 3, 4)**. Đặc trưng đề xuất hiện ở 2 tiểu dạng chính — nếu chuẩn bị sẵn bảng ma trận nháp trước khi nghe, em sẽ làm chủ hoàn toàn bài cuối này!",
        "theory_table": [
            ("Dạng 1 (1 câu hỏi — Thảo luận chọn 1 từ 4 phương án)", "Ví dụ: 3 người trong công ty bàn xem dùng kế hoạch quảng cáo A/B/C/D nào", "Kẻ bảng 4 cột `1 | 2 | 3 | 4` trên nháp. Nghe ưu điểm (+) và lý do bị loại (-) của từng cái. Cái cuối cùng KHÔNG bị ai gạt hoặc giải quyết được nhược điểm là đáp án!"),
            ("Dạng 2 (2 câu hỏi nối tiếp — Nghe giới thiệu rồi 2 người chọn)", "Ví dụ: Nhân viên hướng dẫn 4 tour du lịch/lớp học -> rồi Người Nam & Người Nữ bàn nhau chọn cái nào cho mỗi người", "Chia nháp làm 4 dòng mô tả đặc điểm khóa 1-2-3-4 (Giá/Ngày/Nội dung). Sau đoạn hướng dẫn, viết nhanh điều kiện của **男** và **女** để khớp!"),
        ],
        "strategies": [
            "**Tuyệt đối ghi chú dạng ký hiệu ngắn trên nháp:** Ví dụ: `① 1万・土曜・駅から遠`, `② 8千・平日・初級`.",
            "**Nghe kỹ câu hỏi cuối Dạng 2:** Câu 1 luôn hỏi một người (vd: **男の人はどのコース**), câu 2 hỏi người còn lại (**女の人はどのコース**) — đừng điền nhầm hàng!"
        ],
        "tracks": [
            {
                "track_id": "N2-C6-T01",
                "speakers": "職員 (Nhân viên giới thiệu) + 男 (Nam sinh viên) & 女 (Nữ sinh viên)",
                "context": "Mondai 5 Dạng 2 hoàn chỉnh — Nhân viên trung tâm văn hóa giới thiệu 4 lớp học nấu ăn, sau đó 2 bạn bàn chọn lớp phù hợp.",
                "script_lines": [
                    ("職員", "市民（しみん）クッキングスクールへようこそ。今月（こんげつ）のおすすめコースを4つご紹介（しょうかい）します。"),
                    ("職員", "1番（ばん）の『和食（わしょく）基礎（きそ）コース』は毎週水曜日（すいようび）の昼（ひる）、包丁（ほうちょう）の使（つか）い方（かた）から丁寧（ていねい）に学（まな）べる初心者（しょしんしゃ）向（む）けです。"),
                    ("職員", "2番（ばん）の『時短（じたん）お弁（べん）とうコース』は毎週土曜日（どようび）の午前（ごぜん）、15分（じゅうごふん）で作（つく）れる簡単（かんたん）メニューが中心（ちゅうしん）です。"),
                    ("職員", "3番（ばん）の『本格（ほんかく）パン・スイーツコース』は毎週日曜日（にちようび）の午後（ごご）、オーブンを使（つか）った特別（とくべつ）なレシピを習（なら）います。"),
                    ("職員", "4番（ばん）の『スパイスカレー研究（けんきゅう）コース』は毎週木曜日（もくようび）の夜（よる）7時（しちじ）からで、材料（ざいりょう）費（ひ）が少（すこ）し高（たか）めですが本格的（ほんかくてき）な味（あじ）が楽（たの）しめます。"),
                    ("男", "ねえ、どれにする？ 僕（ぼく）は平日の昼間（ひるま）はアルバイトだし、夜（よる）も木曜日（もくようび）はサークルがあるから土日（どにち）がいいな。あまりお料理（りょうり）の経験（けいけん）がないから、手軽（てがる）に作（つく）れてお昼（ひる）に持（も）っていけるものが学（まな）びたいんだ。"),
                    ("女", "そうね。私（わたし）は甘い（あまい）スイーツもいいなと思（おも）ったんだけど、日曜日（にちようび）は家族（かぞく）と出（で）かけることが多（おお）いのよ。和食（わしょく）の基礎（きそ）はもう知（し）ってるし、仕事（しごと）帰（かえ）りの夜（よる）に通（かよ）えるのが助（たす）かるわ。多少（たしょう）材料（ざいりょう）費（ひ）がかかってもいいから、しっかり学（まな）んでみたい！")
                ],
                "vi": "Nhân viên: Chào mừng tới trung tâm nấu ăn. 1) Món Nhật cơ bản (T4 trưa, cho người mới từ cách cầm dao). 2) Cơm hộp siêu tốc (T7 sáng, làm nhanh 15 phút). 3) Bánh mì & đồ ngọt chuyên nghiệp (CN chiều, dùng lò nướng). 4) Cà ri gia vị chuyên sâu (T5 tối 19h, phí nguyên liệu hơi cao nhưng vị chuẩn).\nNam: Tớ ban ngày ngày thường đi làm thêm, tối T5 họp CLB nên muốn học T7 hoặc CN. Vì chưa có kinh nghiệm nấu ăn nên muốn học món làm nhanh gọn mang đi ăn trưa.\nNữ: Chị thì cũng thích đồ ngọt đấy nhưng CN hay đi chơi cùng gia đình. Món Nhật cơ bản biết rồi, đi học buổi tối sau giờ làm thì tiện hơn. Chi phí hơi cao một chút cũng không sao miễn học được bài bản!",
                "question": "質問1：男（おとこ）の人（ひと）はどのコースに申（もう）し込（こ）みますか。 / 質問2：女（おんな）の人（ひと）はどのコースに申（もう）し込（こ）みますか。",
                "options": [
                    "Nam: 2番（時短お弁とう） | Nữ: 4番（スパイスカレー研究）",
                    "Nam: 3番（パン・スイーツ） | Nữ: 1番（和食基礎）",
                    "Nam: 2番（時短お弁とう） | Nữ: 3番（パン・スイーツ）",
                    "Nam: 1番（和食基礎） | Nữ: 4番（スパイスカレー）"
                ],
                "ans": 1,
                "exp": "Nam: Tránh ngày thường -> chỉ còn 2 (T7) hoặc 3 (CN); muốn làm nhanh mang ăn trưa -> **2番（時短お弁とう）**. Nữ: Thích 3 nhưng CN bận với gia đình (loại 3!), biết món Nhật rồi (loại 1!), muốn học tối ngày thường và không ngại phí cao -> **4番（スパイスカレー研究）**!"
            }
        ]
    }
]
