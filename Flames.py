name1=list(input("enter your name:"))
name2=list(input("enter your partner name:"))
for i in name1:
    for n in name2:
        if i==n:
            name1.remove(i)
            name2.remove(n)
            break
for i in name1:
    for n in name2:
        if i==n:
            name1.remove(i)
            name2.remove(n)
            break
name1.extend(name2)
length=(len(name1))
print("your flames number is :",length)
print("\n\n\n")
if length==1:
    print("your relationship is Sister")
#enemy
elif length==2:
    print("your relationship is  Enemy")
elif length==4:
    print("your relationship is  Enemy")
elif length==7:
    print("your relationship is  Enemy")
elif length==9:
    print("your relationship is  Enemy")
elif length==15:
    print("your relationship is  Enemy")
elif length==20:
    print("your relationship is  Enemy")
#friend
elif length==3:
    print("your relationship is Friend")
elif length==5:
    print("your relationship is Friend")
elif length==16:
    print("your relationship is Friend")
elif length==18:
    print("your relationship is Friend")
elif length==14:
    print("your relationship is Friend")

#lover

elif length==19:
    print("your relationship is lover")
elif length==10:
    print("your relationship is lover")
#affection
elif length==8:
    print("your relationship is Affection")
elif length==12:
    print("your relationship is Affection")
elif length==17:
    print("your relationship is Affection")
elif length==13:
    print("your relationship is Affection")

#marriage
elif length==6:
    print("your relationship is marriage")
elif length==11:
    print("your relationship is marriage")

