marklist=[]
scorelist=[]
no_students = int(input("no of students "))
for i in range(no_students):
    name = input("enter names ")
    score = float(input("enter scores "))
    marklist += [[name,score]]
    scorelist += [score]

scorelist =list(dict.fromkeys(scorelist))

b = sorted(scorelist)[1]
for a,c in sorted(marklist):
    if c == b:
        print(a)
        
