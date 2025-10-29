🧠 **Frequency Counter**
📘 **Overview**

This is a simple Python program that takes a sentence as input and counts how many times each word appears in that sentence.
It demonstrates basic concepts like string manipulation, lists, and dictionaries in Python.

**🧩 How It Works**

The program asks the user to enter a random sentence.

It splits the sentence into individual words using the split() method.

It then creates an empty dictionary (output) to store the word frequencies.

For each word in the sentence:

It counts how many times the word appears using words.count(word).

It stores that count in the dictionary with the word as the key.

Finally, it prints the dictionary showing each word and its frequency.

**💻 Example Run**
enter a random sentence: krishna is a good boy and a smart boy

Output:
{'krishna': 1, 'is': 1, 'a': 2, 'good': 1, 'boy': 2, 'and': 1, 'smart': 1}

**🧠 Key Concepts Demonstrated**

input() – To get user input.

split() – To break a sentence into a list of words.

for loop – To iterate through each word.

Dictionary – To store key-value pairs (word → frequency).

count() – To count the occurrences of a word in the list.

**⚙️ Possible Improvements**

Make it case-insensitive (so Boy and boy are counted as the same).

Remove punctuation before counting.

Use a more efficient counting method with collections.Counter to improve performance.

**🚀 Enhanced Version (Efficient)**
from collections import Counter

sentence = input("Enter a random sentence: ")
words = sentence.lower().split()
output = Counter(words)
print(dict(output))