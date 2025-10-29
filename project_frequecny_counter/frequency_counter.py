#frequency counter
sentence=input('enter a random sentence: ')
words=sentence.split()
#krishna is a good boy and a smart boy
output={}
for word in words:
    output[word]=words.count(word)
print(output)