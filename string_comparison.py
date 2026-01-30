s = "cat"
#s[0] = "r"
s = "r" + s[1:]
print(s)
#This code changes "cat" into "rat", and it does it the only way strings allow.
#Basically you take r and then add the last 2 letters.

s1 = "bob"
s2 = "banana"
print(s1)
print(s1 < s2)
#this goes from the left to right, b mathces , and then o and a dont match ,
# so the better one end up being the first one on the alphabet.

s1 = "BOB"
s2 = "bob"
print(s1 > s2)

##Python compares strings alphabetically, character by character, using their ASCII/Unicode values.
⚠#️ Capital letters come before lowercase letters in ASCII.
#So:
#"B" (uppercase) has a smaller value
#"b" (lowercase) has a larger value


#in operator checks is a string 