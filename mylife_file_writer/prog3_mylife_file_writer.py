import os

class JournalWriter:
    def __init__(self):
        self.folder = "mylife_file_writer"
        self.file_name = os.path.join(self.folder, "mylife.txt")

        # Ensure the folder exists
        os.makedirs(self.folder, exist_ok=True)

    def write_lines(self):
        with open(self.file_name, "a") as file:
            while True:
                line = input("Enter line: ")
                file.write(line + "\n")

                more = input("Are there more lines y/n? ").lower()

                if more == "n":
                    print(f"Lines have been added to {self.file_name}")
                    break

writer = JournalWriter()
writer.write_lines()