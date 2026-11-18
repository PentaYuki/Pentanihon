# -*- coding: utf-8 -*-
"""
3 Bộ Đề Ôn Tập Chuẩn JLPT Theo Từng Bộ Tiểu Thuyết (20 câu mỗi bộ — 20 phút):
- review-romcom: Tổng ôn 13 Bài (314 từ) trong Bộ 1 Romcom
- review-yandere: Tổng ôn 12 Bài (233 từ) trong Bộ 2 Yandere
- review-isekai: Tổng ôn 12 Bài (233 từ) trong Bộ 3 Isekai
"""

EXAM_REVIEW_ROMCOM = {
    "id": "review-romcom",
    "code": "ÔN TẬP BỘ 1 • ROMCOM N2",
    "title_jp": "【Romcom復習テスト】桜色キッチンと契約同居の全語彙（20問）",
    "title_vi": "Đề Ôn Tập Nhanh Bộ 1: Romcom (13 Bài • 20 Câu Chuẩn JLPT)",
    "category": "review",
    "novel_id": "romcom",
    "duration_min": 20,
    "pass_score": 12,
    "max_score": 20,
    "description": "Bài kiểm tra tổng ôn toàn bộ 13 bài học Shinkanzen N2 (Gia đình, Tính cách, Ẩm thực, Việc nhà, Sở thích, Trường học, Công việc, Truyền thông, Lễ hội, Đa nghĩa, Quán dụng ngữ) lồng theo cốt truyện Romcom của Kenji & Misaki.",
    "yuki_note_start": "Chúc mừng em đã đọc qua **Bộ 1 Romcom** cùng cặp đôi gà bông Kenji & Misaki nè~ 💕 Bài test nhanh 20 câu này sẽ quét sạch sẽ đủ 13 bài trong bộ Romcom xem em nhớ hết các mẹo nhà bếp, công sở và quán dụng ngữ chưa đó nha! Cố lên nè 🌸",
    "yuki_note_finish_pass": "Quá siêu!! Ngôn tình Romcom vừa ngọt mà từ vựng Shinkanzen trong đầu em cũng chắc nịch luôn ha~ Tiếp tục giữ lửa sang thử thách Bộ 2 hoặc Đề Full JLPT nhé! 💖🎉",
    "yuki_note_finish_try": "Hihi không sao đâu em ơi~ Vừa mới cày xong tận 314 từ ở Bộ 1 nên quên vài chữ là bình thường lắm luôn! Em bấm xem giải thích từng câu rồi ghé lại chương tiểu thuyết tương ứng đọc lại 1 phút là nhớ rụp hà 🌸💪",
    "questions": [
        {
            "num": 1,
            "mondai": "問題1：漢字読み",
            "mondai_vi": "Cách đọc Kanji",
            "prompt": "料理の味を良くするために、スープを弱火でじっくり<u>煮込んだ</u>。",
            "prompt_vi": "Để món ăn thêm ngon đậm đà, tôi đã hầm ninh súp từ từ trên lửa nhỏ.",
            "options": ["にこんだ", "やきこんだ", "むしこんだ", "いためこんだ"],
            "ans": 1,
            "cute_right_msg": "Chuẩn bài đầu bếp Kenji!! `煮込む（にこむ）` = hầm nhừ cho ngấm gia vị! 🍲✨",
            "right_exp": "`煮込む（にこむ）` đọc là **にこむ** (Ninh / Chử + Nhập: ninh kỹ cho thấm vị).",
            "cute_wrong_msg": "Bí kíp Bếp nhà Kenji (Romcom Ch.03): nấu súp/cà ri lửa nhỏ cho nhừ ngấm vị dùng động từ **煮込む（にこむ）** nha em! 🥕",
            "wrong_exps": [
                "Chính xác! `煮込（にこ）む` = hầm, ninh nhừ.",
                "`やく` là chữ `焼く` (nướng/áp chảo).",
                "`むす` là chữ `蒸す` (hấp cách thủy).",
                "`いためる` là chữ `炒める` (xào)."
            ],
            "source_ref": {"novel": "romcom", "chapter": 3, "lesson_id": "p1_c02_b01", "label": "Bộ 1 Romcom Ch.03 (Ẩm thực)"}
        },
        {
            "num": 2,
            "mondai": "問題2：表記",
            "mondai_vi": "Chọn Kanji đúng",
            "prompt": "彼女はどんなに失敗しても<u>れいせい</u>な態度を失わなかった。",
            "prompt_vi": "Cô ấy dù thất bại thế nào cũng không hề đánh mất thái độ điềm tĩnh sáng suốt.",
            "options": ["礼正", "冷静", "例生", "冷政"],
            "ans": 2,
            "cute_right_msg": "Quá chuẩn! `冷静（れいせい）な` = Lãnh Tĩnh (giữ cái đầu lạnh bình tĩnh)! ❄️✨",
            "right_exp": "`冷静（れいせい）` = điềm tĩnh, bình tĩnh phán đoán khách quan (trái với hoảng loạn `慌てる`).",
            "cute_wrong_msg": "'Giữ cái đầu lạnh và tâm thế tĩnh lặng' chính là hai chữ `冷` (lạnh) + `静` (tĩnh) = **冷静** đó em! 🌸",
            "wrong_exps": [
                "`礼正` không phải từ này (có `礼儀正しい`).",
                "Chính xác tuyệt đối! `冷静（れいせい）な態度`.",
                "`例生` không tồn tại.",
                "`冷政` không tồn tại."
            ],
            "source_ref": {"novel": "romcom", "chapter": 2, "lesson_id": "p1_c01_b02", "label": "Bộ 1 Romcom Ch.02 (Tính cách)"}
        },
        {
            "num": 3,
            "mondai": "問題4：文脈規定",
            "mondai_vi": "Điền từ vựng theo ngữ cảnh",
            "prompt": "同じ大学で同じゼミに通った彼とは、今でも（　　）として何でも相談できる仲だ。",
            "prompt_vi": "Với anh ấy — người từng học chung trường đại học và chung nhóm nghiên cứu — đến giờ tôi vẫn là người quen thân / tri kỷ có thể tâm sự mọi điều.",
            "options": ["親友（しんゆう）", "赤の他人（あかのたにん）", "ご近所（きんじょ）", "いとこ"],
            "ans": 1,
            "cute_right_msg": "Đúng phóc! Bạn thân tri kỷ có thể tâm sự mọi thứ = `親友（しんゆう）`! 🤝💕",
            "right_exp": "`親友（しんゆう）` = bạn thân thiết chí cốt (`何でも相談できる仲` — mối quan hệ có thể tâm sự đủ chuyện).",
            "cute_wrong_msg": "Người học chung đại học mà thân đến mức 'chuyện gì cũng chia sẻ được' chính là bạn thân **親友（しんゆう）**, chứ không phải người lạ hay anh em họ đâu ha~ 🌸",
            "wrong_exps": [
                "Chính xác! `親友` = bạn thân chí cốt.",
                "`赤の他人` = người dưng nước lã hoàn toàn xa lạ (ngược nghĩa!).",
                "`ご近所` = hàng xóm gần nhà.",
                "`いとこ` = anh chị em họ ruột thịt."
            ],
            "source_ref": {"novel": "romcom", "chapter": 1, "lesson_id": "p1_c01_b01", "label": "Bộ 1 Romcom Ch.01 (Bạn bè & Người quen)"}
        },
        {
            "num": 4,
            "mondai": "問題4：文脈規定",
            "mondai_vi": "Điền từ vựng theo ngữ cảnh",
            "prompt": "洗剤を混ぜてよく（　　）と、白い汚れもきれいに落ちるよ。",
            "prompt_vi": "Trộn bột giặt rồi ngâm vào nước xong chà rửa thật kỹ thì vết bẩn trắng cũng sạch tinh tươm đấy.",
            "options": ["こすると", "つぶすと", "かむと", "ほすと"],
            "ans": 1,
            "cute_right_msg": "Chuẩn không cần chỉnh! Vết bẩn dùng `こする` (chà xát, cọ rửa) để đánh bay vết dơ trên áo hay sàn! 🧼✨",
            "right_exp": "`擦（こす）る` = chà xát, kỳ cọ (`汚れをこすって落とす`).",
            "cute_wrong_msg": "Thao tác dọn dẹp giặt giũ trong Romcom Ch.04: dùng bàn chải hoặc tay chà cọ lên vết bẩn là `こする`, còn `ほす（干す）` là đem đi phơi sau khi giặt xong nha em! 🧺",
            "wrong_exps": [
                "Chính xác! `こする` = chà cọ xát (để tẩy vết bẩn).",
                "`つぶす` = nghiền nát (`じゃがいもをつぶす`).",
                "`かむ` = cắn nhai.",
                "`ほす` = phơi khô quần áo (`洗濯物を干す`), phải thực hiện *sau* khi giặt chứ không phải cách đánh tan vết bẩn ngay lúc trộn xà phòng."
            ],
            "source_ref": {"novel": "romcom", "chapter": 4, "lesson_id": "p1_c02_b02", "label": "Bộ 1 Romcom Ch.04 (Việc nhà)"}
        },
        {
            "num": 5,
            "mondai": "問題4：文脈規定",
            "mondai_vi": "Điền từ vựng theo ngữ cảnh",
            "prompt": "新人のころは失敗ばかりで落ち込んだが、先輩の温かいアドバイスに（　　）救われた。",
            "prompt_vi": "Hồi mới vào làm toàn mắc lỗi nên suy sụp lắm, nhưng tôi đã được cứu rỗi rất nhiều nhờ lời khuyên ấm áp của tiền bối.",
            "options": ["大いに", "ろくに", "さっぱり", "あいにく"],
            "ans": 1,
            "cute_right_msg": "Tuyệt vời! `大いに（おおいに）` = vô cùng nhiều, hết sức (mang ý nhấn mạnh tích cực cho hiệu quả/sự giúp đỡ/vui mừng)! 🌟",
            "right_exp": "`大いに（おおいに）` = vô cùng, hết sức (`大いに役立つ・助けられる・楽しむ`) — luôn đi với câu khẳng định tích cực.",
            "cute_wrong_msg": "Kiểm tra bài Phó từ Romcom Ch.12 nhé: `ろくに〜ない` và `さっぱり〜ない` đều là phủ định; còn muốn khen 'được cứu vớt rất nhiều' (câu khẳng định!) phải chọn **大いに** nha em! 💖",
            "wrong_exps": [
                "Chính xác! `大いに救われた` = được cứu giúp rất nhiều.",
                "`ろくに` là phó từ hô ứng PHỦ ĐỊNH (`ろくに休めない`).",
                "`さっぱり` thường đi với phủ định ('hoàn toàn không hiểu') hoặc tả vị thanh mát.",
                "`あいにく` = thật không may (tiêu cực)."
            ],
            "source_ref": {"novel": "romcom", "chapter": 12, "lesson_id": "p2_c02_b01", "label": "Bộ 1 Romcom Ch.12 (Bài 25: Phó từ)"}
        },
        {
            "num": 6,
            "mondai": "問題4：文脈規定",
            "mondai_vi": "Điền từ vựng theo ngữ cảnh",
            "prompt": "有名なホテルに（　　）して、ゆっくり温泉と景色を楽しみたい。",
            "prompt_vi": "Tôi muốn nghỉ trọ qua đêm tại một khách sạn nổi tiếng để thong thả tận hưởng suối nước nóng và phong cảnh.",
            "options": ["宿泊（しゅくはく）", "往復（おうふく）", "見送り（みおくり）", "混雑（こんざつ）"],
            "ans": 1,
            "cute_right_msg": "Chuẩn luôn! `ホテルに宿泊する` = lưu trú nghỉ qua đêm tại khách sạn! 🏨♨️",
            "right_exp": "`宿泊（しゅくはく）する` = nghỉ trọ qua đêm tại khách sạn, lữ quán.",
            "cute_wrong_msg": "Từ vựng Du lịch trong Romcom Ch.06 (`ホテルに...する`): nghỉ qua đêm là `宿泊（しゅくはく）する` nha em! 🧳",
            "wrong_exps": [
                "Chính xác! `宿泊する` = lưu trú qua đêm.",
                "`往復する` = đi và về khứ hồi.",
                "`見送り` = tiễn người lên đường.",
                "`混雑する` = đông đúc chen chúc."
            ],
            "source_ref": {"novel": "romcom", "chapter": 6, "lesson_id": "p1_c04_b01", "label": "Bộ 1 Romcom Ch.06 (Du lịch)"}
        },
        {
            "num": 7,
            "mondai": "問題4：文脈規定",
            "mondai_vi": "Điền từ vựng theo ngữ cảnh",
            "prompt": "大学で建築学を（　　）して、将来は地震に強い家を設計したい。",
            "prompt_vi": "Tôi muốn theo học chuyên ngành kiến trúc ở đại học, tương lai sẽ thiết kế những ngôi nhà chống động đất kiên cố.",
            "options": ["専攻（せんこう）", "卒業（そつぎょう）", "受験（じゅけん）", "欠席（けっせき）"],
            "ans": 1,
            "cute_right_msg": "Quá chuẩn! `大学で〜を専攻する` = học chuyên ngành gì ở đại học! 🏛️📐",
            "right_exp": "`専攻（せんこう）する` (Chuyên Công) = học chuyên sâu một ngành cụ thể ở bậc đại học/cao học.",
            "cute_wrong_msg": "Động từ đi với 'ngành học ở đại học' (`建築学を...`) chính là `専攻（せんこう）する` (theo chuyên ngành) đó em~ 🎓",
            "wrong_exps": [
                "Chính xác! `建築学を専攻する` = học chuyên ngành kiến trúc.",
                "`卒業する` = tốt nghiệp (đi với tên trường `大学を卒業する`, không đi với tên môn học rồi bảo tương lai sẽ học).",
                "`受験する` = thi tuyển đầu vào.",
                "`欠席する` = vắng mặt nghỉ học."
            ],
            "source_ref": {"novel": "romcom", "chapter": 7, "lesson_id": "p1_c05_b01", "label": "Bộ 1 Romcom Ch.07 (Trường học)"}
        },
        {
            "num": 8,
            "mondai": "問題4：文脈規定",
            "mondai_vi": "Điền từ vựng theo ngữ cảnh",
            "prompt": "仕事と子育てを（　　）させながら働く人が増えている。",
            "prompt_vi": "Số người vừa dung hòa cả công việc lẫn việc nuôi dạy con cái song song cùng lúc đang tăng lên.",
            "options": ["両立（りょうりつ）", "採用（さいよう）", "出張（しゅっちょう）", "退職（たいしょく）"],
            "ans": 1,
            "cute_right_msg": "Đỉnh luôn!! `仕事と育児・子育てを両立させる` (cân bằng làm tốt song song cả công việc và gia đình)! 💼🏡",
            "right_exp": "`A と B を両立（りょうりつ）させる`: Vừa gánh vác trọn vẹn cả công việc A lẫn chuyện B song song cùng lúc.",
            "cute_wrong_msg": "Hihi vừa cân bằng cả việc công ty lẫn chăm con/gia đình cùng lúc gọi là `両立（りょうりつ）` nha em! 💼🏡",
            "wrong_exps": [
                "Chính xác! `両立（りょうりつ）` = dung hòa, làm tốt song song cả hai.",
                "`採用（さいよう）` = tuyển dụng nhận vào làm.",
                "`出張（しゅっちょう）` = đi công tác.",
                "`退職（たいしょく）` = nghỉ việc hẳn."
            ],
            "source_ref": {"novel": "romcom", "chapter": 8, "lesson_id": "p1_c05_b02", "label": "Bộ 1 Romcom Ch.08 (Công việc)"}
        },
        {
            "num": 9,
            "mondai": "問題4：文脈規定",
            "mondai_vi": "Điền từ vựng theo ngữ cảnh",
            "prompt": "このテレビ番組は、最近の若者の本音を（　　）した特集が人気だ。",
            "prompt_vi": "Chương trình truyền hình này nổi tiếng với chuyên mục phỏng vấn lấy ý kiến thật lòng của giới trẻ gần đây.",
            "options": ["取材（しゅざい）", "投書（とうしょ）", "購読（こうどく）", "発行（はっこう）"],
            "ans": 1,
            "cute_right_msg": "Chuẩn bài Ch.09 (Truyền thông)! Phóng viên đi tác nghiệp thu thập tư liệu/phỏng vấn là `取材（しゅざい）する`! 🎥🎙️",
            "right_exp": "`取材（しゅざい）する` = tác nghiệp báo chí, thu thập thông tin phỏng vấn hiện trường để làm bài báo/chương trình TV.",
            "cute_wrong_msg": "Nhà đài đi gặp người dân lấy tin bài đưa lên phóng sự truyền hình là `取材（しゅざい）` nhé em! 📰",
            "wrong_exps": [
                "Chính xác! `取材（しゅざい）` = tác nghiệp lấy tin, phỏng vấn làm tư liệu.",
                "`投書（とうしょ）` = độc giả gửi thư góp ý tới tòa soạn.",
                "`購読（こうどく）` = đặt mua báo dài hạn.",
                "`発行（はっこう）` = xuất bản phát hành báo/tạp chí."
            ],
            "source_ref": {"novel": "romcom", "chapter": 9, "lesson_id": "p1_c06_b01", "label": "Bộ 1 Romcom Ch.09 (Truyền thông)"}
        },
        {
            "num": 10,
            "mondai": "問題4：文脈規定",
            "mondai_vi": "Điền từ vựng theo ngữ cảnh",
            "prompt": "年末が近づくにつれて、家の近所の商店街も正月準備でだんだん（　　）になってきた。",
            "prompt_vi": "Càng gần cuối năm, khu phố thương mại gần nhà tôi cũng dần trở nên tấp nập rộn ràng chuẩn bị đón Tết.",
            "options": ["にぎやか", "地味", "寂しげ", "静か"],
            "ans": 1,
            "cute_right_msg": "Tuyệt vời! Phố chợ chuẩn bị đón năm mới ngày càng nhộn nhịp `にぎやか` — không khí Chương 10 Lễ Tết luôn! 🎍✨",
            "right_exp": "`にぎやか（賑やか）` = đông vui, rộn rã náo nhiệt.",
            "cute_wrong_msg": "Không khí phố chợ cuối năm nhộn nhịp đông vui sắm Tết thì chắc chắn chọn `にぎやか` rồi ha em! 🏮",
            "wrong_exps": [
                "Chính xác! `にぎやか` = đông vui rộn ràng.",
                "`地味（じみ）` = giản dị tối màu (hoặc tẻ nhạt).",
                "`寂しげ` = có vẻ cô đơn hiu quạnh.",
                "`静か` = yên ắng vắng vẻ (trái nghĩa không khí cuối năm)."
            ],
            "source_ref": {"novel": "romcom", "chapter": 10, "lesson_id": "p1_c07_b01", "label": "Bộ 1 Romcom Ch.10 (Lễ hội & Sự kiện)"}
        },
        {
            "num": 11,
            "mondai": "問題5：言い換え類義",
            "mondai_vi": "Từ / cụm từ đồng nghĩa",
            "prompt": "あのカフェのケーキは味が<u>濃厚</u>で、コーヒーにとてもよく合う。",
            "prompt_vi": "Bánh ngọt ở quán cà phê kia vị đậm đà béo ngậy, hợp với cà phê lắm luôn.",
            "options": ["薄くてさっぱりして", "濃くて深みがあって", "苦くて食べにくく", "硬くて冷たく"],
            "ans": 2,
            "cute_right_msg": "Đỉnh của chóp!! `濃厚・濃い` và `深い` trong Chương 11 Đa nghĩa chuẩn gu ẩm thực của Kenji luôn! 🍰☕",
            "right_exp": "Tính từ `濃い（こい）` / `濃厚な` khi dùng cho hương vị món ăn mang nghĩa đậm đà, sánh đặc, có chiều sâu hương vị.",
            "cute_wrong_msg": "Chữ `濃厚` gồm chữ `濃（こ）い` (đặc, đậm) và `厚（あつ）い` (dày vị): nghĩa là vị đậm đà sánh quyện béo ngậy nha em! 🌸",
            "wrong_exps": [
                "`薄い` = nhạt nhẽo, loãng (trái nghĩa!).",
                "Chính xác! `濃くて深みがあって` = đậm đà sâu vị.",
                "`苦い` = đắng (lệch nghĩa).",
                "`硬い` = cứng nhắc (sai phạm trù hương vị)."
            ],
            "source_ref": {"novel": "romcom", "chapter": 11, "lesson_id": "p2_c01_b03", "label": "Bộ 1 Romcom Ch.11 (Tính từ đa nghĩa)"}
        },
        {
            "num": 12,
            "mondai": "問題5：言い換え類義",
            "mondai_vi": "Từ / cụm từ đồng nghĩa",
            "prompt": "彼女は甘いお菓子にはまったく<u>目がない</u>そうだ。",
            "prompt_vi": "Nghe nói cô ấy cực kỳ mê tít đồ ngọt bánh kẹo luôn đó.",
            "options": ["まったく興味がない", "とても嫌いだ", "大好きでたまらない", "見ることもできない"],
            "ans": 3,
            "cute_right_msg": "Chuẩn 100 điểm!! Quán dụng cực bẫy trong Chương 13: `〜に目がない` KHÔNG phải 'không để mắt tới' mà là **mê tít mù mắt không kìm nổi**! 🍮💕",
            "right_exp": "`N + に目がない`: Quá mê mẩn món gì đó đến mức 'hoa mắt' không còn biết gì khác = `大好きでたまらない`!",
            "cute_wrong_msg": "Đừng dịch đen chữ `ない` trong `目がない` thành ghét hay không thích nha em ơi!! Thành ngữ này nghĩa ngược lại 180 độ là **cực kỳ mê tít (`大好きでたまらない`)** đó! 🍰",
            "wrong_exps": [
                "Rất dễ bị đánh lừa! `目がない` là mê tít chứ KHÔNG phải không hứng thú.",
                "Ngược nghĩa hoàn toàn!",
                "Chính xác tuyệt đối! `甘いものに目がない` = mê đồ ngọt phát cuồng.",
                "Không dịch nghĩa đen 'không nhìn thấy'."
            ],
            "source_ref": {"novel": "romcom", "chapter": 13, "lesson_id": "p2_c06_b01", "label": "Bộ 1 Romcom Ch.13 (Quán dụng ngữ 1)"}
        },
        {
            "num": 13,
            "mondai": "問題5：言い換え類義",
            "mondai_vi": "Từ / cụm từ đồng nghĩa",
            "prompt": "美咲さんはクラスのみんなの間で<u>気さくな</u>先輩として親しまれている。",
            "prompt_vi": "Misaki được mọi người trong lớp yêu mến như một tiền bối cởi mở thân thiện.",
            "options": ["きびしくて怖い", "打ち解けやすく親しみやすい", "無口で真面目な", "わがままで勝手な"],
            "ans": 2,
            "cute_right_msg": "Quá chuẩn!! `気さくな（きさくな）` = cởi mở, xởi lởi dễ bắt chuyện (`親しみやすい`)! 🌟",
            "right_exp": "`気さくな（人）`: Dễ gần, cởi mở, không giữ kẽ hay kiêu kỳ nên rất dễ trò chuyện.",
            "cute_wrong_msg": "Từ khóa tính cách dễ mến trong Romcom Ch.02: `気さくな人` là người **dễ bắt chuyện, cởi mở chan hòa** (`親しみやすい`) nha em! 🌸",
            "wrong_exps": [
                "`きびしくて怖い` = nghiêm khắc đáng sợ (trái nghĩa).",
                "Chính xác! `気さくな` = hòa đồng dễ gần dễ nói chuyện.",
                "`無口で真面目` = trầm lặng ít nói.",
                "`わがまま` = ích kỷ bướng bỉnh."
            ],
            "source_ref": {"novel": "romcom", "chapter": 2, "lesson_id": "p1_c01_b02", "label": "Bộ 1 Romcom Ch.02 (Tính cách)"}
        },
        {
            "num": 14,
            "mondai": "問題6：用法",
            "mondai_vi": "Cách dùng từ đúng trong câu",
            "prompt": "次の言葉の使い方として最もよいものを、1・2・3・4から一つ選びなさい。\n【言葉：<b><u>顔に出る</u></b>】",
            "prompt_vi": "Chọn câu sử dụng đúng nhất từ 【顔に出る】 (lộ rõ cảm xúc lên nét mặt).",
            "options": [
                "彼は嘘をつくのが下手で、緊張するとすぐ顔に出てしまう。",
                "久しぶりに太陽の光を浴びたので、顔に出て日焼けした。",
                "毎日化粧水をしっかり塗っているので、顔に出てつやつやだ。",
                "試験会場の前で友達と偶然顔に出たので驚いた。"
            ],
            "ans": 1,
            "cute_right_msg": "Chuẩn không cần chỉnh! `顔に出る` chỉ **tâm trạng / cảm xúc / lời nói dối lộ hẳn lên gương mặt**, không dùng cho cháy nắng hay chạm mặt nhau ngoài đường đâu nhé! 😊✨",
            "right_exp": "`顔に出る` = vui buồn lo lắng hay cảm xúc bên trong bị lộ ngay lên nét mặt (`嬉しさ・緊張が顔に出る`). Gặp mặt trực tiếp dùng `顔を合わせる`.",
            "cute_wrong_msg": "Quán dụng `顔に出る` nói về **cảm xúc bên trong trồi lộ ra nét mặt** (`すぐ顔に出る`: nhìn mặt là biết ngay đang nghĩ gì) chứ không phải da dẻ hay gặp mặt ngoài đường đâu em! 🌸",
            "wrong_exps": [
                "Chính xác! Cứ căng thẳng là lộ ngay lên nét mặt (`顔に出る`).",
                "Cháy nắng dùng `日焼けする` / `顔が焼ける`.",
                "Da mịn dùng `肌に効果が出る / つやつやになる`.",
                "Tình cờ chạm mặt nhau dùng `顔を合わせる / ばったり会う`."
            ],
            "source_ref": {"novel": "romcom", "chapter": 13, "lesson_id": "p2_c06_b01", "label": "Bộ 1 Romcom Ch.13 (Quán dụng ngữ 1)"}
        },
        {
            "num": 15,
            "mondai": "問題6：用法",
            "mondai_vi": "Cách dùng từ đúng trong câu",
            "prompt": "次の言葉の使い方として最もよいものを、1・2・3・4から一つ選びなさい。\n【言葉：<b><u>丸く収まる</u></b>】",
            "prompt_vi": "Chọn câu sử dụng đúng nhất từ 【丸く（収まる）】 (giải quyết êm thấm, ổn thỏa không sứt mẻ).",
            "options": [
                "おにぎりを手のひらで丸く収まるように優しく握った。",
                "お互いに意見を譲り合ったおかげで、話し合いは丸く収まった。",
                "荷物がトランクの中に丸く収まるように、小さくたたんだ。",
                "新しいお皿を買ったが、棚の隅に丸く収まった。"
            ],
            "ans": 2,
            "cute_right_msg": "Quá đỉnh!! Ở Romcom Ch.11 (`丸い` đa nghĩa) ta có `丸く収まる` nghĩa bóng là **mọi mâu thuẫn được giải quyết êm đẹp hài hòa**! 🕊️✨",
            "right_exp": "`丸く収まる` là cụm cố định mang nghĩa *mâu thuẫn, tranh cãi được dàn xếp giải quyết êm thấm, đôi bên cùng hài lòng* (chú ý: bỏ đồ vào vali dùng `うまく収まる / きれいに収まる`, nặn cơm nắm dùng `丸く握る`).",
            "cute_wrong_msg": "Trong Chương 11 (Tính từ đa nghĩa), chữ `丸い` ngoài nghĩa 'hình tròn' còn có cụm cực hay thi là `丸く収まる` = **giải quyết mâu thuẫn êm thấm hòa bình** nha em! 💖",
            "wrong_exps": [
                "Nắm cơm hình tròn dùng `丸く握る` (`丸く収まる` không dùng cho hình dáng đồ vật).",
                "Chính xác tuyệt đối! Nhờ nhượng bộ nên cuộc thương lượng kết thúc êm đẹp (`丸く収まった`).",
                "Đồ vật lọt gọn vào vali dùng `ぴったり収まる / すっぽり収まる`.",
                "Đĩa cất gọn lên kệ dùng `きちんと収まった`."
            ],
            "source_ref": {"novel": "romcom", "chapter": 11, "lesson_id": "p2_c01_b03", "label": "Bộ 1 Romcom Ch.11 (Đa nghĩa 丸く)"}
        },
        {
            "num": 16,
            "mondai": "問題6：用法",
            "mondai_vi": "Cách dùng từ đúng trong câu",
            "prompt": "次の言葉の使い方として最もよいものを、1・2・3・4から一つ選びなさい。\n【言葉：<b><u>熱中する</u></b>】",
            "prompt_vi": "Chọn câu sử dụng đúng nhất từ 【熱中（ねっちゅう）する】 (say mê, đắm chìm hết mình vào một việc/sở thích).",
            "options": [
                "夏は気温が35度を超えて、毎日熱中してとても暑い。",
                "子どものころ、休日はいつも時間を忘れてゲームに熱中していた。",
                "おいしい料理を食べたら、お腹がいっぱいで熱中した。",
                "風邪をひいて熱が高くなったので、学校を休んで熱中した。"
            ],
            "ans": 2,
            "cute_right_msg": "Chuẩn bài Sở thích Romcom Ch.05 (`趣味・娯楽`)! Say sưa đắm chìm vào trò chơi hay sở thích là `〜に熱中する`! 🎮✨",
            "right_exp": "`N + に熱中（ねっちゅう）する`: Dồn hết tâm trí say mê đắm đuối vào một việc/sở thích/nghiên cứu (`ゲーム・趣味・練習に熱中する`). Đừng nhầm với say nắng (`熱中症`) hay bị sốt cao (`発熱`).",
            "cute_wrong_msg": "Chữ `熱中` dù có chữ 'Nhiệt' nhưng KHÔNG dùng để tả trời nóng 35 độ (`暑い`) hay sốt bệnh (`発熱・高熱`) đâu nha em! Nó mang nghĩa **say mê mải miết vào việc gì đó** (`趣味に熱中する`)! 🌟",
            "wrong_exps": [
                "Trời nóng bức dùng `蒸し暑い / 猛暑になる` (say nắng là `熱中症になる`, không phải `熱中する`).",
                "Chính xác tuyệt đối! Say mê chơi game quên cả thời gian (`ゲームに熱中していた`).",
                "No bụng thỏa mãn dùng `満足した`.",
                "Bị sốt cao dùng `熱が出た / 発熱した`."
            ],
            "source_ref": {"novel": "romcom", "chapter": 5, "lesson_id": "p1_c03_b01", "label": "Bộ 1 Romcom Ch.05 (Sở thích & Giải trí)"}
        },
        {
            "num": 17,
            "mondai": "問題7：文の文法1",
            "mondai_vi": "Ngữ pháp câu N2",
            "prompt": "料理の味は（　　）、盛り付けの美しさにもこだわってこそ一流のシェフだ。",
            "prompt_vi": "Hương vị món ăn đã đành là đương nhiên rồi, phải cầu kỳ cả vẻ đẹp trình bày món ăn nữa mới xứng là đầu bếp hạng nhất.",
            "options": ["もちろんのこと", "はおろか", "にあたって", "からには"],
            "ans": 1,
            "cute_right_msg": "Quá mượt!! Đọc đúng câu chuyện nấu nướng của Kenji với mẫu `〜はもちろんのこと、〜も`! 🍽️✨",
            "right_exp": "`A はもちろんのこと、B も`: A đương nhiên phải có/giỏi rồi, còn chăm chút cả B nữa.",
            "cute_wrong_msg": "Hương vị ngon (tất nhiên rồi) + chú trọng thêm cả bày trí (`盛り付けにも`): mẫu nâng tầm bổ sung hai vế cùng hay là `もちろんのこと` nha em! 🌸",
            "wrong_exps": [
                "Chính xác! `味はもちろんのこと、盛り付けにも...`",
                "`はおろか` chỉ dùng với câu phủ định ('A còn chẳng được huống chi B').",
                "`にあたって` = nhân dịp cột mốc trọng đại.",
                "`からには` = một khi đã quyết tâm làm V thì..."
            ],
            "source_ref": {"novel": "romcom", "chapter": 3, "lesson_id": "p1_c02_b01", "label": "Ngữ pháp N2 — 〜はもちろんのこと"}
        },
        {
            "num": 18,
            "mondai": "問題7：文の文法1",
            "mondai_vi": "Ngữ pháp câu N2",
            "prompt": "どんなに素晴らしい才能があった（　　）、毎日の努力がなければ一流にはなれない。",
            "prompt_vi": "Dẫu cho có tài năng xuất chúng đến đâu đi chăng nữa, nếu thiếu nỗ lực mỗi ngày thì cũng chẳng thể trở thành bậc thầy hàng đầu.",
            "options": ["としても", "だけあって", "ことから", "ばかりに"],
            "ans": 1,
            "cute_right_msg": "Chính xác! `どんなに〜たとしても` (cho dù giả sử có... đi chăng nữa) khớp hô ứng 100%! 🏆",
            "right_exp": "`どんなに〜たとしても`: Cho dù giả thiết có đúng là X đi chăng nữa thì vế sau vẫn không thay đổi / vẫn cần điều kiện khác.",
            "cute_wrong_msg": "Thấy từ để hỏi `どんなに` ở đầu câu giả định nhượng bộ ('dù có tài năng đến mấy đi nữa...'): chọn ngay đuôi `としても` nha em! 💡",
            "wrong_exps": [
                "Chính xác! `どんなに才能があったとしても`.",
                "`だけあって` = quả đúng xứng với danh tiếng/thực lực (`才能があるだけあって...`).",
                "`ことから` = xuất phát từ dấu hiệu/lý do đó nên...",
                "`ばかりに` = chỉ tại vì lỡ X nên kết quả tồi tệ."
            ],
            "source_ref": {"novel": "romcom", "chapter": 5, "lesson_id": "p1_c03_b01", "label": "Ngữ pháp N2 — 仮定譲歩（〜としても）"}
        },
        {
            "num": 19,
            "mondai": "問題7：文の文法1",
            "mondai_vi": "Ngữ pháp câu N2",
            "prompt": "ケンジは料理が苦手な人の気持ちがよく分かる（　　）、教え方がとても丁寧だ。",
            "prompt_vi": "Chính vì Kenji hiểu rất rõ cảm giác của người nấu ăn kém, nên cách cậu ấy chỉ dạy mới tận tâm và tỉ mỉ đến vậy.",
            "options": ["にしては", "ものの", "どころか", "だけに"],
            "ans": 4,
            "cute_right_msg": "Quá ngọt luôn!! `〜だけに` (chính vì X nên kết quả Y càng xứng hợp!) đúng chuẩn phong thái chàng bếp trưởng ấm áp Kenji! 🍳💖",
            "right_exp": "`〜だけに`: Chính vì là X nên đương nhiên/càng tương xứng dẫn đến Y (`気持ちが分かるだけに、教え方が丁寧だ`).",
            "cute_wrong_msg": "Chính vì (X) nên càng tương xứng với kết quả (Y) → mẫu N2 cực ngọt `だけに` nha em! 🌸",
            "wrong_exps": [
                "`〜にしては` là trái ngược với tiêu chuẩn thông thường.",
                "`〜ものの` là tuy rằng nhưng.",
                "`〜どころか` là đừng nói đến... trái lại...",
                "Chính xác tuyệt đối! `よく分かるだけに、とても丁寧だ`."
            ],
            "source_ref": {"novel": "romcom", "chapter": 3, "lesson_id": "p1_c02_b01", "label": "Ngữ pháp N2 — 〜だけに"}
        },
        {
            "num": 20,
            "mondai": "問題8：文の文法2 ★",
            "mondai_vi": "Sắp xếp thành phần câu",
            "prompt": "ミサキは不器用な ＿＿＿ ＿＿＿ ★ ＿＿＿ お菓子を作っていた。",
            "prompt_vi": "Misaki tuy vụng về thế thôi nhưng vì muốn chúc mừng sinh nhật Kenji nên đã thức khuya tỉ mỉ tự làm bánh ngọt.",
            "options": ["祝おうとして", "ケンジの", "誕生日を", "わりに、"],
            "ans": 3,
            "cute_right_msg": "Chúc mừng em hoàn thành 20/20 câu ôn tập Bộ 1 Romcom!! `[4] わりに、 → [2] ケンジの → ★[3] 誕生日を → [1] 祝おうとして` ngọt lịm luôn! 🎂💕",
            "right_exp": "Ghép chuẩn xác: `不器用な [4]わりに、 [2]ケンジの ★[3]誕生日を [1]祝おうとして お菓子を作っていた。`\n- `不器用な` (vụng về) nối với `[4]わりに、` (tuy vụng về nhưng so với điều đó lại...).\n- `[2]ケンジの` + `[3]誕生日を` + `[1]祝おうとして` (định chúc mừng sinh nhật của Kenji).\n→ Vị trí dấu ★ là **3 (`誕生日を`)**!",
            "cute_wrong_msg": "Nhớ cảnh dễ thương trong Romcom Ch.10 không em: đứng ngay sau tính từ `不器用な` là `[4] わりに、`! Rồi nối cụm `ケンジの + 誕生日を + 祝おうとして` chuẩn không lệch 1 chữ luôn! 🌸✨",
            "wrong_exps": [
                "`[1] 祝おうとして` đứng ở ô số 4.",
                "`[2] ケンジの` đứng ở ô số 2.",
                "Chính xác tuyệt đối! Vị trí ★ là `[3] 誕生日を` (`4 → 2 → 3 → 1`).",
                "`[4] わりに、` đứng ngay ô số 1 (sau `不器用な`)."
            ],
            "source_ref": {"novel": "romcom", "chapter": 10, "lesson_id": "p1_c07_b01", "label": "Bộ 1 Romcom Ch.10 ★ (〜わりに)"}
        },
    ]
}


