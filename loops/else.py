count = 0
while(count < 5):
    print (count)
    count += 1
else:
    print ("count value reached %d" % count)

# the loop goes on untill we don't bump into number % (kratnoe) 5 and then the loop breakes
for i in range(1, 10):
    if(i % 5 == 0):
        break             #
    print (i)
else:
    print ("This is not printed cause for loop is terminated because of break but not due to fail in condition")
