# Text Analyzer CLI

A command-line application that analyzes text files and provides useful statistics using Python collections.

## Features

- Analyze a text file
- Count total words
- Count unique words
- Display vocabulary ratio
- Find the longest word
- Find the shortest word
- Display the most common words
- Search for a specific word
- Keep a history of recent analyses

## Requirements

- Python 3.12+

## Run

```bash
python -m src.main
```

## Menu

```text
1. Analyze a text file
2. View statistics
3. View top words
4. Search for a word
5. View analysis history
0. Exit
```

## Test Files

The project includes several sample files for testing.

| File | Purpose |
|--------|---------|
| sample.txt | General text analysis |
| article.txt | Longer article |
| repetition.txt | Word frequency testing |
| unique.txt | Unique words testing |
| punctuation.txt | Punctuation and case normalization |
| islam.txt | Additional text sample |
| empty.txt | Empty file validation |

## Example

```text
Enter filename: sample.txt
```

Available test files:

```text
sample.txt
article.txt
repetition.txt
unique.txt
punctuation.txt
islam.txt
empty.txt
```

## Example Statistics

```text
=== TEXT STATISTICS ===

Total words        : 120
Unique words       : 75
Vocabulary ratio   : 62.50%
Longest word       : programming
Shortest word      : is
```

## Concepts Practiced

### Counter

Used to:

- Count word frequencies
- Find the most common words
- Search word occurrences

### deque

Used to:

- Store recent analyses
- Limit history size with `maxlen`

### JSON

Used to:

- Persist analysis history

## Project Structure

```text
01-text-analyzer-cli/
│
├── data/
│   ├── sample.txt
│   ├── article.txt
│   ├── repetition.txt
│   ├── unique.txt
│   ├── punctuation.txt
│   ├── islam.txt
│
├── src/
│   ├── analyzer.py
│   ├── menu.py
│   ├── storage.py
│   ├── utils.py
│   └── main.py
│
└── README.md
```

## Learning Goals

This project was created to practice:

- Modular programming
- File handling
- Data validation
- JSON persistence
- Python collections (`Counter`, `deque`)
- CLI application design