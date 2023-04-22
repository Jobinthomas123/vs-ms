x = 5
while x < 1135:
    file = open(f"songtext/{x}.txt", "w")
    file.close()
    x = x + 1
