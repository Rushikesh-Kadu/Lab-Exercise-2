class NotEligible(Exception):
    pass

age = int(input("Enter Age:"))
if(age>=18):
    print("Eligible for permanat driving license")
else:
    raise NotEligible("Not Eligible")