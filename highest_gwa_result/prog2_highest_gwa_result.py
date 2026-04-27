class StudentGWA:
    def __init__(self):
        self.file_name = "students.txt"

    def highest_gwa(self):
        try:
            with open(self.file_name, "r") as file:
                students = file.readlines()

            highest_name = ""
            highest_gwa = float("inf")

            for student in students:
                name, gwa = student.strip().split(",")
                gwa = float(gwa)

                if gwa < highest_gwa:
                    highest_gwa = gwa
                    highest_name = name