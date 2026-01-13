while True:
    print("Welcome to the bill splitter App")

    while True:
        Bill = float(input("Enter total bill amount: "))
        if Bill <= 0:
            print("Bill amount is not negative.")
        else:
            break
    
    while True:
        People = int(input("Enter total number of people: "))
        if People <= 0:
            print("Number of people is not negative.")
        else:
            break        

    while True:
        tipp = int(input("Enter tip percentage (0/5/10/15/20): "))
        if tipp not in [0, 5, 10, 15, 20]:
            print("Tip itni honi chahiye 0, 5, 10, 15, 20.")
        else:
            break

    tipp_amount = (tipp / 100) * Bill
    total_bill = Bill + tipp_amount
    per_person = total_bill / People

    print("Tip Amount: $", "%.2f" % tipp_amount)
    print("Total Bill : $", "%.2f" % total_bill)
    print("One person pay amount: $", "%.2f" % per_person)

    again = input("Would you like to calculate another bill? (y/n): ")
    if again.lower() != 'y':
        print("THANK YOU FOR USING BILL SPLITTER APP. VISIT AGAIN!")
        break
