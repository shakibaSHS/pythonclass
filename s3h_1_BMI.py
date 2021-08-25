weight = int(input('input your weight in kg\n weight='))
height = float(input('input your height in meter\n height='))

def BMI(weight , height):
    B = weight / (height ** 2)
    return B

print(f'Your BMI is= {BMI(weight , height)}')
