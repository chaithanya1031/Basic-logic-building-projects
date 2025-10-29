#character frequency
rand_str=input("enter random string:")
# print(rand_str)
characters={}
for char in rand_str:
    characters[char]=characters.get(char,0)+1
print(characters)