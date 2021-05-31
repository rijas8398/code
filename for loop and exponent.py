friends=["muthu","manuttan","kunjutty"]
for friend in friends:
    print(friend)
for letter in "kottumala":
     print(letter)

for index in range(15):
    print(index)
for index in range(len(friends)):
    print(friends[index])

for index in range(5):
    if index==0:
        print("first iteration")
    else:
        print("not first iteration")



print("exponent")

def raise_to_power(base_num, pow_num):
    result=1
    for index in range(pow_num):
        result *= base_num
    return result
print(raise_to_power(2,5))