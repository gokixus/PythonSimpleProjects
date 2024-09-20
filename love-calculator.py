name1 = input("Your name: ") #names input
name2 = input("Girlfriend/Boyfriend is name: ")

love = len(name1) + len(name2) 

if len(name1) > len(name2):
    love -= 5
else:
    love += 3
     
love *= 42
love = love / (100 + len(name2))
love = 10 if love > 10 else round(love, 0)
print(f"{name1} and {name2} score is {love} out of 10")