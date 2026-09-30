#session_08
#3) Text.transactions
b='C://Users//Fatemeh//Desktop//tamrin//transactions.txt'
def calculate_balance(username):
    file=open(b,'r')
    balance=0
    for line in file:
        data=line.strip().split(',')
        user=data[0]
        transaction_type=data[1]
        amount=int(data[2])
        if user==username:
            if transaction_type=='deposite':
                balance+=amount
            elif transaction_type=='withdraw': 
                if amount<=balance:
                    balance-=amount
    file.close()
    return balance
def total_deposits(username):
    file=open(b,'r')
    total=0
    for line in file:
        data=line.strip().split(',')
        user=data[0]
        transaction_type=data[1]
        amount=int(data[2])
        if user==username and transaction_type=='deposite':
            total+=amount
    file.close() 
    return total
def total_withdrawals(username):
     file=open(b,'r')
     total=0
     for line in file:
         data=line.strip().split(',')
         user=data[0]
         transaction_type=data[1]
         amount=int(data[2])
         if user==username and transaction_type=='withdraw':
             total+=amount
     file.close() 
     return total   

def find_invalid_transactions(username):
    file=open(b,'r')
    balance=0
    invalid_transactions=[]
    for line in file:
        data=line.strip().split(',')
        user=data[0]
        transaction_type=data[1]
        amount=int(data[2])
        if user==username:
            if transaction_type=='deposite':
                balance+=amount
            elif transaction_type=='withdraw': 
                if amount> balance:
                    invalid_transactions.append(line.strip())
                else:    
                    balance-=amount
    file.close()
    return invalid_transactions
def generate_report():
        file=open(b,'r')
        users=[]
        for line in file:
            data=line.strip().split(',')
            username=data[0]
            if username not in users:
                users.append(username)
        file.close()
        print('Final Report')
        for username in users:
            deposits=total_deposits(username)
            withdrawals=total_withdrawals(username)
            balance=calculate_balance(username)
            invalid_transactions=find_invalid_transactions(username)
            print('Name:',username)
            print('Total deposits:',deposits)
            print('Total withdrawals:',withdrawals)
            print('Balance:',balance)
            print('Invalid transactions:')
            if len(invalid_transactions)==0:
                print('None')
            else:
                for transaction in invalid_transactions:
                    print(transaction)
generate_report()            
                            