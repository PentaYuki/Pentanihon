#!/usr/bin/env python3
"""
Pentanihon Daily Story Generator
Tự động viết câu chuyện tiếng Nhật mới mỗi ngày kèm giải thích ngữ pháp và câu hỏi luyện tập.
"""
import os
import datetime
import glob
import re

WORKSPACE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STORY_DIR = os.path.join(WORKSPACE_DIR, 'story')

# Kho ý tưởng & chủ đề câu chuyện phong phú chuẩn N2
STORY_BANK = [
    {
        "filename": "story-04_hoa_anh_dao_no_muon.md",
        "title_jp": "遅咲（おそざ）きの桜（さくら）と新（あたら）しい旅立（たびだ）ち",
        "title_vi": "Hoa Anh Đào Nở Muộn Và Chuyến Khởi Hành Mới",
        "grammar_points": ["〜にほかならない", "〜どころか", "〜にすぎない", "〜からこそ"],
        "content_jp": """四月（しがつ）の半（なか）ばを過（す）ぎ、街（まち）の桜（さくら）がすっかり散（ち）ってしまった頃（ころ）、山裾（やますそ）の小（ちい）さな寺（てら）の境内（けいだい）に、今（いま）まさに満開（まんかい）を迎（むか）えようとしている一本（いっぽん）の桜（さくら）の木（き）があった。

周囲（しゅうい）の木々（きぎ）が新緑（しんりょく）の青葉（あおば）を茂（しげ）らせる中（なか）で、その桜（さくら）だけが誰（だれ）に急（せ）かされることもなく、自（みずか）らのペースで淡（あわ）い花（はな）びらを誇（ほこ）らしげに咲（さ）き誇（ほこ）らせていた。

「周（まわ）りと比（くら）べて遅（おく）れているからといって、恥（は）じることなど何（なに）もないよ」

境内（けいだい）を掃除（そうじ）していた住職（じゅうしょく）のおじいさんが、花（はな）を見上（みあ）げる私（わたし）に温（あたた）かい声（こえ）をかけてくれた。就職（しゅうしょく）活動（かつどう）が難航（なんこう）し、同期（どうき）が次々（つぎつぎ）と内定（ないてい）を決（き）めていく中（なか）で、私（わたし）は焦（あせ）り**どころか**、自暴自棄（じぼうじき）になりかけていたのだ。

「桜（さくら）がそれぞれの時期（じき）に咲（さ）くように、人（ひと）の花（はな）が咲（さ）くタイミングも人（ひと）それぞれだ。大事（だいじ）なのは、根（ね）を張（は）り続（つづ）けること**にほかならない**」

その言葉（ことば）を聞（き）いた瞬間（しゅんかん）、心（こころ）に覆（おお）いかぶさっていた暗（くら）い雲（くも）が晴（は）れ渡（わた）った。人（ひと）より少（すこ）し遠回（とおまわ）りをしたことなど、人生（じんせい）の長（なが）い旅（たび）から見（み）ればほんの小（ちい）さな出来事（できごと）**にすぎない**。今（いま）の苦（くる）しい経験（けいけん）がある**からこそ**、咲（さ）いたときには誰（だれ）よりも美（うつく）しく力強（ちからづよ）い花（はな）を咲（さ）かせることができるはずだ。""",
        "content_vi": """Quá nửa tháng Tư, khi những cánh hoa anh đào nơi phố thị đã trút lá gần hết, trong khuôn viên một ngôi chùa nhỏ dưới chân núi vẫn có một cây hoa anh đào đang rực rỡ đón mùa bung nở muộn.

Giữa lúc cây cỏ xung quanh đã đâm chồi xanh mướt, riêng cây đào ấy chẳng hề bị ai thúc ép, cứ thong dong kiêu hãnh khoe sắc hồng phớt theo đúng nhịp điệu của riêng mình.

"Dẫu có nở muộn hơn xung quanh đôi chút, cũng chẳng có gì phải hổ thẹn cả con à."

Vị sư trụ trì đang quét sân chùa cất lời ôn tồn với tôi. Trong khi bạn bè đồng trang lứa đã lần lượt nhận việc, hành trình tìm việc của tôi lại trắc trở vô cùng. Thay vì bình tĩnh, tôi **nói gì đến giữ được thăng bằng, ngược lại** còn suýt buông xuôi tất cả.

"Cũng như hoa nở vào thời điểm thích hợp của nó, thời khắc đơm hoa của mỗi con người cũng chẳng ai giống ai. Điều quan trọng nhất **chính là** việc con có bền bỉ bám sâu rễ xuống lòng đất hay không."

Ngay khoảnh khắc ấy, tảng mây đen trĩu nặng trong lòng tôi bỗng chốc tan biến. Đi đường vòng hơn người khác đôi chút, nhìn từ chặng đường dài nhân sinh **chẳng qua cũng chỉ là** một hạt cát nhỏ nhoi. **Chính vì** có những tháng ngày thử thách này, một mai khi đơm hoa, ta mới có thể nở rộ rực rỡ và kiên cường hơn bất kỳ ai!""",
        "grammar_analysis": """### 1. `〜どころか`
- **Câu trong bài:** `焦（あせ）りどころか、自暴自棄（じぼうじき）になりかけていた`
- **Ý nghĩa:** "Nói gì đến lo lắng sốt ruột, ngược lại tôi còn suýt buông xuôi tất cả" (Nhấn mạnh kết quả trái ngược, tiêu cực hơn dự tính).

### 2. `〜にほかならない`
- **Câu trong bài:** `根（ね）を張（は）り続（つづ）けることにほかならない`
- **Ý nghĩa:** "Chính là / Không gì khác ngoài việc kiên trì bám rễ" (Khẳng định bản chất cốt lõi).

### 3. `〜にすぎない`
- **Câu trong bài:** `ほんの小（ちい）さな出来事（できごと）にすぎない`
- **Ý nghĩa:** "Chẳng qua chỉ là chuyện cỏn con không đáng để gục ngã".

### 4. `〜からこそ`
- **Câu trong bài:** `苦（くる）しい経験（けいけん）があるからこそ...`
- **Ý nghĩa:** "Chính vì có những trải nghiệm gian khó này..." (Nhấn mạnh nguyên nhân dẫn tới sức mạnh nội tâm).""",
        "vocab_notes": """- **遅咲（おそざ）き:** Nở muộn (hoa); Thành công muộn nhưng vững chắc (người).
- **自暴自棄（じぼうじき - TỰ BẠO TỰ KHÍ）:** Buông xuôi, bất cần đời.
- **誇（ほこ）らしげに:** Một cách đầy kiêu hãnh, tự hào.
- **根（ね）を張（は）る:** Đâm rễ sâu, xây nền tảng vững vàng.""",
        "questions": [
            ("住職が伝えたかった最も重要な教えは何か。",
             ["早く就職先を決めるために無理をしてでも働くべきだ。",
              "他人と比べるのではなく、自分の時期が来るまで努力を積み重ねることが大切だ。",
              "桜の花は早く咲くものほど美しいということ。",
              "同期に負けないように常に競争心を燃やすべきだ。"], 2),
            ("主人公の心の変化として最も適切なものはどれか。",
             ["就職活動を完全に諦めて出家することにした。",
              "他人と比べて焦っていたが、遅咲きでも自分らしく根を張って進む決意をした。",
              "寺の掃除を手伝うことで一生を過ごそうと決めた。",
              "同期の友人たちを激しく羨んで絶望した。"], 2)
        ],
        "sister_message": "Bé ơi, mỗi bông hoa đều có một mùa nở rộ của riêng nó. Đừng bao giờ so sánh đồng hồ của mình với người khác nha! Hãy kiên trì mỗi ngày cùng chị nhé! 🌸"
    }
]

