from rapidfuzz import fuzz, process

KNOWN_TERMS = [
    "محاضرة", "امتحان", "ذكاء اصطناعي", "شبكات", "نظم تشغيل", "برمجة",
    "متى", "أين", "الساعة", "اليوم", "المكان", "الدكتور", "البريد", "مكتب",
    "استشارة", "القاعة", "الامتحانات", "المحاضرات", "الأساتذة", "القسم"
]

def correct_text(text, terms=KNOWN_TERMS, threshold=85):
    corrected_words = []
    for word in text.split():
        result = process.extractOne(word, terms, scorer=fuzz.ratio)
        if result:
          match = result[0]
          score = result[1]
        else:
          match = word
          score = 0
        if score >= threshold:
            corrected_words.append(match)
        else:
            corrected_words.append(word)
    return " ".join(corrected_words)