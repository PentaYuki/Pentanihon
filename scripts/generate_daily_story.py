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
    6: {
        "filename": "series-01_tap-06_dem_dong_jimbocho.md",
        "title_jp": "神保町（じんぼうちょう）の冬（ふゆ）の夜（よる）とユキ姉（ねえ）の過去（かこ）",
        "title_vi": "Đêm Đông Jimbocho & Ký Ức Của Chị Yuki",
        "summary_prev": "Sau khi xuất sắc vượt qua vòng phỏng vấn 1 tại tập đoàn Mirai Technology bằng câu chuyện làm phần mềm thực chiến, Ren bước vào giai đoạn ôn thi nước rút cho kỳ thi JLPT N2 sắp diễn ra.",
        "grammar_points": ["〜にほかならない", "〜どころか", "〜にすぎない", "〜からこそ"],
        "content_jp": """十二月（じゅうにがつ）初旬（しょじゅん）、東京（とうきょう）の街（まち）は冷（つめ）たい木枯（こが）らしが吹（ふ）き抜（ぬ）けていた。

JLPT N2の本番（ほんばん）まであと一週間（いっしゅうかん）。レンはカフェの閉店（へいてん）後（ご）も、読解（どっかい）と文法（ぶんぽう）の過去問（かこもん）と格闘（かくとう）していた。だが、連日（れんじつ）の猛勉強（もうべんきょう）と面接（めんせつ）の準備（じゅんび）が重（かさ）なり、疲労（ひろう）は限界（げんかい）に達（たっ）していた。

「コホン、コホン……」

激（はげ）しい咳（せき）とともに、視界（しかい）がぐらりと揺（ゆ）れた。机（つくえ）に突（つ）っ伏（ぷ）したレンの額（ひたい）に、冷（つめ）たいタオルがそっと当（あ）てられた。

「無理（むり）をしちゃダメって言（い）ったでしょ、レン」

ユキ姉（ねえ）が生姜（しょうが）湯（ゆ）の入（はい）ったマグカップを置（お）き、心配（しんぱい）そうにレンを見（み）つめていた。

「すみません、ユキ姉（ねえ）……。試験（しけん）まで時間（じかん）がないのに、こんなところで倒（たお）れるなんて……」

焦（あせ）るレンの手（て）を、ユキ姉（ねえ）は優（やさ）しく包（つつ）み込（こ）んだ。

「実（じつ）はね、私（わたし）も５年前（ごねんまえ）、大手（おおて）の商社（しょうしゃ）で働（はたら）いていた頃（ころ）、誰（だれ）にも頼（たよ）れずに一人（ひとり）で抱（かか）え込（こ）んで、過労（かろう）で倒（たお）れたことがあるのよ」

ユキ姉（ねえ）の告白（こくはく）に、レンは驚（おどろ）いて目（め）を見開（みひら）いた。いつも明（あか）るく頼（たよ）もしい彼女（かのじょ）に、そんな過去（かこ）があったとは知（し）らなかったのだ。

「その時（とき）、田中（たなか）さんがこの古本（ふるほん）屋（や）街（がい）に連（つ）れてきてくれて、温（あたた）かい珈琲（コーヒー）を淹（い）れてくれたの。『休（やす）むことは逃（に）げることじゃない。次（つぎ）に大（おお）きく跳（と）ぶための助走（じょそう）**にほかならない**』ってね。その言葉（ことば）に救（すく）われて、私（わたし）は自分（じぶん）のペースで人（ひと）が集（あつ）まれるこのカフェを開（ひら）いたの」

ユキ姉（ねえ）は微笑（ほほえ）みながらレンの頭（あたま）を撫（な）でた。

「今（いま）の熱（ねつ）はね、体（からだ）が『少（すこ）し休（やす）みなさい』とサインを出（だ）している**にすぎない**の。焦（あせ）り**どころか**、ここまでの努力（どりょく）は絶対（ぜったい）にレンを裏切（うらぎ）らないわ。今日（きょう）はもう寝（ね）なさい。明日（あした）になれば、また青空（あおぞら）が見（み）えるんだ**からこそ**ね」

温（あたた）かい生姜（しょうが）湯（ゆ）の香（かお）りとユキ姉（ねえ）の優（やさ）しさに包（つつ）まれ、レンの緊張（きんちょう）の糸（いと）が解（ほぐ）れ、深（ふか）い眠（ねむ）りへと落（お）ちていった。""",
        "content_vi": """Đầu tháng Mười Hai, những cơn gió đông bắc lạnh buốt quét qua từng con phố Tokyo.

Chỉ còn đúng một tuần nữa là kỳ thi JLPT N2 chính thức diễn ra. Dù quán cà phê đã đóng cửa, Ren vẫn ngồi lại miệt mài đánh vật với các đề thi đọc hiểu và ngữ pháp năm trước. Thế nhưng, chuỗi ngày học thâu đêm kết hợp cùng áp lực phỏng vấn đã đẩy cơ thể cậu đến bờ vực kiệt sức.

Cơn ho dữ dội bất ngờ ập đến, trời đất trước mắt Ren chao đảo. Khi cậu gục xuống bàn, một chiếc khăn ấm được đặt nhẹ nhàng lên trán cậu.

"Chị đã bảo em không được gượng ép quá sức cơ mà, Ren."

Chị Yuki đặt cốc nước gừng nóng hổi xuống bàn, lo lắng nhìn cậu.

"Em xin lỗi chị Yuki... Sắp thi đến nơi rồi mà em lại đổ bệnh thế này..."

Nắm lấy đôi bàn tay đang run rẩy của Ren, chị Yuki dịu dàng nói:

"Thực ra, 5 năm trước khi còn làm việc tại một tập đoàn thương mại lớn, chị cũng từng không dám nhờ vả ai, cứ ôm đồm một mình đến mức ngất xỉu vì làm việc quá sức đấy."

Nghe lời bộc bạch của chị, Ren mở to mắt kinh ngạc. Cậu chưa từng biết người chị gái lúc nào cũng rạng rỡ và tháo vát kia lại từng nếm trải quá khứ cay đắng đến thế.

"Lúc đó, bác Tanaka đã dắt chị về khu phố sách cổ này, tự tay pha cho chị một tách cà phê nóng rồi bảo: 'Nghỉ ngơi không phải là trốn chạy, mà chính là bước chạy đà để nhảy cao hơn'. Được lời nói ấy cứu rỗi, chị mới quyết định sống chậm lại và mở quán cà phê này."

Chị Yuki xoa nhẹ đầu Ren:

"Cơn sốt lúc này chẳng qua chỉ là tín hiệu cơ thể em đang đòi nghỉ ngơi đôi chút thôi. Thay vì sốt ruột lo lắng, hãy tin rằng toàn bộ mồ hôi công sức bấy lâu nay tuyệt đối sẽ không phản bội em. Uống hết cốc nước gừng này rồi ngủ một giấc thật sâu nhé, chính vì ngày mai bầu trời xanh sẽ lại mở ra đón em mà!"

Hương nước gừng cay nồng ấm áp cùng tình thương của chị gái đã xoa dịu toàn bộ âu lo, đưa Ren chìm vào một giấc ngủ bình yên trọn vẹn.""",
        "grammar_analysis": """### 1. `〜にほかならない`
- **Câu trong tập:** `次（つぎ）に大（おお）きく跳（と）ぶための助走（じょそう）にほかならない`
- **Ý nghĩa:** "Chính là / Không gì khác ngoài..." (Khẳng định bản chất cốt lõi: nghỉ ngơi chính là bước chạy đà).

### 2. `〜にすぎない`
- **Câu trong tập:** `体（からだ）がサインを出（だ）しているにすぎない`
- **Ý nghĩa:** "Chẳng qua chỉ là..." (Giảm nhẹ vấn đề, khuyên không nên quá hoảng loạn).

### 3. `〜どころか`
- **Câu trong tập:** `焦（あせ）りどころか、ここまでの努力（どりょく）は絶対（ぜったい）に裏切（うらぎ）らない`
- **Ý nghĩa:** "Nói gì đến chuyện hoang mang lo lắng, ngược lại công sức sẽ được đền đáp".

### 4. `〜からこそ`
- **Câu trong tập:** `明日（あした）になれば、また青空（あおぞら）が見（み）えるんだからこそ`
- **Ý nghĩa:** "Chính vì ngày mai tươi sáng..." (Tiếp thêm niềm tin và động lực sống).""",
        "vocab_notes": """- **木枯（こが）らし (MỘC KHÔ):** Cơn gió lạnh đầu đông làm rụng lá cây.
- **突（つ）っ伏（ぷ）す (ĐỘT PHỤC):** Gục mặt xuống bàn vì mệt mỏi hoặc suy sụp.
- **抱（かか）え込（こ）む (BÃO NHẬP):** Ôm đồm mọi việc vào người một mình.
- **助走（じょそう - TRỢ TẨU):** Bước chạy đà chuẩn bị bật nhảy xa.""",
        "questions": [
            ("ユキ姉が5年前に倒れた根本的な原因は何か。",
             ["神保町のカフェの経営がうまくいかなかったから。",
              "商社で働いていた時に誰にも頼れず一人で仕事を抱え込みすぎたから。",
              "日本語能力試験の勉強に失敗したから。",
              "田中さんと口論になって心労が重なったから。"], 2),
            ("ユキ姉がレンに伝えた「休むこと」の真の意味はどれか。",
             ["夢を諦めて国へ帰る準備をすること。",
              "試験の勉強を完全にやめてカフェを手伝うこと。",
              "逃げることではなく、次に大きく前進するための大切な充電期間であること。",
              "病気になった自分を責め続けること。"], 3)
        ],
        "sister_message": "Bé cưng ơi, máy móc chạy mãi còn nóng máy cần nghỉ, huống chi con người chúng mình! Hãy biết yêu thương cơ thể và ngủ đủ giấc nhé! 🌸",
        "next_preview": "Sau giấc ngủ hồi sinh, kỳ thi JLPT N2 lịch sử vào ngày Chủ nhật đầu tiên của tháng 12 đã chính thức điểm chuông! Ren và Aoi cùng bước vào phòng thi tại Đại học Tokyo. Những bẫy ngữ pháp nào đang chờ đón họ? Đón đọc Tập 07: Tháng 12 Định Mệnh! Ngày Quyết Chiến JLPT N2 nhé!"
    },
    7: {
        "filename": "series-01_tap-07_ngay_quyet_chien_jlpt.md",
        "title_jp": "運命（うんめい）の12月（じゅうにがつ）！ JLPT N2決戦（けっせん）の日（ひ）",
        "title_vi": "Tháng 12 Định Mệnh! Ngày Quyết Chiến JLPT N2",
        "summary_prev": "Nhờ chén nước gừng ấm áp và câu chuyện vượt qua quá khứ của chị Yuki, Ren đã hồi phục cả về thể chất lẫn tinh thần, tự tin bước vào tuần cuối cùng trước kỳ thi.",
        "grammar_points": ["〜に際して", "〜を契機に", "〜ざるを得ない", "〜抜く"],
        "content_jp": """十二月（じゅうにがつ）の第一（だいいち）日曜日（にちようび）。東京（とうきょう）大学（だいがく）のキャンパスは、日本（にほん）全国（ぜんこく）から集（あつ）まった受験生（じゅけんせい）の熱気（ねっき）に包（つつ）まれていた。

会場（かいじょう）の門（もん）の前（まえ）で、レンはアオイと合流（ごうりゅう）した。彼女（かのじょ）の手（て）には、ユキ姉（ねえ）手作（てづく）りのお守（まも）りがしっかりと握（にぎ）りしめられていた。

「レン君（くん）、いよいよだね」

「うん。緊張（きんちょう）していないと言（い）ったら嘘（うそ）になるけれど……不思議（ふしぎ）と怖（こわ）くはないよ。僕（ぼく）たちには、神保町（じんぼうちょう）で積み重（つみかさ）ねてきた時間（じかん）があるから」

試験（しけん）開始（かいし）のチャイムが鳴（な）り響（ひび）く。問題（もんだい）用紙（ようし）を開（ひら）い**たとたん**、レンの集中力（しゅうちゅうりょく）は研（と）ぎ澄（す）まされた。

文字（もじ）・語彙（ごい）、文法（ぶんぽう）、そして長文（ちょうぶん）読解（どっかい）――目（め）の前に現（あらわ）れる問題（もんだい）の数々（かずかず）は、まさにユキ姉（ねえ）と毎日（まいにち）確認（かくにん）し合（あ）ったフレーズばかりだった。

『筆者（ひっしゃ）の最も言（い）いたいことは何（なに）か』という難解（なんかい）な最終（さいしゅう）問題（もんだい）に対（たい）しても、田中（たなか）さんから教（おし）わった「文章（ぶんしょう）の奥（おく）にある体温（たいおん）を感（かん）じる」読（よ）み方（かた）で、確信（かくしん）を持（も）って正解（せいかい）の番号（ばんごう）をマークシートに塗（ぬ）りつぶした。

聴解（ちょうかい）の最後（さいご）の音（おと）が消（き）え、「やめ！」という試験官（しけんかん）の声（こえ）が響（ひび）いた瞬間（しゅんかん）、レンは長（なが）い息（いき）を吐（は）き出（だ）した。最後（さいご）の１秒（びょう）まで全（すべ）ての力（ちから）をやり**抜（ぬ）いた**という充実感（じゅうじつかん）が、全身（ぜんしん）を満（み）たしていた。

教室（きょうしつ）を出（で）ると、門（もん）のところで待（ま）っていたユキ姉（ねえ）が、大（おお）きく手（て）を振（ふ）っていた。冬（ふゆ）の夕日（ゆうひ）を浴（あ）びながら、レンとアオイは笑顔（えがお）で駆（か）け寄（よ）った。""",
        "content_vi": """Chủ nhật đầu tiên của tháng Mười Hai. Khuôn viên trường Đại học Tokyo ngập tràn bầu không khí nghiêm trang và khẩn trương của hàng nghìn thí sinh tham dự kỳ thi JLPT.

Trước cổng trường, Ren gặp lại Aoi. Trên tay cô bạn đang nắm chặt chiếc túi bùa hộ mệnh may mắn do chính tay chị Yuki tự may tặng.

"Ren ơi, cuối cùng giờ G cũng điểm rồi."

"Ừ. Nếu bảo không run thì là nói dối... nhưng kỳ lạ là tớ không hề thấy sợ hãi nữa. Bởi chúng mình đã có những đêm miệt mài bên trang sách ở Jimbocho làm điểm tựa."

Hồi chuông báo hiệu bắt đầu làm bài vang lên. Ngay khoảnh khắc mở tập đề thi, toàn bộ sự tập trung của Ren đạt đến độ chuẩn xác cao độ.

Từ vựng chữ Hán, ngữ pháp, rồi các bài đọc hiểu văn luận dài dằng dặc — những câu hỏi hiện ra trước mắt như chính những cấu trúc mà cậu và chị Yuki đã cùng nhau mổ xẻ mỗi ngày.

Trước câu hỏi then chốt cuối cùng 'Điều tác giả muốn truyền đạt nhất là gì', nhớ lại lời dặn của bác Tanaka về 'hơi ấm ẩn sau câu chữ', Ren bình tĩnh tìm ra luận điểm cốt lõi và tô tròn đáp án vào phiếu trả lời.

Khi âm thanh cuối cùng của phần thi nghe hiểu vừa dứt cùng tiếng hô dõng dạc của giám thị 'Hết giờ, dừng bút!', Ren thở phào một hơi dài nhẹ nhõm. Cảm giác mãn nguyện vì đã kiên trì chiến đấu đến giây phút cuối cùng tràn ngập khắp huyết quản.

Bước ra khỏi cổng trường thi, chị Yuki đã đứng đợi từ lúc nào, giơ cao tay vẫy chào hai đứa. Dưới ánh nắng hoàng hôn ấm áp của mùa đông Tokyo, Ren và Aoi rạng rỡ chạy tới.""",
        "grammar_analysis": """### 1. `〜たとたん（に）`
- **Câu trong tập:** `問題用紙を開いたとたん、集中力が研ぎ澄まされた。`
- **Ý nghĩa:** "Vừa mới mở đề thi ra thì ngay lập tức toàn bộ sự tập trung trỗi dậy".

### 2. `〜抜（ぬ）く`
- **Câu trong tập:** `最後（さいご）の１秒（びょう）までやり抜（ぬ）いた`
- **Ý nghĩa:** "Kiên trì nỗ lực làm tới giây phút cuối cùng không bỏ cuộc".

### 3. `〜に際（さい）して`
- **Câu trong tập:** *(Ôn tập)* `決戦（けっせん）に際（さい）して...`
- **Ý nghĩa:** "Nhân thời khắc bước vào kỳ thi quyết định".

### 4. `〜ざるを得（え）ない`
- **Câu trong tập:** *(Ôn tập)* `認（みと）めざるを得（え）ない`
- **Ý nghĩa:** "Đành phải thừa nhận sự nỗ lực của chính mình".""",
        "vocab_notes": """- **研（と）ぎ澄（す）まされる (NGHIỄN TRỪNG):** Trở nên sắc bén, tinh tế tột bậc (giác quan, sự tập trung).
- **やり抜（ぬ）く (VI BẠT):** Làm đến cùng, chiến đấu tới giọt mồ hôi cuối cùng.
- **充実感（じゅうじつかん - SUNG THỰC CẢM):** Cảm giác mãn nguyện, trọn vẹn sau khi hoàn thành mục tiêu.""",
        "questions": [
            ("レンが試験本番で怖さを感じなかった最大の理由は何か。",
             ["神保町のカフェで仲間と共に着実に努力を積み重ねてきた自信があったから。",
              "問題が簡単すぎて満点が取れると確信していたから。",
              "すでに大企業の内定が決まっていて合格する必要がなかったから。",
              "試験会場が暖房でとても暖かかったから。"], 1),
            ("読解の最難問を解く際に、レンを助けた教えはどれか。",
             ["消去法を使って適当にマークすること。",
              "文章の表面的な言葉だけでなく、奥にある著者の意図や体温を感じ取ること。",
              "辞書をこっそり開いて単語を調べること。",
              "隣の受験生の回答を覗き見ること。"], 2)
        ],
        "sister_message": "Chiến đấu hết mình trong phòng thi chính là chiến thắng vĩ đại nhất rồi bé cưng ơi! Hãy tự hào về chính bản thân mình nhé! 🌸",
        "next_preview": "Vừa thi xong N2, Ren nhận được cú điện thoại hẹn gặp trực tiếp từ Tổng Giám Đốc tập đoàn Mirai Tech cho vòng phỏng vấn Ban Điều Hành cuối cùng. Liệu cậu có giành được tấm vé Naitei mơ ước? Đón đọc Tập 08 nhé!"
    }
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
    
    if next_ep not in SERIES_EPISODES:
        print(f"Episode {next_ep} is not yet scripted in the pipeline bank.")
        return None
        
    ep_data = SERIES_EPISODES[next_ep]
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
            # Chèn thêm vào bảng danh sách tập
            lines = readme_content.split('\n')
            new_lines = []
            for line in lines:
                new_lines.append(line)
                if f"| **{max_ep:02d}** |" in line:
                    new_lines.append(new_row.strip())
            with open(readme_path, 'w', encoding='utf-8') as f:
                f.write('\n'.join(new_lines))

    print(f" Successfully released Episode {next_ep:02d}: {ep_data['filename']}")
    return ep_data['filename']

if __name__ == '__main__':
    generate_next_series_episode()
