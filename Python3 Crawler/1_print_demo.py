# BMI = weight / (height ** 2)

user_weight = float(input("Please enter your weight:"))
user_height = float(input("Please enter your height:"))
user_BMI = user_weight / user_height ** 2
print("Your BMI is :" + str(user_BMI))
