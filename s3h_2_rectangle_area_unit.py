lenght = float(input('input the lenght of the rectangle \n lenght='))
width = float(input('input the width of the rectangle\n width='))
unit = str(input('input the unit of the lenght and width with mm ,cm or m \n unit(mm/cm/m)='))

def area(lenght , width ,unit):
    if unit == 'mm':
       a = lenght * width * (10 ** (-6))
    elif unit =='cm':
       a = lenght * width * (10 ** (-4))
    else:
       a = lenght * width

    return a

print(f'The area of the rectangle is= {area(lenght ,width ,unit)} m^2')
