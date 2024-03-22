class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.balance = 0.0
    
    def __repr__(self) -> str:
        header = self.name.center(30, "*") + "\n"
        ledger = ""
        for item in self.ledger:
            line_description = "{:<23}".format(item["description"])
            line_amount = "{:>7.2f}".format(item["amount"])
            ledger += "{0}{1}\n".format(line_description[:23], line_amount[:7])
        total = "Total: {:.2f}".format(self.balance)
        return header + ledger + total
    
    def check_funds(self, amount):
        if amount > self.balance:
            return False
        else:
            return True

    def deposit(self, amount, desc=""):
        self.ledger.append({"amount": amount, "description": desc})
        self.balance += amount

    def withdraw(self, amount, desc=""):
        ## need to add if balance less
        if not self.check_funds:
            return False
        else:
            self.ledger.append({"amount": -amount, "description": desc})
            self.balance -= amount
            return True

    def get_balance(self):
        return self.balance 
    
    def transfer(self, amount, category):
        if not self.check_funds:
            return False
        else:
            self.widthdraw(amount, f"Transfer to {category.name}")
            self.deposit(amount, f"Transfer from {self.name}")
            return True
    

def create_spend_chart(categories):
    spent_dict = {}
    for item in categories:
        spent = 0 
        for transaction in item.ledger:
            if transaction["amount"] < 0:
                spent += abs(transaction["amount"])
        spent_dict[item.name] = round(spent,2)
    total = sum(spent_dict.values())
    percent_dict = {}

    for transaction in spent_dict.keys():
        percent_dict[transaction] = int(round(spent_dict[transaction]/total,2)*100)
    result = 'Percentage spent by category\n'

    for i in range(100,-10,-10):
        result += f'{i}'.rjust(3) + '| '
        for percent in percent_dict.values():
            if percent >= i:
                result+= 'o  '
            else:
                result+= '   '
            result += '\n' 

    result += ' '*4+'-'*(len(percent_dict.values())*3+1)
    result += '\n     '

    dict_key_list = list(percent_dict.keys())
    max_len_category = max([len(i) for i in dict_key_list])
   
    for i in range(max_len_category):    
        for name in dict_key_list:
            if len(name)>i:
                result+= name[i] +'  '
            else:
                result+= '   '
            if i < max_len_category-1:
                result+='\n     '
    
    return result


