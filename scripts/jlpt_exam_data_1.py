# -*- coding: utf-8 -*-
"""
Đề Thi Thử JLPT N2 Chuẩn Số 01 — 言語知識（文字・語彙・文法）
Cấu trúc chuẩn 100% kỳ thi thật (54 câu — 55 phút):
- 問題1 (1-5): 漢字読み (Cách đọc Kanji)
- 問題2 (6-10): 表記 (Chọn chữ Hán đúng)
- 問題3 (11-15): 語形成 (Cấu tạo từ / Tiền tố - Hậu tố)
- 問題4 (16-22): 文脈規定 (Điền từ vào ngữ cảnh)
- 問題5 (23-27): 言い換え類義 (Từ đồng nghĩa)
- 問題6 (28-32): 用法 (Cách dùng từ đúng trong câu)
- 問題7 (33-44): 文の文法1 (Ngữ pháp câu)
- 問題8 (45-49): 文の文法2 ★ (Sắp xếp thứ tự câu)
- 問題9 (50-54): 文章の文法 (Ngữ pháp đoạn văn)
"""

PASSAGE_EXAM1 = (
    "最近、日本人の間でも電子書籍を読む人が増えてきた。通勤電車の中でスマートフォンやタブレットを開いている姿を（　50　）、紙の本が完全に消えたわけではない。\n"
    "紙の本には、ページをめくる手触りやインクの香り、（　51　）自分の本棚に並べて眺める楽しみがある。実際、「小説だけは紙で読みたい」という読者も少なくない。電子書籍は持ち運びに便利である（　52　）、目が疲れやすいという短所も指摘されている。\n"
    "（　53　）、両者にはそれぞれの良さがあり、場面に応じて使い分けるのが最も賢い方法だと言えるだろう。技術の進歩によって本の形は変わっても、物語が人の心を動かす力そのものはこれからも（　54　）。"
)

PASSAGE_EXAM1_VI = (
    "Gần đây ngay cả ở Nhật Bản số người đọc sách điện tử cũng tăng lên. Dù ta thường thấy cảnh mọi người mở điện thoại hay máy tính bảng trên tàu điện đi làm, nhưng sách giấy vẫn chưa hề biến mất hoàn toàn.\n"
    "Sách giấy có cảm giác lật từng trang giấy, mùi hương của mực in, và hơn thế nữa còn có niềm vui được xếp lên giá sách của riêng mình để ngắm nhìn. Thực tế không ít độc giả vẫn nói 'Riêng tiểu thuyết thì tôi chỉ muốn đọc bản giấy'. Mặt khác dù sách điện tử tiện mang theo nhưng cũng bị chỉ ra nhược điểm là dễ gây mỏi mắt.\n"
    "Chính vì vậy, mỗi bên đều có cái hay riêng, nên việc sử dụng linh hoạt tùy hoàn cảnh có lẽ là cách thông minh nhất. Dù hình thức của cuốn sách có thay đổi theo tiến bộ công nghệ, bản thân sức mạnh lay động trái tim con người của câu chuyện chắc chắn từ nay về sau cũng sẽ không bao giờ đổi thay."
)

