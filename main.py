from HeartRates import HeartRates

print("***************************************************************************************************************")
print("Could you please enter your information to calculate target heart rate...\n")
print("***************************************************************************************************************")
Name = input("Name: ")
Surname = input("Surname: ")
Birthday = input("Date of birth (format: xx/xx/xxxx): ")

year = int(Birthday[6:10])
person = HeartRates(Name,Surname,year)
personAge = person.ageCalculate()
print("***************************************************************************************************************")
heartRate = person.result(personAge)
print("***************************************************************************************************************")