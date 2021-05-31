import random as r

lst = []
for _ in range(20):
    ph_no = []

    # the first number should be in the range of 6 to 9
    ph_no.append(str(r.randint(6, 9)))

    # the for loop is used to append the other 9 numbers.
    # the other 9 numbers can be in the range of 0 to 9.
    for i in range(1, 10):
        ph_no.append(str(r.randint(0, 9)))

    # printing the number
    lst.append(("").join(ph_no))

for ele in lst:
    print(ele)