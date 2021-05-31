string=input("enter the string: ")
vowels=0
for ele in string:
    if (ele=='a' or ele=='e' or ele=='i' or ele=='o' or ele=='u' or   ele=='A' or ele=='E' or ele=='I' or ele=='O' or ele=='U'):
        vowels+=1
print("no of vowels are",vowels)
