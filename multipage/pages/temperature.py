from taipy.gui import Markdown

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

fahrenheit = 100
celsius = fahrenheit_to_celsius(fahrenheit)

temperature_md = Markdown("""
# Fahrenheit to Celsius

Farenheit: <|{fahrenheit}|>
Celsius: <|{celsius}|>
""")