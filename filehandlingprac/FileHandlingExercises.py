#Exercise 1: Write User Name to File
 
# UserName = str(input("Enter your user name: "))
# with open("NewPracFile.txt", "w") as f:
#     f.write(UserName)
# print("username entered sucessfully:")
# with open("NewPracFile.txt") as f:
#     print(f.read())

from itertools import islice
#read first n lines
def read_cert_lines(filename, nlines):
    with open(filename) as f:
        for line in islice(f, nlines):
            print(line)

#append text to file
def append_text(filename, text):
    with open(filename, "a") as f:
        print(f.write("\n"+ text))

#read the full file
def read_full_file(filename):    
    with open(filename) as f:
        print(f.read())

#print only the last lines
fileslines=[]
def read_last_lines(filename, nlines):
    with open(filename) as f:
        for line in f:
            #print(line)
            fileslines.insert(0,line)
    # print(fileslines[nlines:0:-1])
    for i in fileslines[0:nlines]:
        text = i
        target = "\n"
        cleaned_text = text.replace(target, "")
        print(cleaned_text)

#optimal way as the old one was O(n^2) this is O(n)
from collections import deque

def read_last_lines_optimized(filename, nlines):
    # maxlen ensures the list never holds more than 'nlines' in memory
    with open(filename, 'r') as f:
        last_lines = deque(f, maxlen=nlines)
    
    # Print them in their original order, stripping the trailing newlines
    for line in last_lines:
        print(line.rstrip('\n'))

def read_longest_word(filename):
    words = set()
    max_len = 0
    with open(filename, "r") as f:
        for line in f:
            for word in line.split():
                word_len = len(word)
                if word_len > max_len:
                    max_len = word_len
                elif word_len == max_len and word_len >0:
                    words.add(word)
    return words
    #     words = f.read().split() #split() = Default Behavior: If no argument is provided, it splits the string at every whitespace character (spaces, tabs, newlines).
    # max_len = len(max(words, key=len)) 
    # print(max_len)
    # return (word for word in words if len(word) == max_len)

def line_count(filename):
    with open(filename, "r") as f:
        print(f"this file is {len(f.readlines())} lines long")

def word_count(filename):
    words = []
    with open(filename, "r") as f:
        words = f.read().split()
    print(len(words))

color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
def write_list_to_file(filename, list):
    with open(filename, "w") as f:
        for c in color:
            f.write(f"{c}\n")

#read a file and output a new file sorted in alphabetical order
def sort_file_alphabetical(filename, newfile):
    fileList = []
    with open(filename, "r") as f:
        for word in f:
            fileList.append(word)
    fileList.sort(key=str.lower)#key helps the sort function compare the upper case and lower case all as lower case because of ascii values
    #ascii_values = [ord(c[0]) for c in fileList]
    #print(ascii_values)
    with open(newfile, "w") as f:
        for space in fileList:
            if(space.endswith("\n")):
                f.write(space)
            else:
                f.write(f"{space}\n")
    #print(fileList)


def main():
    # Your program logic goes here
    #read_full_file("example.txt")
    #read_cert_lines("example.txt", 5)
    # sometext = str(input("Enter Some Text:" ))
    # append_text("NewPracFile.txt", sometext)
    # read_full_file("NewPracFile.txt")

    # read_last_lines("NewPracFile.txt", 3)
    # print()
    # read_last_lines_optimized("NewPracFile.txt", 3)
    # print()
    # print(read_longest_word("text.txt"))

    line_count("text.txt")
    word_count("text.txt")
    write_list_to_file("new_example.txt", color)
    sort_file_alphabetical("NewPracFile.txt", "new_example2.txt")

if __name__ == "__main__":
    main()
