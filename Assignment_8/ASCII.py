


phrase = input("Enter a phrase: ")

print ("letter " + "ASCII " + "next_two_letter")
for i in phrase:
    character = i
    ASCII_code_of_character = ord(i)
    next_two_letter = ord(i) + 2
    print("%6c %5i, %15c" %(character, ASCII_code_of_character, next_two_letter ))
    
message = input("Enter a phrase: ")
print("letter", "ASCII", "next_two_letter")
for ch in message:
    character = ch
    ASCII_code_of_character = ord(ch)
    next_two_letter_of_character = ord(ch) + 2
    
    print("%6c %5i %15c"%(character, ASCII_code_of_character, next_two_letter_of_character))

    