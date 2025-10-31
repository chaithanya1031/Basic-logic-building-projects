dict1={'a':10,'b':20,'c':30}
dict2={'b':5,'c':15,'d':25}
output={}
for key,value in dict1.items():
    output[key]=value
print(output)
for key,value in dict2.items():
    if key in output:
        output[key]=output[key]+value
    else:
        output[key]=value
print(output)