EXAM_REVIEW_YANDERE = {
    "id": "review-yandere",
    "code": "ÔN TẬP BỘ 2 • YANDERE N2",
    "title_jp": "【Yandere復習テスト】紅の檻と執着心理学の全語彙（20問）",
    "title_vi": "Đề Ôn Tập Nhanh Bộ 2: Yandere (12 Bài • 20 Câu Chuẩn JLPT)",
    "category": "review",
    "novel_id": "yandere",
    "duration_min": 20,
    "pass_score": 12,
    "max_score": 20,
    "description": "Bài kiểm tra tổng ôn toàn bộ 12 bài học Shinkanzen N2 (Cảm xúc tâm lý, Y tế sức khỏe, Máy tính, Hình sự, Động từ đa nghĩa, Từ đồng âm dễ nhầm, Phó từ toàn tập, Quán dụng ngữ) theo bước chân Kaito & Sayuri.",
    "yuki_note_start": "Chào mừng em tới bài test tổng ôn **Bộ 2 Yandere** vừa gay cấn vừa rùng mình cùng Kaito và Sayuri nè 🖤🌹 Chỗ này gom sạch từ vựng tâm lý, máy tính, động từ đa nghĩa và đặc biệt là 3 bài Phó Từ siêu bẫy của Shinkanzen N2 đó! Tự tin làm bài nha em~ ✨",
    "yuki_note_finish_pass": "Quá đỉnh em ơi!! Toàn bộ phó từ hô ứng, từ đồng âm `収める・改定` và động từ đa nghĩa trong Bộ Yandere đều không làm khó được em luôn! 🎉🌹",
    "yuki_note_finish_try": "Hít một hơi ấm nào em~ Bộ Yandere gom toàn những cặp từ 'anh em sinh đôi' dễ nhầm nhất cuốn Shinkanzen luôn nên có nhầm 1-2 câu cũng hoàn toàn dễ hiểu nè! Xem giải thích chi tiết bên dưới xong là nhớ suốt đời luôn 💖",
    "questions": [
        {
            "num": 1,
            "mondai": "問題1：漢字読み",
            "mondai_vi": "Cách đọc Kanji",
            "prompt": "いつも仲が良さそうに見える友人に対して、心のどこかで<u>嫉妬</u>していた。",
            "prompt_vi": "Đối với người bạn lúc nào trông cũng vui vẻ hạnh phúc kia, sâu thẳm trong lòng tôi đã thầm ghen tuông đố kỵ.",
            "options": ["しっと", "しつど", "じっと", "しんとう"],
            "ans": 1,
            "cute_right_msg": "Chuẩn bài Ch.01 Yandere!! `嫉妬（しっと）する` = ghen tuông đố kỵ (chữ Tật + Đố, đọc âm ngắt `しっと`)! 🖤🌹",
            "right_exp": "`嫉妬` đọc là **しっと** (có âm ngắt `っ` ở giữa, nghĩa là ghen tuông ghen ghét).",
            "cute_wrong_msg": "Từ khóa tâm lý kinh điển của Bộ Yandere Ch.01: chữ Hán Tật Đố đọc ngắn và có âm ngắt thành **しっと** nha em (đừng nhầm với `しつど` — độ ẩm `湿度`)! 💡",
            "wrong_exps": [
                "Chính xác! `嫉妬（しっと）` = sự ghen tuông.",
                "`しつど` là chữ `湿度` (độ ẩm không khí).",
                "`じっと` là phó từ 'chằm chằm / im thin thít'.",
                "`しんとう` là chữ `浸透` (thẩm thấu)."
            ],
            "source_ref": {"novel": "yandere", "chapter": 1, "lesson_id": "p1_c01_b03", "label": "Bộ 2 Yandere Ch.01 (Cảm xúc)"}
        },
        {
            "num": 2,
            "mondai": "問題2：表記",
            "mondai_vi": "Chọn Kanji đúng",
            "prompt": "このファイルは消えてはいけないので、USBメモリーにも<u>ほぞん</u>しておこう。",
            "prompt_vi": "Vì tệp tin này tuyệt đối không được để mất nên hãy lưu trữ sao lưu cả vào USB đi.",
            "options": ["保尊", "保存", "補存", "保在"],
            "ans": 2,
            "cute_right_msg": "Chính xác! Chữ `保` (bảo vệ) + `存` (tồn tại) = `保存（ほぞん）` (Save file / bảo quản)! 💾✨",
            "right_exp": "`保存（ほぞん）する` = lưu dữ liệu trên máy tính hoặc bảo quản thực phẩm, di sản.",
            "cute_wrong_msg": "Trong Yandere Ch.03 (Máy tính): ấn Save lưu file lại là `保存（ほぞん）`, gồm chữ Bảo và chữ Tồn nha em! 💻",
            "wrong_exps": [
                "`保尊` không có từ này (`尊敬` là chữ Tôn).",
                "Chính xác tuyệt đối! `保存（ほぞん）` = lưu giữ, bảo quản.",
                "`補存` không tồn tại.",
                "`保在` không tồn tại."
            ],
            "source_ref": {"novel": "yandere", "chapter": 3, "lesson_id": "p1_c06_b02", "label": "Bộ 2 Yandere Ch.03 (Máy tính)"}
        },
        {
            "num": 3,
            "mondai": "問題4：文脈規定",
            "mondai_vi": "Điền từ vựng theo ngữ cảnh",
            "prompt": "大切な仕事で失敗してしまい、上司に（　　）する余地もなく厳しく叱られた。",
            "prompt_vi": "Làm hỏng công việc quan trọng nên tôi bị sếp mắng nghiêm khắc mà chẳng còn chỗ nào để biện minh thanh minh cả.",
            "options": ["言い訳（いいわけ）", "お世辞（おせじ）", "尊敬（そんけい）", "誤解（ごかい）"],
            "ans": 1,
            "cute_right_msg": "Quá chuẩn! `言い訳（いいわけ）をする` = viện cớ, thanh minh biện hộ cho lỗi lầm! 💼",
            "right_exp": "`言い訳（いいわけ）` = lời biện bạch, viện cớ thoái thác khi mắc lỗi (`言い訳の余地もない`: không còn lời nào để bào chữa).",
            "cute_wrong_msg": "Làm sai việc rồi tìm lý do chối lỗi / thanh minh trước sếp là `言い訳（いいわけ）`, chứ không phải 'lời khen nịnh xã giao' (`お世辞`) đâu nhé em~ 🌸",
            "wrong_exps": [
                "Chính xác! `言い訳` = lời biện minh, viện cớ.",
                "`お世辞` = lời khen nịnh xã giao cho đẹp lòng (`お世辞を言う`).",
                "`尊敬` = sự tôn kính.",
                "`誤解` = sự hiểu lầm."
            ],
            "source_ref": {"novel": "yandere", "chapter": 1, "lesson_id": "p1_c01_b03", "label": "Bộ 2 Yandere Ch.01 (Cảm xúc)"}
        },
        {
            "num": 4,
            "mondai": "問題4：文脈規定",
            "mondai_vi": "Điền từ vựng theo ngữ cảnh",
            "prompt": "昨日食べた刺身にあたったのか、夜中から（　　）が止まらなくて本当に苦しかった。",
            "prompt_vi": "Không biết có phải trúng thực món sashimi ăn hôm qua không mà từ nửa đêm tôi cứ buồn nôn / tiêu chảy không dứt khổ sở vô cùng.",
            "options": ["吐き気（はきけ）", "睡眠（すいみん）", "予防（よぼう）", "健康（けんこう）"],
            "ans": 1,
            "cute_right_msg": "Chuẩn bài Y tế Yandere Ch.02 (`Sức khỏe`)!! Bị ngộ độc thực phẩm gây cơn buồn nôn (`吐き気（はきけ）`) không dứt! 🤢💊",
            "right_exp": "`吐き気（はきけ）` = cảm giác buồn nôn nôn nao (`吐き気がする / 止まらない`).",
            "cute_wrong_msg": "Đọc cụm 'trúng thực thức ăn... không ngừng lại được nên khổ sở vô cùng': triệu chứng đó là buồn nôn `吐き気（はきけ）` nha em! 🩺",
            "wrong_exps": [
                "Chính xác! `吐き気` = cơn buồn nôn.",
                "`睡眠` = giấc ngủ.",
                "`予防` = phòng ngừa.",
                "`健康` = sức khỏe."
            ],
            "source_ref": {"novel": "yandere", "chapter": 2, "lesson_id": "p1_c02_b03", "label": "Bộ 2 Yandere Ch.02 (Sức khỏe)"}
        },
        {
            "num": 5,
            "mondai": "問題4：文脈規定",
            "mondai_vi": "Điền từ vựng theo ngữ cảnh",
            "prompt": "夜の公園で怪しい男が逃げるところを（　　）した人が、すぐ110番に通報した。",
            "prompt_vi": "Người tận mắt chứng kiến cảnh kẻ khả nghi bỏ chạy trong công viên ban đêm đã lập tức gọi báo cảnh sát 110.",
            "options": ["目撃（もくげき）", "逮捕（たいほ）", "捜査（そうさ）", "盗難（とうなん）"],
            "ans": 1,
            "cute_right_msg": "Chính xác! Người dân đi ngang qua nhìn thấy hiện trường là `目撃（もくげき）する` (mục kích, chứng kiến tận mắt)! 🕵️‍♂️",
            "right_exp": "`目撃（もくげき）する` = tận mắt chứng kiến cảnh tượng xảy ra (tai nạn, tội phạm). Cảnh sát mới `逮捕` (bắt) và `捜査` (điều tra).",
            "cute_wrong_msg": "Chủ ngữ ở đây là người dân gọi báo cảnh sát 110, nên người đó là nhân chứng nhìn thấy sự việc = `目撃する` nha em! ✨",
            "wrong_exps": [
                "Chính xác! `目撃する` = tận mắt chứng kiến.",
                "`逮捕する` = bắt giữ tội phạm (công việc của cảnh sát).",
                "`捜査する` = điều tra phá án.",
                "`盗難` = nạn trộm cắp (`盗難に遭う`)."
            ],
            "source_ref": {"novel": "yandere", "chapter": 4, "lesson_id": "p1_c07_b02", "label": "Bộ 2 Yandere Ch.04 (Sự kiện & Hình sự)"}
        },
        {
            "num": 6,
            "mondai": "問題4：文脈規定",
            "mondai_vi": "Điền từ vựng theo ngữ cảnh",
            "prompt": "地震が起きたときは慌てて外へ飛び出さず、まず机の下に隠れるなど身の安全を（　　）してください。",
            "prompt_vi": "Khi động đất xảy ra đừng hoảng loạn chạy nhào ra ngoài, trước tiên hãy đảm bảo an toàn tính mạng như trốn dưới gầm bàn.",
            "options": ["確保（かくほ）", "発生（はっせい）", "避難（ひなん）", "被害（ひがい）"],
            "ans": 1,
            "cute_right_msg": "Chuẩn collocation thảm họa Ch.04!! `安全を確保（かくほ）する` = bảo đảm giữ an toàn tính mạng trước tiên! ⛑️",
            "right_exp": "`安全を確保（かくほ）する`: Bảo đảm, giữ chắc lấy sự an toàn trước thiên tai hoặc trong khâu kiểm soát chất lượng.",
            "cute_wrong_msg": "Cụm từ vàng khi phòng tránh thiên tai ở Nhật: `身の安全を確保する` (bảo đảm an toàn thân thể), còn `避難する` là sơ tán di chuyển tới nơi trú ẩn (người ta dặn ĐỪNG vội lao ra ngoài trước mà hãy chui xuống gầm bàn bảo đảm an toàn trước)! 🌍",
            "wrong_exps": [
                "Chính xác tuyệt đối! `安全を確保する` = bảo đảm an toàn.",
                "`発生する` = phát sinh xảy ra (dùng cho bão, hỏa hoạn, tai nạn).",
                "`避難する` = sơ tán tới khu trú ẩn, không đứng sau `身の安全を` với trợ từ `を`.",
                "`被害` = thiệt hại (`被害に遭う`)."
            ],
            "source_ref": {"novel": "yandere", "chapter": 4, "lesson_id": "p1_c07_b02", "label": "Bộ 2 Yandere Ch.04 (Thiên tai)"}
        },
        {
            "num": 7,
            "mondai": "問題4：文脈規定",
            "mondai_vi": "Điền từ vựng theo ngữ cảnh",
            "prompt": "新しいプロジェクトを成功させるため、営業部と開発部が何度も（　　）を行った。",
            "prompt_vi": "Để dự án mới thành công, phòng kinh doanh và phòng phát triển đã tiến hành trao đổi bàn bạc / đàm phán rất nhiều lần.",
            "options": ["打ち合わせ（うちあわせ）", "勘違い（かんちがい）", "嫌がらせ（いやがらせ）", "言い訳（いいわけ）"],
            "ans": 1,
            "cute_right_msg": "Quá chuẩn! `打ち合わせ` (họp bàn thống nhất kế hoạch giữa các bộ phận/đối tác) rất hay gặp trong Bộ Yandere Ch.08! 📋✨",
            "right_exp": "`打ち合わせ` = buổi họp bàn chuẩn bị kế hoạch, thống nhất chi tiết công việc.",
            "cute_wrong_msg": "Hai phòng ban ngồi lại bàn thảo để giúp dự án thành công thì chắc chắn là họp thống nhất = `打ち合わせ` rồi ha em! 🤝",
            "wrong_exps": [
                "Chính xác! `打ち合わせを行う` = tiến hành họp bàn công việc.",
                "`勘違い` = sự hiểu nhầm tưởng bở.",
                "`嫌がらせ` = trò chơi khăm quấy rối.",
                "`言い訳` = lời biện minh."
            ],
            "source_ref": {"novel": "yandere", "chapter": 7, "lesson_id": "p2_c02_b02", "label": "Bộ 2 Yandere Ch.07 (Từ gần nghĩa)"}
        },
        {
            "num": 8,
            "mondai": "問題4：文脈規定",
            "mondai_vi": "Điền từ vựng theo ngữ cảnh",
            "prompt": "その古い工場では、時代遅れになった設備を新しく（　　）計画が進んでいる。",
            "prompt_vi": "Tại nhà máy cũ kia, kế hoạch thay mới cải tiến dàn thiết bị đã lỗi thời đang được xúc tiến.",
            "options": ["取り替える", "取り戻す", "取り締まる", "受け持つ"],
            "ans": 1,
            "cute_right_msg": "Tuyệt vời! `古いものを新しく取り替える` = thay thế đồ cũ bằng đồ mới — nhớ nghĩa cốt lõi động từ đa nghĩa ở Yandere Ch.06! 🔧✨",
            "right_exp": "`取り替える` (từ đa nghĩa/từ ghép Ch.06-07): thay thế cái cũ/hỏng bằng cái mới (`部品・電池・設備を取り替える`).",
            "cute_wrong_msg": "Đọc ngữ cảnh 'đổi trang thiết bị cũ lỗi thời thành đồ mới': dùng `取り替える` (thay thế) chứ không phải lấy lại đồ bị mất (`取り戻す`) hay truy quét phạm pháp (`取り締まる`) nha em! 💡",
            "wrong_exps": [
                "Chính xác! `設備を取り替える` = thay mới trang thiết bị.",
                "`取り戻す` = giành lại, lấy lại thứ từng thuộc về mình (`信頼・平和を取り戻す`).",
                "`取り締まる` = cảnh sát tuần tra trấn áp xử lý vi phạm.",
                "`受け持つ` = phụ trách đảm nhận (lớp học, khu vực)."
            ],
            "source_ref": {"novel": "yandere", "chapter": 7, "lesson_id": "p2_c02_b02", "label": "Bộ 2 Yandere Ch.07 (Từ gần nghĩa)"}
        },
        {
            "num": 9,
            "mondai": "問題4：文脈規定",
            "mondai_vi": "Điền từ vựng theo ngữ cảnh",
            "prompt": "彼は人見知りで話しかけにくいように見えるが、実は一度話すと（　　）優しい人だ。",
            "prompt_vi": "Anh ấy nhìn có vẻ lạ người khó bắt chuyện thế thôi, nhưng thật ra hễ nói chuyện một lần rồi thì lại là người dịu dàng bất ngờ.",
            "options": ["案外（あんがい）", "あいにく", "わざと", "せっかく"],
            "ans": 1,
            "cute_right_msg": "Chính xác! Phó từ `案外（あんがい）` = bất ngờ khác với vẻ ngoài/dự đoán ban đầu ('tưởng thế nhưng hóa ra lại...')! 🌟",
            "right_exp": "`案外（あんがい）` ≈ `意外に` (ngoài dự đoán, hóa ra lại... hơn mình tưởng ban đầu).",
            "cute_wrong_msg": "Nhìn sự đối lập 'bề ngoài nhìn khó gần ↔ thực chất lại dịu dàng hơn mình nghĩ': phó từ diễn tả điều bất ngờ khác dự đoán ban đầu là `案外（あんがい）` nha em! 💖",
            "wrong_exps": [
                "Chính xác! `案外優しい` = dịu dàng hơn tưởng tượng rất nhiều.",
                "`あいにく` = thật không may đúng lúc...",
                "`わざと` = cố tình làm điều xấu/trêu chọc.",
                "`せっかく` = cất công quý giá lắm mới..."
            ],
            "source_ref": {"novel": "yandere", "chapter": 11, "lesson_id": "p2_c04_b03", "label": "Bộ 2 Yandere Ch.11 (Phó từ 3)"}
        },
        {
            "num": 10,
            "mondai": "問題4：文脈規定",
            "mondai_vi": "Điền từ vựng theo ngữ cảnh",
            "prompt": "今度のテストで満点を取るなんて、（　　）無理だろうと最初から諦めていた。",
            "prompt_vi": "Chuyện đạt điểm tuyệt đối trong bài kiểm tra lần này thì đằng nào cũng bất khả thi thôi nên tôi đã bỏ cuộc ngay từ đầu rồi.",
            "options": ["どうせ", "せめて", "ろくに", "かならず"],
            "ans": 1,
            "cute_right_msg": "Quá chuẩn!! Cặp phó từ hô ứng `どうせ〜だろう / 〜ない` ('đằng nào thì cũng...') siêu hay gặp trong Yandere Ch.10! 💡",
            "right_exp": "`どうせ`: Dù thế nào đi nữa thì đằng nào cũng... (mang sắc thái buông xuôi hoặc bi quan cho trước kết quả không đổi).",
            "cute_wrong_msg": "Nghe giọng điệu 'đằng nào cũng vô phương nên bỏ cuộc từ đầu': phó từ hô ứng buông xuôi đó chính là `どうせ` nha em (`せめて` nghĩa tích cực hơn: 'ít nhất thì cho tôi...')! 🌸",
            "wrong_exps": [
                "Chính xác! `どうせ無理だろう` = đằng nào cũng không nổi đâu.",
                "`せめて` = ít nhất thì (mong ước tối thiểu).",
                "`ろくに` = chẳng làm ra hồn (`ろくに〜ない`).",
                "`かならず` = chắc chắn (không hợp vế bi quan bỏ cuộc `無理` ở đây)."
            ],
            "source_ref": {"novel": "yandere", "chapter": 10, "lesson_id": "p2_c04_b02", "label": "Bộ 2 Yandere Ch.10 (Phó từ hô ứng)"}
        },
        {
            "num": 11,
            "mondai": "問題5：言い換え類義",
            "mondai_vi": "Từ / cụm từ đồng nghĩa",
            "prompt": "明日のピクニックを楽しみにしていたのに、<u>あいにく</u>朝から雨が降り出した。",
            "prompt_vi": "Đã háo hức mong chờ chuyến dã ngoại ngày mai thế rồi mà thật không may từ sáng trời lại đổ mưa.",
            "options": ["都合の悪いことに", "幸いなことに", "思っていた通り", "あっという間に"],
            "ans": 1,
            "cute_right_msg": "Chuẩn luôn! `あいにく` = thật xui xẻo / thật không đúng lúc (`都合の悪いことに`)! ☔",
            "right_exp": "`あいにく` = thật không may, đúng lúc không mong muốn lại xảy ra chuyện bất lợi (`あいにく留守・雨だ`).",
            "cute_wrong_msg": "Đang mong đi chơi thì trời mưa: phó từ cảm thán 'thật éo le không may đúng lúc' `あいにく` = `都合の悪いことに` nha em! 🌦️",
            "wrong_exps": [
                "Chính xác! `あいにく` = thật bất tiện không may đúng lúc.",
                "`幸いなことに` = may mắn thay (trái nghĩa!).",
                "`思っていた通り` = đúng như dự đoán.",
                "`あっという間に` = trong chớp mắt."
            ],
            "source_ref": {"novel": "yandere", "chapter": 11, "lesson_id": "p2_c04_b03", "label": "Bộ 2 Yandere Ch.11 (Phó từ 3)"}
        },
        {
            "num": 12,
            "mondai": "問題5：言い換え類義",
            "mondai_vi": "Từ / cụm từ đồng nghĩa",
            "prompt": "深夜まで働いた翌日は、朝ご飯を<u>ろくに</u>食べられずに出社することも多い。",
            "prompt_vi": "Hôm sau ngày làm tới khuya, có nhiều hôm tôi chẳng ăn uống bữa sáng được ra hồn đã phải đi làm rồi.",
            "options": ["お腹いっぱい", "十分にきちんと", "嬉しそうに", "ゆっくり静かに"],
            "ans": 2,
            "cute_right_msg": "Chuẩn bài!! `ろくに〜ない` = không được đầy đủ / chẳng ra hồn (`十分に〜できない`)! 🍚",
            "right_exp": "`ろくに〜ない`: Không làm một việc gì đó cho tử tế, đầy đủ đàng hoàng (`十分に〜ない`).",
            "cute_wrong_msg": "Đừng nhìn chữ `食べられずに` (không thể ăn...) rồi chọn sai nha! `ろくに` đứng trước thể phủ định nghĩa là 'không ăn được **đàng hoàng tử tế** (`十分に`)' đó em! 🌸",
            "wrong_exps": [
                "`お腹いっぱい` là ăn no căng bụng.",
                "Chính xác! `ろくに＋ない` = `十分に・きちんと＋ない` (chẳng làm tử tế đàng hoàng).",
                "`嬉しそうに` = trông vẻ vui mừng.",
                "`ゆっくり静かに` = thong thả yên tĩnh."
            ],
            "source_ref": {"novel": "yandere", "chapter": 10, "lesson_id": "p2_c04_b02", "label": "Bộ 2 Yandere Ch.10 (Phó từ hô ứng)"}
        },
        {
            "num": 13,
            "mondai": "問題5：言い換え類義",
            "mondai_vi": "Từ / cụm từ đồng nghĩa",
            "prompt": "その問題については、一度二人で<u>腹を割って話そう</u>じゃないか。",
            "prompt_vi": "Về vấn đề đó, hai đứa mình hãy thử ngồi xuống nói thẳng hết ruột gan với nhau một lần xem sao.",
            "options": ["互いに隠さず本音で話し合おう", "怒りを抑えて黙っていよう", "笑いながら冗談を言い合おう", "それぞれ別の部屋で考えよう"],
            "ans": 1,
            "cute_right_msg": "Tuyệt vời! Quán dụng kết thúc bộ Yandere Ch.12: `腹を割って話す` = mổ bụng trải lòng, nói hết tâm tư thật không giấu giếm! ❤️",
            "right_exp": "`腹を割って話す`: Mở lòng nói hết suy nghĩ thực sự từ đáy lòng với đối phương, không che giấu khách sáo.",
            "cute_wrong_msg": "Thành ngữ nổi tiếng Yandere Ch.12 nè em: 'mở lòng phơi bày hết' (`腹を割って`) có nghĩa là **nói hết tâm sự thật lòng chẳng giấu giếm** (`本音で話し合う`) nhé! 🌸",
            "wrong_exps": [
                "Chính xác! `本音で話し合う` = nói thẳng thật lòng không giấu giếm.",
                "Im lặng kiềm nén là ngược hoàn toàn.",
                "Cười đùa nói phét cũng sai sắc thái thẳng thắn nghiêm túc.",
                "Tách nhau ra tự nghĩ càng ngược lại."
            ],
            "source_ref": {"novel": "yandere", "chapter": 12, "lesson_id": "p2_c06_b02", "label": "Bộ 2 Yandere Ch.12 (Quán dụng ngữ 2)"}
        },
        {
            "num": 14,
            "mondai": "問題6：用法",
            "mondai_vi": "Cách dùng từ đúng trong câu",
            "prompt": "次の言葉の使い方として最もよいものを、1・2・3・4から一つ選びなさい。\n【言葉：<b><u>わざわざ</u></b>】",
            "prompt_vi": "Chọn câu sử dụng đúng nhất từ 【わざわざ】 (cất công bỏ công sức làm việc không bắt buộc).",
            "options": [
                "お腹が空いたので、わざわざ冷蔵庫からパンを出して食べた。",
                "雨の中、こんな遠くの家までわざわざ来てくださってありがとうございます。",
                "毎日電車が時間通りに来るので、わざわざ通勤に便利だ。",
                "テストの点数が悪くて、先生にわざわざ怒られてしまった。"
            ],
            "ans": 2,
            "cute_right_msg": "Bắt trọn sắc thái cảm ơn của `わざわざ` (cất công làm điều không bắt buộc vì ai đó / mục đích riêng) luôn! 🙏💕",
            "right_exp": "`わざわざ`: Chủ động bỏ công bỏ sức, lặn lội làm một việc không bắt buộc (dùng khi cảm ơn khách/bạn bỏ công ghé thăm hoặc bản thân cất công đi tận nơi). Khác hoàn toàn với `わざと` (cố tình chơi xấu).",
            "cute_wrong_msg": "Phân biệt cặp siêu hay nhầm `わざわざ` vs `わざと` nha em: `わざわざ` là **cất công tốn sức bỏ thời gian để làm điều quý giá / chu đáo** (như đội mưa ghé thăm), KHÔNG dùng cho việc sinh hoạt đương nhiên như mở tủ lạnh khi đói đâu nhé! 🌸",
            "wrong_exps": [
                "Đói tự lấy bánh mì ăn là chuyện bình thường hiển nhiên, không ai gọi là 'cất công' (`わざわざ`).",
                "Chính xác tuyệt đối! Cảm ơn bạn đã lặn lội đội mưa cất công tới tận nhà (`わざわざ来てくださって`).",
                "`とても・非常に便利だ` mới đúng, không dùng `わざわざ`.",
                "Bị thầy mắng ngoài ý muốn không dùng `わざわざ` (và thầy mắng cũng không gọi là 'cất công' theo nghĩa này)."
            ],
            "source_ref": {"novel": "yandere", "chapter": 11, "lesson_id": "p2_c04_b03", "label": "Bộ 2 Yandere Ch.11 (Phó từ 3)"}
        },
        {
            "num": 15,
            "mondai": "問題6：用法",
            "mondai_vi": "Cách dùng từ đúng trong câu",
            "prompt": "次の言葉の使い方として最もよいものを、1・2・3・4から一つ選びなさい。\n【言葉：<b><u>足が棒になる</u></b>】",
            "prompt_vi": "Chọn câu sử dụng đúng nhất từ 【足が棒になる】 (đi bộ/đứng quá nhiều khiến chân mỏi nhừ cứng đơ).",
            "options": [
                "スキーで転んで足の骨を折り、足が棒になって病院へ運ばれた。",
                "遊園地で一日中歩き回って並んだせいで、足が棒になった。",
                "スポーツをして毎日足が棒になるので、だんだん筋肉がついてきた。",
                "狭い椅子にずっと座っていたら、頭が痛くて足が棒になった。"
            ],
            "ans": 2,
            "cute_right_msg": "Chuẩn đét! `足が棒になる` = đứng/đi bộ nhiều cả ngày đến mức mỏi nhừ chân cứng như khúc gỗ! 🎡👟",
            "right_exp": "`足が棒になる`: Chỉ cảm giác mỏi nhừ chân không nhấc nổi bước nữa sau khi đi bộ hoặc đứng liên tục hàng giờ liền.",
            "cute_wrong_msg": "Thành ngữ `足が棒になる` diễn tả đôi chân **mỏi nhừ vì đi bộ hoặc đứng quá nhiều**, chứ KHÔNG phải bị gãy xương bó bột hay đi tập gym lên cơ bắp đâu nha em! 🌸",
            "wrong_exps": [
                "Gãy xương là chấn thương bệnh lý `骨折した` (chứ không phải thành ngữ mỏi chân).",
                "Chính xác! Cả ngày đi bộ xếp hàng trong công viên giải trí nên mỏi nhừ chân (`足が棒になった`).",
                "Tập luyện khỏe lên lên cơ bắp là tích cực, không dùng thành ngữ mỏi rã rời.",
                "Ngồi một chỗ không phải đi lại nhiều làm mỏi chân."
            ],
            "source_ref": {"novel": "yandere", "chapter": 12, "lesson_id": "p2_c06_b02", "label": "Bộ 2 Yandere Ch.12 (Quán dụng ngữ 2)"}
        },
        {
            "num": 16,
            "mondai": "問題6：用法",
            "mondai_vi": "Cách dùng từ đúng trong câu",
            "prompt": "次の言葉の使い方として最もよいものを、1・2・3・4から一つ選びなさい。\n【言葉：<b><u>ついつい</u></b>】",
            "prompt_vi": "Chọn câu sử dụng đúng nhất từ 【ついつい / つい】 (dù biết không nên nhưng vô thức lỡ làm theo thói quen/cám dỗ).",
            "options": [
                "夜遅いから寝ようと思っても、面白い漫画があるとついつい読んでしまう。",
                "明日の朝は6時に起きなければならないので、目覚まし時計をついついかけた。",
                "上司に褒められたくて、毎日1時間前に会社へついつい出勤している。",
                "信号が赤になったので、道路の真ん中でついつい止まって待っていた。"
            ],
            "ans": 1,
            "cute_right_msg": "Quá chuẩn!! `ついつい〜てしまう` = dù tự nhủ không nên nhưng lỡ bị cuốn vào thói quen xấu/cám dỗ! 📖✨",
            "right_exp": "`つい / ついつい`: Bất giác lỡ làm hành động dù bản thân định kiềm chế hoặc vô thức lặp lại (`ついつい食べてしまう・夜更かししてしまう`). Luôn kết hợp `〜てしまう`, không dùng cho hành động có chủ ý tích cực (đặt báo thức, tuân thủ luật giao thông).",
            "cute_wrong_msg": "`ついつい` luôn diễn tả hành động **vô thức không kìm được** (`ダイエット中なのについついケーキを食べちゃった`), KHÔNG dùng cho việc có kế hoạch chủ đích như đặt đồng hồ báo thức hay dừng đèn đỏ nha em! 💖",
            "wrong_exps": [
                "Chính xác tuyệt đối! Định đi ngủ sớm mà thấy truyện hay lại lỡ đọc miết (`ついつい読んでしまう`).",
                "Đặt báo thức vì phải dậy sớm là hành động có kế hoạch chủ động.",
                "Đi làm sớm vì muốn được sếp khen cũng là cố ý có mục tiêu rõ ràng.",
                "Dừng đèn đỏ là tuân thủ quy tắc có ý thức."
            ],
            "source_ref": {"novel": "yandere", "chapter": 11, "lesson_id": "p2_c04_b03", "label": "Bộ 2 Yandere Ch.11 (Phó từ 3)"}
        },
        {
            "num": 17,
            "mondai": "問題7：文の文法1",
            "mondai_vi": "Ngữ pháp câu N2",
            "prompt": "どれほど好きになった相手（　　）、プライバシーまで勝手に調べる権利はないはずだ。",
            "prompt_vi": "Dẫu cho có yêu thích đối phương đến nhường nào đi chăng nữa, cũng chẳng có quyền gì tự tiện lục lọi đời tư của họ được.",
            "options": ["だとしても", "だからといって", "ばかりに", "こととて"],
            "ans": 1,
            "cute_right_msg": "Chuẩn thông điệp Bộ Yandere luôn!! `どれほど〜だとしても` (dù cho có thích tới đâu đi nữa thì vẫn...)! 🖤💌",
            "right_exp": "`どれほど〜だとしても`: Dù cho giả định có đến mức X đi chăng nữa (`どんなに・どれほど〜だとしても`). (Lưu ý: không có dạng tiếp nối N + だからといって — phải là `N + だからといって` nhưng chữ `どれほど` luôn hô ứng với `ても / としても`, KHÔNG hô ứng với `だからといって`!).",
            "cute_wrong_msg": "Chú ý từ để hỏi `どれほど` ở đầu câu nhượng bộ nhé em! `どれほど・いくら・どんなに` luôn cặp đôi với `〜ても / 〜としても` (`どれほど好きだとしても`), không đi cùng `だからといって` đâu nha! 🌸",
            "wrong_exps": [
                "Chính xác! `どれほど〜だとしても` = dù có yêu đến mức nào đi nữa.",
                "`だからといって` không kết hợp tự nhiên với `どれほど` ở mệnh đề nhượng bộ tổng quát.",
                "`ばかりに` = chỉ tại vì lỡ X nên kết quả xấu.",
                "`こととて` = vì là hoàn cảnh đặc biệt..."
            ],
            "source_ref": {"novel": "yandere", "chapter": 3, "lesson_id": "p1_c06_b02", "label": "Ngữ pháp N2 — 譲歩（〜だとしても）"}
        },
        {
            "num": 18,
            "mondai": "問題7：文の文法1",
            "mondai_vi": "Ngữ pháp câu N2",
            "prompt": "鍵がどこにも見当たらないのだが、さっきカバンに（　　）つもりだったのに……。",
            "prompt_vi": "Chẳng thấy chìa khóa đâu cả, rõ ràng lúc nãy tôi cứ đinh ninh là đã bỏ vào túi xách rồi thế mà...",
            "options": ["入れた", "入れる", "入れておく", "入らない"],
            "ans": 1,
            "cute_right_msg": "Chuẩn 100 điểm!! Cặp ngữ pháp lừa siêu hay `Vた + つもり` = ĐINH NINH TƯỞNG NHẦM rằng mình đã làm rồi thế mà thực tế lại quên chưa bỏ vào! 🔑✨",
            "right_exp": "`Vた + つもりだ / だった`: Cứ đinh ninh tưởng là mình đã làm V rồi (thực chất là nhầm hoặc không phải vậy). Khác với `Vる + つもり` (dự định tương lai).",
            "cute_wrong_msg": "Soi ngữ cảnh 'tìm chìa khóa khắp nơi chẳng thấy đâu': hành động trong trí nhớ tưởng là ĐÃ bỏ vào túi (`入れたつもり`) rồi thế mà hóa ra không có trong túi đó em! 💡",
            "wrong_exps": [
                "Chính xác! `入れたつもりだった` = cứ tưởng chắc mẩm mình đã bỏ vào rồi chứ.",
                "`入れるつもりだった` là 'đã dự định bỏ vào nhưng cuối cùng không bỏ', không nhấn cảm giác 'đinh ninh trong trí nhớ đã cất rồi' khi đang tìm đồ thất lạc bằng `入れたつもり`.",
                "`入れておく` ở thì hiện tại không khớp ý nhớ nhầm quá khứ.",
                "`入らない` ngược nghĩa."
            ],
            "source_ref": {"novel": "yandere", "chapter": 5, "lesson_id": "p2_c01_b01", "label": "Ngữ pháp N2 — 錯覚（〜たつもりが）"}
        },
        {
            "num": 19,
            "mondai": "問題7：文の文法1",
            "mondai_vi": "Ngữ pháp câu N2",
            "prompt": "彼女の微笑みを見る（　　）、最初は優しいと思ったのに、どこか背筋が冷たくなる気もした。",
            "prompt_vi": "Càng nhìn nụ cười của cô ấy — ban đầu cứ ngỡ hiền dịu — tôi lại cảm thấy có gì đó lạnh sống lưng.",
            "options": ["につけ", "ばかりに", "ことなしに", "だけに"],
            "ans": 1,
            "cute_right_msg": "Chất Yandere lạnh gáy quá đỉnh luôn!! `〜につけ` (hễ cứ mỗi lần nhìn thấy/nghe thấy là tự nhiên lại cảm thấy...)! 🌹❄️",
            "right_exp": "`Vる / Aい / N + につけ`: Hễ cứ khi làm/thấy điều X là tự nhiên trong lòng lại nảy sinh suy nghĩ/cảm xúc Y (`見るにつけ・聞くにつけ・季節が変わるにつけ`).",
            "cute_wrong_msg": "Mỗi lần bắt gặp nụ cười ấy thì lại bất giác dấy lên cảm giác ớn lạnh: mẫu 'hễ cứ mỗi lần... là lòng lại tự nhiên...' là `Vる + につけ` nha em! 🖤",
            "wrong_exps": [
                "Chính xác! `見るにつけ〜気がした` = hễ cứ nhìn thấy là lại cảm thấy...",
                "`ばかりに` = chỉ tại vì X nên kết quả tồi tệ xảy ra (mâu thuẫn 'nụ cười dịu dàng').",
                "`ことなしに` = mà không cần làm X.",
                "`だけに` = chính vì là nụ cười dịu dàng nên xứng đáng lạnh sống lưng (phi logic!)."
            ],
            "source_ref": {"novel": "yandere", "chapter": 1, "lesson_id": "p1_c01_b03", "label": "Ngữ pháp N2 — 契機（〜につけ）"}
        },
        {
            "num": 20,
            "mondai": "問題8：文の文法2 ★",
            "mondai_vi": "Sắp xếp thành phần câu",
            "prompt": "小百合は、海斗の ＿＿＿ ＿＿＿ ★ ＿＿＿ 彼を見つめていた。",
            "prompt_vi": "Sayuri chăm chú ngắm nhìn Kaito như thể đã nhìn thấu tất thảy mọi điều sâu thẳm trong trái tim anh vậy.",
            "options": ["見透かした", "すべてを", "心の中の", "かのように"],
            "ans": 1,
            "cute_right_msg": "Đỉnh của chóp!! Thứ tự chuẩn từng chút: `[3] 心の中の → [2] すべてを → ★[1] 見透かした → [4] かのように`! 🖤✨",
            "right_exp": "Ghép chuẩn xác: `海斗の [3]心の中の [2]すべてを ★[1]見透かした [4]かのように 彼を見つめていた。`\n- `海斗の` + `[3]心の中の` + `[2]すべてを` (tất cả mọi thứ trong tâm trí Kaito).\n- `[1]見透かした` (đã nhìn thấu suốt) + `[4]かのように` (`〜たかのように`: cứ như thể là...).\n→ Vị trí dấu ★ là **1 (`見透かした`)**!",
            "cute_wrong_msg": "Bắt ngay bộ đôi `[4] かのように` (đi sau động từ chia thể Vた là `[1] 見透かした`) ở vị trí cuối nha em! Còn phía trước `海斗の + 心の中の + すべてを` ghép lại vừa in luôn~ 🌸",
            "wrong_exps": [
                "Chính xác tuyệt đối! Vị trí ★ là `[1] 見透かした` (`3 → 2 → 1 → 4`).",
                "`[2] すべてを` đứng ở ô số 2.",
                "`[3] 心の中の` đứng ở ô số 1.",
                "`[4] かのように` đứng ở ô số 4 (`Vた＋かのように`)."
            ],
            "source_ref": {"novel": "yandere", "chapter": 6, "lesson_id": "p2_c01_b02", "label": "Ngữ pháp N2 ★ — 〜かのように"}
        },
    ]
}

