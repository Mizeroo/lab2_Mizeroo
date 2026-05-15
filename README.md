# Plagiarism Detector : Lab 2

## Project Overview
This is a Python program that compares two essays and determines if plagiarism has occurred by analyzing their content using file handling, data structures, and set operations.

---

## Project Structure

```
lab2/
├── plagiarism_detector.py  ← my  main Python script
├──   README.md             ← this file
├── essay1.txt              ← first essay
└── essay2.txt             ← second essay
```

## Key Concepts Used

### 1. File Handling : `open()`
Reading the essay files using the `with` statement:
```python
with open("essay1.txt", "r") as file:
    essay1 = file.read()
with open("essay2.txt", "r") as file:
    essay2 = file.read()
```

### 2. Text Cleaning
Before comparing, clean the text:
```python
import string

essay1 = essay1.lower()
essay1 = essay1.translate(str.maketrans("", "", string.punctuation))
words1 = essay1.split()

essay2 = essay2.lower()
essay2 = essay2.translate(str.maketrans("", "", string.punctuation))
words2 = essay2.split()
```
- `.lower()` : makes everything lowercase
- `.translate()` : removes punctuation
- `.split()` : breaks text into a list of individual words
  

### 3. Counting Words : Dictionary
```python
dictionary1 = {}
for word in words1:
    if word in dictionary1:
        dictionary1[word] = dictionary1[word] + 1
    else:
        dictionary1[word] = 1


dictionary2 = {}
for word in words2:
    if word in dictionary2:
        dictionary2[word] = dictionary2[word] + 1
    else:
        dictionary2[word] = 1
```


```

### 4. Search Function
```python
def search_word(word, dictionary1, dictionary2):
    if word in dictionary1 or word in dictionary2:
        if word in dictionary1:
            print(f"{word} appears in essay1: {dictionary1[word]} times")
        else:
            print(f"{word} does not appear in essay1")
        if word in dictionary2:
            print(f"{word} appears in essay2: {dictionary2[word]} times")
        else:
            print(f"{word} does not appear in essay2")
        return True
    else:
        return False
```
### 5. Comparing Essays :  Sets

```python
set1 = set(words1)
set2 = set(words2)

intersection = set1 & set2   # common words
union = set1 | set2          # all unique words
```

### 6. Plagiarism Percentage
```python
plagiarism = (len(intersection) / len(union)) * 100

if plagiarism >= 50:
    print("Plagiarism detected")
else:
    print("No plagiarism")

---

## Data Structures Summary

| Structure | Variable                      | Purpose                        |
| List      | `words1`, `words2`            | Store individual cleaned words |
| Dictionary| `dictionary1`, `dictionary2` | Store word counts              |
| Set       | `set1`, `set2`               | Compare essays |

---

## How to Run

1. Place `essay1.txt`, `essay2.txt`, and `plagiarism_detector.py` in the same folder
2. Open terminal in that folder
3. Run:
```bash
python plagiarism_detector.py
```

---

## Learning Outcomes

- File Handling — reading and processing text files
- Data Structures — lists, sets, and dictionaries
- String Manipulation — cleaning and splitting text
- Loops and Iteration — counting and comparing words
- Input/Output — searching words and displaying results
