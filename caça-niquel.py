from random import choice
print(''' 
****************************************
2 EMOJIS IGUAIS 30 PONTOS
OS 3 EMOJIS IGUAIS 100 PONTOS
PRESSIONE s PARA CONTINUAR E n PRA PARAR
****************************************''')

x = 0
y = 0
pt = ' '

while True:
    emoji = ["😃","😠","😅"]



    a = choice(emoji)
    b = choice(emoji)
    c = choice(emoji)
 
    
    print('\n\n',a, b, c,'\n\n')
    
    
    if a == b or b == a and [a,b] != c or a == c or c == a and [a,c] != b or b == c or c == b and [b,c] == a:
        pt = '\033[0;33m30 PTs\033[m'
        y += 30
     
    

    if a == b and a == c:
        pt = '\033[0;32m100 PTs\033[m'
        if y == 0:
            x += 100
        else:
            x += 70 
            
    if a != b and a != c and b != a and b != c and c != b and c != a:
        pt = "00 PTs"
    
    print(pt)   
    a = y + x
    print("Placar: {}".format(a))
        
    b = input("Quer Continuar? ")
    if b in "nN":
        break
    
    


    
    


