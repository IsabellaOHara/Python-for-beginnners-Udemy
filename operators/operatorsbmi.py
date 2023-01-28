
def calcBMI(height, weight):
    heightInMeters = height * 0.4536
    bmi = weight / (heightInMeters * heightInMeters)
    return bmi


print(calcBMI(5.8, 70))

