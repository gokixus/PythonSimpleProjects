from random import choice

words = [
    choice(["Enchanting", "Amazing", "Colourful", "Delightful", "Delicate"]),
    choice(["visions", "distance", "conscience", "process", "chaos"]),
    choice(["superstitious", "contrasting", "graceful", "inviting", "contradicting", "overwhelming"]),
    choice(["true", "dark", "cold", "warm", "great"]),
    choice(["scenery","season", "colours","lights","Spring","Winter","Summer","Autumn"]),
    choice(["undeniable", "beautiful", "irreplaceable", "unbelievable", "irrevocable"]),
    choice(["inspiration", "imagination", "wisdom", "thoughts"])
]
a, b, c, d, e, f, g = words    
print(f"{a} {b},\n{c} {d} {e},\n{f} {g}.") # veya print("{} {},\n{} {} {},\n{} {}.".format(*words)) yapılabilir.
