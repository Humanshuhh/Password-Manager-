def cerdit_card(number):
    i = number.length-2;
    while(i != 0):
        i = i * 2;
        if( i > 9):
            i = i - 9
        i = i-1
        sum = sum + i
    
    sum = sum + number.length -1 ;     
    



    
print(credit_card("4532015112830366"))
    
    