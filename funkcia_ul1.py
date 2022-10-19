def rec(a:int,x = '*'):
    print(a*x)
    print(x+(a-2)*' '+x)
    print(a*x)
rec(7,'x')
