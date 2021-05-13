from datetime import date


class HeartRates:
    def __init__(self, Name, Surname, Birth_year):
        self.Name = Name
        self.Surname = Surname
        self.Birth_year = Birth_year

    def ageCalculate(self):
        today = date.today()
        year = int(today.strftime("%Y"))
        print("year:{}".format(year))
        age = year - self.Birth_year
        return age

    def bottomBound(self, age):
        if age <= 20:
            return 200 * 0.5
        elif 30 >= age > 20:
            return 190 * 0.5
        elif 35 >= age > 30:
            return 185 * 0.5
        elif 40 >= age > 35:
            return 180 * 0.5
        elif 45 >= age > 40:
            return 175 * 0.5
        elif 50 >= age > 45:
            return 170 * 0.5
        elif 55 >= age > 50:
            return 165 * 0.5
        elif 60 >= age > 55:
            return 160 * 0.5
        elif 65 >= age > 60:
            return 155 * 0.5
        elif 70 >= age > 65:
            return 150 * 0.5
        else:
            return 0

    def upperBound(self, age):
        if age <= 20:
            return 200 * 0.85
        elif 30 >= age > 20:
            return 190 * 0.85
        elif 35 >= age > 30:
            return 185 * 0.85
        elif 40 >= age > 35:
            return 180 * 0.85
        elif 45 >= age > 40:
            return 175 * 0.85
        elif 50 >= age > 45:
            return 170 * 0.85
        elif 55 >= age > 50:
            return 165 * 0.85
        elif 60 >= age > 55:
            return 160 * 0.85
        elif 65 >= age > 60:
            return 155 * 0.85
        elif 70 >= age > 65:
            return 150 * 0.85
        else:
            return 0

    def result(self, age):

        print("**********PERSONAL INFORMATION**********")
        print("Name: {}".format(self.Name))
        print("Surname: {}".format(self.Surname))
        print("Age: {}".format(self.ageCalculate()))
        print("Target heart rate between {}-{} bps".format(self.bottomBound(age), self.upperBound(age)))
