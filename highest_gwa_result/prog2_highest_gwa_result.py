class StudentGWA:
    def __init__(self):
        self.file_name = "students.txt"

    def highest_gwa(self):
        try:
            with open(self.file_name, "r") as file:
                students = file.readlines()