#Employee salary filter
employees={'ramesh':50000,
           'akshay':45000,
           'revanth':100000,
           'sreenu':75000,
           'venu':80000,
           'naresh':40000}
top_paid={}
for key,value in employees.items():
    if value>50000:
        top_paid[key]=value
print(f"high paid employee are {top_paid}")