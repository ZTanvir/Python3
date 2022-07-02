# Write your solution here!
class NumberStats:
    def __init__(self):
        self.numbers = 0
        self.count = 0

    def add_number(self, number: int):
        self.count += 1
        self.numbers += number

    def count_numbers(self):
        total_count = self.count
        return total_count

    def get_sum(self):
        if self.numbers == 0:
            return 0
        else:
            return self.numbers

    def average(self):
        try:
            avg = self.numbers / self.count
            return avg
        except ZeroDivisionError:
            print("Can't divide by zero")


# Create three object using NumberStats class
all_numbers_stats = NumberStats()
even_numbers_stats = NumberStats()
odd_numbers_stats = NumberStats()
# Take numbers from user untill number is -1
print("Please type in integer numbers:")
while(True):
    number = int(input(""))
    if number == -1:
        break

    # Get the even number for even and all numbers add number method
    elif number % 2 == 0:
        even_numbers_stats.add_number(number)
        all_numbers_stats.add_number(number)

    # Get the even number for even and all numbers add number method
    elif number % 2 != 0:
        odd_numbers_stats.add_number(number)
        all_numbers_stats.add_number(number)


print("Sum of numbers:", all_numbers_stats.get_sum())
print("Mean of numbers:", all_numbers_stats.average())
print("Sum of even numbers:", even_numbers_stats.get_sum())
print("Sum of odd numbers:", odd_numbers_stats.get_sum())
