def solution(enroll, referral, seller, amount):
    answer = []
    
    # seller해시, money해시 만들기
    seller_h = {} # 'john': '-', 'mary': '-', 'edward': 'mary', ...
    money_h = {}
    for i in range(len(enroll)): 
        seller_h[enroll[i]] = referral[i]
        money_h[enroll[i]] = 0
    
    # while: now_seller=='-'면 break, 해시를 따라 10%다단계 반복, 10%다단계동작 중 1원미만되면 break, 10%배분 후 now_seller 갱신
    for i in range(len(seller)):
        now_seller = seller[i]
        leftCash = amount[i]*100
        while True:
            if now_seller == '-': break
            cashToGive = int(leftCash*0.1)
            if cashToGive < 1:
                money_h[now_seller] += leftCash
                break
            else:
                money_h[now_seller] += (leftCash-cashToGive)
                leftCash = cashToGive
                now_seller = seller_h[now_seller]
    
    for name in enroll: answer.append(money_h[name])
    
    return answer
