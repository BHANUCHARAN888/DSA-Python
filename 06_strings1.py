# Strings
# Slicing strings
word="Learning Python"
# index 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14
# total length of string is 15 ,index start from 0 to 14
print(word[0])
print(word[9])
print(word[0:15])  
print(word[0:8])
print(word[9:15])
print(word[0:15:2])  
print(word[0:15:3])
# Negative indexing -15 -14 -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
print(word[-15])
print(word[-6])
print(word[-15:-1])
# srring methods
print(len(word)) #t the length of the string
print(word.lower()) #convert to lower case
print(word.upper()) #convert to upper 
print(word.title()) #convert to title case
print(word.find("Python")) #find the index of substring
print(word.count("P")) #count the number of occurrences of a substring
print(word.replace("Python", "Java")) #replace substring
print(word.split(" ")) #split the string into a list
print(word.strip()) #remove leading and trailing whitespace
print(word.lstrip()) #remove leading whitespace
print(word.rstrip()) #remove trailing whitespace
print(word.join(["is", "fun"])) #join a list of strings with the original string as a separator
print(word.startswith("Learning")) #check if the string starts with a substring
print(word.endswith("Python")) #check if the string ends with a substring