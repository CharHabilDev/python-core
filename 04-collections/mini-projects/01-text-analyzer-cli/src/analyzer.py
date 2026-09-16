from collections import Counter, deque
import re

from src.storage import load_file, load_data, save_data


def analyze_file(filename: str):
    text = load_file(filename)

    if text is None:
        print("File doesn't exist.")
        return None

    if not text.strip():
        print("File cannot be empty.")
        return None

    text = re.sub(r"[^\w\s]", "", text.lower())

    counter = Counter(text.split())

    try:
        history = load_data("history.json")
    except ValueError:
        history = []

    history = deque(history, maxlen=4)
    history.append(filename)

    save_data("history.json", list(history))

    print("Analysis completed.")

    return text, counter


def total_words(counter:Counter,):
    return sum(counter.values())


def unique_words(counter:Counter,):
    return len(counter)


def longest_word(text:str):
    return max(text.split(), key=len)


def shortest_word(text:str):
    return min(text.split(), key=len)



def word_frequency(counter:Counter, n:int = 3):
    return counter.most_common(n)


def search_word(counter:Counter, word:str):
    value = counter.get(word)
    if value is None:
        return None
    return value