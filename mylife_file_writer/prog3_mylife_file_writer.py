class JournalWriter:
    def __init__(self):
        self.file_name = "mylife.txt"

        def write_lines(self):
        with open(self.file_name, "a") as file:
            while True:
                line = input("Enter line: ")
                file.write(line + "\n")

                more = input("Are there more lines y/n? ").lower()

                if more == "n":
                    print("Lines have been added to mylife.txt")
                    break