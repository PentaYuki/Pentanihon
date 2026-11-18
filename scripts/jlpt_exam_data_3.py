# -*- coding: utf-8 -*-
"""
Đề Thi Thử JLPT N2 Chuẩn Số 03 — 言語知識（文字・語彙・文法）
Cấu trúc chuẩn 100% kỳ thi thật (54 câu — 55 phút)
"""

PASSAGE_EXAM3 = (
    "近年、プラスチックごみが海を汚染し、多くの海洋生物の命を奪っていることが世界中で深刻な問題となっている。そのため、使い捨てプラスチック製品の製造や販売を法律で（　50　）国々も増えてきた。\n"
    "しかし、法律による規制だけで問題を解決するのは難しい。私たちの便利さへの追求こそが、結果としてこれほど多くのごみを（　51　）からである。\n"
    "買い物の際にマイバッグを持参する（　52　）、小さな行動の積み重ねが大きな変化につながる。将来の世代に美しい地球を残す（　53　）、今の生活スタイルを見直す時期が来ているの（　54　）。"
)

PASSAGE_EXAM3_VI = (
    "Những năm gần đây, việc rác thải nhựa gây ô nhiễm đại dương và cướp đi sinh mạng của nhiều sinh vật biển đã trở thành vấn đề nhức nhối trên toàn cầu. Chính vì thế, ngày càng có nhiều quốc gia quy định hạn chế sản xuất và bán các sản phẩm nhựa dùng một lần bằng pháp luật.\n"
    "Tuy nhiên, thật khó để giải quyết triệt để vấn đề chỉ bằng quy định pháp luật. Bởi lẽ chính sự theo đuổi tiện lợi của chúng ta hệ quả đã dẫn đến việc tạo ra ngần ấy rác thải.\n"
    "Chẳng hạn như việc mang theo túi cá nhân khi đi mua sắm, sự tích lũy của những hành động nhỏ sẽ dẫn tới biến đổi to lớn. Để lưu giữ lại một Trái Đất tươi đẹp cho thế hệ tương lai, chẳng phải đã đến lúc chúng ta nhìn nhận lại lối sống hiện nay hay sao."
)

