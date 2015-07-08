#!/usr/bin/env python3

# Convert Fahrenheit to Celsius

Fahrenheit = float(input("Enter a temperature in Fahrenheit: "))

Celsius = (Fahrenheit - 32) * 5.0/9.0

print("Temperature: {F} Fahrenheit = {C} Celsius".format(F=Fahrenheit, C=Celsius))


# Convert Celsius to Fahrenheit

Celsius = float(input("Enter a temperature in Celsius: "))

Fahrenheit = 9.0/5.0 * Celsius + 32

print("Temperature: {C} Celsius = {F} Fahrenheit".format(F=Fahrenheit, C=Celsius))



