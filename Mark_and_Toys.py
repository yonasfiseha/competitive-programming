def MaximumToys(prices, k):
    prices.sort()
    number_of_toys = 0
    ln = len(prices)
    for i in range(0, ln):
        k = k - prices[i]
        if k < 0:
            break
        number_of_toys = number_of_toys + 1
    return number_of_toys


print(MaximumToys([1, 2, 3, 4, 5], 2))
