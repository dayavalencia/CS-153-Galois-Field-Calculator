fo = open("input.txt", "r")
poly = fo.read().splitlines()

print poly[0] + ", " + poly[1] + ", " + poly[2]

print "A(x):"
poly_a = raw_input().split()

print "B(x):"
poly_b = raw_input().split()

print "P(x):"
poly_p = raw_input().split()

# Length
a_len = len(poly_a)
b_len = len(poly_b)

if (a_len > b_len):
    for x in range(0, a_len - b_len):
        poly_b.insert(0, "0")
    b_len = a_len
elif (a_len < b_len):
    for x in range(0, b_len - a_len):
        poly_a.insert(0, "0")
    a_len = b_len

print poly_a
print poly_b
print poly_p

print "Choose an operation:\n1. A(x) + B(x) \n2. A(x) - B(x)\n3. A(x) x B(x)\n4. A(x) / B(x)"
inp = input()

if (inp == 1):
    # Make sure to always throw up int() modifiers
    print "one"
    # Which of A(x) and B(x) are longer?
    # Get len() first, then add coefficients backwards from len() - 1
    sum = []
    for x in range(0, a_len):
        sum.append((int(poly_a[x]) + int(poly_b[x])) % 2)
    print sum

elif (inp == 2):
    print "two"

    diff = []
    for x in range(0, a_len):
        diff.append((int(poly_a[x]) - int(poly_b[x])) % 2)
    print diff

elif (inp == 3):
    print "three"
elif (inp == 4):
    print "four"

fo.close()
