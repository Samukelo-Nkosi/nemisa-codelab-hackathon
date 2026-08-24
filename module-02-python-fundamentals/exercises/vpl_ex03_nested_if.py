# Exercise 3: Nested If Statements

# Write a program that checks the temperature and humidity. If the temperature is above 30 degrees, check if the humidity is also above 70%. 
# Print appropriate messages based on these conditions. 
# Remember to test your program using different temperatures and humidities to ensure you get the correct output.

temperature = float(input("Enter the temperature: "))

humidity = float(input("Enter the humidity (%): "))

if temperature > 30:
    
    if humidity > 70:
        print("Temperature is above 30°C and humidity is above 70%.")
    else:
        print("Temperature is above 30°C, but humidity is not above 70%.")
else:
    print("Temperature is not above 30°C.")