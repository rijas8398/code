def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation
print(translate(input("enter a phrase:")))


#comments are specified by hash tags
#for multiple line of codes use # tag in each lines or use triple quotes .
'''whjdbwd
dejndejdne
edelnfeslf
dnkd'''