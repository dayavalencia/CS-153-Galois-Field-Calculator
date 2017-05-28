def mult(a, b, poly_p):
    bin_a = bin(int(a)) # 0b11111
    bin_b = bin(int(b)) # 0b00000

    bin_a = list(bin_a[2:])
    bin_b = list(bin_b[2:])

    final_product = [0 for x in range(len(bin_a) + len(bin_b) - 1)]
    sub_product = [[0 for x in range(len(bin_a))] for y in range(len(bin_b))]

    for x in range(len(bin_b)):
        for y in range(len(bin_a)):
            if (bin_b[x] == '1'):
                sub_product[x][y] = bin_a[y]
            else:
                sub_product[x][y] = '0'

    print sub_product

def add(a, b):
    bin_a = bin(a) # 0b11111
    bin_b = bin(b) # 0b00000

    bin_a = bin_a[2:]
    bin_b = bin_b[2:]

    bin_sum = ""

    if (len(bin_a) > len(bin_b)):
        for x in range(0, len(bin_a) - len(bin_b)):
            bin_b = '0' + bin_b
    elif (len(bin_a) < len(bin_b)):
        for x in range(0, len(bin_b) - len(bin_a) ):
            bin_a = '0' + bin_a

    for x in range(max(len(bin_a), len(bin_b))):
        if (bin_a[x] == bin_b[x]):
            bin_sum = bin_sum + '0'
        else:
            bin_sum = bin_sum + '1'

    return int(bin_sum, 2)

print "A(x):"
poly_a = raw_input().split()

print "B(x):"
poly_b = raw_input().split()

print "P(x):"
poly_p = raw_input().split()

# Length
a_len = len(poly_a)
b_len = len(poly_b)

print poly_a
print poly_b
print poly_p

print "Choose an operation:\n1. A(x) + B(x) \n2. A(x) - B(x)\n3. A(x) x B(x)\n4. A(x) / B(x)"
inp = input()

if (inp == 1):
    # Make sure to always throw up int() modifiers
    # Which of A(x) and B(x) are longer?
    # Get len() first, then add coefficients backwards from len() - 1
    sum = []
    sum_s =  ""

    if (a_len > b_len):
        for x in range(0, a_len - b_len):
            poly_b.insert(0, "0")
    elif (a_len < b_len):
        for x in range(0, b_len - a_len):
            poly_a.insert(0, "0")

    for x in range(0, max(a_len, b_len)):
        sum.append(add(int(poly_a[x]), int(poly_b[x])))
        print "Adding digits: " + str(poly_a[x]) + " and " + str(poly_b[x]) + " --> " + str(add(int(poly_a[x]), int(poly_b[x])))

    for x in range(len(sum)):
        sum_s = sum_s + str(sum[x]) + " "

    print "A(x) + B(x) is " + sum_s
elif (inp == 2):
    diff = []

    diff_s = ""

    if (a_len > b_len):
        for x in range(0, a_len - b_len):
            poly_b.insert(0, "0")
    elif (a_len < b_len):
        for x in range(0, b_len - a_len):
            poly_a.insert(0, "0")

    for x in range(0, max(a_len, b_len)):
        diff.append(add(int(poly_a[x]), int(poly_b[x])))
        print "Subtracting digits: " + str(poly_a[x]) + " and " + str(poly_b[x]) + " --> " + str(add(int(poly_a[x]), int(poly_b[x])))

    for x in range(len(diff)):
        diff_s = diff_s + str(diff[x]) + " "

    print "A(x) - B(x) is " + diff_s

elif (inp == 3):
    final_product = [0 for x in range(a_len + b_len - 1)]
    sub_product = [[0 for x in range(a_len)] for y in range(b_len)]

    for x in range(0, b_len):
        for y in range(0, a_len):
            sub_product[x][y] = mult(poly_b[x], poly_a[y], poly_p)

    # for every subproduct array, we move one starting index to the right
    # for every element in every subproduct array, we add to sub_product

    for x in range(0, 3):
        for y in range(len(sub_product[x])):
            final_product[x + y] = final_product[x + y] + sub_product[x][y] # replace with add()

    print final_product


elif (inp == 4):
    pass
