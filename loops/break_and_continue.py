count = 0
while True:
    print (count)
    count += 1
    if count >= 5:
        break


for x in range(10):
    # check if x is even
    if x % 2 == 0:
        continue
    print (x)

