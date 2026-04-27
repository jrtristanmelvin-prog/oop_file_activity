class StudentGwa:
    def __init__(self):
        self.file_name = "highest_gwa_result/students.txt"

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

            print("Student with highest GWA:")
            print(highest_name, "-", highest_gwa)

        except FileNotFoundError:
            print("students.txt file not found.")

obj = StudentGwa()
obj.highest_gwa()
