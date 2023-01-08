n = int(input())

for _ in range(n):
    a, b= input().split()
    size_type_a = a[-1]
    size_type_b = b[-1]
      
    if(size_type_a == size_type_b):
        if(size_type_a == 'S'):
             # for small the larger the x value the smaller the shirt
            if(len(a) == len(b)):
                print('=')
            elif(len(a) > len(b)):
                print('<')
            else:
                print('>')     
        else:
            # for medium and large the larger the x value the smaller the shirt
            if(len(a) == len(b)):
                print('=')
            elif(len(a) > len(b)):
                print('>')
            else:
                print('<')
    else:
    
        # since ord of S > M > L
        if(ord(size_type_a) > ord(size_type_b)):
            print('<')
        else:
            print('>')
        
            
        
            

                 
     
