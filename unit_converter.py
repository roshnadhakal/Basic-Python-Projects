def miles_to_km(miles):
    # 1 mile = 1.60934 km
    return miles * 1.60934

def km_to_miles(km):
    # 1 kilometer = 0.621371 miles
    return km * 0.621371

def celsius_To_F(celsius):
    return(celsius * 9/5) + 32

def F_to_celsius(F):
    return (F - 32) * 5/9

# Main function to handle user input and conversion
def main():
    print("Unit Converter Program")
    print("1. Convert Miles to Kilometers")
    print("2. Convert Kilometers to Miles")
    print("3. Convert Celsius to Fahrenheit")
    print("4. Convert Fahrenheit to Celsius")
        
    choice = input("Enter your choice (1/2/3/4): ")

    if choice == "1":
        miles = float(input("Enter miles:"))
        km =  miles_to_km(miles)
        print(f"{miles} miles is equal to {km} kilometers")

    elif choice == "2":
        km = float(input("Enter Kilometers: "))
        miles = km_to_miles(km)
        print(f"{km} kilometers is equal to {miles} miles")
    
    elif choice == "3":
        celsius = float(input("Enter temperature in celsius: "))
        F = celsius_To_F(celsius)
        print(f"{celsius} degree celsius is equal to {F} degree fahrenheit")

    elif choice == "4":
        F = float(input("Enter temperature in fahrenheit: "))
        celsius = F_to_celsius(F)
        print(f"{F} degree fahrenheit is equal to {celsius} degree celsius.")

    else:
        print("Invalid choice")

main()

