def calculator():
    number = int(input("type a number"))
    totaleven = []
    totalodd = []
    for i in range(1, number+1):
        if i%2 == 0:
            totaleven.append(i)
        if i%2 == 1:
            totalodd.append(i)
    sumeven = 0
    sumodd = 0
    for even in totaleven:
        sumeven = sumeven + even
    for odd in totalodd:
        sumodd = sumodd + odd
    print("Sum of odd numbers = ", sumodd)
    print("Average of even numbers = ", sumeven/len(totaleven))
calculator()