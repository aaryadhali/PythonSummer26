
#num = 5421


def reverse_num(num):
    reversed = 0
    while(num > 0):
        remainder = num % 10
        reversed = reversed * 10 + remainder #last number * 10 every loop traversal 
        #will add a 0 at the edn then add to the single number 
        num = num//10
        
        #print(remainder, end='')

    return(f"\n{reversed}")

print(reverse_num(5432))