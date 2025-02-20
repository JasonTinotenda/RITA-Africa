temperature = float(input("Please enter the temperature for today: "))
if temperature < 0:
    print("Freezing")
elif temperature <= 15 :
    print("Cold")
elif temperature <=25 :
    print("Mild")
else:
    print("Hot")