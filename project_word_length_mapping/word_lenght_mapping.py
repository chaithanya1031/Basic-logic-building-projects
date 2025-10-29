#word length mapping
mapped_dct={}
word_lst=['apple','bat','banana']
for i in word_lst:
    value=len(i)
    mapped_dct[i]=value
print(mapped_dct)