EXAM_3 = {
    "id": "jlpt-n2-de-03",
    "code": "ĐỀ CHUẨN JLPT N2 — SỐ 03",
    "title_jp": "第3回 JLPT N2 模擬試験（言語知識：文字・語彙・文法）",
    "title_vi": "Đề Thi Thử JLPT N2 Số 03 — Xã Hội, Môi Trường & Ngữ Pháp Tinh Hoa",
    "category": "full",
    "duration_min": 55,
    "pass_score": 19,
    "max_score": 60,
    "description": "Đề thi tổng hợp độ khó cao chuẩn kỳ thi JLPT N2 chính thức: tập trung vào từ đồng âm khác nghĩa, từ tượng thanh/tượng hình, quán dụng ngữ, cụm cấu trúc liên kết câu văn dài và bài đọc môi trường.",
    "yuki_note_start": "Đây là Đề Chuẩn Số 03 — chặng leo dốc cuối cùng trong bộ 3 full test nha em~ 💪 Độ lắt léo ở Đề 03 tiệm cận sát rạt đề thi thật tháng 7 & tháng 12 luôn! Cứ bình tĩnh phân tích cấu tạo chữ Hán và ngữ pháp tiếp nối nhé, chị Yuki tin em làm được mà 🌸✨",
    "yuki_note_finish_pass": "QUÁ XUẤT SẮC LUÔN EM ƠI!! 🎉🏆 Vượt qua cả Đề số 03 khó nhằn này rồi thì tấm bằng **JLPT N2** đang vẫy tay chào đón em rồi đó!! Nhớ lưu lại mục Lịch sử điểm để tự hào nhìn lại tiến bộ của mình nhé 💖",
    "yuki_note_finish_try": "Ôm an ủi em một cái thật dịu dàng nè~ 🫂 Đề 03 là đề nâng cao lọc bẫy cực gắt nên có sai vài câu cũng là chuyện siêu bình thường luôn! Quan trọng là mình xem kỹ phần phân tích cả 4 đáp án ở dưới để sau này không bao giờ sập lại cái bẫy đó nữa nhé 🌸✨",
    "questions": [
        # --- 問題1: 漢字読み (1-5) ---
        {
            "num": 1,
            "mondai": "問題1：漢字読み",
            "mondai_vi": "Cách đọc Kanji",
            "prompt": "新しい計画を進めるにあたって、住民の反発も<u>懸念</u>されている。",
            "prompt_vi": "Khi xúc tiến kế hoạch mới, sự phản đối từ cư dân cũng là điều đang được quan ngại.",
            "options": ["けんねん", "けねん", "きねん", "かんねん"],
            "ans": 2,
            "cute_right_msg": "Đỉnh luôn!! Em tránh được bẫy chữ `ん` ở âm `けねん` (`懸` là け chứ không phải けん ở đây)! 🌟",
            "right_exp": "`懸念（けねん）` (Huyền Niệm — mối lo ngại quan ngại) đọc ngắn chữ đầu là **けねん** (nhiều người hay đọc nhầm thành けんねん giống `懸命けんめい`).",
            "cute_wrong_msg": "Ôi cái bẫy đọc thêm âm mũi `ん` siêu tinh vi của `懸念` nè em! Nhớ nhé: `懸（け）` + `念（ねん）` = **けねん** thôi chứ không có `ん` ở giữa đâu nha! 💡",
            "wrong_exps": [
                "Dư âm mũi `ん` rồi em ơi! Âm chuẩn là `けねん`, không phải `けんねん`.",
                "Chính xác tuyệt đối! `懸念（けねん）` = mối quan ngại lo lắng.",
                "`きねん` là chữ `記念` (kỷ niệm) hoặc `祈念` (cầu nguyện).",
                "`かんねん` là chữ `観念` (quan niệm)."
            ],
            "source_ref": {"novel": "isekai", "chapter": 3, "lesson_id": "p1_c07_b04", "label": "Bộ 3 Isekai Ch.03 (Bài 17: Chính trị)"}
        },
        {
            "num": 2,
            "mondai": "問題1：漢字読み",
            "mondai_vi": "Cách đọc Kanji",
            "prompt": "会議の予定が急に変更され、<u>慌ただしく</u>準備を進めた。",
            "prompt_vi": "Lịch họp bất ngờ bị thay đổi khiến mọi người phải tất bật vội vã chuẩn bị.",
            "options": ["あわただしく", "いそがしく", "そうぞうしく", "さわがしく"],
            "ans": 1,
            "cute_right_msg": "Quá chuẩn! `慌ただしい` = `あわただしい` (tất bật, hối hả gấp gáp — cùng gốc với `慌てる`)! ⏱️",
            "right_exp": "`慌ただしい` đọc là **あわただしい** (tất bật, vội vàng cuống cuồng, biến thể của động từ `慌あわてる`).",
            "cute_wrong_msg": "Thấy chữ Hán `慌` là nhớ ngay động từ `慌（あわ）てる` (vội vã bối rối) → tính từ chính là `あわただしく` nha em! 🌸",
            "wrong_exps": [
                "Chính xác! `慌（あわ）ただしい` = tất bật hối hả.",
                "`いそがしい` là chữ `忙しい` (bận rộn).",
                "`そうぞうしい` là chữ `騒々しい` (ồn ào ầm ĩ).",
                "`さわがしい` là chữ `騒がしい` (náo động huyên náo)."
            ],
            "source_ref": {"novel": "romcom", "chapter": 12, "lesson_id": "p2_c02_b01", "label": "Bộ 1 Romcom Ch.12 (Bài 25: Tính từ N2)"}
        },
        {
            "num": 3,
            "mondai": "問題1：漢字読み",
            "mondai_vi": "Cách đọc Kanji",
            "prompt": "彼はとても<u>穏やか</u>な笑顔で、私たちの緊張をほぐしてくれた。",
            "prompt_vi": "Anh ấy với nụ cười vô cùng điềm đạm hiền hòa đã giúp chúng tôi xua tan căng thẳng.",
            "options": ["おだやか", "なごやか", "さわやか", "しとやか"],
            "ans": 1,
            "cute_right_msg": "Chính xác! `穏（おだ）やか` (Ôn hòa, điềm tĩnh dịu dàng) chuẩn không cần chỉnh! 🌿✨",
            "right_exp": "`穏やか（おだやか）` = hiền hòa, êm đềm, điềm tĩnh (`穏やかな天気・笑顔・性格`).",
            "cute_wrong_msg": "Nhớ ngay bài tính cách Romcom Ch.02 nè em: tính từ đuôi な có chữ `穏` (bên chữ lúa hòa bình) luôn đọc là **おだやか** nhé! 💖",
            "wrong_exps": [
                "Chính xác tuyệt đối! `穏（おだ）やか`.",
                "`なごやか` là chữ `和やか` (hòa nhã ấm cúng).",
                "`さわやか` là chữ `爽やか` (tươi mát sảng khoái).",
                "`しとやか` là chữ `淑やか` (đoan trang thùy mị)."
            ],
            "source_ref": {"novel": "romcom", "chapter": 2, "lesson_id": "p1_c01_b02", "label": "Bộ 1 Romcom Ch.02 (Bài 2: Tính cách)"}
        },
        {
            "num": 4,
            "mondai": "問題1：漢字読み",
            "mondai_vi": "Cách đọc Kanji",
            "prompt": "新入生を歓迎する催しは、とても<u>賑やか</u>だった。",
            "prompt_vi": "Sự kiện chào đón tân sinh viên đã diễn ra vô cùng náo nhiệt vui vẻ.",
            "options": ["はなやか", "にぎやか", "きらびやか", "あざやか"],
            "ans": 2,
            "cute_right_msg": "Quá mượt! `賑（にぎ）やか` = náo nhiệt tưng bừng (liên quan đến `賑わう` đông vui)! 🎉",
            "right_exp": "`賑やか` đọc là **にぎやか** (nhộn nhịp, đông vui náo nhiệt — cùng chữ Hán với động từ `賑わう` trong lễ hội Romcom Ch.10).",
            "cute_wrong_msg": "Chữ `賑` (chữ Bối tài sản + Thìn) chuyên chỉ không khí đông vui rộn rã: `にぎやか` nha em! ✨",
            "wrong_exps": [
                "`はなやか` là chữ `華やか` (lộng lẫy hoa lệ).",
                "Chính xác! `賑（にぎ）やか` = náo nhiệt nhộn nhịp.",
                "`きらびやか` là chữ `煌びやか` (hào nhoáng rực rỡ).",
                "`あざやか` là chữ `鮮やか` (tươi tắn rực rỡ sắc màu)."
            ],
            "source_ref": {"novel": "romcom", "chapter": 10, "lesson_id": "p1_c07_b01", "label": "Bộ 1 Romcom Ch.10 (Bài 14: Sự kiện)"}
        },
        {
            "num": 5,
            "mondai": "問題1：漢字読み",
            "mondai_vi": "Cách đọc Kanji",
            "prompt": "テストの成績を<u>競う</u>うちに、二人は良いライバルになった。",
            "prompt_vi": "Trong lúc cạnh tranh thành tích kiểm tra với nhau, cả hai đã trở thành những đối thủ tốt của nhau.",
            "options": ["あらそう", "きそう", "たたかう", "うばう"],
            "ans": 2,
            "cute_right_msg": "Chính xác! `競（きそ）う` (Cạnh — cạnh tranh thi đua tích cực), trong `競争（きょうそう）` đó! 🏆",
            "right_exp": "`競う` đọc là **きそう** (thi đua, ganh đua cạnh tranh lành mạnh về thành tích, tốc độ, tay nghề).",
            "cute_wrong_msg": "Chữ `競` trong `競争（きょうそう）・競技` khi đứng một mình làm động từ đọc là **きそう** (đối lập lành mạnh hơn `争う あらそう` là tranh giành xô xát)! 🌸",
            "wrong_exps": [
                "`あらそう` là chữ `争う` (tranh cãi, tranh giành mâu thuẫn).",
                "Tuyệt vời! `競（きそ）う` = thi đua cạnh tranh.",
                "`たたかう` là chữ `戦う / 闘う` (chiến đấu).",
                "`うばう` là chữ `奪う` (cướp đoạt)."
            ],
            "source_ref": {"novel": "romcom", "chapter": 7, "lesson_id": "p1_c05_b01", "label": "Bộ 1 Romcom Ch.07 (Bài 10: Trường học)"}
        },
        # --- 問題2: 表記 (6-10) ---
        {
            "num": 6,
            "mondai": "問題2：表記",
            "mondai_vi": "Chọn Kanji đúng",
            "prompt": "先輩に<u>はげまされて</u>、もう一歩だけ頑張ってみようと決心した。",
            "prompt_vi": "Được tiền bối động viên khích lệ, tôi quyết tâm thử cố gắng thêm một bước nữa.",
            "options": ["励まされて", "慰まされて", "労わられて", "慕われて"],
            "ans": 1,
            "cute_right_msg": "Quá đỉnh!! `励（はげ）ます` (chữ Lệ — có bộ 力 sức lực ở bên phải để cổ vũ tiếp sức!) chuẩn 100%! 💪✨",
            "right_exp": "`励ます（はげます）` = khích lệ, cổ vũ động viên tinh thần cho người khác cố gắng tiếp (`励まされる`: được khích lệ).",
            "cute_wrong_msg": "Nhìn cách chia đuôi `〜まされて`: chỉ có động từ `励ます` (nhóm 1 đuôi す → bị động `まされる`) dùng chữ Lệ `励` (khích lệ tiếp thêm sức `力`), còn `慰める` chia là `慰められる` nhé! 🌸",
            "wrong_exps": [
                "Chính xác! `励（はげ）ます → 励まされる` (được động viên khích lệ).",
                "`慰める` đọc là `なぐさめる` (an ủi người buồn) — bị động là `慰められて` chứ không có âm `ま`.",
                "`労わる` không tồn tại dạng viết `労わられて` (`労う ねぎらう` / `いたわる`).",
                "`慕う` đọc là `したう` (quý mến), bị động là `慕われて`."
            ],
            "source_ref": {"novel": "yandere", "chapter": 1, "lesson_id": "p1_c01_b03", "label": "Bộ 2 Yandere Ch.01 (Bài 3: Cảm xúc)"}
        },
        {
            "num": 7,
            "mondai": "問題2：表記",
            "mondai_vi": "Chọn Kanji đúng",
            "prompt": "会社は利益だけでなく、社会全体の幸福も<u>ついきゅう</u>するべきだ。",
            "prompt_vi": "Công ty không chỉ theo đuổi lợi nhuận mà còn nên hướng tới theo đuổi hạnh phúc của toàn xã hội.",
            "options": ["追究", "追求", "追及", "推求"],
            "ans": 2,
            "cute_right_msg": "TRỜI ƠI ĐỈNH CAO KANJI N2!! Ba anh em đồng âm `ついきゅう`: **追求** (theo đuổi giá trị/hạnh phúc/lợi ích), **追究** (truy cứu tìm hiểu sâu chân lý), **追及** (truy vấn gặng hỏi lỗi lầm)! 🏆",
            "right_exp": "Bộ ba đồng âm `ついきゅう` cực hay gặp trong đề thi thật:\n- **追求**: theo đuổi lý tưởng, mục tiêu, lợi ích, hạnh phúc.\n- **追究**: nghiên cứu truy tìm tới tận cùng chân lý/nguyên nhân.\n- **追及**: truy vấn trách nhiệm, dồn ép người phạm lỗi.",
            "cute_wrong_msg": "Phân biệt bộ ba sát thủ `ついきゅう` nè em ơi:\n- Tìm lợi ích/hạnh phúc/ước mơ = chữ Cầu **追求** (`要求・求`).\n- Tìm tòi khoa học chân lý = chữ Cứu **追究** (`研究`).\n- Truy hỏi trách nhiệm người gây lỗi = chữ Cập **追及**! 💡",
            "wrong_exps": [
                "`追究` dùng khi truy tìm sâu chân lý, nguyên nhân khoa học (`真理・原因を追究する`).",
                "Chính xác tuyệt đối! Theo đuổi lợi ích/hạnh phúc/tiện ích dùng `追求（ついきゅう）`.",
                "`追及` dùng khi chất vấn, truy cứu trách nhiệm người phạm lỗi (`責任を追及する`).",
                "Không ghép thành `推求`."
            ],
            "source_ref": {"novel": "yandere", "chapter": 8, "lesson_id": "p2_c03_b01", "label": "Bộ 2 Yandere Ch.08 (Bài 27: Từ gần hình dễ nhầm)"}
        },
        {
            "num": 8,
            "mondai": "問題2：表記",
            "mondai_vi": "Chọn Kanji đúng",
            "prompt": "国民は決められた期限までに税金を<u>おさめる</u>義務がある。",
            "prompt_vi": "Công dân có nghĩa vụ phải đóng nộp tiền thuế đúng trước thời hạn quy định.",
            "options": ["収める", "納める", "修める", "治める"],
            "ans": 2,
            "cute_right_msg": "Xuất sắc 10/10!! Tứ đại đồng âm `おさめる` trong Bài 27 (Yandere Ch.08): nộp thuế/học phí = **納める** (`納税・納入`)! 💳✨",
            "right_exp": "Phân biệt bộ tứ `おさめる` kinh điển:\n- **納める**: nộp tiền, thuế, học phí (`税金を納める・注文を納める`).\n- **収める**: gặt hái thành công (`成功を収める`), cất gọn vào hộp/ảnh (`写真に収める`).\n- **修める**: tu dưỡng, hoàn tất học vấn (`学問を修める`).\n- **治める**: cai trị đất nước, dẹp yên bão loạn (`国を治める`).",
            "cute_wrong_msg": "Nhớ bảng phân biệt tứ đại `おさめる` trong Bộ 2 Yandere Ch.08 nha em: đóng tiền thuế có chữ Nạp trong Nộp (`納める`), khác với gặt hái thành công (`収める`) hay cai trị (`治める`)! 💡",
            "wrong_exps": [
                "`収める` dùng cho kết quả/thu hoạch/thu ảnh (`成功を収める・写真に収める`).",
                "Chính xác tuyệt đối! `税金を納める` = nộp thuế.",
                "`修める` dùng cho học vấn, đạo đức (`学問を修める`).",
                "`治める` dùng cho cai trị đất nước hoặc làm dịu bệnh/bạo loạn."
            ],
            "source_ref": {"novel": "yandere", "chapter": 8, "lesson_id": "p2_c03_b01", "label": "Bộ 2 Yandere Ch.08 (Bài 27: Đồng âm おさめる)"}
        },
        {
            "num": 9,
            "mondai": "問題2：表記",
            "mondai_vi": "Chọn Kanji đúng",
            "prompt": "今年の梅雨は雨が多く、気温が急に下がって体調を<u>くずす</u>人が多い。",
            "prompt_vi": "Mùa mưa năm nay mưa nhiều, nhiệt độ hạ đột ngột nên nhiều người bị suy sụp đổ bệnh.",
            "options": ["崩す", "壊す", "乱す", "傾す"],
            "ans": 1,
            "cute_right_msg": "Chuẩn bài Yandere Ch.02!! Cụm vàng `体調を崩す（くずす）` dùng chữ `崩` (Băng — đổ sụp xuống)! 🤒🌸",
            "right_exp": "`体調を崩す（たいちょうをくずす）` = đổ bệnh, xuống sức suy nhược (dùng chữ **崩す**, KHÔNG dùng `壊す`).",
            "cute_wrong_msg": "Cụm kết hợp cố định N2 không đổi nè em: sức khỏe suy sụp là `体調を崩す` (chữ Băng `崩`, giống núi lở/thế thăng bằng sụp đổ), còn làm hỏng máy móc mới là `壊す（こわす）` nhé! 💊",
            "wrong_exps": [
                "Chính xác! `体調を崩（くず）す` = đổ bệnh, suy giảm sức khỏe.",
                "`壊す` đọc là `こわす` (làm hỏng đồ vật; hoặc `お腹を壊す` = đau bụng đi ngoài, KHÔNG dùng `体調を壊す`).",
                "`乱す` đọc là `みだす` (làm rối loạn hàng ngũ/nhịp điệu).",
                "`傾す` không có từ này (`傾く かたむく`)."
            ],
            "source_ref": {"novel": "yandere", "chapter": 2, "lesson_id": "p1_c02_b03", "label": "Bộ 2 Yandere Ch.02 (Bài 6: Sức khỏe)"}
        },
        {
            "num": 10,
            "mondai": "問題2：表記",
            "mondai_vi": "Chọn Kanji đúng",
            "prompt": "来月から電気料金の仕組みが<u>かいてい</u>されることになった。",
            "prompt_vi": "Từ tháng sau, cơ chế tính giá tiền điện sẽ được sửa đổi điều chỉnh lại.",
            "options": ["改訂", "改定", "開廷", "海底"],
            "ans": 2,
            "cute_right_msg": "Quá xịn!! Phân biệt được cặp `改定` (sửa đổi *giá cả, quy định, chế độ* `料金改定`) vs `改訂` (hiệu đính *sách vở, từ điển* `改訂版`) là trùm Kanji N2 rồi đó! 📖💳",
            "right_exp": "Cặp đồng âm `かいてい` siêu kinh điển của Shinkanzen Bài 27:\n- **改定（かいてい）**: sửa đổi, điều chỉnh lại **quy định, mức giá, thuế suất** (`料金・運賃・法律を改定する`).\n- **改訂（かいてい）**: chỉnh sửa biên tập lại **sách giáo khoa, từ điển, văn bản** (`教科書・辞書を改訂する`, `改訂版`).",
            "cute_wrong_msg": "Ôi cặp bẫy kinh điển trong Yandere Ch.08 đây rồi em ơi!! Có chữ 言 (ngôn từ/sách vở) là `改訂` (sửa sách), còn có chữ 定 (ấn định giá cả/quy định) mới là `改定` (`電気料金を改定`) nha! ✨",
            "wrong_exps": [
                "`改訂` (có bộ Ngôn `言`) chỉ dùng khi biên tập sửa nội dung sách báo, từ điển (`改訂版`).",
                "Chính xác tuyệt đối! Giá cả/quy định/mức cước dùng **改定（かいてい）**.",
                "`開廷` = mở phiên tòa xét xử.",
                "`海底` = đáy biển sâu."
            ],
            "source_ref": {"novel": "yandere", "chapter": 8, "lesson_id": "p2_c03_b01", "label": "Bộ 2 Yandere Ch.08 (Bài 27: 改定・改訂)"}
        },
        # --- 問題3: 語形成 (11-15) ---
        {
            "num": 11,
            "mondai": "問題3：語形成",
            "mondai_vi": "Cấu tạo từ (Tiền tố / Hậu tố)",
            "prompt": "どんな仕事でも自分の任された仕事に対して強い（　　）<u>感</u>を持って取り組むべきだ。",
            "prompt_vi": "Dù là công việc gì đi nữa cũng nên dốc sức làm với tinh thần trách nhiệm cao đối với phần việc mình được giao.",
            "options": ["安心", "親近", "危機", "責任"],
            "ans": 4,
            "cute_right_msg": "Chính xác! Làm việc được giao thì phải có `責任感（せきにんかん）` (tinh thần trách nhiệm)! 💼✨",
            "right_exp": "`責任感（せきにんかん）` = tinh thần trách nhiệm (đi với cụm cố định `責任感を持って取り組む`).",
            "cute_wrong_msg": "Đọc ngữ cảnh công việc 'đối với phần việc được giao phó': yếu tố cần có nhất là tinh thần trách nhiệm `責任感` chứ nhỉ~ 🌸",
            "wrong_exps": [
                "`安心感` là cảm giác an tâm thoải mái (không hợp cụm 'cầm lấy cảm giác an tâm để giải quyết việc').",
                "`親近感` là cảm giác gần gũi thân thiện.",
                "`危機感` là cảm giác nguy cấp báo động (lệch sắc thái mẫu chuẩn với `任された仕事`).",
                "Chính xác! `責任感（せきにんかん）を持って取り組む`."
            ],
            "source_ref": {"novel": "isekai", "chapter": 11, "lesson_id": "p2_c07_b03", "label": "Bộ 3 Isekai Ch.11 (Bài 36: Hậu tố 〜感)"}
        },
        {
            "num": 12,
            "mondai": "問題3：語形成",
            "mondai_vi": "Cấu tạo từ (Tiền tố / Hậu tố)",
            "prompt": "今日は朝から少し（　　）<u>気味</u>なので、会議が終わったら早く帰って休もう。",
            "prompt_vi": "Hôm nay từ sáng đã thấy người hơi mệt mệt rồi, nên họp xong tôi sẽ về sớm nghỉ ngơi.",
            "options": ["疲れ", "元気", "健康", "幸せ"],
            "ans": 1,
            "cute_right_msg": "Chuẩn luôn! `〜気味（ぎみ）` hay đi với trạng thái chớm mệt / chớm ốm / chậm: `疲れ気味（つかれぎみ）`! 🍵✨",
            "right_exp": "Hậu tố **〜気味（ぎみ）** gắn sau V(ます) hoặc Danh từ để diễn tả dấu hiệu hơi thiên về hướng (thường hơi tiêu cực hoặc chớm xuất hiện): `疲れ気味`, `風邪気味`, `遅れ気味`, `太り気味`.",
            "cute_wrong_msg": "Nhớ đặc tính của hậu tố **〜気味（ぎみ）** nha em: nó đi với dấu hiệu hơi chớm (thường hướng mệt/ốm/chậm/tăng cân), KHÔNG gắn với tính từ tích cực như khỏe/vui/hạnh phúc đâu! Vì thế 'về sớm nghỉ' đi với `疲れ気味` đó~ 💊",
            "wrong_exps": [
                "Chính xác! `疲れ気味` = hơi có cảm giác mệt mỏi đuối sức.",
                "`元気気味` không dùng trong tiếng Nhật.",
                "`健康気味` không dùng trong tiếng Nhật.",
                "`幸せ気味` không tồn tại."
            ],
            "source_ref": {"novel": "isekai", "chapter": 11, "lesson_id": "p2_c07_b03", "label": "Bộ 3 Isekai Ch.11 (Bài 36: Hậu tố 〜気味)"}
        },
        {
            "num": 13,
            "mondai": "問題3：語形成",
            "mondai_vi": "Cấu tạo từ (Tiền tố / Hậu tố)",
            "prompt": "この会議は機密事項を扱うため、内容は（　　）<u>公開</u>となっている。",
            "prompt_vi": "Vì cuộc họp này bàn về thông tin cơ mật nên nội dung được quy định là không công khai.",
            "options": ["無", "不", "非", "未"],
            "ans": 3,
            "cute_right_msg": "Quá chuẩn!! Tính chất 'không thuộc diện công khai chính thức' dùng tiền tố **非（ひ）**: `非公開（ひこうかい）` / `非公式`! 🔒",
            "right_exp": "Tiền tố **非（ひ）**: chỉ trạng thái không thuộc phạm trù chính thức/công khai: `非公開（ひこうかい）`, `非公式（ひこうしき）`, `非常識`.",
            "cute_wrong_msg": "Cặp song sinh cực hay thi cùng `公開・公式`: cả hai đều đi với tiền tố **非（ひ）** (`非公開` = bảo mật không công khai, `非公式` = không chính thức) nha em! ✨",
            "wrong_exps": [
                "`無公開` không tồn tại.",
                "`不公開` không dùng (nhưng lưu ý có từ `不透明` không rõ ràng).",
                "Chính xác tuyệt đối! `非公開（ひこうかい）` = không công khai.",
                "`未公開` là 'chưa công bố tới thời điểm này' (ví dụ phim chưa công chiếu `未公開映像`), nhưng ở đây nói quy định bảo mật vì chứa bí mật cơ mật nên chọn `非公開`."
            ],
            "source_ref": {"novel": "isekai", "chapter": 10, "lesson_id": "p2_c07_b02", "label": "Bộ 3 Isekai Ch.10 (Bài 35: Tiền tố 非〜)"}
        },
        {
            "num": 14,
            "mondai": "問題3：語形成",
            "mondai_vi": "Cấu tạo từ (Tiền tố / Hậu tố)",
            "prompt": "アパートを借りるときは、毎月の家賃だけでなく共益費などの（　　）<u>費用</u>も確認しよう。",
            "prompt_vi": "Khi thuê căn hộ, đừng chỉ xem tiền nhà hàng tháng mà hãy kiểm tra cả các khoản chi phí phát sinh khác như phí quản lý chung nữa nhé.",
            "options": ["各", "諸", "総", "最"],
            "ans": 2,
            "cute_right_msg": "ĐỈNH CỦA ĐỈNH!! `諸費用（しょひよう）` (nhiều loại chi phí lặt vặt khác nhau) = tiền tố **諸（しょ）** ăn điểm tuyệt đối luôn! 🏠📋",
            "right_exp": "Tiền tố **諸（しょ）** ghép trước Danh từ đếm chung nhiều loại khác nhau: `諸費用` (nhiều khoản phụ phí), `諸問題` (các vấn đề liên quan), `諸外国` (các nước ngoài).",
            "cute_wrong_msg": "Phân biệt nhanh `各` vs `諸` nè em: `各〜` đứng trước *đơn vị riêng lẻ* như `各国・各自・各駅`, còn gộp nhiều khoản/vấn đề đa dạng lại thành `〜費用・〜問題` phải dùng **諸（しょ）** (`諸費用・諸問題`) nhé! 🌟",
            "wrong_exps": [
                "`各` gắn vào đơn vị đếm riêng (`各国・各自`), không ghép thành `各費用`.",
                "Chính xác! `諸費用（しょひよう）` = các khoản chi phí liên quan khác nhau.",
                "`総費用` = tổng chi phí toàn bộ (nhưng câu có 'cả... nữa nhé' tách nhà riêng và các phụ phí khác ngoài tiền nhà).",
                "`最費用` không tồn tại."
            ],
            "source_ref": {"novel": "isekai", "chapter": 10, "lesson_id": "p2_c07_b02", "label": "Bộ 3 Isekai Ch.10 (Bài 35: Tiền tố 諸〜)"}
        },
        {
            "num": 15,
            "mondai": "問題3：語形成",
            "mondai_vi": "Cấu tạo từ (Tiền tố / Hậu tố)",
            "prompt": "旅行の前日に準備をしていて、肝心なカメラの充電器を入れ（　　）しまった。",
            "prompt_vi": "Chuẩn bị đồ trước ngày đi du lịch, tôi lại quên khuấy mất không cho cục sạc máy ảnh quan trọng vào vali.",
            "options": ["忘れて", "切って", "抜いて", "直して"],
            "ans": 1,
            "cute_right_msg": "Quá chuẩn! `入れ忘れる（いれわすれる）` = quên mất không bỏ vào (cấu trúc `V(ます) + 忘れる` giống `言い忘れる`)! 📷",
            "right_exp": "`V(ます) + 忘れる`: Quên làm hành động V (`入れ忘れる`: quên nhét vào, `言い忘れる`: quên chưa nói, `買い忘れる`: quên mua).",
            "cute_wrong_msg": "Ngữ cảnh chuẩn bị hành lý mà để lỡ món quan trọng (`充電器`): hành động bỏ vào túi nhưng lỡ quên chính là `入れ＋忘れる` (`入れ忘れてしまった`) nha em! 🎒",
            "wrong_exps": [
                "Chính xác! `入れ忘れてしまった` = lỡ quên chưa bỏ vào.",
                "`〜切る` là làm tới hết cạn (`使い切る`), không nói `入れ切る` cho 1 cái sạc.",
                "`〜抜く` là làm tới đích cuối (`走り抜く`).",
                "`〜直す` là sửa làm lại (`やり直す`), nếu cho lại từ đầu thì nghĩa sai ngữ cảnh '肝心な充電器を'."
            ],
            "source_ref": {"novel": "isekai", "chapter": 9, "lesson_id": "p2_c07_b01", "label": "Bộ 3 Isekai Ch.09 (Bài 34: Động từ ghép)"}
        },
        # --- 問題4: 文脈規定 (16-22) ---
        {
            "num": 16,
            "mondai": "問題4：文脈規定",
            "mondai_vi": "Điền từ vựng theo ngữ cảnh",
            "prompt": "この商品は（　　）な宣伝は必要ない。実際に使ってみた人の口コミだけで十分売れている。",
            "prompt_vi": "Sản phẩm này chẳng cần quảng cáo phô trương rầm rộ gì cả. Chỉ nhờ truyền miệng từ người dùng thực tế thôi cũng đã bán chạy lắm rồi.",
            "options": ["過剰（かじょう）", "わずか", "最低（さいてい）", "未満（みまん）"],
            "ans": 1,
            "cute_right_msg": "Chuẩn 100%! `過剰（かじょう）な宣伝 / 包装` (quảng cáo thái quá / đóng gói dư thừa quá mức) là từ tủ của N2 luôn! 🛍️",
            "right_exp": "`過剰（かじょう）な` = dư thừa, thái quá vượt mức cần thiết (`過剰な宣伝・期待・包装`).",
            "cute_wrong_msg": "Nhìn cụm phủ định 'không cần thiết phải quảng cáo quá lố vì hữu xạ tự nhiên hương': tính từ chỉ sự 'thừa thãi quá mức' là `過剰（かじょう）な` nha em! ✨",
            "wrong_exps": [
                "Chính xác! `過剰な宣伝` = quảng cáo phô trương thái quá.",
                "`わずか` nghĩa là ít ỏi (sai nghĩa: bảo không cần quảng cáo ít ỏi trong khi truyền miệng đã đủ?!).",
                "`最低` là mức tệ nhất / tối thiểu.",
                "`未満` chỉ gắn sau con số để nói 'dưới mốc'."
            ],
            "source_ref": {"novel": "isekai", "chapter": 6, "lesson_id": "p1_c09_b01", "label": "Bộ 3 Isekai Ch.06 (Bài 20: Số lượng)"}
        },
        {
            "num": 17,
            "mondai": "問題4：文脈規定",
            "mondai_vi": "Điền từ vựng theo ngữ cảnh",
            "prompt": "試験の合格発表を見てほっとした瞬間、これまで感じていた肩の荷が（　　）気がした。",
            "prompt_vi": "Khoảnh khắc nhìn thấy thông báo đỗ kỳ thi và thở phào nhẹ nhõm, tôi cảm thấy như vừa trút được gánh nặng khỏi vai vậy.",
            "options": ["上がった", "下りた", "乗った", "落ちた"],
            "ans": 2,
            "cute_right_msg": "Tuyệt vời!! Thành ngữ `肩の荷が下（お）りる` = trút bỏ được gánh nặng lo âu / trách nhiệm trên vai! 🎒✨",
            "right_exp": "`肩の荷が下（お）りる` là quán dụng ngữ cố định mang nghĩa thở phào nhẹ nhõm sau khi xong việc nặng hoặc đạt kết quả tốt.",
            "cute_wrong_msg": "Nhớ nguyên cụm quán dụng không được thay động từ nha em: trên vai `肩の荷` chỉ có `下りる` (hạ gánh xuống = nhẹ nhõm) chứ không dùng `落ちる` (rơi) đâu nè! 🌸",
            "wrong_exps": [
                "Không có cụm `肩の荷が上がる`.",
                "Chính xác tuyệt đối! `肩の荷が下りる` = trút bỏ gánh nặng trên vai.",
                "Không có cụm `肩の荷が乗る`.",
                "Rất dễ nhầm `落ちる` (rơi rớt) — thành ngữ Nhật bắt buộc phải là **下りる** (`おりる`)!"
            ],
            "source_ref": {"novel": "yandere", "chapter": 12, "lesson_id": "p2_c06_b02", "label": "Bộ 2 Yandere Ch.12 (Bài 33: Quán dụng ngữ 2)"}
        },
        # Chú ý sửa lại câu prompt Q17 mượt gọn ngay không có "……いや" trong prompt bằng edit nhanh sau khi ghi file (hoặc viết mượt luôn)!
        {
            "num": 18,
            "mondai": "問題4：文脈規定",
            "mondai_vi": "Điền từ vựng theo ngữ cảnh",
            "prompt": "新しい法律ができたとしても、すべての人がそれをきちんと（　　）しなければ意味がない。",
            "prompt_vi": "Dù có ban hành luật mới đi nữa, nếu mọi người không nghiêm chỉnh tuân thủ nó thì cũng vô nghĩa.",
            "options": ["遵守（じゅんしゅ）", "施行（しこう）", "制定（せいてい）", "判決（はんけつ）"],
            "ans": 1,
            "cute_right_msg": "Quá chuẩn!! Chủ ngữ là `すべての人` (người dân/mọi người) đối với luật thì chỉ có thể là `遵守（じゅんしゅ）する` (tuân thủ) thôi! ⚖️",
            "right_exp": "Người dân thì `法律を遵守する` (tuân thủ luật), còn nhà nước/quốc hội mới `法律を制定する` (lập luật) và luật `施行される` (có hiệu lực).",
            "cute_wrong_msg": "Nhìn chủ thể thực hiện ở đây là `すべての人` (toàn dân) nha em: dân chúng không thể tự ban hành (`制定`) hay tự xét xử (`判決`), dân chúng phải **tuân thủ** (`遵守する`) luật đó! 📜",
            "wrong_exps": [
                "Chính xác! `法律を遵守する` = tuân thủ luật pháp.",
                "`施行する/される` là cơ quan nhà nước cho luật đi vào hiệu lực.",
                "`制定する` là quốc hội/chính phủ ban hành lập luật mới.",
                "`判決` là bản án của thẩm phán tòa án."
            ],
            "source_ref": {"novel": "isekai", "chapter": 3, "lesson_id": "p1_c07_b04", "label": "Bộ 3 Isekai Ch.03 (Bài 17: Pháp luật)"}
        },
        {
            "num": 19,
            "mondai": "問題4：文脈規定",
            "mondai_vi": "Điền từ vựng theo ngữ cảnh",
            "prompt": "いくら親しい友達でも、人の悪口ばかり言っているのは（　　）。",
            "prompt_vi": "Dù có là bạn thân thiết đến mấy, việc cứ nói xấu sau lưng người khác mãi thật quá chướng mắt khó chấp nhận.",
            "options": ["目に余る", "目がない", "目を丸くする", "鼻が高い"],
            "ans": 1,
            "cute_right_msg": "ĐỈNH LUÔN!! Quán dụng cực sang `目に余る` = chướng tai gai mắt, quá đáng vượt ngưỡng chịu đựng! 👁️🚫",
            "right_exp": "`目に余る` = hành vi sai trái/xấu xí đến mức quá đáng không thể làm ngơ bỏ qua (`マナー違反が目に余る`).",
            "cute_wrong_msg": "Trong nhóm 3 quán dụng với `目` của Romcom Ch.13 nè: rất mê là `目がない`; ngạc nhiên là `目を丸くする`; còn hành vi xấu quá đáng chướng mắt là `目に余る` nha em! 🌸",
            "wrong_exps": [
                "Chính xác! `悪口ばかり言っているのは目に余る` = thật quá chướng mắt khó chấp nhận.",
                "`目がない` = mê mẩn cực kỳ thích món gì đó (`甘いものに目がない`).",
                "`目を丸くする` = tròn xoe mắt vì ngạc nhiên bất ngờ.",
                "`鼻が高い` = tự hào hãnh diện nở mũi."
            ],
            "source_ref": {"novel": "romcom", "chapter": 13, "lesson_id": "p2_c06_b01", "label": "Bộ 1 Romcom Ch.13 (Bài 32: Quán dụng ngữ 1)"}
        },
        {
            "num": 20,
            "mondai": "問題4：文脈規定",
            "mondai_vi": "Điền từ vựng theo ngữ cảnh",
            "prompt": "今度こそ合格できるように、毎日（　　）腰を据えて勉強に取り組むことにした。",
            "prompt_vi": "Để lần này nhất định thi đỗ, tôi quyết định mỗi ngày sẽ chuyên tâm ngồi ổn định dốc lòng học tập nghiêm túc.",
            "options": ["落ち着いて", "ふらふらと", "ぎりぎりで", "いいかげんに"],
            "ans": 1,
            "cute_right_msg": "Quá chuẩn! Ôm cặp `落ち着いて腰を据える` (bình tĩnh chuyên tâm ngồi vững một chỗ theo đuổi mục tiêu đến cùng)! 📚✨",
            "right_exp": "`腰を据える` (đặt hông vững vàng) = làm việc/nghiên cứu một cách kiên trì, tập trung sâu và nghiêm túc lâu dài, đi tự nhiên với `落ち着いて`.",
            "cute_wrong_msg": "Quán dụng `腰を据えて取り組む` mang nghĩa 'ngồi vững tâm dốc lòng theo đuổi tới cùng', nên trạng từ đứng kèm phải mang nghĩa điềm tĩnh tập trung (`落ち着いて`) nha em! 💡",
            "wrong_exps": [
                "Chính xác! `落ち着いて腰を据えて取り組む` = bình tĩnh chuyên tâm theo đuổi mục tiêu.",
                "`ふらふらと` là đi loạng choạng vô định (mâu thuẫn `腰を据える`).",
                "`ぎりぎりで` = sát nút giờ chót (sai cấu trúc với `毎日`).",
                "`いいかげんに` = qua loa cẩu thả (ngược nghĩa hoàn toàn)."
            ],
            "source_ref": {"novel": "yandere", "chapter": 12, "lesson_id": "p2_c06_b02", "label": "Bộ 2 Yandere Ch.12 (Bài 33: Quán dụng ngữ 2)"}
        },
        {
            "num": 21,
            "mondai": "問題4：文脈規定",
            "mondai_vi": "Điền từ vựng theo ngữ cảnh",
            "prompt": "彼女はとても真面目な人だから、約束を（　　）ようなことは絶対にしない。",
            "prompt_vi": "Vì cô ấy là người rất đứng đắn nghiêm túc, chuyện thất hứa phá bỏ lời hẹn thì tuyệt đối cô ấy không bao giờ làm đâu.",
            "options": ["破る", "壊す", "乱す", "外す"],
            "ans": 1,
            "cute_right_msg": "Chuẩn 100%! Collocation kinh điển `約束を破る（やぶる）` = thất hứa / phá vỡ cam kết! 🤝",
            "right_exp": "`約束を破る` (cũng dùng với `ルールを破る`, `記録を破る`): thất hứa, phá vỡ quy tắc hoặc phá kỷ lục.",
            "cute_wrong_msg": "Cụm kết hợp của danh từ `約束` (lời hứa): giữ lời là `約束を守る`, còn thất hứa phá lời hứa dùng động từ `破る（やぶる）` (như xé rách tờ giao ước) nha em! 🌸",
            "wrong_exps": [
                "Chính xác tuyệt đối! `約束を破る` = thất hứa.",
                "`壊す` dùng cho vật thể hữu hình như máy móc đồ đạc (`時計を壊す`), không dùng `約束を壊す`.",
                "`乱す` = làm xáo trộn hàng ngũ/nhịp sống.",
                "`外す` = tháo gỡ ra (`メガネを外す`), không dùng `約束を外す`."
            ],
            "source_ref": {"novel": "yandere", "chapter": 12, "lesson_id": "p2_c06_b02", "label": "Bộ 2 Yandere Ch.12 (collocation 約束を破る)"}
        },
        {
            "num": 22,
            "mondai": "問題4：文脈規定",
            "mondai_vi": "Điền từ vựng theo ngữ cảnh",
            "prompt": "海外からの留学生の（　　）に伴い、大学内の案内表示も多言語化された。",
            "prompt_vi": "Cùng với việc lượng du học sinh nước ngoài tăng vọt đột biến, các biển chỉ dẫn trong khuôn viên đại học cũng được đa ngôn ngữ hóa.",
            "options": ["急増（きゅうぞう）", "急減（きゅうげん）", "不足（ふそく）", "減少（げんしょう）"],
            "ans": 1,
            "cute_right_msg": "Chính xác! Phía sau phải đa ngôn ngữ hóa biển hiệu (`多言語化`) thì lý do tất yếu là du học sinh *tăng vọt* = `急増`! 🌏✨",
            "right_exp": "`急増（きゅうぞう）` = sự tăng vọt nhanh chóng trong thời gian ngắn, gắn trực tiếp trước `〜に伴い` (`N に伴い`).",
            "cute_wrong_msg": "Nhìn kết quả vế sau 'biển chỉ dẫn đại học phải làm thêm nhiều ngôn ngữ khác nhau' nha em → lượng du học sinh phải *tăng mạnh đột ngột* (`急増`) mới cần đổi biển chứ nhỉ~ 🌸",
            "wrong_exps": [
                "Chính xác tuyệt đối! `急増` = sự tăng vọt.",
                "`急減` là giảm đột ngột (vế sau không cần dịch đa ngôn ngữ thêm nữa).",
                "`不足` là sự thiếu hụt.",
                "`減少` là sự sụt giảm."
            ],
            "source_ref": {"novel": "isekai", "chapter": 6, "lesson_id": "p1_c09_b01", "label": "Bộ 3 Isekai Ch.06 (Bài 20: Số lượng)"}
        },
        # --- 問題5: 言い換え類義 (23-27) ---
        {
            "num": 23,
            "mondai": "問題5：言い換え類義",
            "mondai_vi": "Từ / cụm từ đồng nghĩa",
            "prompt": "あの二人の間では、この計画をめぐって<u>しきりに</u>意見が交わされた。",
            "prompt_vi": "Giữa hai người họ, ý kiến xoay quanh kế hoạch này được trao đổi liên tục dồn dập.",
            "options": ["めったに", "何度も続けて", "たまに", "しぶしぶ"],
            "ans": 2,
            "cute_right_msg": "Đỉnh luôn!! Phó từ `しきりに` (liên tiếp không ngớt, dồn dập nhiệt tình) học trong Yandere Ch.09 mà em vẫn nhớ chuẩn đét! 💬🔥",
            "right_exp": "`しきりに` diễn tả hành động lặp đi lặp lại liên tục trong một khoảng thời gian (`しきりに時計を見る・雨がしきりに降る・意見が交わされる`) ≈ `何度も続けて`.",
            "cute_wrong_msg": "Nhắc nhẹ bạn phó từ `しきりに` (cặp hay ra thi N2 đó nha em): nghĩa là hành động diễn ra **liên tục dồn dập hết lần này đến lần khác** (`何度も続けて`) nhé! ✨",
            "wrong_exps": [
                "`めったに（〜ない）` là hiếm khi.",
                "Chính xác! `しきりに` = `何度も続けて` (liên tiếp nhiều lần).",
                "`たまに` là thỉnh thoảng họa hoằn.",
                "`しぶしぶ` là miễn cưỡng gượng gạo."
            ],
            "source_ref": {"novel": "yandere", "chapter": 9, "lesson_id": "p2_c04_b01", "label": "Bộ 2 Yandere Ch.09 (Bài 28: Phó từ 1)"}
        },
        {
            "num": 24,
            "mondai": "問題5：言い換え類義",
            "mondai_vi": "Từ / cụm từ đồng nghĩa",
            "prompt": "山田さんの話によると、駅前に新しい図書館ができるという<u>耳寄りな</u>情報があるそうだ。",
            "prompt_vi": "Theo lời anh Yamada, nghe nói có một tin rất đáng nghe / hấp dẫn là sắp có thư viện mới xây trước ga đấy.",
            "options": ["聞くと嬉しいお得な", "信じられないほど悲しい", "誰でも知っている古い", "秘密にしておくべき悪い"],
            "ans": 1,
            "cute_right_msg": "Quá dễ thương luôn!! `耳寄りな情報（みみよりなじょうほう）` = tin hay đáng nghe, có lợi thú vị! 👂💖",
            "right_exp": "`耳寄りな話・情報`: Thông tin hay ho, hấp dẫn và có lợi khiến người nghe rất mừng muốn biết (`聞くと嬉しいお得な`).",
            "cute_wrong_msg": "Hễ thấy quán dụng `耳寄りな（みみよりな）` ('nghe mà tai muốn ghé sát vào') thì chắc chắn là **tin vui, thú vị, có lợi** (`お得な情報`), đừng nhầm với `耳が痛い` (nhột vì chê) nha em! 🌸",
            "wrong_exps": [
                "Chính xác! `耳寄りな話` = thông tin thú vị, hữu ích đáng nghe.",
                "Tin buồn đau lòng không dùng `耳寄りな`.",
                "Tin cũ ai cũng biết càng không gọi là `耳寄りな`.",
                "Tin xấu bí mật càng trái ngược hoàn toàn."
            ],
            "source_ref": {"novel": "romcom", "chapter": 13, "lesson_id": "p2_c06_b01", "label": "Bộ 1 Romcom Ch.13 (Bài 32: Quán dụng ngữ 1)"}
        },
        {
            "num": 25,
            "mondai": "問題5：言い換え類義",
            "mondai_vi": "Từ / cụm từ đồng nghĩa",
            "prompt": "深夜まで仕事をしたあと、友達と温泉に入って心から<u>すっきりした</u>。",
            "prompt_vi": "Sau khi làm việc đến tận khuya, tôi cùng bạn đi ngâm suối nước nóng và thấy sảng khoái nhẹ nhàng hẳn cả người.",
            "options": ["イライラした", "がっかりした", "さわやかな気分になった", "ぐったり疲れた"],
            "ans": 3,
            "cute_right_msg": "Tuyệt vời! Tắm suối nước nóng xong thấy đầu óc `すっきり` = sảng khoái dễ chịu hẳn (`さわやかな気分になった`)! ♨️✨",
            "right_exp": "`すっきりする`: Cắt bỏ hết bức bối/bẩn/mệt mỏi, cảm thấy thanh thản, sảng khoái và nhẹ đầu (`さわやかな気分になる`).",
            "cute_wrong_msg": "Ngâm onsen nóng hổi sau giờ làm thì cảm giác `すっきりする` chắc chắn là sảng khoái nhẹ nhõm đầu óc (`さわやかな気分`) rồi ha em~ Chớ nhầm với `ぐったり` (mệt rũ rượi) nhé! 🌺",
            "wrong_exps": [
                "`イライラした` = cáu kỉnh bực bội.",
                "`がっかりした` = thất vọng chán nản.",
                "Chính xác! `すっきりした` ≈ `さわやかな気分になった` (sảng khoái, nhẹ nhõm).",
                "`ぐったり疲れた` = mệt lả rũ rượi (ngược nghĩa hoàn toàn sau khi thư giãn ở onsen)."
            ],
            "source_ref": {"novel": "isekai", "chapter": 8, "lesson_id": "p2_c05_b01", "label": "Bộ 3 Isekai Ch.08 (Bài 31: Onomatopoeia)"}
        },
        {
            "num": 26,
            "mondai": "問題5：言い換え類義",
            "mondai_vi": "Từ / cụm từ đồng nghĩa",
            "prompt": "彼の誠実な仕事ぶりには、上司である私でさえ<u>頭が下がる</u>思いだ。",
            "prompt_vi": "Trước tác phong làm việc chân thành tận tâm của cậu ấy, đến cả một người sếp như tôi cũng cảm thấy vô cùng kính nể.",
            "options": ["心から感心する", "ひどくあきれる", "申し訳なく思う", "大変腹が立つ"],
            "ans": 1,
            "cute_right_msg": "Chuẩn đét! `頭が下がる` = cúi đầu kính phục khâm phục sâu sắc trước đức tính tốt đẹp (`感心する`)! 🙇‍♂️✨",
            "right_exp": "`頭が下がる`: Khâm phục, kính nể sâu sắc từ đáy lòng (`心から感心する・尊敬する`). Nhớ phân biệt với `頭が上がらない` (lép vế/mang ơn nên không dám cãi).",
            "cute_wrong_msg": "Coi vế trước khen ngợi phẩm chất cao đẹp 'tác phong làm việc chân thành tận tâm (`誠実な仕事ぶり`)': cúi đầu trước điều tốt chính là vô cùng **kính nể khâm phục** (`感心する`), KHÔNG phải xin lỗi đâu nha! 🌸",
            "wrong_exps": [
                "Chính xác tuyệt đối! `頭が下がる` = `心から感心する` (vô cùng khâm phục).",
                "`ひどくあきれる` = chán nản cạn lời ngán ngẩm.",
                "`申し訳なく思う` = thấy áy náy có lỗi.",
                "`腹が立つ` = tức giận bực mình."
            ],
            "source_ref": {"novel": "romcom", "chapter": 13, "lesson_id": "p2_c06_b01", "label": "Bộ 1 Romcom Ch.13 (Bài 32: Quán dụng ngữ 1)"}
        },
        {
            "num": 27,
            "mondai": "問題5：言い換え類義",
            "mondai_vi": "Từ / cụm từ đồng nghĩa",
            "prompt": "新発売の薬品が市場に出回るや否や、効果の高さから予想を<u>上回る</u>注文が集まった。",
            "prompt_vi": "Dược phẩm mới ra mắt vừa tung ra thị trường, nhờ hiệu quả cao đã thu hút lượng đơn đặt hàng vượt xa mức dự đoán.",
            "options": ["よりずっと少なくなる", "よりずっと多くなる", "と同じくらいになる", "より少し遅くなる"],
            "ans": 2,
            "cute_right_msg": "Quá xịn! `予想を上回る（うわまわる）` = vượt xa hẳn con số dự tính (`よりずっと多くなる`)! 📈",
            "right_exp": "`上回る（うわまわる）` = cao hơn, nhiều hơn, vượt qua một ngưỡng/mức dự báo cho trước (`下回る` là thấp hơn).",
            "cute_wrong_msg": "Chữ Thượng (`上`) + Hồi (`回る`) trong `上回る`: chắc chắn là lớn hơn/nhiều hơn mức dự báo phía trước chứ không phải ít hơn hay bằng nhau nha em! ✨",
            "wrong_exps": [
                "`よりずっと少なくなる` ứng với động từ trái nghĩa `下回る（したまわる）`.",
                "Chính xác! `予想を上回る` = lớn hơn/vượt mức dự đoán.",
                "`と同じくらい` = ngang bằng (trùng cỡ khoảng).",
                "`遅くなる` = chậm trễ (sai phạm trù số lượng/mức độ)."
            ],
            "source_ref": {"novel": "isekai", "chapter": 6, "lesson_id": "p1_c09_b01", "label": "Bộ 3 Isekai Ch.06 (Bài 20: Số lượng)"}
        },
        # --- 問題6: 用法 (28-32) ---
        {
            "num": 28,
            "mondai": "問題6：用法",
            "mondai_vi": "Cách dùng từ đúng trong câu",
            "prompt": "次の言葉の使い方として最もよいものを、1・2・3・4から一つ選びなさい。\n【言葉：<b><u>間隔</u></b>】",
            "prompt_vi": "Chọn câu sử dụng đúng nhất từ 【間隔（かんかく）】 (khoảng cách giãn cách đều giữa các vật/thời điểm).",
            "options": [
                "バスの運行間隔が長すぎて、次のバスまで30分も待たされた。",
                "初めて会ったのに、彼はとても温かい間隔を持っている人だ。",
                "東京と大阪の間の間隔は、新幹線で約2時間半かかる。",
                "音楽を聴くとき、音の間隔が大きすぎて耳が痛くなった。"
            ],
            "ans": 1,
            "cute_right_msg": "ĐỈNH CỦA CHÓP!! Phân biệt được 3 anh em đồng âm `かんかく`: **間隔** (khoảng cách giãn cách giữa các chuyến/cây/người), **感覚** (giác quan/cảm giác), **距離** (cự ly giữa 2 thành phố)! 🚌📏",
            "right_exp": "`間隔（かんかく）` chỉ **khoảng cách (không gian hoặc thời gian) xen giữa những sự vật/sự việc lặp lại nối tiếp nhau** (`運行間隔`: giãn cách chuyến xe, `間隔をあけて並べる`: xếp cách đều). Khác với `感覚` (cảm giác/giác quan) và `距離` (quãng đường giữa 2 điểm địa lý).",
            "cute_wrong_msg": "Đây là câu lọc đồng âm `かんかく` kinh điển nhất Mondai 6 JLPT N2 đó em!! `間隔（かんかく）` = **quãng cách giữa các chuyến tàu xe / đồ vật xếp hàng**, KHÔNG phải 'cảm giác' (`感覚`), 'cự ly 2 thành phố' (`距離`), hay 'âm lượng' (`音量`) nha! 🌟",
            "wrong_exps": [
                "Chính xác tuyệt đối! `バスの運行間隔` = giãn cách thời gian giữa các chuyến xe buýt.",
                "Cảm giác, sự nhạy cảm tâm hồn dùng chữ Hán khác: `感覚（かんかく）`.",
                "Quãng đường giữa 2 thành phố dùng `距離（きょり）`, không dùng `間隔`.",
                "Độ to nhỏ âm thanh dùng `音量（おんりょう）`, không phải `音の間隔`."
            ],
            "source_ref": {"novel": "isekai", "chapter": 7, "lesson_id": "p1_c09_b02", "label": "Bộ 3 Isekai Ch.07 (Bài 21: Không gian)"}
        },
        {
            "num": 29,
            "mondai": "問題6：用法",
            "mondai_vi": "Cách dùng từ đúng trong câu",
            "prompt": "次の言葉の使い方として最もよいものを、1・2・3・4から一つ選びなさい。\n【言葉：<b><u>受け継ぐ</u></b>】",
            "prompt_vi": "Chọn câu sử dụng đúng nhất từ 【受け継ぐ（うけつぐ）】 (tiếp nối, kế thừa truyền thống/tài sản/ý chí).",
            "options": [
                "駅で友達から大切な荷物をしっかり受け継いだ。",
                "先代から守られてきた伝統の製法を、次の世代へ受け継ぐ。",
                "大学に合格して、希望していた奨学金を大学から受け継いだ。",
                "風邪が家族に受け継いでしまい、みんな寝込んでしまった。"
            ],
            "ans": 2,
            "cute_right_msg": "Chuẩn 100 điểm luôn! `受け継ぐ` chuyên dùng cho việc kế thừa **truyền thống, nghề gia truyền, tài sản trí tuệ, ý chí** qua các thế hệ — KHÔNG dùng để nhận bưu kiện, nhận học bổng hay... lây cảm cúm đâu nhé! 🏮✨",
            "right_exp": "`受け継ぐ` = kế thừa di sản vô hình hoặc truyền thống lâu đời (`伝統・技術・意志を受け継ぐ`). Nhận đồ dùng `受け取る`, lây bệnh dùng `うつる・感染する`.",
            "cute_wrong_msg": "Mẹo phân biệt siêu nét nha em: nhận hành lý từ bạn là `受け取る`; nhận tiền học bổng là `受け取る / もらう`; còn `受け継ぐ` (Thụ + Kế) bắt buộc mang nghĩa **kế thừa nối dõi truyền thống/ý chí/nghề nghiệp** qua thế hệ! 🌸",
            "wrong_exps": [
                "Nhận hành lý trực tiếp dùng `受け取る` (`荷物を受け取った`).",
                "Chính xác tuyệt đối! Kế thừa bí quyết truyền thống cho thế hệ sau (`受け継ぐ`).",
                "Nhận học bổng dùng `受ける / 受け取る / もらう`.",
                "Lây bệnh cảm cúm dùng `うつる` hoặc `感染する` (NOT `受け継ぐ`!)."
            ],
            "source_ref": {"novel": "isekai", "chapter": 9, "lesson_id": "p2_c07_b01", "label": "Bộ 3 Isekai Ch.09 (Bài 34: Từ ghép)"}
        },
        {
            "num": 30,
            "mondai": "問題6：用法",
            "mondai_vi": "Cách dùng từ đúng trong câu",
            "prompt": "次の言葉の使い方として最もよいものを、1・2・3・4から一つ選びなさい。\n【言葉：<b><u>あえて</u></b>】",
            "prompt_vi": "Chọn câu sử dụng đúng nhất từ 【あえて】 (dẫu biết khó/bất lợi/không cần thiết nhưng vẫn cố tình/mạnh dạn làm).",
            "options": [
                "彼女はとても優しいので、みんなのためにあえて親切にしている。",
                "失敗する危険があると知りながら、私はあえて難しい道を選んだ。",
                "道に迷ってしまい、あえて駅の周りをうろうろ歩いた。",
                "雨がひどく降っているので、あえて傘を持って外に出た。"
            ],
            "ans": 2,
            "cute_right_msg": "Cảm giác ngôn ngữ đỉnh cao!! `あえて` hàm ý **chủ động làm ngược với điều hiển nhiên / dẫu biết rủi ro khó khăn vẫn cố tình chọn làm** (`あえて挑戦する・言わない・選ぶ`)! 🔥",
            "right_exp": "`あえて`: Cố ý làm một điều dù biết là mạo hiểm, trái thông lệ, không cần thiết hoặc gây khó khăn (nhấn mạnh *ý chí chủ động* vượt qua trở ngại hoặc chọn cách khác người).",
            "cute_wrong_msg": "Từ `あえて` trong Shinkanzen (Yandere Ch.11) cực hay nhầm trong đề thi thật nha em! Nhớ nhé: nếu làm điều hợp lý đương nhiên (che ô khi mưa, tốt bụng giúp người) hoặc vô thức (lạc đường đi loanh quanh) thì KHÔNG dùng `あえて`! Chỉ dùng khi **biết khó/lạ mà vẫn cố tình làm**! 💖",
            "wrong_exps": [
                "Vì tính tốt nên đối xử tử tế là điều tự nhiên đương nhiên, không dùng `あえて` (cố tình trái thường lệ).",
                "Chính xác tuyệt đối! Biết rõ nguy hiểm thất bại mà vẫn cố tình chọn con đường khó (`あえて選んだ`).",
                "Đi lạc loanh quanh không phải hành động 'mạnh dạn cố tình vượt trở ngại'.",
                "Trời mưa to cầm ô là lẽ thường tình đương nhiên (`当然` mới hợp, trừ phi vế nói 'trời mưa nhưng tôi *cố tình KHÔNG* cầm ô' thì mới dùng `あえて`)."
            ],
            "source_ref": {"novel": "yandere", "chapter": 11, "lesson_id": "p2_c04_b03", "label": "Bộ 2 Yandere Ch.11 (Bài 30: Phó từ khác)"}
        },
        {
            "num": 31,
            "mondai": "問題6：用法",
            "mondai_vi": "Cách dùng từ đúng trong câu",
            "prompt": "次の言葉の使い方として最もよいものを、1・2・3・4から一つ選びなさい。\n【言葉：<b><u>ぎっしり</u></b>】",
            "prompt_vi": "Chọn câu sử dụng đúng nhất từ 【ぎっしり】 (chật ních, ken đặc kín mít không còn chỗ trống).",
            "options": [
                "今月の手帳は、毎日の仕事やアルバイトの予定でぎっしり詰まっている。",
                "風が気持ちよくて、部屋の中がぎっしり涼しくなった。",
                "あの二人は性格が似ていて、いつもぎっしり仲良くしている。",
                "試験が終わって肩の荷が下り、心がぎっしり軽くなった。"
            ],
            "ans": 1,
            "cute_right_msg": "Chuẩn 100%! `ぎっしり詰まっている` = nhét chật ních kín mít từng khoảng trống trong sổ/valy/xe tàu! 📅✨",
            "right_exp": "`ぎっしり` diễn tả vật thể, chữ viết hoặc lịch trình được **nhồi nhét lấp kín không còn kẽ hở nào** (`予定・荷物・文字がぎっしり詰まっている`).",
            "cute_wrong_msg": "Hình dung 1 chiếc hộp hay quyển sổ được xếp đồ/chữ kín không còn 1 milimet hở → `ぎっしり詰まる` nha em! Không dùng cho không khí mát (`涼しい`), thân thiết hay nhẹ lòng (`すっきり`) đâu nhé! 🌸",
            "wrong_exps": [
                "Chính xác tuyệt đối! Lịch làm việc viết kín đặc trong sổ tay (`予定がぎっしり詰まっている`).",
                "Gió mát sảng khoái không dùng `ぎっしり`.",
                "Thân thiết hợp nhau dùng `ぴったり` hoặc `とても仲良く`, không dùng `ぎっしり`.",
                "Nhẹ nhõm đầu óc dùng `すっきり`, không dùng `ぎっしり`."
            ],
            "source_ref": {"novel": "isekai", "chapter": 8, "lesson_id": "p2_c05_b01", "label": "Bộ 3 Isekai Ch.08 (Bài 31: Onomatopoeia)"}
        },
        {
            "num": 32,
            "mondai": "問題6：用法",
            "mondai_vi": "Cách dùng từ đúng trong câu",
            "prompt": "次の言葉の使い方として最もよいものを、1・2・3・4から一つ選びなさい。\n【言葉：<b><u>提携</u></b>】",
            "prompt_vi": "Chọn câu sử dụng đúng nhất từ 【提携（ていけい）】 (bắt tay hợp tác liên minh chiến lược giữa các công ty/tổ chức).",
            "options": [
                "来週の日曜日に、仲の良い友達と図書館で勉強の提携をしよう。",
                "A社とB社が技術面で業務提携を結び、新しいアプリを開発した。",
                "料理を作るとき、砂糖と塩の提携を間違えないように気をつける。",
                "電車の時刻とバスの出発を提携して、毎日学校へ通っている。"
            ],
            "ans": 2,
            "cute_right_msg": "Quá chuẩn! `企業間の業務提携（ぎょうむていけい）` = hợp tác liên kết nghiệp vụ giữa các công ty/tổ chức — chuyên dùng trong bài Kinh tế Isekai Ch.02! 🤝💼",
            "right_exp": "`提携（ていけい）` chỉ sự **liên minh hợp tác kinh doanh/nghiệp vụ/kỹ thuật giữa 2 doanh nghiệp, tổ chức hoặc địa phương với nhau** (`業務提携を結ぶ・資本提携`). Không dùng cho cá nhân học bài hay gia vị nấu ăn.",
            "cute_wrong_msg": "Từ vựng `提携（ていけい）` (Đề Huệ — nắm tay nhau phát triển) trong Shinkanzen chỉ dùng giữa **các công ty / tổ chức / trường học / thành phố kết nghĩa**, KHÔNG dùng cho hai bạn rủ nhau học bài hay pha gia vị đâu nha! 🏢✨",
            "wrong_exps": [
                "Hai người bạn rủ nhau học dùng `協力して勉強する` hoặc `約束する`, không dùng `提携`.",
                "Chính xác! Hai công ty ký kết hợp tác nghiệp vụ kỹ thuật (`業務提携を結ぶ`).",
                "Tỷ lệ phân lượng gia vị dùng `割合・分量`, không phải `提携`.",
                "Kết nối chuyển tàu/xe buýt dùng `乗り換え・接続・調整`."
            ],
            "source_ref": {"novel": "isekai", "chapter": 2, "lesson_id": "p1_c07_b03", "label": "Bộ 3 Isekai Ch.02 (Bài 16: Kinh tế)"}
        },
        # --- 問題7: 文の文法1 (33-44) ---
        {
            "num": 33,
            "mondai": "問題7：文の文法1",
            "mondai_vi": "Ngữ pháp câu N2",
            "prompt": "あの人が嘘をつく人だなんて、とても（　　）。きっと何かの誤解に違いない。",
            "prompt_vi": "Chuyện người đó là kẻ nói dối thì tôi chẳng tài nào tin nổi. Chắc chắn có sự hiểu lầm gì đó rồi.",
            "options": ["信じられないことだ", "信じかねない", "信じがたい", "信じようがないわけだ"],
            "ans": 3,
            "cute_right_msg": "Chuẩn 100 điểm!! `信じがたい` (V(ます) + がたい = thật khó lòng mà tin nổi) kết hợp câu sau 'chắc hẳn chỉ là hiểu nhầm' quá mượt! 💖",
            "right_exp": "`V(ます) + がたい`: Khó mà thực hiện nổi (chỉ cảm xúc/nhận thức như `信じがたい・許しがたい・想像しがたい`).",
            "cute_wrong_msg": "Ôn nhẹ mẫu từ chối khả năng tâm lý nhé: `信じる` → `信じがたい` = rất khó mà tin nổi! (Cẩn thận `信じかねない` nghĩa ngược thành 'có nguy cơ sẽ tin mất' đó nha!) 🌸",
            "wrong_exps": [
                "`信じられないことだ` (chuyện đó là điều không tin được) làm câu nặng và hơi lệch với chủ ngữ ngầm 'người nói khó tin' ở vế này so với `信じがたい` (và `ことだ` thường dùng cho lời khuyên).",
                "`〜かねない` mang nghĩa 'rất có nguy cơ sẽ xảy ra điều xấu' (`信じかねない` = không khéo lại tin sái cổ mất — ngược nghĩa!).",
                "Chính xác tuyệt đối! `とても信じがたい` = thật khó lòng mà tin được.",
                "`信じようがないわけだ` sai logic (`わけだ` = bảo sao hèn gì)."
            ],
            "source_ref": {"novel": "yandere", "chapter": 5, "lesson_id": "p2_c01_b01", "label": "Ngữ pháp N2 — 困難（〜がたい）"}
        },
        {
            "num": 34,
            "mondai": "問題7：文の文法1",
            "mondai_vi": "Ngữ pháp câu N2",
            "prompt": "母は年をとった（　　）、同じ話を何度も繰り返すようになった。",
            "prompt_vi": "Có lẽ tại vì mẹ đã có tuổi rồi hay sao ấy, mà gần đây mẹ bắt đầu lặp đi lặp lại cùng một câu chuyện nhiều lần.",
            "options": ["せいか", "うえで", "だけに", "あまり"],
            "ans": 1,
            "cute_right_msg": "Tinh tế quá!! `〜せいか` diễn tả nguyên nhân suy đoán nhẹ nhàng 'có lẽ là vì...' trước hiện tượng không mong muốn lắm! 🌸",
            "right_exp": "`〜せいか` (có lẽ tại vì...): Phỏng đoán nguyên nhân không chắc chắn lắm cho một kết quả tiêu cực/bất ngờ.",
            "cute_wrong_msg": "Xem sắc thái phỏng đoán khiêm tốn 'Chắc có lẽ tại có tuổi rồi hay sao mà mẹ hay nhắc lại 1 chuyện': không khẳng định gắt `だけに` hay `うえで`, mà chọn `せいか` nha em! 💕",
            "wrong_exps": [
                "Chính xác! `年をとったせいか` = chắc có lẽ do có tuổi rồi...",
                "`〜うえで` = sau khi làm X rồi mới làm Y (hành động có ý thức) hoặc 'trên phương diện...'.",
                "`〜だけに` = chính vì là sự thật X nên đương nhiên dẫn tới kết quả tương xứng mạnh hơn (`高価なだけに品質が良い`), không tự nhiên khi nói về mẹ già lặp lại chuyện.",
                "`〜あまり` = vì quá mức X (`嬉しさのあまり泣いた`), phải đi với danh từ cảm xúc hoặc Vる ở mức độ cực đoan."
            ],
            "source_ref": {"novel": "romcom", "chapter": 1, "lesson_id": "p1_c01_b01", "label": "Ngữ pháp N2 — 原因推量（〜せいか）"}
        },
        {
            "num": 35,
            "mondai": "問題7：文の文法1",
            "mondai_vi": "Ngữ pháp câu N2",
            "prompt": "自分の夢を諦めるくらいなら、どんなに苦しくても最後まで（　　）。",
            "prompt_vi": "Thà rằng chịu vất vả đến mấy mà tiếp tục tới cùng chứ nhất quyết không chịu từ bỏ ước mơ của mình.",
            "options": ["続けてみよう", "続けるべきではない", "続けるどころではない", "続けてはいられない"],
            "ans": 1,
            "cute_right_msg": "Đỉnh cao ý chí luôn!! Cấu trúc `A くらいなら B（ほうがましだ・Vよう）`: 'Thà làm B còn hơn phải chấp nhận A!' 🔥✨",
            "right_exp": "`V1る + くらいなら、V2`: Thà chọn làm V2 (dù khổ cực) còn hơn phải rơi vào tình cảnh tồi tệ V1 (`諦めるくらいなら、続けてみよう`).",
            "cute_wrong_msg": "Cấu trúc so sánh lựa chọn quyết liệt `A くらいなら B` = 'Nếu phải chịu cảnh từ bỏ ước mơ (A), thì thà rằng tôi cứ tiếp tục (B)!' đó em~ Chọn câu ý chí khẳng định `続けてみよう` nha! 💪",
            "wrong_exps": [
                "Chính xác! Thà cứ tiếp tục thử đến cùng còn hơn bỏ cuộc (`〜てみよう`).",
                "`べきではない` = không nên tiếp tục (ngược nghĩa hoàn toàn!).",
                "`どころではない` = chẳng phải lúc mà làm thế (ngược nghĩa).",
                "`〜てはいられない` = đứng ngồi không yên không thể tiếp tục mãi trạng thái đó."
            ],
            "source_ref": {"novel": "isekai", "chapter": 9, "lesson_id": "p2_c07_b01", "label": "Ngữ pháp N2 — 比較（〜くらいなら）"}
        },
        {
            "num": 36,
            "mondai": "問題7：文の文法1",
            "mondai_vi": "Ngữ pháp câu N2",
            "prompt": "この町は、春は桜、夏は花火大会（　　）、一年中観光客で賑わっている。",
            "prompt_vi": "Thị trấn này, hết mùa xuân hoa anh đào rồi mùa hè lễ hội pháo hoa, quanh năm suốt tháng lúc nào cũng tấp nập du khách.",
            "options": ["をはじめとして", "を契機として", "にわたって", "といったように"],
            "ans": 4,
            "cute_right_msg": "Chuẩn không cần chỉnh! `A、B といったように` = nào là A, nào là B như thế đó, khiến thị trấn quanh năm đông khách! 🎆🌸",
            "right_exp": "`A、B といったように`: Liệt kê những ví dụ tiêu biểu rồi khái quát lại bằng một đặc điểm chung phía sau (quanh năm đều náo nhiệt).",
            "cute_wrong_msg": "Xem hai ví dụ đại diện cho từng mùa trong năm (xuân có hoa anh đào, hè có pháo hoa...) rồi tóm lại 'quanh năm đông vui': mẫu liệt kê tổng quát là `といったように` nha em! 💡 (Nếu dùng `をはじめとして` thì vế trước thường chỉ nêu **1** ví dụ đứng đầu, kiểu `桜をはじめとして様々な花...`).",
            "wrong_exps": [
                "`〜をはじめとして` thường nêu một đối tượng dẫn đầu cho tập hợp cùng loại (`富士山をはじめ、日本の山々は...`), ít dùng sau cặp liệt kê song song `春は〜、夏は〜` như `といったように`.",
                "`を契機として` = lấy mốc biến cố làm bước ngoặt.",
                "`にわたって` = trải dài suốt khoảng thời gian/không gian (`3時間にわたって`).",
                "Chính xác tuyệt đối! `といったように` = như kiểu vậy đó."
            ],
            "source_ref": {"novel": "romcom", "chapter": 10, "lesson_id": "p1_c07_b01", "label": "Ngữ pháp N2 — 例示（〜といったように）"}
        },
        {
            "num": 37,
            "mondai": "問題7：文の文法1",
            "mondai_vi": "Ngữ pháp câu N2",
            "prompt": "今回の優勝は彼一人の力によるものではなく、チーム全員の努力の（　　）。",
            "prompt_vi": "Chức vô địch lần này không phải nhờ sức lực của một mình cậu ấy, mà chính là thành quả từ nỗ lực của toàn bộ đội ngũ.",
            "options": ["賜物（たまもの）だ", "末（すえ）だ", "あまりだ", "おそれだ"],
            "ans": 1,
            "cute_right_msg": "Đẳng cấp N1/N2 văn chương!! `努力の賜物（たまもの）だ` = thành quả xứng đáng kết tinh từ bao nỗ lực! 🏆✨",
            "right_exp": "`N + の賜物（たまもの）だ`: Là kết quả tốt đẹp, món quà xứng đáng gặt hái được nhờ nỗ lực, nghiên cứu hoặc sự hỗ trợ nào đó (`努力の賜物`).",
            "cute_wrong_msg": "Cụm kết câu kinh điển ca ngợi kết quả tốt đẹp nhờ cố gắng (`努力の結果`) trong văn viết trang trọng Nhật Bản là `努力の賜物（たまもの）だ` nha em! 🌟",
            "wrong_exps": [
                "Chính xác! `努力の賜物だ` = thành quả xứng đáng của sự nỗ lực.",
                "`末に` đi với động từ (`考え抜いた末に`), không kết câu bằng `努力の末だ` khi khen thành tựu chung như `賜物だ`.",
                "`あまり` mang nghĩa 'vì quá mức đến nỗi...', thường kết bằng `〜のあまり + V`.",
                "`おそれ` = nguy cơ xấu (ngược nghĩa hoàn toàn)."
            ],
            "source_ref": {"novel": "romcom", "chapter": 5, "lesson_id": "p1_c03_b01", "label": "Ngữ pháp N2 — 〜の賜物"}
        },
        {
            "num": 38,
            "mondai": "問題7：文の文法1",
            "mondai_vi": "Ngữ pháp câu N2",
            "prompt": "明日の面接試験（　　）、事前に志望動機をノートにまとめておいた。",
            "prompt_vi": "Hướng tới / chuẩn bị cho buổi phỏng vấn thi ngày mai, tôi đã tóm tắt sẵn lý do ứng tuyển vào sổ tay từ trước.",
            "options": ["に向けて", "について", "にかけて", "につれて"],
            "ans": 1,
            "cute_right_msg": "Phân biệt chuẩn đét 4 bạn hay nhầm `に向けて・について・にかけて・につれて`!! Hướng về mục tiêu tương lai có chuẩn bị là **に向けて**! 📝✨",
            "right_exp": "`N に向けて`: Hướng tới cột mốc/mục tiêu tương lai N để chuẩn bị hoặc nỗ lực (`試験・大会・卒業に向けて準備する`).",
            "cute_wrong_msg": "Coi bốn anh em siêu giống nhau nè em:\n- Chuẩn bị hướng tới sự kiện tương lai (`試験・面接・大会`) = **に向けて**!\n- Đề cập chủ đề = `について`.\n- Kéo dài từ mốc A tới B = `AからBにかけて`.\n- Biến đổi theo = `につれて`! 🌸",
            "wrong_exps": [
                "Chính xác! `面接試験に向けて準備する` = chuẩn bị hướng tới buổi phỏng vấn.",
                "`について` = về chủ đề... (dùng cho `話す・調べる・考える`).",
                "`にかけて` = khoảng từ... đến... hoặc lĩnh vực xuất sắc (`〜にかけては`).",
                "`につれて` đi sau Động từ (`Vるにつれて`)."
            ],
            "source_ref": {"novel": "romcom", "chapter": 8, "lesson_id": "p1_c05_b02", "label": "Ngữ pháp N2 — 目標（〜に向けて）"}
        },
        {
            "num": 39,
            "mondai": "問題7：文の文法1",
            "mondai_vi": "Ngữ pháp câu N2",
            "prompt": "この小説は、一度読み始めたら面白くて最後まで一気に読まず（　　）。",
            "prompt_vi": "Cuốn tiểu thuyết này hễ đã bắt đầu đọc một lần là hay đến nỗi không thể không đọc một lèo tới trang cuối cùng được.",
            "options": ["にはおかない", "にはいられない", "わけがない", "っこない"],
            "ans": 2,
            "cute_right_msg": "Xuất sắc 100 điểm!! Cặp ngữ pháp siêu hay thi `Vない + にはいられない` (tự nhiên không thể kiềm chế mà phải làm!) — phân biệt hoàn hảo với `Vずにはおかない` (tác động ngoại cảnh bắt người khác/môi trường phải...)! 📖💕",
            "right_exp": "`Vない(〜ず) + にはいられない`: Bản thân người đọc/chủ thể **không kìm lòng nổi**, tự nhiên phải làm hành động đó (`笑わずにはいられない・読まずにはいられない`). Chú ý: tiếp nối `ず` sẵn có trong `読まず` nối thẳng với `にはいられない`!",
            "cute_wrong_msg": "Ôi phân biệt cặp song sinh huyền thoại JLPT N2 này nhé em:\n- `〜ずにはいられない`: bản thân TỰ KÌM KHÔNG NỔI cảm xúc/hành động (`読まずにはいられない・泣かずにはいられない`).\n- `〜ずにはおかない`: vật gì hay ai đó QUYẾT KHÔNG ĐỂ YÊN / chắc chắn khiến người khác cảm thấy thế (VD: `読者を感動させずにはおかない`)! Ở đây chủ thể đọc một lèo chính là người đọc tự đọc → **読まずにはいられない**! 🌟",
            "wrong_exps": [
                "`〜ずにはおかない` mang sắc thái khách thể tác động khiến mọi người không thể không cảm nhận gì đó (VD: `見事な演技は観衆を感動させずにはおかない`), hoặc ý chí quyết tâm trả đũa ('tao sẽ không để yên!').",
                "Chính xác tuyệt đối! `読まずにはいられない` = không kìm được phải đọc một lèo hết luôn.",
                "`読まず＋わけがない` sai ngữ pháp tiếp nối (`Vる・ない＋わけがない`).",
                "`読まず＋っこない` sai tiếp nối (`Vます + っこない`)."
            ],
            "source_ref": {"novel": "romcom", "chapter": 5, "lesson_id": "p1_c03_b01", "label": "Ngữ pháp N2 — 衝動（〜ずにはいられない）"}
        },
        {
            "num": 40,
            "mondai": "問題7：文の文法1",
            "mondai_vi": "Ngữ pháp câu N2",
            "prompt": "彼のような優れた才能の持ち主にしてみれば、これくらいの問題は簡単なこと（　　）だろう。",
            "prompt_vi": "Đứng trên góc độ một người sở hữu tài năng xuất chúng như cậu ấy mà xét, bài toán cỡ này chắc cũng chỉ là chuyện nhỏ dễ như ăn kẹo thôi.",
            "options": ["にすぎない", "にわたる", "にたえない", "にこたえる"],
            "ans": 1,
            "cute_right_msg": "Quá mượt!! `〜にすぎない` = chỉ là... mà thôi (mang nghĩa đánh giá xem nhẹ chuyện gì trước tài năng lớn)! 🌟",
            "right_exp": "`N / V普通形 + にすぎない`: Chẳng qua chỉ là X mà thôi (không đáng kể là gì cả).",
            "cute_wrong_msg": "Đọc trọn câu nè em: 'Đối với thiên tài như cậu ta, bài toán cỡ này chắc chẳng qua chỉ là chuyện đơn giản (`簡単なことにすぎない`) thôi' — mẫu 'chỉ là...' trong N2 là `にすぎない` nhé! 💡",
            "wrong_exps": [
                "Chính xác! `簡単なことにすぎないだろう` = chắc chẳng qua chỉ là chuyện nhỏ thôi.",
                "`にわたる` = kéo dài trên phạm vi (`長年にわたる`).",
                "`にたえない` = vô cùng cảm kích/không chịu đựng nổi (`感謝にたえない・見るにたえない`).",
                "`にこたえる` = đáp lại kỳ vọng/yêu cầu (`期待にこたえる`)."
            ],
            "source_ref": {"novel": "isekai", "chapter": 6, "lesson_id": "p1_c09_b01", "label": "Ngữ pháp N2 — 限定評価（〜にすぎない）"}
        },
        {
            "num": 41,
            "mondai": "問題7：文の文法1",
            "mondai_vi": "Ngữ pháp câu N2",
            "prompt": "彼女は忙しい仕事の合間を（　　）、毎日ボランティア活動に参加している。",
            "prompt_vi": "Tranh thủ xen kẽ giữa khoảng thời gian trống hiếm hoi của công việc bận rộn, ngày nào cô ấy cũng tham gia hoạt động tình nguyện.",
            "options": ["ぬって", "こめて", "あけて", "おいて"],
            "ans": 1,
            "cute_right_msg": "OHHH!! Quán dụng ngữ N2 cao cấp `合間（あいま）を縫（ぬ）って` (tranh thủ từng khe hở thời gian ít ỏi trong lịch trình bận rộn)! 🧵⏰",
            "right_exp": "`時間の合間（あいま）を縫（ぬ）って`: Len lỏi, tận dụng từng khoảng trống thời gian hiếm hoi giữa lúc bận rộn để làm việc có ý nghĩa.",
            "cute_wrong_msg": "Cụm kết hợp cố định cực hay thi N2 này em phải bỏ túi ngay nhé: `仕事の合間を縫（ぬ）って` (khâu vá/luồn lách qua kẽ hở thời gian bận rộn)! ✨",
            "wrong_exps": [
                "Chính xác tuyệt đối! `仕事の合間を縫って` = tranh thủ khoảng thời gian trống hiếm hoi.",
                "`心を込めて` là gửi gắm tâm tư tình cảm (không đi với `合間`).",
                "`時間を空けて` là chừa thời gian trống, không dùng cụm cố định `合間を空けて`.",
                "`を置いて` không dùng với `合間`."
            ],
            "source_ref": {"novel": "romcom", "chapter": 8, "lesson_id": "p1_c05_b02", "label": "Ngữ pháp & Quán dụng N2 — 合間を縫って"}
        },
        {
            "num": 42,
            "mondai": "問題7：文の文法1",
            "mondai_vi": "Ngữ pháp câu N2",
            "prompt": "事故の原因がはっきりしない（　　）、この機械を再び動かすわけにはいかない。",
            "prompt_vi": "Chừng nào nguyên nhân vụ tai nạn vẫn chưa được làm rõ, thì chừng đó chúng tôi không thể cho cỗ máy này vận hành trở lại được.",
            "options": ["ものだから", "うちは", "どころか", "ものなら"],
            "ans": 2,
            "cute_right_msg": "Tuyệt vời!! `〜ないうちは〜ない` = 'Chừng nào vẫn chưa X thì chưa thể Y' (giới hạn điều kiện thời gian)! ⛔⚙️",
            "right_exp": "`Vない + うちは〜ない`: Trong khi trạng thái chưa đạt được X vẫn tiếp diễn (chừng nào còn chưa...), thì không thể làm Y.",
            "cute_wrong_msg": "Chú ý vế trước chia phủ định `はっきりしない` và vế sau chỉ quy tắc an toàn kỹ thuật: 'Chừng nào nguyên nhân còn chưa rõ thì chưa thể chạy lại máy' → chọn `〜ないうちは` nha em! 🌸",
            "wrong_exps": [
                "`ものだから` giải thích nguyên nhân mang tính biện hộ cá nhân văn nói, không hợp với quy tắc an toàn kỹ thuật `わけにはいかない`.",
                "Chính xác! `はっきりしないうちは` = chừng nào còn chưa sáng tỏ thì...",
                "`どころか` = đừng nói là..., trái lại còn...",
                "`ものなら` = nếu lỡ mà / giá mà..."
            ],
            "source_ref": {"novel": "isekai", "chapter": 5, "lesson_id": "p1_c08_b02", "label": "Ngữ pháp N2 — 時間・条件（〜ないうちは）"}
        },
        {
            "num": 43,
            "mondai": "問題7：文の文法1",
            "mondai_vi": "Ngữ pháp câu N2",
            "prompt": "彼女は普段はとても控えめだが、一度ピアノの前に座る（　　）、まるで別人のように情熱的に演奏する。",
            "prompt_vi": "Cô ấy bình thường rất khiêm tốn nhút nhát, ấy thế mà một khi đã ngồi xuống trước cây đàn piano thì liền hóa thành một người khác chơi đàn đầy nhiệt huyết.",
            "options": ["とあって", "となると", "にしたって", "ときたら"],
            "ans": 2,
            "cute_right_msg": "ĐỈNH!! `一度〜となると` (một khi đã nhắc đến / bước vào trạng thái đó là lập tức biến đổi hẳn)! 🎹🔥",
            "right_exp": "`N / Vる + となると`: Một khi đã rơi vào tình huống/vai trò X thì đương nhiên dẫn đến thái độ/kết quả khác hẳn Y.",
            "cute_wrong_msg": "Chú ý sự lột xác 'bình thường rụt rè ↔ hễ bước vào vị trí ngồi bên phím đàn là khác hẳn': dùng `〜となると` (cũng tương tự `となると / となれば` = một khi đã lâm vào tình cảnh đó) nha em! ✨",
            "wrong_exps": [
                "`とあって` = vì lý do hoàn cảnh đặc biệt đó nên... (`連休とあって混雑している`).",
                "Chính xác! `ピアノの前に座るとなると` = hễ mà đã ngồi trước đàn piano là...",
                "`にしたって` = dù cho là... đi chăng nữa.",
                "`ときたら` = nói đến ai đó là bực/ngán ngẩm (mang nghĩa phàn nàn)."
            ],
            "source_ref": {"novel": "romcom", "chapter": 5, "lesson_id": "p1_c03_b01", "label": "Ngữ pháp N2 — 条件変化（〜となると）"}
        },
        {
            "num": 44,
            "mondai": "問題7：文の文法1",
            "mondai_vi": "Ngữ pháp câu N2",
            "prompt": "日本へ留学する（　　）、まず日本の歴史や生活習慣について本を読んで調べておきたい。",
            "prompt_vi": "Trước thềm du học Nhật Bản, trước tiên tôi muốn đọc sách tìm hiểu sẵn về lịch sử và tập quán sinh hoạt của Nhật.",
            "options": ["にあたり", "において", "にわたって", "に沿って"],
            "ans": 1,
            "cute_right_msg": "Quá chuẩn! `N / Vる + にあたり` (nhân dịp bắt đầu cột mốc quan trọng!) siêu trang trọng và chuẩn văn phong N2! ✈️🎌",
            "right_exp": "`N / Vる + にあたり（にあたって）`: Nhân dịp sắp tiến hành một sự kiện lớn/bước ngoặt quan trọng (như nhập học, khai mạc, kết hôn, du học).",
            "cute_wrong_msg": "Bình tĩnh nè em: chuẩn bị sẵn tâm thế trước khi bước vào một sự kiện trọng đại (`日本へ留学する〜`) là mẫu `にあたり` đó! 🌸",
            "wrong_exps": [
                "Chính xác tuyệt đối! `留学するにあたり` = nhân dịp sắp sang Nhật du học.",
                "`において` chỉ địa điểm/lĩnh vực/thời điểm diễn ra sự việc ('tại...'), không mang sắc thái chuẩn bị cho cột mốc sắp tới.",
                "`にわたって` = trải dài suốt quãng thời gian/không gian.",
                "`に沿って` = tuân theo, men theo đường/chính sách."
            ],
            "source_ref": {"novel": "romcom", "chapter": 7, "lesson_id": "p1_c05_b01", "label": "Ngữ pháp N2 — 機会（〜にあたり）"}
        },
        # --- 問題8: 文の文法2 ★ (45-49) ---
        {
            "num": 45,
            "mondai": "問題8：文の文法2 ★",
            "mondai_vi": "Sắp xếp thành phần câu",
            "prompt": "この街の祭りが毎年人々を惹きつけるのは、衣装の ＿＿＿ ＿＿＿ ★ ＿＿＿ 魅力があるからだ。",
            "prompt_vi": "Lý do lễ hội thị trấn này năm nào cũng thu hút mọi người, không chỉ bởi vẻ đẹp của trang phục mà còn có sức hút ở bầu không khí nhiệt huyết bao trùm khắp hội trường.",
            "options": ["美しさも", "さることながら", "会場を包む", "熱気に"],
            "ans": 3,
            "cute_right_msg": "Tuyệt đỉnh!! `[1] 美しさも → [2] さることながら → ★[3] 会場を包む → [4] 熱気に`! 🏮🎉",
            "right_exp": "Ghép chuẩn xác: `衣装の [1]美しさも [2]さることながら ★[3]会場を包む [4]熱気に 魅力があるからだ。`\n- `衣装の` nối với danh từ `[1]美しさも`.\n- `[1]美しさも` đi liền với `[2]さることながら` ('đã đẹp khỏi bàn rồi, nhưng còn...').\n- `[3]会場を包む` bổ nghĩa cho danh từ `[4]熱気に` (nhiệt huyết bao trùm lễ hội) + `魅力があるからだ`.\n→ Vị trí dấu ★ là **3 (`会場を包む`)**!",
            "cute_wrong_msg": "Coi trợ từ `の` ngay trước ô 1 (`衣装の`) nhé em: sau `の` chỉ có mỗi `[1] 美しさも` vừa khít, rồi kéo thẳng sang `[2] さることながら`! Hai ô cuối là mệnh đề định ngữ `[3] 会場を包む + [4] 熱気に`! 🧩",
            "wrong_exps": [
                "`[1] 美しさも` đứng ở ô số 1 (sau `衣装の`).",
                "`[2] さることながら` đứng ở ô số 2.",
                "Chính xác tuyệt đối! Vị trí ★ là `[3] 会場を包む` (`1 → 2 → 3 → 4`).",
                "`[4] 熱気に` đứng ở ô số 4 (`熱気に魅力がある`)."
            ],
            "source_ref": {"novel": "romcom", "chapter": 10, "lesson_id": "p1_c07_b01", "label": "Ngữ pháp N2 ★ — 〜もさることながら"}
        },
        {
            "num": 46,
            "mondai": "問題8：文の文法2 ★",
            "mondai_vi": "Sắp xếp thành phần câu",
            "prompt": "どれほど最新の機械が導入された ＿＿＿ ＿＿＿ ★ ＿＿＿ 決して変わらない。",
            "prompt_vi": "Dẫu cho máy móc tối tân đến mức nào có được đưa vào sử dụng đi chăng nữa, tầm quan trọng của sự ấm áp từ bàn tay con người tạo nên vẫn chẳng bao giờ đổi thay.",
            "options": ["ところで、", "人の手で", "大切さは", "作る温かみの"],
            "ans": 4,
            "cute_right_msg": "Đẹp từng milimet!! `[1] ところで、 → [2] 人の手で → ★[4] 作る温かみの → [3] 大切さは`! 🤖✋💖",
            "right_exp": "Ghép chuẩn xác: `導入された [1]ところで、 [2]人の手で ★[4]作る温かみの [3]大切さは 決して変わらない。`\n- `導入された` (Vた) nối ngay vào `[1]ところで、` (`どれほど〜Vたところで`: dẫu có làm thế nào đi nữa thì vẫn...).\n- `[2]人の手で` bổ nghĩa cho động từ `[4]作る温かみの` (sự ấm áp được tạo nên bằng bàn tay con người).\n- `温かみの` nối với danh từ `[3]大切さは` làm chủ ngữ cho `決して変わらない`.\n→ Vị trí dấu ★ là **4 (`作る温かみの`)**!",
            "cute_wrong_msg": "Tìm từ khóa `どれほど〜た` ở vế đầu nha em! Cấu trúc `どれほど〜たところで` đặt ngay `[1] ところで、` ở ô 1! Tiếp theo nối cụm danh từ dài `[2] 人の手で → [4] 作る温かみの → [3] 大切さは`! 🌸",
            "wrong_exps": [
                "`[1] ところで、` đứng ở ô số 1 (kết thúc mệnh đề `どれほど〜導入されたところで`).",
                "`[2] 人の手で` đứng ở ô số 2.",
                "`[3] 大切さは` đứng ở ô số 4 (làm chủ ngữ cho `決して変わらない`).",
                "Chính xác tuyệt đối! Vị trí ★ là `[4] 作る温かみの` (`1 → 2 → 4 → 3`)."
            ],
            "source_ref": {"novel": "isekai", "chapter": 5, "lesson_id": "p1_c08_b02", "label": "Ngữ pháp N2 ★ — 〜たところで"}
        },
        {
            "num": 47,
            "mondai": "問題8：文の文法2 ★",
            "mondai_vi": "Sắp xếp thành phần câu",
            "prompt": "先生に一度注意されたくらいで ＿＿＿ ＿＿＿ ★ ＿＿＿ いつまでも前に進めないよ。",
            "prompt_vi": "Mới bị thầy cô nhắc nhở có một lần mà cứ mãi ủ rũ chán nản như vậy thì làm sao tiến lên phía trước được chứ.",
            "options": ["落ち込んで", "ばかり", "いるよう", "では、"],
            "ans": 3,
            "cute_right_msg": "Quá mượt!! `[1] 落ち込んで → [2] ばかり → ★[3] いるよう → [4] では、` (`Vてばかりいるようでは`)! 💪✨",
            "right_exp": "Ghép chuẩn xác: `注意されたくらいで [1]落ち込んで [2]ばかり ★[3]いるよう [4]では、 いつまでも前に進めないよ。`\n- `[1]落ち込んで` + `[2]ばかり` + `[3]いる` = mẫu `Vてばかりいる` (lúc nào cũng chỉ toàn ủ rũ).\n- `いるよう` + `[4]では、` = mẫu `〜ようでは` (nếu tình trạng cứ tệ thế này mãi thì...).\n→ Vị trí dấu ★ là **3 (`いるよう`)**!",
            "cute_wrong_msg": "Nhìn công thức kép trong câu nè em: `〜て + ばかり + いる` kết hợp cùng `〜よう + では`! Ghép 4 mảnh vào đúng thứ tự 1-2-3-4 liền ha~ 🌸",
            "wrong_exps": [
                "`[1] 落ち込んで` đứng ở ô số 1.",
                "`[2] ばかり` đứng ở ô số 2 (`落ち込んでばかり`).",
                "Chính xác tuyệt đối! Vị trí ★ là `[3] いるよう` (`1 → 2 → 3 → 4`).",
                "`[4] では、` đứng ở ô số 4 (`ようでは`)."
            ],
            "source_ref": {"novel": "romcom", "chapter": 7, "lesson_id": "p1_c05_b01", "label": "Ngữ pháp N2 ★ — 〜てばかりいるようでは"}
        },
        {
            "num": 48,
            "mondai": "問題8：文の文法2 ★",
            "mondai_vi": "Sắp xếp thành phần câu",
            "prompt": "この地域の自然環境を守るためには、住民一人一人が ＿＿＿ ＿＿＿ ★ ＿＿＿ 必要がある。",
            "prompt_vi": "Để bảo vệ môi trường tự nhiên khu vực này, mỗi người dân đều cần phải mang ý thức cao độ để hành động.",
            "options": ["意識を", "行動する", "持って", "高い"],
            "ans": 3,
            "cute_right_msg": "Chuẩn không cần chỉnh!! `[4] 高い → [1] 意識を → ★[3] 持って → [2] 行動する` (`必要がある`)! 🌍🌿",
            "right_exp": "Ghép chuẩn xác: `住民一人一人が [4]高い [1]意識を ★[3]持って [2]行動する 必要がある。`\n- `[4]高い` (tính từ đuôi い) đứng trước danh từ `[1]意識を`.\n- `[1]意識を` làm tân ngữ cho `[3]持って` (`意識を持って`).\n- Hành động tiếp theo là `[2]行動する` đứng ngay trước `必要がある`.\n→ Vị trí dấu ★ là **3 (`持って`)**!",
            "cute_wrong_msg": "Bắt cặp tính từ + danh từ `[4] 高い + [1] 意識を`, rồi tới động từ `[3] 持って` (mang ý thức) và kết trước `必要がある` bằng `[2] 行動する` nha em! 💡",
            "wrong_exps": [
                "`[1] 意識を` đứng ở ô số 2 (sau tính từ `高い`).",
                "`[2] 行動する` đứng ở ô số 4 (ngay trước `必要がある`).",
                "Chính xác tuyệt đối! Vị trí ★ là `[3] 持って` (`4 → 1 → 3 → 2`).",
                "`[4] 高い` đứng ở ô số 1."
            ],
            "source_ref": {"novel": "isekai", "chapter": 4, "lesson_id": "p1_c08_b01", "label": "Ngữ pháp N2 ★ — 修飾関係"}
        },
        {
            "num": 49,
            "mondai": "問題8：文の文法2 ★",
            "mondai_vi": "Sắp xếp thành phần câu",
            "prompt": "あの小説は映画化されるや ＿＿＿ ＿＿＿ ★ ＿＿＿ 大ベストセラーになった。",
            "prompt_vi": "Cuốn tiểu thuyết kia ngay vừa mới được chuyển thể thành phim là lập tức bán hết veo khỏi quầy kệ hiệu sách và trở thành tác phẩm bán chạy nhất.",
            "options": ["書店の", "売り切れるほど", "否や、", "店頭から"],
            "ans": 4,
            "cute_right_msg": "SIÊU ĐỈNH!! `[3] 否や、 → [1] 書店の → ★[4] 店頭から → [2] 売り切れるほど`! (`〜や否や`: ngay vừa mới... là lập tức...) 📚🎬",
            "right_exp": "Ghép chuẩn xác: `映画化されるや [3]否や、 [1]書店の ★[4]店頭から [2]売り切れるほど 大ベストセラーになった。`\n- `映画化されるや` gắn trực tiếp vào `[3]否や、` (`Vる＋や否や`: ngay vừa mới V là lập tức...).\n- Tiếp theo: `[1]書店の` + `[4]店頭から` (từ quầy trưng bày của hiệu sách) + `[2]売り切れるほど` (đến mức cháy hàng rồi thành bestseller).\n→ Vị trí dấu ★ là **4 (`店頭から`)**!",
            "cute_wrong_msg": "Thấy chữ `されるや` ngay trước ô 1 là bật ngay phản xạ chọn `[3] 否や、` (`Vるや否や` = vừa mới... xong thì ngay tức khắc)! Sau đó ghép cụm `[1] 書店の + [4] 店頭から + [2] 売り切れるほど` nhé em! 🌟",
            "wrong_exps": [
                "`[1] 書店の` đứng ở ô số 2.",
                "`[2] 売り切れるほど` đứng ở ô số 4 (bổ nghĩa mức độ cho `大ベストセラー`).",
                "`[3] 否や、` đứng ngay ô số 1 (`映画化されるや否や`).",
                "Chính xác tuyệt đối! Vị trí ★ là `[4] 店頭から` (`3 → 1 → 4 → 2`)."
            ],
            "source_ref": {"novel": "romcom", "chapter": 9, "lesson_id": "p1_c06_b01", "label": "Ngữ pháp N2 ★ — 〜や否や"}
        },
        # --- 問題9: 文章の文法 (50-54) ---
        {
            "num": 50,
            "mondai": "問題9：文章の文法",
            "mondai_vi": "Ngữ pháp đoạn văn (Điền khuyết bài đọc)",
            "passage": PASSAGE_EXAM3,
            "passage_vi": PASSAGE_EXAM3_VI,
            "prompt": "空欄（　50　）に入る最もよいものを一つ選びなさい。\n「そのため、使い捨てプラスチック製品の製造や販売を法律で（　50　）国々も増えてきた。」",
            "prompt_vi": "Chọn đáp án đúng nhất điền vào chỗ trống (50): 'Chính vì thế, ngày càng có nhiều quốc gia quy định cấm/hạn chế sản xuất và bán các sản phẩm nhựa dùng một lần bằng pháp luật.'",
            "options": ["禁止するしかない", "禁止しようとする", "禁止させたがる", "禁止される"],
            "ans": 2,
            "cute_right_msg": "Quá chuẩn!! `〜ようとする国々も増えてきた` (nhiều nước đang nỗ lực cố gắng/hướng tới cấm... bằng luật)! 🌍🌿",
            "right_exp": "`Vようとする`: Cố gắng thực hiện / đang hướng tới hành động V (`法律で禁止しようとする国々` = các quốc gia đang nỗ lực cấm bằng luật).",
            "cute_wrong_msg": "Nhìn chủ ngữ đứng sau danh từ: `国々も増えてきた` (những quốc gia đang...). Không dùng `しかない` (chỉ còn mỗi cách) hay `させたがる` (muốn bắt ai làm), mà là các nước đang **nỗ lực tiến tới cấm** (`禁止しようとする`) nha em! 🌱",
            "wrong_exps": [
                "`〜しかない` ghép trực tiếp danh từ `〜しかない国々` (các nước chẳng còn cách nào khác ngoài cấm) mang nghĩa bị ép quá mức và lệch phong cách khách quan của báo chí.",
                "Chính xác! `法律で禁止しようとする国々` = các quốc gia đang hướng tới việc cấm bằng pháp luật.",
                "`させたがる` = tỏ vẻ muốn bắt ai làm gì (không hợp với chủ ngữ trừu tượng `国々`).",
                "`禁止される国々` sai vai bị động ('các quốc gia bị cấm'!)."
            ],
            "source_ref": {"novel": "isekai", "chapter": 4, "lesson_id": "p1_c08_b01", "label": "Ngữ pháp N2 — 意志・試み（〜ようとする）"}
        },
        {
            "num": 51,
            "mondai": "問題9：文章の文法",
            "mondai_vi": "Ngữ pháp đoạn văn (Điền khuyết bài đọc)",
            "passage": PASSAGE_EXAM3,
            "passage_vi": PASSAGE_EXAM3_VI,
            "prompt": "空欄（　51　）に入る最もよいものを一つ選びなさい。\n「私たちの便利さへの追求こそが、結果としてこれほど多くのごみを（　51　）からである。」",
            "prompt_vi": "Chọn đáp án đúng nhất điền vào chỗ trống (51): 'Bởi lẽ chính sự theo đuổi tiện lợi của chúng ta hệ quả đã dẫn đến việc tạo ra ngần ấy rác thải.'",
            "options": ["生み出してしまった", "生み出さずにすんだ", "生み出すはずがなかった", "生み出しかねている"],
            "ans": 1,
            "cute_right_msg": "Chuẩn bài đọc JLPT!! `生み出してしまった` diễn tả kết quả tiêu cực lỡ tạo ra quá nhiều rác thải mà con người không mong muốn! ♻️",
            "right_exp": "`Vてしまった`: Kết quả không mong muốn xảy ra xong rồi ('đã trót tạo ra ngần ấy rác thải'), ăn khớp hoàn toàn với từ `結果として`.",
            "cute_wrong_msg": "Đọc kỹ giọng điệu tự kiểm điểm đáng tiếc (`結果としてこれほど多くのごみを...`): kết cục đáng tiếc đã xảy ra rồi dùng `〜てしまった` nha em! 🌸",
            "wrong_exps": [
                "Chính xác! `生み出してしまった` = đã lỡ tạo ra (kết quả tiêu cực đáng tiếc).",
                "`〜ずにすむ` = tránh khỏi không cần phải làm (ngược nghĩa hoàn toàn).",
                "`はずがなかった` = không đời nào tạo ra (mâu thuẫn thực tế).",
                "`かねている` = đang lúng túng khó lòng làm được (sai ngữ nghĩa)."
            ],
            "source_ref": {"novel": "isekai", "chapter": 4, "lesson_id": "p1_c08_b01", "label": "Ngữ pháp N2 — 完了・残念（〜てしまう）"}
        },
        {
            "num": 52,
            "mondai": "問題9：文章の文法",
            "mondai_vi": "Ngữ pháp đoạn văn (Điền khuyết bài đọc)",
            "passage": PASSAGE_EXAM3,
            "passage_vi": PASSAGE_EXAM3_VI,
            "prompt": "空欄（　52　）に入る最もよいものを一つ選びなさい。\n「買い物の際にマイバッグを持参する（　52　）、小さな行動の積み重ねが大きな変化につながる。」",
            "prompt_vi": "Chọn đáp án đúng nhất điền vào chỗ trống (52): 'Chẳng hạn như việc mang theo túi cá nhân khi đi mua sắm, sự tích lũy những hành động nhỏ dẫn đến thay đổi lớn.'",
            "options": ["どころか", "ものの", "などといった", "にもかかわらず"],
            "ans": 3,
            "cute_right_msg": "Quá mượt!! `〜などといった、小さな行動` (những hành động nhỏ như thế — ví dụ điển hình liên kết danh từ)! 🛍️💚",
            "right_exp": "`Vる + などといった + N`: Đưa ra ví dụ điển hình trước danh từ khái quát `N` ('những hành động nhỏ như là...').",
            "cute_wrong_msg": "Đằng trước (52) nêu ví dụ `mang túi vải cá nhân khi đi chợ`, ngay sau (52) gọi tên nhóm `những hành động nhỏ` → nối ví dụ với danh từ tổng quát dùng `などといった` nha em! ✨",
            "wrong_exps": [
                "`どころか` là phủ định/so sánh vượt mức, không nối ví dụ với nhóm chung.",
                "`ものの` = tuy rằng nhưng (nhượng bộ).",
                "Chính xác tuyệt đối! `マイバッグを持参するなどといった、小さな行動`.",
                "`にもかかわらず` = bất chấp (nghịch tiếp)."
            ],
            "source_ref": {"novel": "isekai", "chapter": 4, "lesson_id": "p1_c08_b01", "label": "Ngữ pháp N2 — 例示（〜などといった）"}
        },
        {
            "num": 53,
            "mondai": "問題9：文章の文法",
            "mondai_vi": "Ngữ pháp đoạn văn (Điền khuyết bài đọc)",
            "passage": PASSAGE_EXAM3,
            "passage_vi": PASSAGE_EXAM3_VI,
            "prompt": "空欄（　53　）に入る最もよいものを一つ選びなさい。\n「将来の世代に美しい地球を残す（　53　）、今の生活スタイルを見直す時期が来ている。」",
            "prompt_vi": "Chọn đáp án đúng nhất điền vào chỗ trống (53): 'Vì để lưu giữ lại cho thế hệ tương lai một Trái Đất tươi đẹp, đã đến lúc xem xét lại lối sống hiện nay.'",
            "options": ["ためにも", "せいでも", "わけにも", "ものの"],
            "ans": 1,
            "cute_right_msg": "Chuẩn không cần chỉnh! `Vる + ためにも` = 'cũng vì mục đích cao đẹp đó mà...'! 🌏✨",
            "right_exp": "`Vる + ため（に）も`: Nhấn mạnh mục đích đáng hướng tới ('cũng là để cho...').",
            "cute_wrong_msg": "Xem quan hệ mục đích-hành động ở câu này: mục đích là giữ Trái Đất đẹp cho tương lai → dùng `ためにも` (vì mục đích đó nữa mà hãy xem lại lối sống)! 🌱",
            "wrong_exps": [
                "Chính xác! `残すためにも` = để giữ lại... cũng vì thế mà...",
                "Không có cấu trúc `Vる＋せいでも` cho mục đích tương lai.",
                "Không tồn tại `わけにも` kiểu này (`〜わけにもいかない` nghĩa khác).",
                "`ものの` = tuy vậy nhưng."
            ],
            "source_ref": {"novel": "isekai", "chapter": 4, "lesson_id": "p1_c08_b01", "label": "Ngữ pháp N2 — 目的（〜ためにも）"}
        },
        {
            "num": 54,
            "mondai": "問題9：文章の文法",
            "mondai_vi": "Ngữ pháp đoạn văn (Điền khuyết bài đọc)",
            "passage": PASSAGE_EXAM3,
            "passage_vi": PASSAGE_EXAM3_VI,
            "prompt": "空欄（　54　）に入る最もよいものを一つ選びなさい。\n「今の生活スタイルを見直す時期が来ているの（　54　）。」",
            "prompt_vi": "Chọn đáp án đúng nhất điền vào chỗ trống (54): '...chẳng phải đã đến lúc chúng ta nhìn nhận lại lối sống hiện nay hay sao.'",
            "options": ["にすぎない", "ではないだろうか", "はずがない", "とばかりに"],
            "ans": 2,
            "cute_right_msg": "HOÀN HẢO!! Khép lại cả 3 đề thi thử bằng câu kết văn phong xã luận kinh điển nhất mọi kỳ thi JLPT: `〜のではないだろうか` (chẳng phải là... hay sao)! 🏆🎊",
            "right_exp": "`〜のではないだろうか`: Câu hỏi tu từ mang sắc thái khẳng định lịch sự, thuyết phục độc giả đồng tình ở câu kết bài tiểu luận/nghị luận JLPT N2 ('Chẳng phải đã đến lúc... hay sao?').",
            "cute_wrong_msg": "Lưu ý chữ `の` đứng ngay trước (54) và giọng văn kết bài kêu gọi suy ngẫm đầy sức thuyết phục nhé em: `〜の + ではないだろうか` chính là câu chốt bài kinh điển nhất trong Mondai 9 JLPT luôn đó! 🌸✨",
            "wrong_exps": [
                "`〜にすぎない` hạ thấp tầm quan trọng ('chỉ là thôi') — mâu thuẫn tính cấp thiết của bảo vệ môi trường, và cũng không nối sau chữ `の` kiểu `来ているのにすぎない`.",
                "Chính xác tuyệt đối! `〜のではないだろうか` = chẳng phải... hay sao.",
                "`来ているのはずがない` vừa sai ngữ pháp chữ `の`, vừa sai nghĩa ('không đời nào đã đến lúc').",
                "`とばかりに` dùng nối giữa câu miêu tả biểu cảm, không đứng kết bài sau `の`."
            ],
            "source_ref": {"novel": "isekai", "chapter": 12, "lesson_id": "p2_c07_b04", "label": "Ngữ pháp N2 — 断定の緩和（〜のではないだろうか）"}
        },
    ]
}
