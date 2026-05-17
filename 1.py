boy_name=input("boy name:")
girl_name=input("girl name:")
boy_age=int(input("boy age:"))
girl_age=int(input("girl age:"))
age_diff=abs(boy_age-girl_age)#abs is used becoz if the age number is higher for girl so that answer comes in minus no.which is wrong so abs is used to get the absolute
print(boy_name+" loves "+girl_name+". Age difference is: "+str(age_diff))
print(f"{boy_name} loves {girl_name}. Age difference is: {age_diff}")