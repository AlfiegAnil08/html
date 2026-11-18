n=int(input("Enter your no"))
if n%400==0:
    print("leapyear")
elif n%100==0:
    print("not a leapyear")
elif n%4==0:
    print("leapyear")
else:
    print("not a leapyear")