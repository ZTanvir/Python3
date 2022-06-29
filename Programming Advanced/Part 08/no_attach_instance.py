class BonusCard:
    def __init__(self, name: str, balance: float):
        self.name = name
        self.balance = balance

    def add_bonus(self):
        bonus = self.balance * 0.25
        self.balance += bonus

    def super_bonus(self):
        super_bonus = self.balance * 0.5
        self.balance += super_bonus

    def __str__(self):
        return f"BonusCard(name={self.name},balance={self.balance})"


rohim_account = BonusCard("Rohim", 100)
print(rohim_account.name)
print(rohim_account.balance)
print(rohim_account.super_bonus())
print(rohim_account.balance)
print(rohim_account.add_bonus())
print(rohim_account)

