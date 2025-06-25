while True:
    mpg = float(input("Enter fuel consumption in miles per gallon (mpg), or 0 to exit: "))
    if mpg == 0:
        print("Exiting program.")
        break
    litres_per_100km = 4.54609 / (mpg * 1.60934) * 100
    litres_per_km = litres_per_100km / 100
    print(f"Fuel consumption: {litres_per_km:.4f} litres per kilometre\n")