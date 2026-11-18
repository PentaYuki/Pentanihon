# -*- coding: utf-8 -*-
"""
Đề Thi Thử JLPT N2 Chuẩn Số 02 — 言語知識（文字・語彙・文法）
Cấu trúc chuẩn 100% kỳ thi thật (54 câu — 55 phút)
"""

PASSAGE_EXAM2 = (
    "会話において、相手の話をただ聞くだけでなく、うなずきや「そうですね」といった相づちを打つことは非常に大切だ。なぜなら、話し手は聞き手の反応を見る（　50　）、自分の話が伝わっているかどうかを確かめているからである。\n"
    "しかし、タイミングがずれたり、会話の内容に関係なく機械的にうなずいたりすると、かえって「話を聞いていないのではないか」という不信感を（　51　）。大切なのは回数ではなく、相手の感情に寄り添おうとする姿勢（　52　）。\n"
    "相手の言葉にしっかり耳を傾け、共感のサインを（　53　）、初めて心と心が通じ合う会話が生まれるのではないだろうか。今日から少しずつ意識して（　54　）。"
)

PASSAGE_EXAM2_VI = (
    "Trong giao tiếp, việc không chỉ nghe đơn thuần mà còn gật đầu hay đáp lời đệm như 'Vâng, đúng vậy nhỉ' rất quan trọng. Bởi lẽ người nói thông qua việc quan sát phản ứng của người nghe mà xác nhận xem câu chuyện của mình có truyền đạt được tới đối phương hay không.\n"
    "Tuy nhiên, nếu lệch nhịp hoặc gật đầu máy móc bất kể nội dung câu chuyện, trái lại còn dễ khiến đối phương nảy sinh sự nghi ngờ rằng 'Hình như cậu ta chẳng thèm nghe mình nói'. Điều quan trọng không nằm ở số lần gật đầu, mà chính là thái độ muốn đồng cảm chia sẻ cảm xúc của người nói.\n"
    "Chỉ khi chịu lắng nghe kỹ lời đối phương và gửi đi tín hiệu đồng cảm thì mới có thể nảy sinh cuộc trò chuyện thấu hiểu từ trái tim đến trái tim được chứ nhỉ. Từ hôm nay chúng ta hãy thử ý thức rèn luyện dần từng chút một xem sao nào."
)

