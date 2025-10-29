#key existence
dct={'name':'Vinod','age':18,'skills':['python','java']}
rand_key=input("check whether key is existed or not: ")
if rand_key in dct.keys():
    print('key existed')
else:
    print('key not existed')