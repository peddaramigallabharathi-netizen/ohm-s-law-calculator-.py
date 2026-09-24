print("=== Ohm's Law Calculator ===")
print("1. Calculate Voltage (V)")
print("2. Calculate Current (I)")
print("3. Calculate Resistance (R)")

choice = input("Choose an option (1/2/3): ")

try:
    if choice == "1":
        current = float(input("Enter current (A): "))
        resistance = float(input("Enter resistance (Ω): "))
        voltage = current * resistance
        print(f"Voltage = {voltage:.2f} V")

    elif choice == "2":
        voltage = float(input("Enter voltage (V): "))
        resistance = float(input("Enter resistance (Ω): "))

        if resistance == 0:
            print("Resistance cannot be zero.")
        else:
            current = voltage / resistance
            print(f"Current = {current:.2f} A")

    elif choice == "3":
        voltage = float(input("Enter voltage (V): "))
        current = float(input("Enter current (A): "))

        if current == 0:
            print("Current cannot be zero.")
        else:
            resistance = voltage / current
            print(f"Resistance = {resistance:.2f} Ω")

    else:
        print("Invalid choice.")

except ValueError:
    print("Please enter numbers only.")
