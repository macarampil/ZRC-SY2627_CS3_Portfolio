class AssignmentSubmission:
    def __init__(self, student_name, student_id, assignment_title, due_date):
        self.student_name = student_name
        self.student_id = student_id
        self._assignment_title = assignment_title
        self._due_date = due_date
        self.__submitted_files = []
      

    def __validate_grade(self, score):
        if score >= 0 and score <= 100:
            return True
        return False



    def __check_submission_status(self):
        if self.__is_submitted == True:
           return True
        else:
            return False


    def __is_duplicate(self, filename):
        if filename in self.__submitted_files:
            print(f"[Warning] '{filename}' is already attached")
            return True 
        return False


    def add_file(self, filename):
        if not self.__is_duplicate(filename):
            self.__submitted_files.append(filename)
            self.__is_submitted = True
            print(f"[Success] {self.student_name} attached '{filename}'. Total files {len(self.__submitted_files)}")
        else:
            print(f"[Warning] '{filename}' is already attached")

    def remove_file(self, filename):
        if filename in self.__submitted_files:
            self.__submitted_files.remove(filename)
            print(f"[Success] {self.student_name} removed '{filename}'")
        else:
            print(f"[Error] File '{filename}' not found in the submission list for {self.student_name}.")

    def assign_grade(self, score):
        
            grade = score 
            print(f"[Success] Grade {grade} assigned to {self.student_name}.")
        
        
        #  print(f"[Error] Invalid grade {score}. Grade must be between 0 and 100.")

    def get_grade(self):
        pass

    def view_files(self):
        if not self.__submitted_files:
            print(f"[Error] No files submitted by {self.student_name}.")
            return []
        return self.__submitted_files

    def get_status_report(self):
        return {
            "ID": self.student_id,
            "Name": self.student_name,
            "Status": f"Submitted {len(self.__submitted_files)} file(s)" if self.__is_submitted else "Missing",
            "Grade": {self.assign_grade}_grade() is not None else "Not graded"
        }


student1 = AssignmentSubmission("Alex Gonzaga", "pshs-1090-x", "CS-101", "2026-10-01")
student2 = AssignmentSubmission("Adelle", "pshs-1920-x", "CS-103", "2026-10-01")
student3 = AssignmentSubmission("Aytr", "pshs-1980-x", "CS-106", "2026-10-01")
student4 = AssignmentSubmission("Elie", "pshs-1989-x", "CS-107", "2026-10-01")
student5 = AssignmentSubmission("Ronald", "pshs-5620-x", "CS-103", "2026-10-01")


print("---INITIALIZING DROPBOX FOR STUDENTS ----")
student1 = AssignmentSubmission(student_name="Alex Gonzaga", student_id="pshs-1090-x", assignment_title="CS-101", due_date="2026-10-01")
student2 = AssignmentSubmission(student_name="Adelle", student_id="pshs-1920-x", assignment_title="CS-103", due_date="2026-10-01")
student3 = AssignmentSubmission(student_name="Aytr", student_id="pshs-1980-x", assignment_title="CS-106", due_date="2026-10-01")
student4 = AssignmentSubmission(student_name="Elie", student_id="pshs-1989-x", assignment_title="CS-107", due_date="2026-10-01")
student5 = AssignmentSubmission(student_name="Ronald", student_id="pshs-5620-x", assignment_title="CS-103", due_date="2026-10-01")
print()

print("--- TEST SCENARIO 1: Multiple Files via List ---")
student1.add_file("main.py")
student1.add_file("report.pdf")
student1.assign_grade(95)
print(f"Alex's Files: {student1.view_files()}\n")

print("--- TEST SCENARIO 2: Removing Files from List ---")
student2.add_file("wrong_homework.docx")
student2.remove_file("wrong_homework.docx")
student2.add_file("correct_project.py")
student2.assign_grade(88)
print(f"Adelle's Files: {student2.view_files()}\n")

print("--- TEST SCENARIO 3: Preventing Duplicate Files ---")
student3.add_file("script.py")
student3.add_file("script.py")
print(f"Aytr's Files: {student3.view_files()}\n")

print("--- TEST SCENARIO 4: Removing file after being graded ---")
student4.add_file("exam_answers.pdf")
student4.assign_grade(75)
student4.remove_file("exam_answers.pdf")
print()

print("--- TEST SCENARIO 5: Empty List Handling ---")
student5.add_file("draft.txt")
student5.remove_file("draft.txt")
student5.assign_grade(100)
print()

print("--- FINAL STATUS REPORTS ---")
print(student1.get_status_report())
print(student2.get_status_report())
print(student3.get_status_report())
print(student4.get_status_report())
print(student5.get_status_report())