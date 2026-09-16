def calculate_distance(speed, time):
    distance = speed * time
    return distance

distance = calculate_distance(340, 20)
print("The distance traveled is", distance, "m")

def calculate_power_to_weight_ratio(power, weight):
    ratio = power / weight
    return ratio

ratio = calculate_power_to_weight_ratio(700, 1500)
print("Power to weight ratio is", ratio, "W/kg")