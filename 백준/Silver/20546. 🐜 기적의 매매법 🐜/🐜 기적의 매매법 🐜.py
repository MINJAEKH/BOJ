money = int(input())
stocks_list = list(map(int, input().split()))

jh_money = money; sm_money = money
jh_stock = 0 ; sm_stock = 0
stock_change = [0]

for i in range(1,len(stocks_list)) :
    changes = stocks_list[i] - stocks_list[i-1]
    if changes == 0 :
        stock_change.append(0)
    elif changes > 0 :
        stock_change.append(1)
    elif changes < 0 :
        stock_change.append(-1)

def sm(day, stock, sm_money, sm_stock) :
    if day >= 3 :
        cnt = stock_change[day] + stock_change[day-1]+ stock_change[day-2]
        if cnt == -3 :
            
            buy = sm_money // stock
            sm_stock += buy
            sm_money -= stock*buy
        elif cnt == 3 :
            sm_money += stock*sm_stock
            sm_stock = 0
    #print(f'성민 : 남은 돈 {sm_money}원, 보유한 주식 수 {sm_stock}주')
    return sm_money, sm_stock

def jh(stock, jh_money, jh_stock) :
    buy = jh_money // stock
    jh_stock += buy
    jh_money -= stock*buy
    #print(f'주현 : 남은 돈 {jh_money}원, 보유한 주식 수 {jh_stock}주')
    return jh_money, jh_stock

def winner(jh_money, sm_money) :
    if jh_money > sm_money :
        print('BNP')
    elif jh_money < sm_money :
        print('TIMING')
    elif jh_money == sm_money :
        print('SAMESAME')

for day in range(len(stocks_list)) : 
    stock = stocks_list[day]
    if day == 13 :
        jh_money += stock * jh_stock
        sm_money += stock * sm_stock
        winner(jh_money, sm_money)
        break
        
    jh_money, jh_stock = jh(stock, jh_money, jh_stock)
    sm_money, sm_stock = sm(day, stock, sm_money, sm_stock)