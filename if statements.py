is_male =True
is_tall =False

if is_male or is_tall:
    print("you are a male or you are tall")
else:
    print("you are neither male nor tall")

is_male =True
is_tall =False

if is_male and is_tall:
    print(" you are a tall male")
else:
    print("you either not male or not tall or both")


is_male =True
is_tall =False

if is_male and is_tall:
    print(" you are a tall male")
elif is_male and not(is_tall):
    print("you are a short male ")
elif not(is_male) and is_tall:
    print("you are not a male but tall")
else:
    print("you are not a male not a tall")


def min_num(num1,num2,num3):
    if num1<= num2 and num1<=num3:
        return num1
    elif num2<=num1 and num2<=num3:
        return num2
    else:
        return num3
print(min_num(5,9,13))
print(min_num(87,25,36))