# Conversion of temperature to fahrenheit
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9 

# Conversion of temperature to celsius
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    """This will accept temperature in fahrenheit, convert and return celsius"""
    FAHRENHEIT_TO_CELSIUS_FACTOR = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit}°F is {FAHRENHEIT_TO_CELSIUS_FACTOR}°C")
 
def convert_to_fahrenheit(celsius):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    """This will accept temperature in celsius, convert and return fahrenheit"""
    CELSIUS_TO_FAHRENHEIT_FACTOR = (celsius * 9/5) + 32
    print(f"{celsius}°C is {CELSIUS_TO_FAHRENHEIT_FACTOR}°F")


temperature = input("Enter the temperature to convert: ")
fahrenheit_or_celsius = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper().strip()
if temperature.isdigit() and fahrenheit_or_celsius == 'F':
    convert_to_celsius(fahrenheit=int(temperature))
elif temperature.isdigit() and fahrenheit_or_celsius == 'C':
    convert_to_fahrenheit(celsius=int(temperature))
else:
    print("Invalid temperature. Please enter a numeric value.")
