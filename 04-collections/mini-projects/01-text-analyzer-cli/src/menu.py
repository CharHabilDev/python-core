from src.analyzer import (
    total_words,
    word_frequency,
    unique_words,
    longest_word,
    shortest_word,
    search_word
)

from src.storage import load_data


def show_statistics(counter, text):
    total_word = total_words(counter)
    unique_word = unique_words(counter)

    print(f"\n=== TEXT STATISTICS ===\n")
    print(f"{'Total words':<20}: {total_word}")
    print(f"{'Unique words':<20}: {unique_word}")
    print(f"{'Vocabulary ratio':<20}: {(unique_word/total_word):.2%}")

    print(f"{'Longest word':<20}: {longest_word(text)}")
    print(f"{'Shortest word':<20}: {shortest_word(text)}")


def show_top_words(counter, n: int):
    print("\n=== Most Common Words ===\n")
    for index, element in enumerate(word_frequency(counter, n), start=1):
        print(f"{index}. {f'{element[0]}':<10}: {f'{element[1]}'}")


def display_search_result(counter, word: str):
    value = search_word(counter, word.lower())
    if value is None:
        print(f"{word} doesn't found.")
        return
    print(f"Occurences: {value}")


def display_analyses_history():
    try:
        history = load_data("history.json")
    except ValueError:
        history = []

    if not history:
        print("No file in history.")
        return

    print("\n=== Recent Analyses ===\n")
    for index, file in enumerate(history, start=1):
        print(f"{index}. {file}")