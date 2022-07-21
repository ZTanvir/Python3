class LunchCard:
    def __init__(self, balance: float):
        self.balance = balance

    def eat_lunch(self):
        remaining_balance = self.balance - 2.60
        if remaining_balance < 0:
            pass
        elif remaining_balance >= 0:
            self.balance = remaining_balance

    def eat_special(self):
        remaining_balance = self.balance - 4.60
        if remaining_balance < 0:
            pass
        self.balance = remaining_balance

    def deposit_money(self, ammount: int):
        if ammount < 0:
            raise ValueError(
                "You cannot deposit an amount of money less than zero")
        elif ammount >= 0:
            self.balance += ammount

    def __str__(self) -> str:
        return f"The balance is {self.balance:.1f} euros"


peters_card = LunchCard(20)
graces_card = LunchCard(30)

peters_card.eat_special()
graces_card.eat_lunch()
print("Peter:", peters_card)
print("Grace:", graces_card)

peters_card.deposit_money(20)
graces_card.eat_special()
print("Peter:", peters_card)
print("Grace:", graces_card)

peters_card.eat_lunch()
peters_card.eat_lunch()
graces_card.deposit_money(50)
print("Peter:", peters_card)
print("Grace:", graces_card)
