#invert dictionary
dct1={'a':1,'b':2,'c':3}
print(dct1)
new_dct={}
for key,value in dct1.items():
    new_dct[value]=key
print(new_dct)