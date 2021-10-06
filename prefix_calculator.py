# prefix calculator
digits = '0123456789'
stack = []



def prefixCalculator(expression):
    for i in expression[::-1]:
        if i in digits:
            stack.append(int(i))
        else:
            d1 = stack.pop()
            d2 = stack.pop()
            if i == '+':
                stack.append(d1 + d2)
            elif i == '-':
                stack.append(d1 - d2)

            elif i == '*':
                stack.append(d1 * d2)

            elif i == '/':
                stack.append(d1 / d2)

    return stack.pop()


print(prefixCalculator('+5*24'))
