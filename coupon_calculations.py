"""
Program name: coupon_calculations.py
Author: Rachel Li
Last modified date: 06/09/2020

The purpose of this program is to write function that accepts
amount of purchase, cash coupon, percent coupon,
and it will calculate and return total order item.
"""

#calculate price after cash coupon and percent coupon
def calculate_price(price, cash_coupon, percent_coupon):
    if cash_coupon == 5:
        if percent_coupon == 10:
            pre_shipping_cost = (price - cash_coupon)*(1-percent_coupon/100)
        elif percent_coupon == 15:
            pre_shipping_cost = (price - cash_coupon)*(1-percent_coupon/100)
        elif percent_coupon == 20:
            pre_shipping_cost = (price - cash_coupon)*(1-percent_coupon/100)
    elif cash_coupon == 10:
        if percent_coupon == 10:
            pre_shipping_cost = (price - cash_coupon)*(1-percent_coupon/100)
        elif percent_coupon == 15:
            pre_shipping_cost = (price - cash_coupon)*(1-percent_coupon/100)
        elif percent_coupon == 20:
            pre_shipping_cost = (price - cash_coupon)*(1-percent_coupon/100)
    return pre_shipping_cost

def calculate_shipping(pre_shipping_cost):
    if pre_shipping_cost < 10.00:
        shipping = 5.95
        with_shipping = pre_shipping_cost + shipping
    if 10.00 <= pre_shipping_cost < 30.00:
        shipping = 7.95
        with_shipping = pre_shipping_cost + shipping
    if 30.00 <= pre_shipping_cost < 50.00:
        shipping = 11.95
        with_shipping = pre_shipping_cost + shipping
    if pre_shipping_cost >= 50.00:
        shipping = 0.00
        with_shipping = pre_shipping_cost + shipping
    return with_shipping

price = float(input("Price of item:$ "))
cash_coupon = float(input("Cash Coupon 5 or 10:$ "))
percent_coupon = float(input("Percent discount 10, 15 or 20: "))
tax = 1.06
cost = calculate_shipping(calculate_price(price, cash_coupon, percent_coupon))*tax
print(f'The total price after tax is ${cost:.2f}')

if __name__ == '__main__':
    pass
