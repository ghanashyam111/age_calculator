name = input(" Whats your name: ")
age = input (" Whats your age: ")
current_year = 2025
future_year = 2030
age_now = current_year - int(age)
age_future = int(age) + (future_year - current_year)
print(name +" is a big bussinessman and he was born in a small town on  " + str(age_now) + ",")
print(" in " + str(future_year) + " he will become " + str(age_future) + " years old ")
