#Write a function convert_temp(value, unit) that converts Celsius to Fahrenheit when unit='C', and
#Fahrenheit to Celsius when unit='F'. Formula: F = C*9/5+32.
def convert_temp(value,unit):
    if unit=='C':
        F = value * 9/5 + 32
        return F
    elif unit=='F':
        C = (value - 32) * 5/9
        return C
    else:
        print("invaild unit")


print(convert_temp(25, 'C'))
print(convert_temp(98, 'F'))        

        