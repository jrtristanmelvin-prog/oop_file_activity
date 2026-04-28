class IntegerProcessor:
    def __init__(self):
        self.file_name = "integer_file_processor/integers.txt"
        self.double_file = "double.txt"
        self.triple_file = "triple.txt"

    def read_numbers(self):
        with open(self.file_name, "r") as file:
            return file.read().split()
        
    def process_numbers(self):
        numbers = self.read_numbers()

        even_squares = []
        odd_cubes = []

        for num in numbers:
            n = int(num)

            if n % 2 == 0:
                even_squares.append(str(n ** 2))  # square of even numbers
            else:
                odd_cubes.append(str(n ** 3))     # cube of odd numbers

        return even_squares, odd_cubes
    
    def write_files(self, even_squares, odd_cubes):
        with open(self.double_file, "w") as file:
            file.write("\n".join(even_squares))

        with open(self.triple_file, "w") as file:
            file.write("\n".join(odd_cubes))

    def execute(self):
        try:
            even_squares, odd_cubes = self.process_numbers()
            self.write_files(even_squares, odd_cubes)
            print("Processing complete. Files created successfully.")
        except FileNotFoundError:
            print("Error: integers.txt file not found.")
        except ValueError:
            print("Error: make sure all values in the file are integers.")

processor = IntegerProcessor()
processor.execute()