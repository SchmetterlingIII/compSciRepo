def enhancedCalc():
    first = float(input("Enter your first number: "))
    second = float(input("Enter your second number: "))

    sum = first + second

    difference = 0 
    quotient = 0 
    if first > second:
        difference = first - second
        quotient = first%second
    else:
        difference = second - first
        quotient = second%first

    product = first * second

    print(f'''Your sum is {sum:.2f}\nThe difference is {difference:.2f}\nProduct: {product:.2f}\nQuotient: {quotient:.2f}''')





