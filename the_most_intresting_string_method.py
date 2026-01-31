#Here I will have a look at what I consider to be the most intresting/weird string method
#this string method basically encrypts strings. it can be decripted by being broken down using decription tables.
#in simple terms what this does is:
# str.translate() applies a character-mapping table to a string,
# allowing fast replacement or deletion of specific characters in a single operation.
text = "hello world, this is python"

# Create a translation table:
# - replace vowels with numbers
# - delete commas and spaces
table = str.maketrans(
    "aeiou",      # characters to replace
    "12345",      # replacements
    ", "          # characters to DELETE
)

result = text.translate(table)
print(result)

##little add on
textexample = "this is another example:"
print(textexample)
text1 = "hello, world"
text2 = "hell oworld"

print(text1.translate(table))
print(text2.translate(table))
