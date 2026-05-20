"""
Module: text_analyzer
Task 2: Regex analysis, date validation, smileys, sentence stats.
Variant 19: date dd/mm/yyyy, uppercase A–Z, words with 'z', remove words starting with 'a'.
"""

import re
import zipfile
import os


def read_file(path: str) -> str:
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()


def write_file(path: str, content: str) -> None:
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)


def sentence_stats(text: str) -> tuple:
    sentences = re.split(r'[.!?]+', text)
    sentences = [s.strip() for s in sentences if s.strip()]
    total = len(sentences)
    dec = sum(1 for s in sentences if not s.endswith(('?', '!')))
    quest = sum(1 for s in sentences if s.endswith('?'))
    excl = sum(1 for s in sentences if s.endswith('!'))
    return total, dec, quest, excl


def avg_sentence_len_chars(text: str) -> float:
    words = re.findall(r'\b\w+\b', text)
    total_chars = sum(len(w) for w in words)
    sentences = [s.strip() for s in re.split(r'[.!?]+', text) if s.strip()]
    return total_chars / len(sentences) if sentences else 0.0


def avg_word_len(text: str) -> float:
    words = re.findall(r'\b\w+\b', text)
    return sum(len(w) for w in words) / len(words) if words else 0.0


def count_smileys(text: str) -> int:
    return len(re.findall(r'[:;]-*[()\[\]]+', text))


def is_valid_date(date_str: str) -> bool:
    return bool(re.fullmatch(r'(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/(1[6-9][0-9]{2}|[2-9][0-9]{3})', date_str))


def count_uppercase_english(text: str) -> int:
    return len(re.findall(r'[A-Z]', text))


def first_word_with_z(text: str):
    words = re.findall(r'\b\w+\b', text)
    for idx, w in enumerate(words, 1):
        if 'z' in w.lower():
            return w, idx
    return '', -1


def remove_words_starting_with_a(text: str) -> str:
    return re.sub(r'\ba\w+\b', '', text, flags=re.I)


def sentences_with_spaces_digits_punct(text: str):
    sentences = re.split(r'[.!?]+', text)
    res = []
    for s in sentences:
        s = s.strip()
        if s and re.search(r'\s', s) and re.search(r'\d', s) and re.search(r'[.,;:!?\'"()\[\]{}<>]', s):
            res.append(s)
    return res


def main_text_analyzer():
    sample = (
        "Hello, world! How are you? The date 15/04/2025 is valid. "
        "Smile :) :---] and ;-) Also a Z-word: amazing! "
        "Another sentence with digits 123 and punctuation, ok? aaaa remove this."
    )
    input_file = "data/input_text.txt"
    output_file = "data/analysis.txt"
    zip_name = "data/result.zip"

    write_file(input_file, sample)
    text = read_file(input_file)

    total, dec, quest, excl = sentence_stats(text)
    avg_sent = avg_sentence_len_chars(text)
    avg_word = avg_word_len(text)
    smileys = count_smileys(text)

    report = f"""
=== Regex Text Analysis ===
Total sentences: {total}
Declarative: {dec}
Interrogative: {quest}
Imperative: {excl}
Avg sentence length (chars in words): {avg_sent:.2f}
Avg word length: {avg_word:.2f}
Smileys: {smileys}

=== Date validation ===
'15/04/2025' valid? {is_valid_date('15/04/2025')}
'31/02/2025' valid? {is_valid_date('31/02/2025')}

=== Variant 19 specific ===
Uppercase English letters: {count_uppercase_english(text)}
First word with 'z': {first_word_with_z(text)}
Text after removing words starting with 'a':
{remove_words_starting_with_a(text)}

=== Sentences with spaces, digits, punctuation ===
"""
    for i, sent in enumerate(sentences_with_spaces_digits_punct(text), 1):
        report += f"{i}. {sent}\n"

    write_file(output_file, report)
    with zipfile.ZipFile(zip_name, 'w') as zf:
        zf.write(output_file)

    print("Analysis saved to data/analysis.txt and zipped to data/result.zip")
    print("\n--- Preview ---")
    print(report[:800])