"""
Nama    : Said Muhammad Mazaya
NIM     : 221402129

Soal 4 =  Write a Python class that calculates and stores the height and weight of a person in metric.
"""
class BMI:
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height

    def BMI_Value(self):
        weight = self.weight * 0.453592  # Convert pounds to kilograms
        height = self.height * 0.3048  # Convert feet to meters
        return weight / (height ** 2)

    def __eq__(self, other):
        if isinstance(other, BMI):
            return self.weight == other.weight and self.height == other.height
        return False

# Example usage:
bmi1 = BMI(150, 5.9)  # weight in pounds, height in feet
bmi2 = BMI(143, 6.2)
bmi3 = BMI(150, 5.9)

# Calculate BMI
print("BMI 1:", bmi1.BMI_Value())
print("BMI 2:", bmi2.BMI_Value())

# Compare two BMI
print(f"Is BMI Equal : {bmi1 == bmi2}")  
print(f"Is BMI Equal : {bmi1 == bmi3}")  


