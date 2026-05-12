import string

with open("c:\\Users\\DELL\\Downloads\\essay-1.txt", "r") as file:
    essay1 = file.read()
essay1 = essay1.lower()
essay1 = essay1.translate(str.maketrans("", "", string.punctuation))
words1 = essay1.split()


with open("c:\\Users\\DELL\\Downloads\\essay-2.txt", "r") as file:
    essay2 = file.read()
essay2 = essay2.lower()
essay2 = essay2.translate(str.maketrans("", "", string.punctuation))
words2 = essay2.split()


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



set1 = set(words1)
set2 = set(words2)

intersection = set1 & set2
union = set1 | set2

plagialism = (len(intersection)/ len(union)) * 100

if plagialism >= 50:
    print("plagialism detected")
else:
    print("No plagialism detected")

def search_word(word, dictionary1, dictionary2 ):
    word = input("Enter word: ")
    if word in dictionary1 or dictionary2:
        if word in dictionary1:
            print(f"{word} appears in essay1: {dictionary1[word]} times")
        else:
         print(f"{word} does not appear in essay1")
        if  word in dictionary2:
            print(f"{word} appears in essay2: {dictionary2[word]} times")
        else:
            print(f"{word} does not appear in essay2")
        return True
    else:
        return False
    