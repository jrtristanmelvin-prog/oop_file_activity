class NumberSeparator:
    def __init__(self):
        self.numbers_file = "numbers.txt"
        self.even_file = "even.txt"
        self.odd_file = "odd.txt"

    def separate_numbers(self):
        try:
            with open(self.numbers_file, "r") as file:
                numbers = file.read().split()

            even_numbers = []
            odd_numbers = []

            for num in numbers:
                number = int(num)

                if number % 2 == 0:
                    even_numbers.append(str(number))
                else:
                    odd_numbers.append(str(number))

            even_numbers.sort()
            odd_numbers.sort()

            with open(self.even_file, "w") as even:
                even.write("\n".join(even_numbers))

            with open(self.odd_file, "w") as odd:
                odd.write("\n".join(odd_numbers))

            print("Even numbers saved in even.txt")
            print("Odd numbers saved in odd.txt")

        except FileNotFoundError:
            print("numbers.txt file not found.")
        except ValueError:
            print("numbers.txt contains invalid data.")

obj = NumberSeparator()
obj.separate_numbers()