EXAM_2 = {
    "id": "jlpt-n2-de-02",
    "code": "ĐỀ CHUẨN JLPT N2 — SỐ 02",
    "title_jp": "第2回 JLPT N2 模擬試験（言語知識：文字・語彙・文法）",
    "title_vi": "Đề Thi Thử JLPT N2 Số 02 — Công Nghệ, Tâm Lý & Tư Duy N2",
    "category": "full",
    "duration_min": 55,
    "pass_score": 19,
    "max_score": 60,
    "description": "Đề thi chuẩn cấu trúc Mondai 1–9 (54 câu), kiểm tra chuyên sâu từ vựng máy tính, tâm lý cảm xúc, phó từ mức độ, từ đa nghĩa, cùng hệ thống ngữ pháp N2 liên kết chặt chẽ.",
    "yuki_note_start": "Đề số 02 bước sang chủ đề công nghệ, thiên văn và tâm lý sâu sắc hơn chút xíu đó nha em~ Nhớ đọc chậm rãi gạch chân từ khóa ở Mondai 6 và Mondai 9 nhé. Chị Yuki tin em sẽ bứt phá điểm cao hơn Đề 01 luôn! 💙✨",
    "yuki_note_finish_pass": "Xuất sắc lắm luôn!! Em đã vượt qua Đề số 02 ngon ơ luôn rồi nè~ Càng làm nhiều đề, phản xạ đọc câu N2 của em càng bén nhạy ha! Giờ chỉ còn 1 đề cuối thôi, giữ vững phong độ nhé 🌟🎊",
    "yuki_note_finish_try": "Đừng nản nha em yêu~ Đề 02 có mấy bẫy từ đa nghĩa và tâm lý khá lắt léo đúng chuẩn JLPT thật đó! Hãy bấm từng câu sai để xem phân tích cả 4 đáp án rồi đọc lướt lại Chương Yandere hoặc Isekai tương ứng là ngộ ra ngay thôi 🌸💪",
    "questions": [
        # --- 問題1: 漢字読み (1-5) ---
        {
            "num": 1,
            "mondai": "問題1：漢字読み",
            "mondai_vi": "Cách đọc Kanji",
            "prompt": "暗い夜道で突然声をかけられ、思わず体が<u>震えた</u>。",
            "prompt_vi": "Bất ngờ bị gọi tiếng giữa con đường tối, cơ thể tôi bất giác run rẩy.",
            "options": ["ふるえた", "おびえた", "こごえた", "しびれた"],
            "ans": 1,
            "cute_right_msg": "Chính xác! `震（ふる）える` (Chấn — run rẩy vì lạnh hoặc sợ hãi) chuẩn không cần chỉnh luôn! ❄️🌹",
            "right_exp": "`震える` đọc là **ふるえる** (run lẩy bẩy vì sợ hãi, xúc động hoặc giá lạnh).",
            "cute_wrong_msg": "Nhẹ nhàng phân biệt nghĩa nha em: `震える` (Chấn) là rung/run = `ふるえる`, còn `おびえる` là `怯える` (sợ hãi khiếp đảm)! 💡",
            "wrong_exps": [
                "Tuyệt vời! `震（ふる）える` = run rẩy.",
                "`おびえる` là chữ `怯える` (sợ sệt, khiếp sợ).",
                "`こごえる` là chữ `凍える` (cóng cóng vì rét buốt).",
                "`しびれる` là chữ `痺れる` (tê cứng tay chân)."
            ],
            "source_ref": {"novel": "yandere", "chapter": 6, "lesson_id": "p2_c01_b02", "label": "Bộ 2 Yandere Ch.06 (Bài 23: Động từ đa nghĩa 2)"}
        },
        {
            "num": 2,
            "mondai": "問題1：漢字読み",
            "mondai_vi": "Cách đọc Kanji",
            "prompt": "深夜までパソコンの画面を見つめていたら、目が<u>かすんで</u>きた。",
            "prompt_vi": "Nhìn chằm chằm màn hình máy tính đến tận khuya nên mắt bắt đầu mờ nhòe đi.",
            "options": ["くもって", "しみて", "いたんで", "かすんで"],
            "ans": 4,
            "cute_right_msg": "Siêu đỉnh!! Từ `霞（かす）む` hay viết hiragana nhưng Kanji trong Bộ Yandere Ch.02 & Ch.03 giúp em nhớ ngay `かすむ` (mắt mờ nhòe / cảnh vật phủ sương)! 👀",
            "right_exp": "`霞む / 掠む` đọc là **かすむ**; khi nói về mắt (`目がかすむ`) nghĩa là mắt hoa mờ nhòe không nhìn rõ.",
            "cute_wrong_msg": "Chữ `霞` hoặc `かすむ` đi với `目` là 'mắt mờ nhòe' = **かすんで** nha em! 🌸",
            "wrong_exps": [
                "`くもる` là `曇る` (trời âm u, kính mờ hơi nước).",
                "`しみる` là `染みる / 沁みる` (ngấm vào, xót mắt).",
                "`いたむ` là `痛む` (đau nhức).",
                "Chính xác! `目がかすむ` = mắt bị mờ nhòe đi."
            ],
            "source_ref": {"novel": "yandere", "chapter": 2, "lesson_id": "p1_c02_b03", "label": "Bộ 2 Yandere Ch.02 (Bài 6: Sức khỏe)"}
        },
        {
            "num": 3,
            "mondai": "問題1：漢字読み",
            "mondai_vi": "Cách đọc Kanji",
            "prompt": "この地域の川は、工場の<u>排水</u>によって汚染されてしまった。",
            "prompt_vi": "Dòng sông vùng này đã bị ô nhiễm bởi nước thải từ nhà máy.",
            "options": ["はいすい", "はいみず", "はっすい", "ひすい"],
            "ans": 1,
            "cute_right_msg": "Chuẩn đét! `排（はい）` + `水（すい）` = `はいすい` (nước thải) gọn ơ! 💧",
            "right_exp": "`排水` đọc theo âm On: **はいすい** (nước thải sinh hoạt/công nghiệp; động từ `排水する` là thoát nước).",
            "cute_wrong_msg": "Ghép hai âm Hán-Nhật On-yomi nha em: chữ `排（はい）` trong `排出（はいしゅつ）` + `水（すい）` → `はいすい` đó! ✨",
            "wrong_exps": [
                "Chính xác tuyệt đối! `排水（はいすい）`.",
                "Không ghép On + Kun thành `はいみず`.",
                "`はっすい` là `撥水` (chống thấm nước trên vải/áo mưa).",
                "`ひすい` là `翡翠` (đá ngọc bích)."
            ],
            "source_ref": {"novel": "isekai", "chapter": 4, "lesson_id": "p1_c08_b01", "label": "Bộ 3 Isekai Ch.04 (Bài 18: Sinh thái)"}
        },
        {
            "num": 4,
            "mondai": "問題1：漢字読み",
            "mondai_vi": "Cách đọc Kanji",
            "prompt": "自分の部屋を<u>片付けて</u>、気分もすっきりした。",
            "prompt_vi": "Dọn dẹp gọn gàng căn phòng của mình xong, tâm trạng cũng sảng khoái hẳn lên.",
            "options": ["かたづけて", "かたずけて", "へんづけて", "かたつけて"],
            "ans": 1,
            "cute_right_msg": "Bẫy `づ` vs `ず` kinh điển của JLPT không làm khó được em luôn! `片付ける` đọc bằng **づ** nhé! 🧹✨",
            "right_exp": "`片付ける` đọc chuẩn là **かたづける** (với chữ `づ` do biến âm từ `片 + 付ける / つける`). Rất nhiều người hay viết nhầm `ず`.",
            "cute_wrong_msg": "Cẩn thận lỗi chính tả bàn phím hay gặp nha em! `片＋付（つ）ける` biến âm từ hàng つ phải giữ âm **づ** (`かたづける`) nhé! 💖",
            "wrong_exps": [
                "Chính xác! `片付（かたづ）ける` — âm `づ` đúng chuẩn quy tắc.",
                "Sai chính tả kana `ず`: nguồn gốc từ `つける` nên bắt buộc là `づ`.",
                "Chữ `片` ở đây đọc âm Kun `かた`.",
                "Thiếu biến âm đục: `つけ → づけ`."
            ],
            "source_ref": {"novel": "romcom", "chapter": 4, "lesson_id": "p1_c02_b02", "label": "Bộ 1 Romcom Ch.04 (Bài 5: Việc nhà)"}
        },
        {
            "num": 5,
            "mondai": "問題1：漢字読み",
            "mondai_vi": "Cách đọc Kanji",
            "prompt": "新しいデータをもとに、事故の本当の原因を<u>解明</u>する。",
            "prompt_vi": "Dựa trên dữ liệu mới để làm sáng tỏ nguyên nhân thực sự của vụ tai nạn.",
            "options": ["かいめい", "かいけつ", "かいかく", "げめい"],
            "ans": 1,
            "cute_right_msg": "Chuẩn luôn! `解明（かいめい）` = Giải Minh (làm sáng tỏ bí ẩn/nguyên nhân)! 🔬",
            "right_exp": "`解明` đọc là **かいめい** (Giải Minh: phân tích giải thích làm sáng tỏ điều chưa rõ).",
            "cute_wrong_msg": "Đọc âm On từng chữ nhẹ nhàng nè: Giải (`かい`) + Minh (`めい` trong 説明/証明) = `かいめい`! 🌟",
            "wrong_exps": [
                "Chính xác! `解明（かいめい）する` = làm sáng tỏ.",
                "`かいけつ` là chữ `解決` (giải quyết vấn đề).",
                "`かいかく` là chữ `改革` (cải cách).",
                "`げめい` không phải âm đọc của `解明`."
            ],
            "source_ref": {"novel": "isekai", "chapter": 5, "lesson_id": "p1_c08_b02", "label": "Bộ 3 Isekai Ch.05 (Bài 19: Khoa học)"}
        },
        # --- 問題2: 表記 (6-10) ---
        {
            "num": 6,
            "mondai": "問題2：表記",
            "mondai_vi": "Chọn Kanji đúng",
            "prompt": "テスト前に徹夜をして勉強したので、授業中つい<u>いねむり</u>をしてしまった。",
            "prompt_vi": "Vì thức trắng đêm học trước kỳ thi nên trong giờ học tôi lỡ ngủ gật mất.",
            "options": ["居眠り", "座眠り", "寝眠り", "入眠り"],
            "ans": 1,
            "cute_right_msg": "Đỉnh quá! Ngủ gật khi đang ngồi thức = `居（い）` + `眠り（ねむり）` → `居眠り（いねむり）`! 😴📘",
            "right_exp": "`居眠り（いねむり）` = ngủ gật (đang ngồi/ở nguyên tại chỗ mà ngủ thiếp đi).",
            "cute_wrong_msg": "Nhớ hình ảnh ngồi ngay trên ghế lớp học mà ngủ gục: dùng chữ `居` (`いる` — đang ở yên chỗ) ghép với `眠り` thành `居眠り` nhé em! 🌸",
            "wrong_exps": [
                "Chính xác! `居眠（いねむ）りをする` = ngủ gật.",
                "Không ghép thành `座眠り`.",
                "Không viết `寝眠り`.",
                "`入眠（にゅうみん）` là thuật ngữ y học 'bắt đầu chìm vào giấc ngủ'."
            ],
            "source_ref": {"novel": "romcom", "chapter": 7, "lesson_id": "p1_c05_b01", "label": "Bộ 1 Romcom Ch.07 (Bài 10: Trường học)"}
        },
        {
            "num": 7,
            "mondai": "問題2：表記",
            "mondai_vi": "Chọn Kanji đúng",
            "prompt": "どんな仕事でも、社会のルールを<u>じゅんしゅ</u>することが求められる。",
            "prompt_vi": "Bất kể công việc nào cũng đòi hỏi phải tuân thủ nghiêm túc các quy tắc xã hội.",
            "options": ["準守", "順守", "遵守", "純守"],
            "ans": 3,
            "cute_right_msg": "Quá xịn!! Chữ Kanji `遵（じゅん）` trong `遵守（じゅんしゅ）` có bộ quay sước `⻌` siêu chuẩn sách Shinkanzen luôn! ⚖️",
            "right_exp": "`遵守（じゅんしゅ）` (Tuân Thủ — giữ gìn tuân theo nghiêm ngặt luật lệ) dùng chữ `遵` (cũng có cách viết thông dụng thay thế trên báo chí là `順守`, nhưng chuẩn giáo trình Shinkanzen & chữ Hán gốc là `遵守`).",
            "cute_wrong_msg": "Chú ý chữ `遵（じゅん）` (Tuân — tuân theo pháp luật, quy tắc) có bộ quay sước `⻌` cùng phần trên là `尊` → `遵守` nha em! ✨",
            "wrong_exps": [
                "`準` là chuẩn bị/tiêu chuẩn (`準備・基準`).",
                "Tuy báo chí đôi khi viết đơn giản hóa bằng `順守`, đáp án chữ Hán chuẩn gốc JLPT & Shinkanzen N2 là `遵守`.",
                "Chính xác tuyệt đối! `遵守（じゅんしゅ）` = tuân thủ nghiêm chỉnh.",
                "`純` là thuần khiết (`純粋`)."
            ],
            "source_ref": {"novel": "isekai", "chapter": 3, "lesson_id": "p1_c07_b04", "label": "Bộ 3 Isekai Ch.03 (Bài 17: Pháp luật)"}
        },
        {
            "num": 8,
            "mondai": "問題2：表記",
            "mondai_vi": "Chọn Kanji đúng",
            "prompt": "この商品は<u>こうりつ</u>よく電力を生み出すことができる。",
            "prompt_vi": "Sản phẩm này có thể sản sinh ra điện năng một cách đạt hiệu suất cao.",
            "options": ["高率", "効率", "功立", "行率"],
            "ans": 2,
            "cute_right_msg": "Chính xác! `効率（こうりつ）` = Hiệu Suất (`効果` + `比率`), chuẩn không cần chỉnh! ⚡",
            "right_exp": "**効率（こうりつ）** (Hiệu Suất) chỉ mức độ đạt được kết quả cao so với công sức/năng lượng bỏ ra (`効率が良い・効率よく`).",
            "cute_wrong_msg": "Chữ 'Hiệu' trong `効果（こうか）` ghép với 'Suất' (`率`) tạo thành `効率（こうりつ）` nha em! Đừng nhầm với chữ `高` (cao) nhé~ 💡",
            "wrong_exps": [
                "Không có cụm `高率よく` (tỉ lệ cao dùng tính từ riêng, không dùng như `効率よく`).",
                "Chính xác! `効率（こうりつ）よく` = một cách hiệu quả, năng suất cao.",
                "`功立` không có nghĩa này.",
                "`行率` không tồn tại."
            ],
            "source_ref": {"novel": "isekai", "chapter": 5, "lesson_id": "p1_c08_b02", "label": "Bộ 3 Isekai Ch.05 (Bài 19: Khoa học)"}
        },
        {
            "num": 9,
            "mondai": "問題2：表記",
            "mondai_vi": "Chọn Kanji đúng",
            "prompt": "画面を<u>かくだい</u>して、細かな部分を確認する。",
            "prompt_vi": "Phóng to màn hình lên để kiểm tra các chi tiết nhỏ.",
            "options": ["確大", "拡大", "各台", "角大"],
            "ans": 2,
            "cute_right_msg": "Chuẩn luôn! Bộ `扌` (bàn tay mở rộng) `拡（かく）` + `大（だい）` = `拡大（かくだい）` (phóng to, mở rộng)! 🖥️",
            "right_exp": "**拡大（かくだい）** (Khuếch Đại) là phóng to hình ảnh/màn hình hoặc mở rộng quy mô (trái nghĩa với `縮小（しゅくしょう）` — thu nhỏ).",
            "cute_wrong_msg": "Cài sẵn mẹo phân biệt nhé em: phóng to ảnh/quy mô phải có chữ `拡` (bàn tay mở rộng không gian) + `大` = `拡大`, không phải `確` (chính xác)! 🔍",
            "wrong_exps": [
                "`確` là xác thực chắc chắn (`確認・正確`).",
                "Chính xác! `画面を拡大（かくだい）する` = phóng to màn hình.",
                "`各台` không có nghĩa phóng to.",
                "`角大` không có nghĩa này."
            ],
            "source_ref": {"novel": "yandere", "chapter": 3, "lesson_id": "p1_c06_b02", "label": "Bộ 2 Yandere Ch.03 (Bài 13: Máy tính)"}
        },
        # Chú ý Q9 prompt ở trên có chữ thử nháp "? ではなく", let's keep prompt clean JLPT style -> will edit right after saving or let's inspect! Actually we can fix that cleanly right after write_file.
        {
            "num": 10,
            "mondai": "問題2：表記",
            "mondai_vi": "Chọn Kanji đúng",
            "prompt": "大切な仕事のときは、前もって計画を立てて<u>じゅうぶん</u>な準備をしておこう。",
            "prompt_vi": "Khi có công việc quan trọng, hãy chuẩn bị đầy đủ chu đáo từ trước.",
            "options": ["十分", "重分", "充文", "中分"],
            "ans": 1,
            "cute_right_msg": "Tuyệt vời! `十分な（じゅうぶん）` viết đơn giản là `十分` (hoặc `充分`), chuẩn bài JLPT luôn! ✨",
            "right_exp": "**十分（じゅうぶん）** = đầy đủ, dư sức, thỏa đáng (`十分な準備・時間が十分にある`).",
            "cute_wrong_msg": "Âm `じゅうぶん` nghĩa 'đầy đủ' dùng chữ số 10 `十` + `分` = `十分` nha em! 💖",
            "wrong_exps": [
                "Chính xác! `十分な準備` = sự chuẩn bị đầy đủ.",
                "Không viết là `重分` (trùng hợp âm `じゅう` của `重` là nặng).",
                "`充` viết là `充分` mới có, không phải `充文`.",
                "`中分` đọc là `ちゅうぶん`."
            ],
            "source_ref": {"novel": "yandere", "chapter": 9, "lesson_id": "p2_c04_b01", "label": "Bộ 2 Yandere Ch.09 (Bài 28: Phó từ)"}
        },
        # --- 問題3: 語形成 (11-15) ---
        {
            "num": 11,
            "mondai": "問題3：語形成",
            "mondai_vi": "Cấu tạo từ (Tiền tố / Hậu tố)",
            "prompt": "このアパートは広くて部屋数も多いので、一人暮らしよりも（　　）<u>向き</u>だ。",
            "prompt_vi": "Căn hộ này rộng rãi lại nhiều phòng nên phù hợp cho hộ gia đình hơn là sống một mình.",
            "options": ["家族", "初心者", "学生", "単身"],
            "ans": 1,
            "cute_right_msg": "Quá chuẩn!! Nhiều phòng rộng rãi mà lại đối lập với `一人暮らし` → đích thị `家族向き（かぞくむき）` (phù hợp với gia đình) rồi! 🏡",
            "right_exp": "`家族向き` = có đặc điểm tự nhiên phù hợp cho gia đình sinh sống (`広くて部屋数も多い`). Hậu tố `〜向き` chỉ sự phù hợp dựa theo tính chất vốn có.",
            "cute_wrong_msg": "Đọc kỹ manh mối 'rộng rãi và nhiều phòng, phù hợp hơn sống một mình' nha em → đáp án trái ngược với sống 1 mình chính là `家族（かぞく）`! 🌸",
            "wrong_exps": [
                "Chính xác! `家族向きのアパート` = căn hộ phù hợp cho gia đình.",
                "`初心者` là người mới bắt đầu (không liên quan căn hộ nhiều phòng).",
                "`学生` thường sống trọ phòng nhỏ, mâu thuẫn với 'hơn là sống 1 mình ở nhà rộng nhiều phòng'.",
                "`単身` chính là độc thân một mình (mâu thuẫn với `一人暮らしより`)."
            ],
            "source_ref": {"novel": "isekai", "chapter": 11, "lesson_id": "p2_c07_b03", "label": "Bộ 3 Isekai Ch.11 (Bài 36: Hậu tố)"}
        },
        {
            "num": 12,
            "mondai": "問題3：語形成",
            "mondai_vi": "Cấu tạo từ (Tiền tố / Hậu tố)",
            "prompt": "彼は（　　）<u>責任</u>な発言ばかりするので、周りの人から信用されなくなった。",
            "prompt_vi": "Anh ta toàn phát ngôn vô trách nhiệm nên dần mất hết lòng tin từ mọi người xung quanh.",
            "options": ["無", "不", "非", "反"],
            "ans": 1,
            "cute_right_msg": "Chuẩn không cần chỉnh! `無責任（むせきにん）` = hoàn toàn không có tinh thần trách nhiệm! ✨",
            "right_exp": "Tiền tố **無（む）** biểu thị sự thiếu vắng hoàn toàn (0%): `無責任` (vô trách nhiệm), `無関係` (không liên quan), `無料` (miễn phí).",
            "cute_wrong_msg": "Từ ghép với `責任` để chỉ 'vô trách nhiệm' luôn dùng **無（む）** (`無責任`), không dùng `不` hay `非` nha em! 💡",
            "wrong_exps": [
                "Chính xác tuyệt đối! `無責任（むせきにん）な発言`.",
                "Không có từ `不責任` trong tiếng Nhật.",
                "Không có từ `非責任` trong tiếng Nhật.",
                "Không dùng `反責任`."
            ],
            "source_ref": {"novel": "isekai", "chapter": 10, "lesson_id": "p2_c07_b02", "label": "Bộ 3 Isekai Ch.10 (Bài 35: Tiền tố)"}
        },
        {
            "num": 13,
            "mondai": "問題3：語形成",
            "mondai_vi": "Cấu tạo từ (Tiền tố / Hậu tố)",
            "prompt": "この川の水はきれいで、（　　）<u>性</u>も確認されているので安心して飲める。",
            "prompt_vi": "Nước dòng sông này sạch lắm, ngay cả tính an toàn cũng đã được xác nhận nên cứ yên tâm uống được.",
            "options": ["可能", "重要", "安全", "専門"],
            "ans": 3,
            "cute_right_msg": "Chính xác! Cặp ghép `安全性（あんぜんせい）` đi liền với cụm phía sau 'có thể yên tâm uống' (`安心して飲める`) chuẩn 100%! 💧",
            "right_exp": "`安全性（あんぜんせい）` (tính an toàn) kết hợp cùng hậu tố `〜性` và vế `安心して飲める`.",
            "cute_wrong_msg": "Đọc vế cuối 'vì đã xác nhận rồi nên cứ yên tâm uống' (`安心して飲める`): yên tâm thì phải xác nhận **tính an toàn** (`安全性`) chứ nhỉ! 🌟",
            "wrong_exps": [
                "`可能性` là khả năng/xác suất có thể xảy ra.",
                "`重要性` là tầm quan trọng.",
                "Chính xác! `安全性が確認されている` = tính an toàn đã được kiểm chứng.",
                "`専門性` là tính chuyên môn sâu."
            ],
            "source_ref": {"novel": "isekai", "chapter": 11, "lesson_id": "p2_c07_b03", "label": "Bộ 3 Isekai Ch.11 (Bài 36: Hậu tố)"}
        },
        {
            "num": 14,
            "mondai": "問題3：語形成",
            "mondai_vi": "Cấu tạo từ (Tiền tố / Hậu tố)",
            "prompt": "新しい制度の導入をめぐって、賛成派と（　　）<u>対</u>派の間で激しい議論が行われた。",
            "prompt_vi": "Xoay quanh việc đưa chế độ mới vào áp dụng, một cuộc tranh luận gay gắt đã diễn ra giữa phe tán thành và phe phản đối.",
            "options": ["逆", "無", "反", "非"],
            "ans": 3,
            "cute_right_msg": "Đỉnh luôn! Cặp đối lập siêu quen `賛成` ↔ `反対（はんたい）` dùng tiền tố **反（はん）**! ⚖️",
            "right_exp": "**反対（はんたい）** (Phản Đối) mang tiền tố `反〜` biểu thị sự đối lập, chống lại (`賛成派と反対派`).",
            "cute_wrong_msg": "Cặp đối nghĩa với `賛成（さんせい）` (tán thành) dùng tiền tố `反` ghép với `対` thành `反対（はんたい）` nha em! 🌸",
            "wrong_exps": [
                "`逆対` không tồn tại (`逆` dùng trong `逆転`, `逆方向`).",
                "`無対` không tồn tại.",
                "Chính xác! `賛成派と反対派` = phe ủng hộ và phe phản đối.",
                "`非対` không phải từ này (`非対称` là bất đối xứng)."
            ],
            "source_ref": {"novel": "isekai", "chapter": 10, "lesson_id": "p2_c07_b02", "label": "Bộ 3 Isekai Ch.10 (Bài 35: Tiền tố)"}
        },
        {
            "num": 15,
            "mondai": "問題3：語形成",
            "mondai_vi": "Cấu tạo từ (Tiền tố / Hậu tố)",
            "prompt": "子どもたちは箱から新しいおもちゃが出てくると、とても（　　）<u>がった</u>。",
            "prompt_vi": "Lũ trẻ khi thấy món đồ chơi mới hiện ra từ trong hộp liền tỏ vẻ vô cùng mừng rỡ.",
            "options": ["楽し", "嬉し", "怖", "嫌"],
            "ans": 2,
            "cute_right_msg": "Quá chuẩn! Đứa trẻ nhận đồ chơi mới thì tất nhiên là `嬉しがった` (tỏ vẻ vui sướng mừng rỡ)! 🎁✨",
            "right_exp": "`嬉しがる` (tính từ cảm xúc ngôi thứ 3 `嬉しい` bỏ `い` + `がる`): biểu lộ niềm vui sướng ra bên ngoài (`子どもたちが嬉しがった`).",
            "cute_wrong_msg": "Coi ngữ cảnh trẻ con mở hộp quà thấy đồ chơi mới nha em: cảm xúc mừng rỡ khi được tặng quà là `嬉しい → 嬉しがる`, còn `楽しむ` thường đi thẳng đuôi `む` chứ không nói `楽しがる` đâu nè! 🎈",
            "wrong_exps": [
                "`楽しい` đi trực tiếp với động từ `楽しむ` (chơi vui tận hưởng), người Nhật hầu như KHÔNG dùng `楽しがる`.",
                "Chính xác! `嬉しがる` = tỏ ra vui mừng hớn hở.",
                "`怖がる` là tỏ ra sợ hãi (không hợp cảnh trẻ nhận đồ chơi bình thường).",
                "`嫌がる` là tỏ vẻ ghét bỏ/khó chịu."
            ],
            "source_ref": {"novel": "isekai", "chapter": 12, "lesson_id": "p2_c07_b04", "label": "Bộ 3 Isekai Ch.12 (Bài 37: Tính từ → N/V)"}
        },
        # --- 問題4: 文脈規定 (16-22) ---
        {
            "num": 16,
            "mondai": "問題4：文脈規定",
            "mondai_vi": "Điền từ vựng theo ngữ cảnh",
            "prompt": "朝起きたばかりのときは頭が（　　）していて、まだよく考えられない。",
            "prompt_vi": "Lúc vừa mới ngủ dậy đầu óc vẫn còn lơ mơ ngái ngủ nên chưa suy nghĩ thông suốt được.",
            "options": ["ぼんやり", "はっきり", "すっきり", "ぴったり"],
            "ans": 1,
            "cute_right_msg": "Chuẩn luôn! Mới tỉnh dậy đầu óc lơ mơ ngơ ngác là `頭がぼんやりしている` — đúng bài Yandere Ch.09 (Phó từ)! ☀️😴",
            "right_exp": "`ぼんやり` diễn tả đầu óc mơ màng chưa tỉnh táo hoặc nhìn cảnh vật mờ nhạt không rõ nét.",
            "cute_wrong_msg": "Vế sau nói 'chưa thể suy nghĩ kỹ được' (`よく考えられない`), nên đầu óc lúc đó đang mông lung lờ mờ `ぼんやり` nha em! 🌸",
            "wrong_exps": [
                "Chính xác! `頭がぼんやりする` = đầu óc lơ mơ chưa tỉnh hẳn.",
                "`はっきり` là rõ ràng tỉnh táo (ngược nghĩa).",
                "`すっきり` là sảng khoái nhẹ nhàng đầu óc.",
                "`ぴったり` là khớp vừa vặn in."
            ],
            "source_ref": {"novel": "yandere", "chapter": 9, "lesson_id": "p2_c04_b01", "label": "Bộ 2 Yandere Ch.09 (Bài 28: Phó từ 1)"}
        },
        {
            "num": 17,
            "mondai": "問題4：文脈規定",
            "mondai_vi": "Điền từ vựng theo ngữ cảnh",
            "prompt": "彼女はとても（　　）人で、いつも周りの様子を見て自然にお茶を出してくれる。",
            "prompt_vi": "Cô ấy là người thực sự rất tinh tế chu đáo, lúc nào cũng để ý tình hình xung quanh và tự nhiên mang trà ra mời.",
            "options": ["気が気じゃない", "気が乗らない", "気が利く", "気が置けない"],
            "ans": 3,
            "cute_right_msg": "Quá chuẩn!! Cô gái tinh tế chu đáo biết quan sát trước khi người khác kịp nhờ là `気が利く人`! 🍵💕",
            "right_exp": "`気が利（き）く` = nhanh nhạy, tinh tế, khéo léo quan tâm tới nhu cầu nhỏ nhất của mọi người xung quanh.",
            "cute_wrong_msg": "Phân biệt 4 quán dụng với `気` cực dễ nè em: 'quan sát mọi người rồi tinh tế mang trà ra' chính là `気が利く` (khéo léo tinh ý) đó! ✨",
            "wrong_exps": [
                "`気が気じゃない` = lo lắng bồn chồn đứng ngồi không yên.",
                "`気が乗らない` = không có hứng thú làm việc gì.",
                "Chính xác! `気が利く人` = người tinh tế, chu đáo.",
                "`気が置けない` = thân thiết thoải mái không cần khách sáo giữ kẽ."
            ],
            "source_ref": {"novel": "yandere", "chapter": 12, "lesson_id": "p2_c06_b02", "label": "Bộ 2 Yandere Ch.12 (Bài 33: Quán dụng ngữ 2)"}
        },
        {
            "num": 18,
            "mondai": "問題4：文脈規定",
            "mondai_vi": "Điền từ vựng theo ngữ cảnh",
            "prompt": "このパソコンの（　　）はとてもシンプルで、お年寄りでもすぐに覚えられる。",
            "prompt_vi": "Cách thao tác vận hành của chiếc máy tính này rất đơn giản, ngay cả người lớn tuổi cũng nhanh chóng nhớ được.",
            "options": ["検索（けんさく）", "操作（そうさ）", "再起動（さいきどう）", "保存（ほぞん）"],
            "ans": 2,
            "cute_right_msg": "Chính xác! `パソコンの操作がシンプル` (thao tác sử dụng máy dễ dàng) là từ vựng quen thuộc trong Bộ 2 Ch.03! 💻✨",
            "right_exp": "`操作（そうさ）` = sự thao tác, điều khiển vận hành máy móc/phần mềm (`操作が簡単 / シンプル`).",
            "cute_wrong_msg": "Cách sử dụng bấm nút vận hành máy móc nói chung là `操作（そうさ）` nha em! 🌸",
            "wrong_exps": [
                "`検索` chỉ riêng việc tra cứu tìm kiếm thông tin.",
                "Đúng rồi! `操作（そうさ）` = thao tác vận hành.",
                "`再起動` là khởi động lại máy (restart).",
                "`保存` là lưu file dữ liệu (save)."
            ],
            "source_ref": {"novel": "yandere", "chapter": 3, "lesson_id": "p1_c06_b02", "label": "Bộ 2 Yandere Ch.03 (Bài 13: Máy tính)"}
        },
        {
            "num": 19,
            "mondai": "問題4：文脈規定",
            "mondai_vi": "Điền từ vựng theo ngữ cảnh",
            "prompt": "新しい規則を守ることは当然だが、時代の変化に合わせて法律を（　　）することも大切だ。",
            "prompt_vi": "Việc tuân thủ quy định mới là đương nhiên, nhưng việc sửa đổi luật pháp cho phù hợp với thay đổi của thời đại cũng rất quan trọng.",
            "options": ["改正（かいせい）", "逮捕（たいほ）", "目撃（もくげき）", "伝染（でんせん）"],
            "ans": 1,
            "cute_right_msg": "Quá chuẩn! `時代の変化に合わせて法律を改正する` là câu ví dụ vàng trong bài Chính trị-Pháp luật Isekai Ch.03 luôn! ⚖️",
            "right_exp": "`改正（かいせい）する` = sửa đổi, điều chỉnh lại cho đúng/phù hợp hơn (dùng cho luật pháp, quy chế, lịch trình tàu xe, giá cả).",
            "cute_wrong_msg": "Đọc cụm 'điều chỉnh lại luật sao cho hợp thời đại': động từ có chữ `改` (cải) + `正` (chính) là `改正する` nhé em! 📜",
            "wrong_exps": [
                "Chính xác! `法律を改正する` = sửa đổi luật pháp.",
                "`逮捕する` là bắt giữ tội phạm.",
                "`目撃する` là tận mắt chứng kiến tai nạn/vụ việc.",
                "`伝染する` là lây lan dịch bệnh."
            ],
            "source_ref": {"novel": "isekai", "chapter": 3, "lesson_id": "p1_c07_b04", "label": "Bộ 3 Isekai Ch.03 (Bài 17: Pháp luật)"}
        },
        {
            "num": 20,
            "mondai": "問題4：文脈規定",
            "mondai_vi": "Điền từ vựng theo ngữ cảnh",
            "prompt": "彼はいつも明るく元気そうに見えるが、実は誰にも言えない（　　）な悩みを抱えているようだ。",
            "prompt_vi": "Anh ấy nhìn bề ngoài lúc nào cũng có vẻ vui tươi khỏe khoắn, nhưng thực ra dường như đang ôm nỗi phiền muộn sâu sắc chẳng thể nói cùng ai.",
            "options": ["陽気（ようき）", "深刻（しんこく）", "単純（たんじゅん）", "穏（おだ）やか"],
            "ans": 2,
            "cute_right_msg": "Chuẩn không cần chỉnh! `深刻（しんこく）な悩み・問題` (nỗi lo âu / vấn đề nghiêm trọng sâu sắc)! 💭",
            "right_exp": "`深刻（しんこく）な` = nghiêm trọng, sâu sắc, trầm trọng (`深刻な悩み / 不況 / 問題`).",
            "cute_wrong_msg": "'Nỗi phiền muộn nặng nề không thể tâm sự cùng ai' đi cặp chuẩn nhất với tính từ `深刻な` (trầm trọng/sâu sắc) nha em! 🖤",
            "wrong_exps": [
                "`陽気な` = vui vẻ sôi nổi (trùng vế đầu chứ không hợp với 'nỗi lo giấu kín').",
                "Chính xác! `深刻な悩み` = nỗi phiền muộn sâu sắc.",
                "`単純な` = đơn giản ngây thơ.",
                "`穏やかな` = hiền hòa, êm ả (`穏やかな天気・性格`)."
            ],
            "source_ref": {"novel": "romcom", "chapter": 12, "lesson_id": "p2_c02_b01", "label": "Bộ 1 Romcom Ch.12 (Bài 25: Từ gần nghĩa)"}
        },
        {
            "num": 21,
            "mondai": "問題4：文脈規定",
            "mondai_vi": "Điền từ vựng theo ngữ cảnh",
            "prompt": "あの二人は考え方も趣味も（　　）違っていて、まるで正反対だ。",
            "prompt_vi": "Hai người kia từ cách suy nghĩ đến sở thích đều khác biệt hoàn toàn, cứ như hai thái cực trái ngược hẳn nhau vậy.",
            "options": ["すっかり", "そっくり", "うっかり", "がっかり"],
            "ans": 1,
            "cute_right_msg": "Phân biệt chuẩn đét cặp song sinh âm `すっかり` (hoàn toàn toàn bộ) vs `そっくり` (giống hệt nhau như đúc)! 👯‍♀️✨",
            "right_exp": "`すっかり` diễn tả sự *hoàn toàn 100%* (`すっかり忘れていた`, `すっかり違っている`). Còn `そっくり` là 'giống hệt nhau', sẽ mâu thuẫn hoàn toàn với 'khác biệt / trái ngược' (`違っている・正反対`).",
            "cute_wrong_msg": "Hihi cái bẫy kinh điển `すっかり` vs `そっくり` đó em!! Ở đây vế sau là `違っている` (khác biệt trái ngược), không thể chọn 'giống hệt' (`そっくり`) mà phải là 'hoàn toàn' (`すっかり`) nha! 🌸",
            "wrong_exps": [
                "Chính xác! `すっかり違っている` = khác biệt hoàn toàn 100%.",
                "`そっくり` là giống y hệt (mâu thuẫn trực tiếp với `違っている・正反対`!).",
                "`うっかり` là lơ đễnh sơ suất.",
                "`がっかり` là thất vọng chán nản."
            ],
            "source_ref": {"novel": "yandere", "chapter": 9, "lesson_id": "p2_c04_b01", "label": "Bộ 2 Yandere Ch.09 (Bài 28: Phó từ 1)"}
        },
        {
            "num": 22,
            "mondai": "問題4：文脈規定",
            "mondai_vi": "Điền từ vựng theo ngữ cảnh",
            "prompt": "長い間大切にしていた時計をなくしてしまい、見つかるまで（　　）。",
            "prompt_vi": "Làm mất chiếc đồng hồ quý giữ gìn bao năm trời, cho đến khi tìm lại được tôi cứ đứng ngồi không yên lòng như lửa đốt.",
            "options": ["気が気じゃなかった", "目がなかった", "鼻が高かった", "顔が広かった"],
            "ans": 1,
            "cute_right_msg": "Quá chuẩn!! `気が気じゃない` = lòng dạ rối bời lo lắng đứng ngồi không yên! ⌚💓",
            "right_exp": "`気が気じゃない` nghĩa là lo lắng bồn chồn đến độ đứng ngồi không yên (`帰りが遅くて気が気じゃない`).",
            "cute_wrong_msg": "Mất món đồ cực quý chưa tìm thấy thì tâm trạng lúc đó là bồn chồn lo lắng không yên → `気が気じゃなかった` nha em! 🌸",
            "wrong_exps": [
                "Chính xác! `気が気じゃなかった` = lo lắng đứng ngồi không yên.",
                "`目がなかった` = cực kỳ mê mẩn đồ gì đó (như đồ ngọt `甘いものに目がない`).",
                "`鼻が高かった` = hãnh diện tự hào nở mũi.",
                "`顔が広かった` = quen biết giao thiệp rộng."
            ],
            "source_ref": {"novel": "yandere", "chapter": 12, "lesson_id": "p2_c06_b02", "label": "Bộ 2 Yandere Ch.12 (Bài 33: Quán dụng ngữ 2)"}
        },
        # --- 問題5: 言い換え類義 (23-27) ---
        {
            "num": 23,
            "mondai": "問題5：言い換え類義",
            "mondai_vi": "Từ / cụm từ đồng nghĩa",
            "prompt": "新商品の良さを多くの人に知ってもらうため、テレビで<u>大々的</u>に宣伝した。",
            "prompt_vi": "Để nhiều người biết đến điểm hay của sản phẩm mới, chúng tôi đã quảng cáo rầm rộ quy mô lớn trên truyền hình.",
            "options": ["こっそり", "大規模に", "わずか", "一時的に"],
            "ans": 2,
            "cute_right_msg": "Chuẩn không cần chỉnh! `大々的（だいだいてき）に` = quy mô rầm rộ lớn lao (`大規模に`)! 📺✨",
            "right_exp": "`大々的（だいだいてき）に` = một cách rầm rộ, hoành tráng trên quy mô lớn ≈ `大規模に・派手に`.",
            "cute_wrong_msg": "Nhìn hai chữ Đại Đại (`大々的`) siêu to khổng lồ là đoán ngay đồng nghĩa `大規模に` (trên quy mô lớn) liền ha em~ 💡",
            "wrong_exps": [
                "`こっそり` là lén lút âm thầm (trái nghĩa).",
                "Chính xác! `大々的に` = `大規模に` (trên quy mô lớn rầm rộ).",
                "`わずか` là ít ỏi nhỏ bé.",
                "`一時的に` là tạm thời chốc lát."
            ],
            "source_ref": {"novel": "romcom", "chapter": 9, "lesson_id": "p1_c06_b01", "label": "Bộ 1 Romcom Ch.09 (Bài 12: Truyền thông)"}
        },
        {
            "num": 24,
            "mondai": "問題5：言い換え類義",
            "mondai_vi": "Từ / cụm từ đồng nghĩa",
            "prompt": "兄はとても<u>口が堅い</u>から、大切な秘密を相談しても絶対に安心だ。",
            "prompt_vi": "Anh trai tôi rất kín miệng nên dù có tâm sự bí mật quan trọng cũng hoàn toàn yên tâm.",
            "options": ["言葉が丁寧だ", "秘密をよく守る", "おしゃべりが好きだ", "無口でおとなしい"],
            "ans": 2,
            "cute_right_msg": "Đỉnh luôn!! Nhớ kỹ `口が堅い` là *giữ bí mật giỏi* (có thể nói nhiều chuyện khác bình thường, chứ không hẳn là `無口` ít nói đâu nha)! 🤐✨",
            "right_exp": "`口が堅（かた）い` = kín miệng, đáng tin cậy, tuyệt đối không để lộ bí mật của người khác (`秘密をよく守る`).",
            "cute_wrong_msg": "Coi chừng nhầm `口が堅い` (kín miệng giữ bí mật giỏi) với `無口（むくち）` (tính trầm ít nói) nha em! Người kín miệng vẫn có thể giao tiếp vui vẻ, chỉ là họ **giữ bí mật cực chuẩn** thôi! 🌸",
            "wrong_exps": [
                "`言葉が丁寧だ` = ăn nói lịch sự nhã nhặn.",
                "Chính xác tuyệt đối! `口が堅い` = giữ bí mật rất kín.",
                "`おしゃべりが好きだ` gần với `口が軽い` (bép xép hay hớ lời - trái nghĩa!).",
                "`無口（むくち）` là người ít nói trầm tính (không đồng nghĩa với 'giữ được bí mật')."
            ],
            "source_ref": {"novel": "romcom", "chapter": 13, "lesson_id": "p2_c06_b01", "label": "Bộ 1 Romcom Ch.13 (Bài 32: Quán dụng ngữ 1)"}
        },
        {
            "num": 25,
            "mondai": "問題5：言い換え類義",
            "mondai_vi": "Từ / cụm từ đồng nghĩa",
            "prompt": "このテストの問題は、私にとっては<u>さほど</u>難しくなかった。",
            "prompt_vi": "Đề bài kiểm tra này đối với tôi cũng không đến mức quá khó lắm đâu.",
            "options": ["たいして", "まるで", "けっして", "あいにく"],
            "ans": 1,
            "cute_right_msg": "Quá chuẩn!! Phó từ hô ứng phủ định `さほど〜ない` = `たいして〜ない` / `それほど〜ない` (không đến mức lắm)! 📝🌟",
            "right_exp": "`さほど〜ない` (giống `たいして〜ない` / `それほど〜ない`): không đến nỗi / không đến mức quá... lắm đâu.",
            "cute_wrong_msg": "Bắt cặp phó từ phủ định trong Yandere Ch.10 nè em: `さほど〜ない` nghĩa nhẹ nhàng hơn 'hoàn toàn không', nó đồng nghĩa với `たいして〜ない` (không đến mức lắm đâu)! 💖",
            "wrong_exps": [
                "Chính xác! `さほど〜ない` ≈ `たいして〜ない` (không quá mức lắm).",
                "`まるで〜ない` nghĩa quá mạnh ('hoàn toàn không một chút nào' / 'như thể là...').",
                "`けっして〜ない` là 'tuyệt đối không bao giờ' (diễn tả quyết tâm/lời thề mạnh mẽ, không dùng cho cảm nhận độ khó bài thi bình thường).",
                "`あいにく` = thật không may đúng lúc..."
            ],
            "source_ref": {"novel": "yandere", "chapter": 10, "lesson_id": "p2_c04_b02", "label": "Bộ 2 Yandere Ch.10 (Bài 29: Phó từ hô ứng)"}
        },
        {
            "num": 26,
            "mondai": "問題5：言い換え類義",
            "mondai_vi": "Từ / cụm từ đồng nghĩa",
            "prompt": "台風の影響で、明日の飛行機の出発が<u>わずかに</u>遅れるそうだ。",
            "prompt_vi": "Do ảnh hưởng bão, nghe nói chuyến bay ngày mai sẽ bị trễ một chút ít.",
            "options": ["大幅に", "ほんの少し", "完全に", "次々に"],
            "ans": 2,
            "cute_right_msg": "Chính xác! `わずかに` = `ほんの少し` (chỉ một chút xíu ít ỏi thôi)! ✈️",
            "right_exp": "`わずか（に）` = chỉ một chút ít, vỏn vẹn, số lượng/mức độ rất nhỏ (`ほんの少し`).",
            "cute_wrong_msg": "Từ `わずか` mang nghĩa rất ít/chút xíu (`ほんの少し`), trái ngược hoàn toàn với 'rất nhiều / đáng kể' (`大幅に`) nha em! ✨",
            "wrong_exps": [
                "`大幅に` là trên diện rộng/rất nhiều (trái nghĩa!).",
                "Tuyệt vời! `わずかに` = `ほんの少し` (một chút xíu).",
                "`完全に` là hoàn toàn 100%.",
                "`次々に` là liên tiếp hết cái này tới cái khác."
            ],
            "source_ref": {"novel": "isekai", "chapter": 6, "lesson_id": "p1_c09_b01", "label": "Bộ 3 Isekai Ch.06 (Bài 20: Số lượng)"}
        },
        {
            "num": 27,
            "mondai": "問題5：言い換え類義",
            "mondai_vi": "Từ / cụm từ đồng nghĩa",
            "prompt": "最近、彼女はどうも様子がおかしくて、<u>気がかりだ</u>。",
            "prompt_vi": "Dạo này trông cô ấy cứ sao sao lạ lắm, làm tôi thấy bận tâm lo lắng quá.",
            "options": ["楽しみだ", "うらやましい", "心配だ", "退屈だ"],
            "ans": 3,
            "cute_right_msg": "Chuẩn luôn! `気がかりだ` (vướng bận trong lòng = lo lắng `心配だ`) — gặp ngay ở Bộ 2 Yandere Ch.08 (Từ đồng âm/dễ nhầm)! 🌹",
            "right_exp": "`気がかり（な・だ）` = cứ vướng bận mãi trong tâm trí, khiến mình thấy lo âu bất an ≈ `心配だ`.",
            "cute_wrong_msg": "Nhìn chữ Kanji `気` (tâm trí) + `掛かり` (vướng mắc treo lơ lửng): cái gì cứ treo trong lòng khiến mình bất an chính là lo lắng = `心配だ` đó em! 💌",
            "wrong_exps": [
                "`楽しみだ` là háo hức mong chờ.",
                "`うらやましい` là ghen tị ngưỡng mộ.",
                "Chính xác! `気がかりだ` = `心配だ` (lo lắng, bận tâm).",
                "`退屈だ` là buồn chán vô vị."
            ],
            "source_ref": {"novel": "yandere", "chapter": 8, "lesson_id": "p2_c03_b01", "label": "Bộ 2 Yandere Ch.08 (Bài 27: Dễ nhầm lẫn)"}
        },
        # --- 問題6: 用法 (28-32) ---
        {
            "num": 28,
            "mondai": "問題6：用法",
            "mondai_vi": "Cách dùng từ đúng trong câu",
            "prompt": "次の言葉の使い方として最もよいものを、1・2・3・4から一つ選びなさい。\n【言葉：<b><u>ふもと</u></b>】",
            "prompt_vi": "Chọn câu sử dụng đúng nhất từ 【ふもと】 (chân núi).",
            "options": [
                "テーブルのふもとにスマホが落ちていたので拾った。",
                "あの大きなビルのふもとで待ち合わせをしよう。",
                "富士山のふもとに広がる温泉街でゆっくり休んだ。",
                "木のふもとに座って、涼しい日陰で本を読んだ。"
            ],
            "ans": 3,
            "cute_right_msg": "Quá chuẩn! `ふもと` CHỈ dùng cho **núi / đồi lớn** (`山のふもと`), KHÔNG dùng cho cái bàn, tòa nhà hay gốc cây đâu nhé! 🏔️✨",
            "right_exp": "`ふもと（麓）` chỉ khu vực **chân núi / vùng đất nằm sát dưới sườn núi**. Chân bàn dùng `テーブルの下`, gốc cây dùng `木の下 / 根元`, chân tòa nhà dùng `ビルの下 / 入口付近`.",
            "cute_wrong_msg": "Quy tắc vàng cho `ふもと`: chữ Kanji của nó có hai cái cây bên dưới chữ Lâm & Lộc (`麓`) chỉ **chân ngọn núi** thôi, không dùng cho bàn, nhà cao tầng hay cái cây đâu nha! 🌱",
            "wrong_exps": [
                "Dưới gầm bàn dùng `テーブルの下`, không dùng `ふもと`.",
                "Chân tòa cao ốc dùng `ビルの下 / 前`, không dùng `ふもと`.",
                "Chính xác tuyệt đối! `富士山のふもと` (dưới chân núi Phú Sĩ).",
                "Gốc cây dùng `木の下 / 根元（ねもと）`, không dùng `ふもと`."
            ],
            "source_ref": {"novel": "isekai", "chapter": 1, "lesson_id": "p1_c04_b02", "label": "Bộ 3 Isekai Ch.01 (Bài 9: Thiên nhiên)"}
        },
        {
            "num": 29,
            "mondai": "問題6：用法",
            "mondai_vi": "Cách dùng từ đúng trong câu",
            "prompt": "次の言葉の使い方として最もよいものを、1・2・3・4から一つ選びなさい。\n【言葉：<b><u>ぐっすり</u></b>】",
            "prompt_vi": "Chọn câu sử dụng đúng nhất từ 【ぐっすり】 (ngủ say sưa ngon lành).",
            "options": [
                "今日はたくさん歩いたので、夜は朝までぐっすり眠った。",
                "大事な面接の前で緊張しすぎて、昨日からぐっすりしている。",
                "部屋を掃除したら、ほこりが取れてぐっすりきれいになった。",
                "会議中なのに、コーヒーを飲まないとすぐぐっすりなる。"
            ],
            "ans": 1,
            "cute_right_msg": "Tuyệt vời! `ぐっすり` chuyên đi với động từ `眠る・寝る` (ngủ say sưa không biết trời đất)! 😴🌙",
            "right_exp": "`ぐっすり` là từ tượng hình CHỈ ĐỘ SÂU GIẤC NGỦ (`ぐっすり眠る・寝る`). Không dùng với `緊張` (dùng `どきどき`), `きれい` (`すっきり / さっぱり`), hay buồn ngủ gật ngắn giữa họp (`うとうと`).",
            "cute_wrong_msg": "Phó từ `ぐっすり` hầu như là bạn chung thân duy nhất của động từ **眠る / 寝る** (ngủ sâu cả đêm) nha em~ Không dùng để tả sạch sẽ (`すっきり`) hay gật gù trong cuộc họp (`うとうと`) đâu nhé! 🌸",
            "wrong_exps": [
                "Chính xác! `朝までぐっすり眠った` = ngủ say giấc đến tận sáng.",
                "Căng thẳng tim đập mạnh dùng `どきどき`, không dùng `ぐっすり`.",
                "Sạch sẽ gọn gàng dùng `すっきり`, không dùng `ぐっすり`.",
                "Ngủ gà gật giữa cuộc họp dùng `うとうと`, `ぐっすり` là ngủ say sưa."
            ],
            "source_ref": {"novel": "isekai", "chapter": 8, "lesson_id": "p2_c05_b01", "label": "Bộ 3 Isekai Ch.08 (Bài 31: Onomatopoeia)"}
        },
        {
            "num": 30,
            "mondai": "問題6：用法",
            "mondai_vi": "Cách dùng từ đúng trong câu",
            "prompt": "次の言葉の使い方として最もよいものを、1・2・3・4から一つ選びなさい。\n【言葉：<b><u>いたわる</u></b>】",
            "prompt_vi": "Chọn câu sử dụng đúng nhất từ 【いたわる】 (chăm nom ân cần người yếu/già/ốm/mệt mỏi).",
            "options": [
                "試験に100点を取って優勝した弟を、拍手して大きくいたわった。",
                "風邪で寝込んでいる母の体を気づかって、優しくいたわった。",
                "約束の時間に遅れた友達を、厳しくいたわって注意した。",
                "毎日大切にパソコンをいたわって使っているので、まだ壊れない。"
            ],
            "ans": 2,
            "cute_right_msg": "Đỉnh cao ngữ nghĩa! `いたわる` là sự **ân cần chăm nom xoa dịu người đang yếu/mệt/lớn tuổi**, không dùng cho đồ vật hay khen thắng giải/mắng bạn đâu nha! 💕",
            "right_exp": "`いたわる` (Chăm nom ân cần người mệt mỏi, ốm đau, người lớn tuổi hoặc chịu thiệt thòi) chỉ dùng cho **con người** đang ở trạng thái mệt/yếu cần vỗ về chăm sóc.",
            "cute_wrong_msg": "Chị Yuki nhắc nhẹ phân biệt siêu rõ ở Yandere Ch.01 nè em: động viên người có công/mệt việc là `労う（ねぎらう）`; còn chăm nom an ủi người **ốm/mệt/người già** là `いたわる` (không dùng cho đồ vật hay chúc mừng thắng giải)! 🌸",
            "wrong_exps": [
                "Chúc mừng tán dương em giành giải dùng `褒める・祝う・労う`, không dùng `いたわる`.",
                "Chính xác! Quan tâm chăm sóc mẹ đang ốm nằm giường (`母をいたわった`).",
                "Mắng nhắc bạn đi muộn dùng `注意する・叱る`, trái nghĩa với ân cần vỗ về `いたわる`.",
                "Giữ gìn cẩn thận đồ vật dùng `大切にする・大事に扱う`, không dùng `いたわる`."
            ],
            "source_ref": {"novel": "yandere", "chapter": 1, "lesson_id": "p1_c01_b03", "label": "Bộ 2 Yandere Ch.01 (Bài 3: Cảm xúc)"}
        },
        {
            "num": 31,
            "mondai": "問題6：用法",
            "mondai_vi": "Cách dùng từ đúng trong câu",
            "prompt": "次の言葉の使い方として最もよいものを、1・2・3・4から一つ選びなさい。\n【言葉：<b><u>手につかない</u></b>】",
            "prompt_vi": "Chọn câu sử dụng đúng nhất từ 【手につかない】 (không thể tập trung làm việc gì nổi vì lo âu/bồn chồn).",
            "options": [
                "この新しいのりは質が悪くて、紙に塗っても全然手につかない。",
                "合格発表の結果が気になりすぎて、朝から勉強が手につかない。",
                "彼は料理がとても上手で、何を作っても手につかないものはない。",
                "棚が高すぎて、一番上の箱まで私の手につかない。"
            ],
            "ans": 2,
            "cute_right_msg": "Không dính bẫy nghĩa đen luôn!! Quán dụng `勉強・仕事が手につかない` = tâm trí rối bời không thể tập trung học/làm nổi! 🎯",
            "right_exp": "`〜が手につかない` là quán dụng ngữ mang nghĩa tâm trí phân tâm vì quá lo lắng/hồi hộp/buồn bã đến nỗi không tập trung vào học tập/công việc nổi.",
            "cute_wrong_msg": "Cẩn thận bị lừa theo nghĩa đen 'dính vào tay' hay 'với tay chạm tới (`手が届かない`)' nha em! Quán dụng `手につかない` dùng cho `勉強・仕事` khi tâm trạng bồn chồn! 💌",
            "wrong_exps": [
                "Keo dán không dính tay dùng nghĩa đen `くっつかない / つかない` (bỏ chữ 手), hoặc nếu nghĩa đen vẫn không phải thành ngữ `手につかない`.",
                "Chính xác! Quá hồi hộp chờ kết quả thi nên học không vào (`勉強が手につかない`).",
                "Không có cách dùng `手につかない` cho tài nấu ăn khéo léo (`作れないものはない` mới đúng).",
                "Không với tới kệ trên cao dùng `手が届かない` (NOT `手につかない`)."
            ],
            "source_ref": {"novel": "yandere", "chapter": 12, "lesson_id": "p2_c06_b02", "label": "Bộ 2 Yandere Ch.12 (Bài 33: Quán dụng ngữ 2)"}
        },
        {
            "num": 32,
            "mondai": "問題6：用法",
            "mondai_vi": "Cách dùng từ đúng trong câu",
            "prompt": "次の言葉の使い方として最もよいものを、1・2・3・4から一つ選びなさい。\n【言葉：<b><u>直前</u></b>】",
            "prompt_vi": "Chọn câu sử dụng đúng nhất từ 【直前（ちょくぜん）】 (ngay sát trước thời điểm sự việc xảy ra).",
            "options": [
                "私の家の直前には、大きなスーパーマーケットが建っている。",
                "発表の直前になって急に緊張し、頭が真っ白になった。",
                "10年直前に行った旅行の写真を今でも部屋に飾っている。",
                "彼は駅の直前で友達と待ち合わせをした。"
            ],
            "ans": 2,
            "cute_right_msg": "Đỉnh cao! `直前` chỉ **thời điểm sát nút trước 1 sự kiện**, KHÔNG dùng chỉ vị trí không gian trước nhà/trước ga hay quãng thời gian 10 năm trước đâu nhé! ⏱️✨",
            "right_exp": "`直前（ちょくぜん）` chỉ **mốc thời gian ngay sát trước khi sự kiện bắt đầu** (`発表の直前`, `試験の直前`, `出発の直前`). Không dùng cho khoảng cách không gian (`家の前`, `駅前`) hay mốc xa (`10年前`).",
            "cute_wrong_msg": "Mẹo siêu hữu ích nè em: `直前（ちょくぜん）` chỉ dùng cho **thời gian sát nút ngay trước sự kiện** (trước giờ G vài phút/giờ), KHÔNG dùng chỉ không gian 'trước mặt/trước cửa nhà' (`目の前・家の前`) đâu nhé! 🌸",
            "wrong_exps": [
                "Không gian phía trước nhà dùng `家の目の前 / 前`, không dùng `直前`.",
                "Chính xác! Ngay sát trước giờ thuyết trình (`発表の直前`).",
                "10 năm trước dùng `10年前`, không dùng `直前`.",
                "Địa điểm trước ga dùng `駅の目の前 / 駅前`, không dùng `直前`."
            ],
            "source_ref": {"novel": "isekai", "chapter": 7, "lesson_id": "p1_c09_b02", "label": "Bộ 3 Isekai Ch.07 (Bài 21: Thời gian)"}
        },
        # --- 問題7: 文の文法1 (33-44) ---
        {
            "num": 33,
            "mondai": "問題7：文の文法1",
            "mondai_vi": "Ngữ pháp câu N2",
            "prompt": "練習を重ねる（　　）、ピアノの音が少しずつ滑らかになってきた。",
            "prompt_vi": "Càng luyện tập chăm chỉ lặp đi lặp lại thì âm thanh tiếng đàn piano cũng dần trở nên mượt mà hơn theo.",
            "options": ["にしたがって", "ことなしに", "わりには", "かのようだ"],
            "ans": 1,
            "cute_right_msg": "Chuẩn luôn! `Vる + にしたがって` (càng X thì càng biến đổi Y tương ứng theo tiến trình)! 🎹✨",
            "right_exp": "`Vる / N + にしたがって`: Theo đà biến đổi của A thì B cũng thay đổi tương ứng (`練習を重ねるにしたがって`).",
            "cute_wrong_msg": "Nhìn diễn tiến song song 'càng luyện tập thêm → âm đàn dần mượt mà hơn': mẫu chỉ sự biến đổi tỷ lệ thuận là `にしたがって` nha em! 🌸",
            "wrong_exps": [
                "Chính xác! `練習を重ねるにしたがって` = càng luyện tập nhiều thì càng...",
                "`〜ことなしに` = mà không cần làm X (`相談することなしに`).",
                "`〜わりには` = tuy X nhưng kết quả lại Y trái với tiêu chuẩn.",
                "`かのようだ` kết thúc mệnh đề ('cứ như thể là'), không đứng nối giữa 2 mệnh đề kiểu này."
            ],
            "source_ref": {"novel": "romcom", "chapter": 5, "lesson_id": "p1_c03_b01", "label": "Ngữ pháp N2 — 伴う変化（〜にしたがって）"}
        },
        {
            "num": 34,
            "mondai": "問題7：文の文法1",
            "mondai_vi": "Ngữ pháp câu N2",
            "prompt": "いくら親しい友人（　　）、お金の貸し借りだけは慎重にすべきだ。",
            "prompt_vi": "Dẫu có là bạn bè thân thiết đến đâu đi chăng nữa, riêng chuyện vay mượn tiền bạc vẫn nên thận trọng.",
            "options": ["であれ", "だけあって", "どころか", "ときたら"],
            "ans": 1,
            "cute_right_msg": "Đỉnh luôn! `いくら〜であれ` = cho dù là ai/cái gì đi nữa (cặp hô ứng `いくら / たとえ〜であれ`) chuẩn văn N2 luôn! 💎",
            "right_exp": "`（いくら / たとえ）N + であれ`: Dù cho là N đi chăng nữa thì vẫn... (tương đương `〜であっても`, thường kết hợp phó từ `どんなに・いくら`).",
            "cute_wrong_msg": "Thấy từ mở đầu `いくら` ('dù có... đến mấy đi nữa') thì đi tìm cấu trúc nhượng bộ ngay nhé em: `N + であれ` (= `であっても`)! 💡",
            "wrong_exps": [
                "Chính xác! `いくら親しい友人であれ` = dù là bạn thân tới đâu đi nữa.",
                "`だけあって` = quả đúng xứng đáng với danh tiếng/nỗ lực (`〜だけあって`).",
                "`どころか` = đừng nói đến, trái lại còn...",
                "`ときたら` = nói đến tên ấy là chỉ thấy bực mình/chán ngán (phàn nàn)."
            ],
            "source_ref": {"novel": "romcom", "chapter": 1, "lesson_id": "p1_c01_b01", "label": "Ngữ pháp N2 — 譲歩（〜であれ）"}
        },
        {
            "num": 35,
            "mondai": "問題7：文の文法1",
            "mondai_vi": "Ngữ pháp câu N2",
            "prompt": "彼の描く絵はどれも独創的で、プロの画家（　　）見事な出来栄えだ。",
            "prompt_vi": "Những bức tranh cậu ấy vẽ bức nào cũng độc đáo, đạt trình độ xuất sắc chẳng kém gì họa sĩ chuyên nghiệp.",
            "options": ["顔負けの", "だらけの", "抜きの", "まみれの"],
            "ans": 1,
            "cute_right_msg": "Quá chất!! Mẫu thành ngữ N2 nâng cao `〜顔負け（かおまけ）の` = giỏi đến mức ngay cả chuyên gia/người thật cũng phải chịu thua! 🎨🏆",
            "right_exp": "`N + 顔負け（かおまけ）だ / の`: Tài giỏi / xuất sắc đến mức ngay cả bậc thầy N cũng phải 'chào thua xấu hổ' (`プロ顔負けの腕前`).",
            "cute_wrong_msg": "Mẹo nhớ từ độc đáo nè em: cậu ta không phải họa sĩ chuyên nghiệp mà vẽ đẹp khiến 'dân pro cũng phải thua mặt tái mét' → `プロ顔負けの` nha! ✨",
            "wrong_exps": [
                "Chính xác! `プロ顔負けの出来栄え` = thành phẩm đẹp đến dân chuyên cũng phải nể.",
                "`だらけの` = đầy rẫy thứ tiêu cực (`間違いだらけ`).",
                "`抜きの` = bỏ qua, lược bỏ cái gì (`昼食抜きの会議`).",
                "`まみれの` = lấm lem bê bết (`泥まみれ・汗まみれ`)."
            ],
            "source_ref": {"novel": "romcom", "chapter": 5, "lesson_id": "p1_c03_b01", "label": "Ngữ pháp N2 — 〜顔負け"}
        },
        {
            "num": 36,
            "mondai": "問題7：文の文法1",
            "mondai_vi": "Ngữ pháp câu N2",
            "prompt": "彼女はその知らせを聞いた瞬間、信じられない（　　）目を見開いて立ち尽くした。",
            "prompt_vi": "Khoảnh khắc nghe được tin tức ấy, cô ấy mở to mắt đứng sững lại như thể muốn nói rằng chuyện này thật không thể tin nổi.",
            "options": ["とばかりに", "こととて", "ものなら", "からといって"],
            "ans": 1,
            "cute_right_msg": "Chuẩn 100 điểm luôn! `信じられないとばかりに` = cứ như thể muốn thốt lên rằng 'không thể tin nổi'! 😲✨",
            "right_exp": "`〜とばかりに`: Cứ như thể muốn nói lên bằng thái độ/ánh mắt rằng... (không nói thành lời nhưng cử chỉ biểu lộ rõ tâm trạng).",
            "cute_wrong_msg": "Nhìn hành động 'mở to mắt đứng sững' không thốt nên lời mà ánh mắt biểu đạt ý 'Không thể tin được!' → mẫu tả biểu cảm kinh điển là `とばかりに` nha em! 🌹",
            "wrong_exps": [
                "Chính xác tuyệt đối! `信じられないとばかりに目を見開く`.",
                "`こととて` = vì là hoàn cảnh/tính chất như thế nên đành phải... (văn phong trang trọng xin lỗi).",
                "`ものなら` = nếu lỡ mà / giá mà làm được... (`できるものならやってみたい`).",
                "`からといって` = dù cho nói là... nhưng chưa chắc..."
            ],
            "source_ref": {"novel": "yandere", "chapter": 5, "lesson_id": "p2_c01_b01", "label": "Ngữ pháp N2 — 様子（〜とばかりに）"}
        },
        {
            "num": 37,
            "mondai": "問題7：文の文法1",
            "mondai_vi": "Ngữ pháp câu N2",
            "prompt": "最近、少し運動しただけで息が切れる。やはり年齢には（　　）ものだなと実感する。",
            "prompt_vi": "Dạo này chỉ vận động chút xíu là đã hụt hơi rồi. Quả nhiên thấm thía rằng chẳng tài nào chống lại được tuổi tác mà.",
            "options": ["勝てないわけだ", "勝てっこない", "勝てるきりだ", "勝つまい"],
            "ans": 2,
            "cute_right_msg": "Quá chuẩn! `V(ます) + っこない` (chắc chắn làm sao mà thắng nổi = `勝てっこない`)! 💪🌟",
            "right_exp": "`V(ます) + っこない`: Phủ định khả năng một cách chắc nịch trong văn nói / độc thoại ('làm sao mà... nổi / đời nào mà... được'). Lưu ý ở câu chia dạng định ngữ cho `ものだ` cũng rất tự nhiên (`勝てっこないものだな`).",
            "cute_wrong_msg": "Kiểm tra kết hợp và sắc thái nhé em: `勝てないわけだ` mang nghĩa 'hèn gì bảo sao chẳng thắng được' (cần lý do trước), còn tâm sự cảm thán 'không tài nào thắng nổi tuổi tác' dùng `Vます+っこない` (`勝てっこない`) nha! 🌸",
            "wrong_exps": [
                "`〜わけだ` là 'hảo nào / hóa ra vì thế nên...' (giải thích kết quả đương nhiên, không tự nhiên khi nói `勝てないわけだものだ`).",
                "Chính xác! `勝てっこないものだな` = quả nhiên chẳng thể thắng nổi tuổi tác mà.",
                "Không có mẫu `Vる＋きりだ`.",
                "`勝つまい` = quyết không thắng / có lẽ sẽ không thắng (sai ý chí)."
            ],
            "source_ref": {"novel": "yandere", "chapter": 2, "lesson_id": "p1_c02_b03", "label": "Ngữ pháp N2 — 不可能（〜っこない）"}
        },
        {
            "num": 38,
            "mondai": "問題7：文の文法1",
            "mondai_vi": "Ngữ pháp câu N2",
            "prompt": "今回の失敗をきっかけ（　　）、これまでの仕事の進め方を根本から見直そうと思う。",
            "prompt_vi": "Nhân cơ hội / lấy thất bại lần này làm bước ngoặt, tôi định xem xét lại phương pháp làm việc từ trước đến nay từ gốc rễ.",
            "options": ["として", "に際して", "にあたって", "のもとで"],
            "ans": 1,
            "cute_right_msg": "Cụm chuẩn Shinkanzen Bunpou: `〜をきっかけとして / 〜をきっかけに`! ✨",
            "right_exp": "`N をきっかけとして / を契機（けいき）として`: Lấy N làm khởi nguồn / bước ngoặt để bắt đầu thay đổi.",
            "cute_wrong_msg": "Mất chữ `として` phía sau `きっかけ` là thiếu cặp `〜をきっかけとして` rồi đó em~ Đừng nhầm với `〜に際して` (nhân dịp bắt đầu việc trọng đại)! 💡",
            "wrong_exps": [
                "Chính xác tuyệt đối! `失敗をきっかけとして` = nhân thất bại làm cột mốc khởi đầu.",
                "`に際して` gắn thẳng sau Danh từ (`〜をきっかけに際して` sai vì dư chữ `きっかけ`).",
                "`にあたって` cũng gắn trực tiếp sau N/V (`卒業にあたって`), không đi sau `をきっかけ`.",
                "`のもとで` = dưới sự hướng dẫn/che chở/quy định của... (`指導のもとで`)."
            ],
            "source_ref": {"novel": "isekai", "chapter": 2, "lesson_id": "p1_c07_b03", "label": "Ngữ pháp N2 — 〜をきっかけとして"}
        },
        {
            "num": 39,
            "mondai": "問題7：文の文法1",
            "mondai_vi": "Ngữ pháp câu N2",
            "prompt": "明日のスピーチ大会は、本番（　　）失敗しないように何度もしゃべる練習をした。",
            "prompt_vi": "Cho cuộc thi hùng biện ngày mai, tôi đã tập nói đi nói lại nhiều lần để lúc vào thi thật không bị vấp lỗi.",
            "options": ["になって", "でいうと", "にしたら", "にあたって"],
            "ans": 1,
            "cute_right_msg": "Quá mượt! `本番になって` (khi bước vào lúc diễn ra chính thức) chuẩn xác hoàn hảo luôn! 🎤✨",
            "right_exp": "`本番になって失敗しないように`: Đến khi bước vào giờ G thi thật (`本番になる`) mà không bị lỗi (hoặc không cuống).",
            "cute_wrong_msg": "Đọc mượt tự nhiên nhé em: 'để đến lúc vào thi chính thức (`本番になって`) không bị hỏng chuyện' — 3 phương án kia đều không hợp ngữ cảnh thời điểm giờ G! 🌸",
            "wrong_exps": [
                "Chính xác! `本番になって` = khi đến lúc thi thật.",
                "`でいうと` = nếu quy theo / xét theo mốc nào (`例でいうと`).",
                "`にしたら` = đứng trên lập trường của người nào (`親にしたら`).",
                "`にあたって` chỉ dùng trước hành động chủ động mang tính tích cực chuẩn bị (`留学にあたって抱負を語る`), KHÔNG dùng ngay trước `失敗しないように`!"
            ],
            "source_ref": {"novel": "romcom", "chapter": 7, "lesson_id": "p1_c05_b01", "label": "Ngữ pháp N2 — 時・場面"}
        },
        {
            "num": 40,
            "mondai": "問題7：文の文法1",
            "mondai_vi": "Ngữ pháp câu N2",
            "prompt": "あの選手は厳しいトレーニングを積み、けがの痛み（　　）見事な優勝を果たした。",
            "prompt_vi": "Vận động viên ấy đã khổ luyện nghiêm khắc, bất chấp cả cơn đau chấn thương để giành chức vô địch ngoạn mục.",
            "options": ["をものともせずに", "を問わず", "をめぐって", "に沿って"],
            "ans": 1,
            "cute_right_msg": "Chất lượng N2 thực thụ!! `痛み・困難・周囲の反対をものともせずに` = bất chấp gian khổ nỗi đau không hề nao núng! 🏅🔥",
            "right_exp": "`N + をものともせずに` = Bất chấp khó khăn, nguy hiểm, bệnh tật hay sự phản đối mà vẫn kiên cường tiến bước.",
            "cute_wrong_msg": "Gợi ý nhẹ nhàng nè em: đối mặt cơn đau chấn thương mà vẫn giành cúp vô địch → mẫu từ trang trọng diễn tả tinh thần bất chấp gian khó là `をものともせずに` nhé! 🌟",
            "wrong_exps": [
                "Chính xác tuyệt đối! `けがの痛みをものともせずに` = bất chấp nỗi đau chấn thương.",
                "`を問わず` = không phân biệt (`男女・年齢を問わず`).",
                "`をめぐって` = tranh luận xoay quanh vấn đề (`新しい制度をめぐって`).",
                "`に沿って` = men theo / dựa theo kế hoạch, quy định (`方針に沿って`)."
            ],
            "source_ref": {"novel": "romcom", "chapter": 5, "lesson_id": "p1_c03_b01", "label": "Ngữ pháp N2 — 〜をものともせずに"}
        },
        {
            "num": 41,
            "mondai": "問題7：文の文法1",
            "mondai_vi": "Ngữ pháp câu N2",
            "prompt": "深夜の住宅街で大声を出して騒ぐなど、近所迷惑になる行為は厳しく（　　）。",
            "prompt_vi": "Những hành vi gây phiền hà hàng xóm như hò hét ầm ĩ giữa khu dân cư lúc nửa đêm không nên được dung thứ.",
            "options": ["許すべきではない", "許すほかない", "許しかねない", "許すまいとする"],
            "ans": 1,
            "cute_right_msg": "Chính xác! `〜べきではない` = không nên, không được phép làm điều gì trái chuẩn mực! 🚫",
            "right_exp": "`Vる + べきではない` = Không nên làm V (nhấn mạnh trách nhiệm đạo đức / quy chuẩn xã hội).",
            "cute_wrong_msg": "Đọc cuối câu 'hành vi gây phiền hà hàng xóm thì tuyệt đối không nên tha thứ/dung túng' → chọn ngay `許すべきではない` nha em! 🌸",
            "wrong_exps": [
                "Chính xác! `厳しく許すべきではない` (về mặt chuẩn mực xã hội không nên dung thứ).",
                "`〜ほかない` = chỉ còn cách đành phải... (ngược nghĩa hoàn toàn!).",
                "`〜かねない` = e rằng có nguy cơ xảy ra chuyện xấu.",
                "`許すまいとする` = cố gắng để không tha thứ (văn cổ/người kể ngôi thứ nhất không hợp giọng quy định chung)."
            ],
            "source_ref": {"novel": "yandere", "chapter": 4, "lesson_id": "p1_c07_b02", "label": "Ngữ pháp N2 — 禁止・忠告（〜べきではない）"}
        },
        {
            "num": 42,
            "mondai": "問題7：文の文法1",
            "mondai_vi": "Ngữ pháp câu N2",
            "prompt": "長年愛用していたカメラが壊れてしまい、写真好きの父は残念（　　）。",
            "prompt_vi": "Chiếc máy ảnh gắn bó yêu thích suốt nhiều năm bỗng bị hỏng mất, người bố mê nhiếp ảnh trông tiếc nuối khôn nguôi.",
            "options": ["がってたまらない", "がりそうな様子だ", "そうでならない", "がっている"],
            "ans": 4,
            "cute_right_msg": "Bắt gọn tính từ cảm xúc ngôi thứ 3 (`父は` + `残念がる` → `残念がっている`)!! Tuyệt vời ông mặt trời! 📸💖",
            "right_exp": "Chủ ngữ là ngôi thứ 3 (`父は`): `残念だ` → `残念がる` → đang biểu lộ ra ngoài là `残念がっている`. (Câu 1 & 3 dùng sai tiếp nối với `たまらない / ならない` cho ngôi thứ 3 khi thiếu `がって...` hợp lý; `がってたまらない` tự mâu thuẫn vì `たまらない` diễn tả cảm giác trực tiếp của người nói!).",
            "cute_wrong_msg": "Coi chủ ngữ ngôi thứ 3 `父は` kìa em ơi!! Bố cảm thấy tiếc nuối thì người ngoài nhìn vào phải dùng `〜がる` (`残念がっている`), chứ `〜てたまらない / 〜てならない` chỉ dùng cho cảm xúc của chính bản thân mình (`私は〜`) nha! 🌟",
            "wrong_exps": [
                "`〜てたまらない` diễn tả cảm xúc dâng trào từ bên trong bản thân người nói (`私は嬉しい・残念でたまらない`), KHÔNG gắn vào `〜がって` cho ngôi thứ 3.",
                "Không có dạng chia ghép thừa `が＋りそう`.",
                "`〜てならない` cũng là cảm xúc tự nhiên của người nói (nếu dùng `残念そうでならない` nghe không chuẩn bằng `残念がっている` trong N2; thực tế `Aい・Aな + でならない` mới là mẫu N2, không phải `そうでならない`).",
                "Chính xác tuyệt đối! `父は残念がっている` (Bố tôi đang tỏ vẻ tiếc nuối lắm)."
            ],
            "source_ref": {"novel": "isekai", "chapter": 12, "lesson_id": "p2_c07_b04", "label": "Ngữ pháp N2 — 感情表出（〜がっている）"}
        },
        {
            "num": 43,
            "mondai": "問題7：文の文法1",
            "mondai_vi": "Ngữ pháp câu N2",
            "prompt": "この仕事は地道な作業の連続で、忍耐力（　　）、とても続けられない。",
            "prompt_vi": "Công việc này toàn là chuỗi tác vụ âm thầm bền bỉ liên tiếp, nếu không có tính kiên nhẫn thì chẳng thể nào làm nổi lâu dài.",
            "options": ["抜きにしては", "によっては", "をめぐっては", "に先立っては"],
            "ans": 1,
            "cute_right_msg": "Chuẩn 100 điểm luôn!! `〜（を）抜きにしては〜ない` = nếu thiếu đi nhân tố X tối quan trọng thì tuyệt đối không thể Y! 🔥",
            "right_exp": "`N + （を）抜きにしては〜ない`: Nếu loại trừ / thiếu vắng N đi thì tuyệt đối không thể nói tới / không thể làm nổi vế sau.",
            "cute_wrong_msg": "Cặp hô ứng với `とても続けられない` (thể phủ định khả năng) ở cuối câu rất hay đi với `〜抜きにしては` ('nếu bỏ qua / thiếu đi lòng kiên nhẫn thì chịu thua không làm nổi!') nha em! 🌸",
            "wrong_exps": [
                "Chính xác! `忍耐力抜きにしては続けられない` = nếu không có sự kiên nhẫn thì chẳng thể theo đuổi nổi.",
                "`によっては` = tùy thuộc vào N mà kết quả khác nhau / một số N thì...",
                "`をめぐっては` = xoay quanh vấn đề tranh cãi nào đó.",
                "`に先立っては` = trước khi tiến hành việc gì đó (`開始に先立って`)."
            ],
            "source_ref": {"novel": "romcom", "chapter": 8, "lesson_id": "p1_c05_b02", "label": "Ngữ pháp N2 — 条件（〜抜きにしては）"}
        },
        {
            "num": 44,
            "mondai": "問題7：文の文法1",
            "mondai_vi": "Ngữ pháp câu N2",
            "prompt": "いくら説明されても、専門外の人にはその複雑な仕組みが（　　）。",
            "prompt_vi": "Dù có được giải thích bao nhiêu đi nữa, đối với người ngoài chuyên ngành thì cũng khó mà hiểu nổi cơ chế phức tạp đó.",
            "options": ["理解しがたい", "理解しがいがある", "理解するまい", "理解しかねるわけがない"],
            "ans": 1,
            "cute_right_msg": "Quá chuẩn!! `V(ます) + がたい` = rất khó để làm được (chủ yếu đi với động từ nhận thức/tâm lý như `理解しがたい・信じがたい・許しがたい`)! 🧠✨",
            "right_exp": "`V(ます) + がたい`: Khó mà thực hiện nổi (thường đi với các động từ cảm xúc/nhận thức như `信じがたい・理解しがたい・想像しがたい・許しがたい`).",
            "cute_wrong_msg": "Hậu tố ngữ pháp N2 siêu kinh điển dùng với các động từ nhận thức (`理解・想像・信じる`) khi 'rất khó mà hiểu nổi' chính là **〜がたい** (`理解しがたい`) đó em! 💡",
            "wrong_exps": [
                "Chính xác! `理解しがたい` = rất khó mà hiểu nổi.",
                "`Vます+がいがある` = đáng giá bỏ công sức làm (`やりがい・生きがい`).",
                "`理解するまい` = quyết sẽ không hiểu / chắc không hiểu (sai sắc thái khi nói về người ngoài ngành khó tiếp thu).",
                "`理解しかねるわけがない` nghĩa kép thành 'không lý nào lại khó hiểu' (ngược nghĩa hoàn toàn)."
            ],
            "source_ref": {"novel": "isekai", "chapter": 5, "lesson_id": "p1_c08_b02", "label": "Ngữ pháp N2 — 困難（〜がたい）"}
        },
        # --- 問題8: 文の文法2 ★ (45-49) ---
        {
            "num": 45,
            "mondai": "問題8：文の文法2 ★",
            "mondai_vi": "Sắp xếp thành phần câu",
            "prompt": "どんな分野でも、必ずしも ＿＿＿ ＿＿＿ ★ ＿＿＿ とは限らない。",
            "prompt_vi": "Trong bất kỳ lĩnh vực nào cũng vậy, không hẳn cứ nỗ lực rồi là chắc chắn sẽ có thể thành công được.",
            "options": ["成功", "からといって", "できる", "努力した"],
            "ans": 1,
            "cute_right_msg": "Tuyệt vời!! Thứ tự chuẩn: `[4] 努力した → [2] からといって → ★[1] 成功 → [3] できる`! Quá mượt luôn! 🏆✨",
            "right_exp": "Ghép chuẩn xác: `必ずしも [4]努力した [2]からといって ★[1]成功 [3]できる とは限らない。`\n- `[4]努力した` nối trước `[2]からといって` (`〜たからといって` = dù nói là đã cố gắng thế nhưng...).\n- Tiếp theo là danh từ `[1]成功` ghép cùng `[3]できる` (`成功できる`) trước `とは限らない`.\n→ Vị trí dấu ★ là **1 (`成功`)**!",
            "cute_wrong_msg": "Nhìn công thức `必ずしも 〜 からといって 〜 とは限らない` là bung ra ngay luôn nha em: `[4] 努力した + [2] からといって`, rồi sau đó đến động từ ghép `[1] 成功 + [3] できる` ở trước `とは限らない`! 🌟",
            "wrong_exps": [
                "Chính xác tuyệt đối! Vị trí ★ là `[1] 成功` (`4 → 2 → 1 → 3`).",
                "`[2] からといって` đứng ở ô số 2 (sau `努力した`).",
                "`[3] できる` đứng ở ô số 4 (ngay trước `とは限らない`).",
                "`[4] 努力した` đứng ở ô số 1."
            ],
            "source_ref": {"novel": "isekai", "chapter": 9, "lesson_id": "p2_c07_b01", "label": "Ngữ pháp N2 ★ — 〜からといって〜とは限らない"}
        },
        {
            "num": 46,
            "mondai": "問題8：文の文法2 ★",
            "mondai_vi": "Sắp xếp thành phần câu",
            "prompt": "インターネットの普及に ＿＿＿ ＿＿＿ ★ ＿＿＿ 増えてきた。",
            "prompt_vi": "Cùng với sự phổ cập của Internet, số người làm việc ngay tại nhà cũng ngày càng tăng lên.",
            "options": ["人が", "自宅で", "伴って、", "働く"],
            "ans": 4,
            "cute_right_msg": "Chuẩn 100%!! `[3] 伴って、 → [2] 自宅で → ★[4] 働く → [1] 人が` (`増えてきた`)! 💻🏡",
            "right_exp": "Ghép chuẩn xác: `普及に [3]伴って、 [2]自宅で ★[4]働く [1]人が 増えてきた。`\n- `普及に` kết hợp ngay với `[3]伴って、` (`〜に伴って`: kéo theo/cùng với sự phổ cập...).\n- Nơi chốn `[2]自宅で` bổ nghĩa cho động từ `[4]働く`.\n- `[4]働く` định ngữ cho danh từ `[1]人が` đi cùng `増えてきた`.\n→ Vị trí dấu ★ là **4 (`働く`)**!",
            "cute_wrong_msg": "Khớp liền chữ `に` ngay trước ô trống 1 bằng `[3] 伴って、` (`〜に伴って`), rồi ghép cụm danh từ trước `増えてきた`: `自宅で 働く 人が`! 🧩",
            "wrong_exps": [
                "`[1] 人が` đứng ở ô số 4 (chủ ngữ trước `増えてきた`).",
                "`[2] 自宅で` đứng ở ô số 2 (chỉ nơi chốn cho động từ `働く`).",
                "`[3] 伴って、` đứng ở ô số 1 (`普及に伴って`).",
                "Chính xác tuyệt đối! Vị trí ★ là `[4] 働く` (`3 → 2 → 4 → 1`)."
            ],
            "source_ref": {"novel": "yandere", "chapter": 3, "lesson_id": "p1_c06_b02", "label": "Ngữ pháp N2 ★ — 〜に伴って"}
        },
        {
            "num": 47,
            "mondai": "問題8：文の文法2 ★",
            "mondai_vi": "Sắp xếp thành phần câu",
            "prompt": "このスマートフォンは、 ＿＿＿ ＿＿＿ ★ ＿＿＿ あまり使いやすくない。",
            "prompt_vi": "Chiếc điện thoại thông minh này, so với việc tính năng dồi dào phong phú thì thao tác lại phức tạp nên chẳng dễ dùng cho lắm.",
            "options": ["機能が", "充実している", "わりに", "操作が複雑で"],
            "ans": 3,
            "cute_right_msg": "Xuất sắc luôn!! `[1] 機能が → [2] 充実している → ★[3] わりに → [4] 操作が複雑で`! 📱✨",
            "right_exp": "Ghép chuẩn xác: `[1]機能が [2]充実している ★[3]わりに [4]操作が複雑で あまり使いやすくない。`\n- `[1]機能が` là chủ ngữ của `[2]充実している`.\n- `充実している` đi với `[3]わりに` (so với độ đầy đủ tính năng thì lại...).\n- `[4]操作が複雑で` nêu nguyên nhân nối sang `あまり使いやすくない`.\n→ Vị trí dấu ★ là **3 (`わりに`)**!",
            "cute_wrong_msg": "Nhìn mẫu `〜わりに` (tuy A thế mà lại B bất ngờ): tính năng phong phú ↔ thao tác phức tạp khó dùng → chọn ngay cụm `[1] 機能が + [2] 充実している + [3] わりに` ở 3 ô đầu nha em! 🌸",
            "wrong_exps": [
                "`[1] 機能が` đứng ở ô số 1.",
                "`[2] 充実している` đứng ở ô số 2.",
                "Chính xác! Vị trí ★ là `[3] わりに` (`1 → 2 → 3 → 4`).",
                "`[4] 操作が複雑で` đứng ở ô số 4."
            ],
            "source_ref": {"novel": "yandere", "chapter": 3, "lesson_id": "p1_c06_b02", "label": "Ngữ pháp N2 ★ — 〜わりに"}
        },
        {
            "num": 48,
            "mondai": "問題8：文の文法2 ★",
            "mondai_vi": "Sắp xếp thành phần câu",
            "prompt": "彼は先月退社した ＿＿＿ ＿＿＿ ★ ＿＿＿ 誰も連絡を取れていない。",
            "prompt_vi": "Từ lúc anh ấy nghỉ việc tháng trước đến giờ bặt vô âm tín, chẳng rõ tung tích đi đâu nên chẳng ai liên lạc được.",
            "options": ["きり、", "行方が", "分からず", "それ以来"],
            "ans": 2,
            "cute_right_msg": "Chuẩn hết chỗ chê!! `[1] きり、 → [4] それ以来 → ★[2] 行方が → [3] 分からず`! 🕵️‍♂️🌹",
            "right_exp": "Ghép chuẩn xác: `先月退社した [1]きり、 [4]それ以来 ★[2]行方が [3]分からず 誰も連絡を取れていない。`\n- `退社した` (Vた) gắn với `[1]きり、` (từ dạo nghỉ việc xong là mất hút luôn).\n- Tiếp theo nhấn mạnh khoảng thời gian từ đó tới nay `[4]それ以来`.\n- Cụm `[2]行方が [3]分からず` (không rõ tung tích nên...) nối sang vế sau.\n→ Vị trí dấu ★ là **2 (`行方が`)**!",
            "cute_wrong_msg": "Để ý động từ quá khứ `退社した` ngay trước ô số 1 nhé em: mẫu `Vた＋きり` ('kể từ khi... đến giờ vẫn nguyên vậy') chắc chắn đặt `[1] きり、` ngay ô 1! Tiếp đó ghép `行方が分からず` ở cuối~ 💡",
            "wrong_exps": [
                "`[1] きり、` đứng ngay ô số 1 (`退社したきり`).",
                "Chính xác tuyệt đối! Vị trí ★ là `[2] 行方が` (`1 → 4 → 2 → 3`).",
                "`[3] 分からず` đứng ở ô số 4.",
                "`[4] それ以来` đứng ở ô số 2."
            ],
            "source_ref": {"novel": "yandere", "chapter": 4, "lesson_id": "p1_c07_b02", "label": "Ngữ pháp N2 ★ — 〜たきり"}
        },
        {
            "num": 49,
            "mondai": "問題8：文の文法2 ★",
            "mondai_vi": "Sắp xếp thành phần câu",
            "prompt": "長年の研究の末、博士はついに ＿＿＿ ＿＿＿ ★ ＿＿＿ 至った。",
            "prompt_vi": "Sau bao năm ròng nghiên cứu, cuối cùng vị tiến sĩ đã thiết lập được phương pháp trị liệu mới và tiến tới ứng dụng vào thực tế.",
            "options": ["治療法を", "実用化", "確立し、", "するに"],
            "ans": 2,
            "cute_right_msg": "Mãn nhãn quá em ơi!! `[1] 治療法を → [3] 確立し、 → ★[2] 実用化 → [4] するに` (`至った`)! 🔬🏅",
            "right_exp": "Ghép chuẩn xác: `博士はついに [1]治療法を [3]確立し、 ★[2]実用化 [4]するに 至った。`\n- `[1]治療法を` làm tân ngữ cho động từ `[3]確立し、` (thiết lập nên phương pháp trị liệu rồi...).\n- Danh động từ `[2]実用化` kết hợp `[4]するに` + `至った` (`〜するに至る` = đạt đến giai đoạn đưa vào thực tế).\n→ Vị trí dấu ★ là **2 (`実用化`)**!",
            "cute_wrong_msg": "Nhìn từ cuối `至った` bên ngoài: cấu trúc N2 là `Vる ＋ に至った`, nên ô số 4 chắc chắn là `[4] するに`, đứng sau `[2] 実用化` (`実用化するに至った`) đó em! ✨",
            "wrong_exps": [
                "`[1] 治療法を` đứng ở ô số 1.",
                "Chính xác! Vị trí ★ là `[2] 実用化` (`1 → 3 → 2 → 4`).",
                "`[3] 確立し、` đứng ở ô số 2.",
                "`[4] するに` đứng ở ô số 4 (ngay trước `至った`)."
            ],
            "source_ref": {"novel": "isekai", "chapter": 5, "lesson_id": "p1_c08_b02", "label": "Ngữ pháp N2 ★ — 〜に至る"}
        },
        # --- 問題9: 文章の文法 (50-54) ---
        {
            "num": 50,
            "mondai": "問題9：文章の文法",
            "mondai_vi": "Ngữ pháp đoạn văn (Điền khuyết bài đọc)",
            "passage": PASSAGE_EXAM2,
            "passage_vi": PASSAGE_EXAM2_VI,
            "prompt": "空欄（　50　）に入る最もよいものを一つ選びなさい。\n「なぜなら、話し手は聞き手の反応を見る（　50　）、自分の話が伝わっているかどうかを確かめているからである。」",
            "prompt_vi": "Chọn đáp án đúng nhất điền vào chỗ trống (50): 'Bởi lẽ, người nói thông qua việc quan sát phản ứng người nghe mà xác nhận xem câu chuyện của mình có truyền đạt được không.'",
            "options": ["ことに対して", "ことによって", "ことにして", "ことになると"],
            "ans": 2,
            "cute_right_msg": "Quá chuẩn!! `〜することによって` (thông qua phương thức/cách thức nhìn phản ứng của người nghe để kiểm chứng)! 💬✨",
            "right_exp": "`〜によって / ことによって`: Thông qua phương pháp/hành động đó mà thực hiện hành động phía sau (`反応を見ることによって確かめる`).",
            "cute_wrong_msg": "Phương tiện/cách thức để người nói kiểm tra xem bạn có hiểu hay không chính là 'bằng việc nhìn phản ứng' → dùng `ことによって` nha em! 🌸",
            "wrong_exps": [
                "`に対して` = đối với / trái ngược với.",
                "Chính xác! `反応を見ることによって` = thông qua việc quan sát phản ứng.",
                "`ことにして` = tự mình quyết định làm gì (`毎日運動することにする`).",
                "`ことになると` = nếu thành ra quy định/kết cục là..."
            ],
            "source_ref": {"novel": "yandere", "chapter": 5, "lesson_id": "p2_c01_b01", "label": "Ngữ pháp N2 — 手段（〜ことによって）"}
        },
        {
            "num": 51,
            "mondai": "問題9：文章の文法",
            "mondai_vi": "Ngữ pháp đoạn văn (Điền khuyết bài đọc)",
            "passage": PASSAGE_EXAM2,
            "passage_vi": PASSAGE_EXAM2_VI,
            "prompt": "空欄（　51　）に入る最もよいものを一つ選びなさい。\n「かえって『話を聞いていないのではないか』という不信感を（　51　）。」",
            "prompt_vi": "Chọn đáp án đúng nhất điền vào chỗ trống (51): '...trái lại còn dễ khiến nảy sinh sự nghi ngờ rằng hình như người kia không thèm nghe mình nói.'",
            "options": ["与えかねない", "与えようがない", "与えるわけがない", "与えてはいけない"],
            "ans": 1,
            "cute_right_msg": "Đỉnh cao!! Vế trước có từ `かえって` (trái lại phản tác dụng) + `不信感` (nguy cơ xấu) → cặp bài trùng `〜かねない` ('e rằng có nguy cơ gây ra sự nghi ngờ mất')! ⚠️",
            "right_exp": "`V(ます) + かねない`: Rất có nguy cơ / không khéo sẽ dẫn đến kết quả tiêu cực X (`不信感を与えかねない` = có nguy cơ gây mất lòng tin).",
            "cute_wrong_msg": "Coi ngữ cảnh cảnh báo kết cục xấu khi gật đầu sai nhịp: dễ gây mất lòng tin! Mẫu chỉ 'có nguy cơ dẫn tới điều không hay' là `〜かねない` nha em! 💡",
            "wrong_exps": [
                "Chính xác tuyệt đối! `不信感を与えかねない` = không khéo sẽ gây ra sự ngờ vực.",
                "`ようがない` = không có cách nào để làm (sai nghĩa).",
                "`わけがない` = không đời nào gây ngờ vực (mâu thuẫn `かえって`).",
                "`与えてはいけない` = 'không được phép tạo ra' (đây là hệ quả vô tình khi gật sai nhịp chứ không phải lời cấm đoán)."
            ],
            "source_ref": {"novel": "yandere", "chapter": 1, "lesson_id": "p1_c01_b03", "label": "Ngữ pháp N2 — 危険（〜かねない）"}
        },
        {
            "num": 52,
            "mondai": "問題9：文章の文法",
            "mondai_vi": "Ngữ pháp đoạn văn (Điền khuyết bài đọc)",
            "passage": PASSAGE_EXAM2,
            "passage_vi": PASSAGE_EXAM2_VI,
            "prompt": "空欄（　52　）に入る最もよいものを一つ選びなさい。\n「大切なのは回数ではなく、相手の感情に寄り添おうとする姿勢（　52　）。」",
            "prompt_vi": "Chọn đáp án đúng nhất điền vào chỗ trống (52): 'Điều quan trọng không nằm ở số lần gật đầu, mà chính là thái độ muốn thấu hiểu cảm xúc đối phương.'",
            "options": ["にほかならない", "にすぎない", "とは限らない", "どころではない"],
            "ans": 1,
            "cute_right_msg": "Chuẩn đét! `〜ではなく〜にほかならない` (không phải là X mà bản chất đích thực chính là Y)! 🏆",
            "right_exp": "`N + にほかならない`: Không phải cái gì khác mà chính là N (dùng kết hợp vế trước `回数ではなく〜` để nhấn mạnh bản chất cốt lõi).",
            "cute_wrong_msg": "Cặp khẳng định nhấn mạnh bản chất sau khi phủ định vế đầu (`回数ではなく...`) luôn dùng **にほかならない** ('chính là thái độ đó chứ không gì khác!') nha em! 🌸",
            "wrong_exps": [
                "Chính xác! `寄り添おうとする姿勢にほかならない`.",
                "`にすぎない` = chỉ là... tầm thường thôi (hạ thấp, trái nghĩa 'điều quan trọng là...').",
                "`とは限らない` = chưa chắc đã là (phủ định toàn phần, lệch ý khẳng định).",
                "`どころではない` = chẳng phải lúc mà làm chuyện đó đâu."
            ],
            "source_ref": {"novel": "yandere", "chapter": 1, "lesson_id": "p1_c01_b03", "label": "Ngữ pháp N2 — 強調（〜にほかならない）"}
        },
        {
            "num": 53,
            "mondai": "問題9：文章の文法",
            "mondai_vi": "Ngữ pháp đoạn văn (Điền khuyết bài đọc)",
            "passage": PASSAGE_EXAM2,
            "passage_vi": PASSAGE_EXAM2_VI,
            "prompt": "空欄（　53　）に入る最もよいものを一つ選びなさい。\n「相手の言葉にしっかり耳を傾け、共感のサインを（　53　）、初めて心と心が通じ合う会話が生まれるのではないだろうか。」",
            "prompt_vi": "Chọn đáp án đúng nhất điền vào chỗ trống (53): 'Chỉ khi thực sự lắng nghe và gửi đi tín hiệu đồng cảm thì mới nảy sinh được cuộc trò chuyện tâm giao.'",
            "options": ["送ることでこそ", "送ったとはいえ", "送らないことには", "送るにつけて"],
            "ans": 1,
            "cute_right_msg": "Tuyệt vời!! `〜ことでこそ〜初めて` = CHỈ BẰNG chính cách làm đó thì LẦN ĐẦU TIÊN mới có thể... (cấu trúc nhấn mạnh điều kiện tiên quyết)! ✨",
            "right_exp": "`Vる + ことでこそ〜初めて`: Chính nhờ / chỉ khi thực hiện V thì lần đầu tiên mới đạt được kết quả cao đẹp phía sau (trợ từ `こそ` nhấn mạnh mạnh mẽ điều kiện khẳng định).",
            "cute_wrong_msg": "Cẩn thận lộn `送ることでこそ` (CHÍNH BẰNG việc gửi tín hiệu thì mới...) với `送らないことには` (nếu KHÔNG gửi thì không... — đằng sau lại có `初めて〜生まれる` khẳng định chứ không phải phủ định `〜ない`!) nha em! 💖",
            "wrong_exps": [
                "Chính xác! `共感のサインを送ることでこそ、初めて〜生まれる`.",
                "`送ったとはいえ` = tuy nói đã gửi rồi nhưng...",
                "`〜ないことには` phía sau BẮT BUỘC phải là câu phủ định (`〜ない` = nếu không làm X thì KHÔNG thể Y), trong khi câu gốc vế sau là khẳng định `初めて〜生まれる`!",
                "`〜につけて` = hễ cứ lúc nào thấy/nghe lại cảm thấy..."
            ],
            "source_ref": {"novel": "romcom", "chapter": 13, "lesson_id": "p2_c06_b01", "label": "Ngữ pháp N2 — 強調（〜てこそ・〜ことでこそ）"}
        },
        {
            "num": 54,
            "mondai": "問題9：文章の文法",
            "mondai_vi": "Ngữ pháp đoạn văn (Điền khuyết bài đọc)",
            "passage": PASSAGE_EXAM2,
            "passage_vi": PASSAGE_EXAM2_VI,
            "prompt": "空欄（　54　）に入る最もよいものを一つ選びなさい。\n「今日から少しずつ意識して（　54　）。」",
            "prompt_vi": "Chọn đáp án đúng nhất điền vào chỗ trống (54): 'Từ hôm nay chúng ta hãy thử ý thức rèn luyện dần từng chút một xem sao nào.'",
            "options": ["みるわけにはいかない", "みてはどうだろうか", "みたつもりだ", "みるほかはない"],
            "ans": 2,
            "cute_right_msg": "Kết bài nhẹ nhàng, truyền cảm hứng chuẩn JLPT 100% luôn!! `〜てみてはどうだろうか` (hãy thử làm như vậy xem sao nhé?)! 🌸🎉",
            "right_exp": "`Vて + みてはどうだろうか`: Đề xuất gợi ý nhẹ nhàng, lịch sự cho người đọc vào cuối bài tiểu luận ('Sao chúng ta không thử làm V xem sao nhỉ?').",
            "cute_wrong_msg": "Câu cuối bài viết khuyên người đọc nên áp dụng thử mẹo giao tiếp hay: giọng văn gợi ý thân thiện chuẩn sách báo Nhật là `〜てみてはどうだろうか` nha em! ✨",
            "wrong_exps": [
                "`〜わけにはいかない` = không thể làm thế được (ngược nghĩa).",
                "Chính xác! `意識してみてはどうだろうか` = hãy thử để ý làm xem sao nhỉ.",
                "`〜つもりだ` = tưởng nhầm rằng / dự định riêng của cá nhân, không hợp lời khuyên cuối bài.",
                "`〜ほかはない` = đành chịu hết cách chỉ còn nước làm thế (sắc thái bất đắc dĩ tiêu cực)."
            ],
            "source_ref": {"novel": "isekai", "chapter": 9, "lesson_id": "p2_c07_b01", "label": "Ngữ pháp N2 — 提案（〜てみてはどうだろうか）"}
        },
    ]
}
