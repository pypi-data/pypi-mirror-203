def palidrome(a):
    b=str(a)   
    print(b)        
    print(type(b))
    reverse=b[::-1]

    if b==reverse:
        print('palidrome')
    else:
        print('nonpalidrome')    

palidrome(a)