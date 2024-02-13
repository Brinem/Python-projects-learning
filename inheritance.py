class Mpesa:
    def __init__(self, account_balance, phone_number):
        self.account_balance = account_balance
        self.phone_number = phone_number

    def send_money(self, amount, recipients):
        if self.account_balance >= amount:
            self.account_balance -= amount
            print(f"{amount} KES has been deposited to {recipients}")
        else:
            print(f"Insufficient Amount to send to {recipients}")


class PersonalMpesa(Mpesa):
    def __init__(self, account_balance, phone_number, id_no):
        super().__init__(account_balance, phone_number)
        self.id_no = id_no

    def buy_airtime(self, amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
            print(f"{amount} KES airtime bought successful")


class BusinessMpesa(Mpesa):
    def __init__(self, account_balance, phone_number, business_name):
        super().__init__(account_balance, phone_number)
        self.business_name = business_name

    def receive_payment(self, amount):
        self.account_balance += amount
        print(f"{amount} KES received from a customer")


# personal
personal_account = PersonalMpesa(2000000, +254702271285, "3456278")
personal_account.send_money(40000, "+254718215685")
personal_account.send_money(40000000, "+254723887879")
personal_account.buy_airtime(2000, )
# business
business = BusinessMpesa(400000, +254702271285, "Motorhub")
business.receive_payment(243553)
business.send_money(236374, "+254718215687")
