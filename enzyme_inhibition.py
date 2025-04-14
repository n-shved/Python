x = int(input("Enter first number: "))
y = int(input("Enter last number: "))
z = int(input("Enter layout number: "))
a = int(input("Enter copy number: "))
b = str(input("Are there any Repeats/Exceptions? (Y/N): "))

if b == "Y":
    c = int(input("Number of Repeats?: "))
    if c == 0:
        pass
    else:
        d = int(input("Enter first R number: "))
        e = d + c
        counter1 = list(range(d, e))
        print("\n")

        for j in counter1:
            print("ISSPOTENCY" + str(j) + "_L" + str(z) + "C" + str(a) + "R")

    print("\n")
    f = int(input("Number of Exceptions?: "))
    if f == 0:
        pass
    else:
        g = int(input("Enter first R number: "))
        k = g + f
        counter2 = list(range(g, k))
        print("\n")

        for h in counter2:
            print("ISSPOTENCY" + str(h) + "_L" + str(z) + "C" + str(a) + "E")
else:
    pass

counter = list(range(x, y+1))
print("\n")

for i in counter:
    print("ISSPOTENCY" + str(i) + "_L" + str(z) + "C" + str(a))

print("\n")

for i in counter:
    print(i)