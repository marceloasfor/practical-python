def loop():
    day = 1
    bills = 1
    bill_thickness = 0.11 * 0.001 # Meters (0.11 mm)
    tower_height = 442 # Height (meters)
    while bills * bill_thickness < tower_height:
        bills = bills * 2
        day += 1
        print(f'Day = {day} | # bills = {bills} | Height = {bills * bill_thickness}')
    
    print(day)

loop()
