#  function goes here

class Category:

    def __init__(self, name):
        self.name = name
        self.ledger = list()
        self.balance = 0
        self.wdraws = 0

    def deposit(self, amount, description=''):
        self.balance += amount
        self.ledger.append({"amount": amount, "description": description})
        pass

    # - get_balance, current balance based on the withdrawals and deposits
    def get_balance(self):
        avail = 0
        for transactions in self.ledger:
            avail += transactions["amount"]
        return avail

    # - withdraw, similar to deposit, but stored as a negative number
    def withdraw(self, amount, description=''):
        if self.check_funds(amount) is True:
            self.balance -= amount
            self.ledger.append({"amount": -abs(amount), "description": description})
            self.wdraws -= amount
            return True
        return False

    # - transfer, an amount and another budget category
    def transfer(self, amount, destination_budget):
        if self.check_funds(amount) is True:
            self.balance -= amount
            destination_budget.deposit(amount, "Transfer from " + self.name)
            self.ledger.append(({"amount": -abs(amount), "description": "Transfer to " + destination_budget.name}))
            self.wdraws -= amount
            return True
        return False

    # - check_funds, if amount is higher than total balance then False.
    def check_funds(self, amount):
        if amount <= self.balance:
            return True
        return False

    # how the objects are presented when printed
    def __str__(self):
        receipt = ""
        # find number of star needed
        stars = (30 - len(self.name)) / 2

        # convert number of stars to str stars
        stars = '*' * int(stars)

        # for printing the banner
        receipt += f"{stars}{self.name}{stars}\n"

        # formatting output
        for state in self.ledger:
            desc = str(state["description"][:23])
            amt = str("{:.2f}".format(state['amount']))
            receipt += desc + amt.rjust(30 - len(desc), ' ') + "\n"

        receipt += "Total: " + str(self.get_balance())
        return receipt


def create_spend_chart(categories):
    c_amt_name = list()
    c_amt = list()
    avg_per = list()

    # grabbing data from category function and making it workable
    for c in categories:
        c_amt.append(abs(round(c.wdraws)))
        c_amt_name.append(c.name)

    # finding averages of withdraws for graph
    tot_wdraw = sum(c_amt)
    for p in c_amt:
        z = (p / tot_wdraw) * 10
        avg_per.append(int(z) * 10)

    # setting up graph Y axis
    ygraph = list(range(0, 101, 10))
    top_graph = ''
    for v in ygraph[::-1]:
        ynum = str(v).rjust(3) + '|'
        for c in avg_per:
            ores = ''
            if c >= v:
                ores += ' ' + "o" + ' '
            else:
                ores += '   '
            ynum += ores
        if v == 0:
            top_graph += ynum + " "
        else:
            top_graph += ynum + " \n"

    # lazy formatting
    top_graph += "\n"

    # setting up dashes. 3 per item in input category
    xgraph = ''
    xgraph += len(c_amt_name) * '---'
    # dashed line for result
    dash = (f"{xgraph + '-'}".rjust(len(c_amt_name * 3) + 5)) + "\n"

    # name handling
    bot_bar = ''
    counter = 0
    name_max = max(c_amt_name, key=len)
    for n in range(len(name_max)):
        nstring = '    '
        for nom in c_amt_name:  # food clothing auto
            if nom == c_amt_name[-1]:  # if last in list, add an extra space... for formatting...
                if counter < len(nom):
                    for letter in nom[counter]:
                        nstring += ' ' + letter + '  '
                else:
                    nstring += '    '
            elif counter < len(nom):
                for letter in nom[counter]:
                    nstring += ' ' + letter + ' '
            else:
                nstring += '   '

        counter += 1
        #  if longest item name, in list don't make new line when finished making bot_bar
        if counter != len(name_max):
            bot_bar += nstring + '\n'
        else:
            bot_bar += nstring
    return "Percentage spent by category\n" + top_graph + dash + bot_bar


#  extra stuff for testing


#  testing the class

food = Category("Food")
food.deposit(1000, "initial deposit")
food.deposit(10, "2 deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
# print(food.get_balance())
clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

print(food)
print(clothing)

print("\n") # just because it looks nicer :)
#  testing spendchart

# print(create_spend_chart([food, clothing, auto]))

#  replit testing
entertainment = Category("Entertainment")
business = Category("Business")
food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)

print(create_spend_chart([food, business, entertainment]))