EXAM_1 = {
    "id": "jlpt-n2-de-01",
    "code": "ĐỀ CHUẨN JLPT N2 — SỐ 01",
    "title_jp": "第1回 JLPT N2 模擬試験（言語知識：文字・語彙・文法）",
    "title_vi": "Đề Thi Thử JLPT N2 Số 01 — Kiến Thức Ngôn Ngữ Toàn Diện",
    "category": "full",
    "duration_min": 55,
    "pass_score": 19,
    "max_score": 60,
    "description": "Đề thi chuẩn cấu trúc Mondai 1–9 (54 câu), tổng hợp từ vựng trọng tâm Shinkanzen N2 (tình cảm, ẩm thực, sức khỏe, kinh tế, cấu tạo từ) cùng hệ thống ngữ pháp N2 kinh điển.",
    "yuki_note_start": "Hít một hơi thật sâu nhé em~ Đề số 01 mô phỏng chuẩn 100% cấu trúc 9 dạng bài **文字・語彙・文法** của kỳ thi JLPT N2 thật luôn! Đừng vội chọn lướt ở Mondai 6 (用法) và Mondai 8 (★) nhé. Chị Yuki ngồi ngay bên cạnh cổ vũ em nè 🌸✨",
    "yuki_note_finish_pass": "Tuyệt vời ông mặt trời!! Em đã vượt mốc điểm liệt và chạm ngưỡng đỗ **JLPT N2** ở Đề 01 rồi đó! Nhớ bấm lọc các câu sai (nếu có) để xem lời nhắc riêng của chị Yuki nha 🎉💖",
    "yuki_note_finish_try": "Ôi không sao hết trơn á~ Đề thi thử chính là lúc mình phát hiện lỗ hổng để vá ngay trước khi đi thi thật mà! Em đọc kỹ từng giải thích cả câu Đúng lẫn câu Sai bên dưới, rồi đọc lại chương tiểu thuyết tương ứng là nhớ vĩnh viễn luôn đó 🌸💪",
    "questions": [
        # --- 問題1: 漢字読み (1-5) ---
        {
            "num": 1,
            "mondai": "問題1：漢字読み",
            "mondai_vi": "Cách đọc Kanji",
            "prompt": "台所で野菜を<u>刻んで</u>、スープの準備をする。",
            "prompt_vi": "Thái nhỏ rau củ trong bếp để chuẩn bị nấu súp.",
            "options": ["きざんで", "つぶして", "むいて", "こねて"],
            "ans": 1,
            "cute_right_msg": "Đỉnh của chóp! Trong Bếp nhà Kenji (Romcom Ch.03), cậu ấy suốt ngày thái hành băm rau luôn đó nhớ hông~ 🌸",
            "right_exp": "`刻（きざ）む` (Khắc) đọc là **きざむ**, nghĩa là thái nhỏ, băm nhỏ (rau củ, hành tỏi) hoặc khắc vào đá/ký ức.",
            "cute_wrong_msg": "Suýt xíu nữa thôi em ơi~ Chữ `刻` trong 'thái nhỏ rau củ' đọc khác mấy động tác nấu ăn kia một chút nha! 🍳",
            "wrong_exps": [
                "Chính xác tuyệt đối! `刻（きざ）む` = thái nhỏ, băm nhuyễn (`きざんで`).",
                "`つぶす` ứng với chữ `潰す` (nghiền nát khoai tây, làm vỡ).",
                "`むく` ứng với chữ `剥く` (gọt vỏ hoa quả/khoai).",
                "`こねる` ứng với chữ `捏ねる` (nhào bột làm bánh)."
            ],
            "source_ref": {"novel": "romcom", "chapter": 3, "lesson_id": "p1_c02_b01", "label": "Bộ 1 Romcom Ch.03 (Bài 4: Ẩm thực)"}
        },
        {
            "num": 2,
            "mondai": "問題1：漢字読み",
            "mondai_vi": "Cách đọc Kanji",
            "prompt": "会議の前に、自分の主張を裏付ける<u>証拠</u>をそろえた。",
            "prompt_vi": "Trước cuộc họp, tôi đã thu thập đầy đủ chứng cứ chứng minh cho lập luận của mình.",
            "options": ["しょうこう", "しょうこ", "せいこう", "せいこ"],
            "ans": 2,
            "cute_right_msg": "Chuẩn không cần chỉnh! Em tỉnh táo né gọn bẫy trường âm `こう` luôn nè, giỏi quá xá 🌟",
            "right_exp": "`証拠` đọc ngắn gọn không có trường âm ở chữ `拠`: **しょうこ** (Chứng cứ).",
            "cute_wrong_msg": "Cẩn thận bẫy trường âm của JLPT nha em ơi! Chữ `拠（こ）` KHÔNG kéo dài `う` đâu nè~ 💡",
            "wrong_exps": [
                "Dư trường âm `う` ở cuối! Chữ `拠` đọc ngắn là `こ`, không phải `こう`.",
                "Chính xác! `証拠（しょうこ）` — không có trường âm ở âm tiết cuối.",
                "`せいこう` là `成功` (thành công) hoặc `精巧` (tinh xảo).",
                "`せいこ` không ứng với từ `証拠`."
            ],
            "source_ref": {"novel": "isekai", "chapter": 3, "lesson_id": "p1_c07_b04", "label": "Bộ 3 Isekai Ch.03 (Bài 17: Pháp luật)"}
        },
        {
            "num": 3,
            "mondai": "問題1：漢字読み",
            "mondai_vi": "Cách đọc Kanji",
            "prompt": "この機械の<u>精度</u>は非常に高く、誤差がほとんどない。",
            "prompt_vi": "Độ chính xác của cỗ máy này cực kỳ cao, hầu như không có sai số.",
            "options": ["せいと", "せいてい", "せいど", "しょうど"],
            "ans": 3,
            "cute_right_msg": "Chính xác luôn! Phân biệt rành rọt với `制度` mà nhớ đọc có biến âm đục `ど` quá giỏi 💕",
            "right_exp": "`精度` (Tinh độ — độ chính xác) đọc là **せいど** (chú ý biến âm đục `ど`, không phải `と`).",
            "cute_wrong_msg": "Nhẹ nhàng nhắc em nè: chữ `度` khi chỉ mức độ/chế độ đứng sau hay đọc là `ど` (đục) hơn là `と` nha! ✨",
            "wrong_exps": [
                "`せいと` thường là `生徒` (học sinh).",
                "`せいてい` là `制定` (ban hành luật lệ).",
                "Tuyệt vời! `精度（せいど）` = độ chính xác.",
                "`しょうど` không phải cách đọc của `精（せい）度（ど）`."
            ],
            "source_ref": {"novel": "isekai", "chapter": 5, "lesson_id": "p1_c08_b02", "label": "Bộ 3 Isekai Ch.05 (Bài 19: Khoa học)"}
        },
        {
            "num": 4,
            "mondai": "問題1：漢字読み",
            "mondai_vi": "Cách đọc Kanji",
            "prompt": "長年つきあっていた恋人に<u>裏切られて</u>、深く傷ついた。",
            "prompt_vi": "Bị người yêu gắn bó nhiều năm phản bội nên tôi tổn thương sâu sắc.",
            "options": ["うらぎられて", "うらきられて", "りきられて", "りぎられて"],
            "ans": 1,
            "cute_right_msg": "Ôi chuẩn đét! Có biến âm đục `ぎ` (`うらぎる`) — em học kỹ Bộ Yandere Ch.01 quá luôn đó 🌹",
            "right_exp": "`裏切る` (Lý Thiết — phản bội) đọc là **うらぎる**, bị động là **うらぎられて** (nhớ biến âm thành `ぎ`!).",
            "cute_wrong_msg": "Ôi nhắc khẽ em nè: ghép `裏（うら）` + `切る（きる）` bị biến âm ở giữa thành đục `ぎ` nha em! 🖤",
            "wrong_exps": [
                "Chính xác tuyệt đối! `裏切（うらぎ）られる` — biến âm `き → ぎ` rất quan trọng.",
                "Thiếu biến âm đục rồi: phải là `うらぎられて`, không phải `うらきられて`.",
                "Chữ `裏` ở đây đọc kun-yomi là `うら`, không đọc on-yomi `り`.",
                "Tương tự, `裏切る` luôn đọc âm kun `うらぎる`."
            ],
            "source_ref": {"novel": "yandere", "chapter": 1, "lesson_id": "p1_c01_b03", "label": "Bộ 2 Yandere Ch.01 (Bài 3: Cảm xúc)"}
        },
        {
            "num": 5,
            "mondai": "問題1：漢字読み",
            "mondai_vi": "Cách đọc Kanji",
            "prompt": "両親の顔に<u>泥</u>を塗るような真似は絶対にできない。",
            "prompt_vi": "Tuyệt đối không thể làm chuyện bôi nhọ danh dự cha mẹ như thế được.",
            "options": ["ほこり", "つち", "どろ", "あせ"],
            "ans": 3,
            "cute_right_msg": "Quá siêu! `顔に泥（どろ）を塗る` là quán dụng ngữ N2 siêu hay gặp luôn đó! ✨",
            "right_exp": "`泥（どろ）` nghĩa là bùn đất. Thành ngữ `顔に泥を塗る` nghĩa là bôi tro trát trấu, làm mất thể diện người khác.",
            "cute_wrong_msg": "Suýt đúng rồi nè! Chữ `泥` đọc là `どろ` (bùn) chứ không phải đất `つち` hay bụi `ほこり` đâu nha~ 🌱",
            "wrong_exps": [
                "`ほこり` là chữ `埃` (bụi bặm) hoặc `誇り` (niềm tự hào).",
                "`つち` là chữ `土` (đất nói chung).",
                "Chính xác! `泥（どろ）` trong quán dụng `顔に泥を塗る`.",
                "`あせ` là chữ `汗` (mồ hôi)."
            ],
            "source_ref": {"novel": "romcom", "chapter": 13, "lesson_id": "p2_c06_b01", "label": "Bộ 1 Romcom Ch.13 (Bài 32: Quán dụng ngữ)"}
        },
        # --- 問題2: 表記 (6-10) ---
        {
            "num": 6,
            "mondai": "問題2：表記",
            "mondai_vi": "Chọn Kanji đúng",
            "prompt": "友人の家族に会ったとき、とても温かく<u>もてなして</u>くれた。",
            "prompt_vi": "Khi gặp gia đình người bạn, họ đã tiếp đón tôi vô cùng nồng hậu.",
            "options": ["持て成して", "待て成して", "持って為して", "歓待して"],
            "ans": 1,
            "cute_right_msg": "Trời ơi chữ Kanji ẩn của `もてなす` hơi bị hiếm mà em cũng nhớ trúng `持て成す` luôn!! Quá đỉnh 🌸",
            "right_exp": "`もてなす` (chiêu đãi, tiếp đón nồng hậu) có chữ Hán là **持て成す** (TRÌ THÀNH).",
            "cute_wrong_msg": "Chữ này hơi khó chút vì hay viết bằng hiragana nè~ Mẹo nhớ: 'cầm (持) lòng thành (成) ra tiếp đãi' = `持て成す` nha em! 💖",
            "wrong_exps": [
                "Chính xác! `持て成（もてな）す` = tiếp đãi, chiêu đãi nồng hậu.",
                "Chữ đầu là `持` (cầm/mang), không phải `待` (chờ đợi).",
                "Không viết theo dạng `持って為して` (thừa `っ` và dùng sai chữ `為`).",
                "`歓待する` đọc là `かんたいする`, không đọc là `もてなす`."
            ],
            "source_ref": {"novel": "yandere", "chapter": 1, "lesson_id": "p1_c01_b03", "label": "Bộ 2 Yandere Ch.01 (Bài 3: Cảm xúc)"}
        },
        {
            "num": 7,
            "mondai": "問題2：表記",
            "mondai_vi": "Chọn Kanji đúng",
            "prompt": "新しい規則が来月から<u>しこう</u>されることになった。",
            "prompt_vi": "Quy định mới sẽ bắt đầu có hiệu lực thi hành từ tháng sau.",
            "options": ["施工", "施行", "思考", "志向"],
            "ans": 2,
            "cute_right_msg": "Chuẩn đét! `法律・規則が施行される` đọc là `しこう` dùng chữ `行` (thi hành) chứ không phải `工` (công trình) nè! ⚖️",
            "right_exp": "Các từ đồng âm `しこう`: **施行** (thi hành luật lệ), `施工` (thi công xây dựng — thường đọc せこう/しこう), `思考` (suy nghĩ), `志向` (chí hướng).",
            "cute_wrong_msg": "Ôi bẫy đồng âm `しこう` kinh điển của JLPT N2 đó em! Luật lệ phải dùng `施行` (chữ Hành = đi vào thực hành) nha~ ✨",
            "wrong_exps": [
                "`施工` dùng cho công trình xây dựng (`工事を施工する`).",
                "Quá chuẩn! `施行（しこう）される` = chính thức có hiệu lực thi hành.",
                "`思考` là tư duy suy nghĩ (`論理的思考`).",
                "`志向` là định hướng, xu hướng tâm lý (`安定志向`)."
            ],
            "source_ref": {"novel": "isekai", "chapter": 3, "lesson_id": "p1_c07_b04", "label": "Bộ 3 Isekai Ch.03 (Bài 17: Pháp luật)"}
        },
        {
            "num": 8,
            "mondai": "問題2：表記",
            "mondai_vi": "Chọn Kanji đúng",
            "prompt": "急激な景気の変化で、企業の<u>ふさい</u>が膨らんでしまった。",
            "prompt_vi": "Vì kinh tế biến động đột ngột nên khoản nợ của doanh nghiệp đã phình to lên.",
            "options": ["不在", "負債", "不採", "付載"],
            "ans": 2,
            "cute_right_msg": "Chính xác! Chữ `負` (gánh) + `債` (nợ) = `負債（ふさい）`, nhớ chắc quá em ơi! 💼",
            "right_exp": "**負債（ふさい）** là khoản nợ nần, nghĩa vụ tài chính tồn đọng (Phụ Trái).",
            "cute_wrong_msg": "Chú ý đồng âm `ふさい` nha em: nợ nần thì phải có chữ `債` (Trái = nợ, như trong 借金/国債) → `負債` đó! 🪙",
            "wrong_exps": [
                "`不在（ふざい）` là vắng mặt (và đọc là ざい, không phải さい).",
                "Chuẩn không cần chỉnh! `負債（ふさい）` = khoản nợ.",
                "Chữ ghép giả không có nghĩa trong tiếng Nhật.",
                "`付載` không phải thuật ngữ kinh tế chỉ khoản nợ."
            ],
            "source_ref": {"novel": "isekai", "chapter": 2, "lesson_id": "p1_c07_b03", "label": "Bộ 3 Isekai Ch.02 (Bài 16: Kinh tế)"}
        },
        {
            "num": 9,
            "mondai": "問題2：表記",
            "mondai_vi": "Chọn Kanji đúng",
            "prompt": "台風が過ぎて、庭の草木が<u>しげって</u>いるのに気づいた。",
            "prompt_vi": "Cơn bão qua đi, tôi nhận ra cây cỏ trong vườn đang mọc sum suê rậm rạp.",
            "options": ["繁って", "茂って", "重って", "恵って"],
            "ans": 2,
            "cute_right_msg": "Chính xác! Cây cỏ mọc um tùm dùng chữ `茂（しげ）る` có bộ thảo (`艹`) ở trên đầu nè~ 🌿",
            "right_exp": "`茂（しげ）る` (Mậu — có bộ Thảo `艹` biểu thị thực vật) nghĩa là cây cối mọc sum suê rậm rạp.",
            "cute_wrong_msg": "Mẹo siêu dễ nhớ nè em: cây cối sum suê thì trên đầu Kanji phải đội mũ cỏ (bộ Thảo `艹`) → **茂る** nhé! 🌱",
            "wrong_exps": [
                "`繁` thường gặp trong `繁華街`, động từ chuẩn chỉ cây cối mọc rậm trong N2 là `茂る`.",
                "Tuyệt vời! `茂（しげ）る` = mọc um tùm, rậm rạp.",
                "`重` đọc là `かさなる` (chồng chất) hoặc `おもい`.",
                "`恵` đọc là `めぐまれる` (được ban tặng)."
            ],
            "source_ref": {"novel": "isekai", "chapter": 1, "lesson_id": "p1_c04_b02", "label": "Bộ 3 Isekai Ch.01 (Bài 9: Thiên nhiên)"}
        },
        {
            "num": 10,
            "mondai": "問題2：表記",
            "mondai_vi": "Chọn Kanji đúng",
            "prompt": "古い商店街を新しく作り直す<u>さいかいはつ</u>が始まった。",
            "prompt_vi": "Dự án tái quy hoạch xây mới khu phố thương mại cũ đã bắt đầu.",
            "options": ["際開発", "最開発", "再開発", "災開発"],
            "ans": 3,
            "cute_right_msg": "Chuẩn luôn! Tiền tố `再（さい）` = làm lại lần nữa (Tái phát triển = `再開発`) siêu mượt! ✨",
            "right_exp": "Tiền tố **再（さい）** mang nghĩa tái lập, làm lại một lần nữa: `再開発` (tái phát triển/quy hoạch lại).",
            "cute_wrong_msg": "Nhầm nhẹ đồng âm `さい` rồi em ơi! 'Tái' (làm lại lần 2) là chữ `再` (`再利用・再確認`), không phải `最` (nhất) nha~ 💡",
            "wrong_exps": [
                "`際` là dịp, khi (`国際`, `際立つ`), không ghép với `開発`.",
                "`最` nghĩa là nhất (`最先端`, `最高`), không mang nghĩa 'làm lại'.",
                "Chính xác tuyệt đối! `再開発（さいかいはつ）`.",
                "`災` là tai họa (`災害`), không dùng ở đây."
            ],
            "source_ref": {"novel": "isekai", "chapter": 10, "lesson_id": "p2_c07_b02", "label": "Bộ 3 Isekai Ch.10 (Bài 35: Tiền tố)"}
        },
        # --- 問題3: 語形成 (11-15) ---
        {
            "num": 11,
            "mondai": "問題3：語形成",
            "mondai_vi": "Cấu tạo từ (Tiền tố / Hậu tố)",
            "prompt": "この商品は（　　）<u>向け</u>に作られているので、専門知識がなくても読める。",
            "prompt_vi": "Sản phẩm này được làm dành riêng cho người mới bắt đầu, nên không có kiến thức chuyên môn vẫn đọc được.",
            "options": ["初心者", "経験者", "専門", "研究"],
            "ans": 1,
            "cute_right_msg": "Quá chuẩn! Đọc vế sau 'không cần kiến thức chuyên môn vẫn hiểu' → đích thị `初心者向け（しょしんしゃむけ）` luôn! 📘",
            "right_exp": "`初心者向け` (dành cho người mới nhập môn) khớp hoàn hảo với vế giải thích phía sau `専門知識がなくても読める`.",
            "cute_wrong_msg": "Nhìn gợi ý ở vế sau nha em: 'không có kiến thức chuyên môn cũng đọc được' thì phải dành cho đối tượng mới bắt đầu chứ nhỉ~ 🌸",
            "wrong_exps": [
                "Chính xác! `初心者向け` = thiết kế riêng cho người mới bắt đầu.",
                "`経験者` là người đã có kinh nghiệm (mâu thuẫn với vế sau).",
                "`専門向け` không tự nhiên và mâu thuẫn với 'không có kiến thức chuyên môn'.",
                "`研究向け` thiếu danh từ chỉ người và sai ngữ cảnh."
            ],
            "source_ref": {"novel": "isekai", "chapter": 11, "lesson_id": "p2_c07_b03", "label": "Bộ 3 Isekai Ch.11 (Bài 36: Hậu tố)"}
        },
        {
            "num": 12,
            "mondai": "問題3：語形成",
            "mondai_vi": "Cấu tạo từ (Tiền tố / Hậu tố)",
            "prompt": "その事件の詳しい原因は、警察の捜査が進んでもまだ（　　）<u>解決</u>のままだ。",
            "prompt_vi": "Nguyên nhân chi tiết của vụ án ấy dù cảnh sát có điều tra tiến triển vẫn còn chưa được giải quyết.",
            "options": ["無", "不", "非", "未"],
            "ans": 4,
            "cute_right_msg": "Chuẩn hết sẩy! Trạng thái 'hiện tại VẪN CHƯA giải quyết xong' phải dùng tiền tố **未（み）** (`未解決`)! 🔍",
            "right_exp": "Tiền tố **未（み）** diễn tả điều gì đó *hiện tại vẫn chưa xong / chưa đạt*: `未解決（みかいけつ）`, `未経験`, `未完成`.",
            "cute_wrong_msg": "Chị Yuki nhắc nhẹ nè: bộ tứ `無・不・非・未` tuy đều phủ định nhưng hễ có từ khóa 'vẫn còn CHƯA... (`まだ〜のまま`)' thì 100% chọn **未（み）** nhé! ✨",
            "wrong_exps": [
                "`無` nghĩa là 'không có 0%' (`無料・無関係`), không có `無解決`.",
                "`不` là bất ổn (`不都合・不規則`), không ghép với `解決`.",
                "`非` là phi chuẩn (`非常識・非公式`).",
                "Tuyệt vời! `未解決（みかいけつ）` = chưa được giải quyết."
            ],
            "source_ref": {"novel": "isekai", "chapter": 10, "lesson_id": "p2_c07_b02", "label": "Bộ 3 Isekai Ch.10 (Bài 35: Tiền tố)"}
        },
        {
            "num": 13,
            "mondai": "問題3：語形成",
            "mondai_vi": "Cấu tạo từ (Tiền tố / Hậu tố)",
            "prompt": "病院へ通うたびに高額な（　　）<u>費</u>がかかるので、保険の大切さを実感した。",
            "prompt_vi": "Cứ mỗi lần đi bệnh viện lại tốn chi phí y tế đắt đỏ nên tôi thấm thía tầm quan trọng của bảo hiểm.",
            "options": ["生活", "医療", "交際", "開発"],
            "ans": 2,
            "cute_right_msg": "Chính xác! Đi bệnh viện (`病院へ通う`) và bảo hiểm (`保険`) → chắc chắn là `医療費（いりょうひ）` rồi! 🏥",
            "right_exp": "`医療費（いりょうひ）` = chi phí y tế khám chữa bệnh, ghép chuẩn với hậu tố `〜費` và ngữ cảnh bệnh viện/bảo hiểm.",
            "cute_wrong_msg": "Đọc kỹ gợi ý 'đi bệnh viện' (`病院`) và 'bảo hiểm' (`保険`) để chọn đúng tiền tố trước `費` nha em~ 💊",
            "wrong_exps": [
                "`生活費` là tiền sinh hoạt chung hàng tháng, không riêng cho mỗi lần đi viện.",
                "Đúng rồi! `医療費（いりょうひ）` = chi phí y tế.",
                "`交際費` là chi phí ngoại giao/giao tiếp xã giao.",
                "`開発費` là kinh phí nghiên cứu phát triển sản phẩm."
            ],
            "source_ref": {"novel": "isekai", "chapter": 11, "lesson_id": "p2_c07_b03", "label": "Bộ 3 Isekai Ch.11 (Bài 36: Hậu tố)"}
        },
        {
            "num": 14,
            "mondai": "問題3：語形成",
            "mondai_vi": "Cấu tạo từ (Tiền tố / Hậu tố)",
            "prompt": "忙しいからといって、決して相手の話を途中で切るような（　　）<u>常識</u>な態度は許されない。",
            "prompt_vi": "Dù có bận rộn đi chăng nữa, thái độ thiếu phép tắc kiểu ngắt lời người khác giữa chừng cũng tuyệt đối không thể chấp nhận.",
            "options": ["無", "不", "非", "反"],
            "ans": 3,
            "cute_right_msg": "Chuẩn luôn! Cụm từ nổi tiếng của tiền tố `非`: `非常識（ひじょうしき）` = vô ý thức, trái với lẽ thường! ✨",
            "right_exp": "**非常識（ひじょうしき）** là từ cố định dùng tiền tố `非` (phi/trái với chuẩn mực thường thức).",
            "cute_wrong_msg": "Nhớ luôn cụm đi liền với `常識` nè em: chỉ có `非常識` chứ không có `無常識` hay `不常識` đâu nha~ 💡",
            "wrong_exps": [
                "Không có từ `無常識` trong tiếng Nhật.",
                "Không có từ `不常識` trong tiếng Nhật.",
                "Chính xác! `非常識（ひじょうしき）な態度` = thái độ thiếu phép tắc lịch sự.",
                "Không dùng tiền tố `反` cho `常識`."
            ],
            "source_ref": {"novel": "isekai", "chapter": 10, "lesson_id": "p2_c07_b02", "label": "Bộ 3 Isekai Ch.10 (Bài 35: Tiền tố)"}
        },
        {
            "num": 15,
            "mondai": "問題3：語形成",
            "mondai_vi": "Cấu tạo từ (Tiền tố / Hậu tố)",
            "prompt": "この小説は登場人物の人間的な（　　）<u>み</u>が丁寧に描かれていて、何度読んでも感動する。",
            "prompt_vi": "Cuốn tiểu thuyết này khắc họa tinh tế chiều sâu tâm hồn con người của các nhân vật nên đọc bao nhiêu lần cũng thấy xúc động.",
            "options": ["長", "広", "深", "高"],
            "ans": 3,
            "cute_right_msg": "Quá tinh tế! `人間的な深み（ふかみ）` = chiều sâu tâm lý con người (tính từ ghép hậu tố `〜み` cảm nhận chiều sâu)! 📖",
            "right_exp": "Tính từ `深い` bỏ `い` + `〜み` → **深み（ふかみ）**: chiều sâu tinh thần, chiều sâu hương vị/nhân văn (ngược với `深さ` đo bằng mét).",
            "cute_wrong_msg": "Bài cuối Isekai Ch.12 vừa học xong đó em: chiều sâu tâm hồn nhân vật dùng `〜み` từ tính từ `深い` → `深み` nha~ 🌸",
            "wrong_exps": [
                "Không dùng `長み` để chỉ chiều sâu nhân văn (`長さ` mới chỉ độ dài).",
                "Không dùng `広み` (`広さ` mới chỉ diện tích).",
                "Tuyệt vời! `人間的な深み（ふかみ）` = chiều sâu tâm hồn.",
                "`高み` nghĩa là đỉnh cao/tầm cao thượng (`高みを目指す`), ít tự nhiên khi đi cùng 'nhân tính' bằng `深み`."
            ],
            "source_ref": {"novel": "isekai", "chapter": 12, "lesson_id": "p2_c07_b04", "label": "Bộ 3 Isekai Ch.12 (Bài 37: Tính từ → N/V)"}
        },
        # --- 問題4: 文脈規定 (16-22) ---
        {
            "num": 16,
            "mondai": "問題4：文脈規定",
            "mondai_vi": "Điền từ vựng theo ngữ cảnh",
            "prompt": "新人のころ、いつも優しく助けてくれた先輩には今でも（　　）。",
            "prompt_vi": "Đối với người tiền bối luôn dịu dàng giúp đỡ mình hồi còn là nhân viên mới, đến giờ tôi vẫn mang ơn không dám cãi / nể phục hết mực.",
            "options": ["頭が下がる", "頭が上がらない", "頭を抱える", "耳が痛い"],
            "ans": 2,
            "cute_right_msg": "Quán dụng ngữ chuẩn đét!! Phân biệt rành mạch `頭が上がらない` (mang ơn/lép vế không ngẩng đầu cãi nổi) với `頭が下がる` (kính phục tự nguyện) luôn! 🏆",
            "right_exp": "`（人に）頭が上がらない` dùng khi mình **mang ơn lớn** hoặc có điểm yếu với đối phương nên luôn tôn trọng/không dám cãi. (Chú ý: nếu khen phẩm chất chung như sự nỗ lực của ai đó mới dùng `頭が下がる`).",
            "cute_wrong_msg": "Úi suýt dính bẫy cặp song sinh `頭が下がる` vs `頭が上がらない` rồi em ơi! Nhớ nhé: 'được giúp đỡ mãi nên mắc nợ ân tình' → `頭が上がらない`! 💖",
            "wrong_exps": [
                "`頭が下がる` là ngưỡng mộ cúi đầu trước nỗ lực cao đẹp của người khác (`その誠実さには頭が下がる`), không nhấn mạnh ân tình mang ơn cá nhân như `頭が上がらない`.",
                "Chính xác tuyệt đối! `助けてくれた人には頭が上がらない`.",
                "`頭を抱える` là ôm đầu bế tắc khổ sở vì rắc rối/nợ nần.",
                "`耳が痛い` là nhột/chói tai vì bị nói trúng khuyết điểm."
            ],
            "source_ref": {"novel": "romcom", "chapter": 13, "lesson_id": "p2_c06_b01", "label": "Bộ 1 Romcom Ch.13 (Bài 32: Quán dụng ngữ 1)"}
        },
        {
            "num": 17,
            "mondai": "問題4：文脈規定",
            "mondai_vi": "Điền từ vựng theo ngữ cảnh",
            "prompt": "あの人は人前では明るく笑っているが、実は誰よりも（　　）性格かもしれない。",
            "prompt_vi": "Anh ấy trước mặt mọi người cứ cười tươi thế thôi, nhưng thật ra có lẽ lại là người nhạy cảm dễ tổn thương hơn ai hết.",
            "options": ["繊細な", "頑固な", "陽気な", "図々しい"],
            "ans": 1,
            "cute_right_msg": "Đỉnh luôn! Nhan đề Chương 02 Bộ Romcom `繊細な心（せんさいなこころ）` là nhớ liền tính từ `繊細（せんさい）` (tinh tế, nhạy cảm) ha em~ 🌸",
            "right_exp": "`繊細（せんさい）な性格` = tính cách nhạy cảm, tinh tế (tạo tương phản với vế trước 'cười rạng rỡ trước mặt mọi người').",
            "cute_wrong_msg": "Đọc kỹ chữ `が` (nhưng) ở vế đầu nha: bên ngoài tươi cười lạc quan, *nhưng thật ra* bên trong lại... mỏng manh nhạy cảm → `繊細な`! 💌",
            "wrong_exps": [
                "Quá chuẩn! `繊細（せんさい）な` = tinh tế, nhạy cảm dễ tổn thương.",
                "`頑固（がんこ）な` là cố chấp, bướng bỉnh.",
                "`陽気（ようき）な` là vui vẻ hoạt bát (trùng nghĩa với 'cười tươi', không hợp nối bằng `が`).",
                "`図々（ずうずう）しい` là trơ trẽn, mặt dày vô duyên."
            ],
            "source_ref": {"novel": "romcom", "chapter": 2, "lesson_id": "p1_c01_b02", "label": "Bộ 1 Romcom Ch.02 (Bài 2: Tính cách)"}
        },
        {
            "num": 18,
            "mondai": "問題4：文脈規定",
            "mondai_vi": "Điền từ vựng theo ngữ cảnh",
            "prompt": "会議の意見がみんな（　　）で、なかなか一つの結論にまとまらない。",
            "prompt_vi": "Ý kiến trong cuộc họp mỗi người một phách rời rạc nên mãi mà chẳng gom lại thành một kết luận chung được.",
            "options": ["ぴったり", "ぎっしり", "ばらばら", "こつこつ"],
            "ans": 3,
            "cute_right_msg": "Chuẩn không cần chỉnh! `意見がばらばら` là từ tượng hình cực hay ra thi JLPT N2 luôn! 🎯",
            "right_exp": "`ばらばら` nghĩa là tản mác, rời rạc, mỗi người một ý không thống nhất.",
            "cute_wrong_msg": "Mỗi người một ý 'mãi không gom lại thành một kết luận' là từ tượng hình `ばらばら` (rời rạc) nha em~ 🌈",
            "wrong_exps": [
                "`ぴったり` là vừa vặn trùng khớp in.",
                "`ぎっしり` là chật ních kín mít.",
                "Chính xác! `意見がばらばらでまとまらない`.",
                "`こつこつ` là kiên trì cần mẫn từng bước."
            ],
            "source_ref": {"novel": "isekai", "chapter": 8, "lesson_id": "p2_c05_b01", "label": "Bộ 3 Isekai Ch.08 (Bài 31: Onomatopoeia)"}
        },
        {
            "num": 19,
            "mondai": "問題4：文脈規定",
            "mondai_vi": "Điền từ vựng theo ngữ cảnh",
            "prompt": "この商品は機能もデザインも素晴らしく、他社製品より価格を低く抑えることで競争力を（　　）。",
            "prompt_vi": "Sản phẩm này vừa tính năng lẫn thiết kế đều tuyệt vời, lại kiềm giữ mức giá thấp hơn đối thủ giúp nâng cao sức cạnh tranh.",
            "options": ["高めた", "弱めた", "早めた", "固まった"],
            "ans": 1,
            "cute_right_msg": "Quá chuẩn! Có trợ từ `を` ở `競争力を` nên chọn Tha động từ `高めた` (nâng cao năng lực cạnh tranh)! ⚙️",
            "right_exp": "`競争力を高（たか）める` = nâng cao sức cạnh tranh (nhớ dùng tha động từ đuôi `〜める` đi với trợ từ `を`).",
            "cute_wrong_msg": "Nhìn vế `競争力を` nhé em: sản phẩm vừa đẹp vừa rẻ thì phải *nâng cao* năng lực cạnh tranh (`高める`) chứ ha! ✨",
            "wrong_exps": [
                "Chính xác! `競争力を高める` = nâng cao sức cạnh tranh.",
                "`弱める` là làm suy yếu đi (ngược nghĩa).",
                "`早める` là đẩy thời gian lên sớm hơn.",
                "`固まった` là TỰ động từ (đi với trợ từ が)."
            ],
            "source_ref": {"novel": "isekai", "chapter": 12, "lesson_id": "p2_c07_b04", "label": "Bộ 3 Isekai Ch.12 (Bài 37: Tính từ → N/V)"}
        },
        {
            "num": 20,
            "mondai": "問題4：文脈規定",
            "mondai_vi": "Điền từ vựng theo ngữ cảnh",
            "prompt": "大切な試験の発表が近くて不安でたまらず、何をしても手（　　）。",
            "prompt_vi": "Sắp công bố kết quả kỳ thi quan trọng nên lo lắng bồn chồn khôn nguôi, làm gì cũng không tập trung nổi.",
            "options": ["を打つ", "を抜く", "につかない", "が回らない"],
            "ans": 3,
            "cute_right_msg": "Chuẩn 100%! Nỗi lòng trước ngày biết điểm JLPT: `何事も手につかない` (không tập trung làm việc gì nổi)! 💓",
            "right_exp": "`手につかない` nghĩa là tâm trí rối bời lo âu hoặc hồi hộp đến mức không thể bắt tay hay tập trung vào làm việc gì.",
            "cute_wrong_msg": "Chà, cả 4 đều có chữ `手` dễ lẫn lắm nè! Khi tâm trí rối bời lo âu 'làm gì cũng chẳng vô đầu' là `手につかない` nha em! 🌸",
            "wrong_exps": [
                "`手を打つ` là chủ động ra tay áp dụng biện pháp đối phó (`事前に手を打つ`).",
                "`手を抜く` là cố tình làm ẩu ăn bớt công đoạn.",
                "Tuyệt vời! `不安で手につかない`.",
                "`手が回らない` là quá nhiều việc bận rộn không đủ tay xoay xở hết."
            ],
            "source_ref": {"novel": "yandere", "chapter": 12, "lesson_id": "p2_c06_b02", "label": "Bộ 2 Yandere Ch.12 (Bài 33: Quán dụng ngữ 2)"}
        },
        {
            "num": 21,
            "mondai": "問題4：文脈規定",
            "mondai_vi": "Điền từ vựng theo ngữ cảnh",
            "prompt": "環境保護のため、不要なエネルギーの消費をできるだけ（　　）する必要がある。",
            "prompt_vi": "Để bảo vệ môi trường, cần thiết phải cắt giảm tối đa việc tiêu thụ năng lượng không cần thiết.",
            "options": ["排出（はいしゅつ）", "削減（さくげん）", "枯渇（こかつ）", "汚染（おせん）"],
            "ans": 2,
            "cute_right_msg": "Chính xác! Cụm tiêu chuẩn bảo vệ môi trường & cắt giảm chi phí: `消費・経費を削減する`! 🌱",
            "right_exp": "`削減（さくげん）する` (Tước Giảm) nghĩa là cắt giảm mạnh (lượng tiêu thụ năng lượng, khí thải CO2, ngân sách/chi phí).",
            "cute_wrong_msg": "Động từ có chữ `減` (giảm) để cắt giảm lãng phí chính là `削減（さくげん）する` đó em~ 🌍",
            "wrong_exps": [
                "`排出する` là thải ra ngoài (khí thải, rác thải).",
                "Quá chuẩn! `エネルギー消費を削減する`.",
                "`枯渇する` là bị cạn kiệt (tài nguyên thiên nhiên).",
                "`汚染する` là gây ô nhiễm."
            ],
            "source_ref": {"novel": "isekai", "chapter": 4, "lesson_id": "p1_c08_b01", "label": "Bộ 3 Isekai Ch.04 (Bài 18: Sinh thái)"}
        },
        {
            "num": 22,
            "mondai": "問題4：文脈規定",
            "mondai_vi": "Điền từ vựng theo ngữ cảnh",
            "prompt": "インターネットの普及により、必要な情報を誰とでも簡単に（　　）できるようになった。",
            "prompt_vi": "Nhờ Internet phổ cập, ta đã có thể dễ dàng chia sẻ những thông tin cần thiết với bất kỳ ai.",
            "options": ["共有（きょうゆう）", "検索（けんさく）", "接続（せつぞく）", "入力（にゅうりょく）"],
            "ans": 1,
            "cute_right_msg": "Đúng phóc! Chia sẻ dùng chung thông tin/tài liệu trên mạng với người khác (`誰とでも`) là `共有（きょうゆう）する`! 💻",
            "right_exp": "`共有（きょうゆう）する` = chia sẻ để nhiều người cùng nắm giữ/sử dụng chung (khớp với đối tượng `誰とでも`).",
            "cute_wrong_msg": "Nhìn cụm `誰とでも` (với bất kỳ ai) ở phía trước nhé em: hành động làm chung với nhiều người là `共有する` (cộng hưởng/chia sẻ) đó~ ✨",
            "wrong_exps": [
                "Chính xác! `情報を共有する` = chia sẻ thông tin cùng nhau.",
                "`検索する` là tự tra cứu tìm kiếm trên Google/hệ thống.",
                "`接続する` là kết nối mạng (`Wi-Fiに接続する`).",
                "`入力する` là nhập dữ liệu vào bàn phím."
            ],
            "source_ref": {"novel": "yandere", "chapter": 3, "lesson_id": "p1_c06_b02", "label": "Bộ 2 Yandere Ch.03 (Bài 13: Máy tính)"}
        },
        # --- 問題5: 言い換え類義 (23-27) ---
        {
            "num": 23,
            "mondai": "問題5：言い換え類義",
            "mondai_vi": "Từ / cụm từ đồng nghĩa",
            "prompt": "新プロジェクトの計画は、<u>およそ</u>3か月後に完成する見込みだ。",
            "prompt_vi": "Kế hoạch dự án mới dự kiến sẽ hoàn thành sau khoảng chừng 3 tháng nữa.",
            "options": ["だいたい", "ちょうど", "めったに", "かろうじて"],
            "ans": 1,
            "cute_right_msg": "Chuẩn luôn! `およそ` = `だいたい` = khoảng chừng, ước chừng đại khái! 🌟",
            "right_exp": "`およそ` là phó từ đứng trước con số chỉ sự ước lượng 'khoảng chừng, đại khái' = **だいたい / 約（やく）**.",
            "cute_wrong_msg": "Từ `およそ` học ở Isekai Ch.06 (Số lượng) nghĩa là 'khoảng chừng' chứ không phải chính xác tuyệt đối hay hiếm khi đâu nha em~ 🕰️",
            "wrong_exps": [
                "Chính xác! `およそ` ≈ `だいたい` (khoảng chừng, xấp xỉ).",
                "`ちょうど` là vừa vặn đúng chẵn (`ちょうど3か月`).",
                "`めったに（〜ない）` là hiếm khi hầu như không.",
                "`かろうじて` là suýt soát vất vả lắm mới qua được."
            ],
            "source_ref": {"novel": "isekai", "chapter": 6, "lesson_id": "p1_c09_b01", "label": "Bộ 3 Isekai Ch.06 (Bài 20: Số lượng)"}
        },
        {
            "num": 24,
            "mondai": "問題5：言い換え類義",
            "mondai_vi": "Từ / cụm từ đồng nghĩa",
            "prompt": "この会議の議長は、どんなに忙しくても絶対に<u>手を抜かない</u>。",
            "prompt_vi": "Vị chủ tọa cuộc họp này dù bận đến mấy cũng tuyệt đối không bao giờ làm ẩu cho qua.",
            "options": ["怒らない", "あきらめない", "いいかげんにしない", "断らない"],
            "ans": 3,
            "cute_right_msg": "Tuyệt vời! `手を抜く` = làm ẩu, cẩu thả `いいかげんにする` — nên phủ định là không bao giờ làm ẩu! 💪",
            "right_exp": "`手を抜く` nghĩa là cắt bớt công đoạn, làm cẩu thả qua loa cho xong chuyện → `手を抜かない` = không làm cẩu thả (`いいかげんにしない`).",
            "cute_wrong_msg": "Đừng dịch đen `手を抜く` là rút tay ra nha em ơi~ Đó là quán dụng ngữ 'làm ẩu, qua loa đại khái' đó! 🌸",
            "wrong_exps": [
                "`怒らない` là không tức giận.",
                "`あきらめない` là không bỏ cuộc (khác với *chất lượng cẩu thả* khi vẫn đang làm!).",
                "Chính xác tuyệt đối! `手を抜かない` = `いいかげんにしない` (không làm cẩu thả qua loa).",
                "`断らない` là không từ chối."
            ],
            "source_ref": {"novel": "yandere", "chapter": 12, "lesson_id": "p2_c06_b02", "label": "Bộ 2 Yandere Ch.12 (Bài 33: Quán dụng ngữ 2)"}
        },
        {
            "num": 25,
            "mondai": "問題5：言い換え類義",
            "mondai_vi": "Từ / cụm từ đồng nghĩa",
            "prompt": "彼女は学生時代、いつも<u>こつこつ</u>と図書館で勉強を続けていた。",
            "prompt_vi": "Thời còn đi học, cô ấy luôn cần mẫn bền bỉ học tập đều đặn ở thư viện.",
            "options": ["急に", "真面目に少しずつ", "にぎやかに", "いらいらしながら"],
            "ans": 2,
            "cute_right_msg": "Đúng phóc! Hình ảnh học tập cần mẫn `こつこつ` = chăm chỉ bền bỉ từng chút một! 📚✨",
            "right_exp": "`こつこつ` diễn tả tác phong cần mẫn, nghiêm túc tích lũy từng chút từng chút một qua thời gian dài.",
            "cute_wrong_msg": "Từ tượng hình `こつこつ` là biểu tượng của sự bền bỉ từng bước nhỏ đó em, nhớ Bộ 3 Ch.08 hông nè~ 🌱",
            "wrong_exps": [
                "`急に` là đột ngột bất ngờ (`急に雨が降る`).",
                "Chính xác! `こつこつ` = kiên trì, nghiêm túc từng chút một.",
                "`にぎやかに` là nhộn nhịp tưng bừng.",
                "`いらいらしながら` là vừa làm vừa cáu kỉnh bực bội."
            ],
            "source_ref": {"novel": "isekai", "chapter": 8, "lesson_id": "p2_c05_b01", "label": "Bộ 3 Isekai Ch.08 (Bài 31: Onomatopoeia)"}
        },
        {
            "num": 26,
            "mondai": "問題5：言い換え類義",
            "mondai_vi": "Từ / cụm từ đồng nghĩa",
            "prompt": "明日の野外コンサートは、大雨が降るため来週に<u>延期</u>された。",
            "prompt_vi": "Buổi hòa nhạc ngoài trời ngày mai vì mưa lớn nên đã bị hoãn sang tuần sau.",
            "options": ["中止された", "先へ延ばされた", "長くされた", "早められた"],
            "ans": 2,
            "cute_right_msg": "Chuẩn tuyệt đối! Phân biệt quá siêu giữa `延期` (`先へ延ばす`: dời lịch ra sau) và `中止` (hủy hẳn)! 🎶",
            "right_exp": "`延期（えんき）する` là lùi lịch tổ chức ra một ngày khác muộn hơn (`先へ延ばす`). Khác với `中止` (hủy bỏ luôn) và `延長` (kéo dài thời lượng `長くする`).",
            "cute_wrong_msg": "Coi chừng lộn `延期` với `中止` (hủy bỏ luôn) hoặc `延長` (kéo dài thêm giờ)! Ở đây có 'sang tuần sau' (`来週に`) là dời lịch = `先へ延ばされた` nha! ⏳",
            "wrong_exps": [
                "`中止された` là hủy bỏ hoàn toàn chứ không có tuần sau nữa.",
                "Chính xác! `延期する` = `日程を先へ延ばす` (dời lịch sang sau).",
                "`長くされた` là `延長された` (tăng thêm thời lượng chương trình).",
                "`早められた` là đẩy lịch lên sớm hơn (`繰り上げる`)."
            ],
            "source_ref": {"novel": "isekai", "chapter": 7, "lesson_id": "p1_c09_b02", "label": "Bộ 3 Isekai Ch.07 (Bài 21: Thời gian)"}
        },
        {
            "num": 27,
            "mondai": "問題5：言い換え類義",
            "mondai_vi": "Từ / cụm từ đồng nghĩa",
            "prompt": "その件については、<u>いっそのこと</u>最初からやり直したほうがいいと思う。",
            "prompt_vi": "Về chuyện đó, tôi nghĩ thà cứ làm lại từ đầu luôn còn hơn là cố sửa chắp vá.",
            "options": ["思い切ってむしろ", "もし万が一", "ほとんど", "だんだん"],
            "ans": 1,
            "cute_right_msg": "Quá xịn!! Phó từ `いっそのこと` học trong Yandere Ch.10 có nghĩa là 'thà dứt khoát đánh bạo mà... còn hơn' đó! 🌟",
            "right_exp": "`いっそのこと` (cũng có dạng `いっそ`) dùng khi đưa ra quyết định táo bạo dứt khoát giữa lúc khó xử: 'thà cứ làm hẳn X cho rồi' ≈ **思い切ってむしろ**.",
            "cute_wrong_msg": "Ôn lại Bộ 2 Yandere Ch.10 (Phó từ hô ứng) nha em: `いっそのこと〜たほうがいい` mang nghĩa dứt khoát 'thà rằng... còn hơn'! 💌",
            "wrong_exps": [
                "Chính xác! `いっそのこと` = `思い切ってむしろ` (thà dứt khoát luôn...).",
                "`もし万が一` ứng với `万一（まんいち）` (nhỡ may vạn nhất).",
                "`ほとんど` là hầu hết / hầu như không.",
                "`だんだん` là dần dần từng chút."
            ],
            "source_ref": {"novel": "yandere", "chapter": 10, "lesson_id": "p2_c04_b02", "label": "Bộ 2 Yandere Ch.10 (Bài 29: Phó từ hô ứng)"}
        },
        # --- 問題6: 用法 (28-32) ---
        {
            "num": 28,
            "mondai": "問題6：用法",
            "mondai_vi": "Cách dùng từ đúng trong câu",
            "prompt": "次の言葉の使い方として最もよいものを、1・2・3・4から一つ選びなさい。\n【言葉：<b><u>うっかり</u></b>】",
            "prompt_vi": "Chọn câu sử dụng đúng nhất từ 【うっかり】 (lơ đễnh, sơ suất).",
            "options": [
                "電車の時刻を確認したのに、うっかり乗り遅れてしまった。",
                "毎日うっかり努力を続けたおかげで、N2に合格できた。",
                "この料理は、うっかりした味がしておいしいですね。",
                "雨がうっかり降り始めたので、傘をさした。"
            ],
            "ans": 1,
            "cute_right_msg": "Đỉnh cao Mondai 6! Em bắt gọn sắc thái 'sơ suất ngoài ý muốn' của `うっかり` chuẩn không cần chỉnh luôn! 🎯",
            "right_exp": "`うっかり` chỉ hành động sơ suất, lơ đễnh quên mất hoặc làm nhầm (`うっかり忘れる / 間違える / 乗り遅れる`) — luôn mang kết quả lỡ dở ngoài ý muốn.",
            "cute_wrong_msg": "Bí kíp Mondai 6: `うっかり` luôn gắn với lỗi *lơ đễnh quên/nhầm của con người*, KHÔNG dùng cho nỗ lực tốt, vị món ăn hay thời tiết nha em~ 🌸",
            "wrong_exps": [
                "Chính xác tuyệt đối! `うっかり乗り遅れてしまった` (vì lơ đễnh nên lỡ mất chuyến tàu).",
                "Nỗ lực chăm chỉ phải dùng `こつこつ`, không bao giờ dùng `うっかり` (sơ suất).",
                "Vị thanh nhạt nhẹ nhàng là `あっさりした味`, không phải `うっかり`.",
                "Thời tiết trời mưa không có ý thức để gọi là 'sơ suất' (`急に・ぽつぽつ` mới đúng)."
            ],
            "source_ref": {"novel": "isekai", "chapter": 8, "lesson_id": "p2_c05_b01", "label": "Bộ 3 Isekai Ch.08 (Bài 31: Onomatopoeia)"}
        },
        {
            "num": 29,
            "mondai": "問題6：用法",
            "mondai_vi": "Cách dùng từ đúng trong câu",
            "prompt": "次の言葉の使い方として最もよいものを、1・2・3・4から一つ選びなさい。\n【言葉：<b><u>見直す</u></b>】",
            "prompt_vi": "Chọn câu sử dụng đúng nhất từ 【見直す】 (xem lại kiểm tra lại / nhìn nhận đánh giá lại cao hơn).",
            "options": [
                "遠くて字がよく見直さないので、もっと前に座ろう。",
                "提出する前に、誤字や脱字がないかレポートを見直した。",
                "昨日見た映画を友達に見直して紹介した。",
                "窓の外を見直すと、きれいな虹が出ていた。"
            ],
            "ans": 2,
            "cute_right_msg": "Quá chuẩn! Kiểm tra lại bài trước khi nộp (`レポートを見直す`) là nghĩa thứ 2 siêu chuẩn của `見直す` luôn! 📝",
            "right_exp": "`見直（みなお）す` có 2 nghĩa chính: (1) xem xét kiểm tra lại bài/tài liệu để sửa sai (`レポートを見直す`); (2) thay đổi cái nhìn theo hướng khâm phục tốt đẹp hơn (`彼を見直した`).",
            "cute_wrong_msg": "Đừng nhầm `見直す` với `見る` (nhìn) hay `見える` (nhìn thấy) nha em! `見直す` luôn hàm ý 'kiểm tra rà soát lại' hoặc 'đánh giá khâm phục lại'! ✨",
            "wrong_exps": [
                "Ở xa chữ không nhìn thấy phải dùng `よく見えない`, không dùng `見直さない`.",
                "Chính xác! Kiểm tra lại lỗi chính tả trước khi nộp báo cáo (`見直す`).",
                "Giới thiệu phim cho bạn xem là `紹介する` hoặc `勧める`, không dùng `見直して`.",
                "Nhìn ra ngoài cửa sổ lần đầu thấy cầu vồng dùng `見ると`."
            ],
            "source_ref": {"novel": "isekai", "chapter": 9, "lesson_id": "p2_c07_b01", "label": "Bộ 3 Isekai Ch.09 (Bài 34: Từ ghép)"}
        },
        {
            "num": 30,
            "mondai": "問題6：用法",
            "mondai_vi": "Cách dùng từ đúng trong câu",
            "prompt": "次の言葉の使い方として最もよいものを、1・2・3・4から一つ選びなさい。\n【言葉：<b><u>枯渇</u></b>】",
            "prompt_vi": "Chọn câu sử dụng đúng nhất từ 【枯渇（こかつ）】 (cạn kiệt nguồn tài nguyên/nước/quỹ).",
            "options": [
                "雨が少なく、この地域のダムの水が枯渇する恐れがある。",
                "風邪をひいて声が出なくなり、喉がすっかり枯渇した。",
                "花瓶の水を換え忘れたので、花が枯渇してしまった。",
                "試験が終わって安心してしまい、毎日やる気が枯渇してよく寝ている。"
            ],
            "ans": 1,
            "cute_right_msg": "Chuẩn đét! `枯渇（こかつ）` dùng cho *nguồn* tài nguyên, nguồn nước hồ đập, khoáng sản hoặc ý tưởng — KHÔNG dùng cho bông hoa hay cổ họng khô đâu nhé! 💧",
            "right_exp": "`枯渇（こかつ）` chỉ sự **cạn kiệt nguồn cung** (nước sông/đập, dầu mỏ, tài nguyên thiên nhiên, ngân quỹ, ý tưởng sáng tạo). Hoa héo dùng `枯れる`, khát họng dùng `渇く`.",
            "cute_wrong_msg": "Hihi chú ý sắc thái của chữ Hán đôi `枯渇`: ghép lại thì dùng cho **nguồn tài nguyên/nước hồ đập/nhiên liệu**, chứ 1 bông hoa héo chỉ là `枯れる`, họng khô là `渇く` nha em! 🌱",
            "wrong_exps": [
                "Chính xác! Nguồn nước ở đập thủy điện có nguy cơ cạn kiệt (`水が枯渇する`).",
                "Họng khô rát dùng `喉が渇く・痛む`, không dùng `枯渇`.",
                "Hoa trong bình héo úa dùng động từ `枯れる` (`花が枯れた`).",
                "Mất động lực sau thi dùng `やる気がなくなる・抜ける`, không dùng `枯渇` (có thể dùng `才能・アイデアが枯渇する` chứ không phải trạng thái nghỉ ngơi sau thi)."
            ],
            "source_ref": {"novel": "isekai", "chapter": 4, "lesson_id": "p1_c08_b01", "label": "Bộ 3 Isekai Ch.04 (Bài 18: Sinh thái)"}
        },
        {
            "num": 31,
            "mondai": "問題6：用法",
            "mondai_vi": "Cách dùng từ đúng trong câu",
            "prompt": "次の言葉の使い方として最もよいものを、1・2・3・4から一つ選びなさい。\n【言葉：<b><u>めったに</u></b>】",
            "prompt_vi": "Chọn câu sử dụng đúng nhất từ 【めったに】 (hiếm khi, hầu như không — hô ứng phủ định).",
            "options": [
                "彼はめったに遅刻するので、よく上司に叱られている。",
                "この地方では雪がとてもめったに降って、毎日スキーができる。",
                "この店は予約が取れず、めったに入ることができない。",
                "母は料理が得意で、めったにおいしいカレーを作ってくれる。"
            ],
            "ans": 3,
            "cute_right_msg": "Bắt bài Phó từ hô ứng chuẩn 10/10!! Thấy `めったに` là tìm ngay đuôi phủ định `〜ない` (`できない`) luôn! 🔥",
            "right_exp": "`めったに` là **phó từ hô ứng phủ định**, BẮT BUỘC phía sau phải đi kèm thể phủ định `〜ない` (`めったに入ることができない` = hiếm khi có thể vào được).",
            "cute_wrong_msg": "Nhớ bí kíp Bộ 2 Yandere Ch.10 (Phó từ hô ứng) nè em: `めったに` là bạn thân vĩnh viễn của **〜ない**! Bỏ qua 3 câu khẳng định ở kia liền luôn ha~ 💖",
            "wrong_exps": [
                "Thường xuyên đi muộn phải là `よく・たびたび遅刻する`. `めったに` không đi với khẳng định `する`.",
                "Tuyết rơi nhiều mỗi ngày trượt tuyết trái hoàn toàn với 'hiếm khi' (`〜ない`).",
                "Chính xác tuyệt đối! Có đuôi phủ định `〜ことができない` khớp với `めったに`.",
                "Mẹ hay nấu ăn ngon dùng `よく・しょっちゅう`, `めったに` không dùng cho câu khẳng định."
            ],
            "source_ref": {"novel": "yandere", "chapter": 10, "lesson_id": "p2_c04_b02", "label": "Bộ 2 Yandere Ch.10 (Bài 29: Phó từ hô ứng)"}
        },
        {
            "num": 32,
            "mondai": "問題6：用法",
            "mondai_vi": "Cách dùng từ đúng trong câu",
            "prompt": "次の言葉の使い方として最もよいものを、1・2・3・4から一つ選びなさい。\n【言葉：<b><u>採算</u></b>】",
            "prompt_vi": "Chọn câu sử dụng đúng nhất từ 【採算（さいさん）】 (tính toán lời lỗ trong kinh doanh).",
            "options": [
                "テストの採算をして、自分の点数を確かめた。",
                "こんなに安い値段で売ったら、材料費も出ず採算が合わない。",
                "山の高さを採算するために、新しい機械を使った。",
                "友達と旅行の採算を立てて、ホテルを予約した。"
            ],
            "ans": 2,
            "cute_right_msg": "Quá siêu!! `採算（さいさん）が合う / 合わない` (có bù vốn sinh lời hay bị lỗ) — em nhớ chắc từ bài Kinh tế Isekai Ch.02 quá! 🪙",
            "right_exp": "`採算（さいさん）` chuyên dùng trong kinh doanh tài chính để nói về tính hiệu quả lời-lỗ (`採算が合う / 合わない / 採算が取れる`).",
            "cute_wrong_msg": "Đừng nhầm chữ `算` (tính) với chấm điểm bài thi (`採点`) hay tính toán bình thường (`計算`) nha em! `採算` chỉ dùng cho **lời - lỗ kinh doanh** (`採算が合わない`)! 💼",
            "wrong_exps": [
                "Chấm điểm bài kiểm tra dùng `採点（さいてん）`, không phải `採算`.",
                "Chính xác! Bán rẻ quá không đủ tiền nguyên liệu nên bị lỗ vốn (`採算が合わない`).",
                "Đo đạc độ cao dùng `測定（そくてい）` hoặc `計算`.",
                "Lập kế hoạch du lịch dùng `計画を立てる` hoặc `予算を計算する`."
            ],
            "source_ref": {"novel": "isekai", "chapter": 2, "lesson_id": "p1_c07_b03", "label": "Bộ 3 Isekai Ch.02 (Bài 16: Kinh tế)"}
        },
        # --- 問題7: 文の文法1 (33-44) ---
        {
            "num": 33,
            "mondai": "問題7：文の文法1",
            "mondai_vi": "Ngữ pháp câu N2",
            "prompt": "いくら頼まれても、会社の秘密に関わること（　　）、誰にも話すわけにはいかない。",
            "prompt_vi": "Dù có bị nài nỉ bao nhiêu đi nữa, nhưng một khi đã liên quan đến bí mật công ty thì tôi tuyệt đối không thể nói cho ai biết được.",
            "options": ["とあっては", "とはいうものの", "とみえて", "といっても"],
            "ans": 1,
            "cute_right_msg": "Tuyệt vời! `〜とあっては` (một khi đã là chuyện X trọng đại như vậy thì...) khớp ngữ cảnh nghiêm túc này luôn! ✨",
            "right_exp": "`N とあっては` (Một khi đã là tình huống đặc biệt/nghiêm trọng là N thì đương nhiên vế sau phải xử lý tương xứng, thường đi với điều không thể làm hoặc phải làm).",
            "cute_wrong_msg": "Coi kỹ vế trước 'vì đây là chuyện liên quan bí mật công ty nên...': cấu trúc trang trọng nhấn mạnh tình huống đặc biệt này là `〜とあっては` nha em~ ⚖️",
            "wrong_exps": [
                "Chính xác! `秘密に関わることとあっては` = một khi đã liên quan tới bí mật thì...",
                "`とはいうものの` = tuy nói vậy nhưng... (nhượng bộ nghịch tiếp, không hợp).",
                "`とみえて` = có vẻ như là (suy đoán nguyên nhân từ quan sát).",
                "`といっても` = dù nói là... nhưng thực chất không đến mức đó."
            ],
            "source_ref": {"novel": "yandere", "chapter": 3, "lesson_id": "p1_c06_b02", "label": "Ngữ pháp N2 — 条件（〜とあっては）"}
        },
        {
            "num": 34,
            "mondai": "問題7：文の文法1",
            "mondai_vi": "Ngữ pháp câu N2",
            "prompt": "この美術館の建物は、外観（　　）、内装も有名デザイナーによって手がけられたものだ。",
            "prompt_vi": "Tòa nhà bảo tàng mỹ thuật này, không chỉ vẻ ngoài mà ngay cả nội thất bên trong cũng đều do nhà thiết kế lừng danh thực hiện.",
            "options": ["にあたり", "はもちろんのこと", "ばかりに", "はおろか"],
            "ans": 2,
            "cute_right_msg": "Chuẩn không cần chỉnh! `A はもちろんのこと、B も` = A là đương nhiên rồi, ngay cả B cũng...! 🎨",
            "right_exp": "`A はもちろんのこと B も`: Không chỉ A (đương nhiên rồi), mà cả B cũng... (dùng cho 2 danh từ song hành tích cực).",
            "cute_wrong_msg": "Ở đây là liệt kê song song hai nét đẹp: ngoại thất đương nhiên rồi, nội thất cũng tuyệt → chọn `はもちろんのこと` nha! (Nhớ `はおろか` chỉ đi với phủ định!) 🌸",
            "wrong_exps": [
                "`〜にあたり` = nhân dịp làm việc quan trọng (`開会にあたり`).",
                "Chính xác! `外観はもちろんのこと、内装も`.",
                "`〜ばかりに` = chỉ tại vì lỡ làm X nên kết quả xấu thảm hại.",
                "`A はおろか B も（ない）` luôn mang nghĩa phủ định tiêu cực ('A còn không được huống chi B')."
            ],
            "source_ref": {"novel": "romcom", "chapter": 7, "lesson_id": "p1_c05_b01", "label": "Ngữ pháp N2 — 付加（〜はもちろんのこと）"}
        },
        {
            "num": 35,
            "mondai": "問題7：文の文法1",
            "mondai_vi": "Ngữ pháp câu N2",
            "prompt": "弟は漫画を読み（　　）、机の上でそのまま眠ってしまった。",
            "prompt_vi": "Em trai tôi đang đọc dở truyện tranh thì cứ thế gục xuống bàn ngủ thiếp đi mất.",
            "options": ["かけたまま", "きりに", "っこなく", "ぬいて"],
            "ans": 1,
            "cute_right_msg": "Đỉnh luôn! Kết hợp siêu tự nhiên `V(ます)かけ（の）＋まま` = đang làm dở dang giữa chừng thì cứ để nguyên trạng thế mà...! 📖😴",
            "right_exp": "`V(ます) + かける` nghĩa là *đang làm dở dang giữa chừng* (`読みかけ・食べかけ`). `読みかけたまま` = đang đọc dở thì cứ thế ngủ gục luôn.",
            "cute_wrong_msg": "Nhìn nghĩa 'vừa mới đọc dở trang sách thì lăn ra ngủ nguyên thế trên bàn': `V(ます)＋かける` là làm dở dang giữa chừng đó em~ 🌸",
            "wrong_exps": [
                "Chính xác! `読みかけたまま` (đang đọc dở dang rồi cứ thế mà...).",
                "`〜きり` phải đi sau **V-た** (`座ったきり`), không đi sau V(ます).",
                "`〜っこない` là 'làm sao mà có chuyện...' (ngôi dự đoán dứt khoát).",
                "`〜ぬく` là làm tới tận cùng hoàn tất (`読み抜く`), trái nghĩa với việc gục ngủ giữa chừng."
            ],
            "source_ref": {"novel": "romcom", "chapter": 4, "lesson_id": "p1_c02_b02", "label": "Ngữ pháp N2 — 途中（〜かける）"}
        },
        {
            "num": 36,
            "mondai": "問題7：文の文法1",
            "mondai_vi": "Ngữ pháp câu N2",
            "prompt": "あのレストランはいつも予約でいっぱいだ。料理の味（　　）、サービスも最高らしい。",
            "prompt_vi": "Nhà hàng kia lúc nào cũng kín chỗ đặt trước. Không chỉ hương vị món ăn mà ngay cả dịch vụ cũng nghe nói tuyệt vời lắm.",
            "options": ["をはじめ", "はおろか", "もさることながら", "をものともせず"],
            "ans": 3,
            "cute_right_msg": "Ôi siêu đỉnh!! Mẫu ngữ pháp N2 sang xịn mịn `A もさることながら B も` = A đã tuyệt rồi nhưng B lại càng ấn tượng hơn! 🍽️✨",
            "right_exp": "`N1 もさることながら N2 も`: Không chỉ N1 (khỏi phải bàn cãi), mà N2 cũng cực kỳ đáng chú ý/tuyệt vời không kém.",
            "cute_wrong_msg": "Gợi ý nhẹ nhàng nè em: `〜もさることながら` là mẫu N2 hay thi để khen cả hai mặt 'Món ăn đã ngon xuất sắc rồi, mà phục vụ cũng đỉnh luôn'! 💖",
            "wrong_exps": [
                "`〜をはじめ` dùng để đưa ví dụ tiêu biểu trong một tập hợp (`東京をはじめ、各地で...`).",
                "`はおろか` chỉ dùng trong câu phủ định ('chẳng nói gì đến A, ngay cả B cũng không').",
                "Chính xác tuyệt đối! `料理の味もさることながら、サービスも`.",
                "`をものともせず` nghĩa là bất chấp gian khổ nguy hiểm (`嵐をものともせず`)."
            ],
            "source_ref": {"novel": "romcom", "chapter": 3, "lesson_id": "p1_c02_b01", "label": "Ngữ pháp N2 — 〜もさることながら"}
        },
        {
            "num": 37,
            "mondai": "問題7：文の文法1",
            "mondai_vi": "Ngữ pháp câu N2",
            "prompt": "雨が降ってきたのを見て、今日は客が来ないだろうと思い込んでいた（　　）、次々と店に入ってきた。",
            "prompt_vi": "Thấy trời đổ mưa nên cứ đinh ninh hôm nay sẽ chẳng có khách nào đến đâu, ấy vậy mà trái với dự đoán khách cứ nối đuôi nhau bước vào quán.",
            "options": ["わけがなく", "どころか", "ものだから", "につれて"],
            "ans": 2,
            "cute_right_msg": "Quá chuẩn!! Cấu trúc tương phản mạnh `思い込んでいたどころか` (đừng nói là vắng, trái lại còn kéo vào nườm nượp)! ☕✨",
            "right_exp": "`〜どころか`: Đừng nói là X, thực tế còn ngược lại hẳn / thậm chí hơn gấp bội ở vế sau.",
            "cute_wrong_msg": "Nhìn độ tương phản 180 độ nha em: nghĩ sẽ *chẳng ai đến* ↔ thực tế lại *nối đuôi nhau vào quán* → dùng `どころか` (đâu có chuyện đó, trái lại...) nè! 🌈",
            "wrong_exps": [
                "`わけがない` dùng ở cuối câu mang nghĩa khẳng định phủ nhận ('không đời nào có chuyện').",
                "Chính xác! `来ないと思っていたどころか` = tưởng không ai đến đâu, nào ngờ trái lại...",
                "`ものだから` giải thích lý do bào chữa ('vì lỡ...'), không nối được 2 vế trái ngược nhau.",
                "`につれて` nghĩa là 'càng X thì càng thay đổi Y theo'."
            ],
            "source_ref": {"novel": "romcom", "chapter": 3, "lesson_id": "p1_c02_b01", "label": "Ngữ pháp N2 — 対比（〜どころか）"}
        },
        {
            "num": 38,
            "mondai": "問題7：文の文法1",
            "mondai_vi": "Ngữ pháp câu N2",
            "prompt": "彼女のことだから、今ごろ図書館の片隅で試験勉強に集中している（　　）。",
            "prompt_vi": "Với tính cách của cô ấy thì chắc hẳn tầm này đang ngồi góc thư viện tập trung ôn thi lắm rồi.",
            "options": ["にすぎない", "にほかならない", "に違いない", "とは限らない"],
            "ans": 3,
            "cute_right_msg": "Cặp bài trùng kinh điển `〜のことだから〜に違いない`!! Bắt sóng chuẩn xác 100% luôn! 📚💕",
            "right_exp": "`N のことだから` (Vì là tính cách vốn có của N) gần như luôn hô ứng với `〜だろう・〜はずだ・〜に違いない` (chắc chắn hẳn là đang...).",
            "cute_wrong_msg": "Mẹo ăn điểm nhanh của chị Yuki: hễ thấy đầu câu có `〜のことだから` (vì hiểu rõ tính người đó nên...) thì 90% cuối câu là **に違いない** / **はずだ** nha em! 🌸",
            "wrong_exps": [
                "`にすぎない` = chỉ là... mà thôi (mang ý đánh giá thấp).",
                "`にほかならない` = không gì khác chính là (chỉ nguyên nhân/bản chất tất yếu, không đi với dự đoán thời điểm hiện tại `今ごろ〜している`).",
                "Tuyệt vời! `彼女のことだから〜に違いない`.",
                "`とは限らない` = chưa chắc đã luôn như vậy."
            ],
            "source_ref": {"novel": "romcom", "chapter": 8, "lesson_id": "p1_c05_b02", "label": "Ngữ pháp N2 — 推量（〜のことだから〜に違いない）"}
        },
        {
            "num": 39,
            "mondai": "問題7：文の文法1",
            "mondai_vi": "Ngữ pháp câu N2",
            "prompt": "こんな夜遅くに一人で暗い夜道を歩くなんて、危ない（　　）。",
            "prompt_vi": "Đi bộ một mình trên con đường tối khuya khoắt như thế này thật là quá sức nguy hiểm đi mà!",
            "options": ["ことか", "ことだ", "極まりない", "べきだ"],
            "ans": 3,
            "cute_right_msg": "Đỉnh cao! `A-な + 極まりない` (vô cùng tận, cực kỳ!) gắn với từ cảm xúc/đánh giá như `危ない・失礼・残念` quá đỉnh luôn! ⚠️",
            "right_exp": "`Aい / Aな(bỏ な) + 極まりない` (cũng có dạng `この上ない`): vô cùng, hết sức, tột độ (nhấn mạnh mức độ cực điểm, hay dùng văn viết/nhận xét mạnh).",
            "cute_wrong_msg": "Câu này cảm thán ở mức tột cùng mà KHÔNG có từ để hỏi như `どんなに・どれほど` ở trước nên `ことか` bị loại nha em! Dùng `極まりない` (tột độ)! 💡",
            "wrong_exps": [
                "`ことか` đòi hỏi phía trước phải có từ nghi vấn như `どんなに / どれほど / 何回`. (Và phải dùng `Aい + ことか`).",
                "`〜ことだ` dùng để khuyên bảo ('nên làm gì', đi với `Vる/Vないことだ`).",
                "Chính xác tuyệt đối! `危ない極まりない` = hết sức nguy hiểm, nguy hiểm tột độ.",
                "`べきだ` đi với động từ mang nghĩa 'nên làm'."
            ],
            "source_ref": {"novel": "yandere", "chapter": 4, "lesson_id": "p1_c07_b02", "label": "Ngữ pháp N2 — 程度（〜極まりない）"}
        },
        {
            "num": 40,
            "mondai": "問題7：文の文法1",
            "mondai_vi": "Ngữ pháp câu N2",
            "prompt": "インターネットは便利である（　　）、個人情報が漏れる危険性も常に抱えている。",
            "prompt_vi": "Internet tuy rất tiện lợi, nhưng mặt khác cũng luôn tiềm ẩn nguy cơ rò rỉ thông tin cá nhân.",
            "options": ["かと思えば", "半面", "ものか", "ことから"],
            "ans": 2,
            "cute_right_msg": "Chuẩn luôn! `便利な半面（はんめん）` = một mặt tiện lợi, mặt trái/mặt khác lại tiềm ẩn rủi ro! 🌐⚖️",
            "right_exp": "`A + 半面（はんめん）` (tiếp nối `Vる・Aい・Aな・Nの + 半面`): Mặt này thì... nhưng mặt trái/mặt khác lại... (dùng cực nhiều trong văn nghị luận so sánh 2 mặt ưu-nhược điểm).",
            "cute_wrong_msg": "Nhìn cấu trúc hai mặt ưu - nhược điểm đối lập của cùng 1 sự vật (`tiện lợi` ↔ `nguy cơ rò rỉ`): mẫu chuẩn chỉ 2 mặt là `半面` nha em! 🌸",
            "wrong_exps": [
                "`かと思えば` = mới vừa thấy thế này thoắt cái đã thấy chuyện ngược lại ở người/việc khác.",
                "Chính xác! `〜反面・半面` = một mặt thì... mặt khác lại...",
                "`ものか` dùng cuối câu biểu thị phủ định mạnh mẽ ('đời nào có chuyện!').",
                "`ことから` = xuất phát từ lý do/dấu hiệu đó nên..."
            ],
            "source_ref": {"novel": "yandere", "chapter": 3, "lesson_id": "p1_c06_b02", "label": "Ngữ pháp N2 — 対比（〜半面）"}
        },
        {
            "num": 41,
            "mondai": "問題7：文の文法1",
            "mondai_vi": "Ngữ pháp câu N2",
            "prompt": "一度しかない人生なのだから、失敗を恐れずに自分のやりたいことに挑戦して（　　）。",
            "prompt_vi": "Vì là cuộc đời chỉ có một lần duy nhất, nên đừng sợ thất bại mà hãy thử thách với điều mình muốn làm thử xem sao.",
            "options": ["みようではないか", "みるわけにはいかない", "みるおそれがある", "みないものか"],
            "ans": 1,
            "cute_right_msg": "Khí thế hừng hực luôn!! `〜ようではないか` = nào chúng ta hãy cùng nhau thử... đi chứ! 🔥✨",
            "right_exp": "`Vようではないか` (dạng văn nói lịch sự/hô hào: `〜じゃないか`): Lời rủ rê, cổ vũ hào hùng 'Nào, chẳng phải chúng ta nên cùng... hay sao / hãy cùng nhau... đi nào!'",
            "cute_wrong_msg": "Đọc giọng văn cổ vũ tích cực đầu câu 'Đời chỉ có một lần nên...': chọn câu kêu gọi hào hứng `〜てみようではないか` nha em~ 🌸",
            "wrong_exps": [
                "Chính xác! `挑戦してみようではないか` = hãy cùng thử thách bản thân xem sao nào!",
                "`〜わけにはいかない` = không thể làm thế được (nghĩa cấm/ngại ngược nghĩa hoàn toàn).",
                "`〜おそれがある` = có nguy cơ xảy ra chuyện xấu (chỉ dùng cho thiên tai, tai nạn, thua lỗ).",
                "`〜ないものか` = ước ao giá mà có thể... (`どうにか合格できないものか`), không hợp vế khuyên 'Đời chỉ có 1 lần...'."
            ],
            "source_ref": {"novel": "isekai", "chapter": 9, "lesson_id": "p2_c07_b01", "label": "Ngữ pháp N2 — 呼びかけ（〜ようではないか）"}
        },
        {
            "num": 42,
            "mondai": "問題7：文の文法1",
            "mondai_vi": "Ngữ pháp câu N2",
            "prompt": "社長が今お戻りになりましたので、会議を始め（　　）。",
            "prompt_vi": "Vì Giám đốc vừa mới quay lại rồi, nên tôi xin phép được bắt đầu cuộc họp ngay ạ.",
            "options": ["させていただきます", "てくださいます", "になります", "ていただきます"],
            "ans": 1,
            "cute_right_msg": "Khiêm nhường ngữ chuẩn công sở Nhật Bản `V(sai khiến て) + いただきます`! Điểm Keigo 10/10! 🙇‍♀️✨",
            "right_exp": "`V(させて) + いただきます`: Xin phép được làm hành động V (khiêm nhường ngữ trang trọng của bản thân khi được sự đồng ý/trong hoàn cảnh có cấp trên/khách hàng).",
            "cute_wrong_msg": "Nhớ cấu trúc Kính ngữ công sở nhé: NGƯỜI NÓI xin phép thực hiện (`会議を始める`) bằng dạng **sai khiến + いただきます** = `始めさせていただきます`! (Còn `てくださいます` là sếp làm cho mình) 💼",
            "wrong_exps": [
                "Chính xác! `始めさせていただきます` = Tôi xin phép được bắt đầu.",
                "`てくださいます` = Ngài (Giám đốc) làm cho tôi (sai chủ thể hành động).",
                "`お＋Vます＋になります` là Tôn kính ngữ dành cho người trên làm, không dùng cho chính mình.",
                "`ていただきます` là mình nhờ người khác làm hộ (`見ていただきます`), không phải mình tự xin phép bắt đầu."
            ],
            "source_ref": {"novel": "romcom", "chapter": 8, "lesson_id": "p1_c05_b02", "label": "Ngữ pháp N2 — 敬語（〜させていただきます）"}
        },
        {
            "num": 43,
            "mondai": "問題7：文の文法1",
            "mondai_vi": "Ngữ pháp câu N2",
            "prompt": "彼はとても明るい性格で、初対面の人（　　）すぐに仲良くなってしまう。",
            "prompt_vi": "Anh ấy có tính cách rất cởi mở, bất kể ngay cả với người lần đầu gặp mặt cũng nhanh chóng trở nên thân thiết.",
            "options": ["とばかりに", "はもとより", "とあっても", "であろうと"],
            "ans": 4,
            "cute_right_msg": "Quá chuẩn!! `N であろうと（〜であっても）` = dù cho là người mới gặp lần đầu đi chăng nữa thì vẫn...! 🌟",
            "right_exp": "`N + であろうと（も）` = Cho dù là N đi chăng nữa (tương tự `N でも / N であっても`, văn viết hay dùng để nhấn mạnh phạm vi rộng không ngoại lệ).",
            "cute_wrong_msg": "Tìm từ mang nghĩa 'cho dù ngay cả với... đi chăng nữa cũng thân ngay' nha em: `N + であろうと` chính là dạng văn phong N2 của `でも` đó! 🌸",
            "wrong_exps": [
                "`〜とばかりに` = như thể muốn nói rằng... (diễn tả thái độ biểu cảm không lời).",
                "`〜はもとより` = điều X là dĩ nhiên rồi (`A はもとより B も`), không nối thẳng với câu đơn 1 vế `〜とすぐに` kiểu này.",
                "`とあっても` hiếm và không hợp bằng `であろうと`.",
                "Chính xác! `初対面の人であろうとすぐに仲良くなる`."
            ],
            "source_ref": {"novel": "romcom", "chapter": 1, "lesson_id": "p1_c01_b01", "label": "Ngữ pháp N2 — 逆接・譲歩（〜であろうと）"}
        },
        {
            "num": 44,
            "mondai": "問題7：文の文法1",
            "mondai_vi": "Ngữ pháp câu N2",
            "prompt": "せっかく苦労して資料を集めた（　　）、誰にも読まれないのでは意味がない。",
            "prompt_vi": "Cất công vất vả thu thập tài liệu đến thế rồi mà chẳng ai thèm đọc cho thì còn ý nghĩa gì nữa.",
            "options": ["にしては", "ものを", "だけに", "といっても"],
            "ans": 2,
            "cute_right_msg": "Ngọt xớt! Dùng `Vた + ものを` (dù đã vất vả thế mà lại... — nỗi tiếc nuối!) siêu tinh tế! 📄💔",
            "right_exp": "`〜ものを` (tiếp nối `Vる/Vた・Aい・Aな・Nの + ものを`): Rõ ràng đã tốn công thế rồi mà lại chẳng thành/chẳng được như ý — diễn tả sự tiếc nuối, trách nhẹ.",
            "cute_wrong_msg": "Nhìn sắc thái tiếc nuối hụt hẫng (`せっかく〜したものを`, giống `〜のに` nhưng mang hàm ý tiếc rẻ trách móc) nha em! 🌸",
            "wrong_exps": [
                "`にしては` đi với sự so sánh bất ngờ so với tiêu chuẩn (`外国人にしては漢字が上手だ`).",
                "Chính xác! `せっかく〜したものを` = đã cất công làm thế rồi mà lại (tiếc nuối)...",
                "`だけに` = chính vì X nên càng Y tương xứng.",
                "`といっても` = dù nói là... nhưng thực chất không bằng."
            ],
            "source_ref": {"novel": "romcom", "chapter": 8, "lesson_id": "p1_c05_b02", "label": "Ngữ pháp N2 — 残念・逆接（〜ものを）"}
        },
        # --- 問題8: 文の文法2 ★ (45-49) ---
        {
            "num": 45,
            "mondai": "問題8：文の文法2 ★",
            "mondai_vi": "Sắp xếp thành phần câu",
            "prompt": "妹は、昨日 ＿＿＿ ＿＿＿ ★ ＿＿＿ もう読まなくなってしまった。",
            "prompt_vi": "Em gái tôi, dù mới hôm qua vừa mua cuốn sách đắt tiền mà nó từng khao khát đến thế, vậy mà giờ đã không thèm đọc nữa rồi.",
            "options": ["にもかかわらず", "高い本を", "買ったばかり", "あれほど欲しがっていた"],
            "ans": 3,
            "cute_right_msg": "Tuyệt đỉnh sắp xếp!! Thứ tự chuẩn: `[4] あれほど欲しがっていた → [2] 高い本を → ★[3] 買ったばかり → [1] にもかかわらず`! 🧩✨",
            "right_exp": "Ghép chuẩn xác: `妹は、昨日 [4]あれほど欲しがっていた [2]高い本を ★[3]買ったばかり [1]にもかかわらず もう読まなくなってしまった。`\n- `[4]あれほど欲しがっていた` bổ nghĩa cho danh từ `[2]高い本を`.\n- `[2]高い本を` là tân ngữ của `[3]買ったばかり`.\n- `買ったばかり` kết hợp với `[1]にもかかわらず` (dù mới vừa mua thế nhưng...).\n→ Vị trí dấu ★ là lựa chọn **3 (`買ったばかり`)**!",
            "cute_wrong_msg": "Bí kíp làm bài dấu ★ của chị Yuki nè: ghép cặp chắc chắn trước! `[4] muốn đến thế` đứng trước `[2] cuốn sách đắt`; còn `〜ばかり` gắn chặt trước `[1] にもかかわらず` ở vị trí cuối → ra ngay thứ tự `[4]-[2]-★[3]-[1]`! 🌟",
            "wrong_exps": [
                "`[1] にもかかわらず` phải đứng ở ô số 4 để nối nghịch tiếp sang vế `もう読まなくなってしまった`.",
                "`[2] 高い本を` đứng ở ô số 2 (ngay sau mệnh đề định ngữ `[4] あれほど欲しがっていた`).",
                "Chính xác tuyệt đối! Vị trí ★ là `[3] 買ったばかり` (`4 → 2 → 3 → 1`).",
                "`[4] あれほど欲しがっていた` đứng ngay ô số 1 để bổ nghĩa cho `高い本`."
            ],
            "source_ref": {"novel": "romcom", "chapter": 7, "lesson_id": "p1_c05_b01", "label": "Ngữ pháp N2 ★ — 〜にもかかわらず"}
        },
        {
            "num": 46,
            "mondai": "問題8：文の文法2 ★",
            "mondai_vi": "Sắp xếp thành phần câu",
            "prompt": "天気予報によると、今回の台風は ＿＿＿ ＿＿＿ ★ ＿＿＿ という話だ。",
            "prompt_vi": "Theo dự báo thời tiết, nghe nói cơn bão lần này có nguy cơ giữ nguyên sức mạnh cấp kỷ lục lịch sử mà đổ bộ vào đất liền.",
            "options": ["おそれがある", "過去最大級の", "上陸する", "勢力を保ったまま"],
            "ans": 3,
            "cute_right_msg": "Quá siêu!! Thứ tự khóa chặt từng mắt xích: `[2] 過去最大級の → [4] 勢力を保ったまま → ★[3] 上陸する → [1] おそれがある`! 🌀",
            "right_exp": "Ghép chuẩn xác: `今回の台風は [2]過去最大級の [4]勢力を保ったまま ★[3]上陸する [1]おそれがある という話だ。`\n- `[2]過去最大級の` (của cấp lớn nhất quá khứ) chỉ có thể đứng trước danh từ `[4]勢力` (`勢力を保ったまま`).\n- Hành động tiếp theo là `[3]上陸する` (đổ bộ).\n- `Vる + [1]おそれがある` (có nguy cơ xảy ra điều xấu).\n→ Vị trí ★ là **3 (`上陸する`)**!",
            "cute_wrong_msg": "Tìm manh mối từ `の` và kết câu `という話だ` nha em! `[2] 過去最大級の` chắc chắn bổ nghĩa cho danh từ `[4] 勢力を...`, còn `[1] おそれがある` luôn chốt cuối trước `という話だ`! 💡",
            "wrong_exps": [
                "`[1] おそれがある` đứng ở ô số 4 (Vる＋おそれがある).",
                "`[2] 過去最大級の` đứng ở ô số 1 (trước danh từ `勢力`).",
                "Chính xác! Vị trí ★ là `[3] 上陸する` (`2 → 4 → 3 → 1`).",
                "`[4] 勢力を保ったまま` đứng ở ô số 2."
            ],
            "source_ref": {"novel": "isekai", "chapter": 7, "lesson_id": "p1_c09_b02", "label": "Ngữ pháp N2 ★ — 〜おそれがある"}
        },
        {
            "num": 47,
            "mondai": "問題8：文の文法2 ★",
            "mondai_vi": "Sắp xếp thành phần câu",
            "prompt": "料理が苦手だった彼が、 ＿＿＿ ＿＿＿ ★ ＿＿＿ おいしい料理を作れるようになった。",
            "prompt_vi": "Anh chàng vốn vụng nấu ăn ấy, trong quá trình luyện tập từng chút một mỗi ngày, đã trở nên nấu được những món ngon đến mức nhường này.",
            "options": ["うちに", "練習する", "こんなにも", "毎日少しずつ"],
            "ans": 1,
            "cute_right_msg": "Đẹp như tranh!! `[4] 毎日少しずつ → [2] 練習する → ★[1] うちに → [3] こんなにも`! Đúng chất Kenji trong Bộ 1 Romcom luôn~ 🍳✨",
            "right_exp": "Ghép chuẩn xác: `[4]毎日少しずつ [2]練習する ★[1]うちに [3]こんなにも おいしい料理を作れるようになった。`\n- `[4]毎日少しずつ` bổ nghĩa cho động từ `[2]練習する`.\n- `練習する` nối với `[1]うちに` (trong lúc kiên trì làm mãi thì có sự biến đổi tốt hơn).\n- `[3]こんなにも` bổ nghĩa cho tính từ `おいしい` ngay sau ô số 4.\n→ Vị trí ★ là **1 (`うちに`)**!",
            "cute_wrong_msg": "Chú ý từ ngay sau dấu gạch cuối cùng là tính từ `おいしい料理` nhé! Phó từ mức độ `[3] こんなにも` phải đứng ở ô số 4 ngay trước nó, còn `[4] 毎日少しずつ + [2] 練習する + [1] うちに` đi thành một cụm liền tù tì! 🌸",
            "wrong_exps": [
                "Chính xác tuyệt đối! Vị trí ★ là `[1] うちに` (`4 → 2 → 1 → 3`).",
                "`[2] 練習する` đứng ở ô số 2 (sau `毎日少しずつ`).",
                "`[3] こんなにも` đứng ở ô số 4 để bổ nghĩa trực tiếp cho `おいしい`.",
                "`[4] 毎日少しずつ` đứng ở ô số 1."
            ],
            "source_ref": {"novel": "romcom", "chapter": 3, "lesson_id": "p1_c02_b01", "label": "Ngữ pháp N2 ★ — 〜うちに"}
        },
        {
            "num": 48,
            "mondai": "問題8：文の文法2 ★",
            "mondai_vi": "Sắp xếp thành phần câu",
            "prompt": "どんなに親しい間柄でも、 ＿＿＿ ＿＿＿ ★ ＿＿＿ 関係は壊れてしまう。",
            "prompt_vi": "Dẫu có là mối quan hệ thân thiết đến đâu đi nữa, nếu lỡ quên mất phép lịch sự tối thiểu cần giữ thì tình cảm cũng sẽ đổ vỡ thôi.",
            "options": ["守るべき", "忘れて", "礼儀を", "しまっては"],
            "ans": 2,
            "cute_right_msg": "Chuẩn 100 điểm luôn!! `[1] 守るべき → [3] 礼儀を → ★[2] 忘れて → [4] しまっては`! 💖",
            "right_exp": "Ghép chuẩn xác: `[1]守るべき [3]礼儀を ★[2]忘れて [4]しまっては 関係は壊れてしまう。`\n- `[1]守るべき` (cần phải giữ) bổ nghĩa cho danh từ `[3]礼儀を`.\n- `[3]礼儀を` là tân ngữ của `[2]忘れて`.\n- `[2]忘れて` nối với `[4]しまっては` (`〜てしまっては`: nếu lỡ để xảy ra điều xấu thì...).\n→ Vị trí ★ là **2 (`忘れて`)**!",
            "cute_wrong_msg": "Bắt cặp cực nhanh nè em: `[1] 守るべき` (nên giữ) đi với danh từ `[3] 礼儀を` (phép lịch sự), còn `[2] 忘れて` gắn liền `[4] しまっては`! 🧩",
            "wrong_exps": [
                "`[1] 守るべき` đứng ở ô số 1 (trước danh từ `礼儀`).",
                "Chính xác tuyệt đối! Vị trí ★ là `[2] 忘れて` (`1 → 3 → 2 → 4`).",
                "`[3] 礼儀を` đứng ở ô số 2.",
                "`[4] しまっては` đứng ở ô số 4 (sau `忘れて`)."
            ],
            "source_ref": {"novel": "yandere", "chapter": 1, "lesson_id": "p1_c01_b03", "label": "Ngữ pháp N2 ★ — 〜べき・〜てしまっては"}
        },
        {
            "num": 49,
            "mondai": "問題8：文の文法2 ★",
            "mondai_vi": "Sắp xếp thành phần câu",
            "prompt": "今回のイベントが無事に成功したのは、 ＿＿＿ ＿＿＿ ★ ＿＿＿ にほかならない。",
            "prompt_vi": "Lần sự kiện này thành công tốt đẹp được như vậy, chẳng qua chính là nhờ sự chung tay góp sức của bà con địa phương đó thôi.",
            "options": ["協力して", "くれた", "地域の人々が", "おかげ"],
            "ans": 2,
            "cute_right_msg": "Ngọt như mía lùi!! `[3] 地域の人々が → [1] 協力して → ★[2] くれた → [4] おかげ`! Chốt đẹp `〜にほかならない`! 🏆",
            "right_exp": "Ghép chuẩn xác: `[3]地域の人々が [1]協力して ★[2]くれた [4]おかげ にほかならない。`\n- `[3]地域の人々が` làm chủ ngữ cho động từ `[1]協力して`.\n- `協力して` + `[2]くれた` (đã giúp đỡ cho chúng tôi) bổ nghĩa cho `[4]おかげ`.\n- `[4]おかげ` đứng ngay trước `にほかならない` (chẳng phải gì khác mà chính là nhờ...).\n→ Vị trí ★ là **2 (`くれた`)**!",
            "cute_wrong_msg": "Xem đuôi `にほかならない` đứng cuối: trước nó bắt buộc là danh từ `[4] おかげ` hoặc lý do `〜から`! Còn trước `おかげ` phải có mệnh đề `地域の人々が協力してくれた` đúng không nè? 🌸",
            "wrong_exps": [
                "`[1] 協力して` đứng ở ô số 2.",
                "Chính xác! Vị trí ★ là `[2] くれた` (`3 → 1 → 2 → 4`).",
                "`[3] 地域の人々が` đứng ở ô số 1.",
                "`[4] おかげ` đứng ở ô số 4 (ngay trước `にほかならない`)."
            ],
            "source_ref": {"novel": "romcom", "chapter": 10, "lesson_id": "p1_c07_b01", "label": "Ngữ pháp N2 ★ — 〜にほかならない"}
        },
        # --- 問題9: 文章の文法 (50-54) ---
        {
            "num": 50,
            "mondai": "問題9：文章の文法",
            "mondai_vi": "Ngữ pháp đoạn văn (Điền khuyết bài đọc)",
            "passage": PASSAGE_EXAM1,
            "passage_vi": PASSAGE_EXAM1_VI,
            "prompt": "空欄（　50　）に入る最もよいものを一つ選びなさい。\n「通勤電車の中でスマートフォンやタブレットを開いている姿を（　50　）、紙の本が完全に消えたわけではない。」",
            "prompt_vi": "Chọn đáp án đúng nhất điền vào chỗ trống (50): 'Dù ta thường thấy mọi người mở điện thoại/máy tính bảng trên tàu điện đi làm, sách giấy vẫn chưa hoàn toàn biến mất.'",
            "options": ["よく見かけるものの", "見かけるどころか", "見かけることから", "見かけるばかりに"],
            "ans": 1,
            "cute_right_msg": "Mượt mà quá luôn!! `よく見かけるものの` (tuy thường xuyên bắt gặp nhưng...) nối mạch văn nghịch tiếp sang 'sách giấy vẫn chưa biến mất' chuẩn 100%! 📖",
            "right_exp": "`〜ものの` diễn tả sự nhượng bộ nghịch tiếp nhẹ nhàng trong văn viết: 'Tuy rằng thường xuyên bắt gặp cảnh X thật đấy, nhưng sự thật vẫn không phải là Y'.",
            "cute_wrong_msg": "Đọc trọn câu chứa chỗ trống (50) nhé em: vế 1 nói nhiều người đọc trên điện thoại, vế 2 bảo 'nhưng sách giấy không biến mất đâu' → cần liên từ nhượng bộ `ものの` (tuy vậy nhưng)! 🌸",
            "wrong_exps": [
                "Chính xác tuyệt đối! `よく見かけるものの` (tuy hay bắt gặp thật đấy nhưng...).",
                "`どころか` nghĩa quá mạnh ('đừng nói là thấy mà ngược lại...') — không phù hợp thực tế là vẫn thấy người đọc điện thoại.",
                "`ことから` chỉ nguyên nhân ('vì thấy nhiều nên sách giấy không biến mất' là sai logic!).",
                "`ばかりに` chỉ nguyên nhân dẫn tới kết quả tệ hại ngoài ý muốn."
            ],
            "source_ref": {"novel": "romcom", "chapter": 9, "lesson_id": "p1_c06_b01", "label": "Ngữ pháp N2 — 文章の文法（〜ものの）"}
        },
        {
            "num": 51,
            "mondai": "問題9：文章の文法",
            "mondai_vi": "Ngữ pháp đoạn văn (Điền khuyết bài đọc)",
            "passage": PASSAGE_EXAM1,
            "passage_vi": PASSAGE_EXAM1_VI,
            "prompt": "空欄（　51　）に入る最もよいものを一つ選びなさい。\n「紙の本には、ページをめくる手触りやインクの香り、（　51　）自分の本棚に並べて眺める楽しみがある。」",
            "prompt_vi": "Chọn đáp án đúng nhất điền vào chỗ trống (51): 'Sách giấy có cảm giác lật trang, mùi mực in, và hơn thế nữa còn có niềm vui xếp trên giá sách riêng để ngắm.'",
            "options": ["それに対して", "さらには", "にもかかわらず", "それにしても"],
            "ans": 2,
            "cute_right_msg": "Đỉnh quá!! Liệt kê thêm điểm cộng thứ 3 nối tiếp phía sau bằng `さらには` (hơn thế nữa còn...) cực chuẩn mạch văn Nhật! ✨",
            "right_exp": "`さらには` dùng để liệt kê bổ sung thêm một ý cùng chiều tích cực hoặc mức độ cao hơn nữa ('và hơn thế nữa là...').",
            "cute_wrong_msg": "Xem quan hệ giữa các vế xung quanh (51) nha: đều đang liệt kê những niềm vui đáng yêu của sách giấy (cảm giác chạm, mùi mực, rồi *thêm nữa là* ngắm giá sách) → dùng `さらには`! 📚",
            "wrong_exps": [
                "`それに対して` dùng khi đối chiếu 2 mặt trái ngược nhau.",
                "Chính xác! `さらには` = và hơn thế nữa là...",
                "`にもかかわらず` = bất chấp mặc dù vậy (nghịch tiếp).",
                "`それにしても` = dẫu vậy đi nữa (nhận xét bất ngờ/đồng cảm về mức độ)."
            ],
            "source_ref": {"novel": "romcom", "chapter": 9, "lesson_id": "p1_c06_b01", "label": "Ngữ pháp N2 — 接続表現（さらには）"}
        },
        {
            "num": 52,
            "mondai": "問題9：文章の文法",
            "mondai_vi": "Ngữ pháp đoạn văn (Điền khuyết bài đọc)",
            "passage": PASSAGE_EXAM1,
            "passage_vi": PASSAGE_EXAM1_VI,
            "prompt": "空欄（　52　）に入る最もよいものを一つ選びなさい。\n「電子書籍は持ち運びに便利である（　52　）、目が疲れやすいという短所も指摘されている。」",
            "prompt_vi": "Chọn đáp án đúng nhất điền vào chỗ trống (52): 'Sách điện tử một mặt tiện mang theo bên mình, nhưng mặt khác cũng bị chỉ ra nhược điểm là dễ mỏi mắt.'",
            "options": ["おかげで", "せいで", "一方で", "だけに"],
            "ans": 3,
            "cute_right_msg": "Chuẩn đét! `便利である一方で` (một mặt tiện lợi, mặt khác lại có nhược điểm `短所も...`) đối xứng tuyệt đẹp luôn! ⚖️",
            "right_exp": "`一方で（いっぽうで）` chuyên dùng để nối hai vế đối lập hoặc hai mặt ưu - nhược song song của cùng một đối tượng (tiện mang đi ↔ dễ mỏi mắt).",
            "cute_wrong_msg": "Nhìn sự đối lập rõ nét giữa `便利` (ưu điểm) và `短所` (nhược điểm dễ mỏi mắt) nha em → chọn từ nối đối xứng 2 mặt là `一方で`! 🌟",
            "wrong_exps": [
                "`おかげで` = nhờ vào (nguyên nhân kết quả tốt — nhưng nhược điểm mỏi mắt là chuyện xấu!).",
                "`せいで` = tại vì (nhưng 'tiện lợi' không thể gây ra 'mỏi mắt' được).",
                "Chính xác! `便利である一方で` = một mặt tiện lợi, nhưng mặt khác...",
                "`だけに` = chính vì tiện nên lại càng... (cùng chiều, sai ngữ nghĩa)."
            ],
            "source_ref": {"novel": "yandere", "chapter": 3, "lesson_id": "p1_c06_b02", "label": "Ngữ pháp N2 — 対比（〜一方で）"}
        },
        {
            "num": 53,
            "mondai": "問題9：文章の文法",
            "mondai_vi": "Ngữ pháp đoạn văn (Điền khuyết bài đọc)",
            "passage": PASSAGE_EXAM1,
            "passage_vi": PASSAGE_EXAM1_VI,
            "prompt": "空欄（　53　）に入る最もよいものを一つ選びなさい。\n「（　53　）、両者にはそれぞれの良さがあり、場面に応じて使い分けるのが最も賢い方法だと言えるだろう。」",
            "prompt_vi": "Chọn đáp án đúng nhất điền vào chỗ trống (53): 'Vì thế / Tóm lại là, cả hai đều có nét hay riêng nên kết hợp linh hoạt tùy hoàn cảnh là khôn ngoan nhất.'",
            "options": ["たとえば", "要するに", "なぜなら", "それどころか"],
            "ans": 2,
            "cute_right_msg": "Chuẩn bài đọc văn nghị luận JLPT!! Đoạn cuối tóm gọn ý tổng kết toàn bài bằng `要するに` (tóm lại là) quá mượt! 📝✨",
            "right_exp": "`要するに（ようするに）` = Nói tóm lại là (dùng ở đoạn kết để đúc rút kết luận từ hai đoạn phân tích sách giấy và sách điện tử trước đó).",
            "cute_wrong_msg": "Chỗ trống (53) đứng ngay đầu đoạn KẾT LUẬN của bài văn đó em! Trong bài phân tích ưu nhược rồi chốt hạ lời khuyên, từ nối tóm tắt vàng là `要するに` (tóm lại là) nha~ 🌸",
            "wrong_exps": [
                "`たとえば` dùng để mở ra ví dụ minh họa, không phải kết luận.",
                "Chính xác! `要するに` = tóm lại mà nói.",
                "`なぜなら` dùng để giải thích lý do cho câu vừa nói ngay trước đó ('Sở dĩ như vậy là bởi vì...').",
                "`それどころか` mang nghĩa phủ định/bác bỏ mạnh hơn thế ('đừng nói thế, trái lại còn...')."
            ],
            "source_ref": {"novel": "romcom", "chapter": 12, "lesson_id": "p2_c02_b01", "label": "Ngữ pháp N2 — 接続表現（要するに）"}
        },
        {
            "num": 54,
            "mondai": "問題9：文章の文法",
            "mondai_vi": "Ngữ pháp đoạn văn (Điền khuyết bài đọc)",
            "passage": PASSAGE_EXAM1,
            "passage_vi": PASSAGE_EXAM1_VI,
            "prompt": "空欄（　54　）に入る最もよいものを一つ選びなさい。\n「技術の進歩によって本の形は変わっても、物語が人の心を動かす力そのものはこれからも（　54　）。」",
            "prompt_vi": "Chọn đáp án đúng nhất điền vào chỗ trống (54): 'Dù hình dáng cuốn sách có thay đổi theo công nghệ, bản thân sức mạnh lay động lòng người của câu chuyện chắc chắn từ nay về sau cũng sẽ không hề đổi thay.'",
            "options": ["変わらないに決まっている", "変わらないはずがない", "変わらないものではないだろうか", "変わりようがないだろう"],
            "ans": 4,
            "cute_right_msg": "ĐỈNH CỦA ĐỈNH!! Kết bài văn viết nghị luận mềm mại, sâu lắng bằng `変わりようがないだろう` (không cách nào có thể thay đổi được đâu nhỉ) chuẩn văn phong JLPT N2 luôn! 🏆💕",
            "right_exp": "`V(ます) + ようがない` = Không có cách nào để làm V / không tài nào xảy ra V được (`変わりようがない` = chẳng thể nào thay đổi nổi). Kết hợp `だろう` tạo sắc thái khẳng định điềm đạm chuẩn văn viết.",
            "cute_wrong_msg": "Chú ý sắc thái văn phong kết bài nghị luận JLPT nhé em! `〜に決まっている` quá chủ quan cảm tính kiểu văn nói; `〜はずがない` là 'không thể nào có chuyện KHÔNG đổi' (ngược nghĩa thành sẽ đổi mất!); còn `〜ようがないだろう` vừa lịch sự vừa khẳng định sâu sắc không thể đổi thay! ✨",
            "wrong_exps": [
                "`〜に決まっている` mang sắc thái khẳng định chủ quan quá mạnh kiểu văn nói ('nhất định là thế rồi!'), thường không hợp câu kết tinh tế kiểu văn viết xã luận.",
                "`変わらない + はずがない` nghĩa phủ định kép = 'không đời nào mà KHÔNG thay đổi' (tức là SẼ thay đổi — ngược nghĩa hoàn toàn!).",
                "`〜ものではないだろうか` thường dùng để khuyên nhủ chuẩn mực đạo đức ('chẳng phải là nên... hay sao'), không dùng với tự động từ `変わらない` về bản chất sự vật.",
                "Chính xác tuyệt đối! `変わりようがないだろう` = không thể nào thay đổi được đâu."
            ],
            "source_ref": {"novel": "isekai", "chapter": 12, "lesson_id": "p2_c07_b04", "label": "Ngữ pháp N2 — 可能性否定（〜ようがない）"}
        },
    ]
}
