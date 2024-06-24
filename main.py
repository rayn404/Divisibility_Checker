def mod(arg, div):
    arg=int(arg)
    div=int(div)
    return arg%div

ex=lambda x: x

limit=10**6

for i in range(1,limit+1):
    print(mod(ex(i),i))