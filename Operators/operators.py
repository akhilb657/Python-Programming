#bmi = (weight in kg) / (height ** 2 in meters)
def calculateBMI(height,weight=60):
    heightInMeters = height * 0.4536

    BMI = weight / (heightInMeters ** 2)
    return BMI

print(calculateBMI(5.9,65))
print(calculateBMI(6))
print(calculateBMI(5.4,58))

