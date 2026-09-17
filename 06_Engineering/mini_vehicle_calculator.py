print("Hi")
name = input("What is your name? ")
print("Hello, " + name + "! Welcome to the mini vehicle calculator.")
vehicle_mass = float(input("What is your vehicle's mass in kilograms? "))
print("Your vehicle's mass is", vehicle_mass, "kg")
vehicle_power = float(input(" What is your vehicle's power in watts?"))
print("Your vehicle's power is", vehicle_power, "W")
vehicle_speed = float(input("What's your vehicle's speed in meters per second? "))
print("Your vehicle's speed is", vehicle_speed, "m/s")
if vehicle_speed > 100:
    print("Your vehicle is very fast!", "High Speed")
else:
    print("Your vehicle is not very fast.", "Low Speed")
weight = vehicle_mass * 9.81
print("Your vehicle's weight is", weight, "N")
power_to_weight_ratio = vehicle_power / weight
print("Your vehicle's power to weight ratio is", power_to_weight_ratio, "W/N")
time_travelled = int(input("How long did your vehicle travel in seconds? "))
print("Your vehicle travelled for", time_travelled, "seconds")
distance_travelled = vehicle_speed * time_travelled
print("Your vehicle travelled", distance_travelled, "meters")