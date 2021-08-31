def solution(price, money, count):
    total = (count + 1) * count * price / 2
    return total - money if total - money > 0 else 0