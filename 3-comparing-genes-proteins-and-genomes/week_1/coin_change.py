def CoinChange(money, coins):
    if money == 0:
        return 0
    dpArr = [0] * (money + 1)
    for m in range(1, money+1):
        min_coins = money
        for coin in coins:
            if m >= coin:
                min_coins = min(min_coins, dpArr[m-coin]+1)
        dpArr[m] = min_coins
    return dpArr[money]

if __name__ == "__main__":
    money = 0
    coins = []
    with open('./datasets/dataset_243_10.txt') as f:
        money = int(f.readline().strip())
        coins = f.readline().strip().split(',')
        coins = [int(coin) for coin in coins]
    
    result = CoinChange(money, coins)
    with open('./results/coin_change.txt', 'w') as f:
        f.write(str(result))