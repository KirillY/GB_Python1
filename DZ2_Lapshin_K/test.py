L=[-32,235,45,35]
s=set(L)
L=list(s)
print(L)

def ave(*args):
    return sum(*args)
print(ave(1,3))

def pr_dict(**kwarg):
    for k, v in kwarg.items():
    print (k, v)

pr_dict(city='Москва', popul=25000000)