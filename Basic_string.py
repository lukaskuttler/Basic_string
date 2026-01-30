#its when there are a bunch of letters, you use quotes or a bunch of quotes
# to show that they are part of the same string.
#A string is a sequence of characters representing text data in Python.
# It must be enclosed in either single or double quotation marks.
# Strings can contain any combination of letters, numbers, symbols, spaces, and special characters.
# They are one of the fundamental data types used for storing and manipulating text.

#11:25String: A sequence of characters representing text data, enclosed in quotation marks,
# that can contain letters, numbers, symbols, and spaces.
#Index: A numerical position that identifies the location of an element within a sequence,
# starting at 0 for the first element in Python.


text = "hello world 2" # single vs double
print(text)
text = 'hello world 2'
print(text[4])
#it counts spaces and starts from 0
print(len(text)) #length of the text
text= ""
print(len(text))

text = "Bob"
print(text[-1]) #last character in the string
print(text[-3])

#print(text[3]) this is an IndexError is a runtime error that happens when your program
# tries to access an element in a sequence using an index that doesn’t exist.

#print(text[6/3]) , this is also an error as its a float and not an integer,
#
# you can fix this by adding another slash.
print(text[6//3])



#-----------------------------
#you can add two strings
#additionante
s1 = "hello"
s2 = "bye"
print(s1 + s2)
print(s1*4) #Only with integer number


#String is iterable, you can use for over it
s1 = "Hello my name is Bob"
for c in s1 :
    print(c)

s1 = "I like to give hi fives"
#Print this string, but replace 'i' with 'y'
#End result should be : Y lyke to gyve hy fyves
for c in s1 :
    if c== "i":
        print("y", end="")
    elif c== "I":
        print("Y", end="")
    else:
        print(c, end="")
print()


s1_new = ""









# 
