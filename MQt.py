import random
power_names = ["RED POTION", "GREEN POTION", "SPIKES", "NEW MOVE", "LV1 ARMOR"]
power_des = ["Adds 5 max HP", "Gives one extra use of 'SWIPE'", "Monster takes 4dmg at start", "Random new move", "Damage taken is 75 percent"]
opt1 = random.randint(0, 4)
opt2 = random.randint(0, 4)
n_opt1 = power_names[opt1]
n_opt2 = power_names[opt2]
des_opt1 = power_des[opt1]
des_opt2 = power_des[opt2]
print("      POWERUPS      ")
print("====================")
print(f"{n_opt1}....{des_opt1}")
print(f"{n_opt2}....{des_opt2}")
print("====================")
ch = input("Option 1 or 2? ")