EXAM_REVIEW_ISEKAI = {
    "id": "review-isekai",
    "code": "ÔN TẬP BỘ 3 • ISEKAI N2",
    "title_jp": "【Isekai復習テスト】最強王国を創る語彙マスター（20問）",
    "title_vi": "Đề Ôn Tập Nhanh Bộ 3: Isekai (12 Bài • 20 Câu Chuẩn JLPT)",
    "category": "review",
    "novel_id": "isekai",
    "duration_min": 20,
    "pass_score": 12,
    "max_score": 20,
    "description": "Bài kiểm tra tổng ôn toàn bộ 12 bài học Shinkanzen N2 cuối sách (Thiên nhiên, Kinh tế, Chính trị-Luật, Sinh thái, Khoa học, Số lượng, Thời-Không gian, Onomatopoeia, Toàn bộ Cấu tạo từ & Chuyển đổi từ loại) cùng lãnh chúa Yūma!",
    "yuki_note_start": "Chúc mừng em đã đi hết hành trình vương quốc Eldia trong **Bộ 3 Isekai**!! ⚔️✨ Đây là 20 câu tổng ôn cực chất phủ trọn cả 12 bài còn lại — đặc biệt kiểm tra phần **Cấu tạo từ (語形成)** và **Từ tượng thanh/tượng hình (オノマトペ)** siêu hay thi JLPT N2 đó nha~ Bung hết công lực nào em! 🌸",
    "yuki_note_finish_pass": "QUÁ XUẤT SẮC LUÔN!! Vậy là cả 3 bộ Romcom — Yandere — Isekai cùng 780 từ Shinkanzen đều đã nằm gọn trong tầm tay em rồi! Sẵn sàng bước vào 3 Bộ Đề Full JLPT N2 ngay thôi nè 🏆🎉",
    "yuki_note_finish_try": "Ủa cố lên một xíu nữa thôi em yêu~ Phần Cấu tạo từ và Số lượng trong Bộ Isekai hơi nhiều từ Hán-Nhật học thuật một chút đó mà! Lướt lại bảng giải thích chi tiết từng câu là nạp lại 100% mana liền hà 💖✨",
    "questions": [
        {
            "num": 1,
            "mondai": "問題1：漢字読み",
            "mondai_vi": "Cách đọc Kanji",
            "prompt": "この山の<u>標高</u>は二千メートルを超えている。",
            "prompt_vi": "Độ cao so với mực nước biển của ngọn núi này vượt quá hai nghìn mét.",
            "options": ["ひょうこう", "ひょうたか", "しゅこう", "びょうこう"],
            "ans": 1,
            "cute_right_msg": "Chính xác! `標高（ひょうこう）` = độ cao so với mực nước biển (Ch.01 Isekai)! 🏔️",
            "right_exp": "`標高` đọc theo âm On là **ひょうこう** (Tiêu Cao).",
            "cute_wrong_msg": "Đọc âm On cho chữ Tiêu (`ひょう` trong `標準`) + Cao (`こう` trong `高速`) = `ひょうこう` nha em! ✨",
            "wrong_exps": [
                "Chính xác! `標高（ひょうこう）`.",
                "Không ghép On + Kun thành `ひょうたか`.",
                "`しゅこう` không phải âm của `標高`.",
                "`びょうこう` nhầm thanh đục chữ `標` (`ひょう`)."
            ],
            "source_ref": {"novel": "isekai", "chapter": 1, "lesson_id": "p1_c04_b02", "label": "Bộ 3 Isekai Ch.01 (Thiên nhiên)"}
        },
        {
            "num": 2,
            "mondai": "問題2：表記",
            "mondai_vi": "Chọn Kanji đúng",
            "prompt": "海外から多くのエネルギー資源を<u>ゆにゅう</u>している。",
            "prompt_vi": "Đất nước đang nhập khẩu rất nhiều tài nguyên năng lượng từ nước ngoài.",
            "options": ["輸人", "入輸", "輸入", "由入"],
            "ans": 3,
            "cute_right_msg": "Quá chuẩn! `輸入（ゆにゅう）` = nhập khẩu (đưa hàng từ ngoài VÀO trong nước)! 🚢📦",
            "right_exp": "`輸入（ゆにゅう）` = Nhập khẩu (ngược với `輸出（ゆしゅつ）` = Xuất khẩu).",
            "cute_wrong_msg": "Nhớ trật tự Kanji tiếng Nhật hơi ngược tiếng Việt mình chút nha em: ở Nhật dùng chữ **輸** (vận chuyển) đứng trước chữ **入** (nhập vào) = `輸入` / `輸出` đó! 🌏",
            "wrong_exps": [
                "`輸人` viết nhầm bộ Nhân `人` thay vì `入`.",
                "Ngược thứ tự Kanji: tiếng Nhật viết `輸入` chứ không viết `入輸`.",
                "Chính xác tuyệt đối! `輸入（ゆにゅう）` = nhập khẩu.",
                "`由入` không phải từ này."
            ],
            "source_ref": {"novel": "isekai", "chapter": 2, "lesson_id": "p1_c07_b03", "label": "Bộ 3 Isekai Ch.02 (Kinh tế)"}
        },
        {
            "num": 3,
            "mondai": "問題3：語形成",
            "mondai_vi": "Cấu tạo từ (Tiền tố / Hậu tố)",
            "prompt": "新幹線が開通したことで、空港へのアクセスが良く（　　）<u>性</u>が高まった。",
            "prompt_vi": "Nhờ tàu cao tốc khai thông, tính tiện lợi kết nối đến sân bay đã được nâng cao rõ rệt.",
            "options": ["利便", "専門", "危険", "安全"],
            "ans": 1,
            "cute_right_msg": "Quá xịn!! `利便性（りべんせい）` (tính tiện lợi) là từ vựng báo chí N2 cực chuẩn khi nói về giao thông và dịch vụ! 🚄✨",
            "right_exp": "`利便性（りべんせい）` = tính tiện ích, sự thuận tiện trong tiếp cận giao thông/dịch vụ (`アクセスが良く〜が高まった`).",
            "cute_wrong_msg": "Tàu Shinkansen mới mở giúp đường ra sân bay thuận tiện hơn nhiều: tính tiện lợi/thuận tiện ghép với `〜性` là `利便性（りべんせい）` nha em! (Nếu nghĩ về an toàn không liên quan trực tiếp đến 'giao thông nhanh thuận tiện' bằng `利便性`) 🌸",
            "wrong_exps": [
                "Chính xác! `利便性（りべんせい）` = tính thuận tiện, tiện ích.",
                "`専門性` = tính chuyên môn.",
                "`危険性` = nguy cơ rủi ro (ngược nghĩa!).",
                "`安全性` = tính an toàn (lệch gợi ý `アクセスが良く` thuận tiện)."
            ],
            "source_ref": {"novel": "isekai", "chapter": 11, "lesson_id": "p2_c07_b03", "label": "Bộ 3 Isekai Ch.11 (Hậu tố 〜性)"}
        },
        {
            "num": 4,
            "mondai": "問題3：語形成",
            "mondai_vi": "Cấu tạo từ (Tiền tố / Hậu tố)",
            "prompt": "プラスチックごみを減らすため、ペットボトルの（　　）<u>利用</u>が進められている。",
            "prompt_vi": "Để giảm rác thải nhựa, hoạt động tái sử dụng chai nhựa PET đang được đẩy mạnh.",
            "options": ["無", "再", "非", "不"],
            "ans": 2,
            "cute_right_msg": "Chuẩn không cần chỉnh! Chai nhựa giảm rác bằng cách **tái sử dụng** = `再利用（さいりよう）`! ♻️✨",
            "right_exp": "`再利用（さいりよう）` = tái sử dụng (tiền tố **再** đứng trước `利用` nhằm giảm rác thải nhựa).",
            "cute_wrong_msg": "Cứ thấy rác thải tái chế chai nhựa dùng lại nhiều lần là tiền tố `再（さい）` (`再利用`) nha em! ♻️",
            "wrong_exps": [
                "`無利用` không tự nhiên (khác với `無料` miễn phí).",
                "Chính xác! `再利用（さいりよう）` = tái sử dụng.",
                "`非利用` không phải từ dùng thông dụng.",
                "`不利用` không tồn tại."
            ],
            "source_ref": {"novel": "isekai", "chapter": 10, "lesson_id": "p2_c07_b02", "label": "Bộ 3 Isekai Ch.10 (Tiền tố 再〜)"}
        },
        {
            "num": 5,
            "mondai": "問題4：文脈規定",
            "mondai_vi": "Điền từ vựng theo ngữ cảnh",
            "prompt": "今回の選挙で、新しい政策を（　　）する議員が過半数を占めた。",
            "prompt_vi": "Trong cuộc bầu cử lần này, các nghị sĩ ủng hộ chính sách mới đã chiếm đa số quá bán.",
            "options": ["支持（しじ）", "裁判（さいばん）", "罰（ばっ）", "違反（いはん）"],
            "ans": 1,
            "cute_right_msg": "Quá chuẩn!! Trong bầu cử chính trị Isekai Ch.03: cử tri / nghị sĩ ủng hộ chính sách hay đảng phái dùng `支持（しじ）する`! 🗳️✨",
            "right_exp": "`支持（しじ）する` = ủng hộ chính kiến, đảng phái, người lãnh đạo (`政策を支持する`).",
            "cute_wrong_msg": "Ủng hộ đường lối chính sách trong nghị trường là `支持（しじ）する` (Chi Trì), tránh nhầm với `指示（しじ）` (chỉ thị ra lệnh) nhé em! 🏛️",
            "wrong_exps": [
                "Chính xác! `政策を支持する` = ủng hộ chính sách.",
                "`裁判` là phiên tòa xét xử.",
                "`罰する` là trừng phạt.",
                "`違反する` là vi phạm luật."
            ],
            "source_ref": {"novel": "isekai", "chapter": 3, "lesson_id": "p1_c07_b04", "label": "Bộ 3 Isekai Ch.03 (Chính trị)"}
        },
        {
            "num": 6,
            "mondai": "問題4：文脈規定",
            "mondai_vi": "Điền từ vựng theo ngữ cảnh",
            "prompt": "太陽の光を受けて（　　）が酸素を作り出す働きを光合成という。",
            "prompt_vi": "Quá trình cây cối thực vật hấp thụ ánh sáng mặt trời để tạo ra khí oxy gọi là quang hợp.",
            "options": ["植物（しょくぶつ）", "装置（そうち）", "遺跡（いせき）", "宇宙（うちゅう）"],
            "ans": 1,
            "cute_right_msg": "Chuẩn bài Sinh thái Isekai Ch.04!! `植物（しょくぶつ）` + `酸素（さんそ）` + `光合成` = bộ ba sinh học kinh điển! 🌿☀️",
            "right_exp": "`植物（しょくぶつ）` = thực vật cây cối (sản sinh ra khí oxy nhờ quang hợp `光合成`).",
            "cute_wrong_msg": "Đọc từ khóa 'tạo ra khí oxy dưới ánh mặt trời gọi là quang hợp': sinh vật thực hiện quá trình đó là `植物` (thực vật) đó em~ 🌱",
            "wrong_exps": [
                "Chính xác! `植物` = thực vật.",
                "`装置` = thiết bị máy móc.",
                "`遺跡` = di tích cổ đại.",
                "`宇宙` = vũ trụ không gian."
            ],
            "source_ref": {"novel": "isekai", "chapter": 4, "lesson_id": "p1_c08_b01", "label": "Bộ 3 Isekai Ch.04 (Sinh thái)"}
        },
        {
            "num": 7,
            "mondai": "問題4：文脈規定",
            "mondai_vi": "Điền từ vựng theo ngữ cảnh",
            "prompt": "新技術が発表されてからわずか半年で一般向けに（　　）され、家庭でも使えるようになった。",
            "prompt_vi": "Chỉ vỏn vẹn nửa năm sau khi công nghệ mới được công bố, nó đã được đưa vào ứng dụng thực tế cho người dùng phổ thông và có thể dùng ngay tại nhà.",
            "options": ["実用化（じつようか）", "蒸発（じょうはつ）", "合併（がっぺい）", "倒産（とうさん）"],
            "ans": 1,
            "cute_right_msg": "Quá chuẩn!! Quá trình từ phòng lab chuyển sang dùng đại trà ngoài đời thực là `実用化（じつようか）` (Ch.05 Khoa học)! 🔬⚙️",
            "right_exp": "`実用化（じつようか）` = đưa một phát minh/nghiên cứu vào áp dụng thực tế trong đời sống sản xuất.",
            "cute_wrong_msg": "Vế sau bảo 'ở gia đình cũng có thể sử dụng được rồi': công nghệ mới từ nghiên cứu chuyển sang dùng thực tế là `実用化される` nha em! 💡",
            "wrong_exps": [
                "Chính xác! `実用化される` = được đưa vào ứng dụng thực tế.",
                "`蒸発する` = bay hơi nước.",
                "`合併する` = hai công ty sáp nhập làm một.",
                "`倒産する` = công ty phá sản."
            ],
            "source_ref": {"novel": "isekai", "chapter": 5, "lesson_id": "p1_c08_b02", "label": "Bộ 3 Isekai Ch.05 (Khoa học công nghệ)"}
        },
        {
            "num": 8,
            "mondai": "問題4：文脈規定",
            "mondai_vi": "Điền từ vựng theo ngữ cảnh",
            "prompt": "この会議室には（　　）50人前後の社員が集まっている。",
            "prompt_vi": "Trong phòng họp này đang tập trung xấp xỉ khoảng chừng 50 nhân viên.",
            "options": ["およそ", "わずか", "さらに", "いまだ"],
            "ans": 1,
            "cute_right_msg": "Chuẩn luôn! `およそ50人前後` = khoảng chừng trên dưới 50 người (từ Ch.06 Số lượng)! 🔢",
            "right_exp": "`およそ` đứng trước con số chỉ sự ước lượng 'khoảng chừng' (có thể dùng cùng `〜前後 / 〜ほど` để ước đoán trên dưới).",
            "cute_wrong_msg": "Phó từ đứng trước số ước lượng 'khoảng chừng 50 người' trong Isekai Ch.06 là `およそ`, còn `わずか` là 'chỉ vỏn vẹn ít ỏi' (mâu thuẫn khi chẳng nêu mốc ít hay nhiều so với sức chứa, ở đây chỉ ước đoán trung tính + `前後` nữa nên `およそ` tự nhiên nhất)! 🌸",
            "wrong_exps": [
                "Chính xác! `およそ50人前後` = khoảng chừng 50 người.",
                "`わずか` nhấn mạnh số ít ỏi vỏn vẹn và không đi mượt với cặp ước đoán trên dưới `前後` bằng `およそ`.",
                "`さらに` = thêm vào đó nữa là.",
                "`いまだ` = đến tận bây giờ vẫn chưa..."
            ],
            "source_ref": {"novel": "isekai", "chapter": 6, "lesson_id": "p1_c09_b01", "label": "Bộ 3 Isekai Ch.06 (Số lượng)"}
        },
        {
            "num": 9,
            "mondai": "問題4：文脈規定",
            "mondai_vi": "Điền từ vựng theo ngữ cảnh",
            "prompt": "大きな図書館の（　　）には、カフェや本屋もたくさん並んでいる。",
            "prompt_vi": "Ở khu vực xung quanh lân cận thư viện lớn, các quán cà phê và hiệu sách cũng mọc lên san sát rất nhiều.",
            "options": ["周辺（しゅうへん）", "斜面（しゃめん）", "奥（おく）", "間隔（かんかく）"],
            "ans": 1,
            "cute_right_msg": "Đúng phóc! `駅の周辺・図書館の周辺` = khu vực lân cận xung quanh một địa điểm! 🗺️✨",
            "right_exp": "`周辺（しゅうへん）` (Chu Biên) = vùng xung quanh lân cận bao quanh tòa nhà, nhà ga, trường học.",
            "cute_wrong_msg": "Khu vực nằm vây quanh một công trình lớn trong bài Không gian Ch.07 gọi là `周辺（しゅうへん）`, còn `奥（おく）` là tít sâu bên trong phòng/núi nha em! 🏛️",
            "wrong_exps": [
                "Chính xác! `図書館の周辺` = khu vực xung quanh thư viện.",
                "`斜面` = sườn dốc núi.",
                "`奥` = phía sâu tận cùng bên trong.",
                "`間隔` = khoảng cách giãn cách đều giữa các hàng."
            ],
            "source_ref": {"novel": "isekai", "chapter": 7, "lesson_id": "p1_c09_b02", "label": "Bộ 3 Isekai Ch.07 (Không gian)"}
        },
        {
            "num": 10,
            "mondai": "問題4：文脈規定",
            "mondai_vi": "Điền từ vựng theo ngữ cảnh",
            "prompt": "明日は初めての海外旅行なので、楽しみで胸が（　　）して眠れない。",
            "prompt_vi": "Vì ngày mai là chuyến du lịch nước ngoài đầu tiên nên lòng tôi háo hức rộn ràng mãi chẳng ngủ nổi.",
            "options": ["わくわく", "げっそり", "いらいら", "うっかり"],
            "ans": 1,
            "cute_right_msg": "Chuẩn 100 điểm!! Háo hức mong chờ niềm vui sắp tới = `わくわくする` (Ch.08 Onomatopoeia)! ✈️💖",
            "right_exp": "`わくわくする`: Háo hức, phấn khởi rộn ràng chờ đợi điều thú vị sắp diễn ra.",
            "cute_wrong_msg": "Cảm xúc háo hức mong chờ trước chuyến đi chơi (`楽しみで〜`) chỉ có thể là bạn `わくわく` siêu đáng yêu của Ch.08 thôi ha em! 🌸",
            "wrong_exps": [
                "Chính xác! `わくわくして眠れない` = háo hức quá chẳng ngủ nổi.",
                "`げっそり` = gầy rộc tiều tụy.",
                "`いらいら` = cáu gắt sốt ruột khó chịu.",
                "`うっかり` = lơ đễnh sơ suất."
            ],
            "source_ref": {"novel": "isekai", "chapter": 8, "lesson_id": "p2_c05_b01", "label": "Bộ 3 Isekai Ch.08 (Onomatopoeia)"}
        },
        {
            "num": 11,
            "mondai": "問題5：言い換え類義",
            "mondai_vi": "Từ / cụm từ đồng nghĩa",
            "prompt": "電車に乗り遅れないように、駅の改札を<u>ぎりぎり</u>に通り抜けた。",
            "prompt_vi": "Để không bị trễ tàu, tôi đã chạy lướt qua cổng soát vé ngay sát nút giờ chót.",
            "options": ["余裕を持って", "間に合うかどうかの瀬戸際で", "いつも通りゆっくりと", "予定よりずっと早く"],
            "ans": 2,
            "cute_right_msg": "Quá chuẩn!! `ぎりぎり` = sát nút giới hạn, suýt soát không kịp! ⏱️💨",
            "right_exp": "`ぎりぎり` = vừa khít giới hạn cuối cùng, sát nút giờ chót (`締め切りぎりぎり・ぎりぎり間に合う`).",
            "cute_wrong_msg": "Từ tượng hình `ぎりぎり` diễn tả ranh giới sát rạt 'suýt nữa thì trễ/hỏng' (`間に合うかどうかの瀬戸際`) chứ không phải thong thả sớm đâu em! 🌟",
            "wrong_exps": [
                "`余裕を持って` = dư dả thời gian thoải mái (trái nghĩa!).",
                "Chính xác! Sát nút ranh giới kịp hay không kịp.",
                "`ゆっくりと` = từ từ thong thả.",
                "`ずっと早く` = sớm hơn rất nhiều (trái nghĩa!)."
            ],
            "source_ref": {"novel": "isekai", "chapter": 8, "lesson_id": "p2_c05_b01", "label": "Bộ 3 Isekai Ch.08 (Onomatopoeia)"}
        },
        {
            "num": 12,
            "mondai": "問題5：言い換え類義",
            "mondai_vi": "Từ / cụm từ đồng nghĩa",
            "prompt": "この薬品の効果は<u>一時的</u>なものにすぎないので、根本的な治療が必要だ。",
            "prompt_vi": "Hiệu quả của loại thuốc này chẳng qua chỉ mang tính nhất thời chốc lát, nên vẫn cần trị liệu tận gốc rễ.",
            "options": ["永遠に続く", "ほんの短い間だけ続く", "非常に強力な", "まったく効果がない"],
            "ans": 2,
            "cute_right_msg": "Chính xác! `一時的（いちじてき）` = tạm thời trong chốc lát (`ほんの短い間だけ続く`) — đối lập với `永遠`! ⏳",
            "right_exp": "`一時的（いちじてき）` = chỉ diễn ra trong một khoảng thời gian ngắn tạm thời, chưa giải quyết được lâu dài vĩnh viễn.",
            "cute_wrong_msg": "Đối chiếu vế sau 'vẫn cần chữa tận gốc' là hiểu ngay `一時的` nghĩa là 'chỉ kéo dài trong chốc lát ngắn ngủi thôi' nha em! 💊",
            "wrong_exps": [
                "`永遠に続く` = kéo dài mãi mãi (trái nghĩa hoàn toàn!).",
                "Chính xác! `一時的` = tạm thời trong thời gian ngắn.",
                "`非常に強力な` = cực kỳ mạnh mẽ.",
                "`まったく効果がない` = vô hiệu hoàn toàn."
            ],
            "source_ref": {"novel": "isekai", "chapter": 7, "lesson_id": "p1_c09_b02", "label": "Bộ 3 Isekai Ch.07 (Thời gian)"}
        },
        {
            "num": 13,
            "mondai": "問題5：言い換え類義",
            "mondai_vi": "Từ / cụm từ đồng nghĩa",
            "prompt": "新しい法律が議会で承認され、国民の<u>権利</u>が大きく広がった。",
            "prompt_vi": "Đạo luật mới được thông qua tại nghị viện, mở rộng đáng kể quyền lợi của người dân.",
            "options": ["法律上認められた利益や自由", "必ず果たすべき仕事", "支払わなければならないお金", "守るべき厳しい罰則"],
            "ans": 1,
            "cute_right_msg": "Quá chuẩn!! Phân biệt rành mạch `権利（けんり）` (quyền lợi/quyền hợp pháp được hưởng) vs `義務（ぎむ）` (nghĩa vụ phải làm)! ⚖️✨",
            "right_exp": "`権利（けんり）` = quyền lợi, quyền chính đáng được pháp luật/xã hội công nhận.",
            "cute_wrong_msg": "Cặp song hành `権利` (Quyền lợi được hưởng) và `義務` (Nghĩa vụ bắt buộc phải làm) rất hay đối chiếu với nhau đó em! Câu hỏi đang hỏi `権利` nha~ 📜",
            "wrong_exps": [
                "Chính xác! `権利` = quyền lợi và sự tự do được luật pháp công nhận.",
                "Việc bắt buộc phải làm là `義務（ぎむ）`.",
                "Tiền phải nộp là `税金・代金・費用`.",
                "Hình phạt phải tuân thủ là `罰則（ばっそく）`."
            ],
            "source_ref": {"novel": "isekai", "chapter": 3, "lesson_id": "p1_c07_b04", "label": "Bộ 3 Isekai Ch.03 (Pháp luật)"}
        },
        {
            "num": 14,
            "mondai": "問題6：用法",
            "mondai_vi": "Cách dùng từ đúng trong câu",
            "prompt": "次の言葉の使い方として最もよいものを、1・2・3・4から一つ選びなさい。\n【言葉：<b><u>恵まれる</u></b>】",
            "prompt_vi": "Chọn câu sử dụng đúng nhất từ 【恵まれる（めぐまれる）】 (được ban tặng ưu đãi yếu tố tốt đẹp).",
            "options": [
                "今日はとても天気に恵まれて、素晴らしい遠足日和になった。",
                "毎日練習したおかげで、難しい試合に恵まれることができた。",
                "テストの前に風邪を引いてしまい、体調に恵まれて残念だ。",
                "レストランで注文した料理がなかなか恵まれず、30分待った。"
            ],
            "ans": 1,
            "cute_right_msg": "Chuẩn đét! `天気に恵まれる / 自然に恵まれる / 才能・機会に恵まれる` — luôn dùng cho điều **tích cực may mắn trời ban**! ☀️🌈",
            "right_exp": "`N + に恵まれる`: Được ưu ái ban tặng điều kiện tốt đẹp (`天気・自然・才能・良い友人・環境に恵まれる`). Không dùng cho điều xui rủi (`風邪`) hay hành động tự cố gắng thắng trận.",
            "cute_wrong_msg": "`〜に恵まれる` có nghĩa là *được thiên nhiên/hoàn cảnh ưu đãi ban tặng điều tốt đẹp* (thời tiết đẹp, thiên nhiên, bạn tốt, tài năng), KHÔNG dùng cho việc ốm đau hay chờ món ăn nha em! 🌸",
            "wrong_exps": [
                "Chính xác tuyệt đối! `天気に恵まれて` (được trời thương ban cho thời tiết đẹp).",
                "Thắng trận đấu dùng `勝つ・優勝する`, không dùng `試合に恵まれる`.",
                "Đổ bệnh là chuyện xui rủi tiêu cực, không dùng `恵まれる`.",
                "Món ăn mang ra dùng `運ばれる / 出される`, không dùng `恵まれる`."
            ],
            "source_ref": {"novel": "isekai", "chapter": 1, "lesson_id": "p1_c04_b02", "label": "Bộ 3 Isekai Ch.01 (Thiên nhiên)"}
        },
        {
            "num": 15,
            "mondai": "問題6：用法",
            "mondai_vi": "Cách dùng từ đúng trong câu",
            "prompt": "次の言葉の使い方として最もよいものを、1・2・3・4から一つ選びなさい。\n【言葉：<b><u>延長</u></b>】",
            "prompt_vi": "Chọn câu sử dụng đúng nhất từ 【延長（えんちょう）】 (gia hạn, kéo dài thêm thời lượng/độ dài).",
            "options": [
                "台風が近づいてきたので、今日の試合を来週の土曜日に延長した。",
                "図書館の利用者が増えたため、開館時間を夜9時まで延長した。",
                "このズボンは少し長すぎるので、店員さんに頼んで延長してもらった。",
                "期限までに間に合わなかったので、レポートの提出を中止に延長した。"
            ],
            "ans": 2,
            "cute_right_msg": "Phân biệt chuẩn 10/10 giữa `延長` (kéo dài thêm khung giờ `開館時間を延長する`) và `延期` (dời lịch sang ngày khác `来週に延期する`)! 🕰️✨",
            "right_exp": "`延長（えんちょう）する`: Kéo dài thêm khung thời gian vốn có (`営業時間の延長・ビザの延長`) hoặc nối dài độ dài tuyến đường (`鉄道の延長`). Nếu dời sự kiện sang ngày khác dùng `延期する`, cắt ngắn ống quần dùng `裾上げ・短くする`.",
            "cute_wrong_msg": "Nhắc lại quy tắc vàng Isekai Ch.07 nè em:\n- Dời lịch sang ngày khác = **延期（えんき）**.\n- Kéo dài thêm thời lượng (mở cửa tới khuya, gia hạn hợp đồng/visa) = **延長（えんちょう）**! 🌟",
            "wrong_exps": [
                "Dời trận đấu hôm nay sang thứ Bảy tuần sau phải dùng `延期（えんき）`, KHÔNG dùng `延長`.",
                "Chính xác tuyệt đối! Kéo dài giờ mở cửa thư viện đến 9 giờ tối (`延長した`).",
                "Quần dài quá phải cắt ngắn đi (`短くする・裾上げする`), không phải kéo dài!",
                "`中止` là hủy bỏ, không ghép `中止に延長した`."
            ],
            "source_ref": {"novel": "isekai", "chapter": 7, "lesson_id": "p1_c09_b02", "label": "Bộ 3 Isekai Ch.07 (Thời gian)"}
        },
        {
            "num": 16,
            "mondai": "問題6：用法",
            "mondai_vi": "Cách dùng từ đúng trong câu",
            "prompt": "次の言葉の使い方として最もよいものを、1・2・3・4から一つ選びなさい。\n【言葉：<b><u>〜だらけ</u></b>】",
            "prompt_vi": "Chọn câu sử dụng đúng nhất từ 【〜だらけ】 (đầy rẫy toàn thứ không mong muốn / dơ bẩn / lỗi sai).",
            "options": [
                "公園で元気に遊んで帰ってきた子どもたちの服は泥だらけだった。",
                "お正月には家族みんなで集まって、楽しい笑顔だらけの時間を過ごした。",
                "テストで100点を取って、先生から嬉しい言葉だらけをもらった。",
                "新しいホテルはとてもきれいで、豪華な家具だらけが並んでいる。"
            ],
            "ans": 1,
            "cute_right_msg": "Quá nét!! Hậu tố `〜だらけ` gắn vào danh từ để tả bề mặt/nơi nào **bị phủ đầy thứ tiêu cực / phiền toái / bùn bụi / lỗi sai** (`泥だらけ・間違いだらけ`) — KHÔNG dùng cho nụ cười vui hay lời khen đâu nha! 👕💨",
            "right_exp": "`N + だらけ`: Đầy rẫy, phủ kín những thứ tiêu cực, bừa bộn hoặc không mong muốn (`泥だらけ・傷だらけ・間違いだらけ・ほこりだらけ`).",
            "cute_wrong_msg": "Mẹo phân biệt hậu tố `〜だらけ` trong Isekai Ch.11 nè em: nó mang sắc thái **tiêu cực / lấm lem / sai sót** (`泥だらけ` lấm bùn, `間違いだらけ` toàn lỗi sai), không dùng để tả điều đẹp đẽ vui vẻ như nụ cười hay đồ sang trọng nhé! 🌸",
            "wrong_exps": [
                "Chính xác! Quần áo trẻ con chơi nghịch dính lấm lem toàn bùn đất (`泥だらけ`).",
                "Không dùng `〜だらけ` cho cảm xúc tích cực đẹp đẽ như nụ cười (`笑顔にあふれた` mới chuẩn).",
                "Lời khen vui mừng không đi với `〜だらけ` (lại càng không thể làm tân ngữ với `〜だらけをもらった`).",
                "Đồ nội thất sang trọng dùng `豪華な家具がずらりと並んでいる`, không dùng `家具だらけ`."
            ],
            "source_ref": {"novel": "isekai", "chapter": 11, "lesson_id": "p2_c07_b03", "label": "Bộ 3 Isekai Ch.11 (Hậu tố 〜だらけ)"}
        },
        {
            "num": 17,
            "mondai": "問題7：文の文法1",
            "mondai_vi": "Ngữ pháp câu N2",
            "prompt": "新しい都市計画が成功するか否かは、住民たちの協力が得られるかどうかに（　　）。",
            "prompt_vi": "Dự án quy hoạch đô thị mới có thành công hay không hoàn toàn phụ thuộc vào việc có nhận được sự hợp tác của cư dân hay không.",
            "options": ["かかっている", "わたっている", "限っている", "向いている"],
            "ans": 1,
            "cute_right_msg": "ĐỈNH!! Mẫu câu N2 vàng mười `〜かどうかにかかっている` = hoàn toàn phụ thuộc/trông cậy vào yếu tố quyết định đó! 🏙️⚖️",
            "right_exp": "`〜かどうかにかかっている`: Kết quả thành bại hay tương lai hoàn toàn phụ thuộc vào yếu tố then chốt phía trước.",
            "cute_wrong_msg": "Khi thấy cặp hỏi nghi vấn ở vế trước `成功するか否かは、〜かどうかに...`: động từ nghĩa 'phụ thuộc vào yếu tố quyết định' là `かかっている` nha em! 💡",
            "wrong_exps": [
                "Chính xác tuyệt đối! `〜かどうかにかかっている` = phụ thuộc vào việc...",
                "`にわたっている` = trải dài khắp thời gian/không gian.",
                "`に限っている` không hợp nghĩa ở đây.",
                "`に向いている` = phù hợp với công việc/đối tượng nào."
            ],
            "source_ref": {"novel": "isekai", "chapter": 10, "lesson_id": "p2_c07_b02", "label": "Ngữ pháp N2 — 依存（〜にかかっている）"}
        },
        {
            "num": 18,
            "mondai": "問題7：文の文法1",
            "mondai_vi": "Ngữ pháp câu N2",
            "prompt": "どんなに小さな一歩（　　）、毎日続けることで必ず大きな成果につながるはずだ。",
            "prompt_vi": "Dẫu cho chỉ là một bước đi nhỏ bé đến nhường nào đi chăng nữa, bằng việc duy trì mỗi ngày chắc chắn cũng sẽ dẫn đến thành quả lớn.",
            "options": ["であれ", "とあって", "だの", "ならではの"],
            "ans": 1,
            "cute_right_msg": "Chuẩn không cần chỉnh! `どんなに〜であれ` = cho dù chỉ là... đi chăng nữa! 🌟",
            "right_exp": "`（どんなに）N + であれ`: Dù là N đi chăng nữa (tương tự `であっても`), kết hợp tự nhiên với `どんなに〜`.",
            "cute_wrong_msg": "Thấy từ đầu câu `どんなに` ('dù... đến mấy') là chọn cấu trúc nhượng bộ **であれ** ngay lập tức nha em! 🌸",
            "wrong_exps": [
                "Chính xác! `どんなに小さな一歩であれ` = dẫu cho có là bước đi nhỏ bé cỡ nào.",
                "`とあって` = bởi vì hoàn cảnh đặc biệt đó nên...",
                "`だの` = nào là... nào là... (liệt kê).",
                "`ならではの` = nét độc đáo chỉ riêng X mới có."
            ],
            "source_ref": {"novel": "isekai", "chapter": 8, "lesson_id": "p2_c05_b01", "label": "Ngữ pháp N2 — 譲歩（〜であれ）"}
        },
        {
            "num": 19,
            "mondai": "問題7：文の文法1",
            "mondai_vi": "Ngữ pháp câu N2",
            "prompt": "新しい装置の実用化にあたっては、安全性について何度も実験を重ねる（　　）。",
            "prompt_vi": "Khi đưa thiết bị mới vào ứng dụng thực tế, không còn cách nào khác ngoài việc phải lặp đi lặp lại thí nghiệm nhiều lần về tính an toàn.",
            "options": ["しかない", "わけがない", "ものではない", "どころではない"],
            "ans": 1,
            "cute_right_msg": "Quá chuẩn!! `Vる + しかない / ほかない` = chỉ còn duy nhất một cách bắt buộc phải làm thế! 🔬✨",
            "right_exp": "`Vる + しかない / ほかない`: Không còn con đường nào khác tốt hơn hoặc bắt buộc chỉ có thể làm V (`実験を重ねるしかない`).",
            "cute_wrong_msg": "Ngữ cảnh kỹ thuật nghiêm túc khẳng định điều tất yếu phải làm để bảo đảm an toàn: 'chỉ có nước lặp đi lặp lại thí nghiệm thôi' → `しかない` nha em! 💖",
            "wrong_exps": [
                "Chính xác! `実験を重ねるしかない` = chỉ có cách thí nghiệm lặp lại thật nhiều lần.",
                "`わけがない` = không đời nào làm vậy (sai nghĩa hoàn toàn!).",
                "`ものではない` = không nên làm vậy theo lẽ thường (ngược nghĩa!).",
                "`どころではない` = chẳng phải lúc mà làm vậy."
            ],
            "source_ref": {"novel": "isekai", "chapter": 5, "lesson_id": "p1_c08_b02", "label": "Ngữ pháp N2 — 限定手段（〜しかない）"}
        },
        {
            "num": 20,
            "mondai": "問題8：文の文法2 ★",
            "mondai_vi": "Sắp xếp thành phần câu",
            "prompt": "エルディアが平和を取り戻したのは、みんなが ＿＿＿ ＿＿＿ ★ ＿＿＿ にほかならない。",
            "prompt_vi": "Việc Eldia giành lại được hòa bình chẳng phải gì khác mà chính là thành quả từ nỗ lực mà mọi người đã đồng lòng xây dựng nên.",
            "options": ["支え合って", "努力の", "築き上げた", "賜物"],
            "ans": 2,
            "cute_right_msg": "HOÀN HẢO 20/20 BỘ 3 ISEKAI!! Thứ tự khóa chặt: `[1] 支え合って → [3] 築き上げた → ★[2] 努力の → [4] 賜物` (`にほかならない`)! ⚔️🏆✨",
            "right_exp": "Ghép chuẩn xác: `みんなが [1]支え合って [3]築き上げた ★[2]努力の [4]賜物 にほかならない。`\n- `みんなが` đi với `[1]支え合って` (nương tựa nâng đỡ lẫn nhau rồi...)\n- `[3]築き上げた` (đã gây dựng nên) bổ nghĩa cho `[2]努力の`\n- `[2]努力の` + `[4]賜物` (`努力の賜物`) đứng ngay trước `にほかならない`.\n→ Vị trí dấu ★ là **2 (`努力の`)**!",
            "cute_wrong_msg": "Nhìn cụm cố định chốt cuối trước `にほかならない`: chính là `[2] 努力の + [4] 賜物` (thành quả của nỗ lực)! Còn đằng trước là 2 động từ `支え合って + 築き上げた` nha em! 🌟",
            "wrong_exps": [
                "`[1] 支え合って` đứng ở ô số 1.",
                "Chính xác tuyệt đối! Vị trí ★ là `[2] 努力の` (`1 → 3 → 2 → 4`).",
                "`[3] 築き上げた` đứng ở ô số 2.",
                "`[4] 賜物` đứng ở ô số 4 (trước `にほかならない`)."
            ],
            "source_ref": {"novel": "isekai", "chapter": 12, "lesson_id": "p2_c07_b04", "label": "Bộ 3 Isekai Ch.12 ★ (努力の賜物にほかならない)"}
        },
    ]
}
