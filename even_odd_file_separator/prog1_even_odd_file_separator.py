import os

class NumberSeparator:
    def __init__(self):
        self.folder = "even_odd_file_separator"
        self.numbers_file = os.path.join(self.folder, "numbers.txt")
        self.even_file = os.path.join(self.folder, "even.txt")
        self.odd_file = os.path.join(self.folder, "odd.txt")

        # Ensure the folder exists
        os.makedirs(self.folder, exist_ok=True)

    def separate_numbers(self):
        try:
            with open(self.numbers_file, "r") as file:
                numbers = file.read().split()

            even_numbers = []
            odd_numbers = []

            for num in numbers:
                number = int(num)
                if number % 2 == 0:
                    even_numbers.append(number)
                else:
                    odd_numbers.append(number)

            even_numbers.sort()
            odd_numbers.sort()

            with open(self.even_file, "w") as even:
                even.write("\n".join(map(str, even_numbers)))

            with open(self.odd_file, "w") as odd:
                odd.write("\n".join(map(str, odd_numbers)))

            print(f"Even numbers saved in {self.even_file}")
            print(f"Odd numbers saved in {self.odd_file}")

        except FileNotFoundError:
            print("numbers.txt file not found.")
        except ValueError:
            print("numbers.txt contains invalid data.")

obj = NumberSeparator()
obj.separate_numbers()