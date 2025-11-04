rice_price = 45
sugar_price = 40
oil_price = 130

rice_qty = 3
sugar_qty = 2.5
oil_qty = 1.8

rice_total = rice_price * rice_qty
sugar_total = sugar_price * sugar_qty
oil_total = oil_price * oil_qty

total_bill = rice_total + sugar_total + oil_total
print("Total for rice:", rice_total)
print("Total for sugar:", sugar_total)
print("Total for oil:", oil_total)
print("Final total bill:", total_bill)

total_bill_int = int(total_bill)
print("Total bill (integer):", total_bill_int)

total_bill_str = str(total_bill)
print("The total bill amount is " + total_bill_str)

import random
delivery_charge = random.randint(5, 10)
final_amount = total_bill + delivery_charge
print("Final bill including delivery charge:", final_amount)
