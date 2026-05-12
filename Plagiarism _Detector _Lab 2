#  Open, read, and clean essays
# Step1: importing  string  to handle punctuations during cleaning
import string

# Step2: opening and cleaning essay1

with open("essay-1.txt", "r") as file:
    essay1 = file.read()
essay1 = essay1.lower()
essay1 = essay1.translate(str.maketrans("", "", string.punctuation))
words1 = essay1.split()

# Step3: opening and cleaning essay2

with open("essay-2.txt", "r") as file:
    essay2 = file.read()
essay2 = essay2.lower()
essay2 = essay2.translate(str.maketrans("", "", string.punctuation))
words2 = essay2.split()

# Step4: turning list (words1) into dictionary for finding common word and number of times it appeared.
# essay1
dictionary1 = {}

for word in words1:
    if word in dictionary1:
        dictionary1[word] = dictionary1[word] + 1
    else:
        dictionary1[word] = 1

# essay2

dictionary2 = {}

for word in words2:
    if word in dictionary2:
        dictionary2[word] = dictionary2[word] + 1
    else:
        dictionary2[word] = 1

#Step5:  Allowing user to Search for a Specific Word

def search_word(word, dictionary1, dictionary2 ):
    word = input("Enter word: ")
    if word in dictionary1 or word in dictionary2:
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
        

# Step6: to culculate plagialism, we need lists but in form of set to avaid duplicate

set1 = set(words1)
set2 = set(words2)

intersection = set1 & set2
union = set1 | set2

plagialism = (len(intersection)/ len(union)) * 100

# Making decision

if plagialism >= 50:
    print("plagialism detected")
else:
    print("No plagialism detected")

# Step7:  at this stage i can call the ficntion, if i want to check for particlur word
search_word( "", dictionary1, dictionary2)



    
