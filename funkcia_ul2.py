def text(n,txt = ''):
    x = len(txt)
    z = (n-(x+2))//2
    if x ==0:
        print(n*'*')
    else:
        if x%2 ==0:
            print (z*'*',txt,z*'*')
        else:
            print (z*'*',txt,(z+1)*'*')
text(20,'Hello world')
text(20,'Heyo world')
