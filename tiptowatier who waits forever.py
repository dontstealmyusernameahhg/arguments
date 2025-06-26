def function(bill, tip):
    total = bill + bill * tip / 100
    total = round(total, 2)
    print("Total amount to be paid is: $", total)

function(150, 20)