print("LIST")

friends=["kunjutty","muthu","manuttan","muthutty"]
print(friends[0])
print(friends[1:])
print(friends[0:3])
friends[3]="manuppa"
print(friends[3])
print(friends)

lucky_no=[8,3,9,83,98,8398]
friends.extend(lucky_no)
print(friends)
friends.append("muthutty")
print(friends)
friends.insert(2,"kutttippa")
print(friends)
friends.remove("muthutty")
print(friends)
lucky_no.clear()
print(lucky_no)
friends.pop()
print(friends)
print(friends.index("kutttippa"))
print(friends.index("manuttan"))
print(friends.count("kunjutty"))
print(friends.append("manuttan"))
print(friends.count("manuttan"))

print(friends)

print(friends)
friends.pop()
print(friends)
friends.pop()
friends.pop()
friends.pop()
print(friends)
friends.pop()
friends.pop()
print(friends)
friends.sort()
print(friends)
lucky_no=[8,3,9,83,98,8398]
print(lucky_no)
lucky_no.sort()
print(lucky_no)
lucky_no.reverse()
print(lucky_no)
frnds2=friends.copy()
print(frnds2)


print("tuples")
coordinates=(2,5,7)
print(coordinates)
coordinates[1] = 3
print(coordinates)