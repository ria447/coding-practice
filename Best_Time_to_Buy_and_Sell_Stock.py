def maxProfit(prices):
        prev_element = prices[0]
        count = 0
        max_profit = 0

        for i in range(1, len(prices)):
            if prices[i] < prev_element:
                count = count + 1
                prev_element = prices[i]

            else:
                if prices[i] - prev_element > max_profit:
                    max_profit = prices[i] - prev_element
                    

        if count == (len(prices) - 1):
            return 0
        else:

            return max_profit

prices = eval(input("Enter a list:"))
output = maxProfit(prices)
print(output)
