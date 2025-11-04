apple = 15.5
orange = 20
grape = 10.25

total_volume = apple + orange + grape
print("Total volume sold:", total_volume, "liters")

total_volume_int = int(total_volume)
print("Total volume (integer):", total_volume_int, "liters")

total_volume_str = str(total_volume)
print("The total volume of juice sold today is " + total_volume_str + " liters.")

import random
bonus = random.randint(5, 10)
final_total = total_volume + bonus
print("Final total volume after adding bonus:", final_total, "liters")
