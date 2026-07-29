#str = "hello"
# print(list(str))
# print(str[1])

def reverse_string(str):
    #mutstr = list(str)
    for i in str[::-1]:
        print(i,end ="")
    return ''

print(reverse_string("hello"))
print(reverse_string("hi my name is"))
#try:
myinput = str(input("Enter a word to reverse: "))
print(reverse_string(myinput))
