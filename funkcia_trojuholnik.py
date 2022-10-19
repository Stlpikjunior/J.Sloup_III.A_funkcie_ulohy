def trj(k, zn = '*'):
    for i in range(1,k+1,2):
        x = int((k-i))
        print((x)*' '+(zn+' ')*i)

trj(7,'*')