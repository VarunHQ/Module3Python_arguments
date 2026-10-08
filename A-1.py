def total_calc(bill_amount, tip_percentage):
    #define a function to calc the tip and bill total

    total = bill_amount*(1 + 0.01*tip_percentage)
    total = round(total,2)
    print(f"You have to pay ${total} in your bill")

total_calc(170.56, 20)