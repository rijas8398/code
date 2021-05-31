def equal(s1,s2):
    if (len(s1)==len(s2)):
        for i in range(len(s2)):
            if s1[i]==s2[i]:
                continue
            else:
                print("not equal")
                return
        print("equal")
    else:
        print("not equal")
    return
s1="rijas"
s2="rijase"
equal(s1,s2)
