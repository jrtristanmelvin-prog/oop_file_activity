class number_separator:
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

