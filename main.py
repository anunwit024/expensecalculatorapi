

i=0
Income=0
Expense=0
Summary=0
Listpay=[]
while i < 4:
    print("Main Menu:")
    print("1. Add Transction")
    print("2. View Transction")
    print("3. Summary")
    print("4. Exit")
    Choose=int(input("Choose: "))
    if Choose==1:
        dateValue=str(input("Enter date (YYYY-MM-DD): "))
        typeValue=str(input("Enter type (Income/Expense): "))
        categoryValue=str(input("Enter category: "))
        amountValue=int(input("Enter amount: "))
        descriptionValue=str(input("Enter description (optional): "))
        if typeValue=="Income":
            Summary+=amountValue
            Income+=amountValue
        elif typeValue=="Expense":
            Summary-=amountValue
            Expense+=amountValue
        Listpay.append({
        "Date": dateValue,
        "Type": typeValue,
        "Category": categoryValue,
        "Amount": amountValue,
        "Description": descriptionValue
        })
        print("Transaction added successfully!")
    elif Choose==2:
        print("Transactions: ")
        for t in Listpay:
          print("Date:", t["Date"] ,"| Type: ", t["Type"] ,"| Category: ", t["Category"], "| Amount: ", t["Amount"] ,"| Description: ", t["Description"] )    
    elif Choose==3:
        print("Summary:")
        print("Total Income: ",Income)
        print("Total Expense: ",Expense)
        
        print("Balance: ",Summary)     
    elif Choose==4:   
        break    
    