def generate_next_story():
    existing_stories = glob.glob(os.path.join(STORY_DIR, 'story-*.md'))
    current_count = len(existing_stories)
    next_idx = current_count + 1
    
    # Lấy câu chuyện từ kho
    story_template = STORY_BANK[0]
    filename = f"story-{next_idx:02d}_hoa_anh_dao_no_muon.md"
    filepath = os.path.join(STORY_DIR, filename)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(f'''# 🌸 Câu Chuyện {next_idx:02d}: {story_template['title_jp']}
## ({story_template['title_vi']})

> 🌸 **Lời dặn của chị gái:**  
> *"{story_template['sister_message']}"*

---

## 1. 📖 Nội Dung Câu Chuyện (Có Phiên Âm Hiragana)

{story_template['content_jp']}

---

## 2. 🇻🇳 Bản Dịch Tiếng Việt

{story_template['content_vi']}

---

## 3. ⛩️ Phân Tích Ngữ Pháp N2 Xuất Hiện Trong Bài

{story_template['grammar_analysis']}

---

## 4. 📝 Từ Vựng & Quán Dụng Ngữ Đắt Giá
{story_template['vocab_notes']}

---

## 5. ✍️ Câu Hỏi Luyện Tập Đọc Hiểu

''')
        for q_i, q in enumerate(story_template['questions'], 1):
            f.write(f"### Câu {q_i}: {q[0]}\n")
            for c_i, choice in enumerate(q[1], 1):
                f.write(f"{c_i}. {choice}  \n")
            f.write(f"\n*(Đáp án đúng: **{q[2]}**)*\n\n")

        f.write(f'''---

## 🌸 Lời Dặn Của Chị Gái
> 💖 *"{story_template['sister_message']}"*
''')

    # Cập nhật story/README.md
    readme_path = os.path.join(STORY_DIR, 'README.md')
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()

    new_entry = f"| {next_idx:02d} | [**{story_template['title_jp']}**<br>*({story_template['title_vi']})*](./{filename}) | `{', '.join(story_template['grammar_points'])}` | ✅ Hoàn thành |\n"
    
    if filename not in content:
        # Thêm vào bảng danh sách
        table_marker = "| 03 | [**雨音のカフェと忘れ物の傘**"
        lines = content.split('\n')
        new_lines = []
        for line in lines:
            new_lines.append(line)
            if table_marker in line:
                new_lines.append(new_entry.strip())
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(new_lines))

    print(f"Successfully generated new story: {filename}")
    return filename

if __name__ == '__main__':
    generate_next_story()
