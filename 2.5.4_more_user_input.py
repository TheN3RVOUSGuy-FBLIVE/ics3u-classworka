print("""Please type in your information\n
Enter your: \n""")

fname = input("First name:\n")
lname = input("Last name:\n")
grade = int(input("Grade:\n"))
student_id = int(input("Student ID:\n"))
login = input("Login:\n")
average = float(input("Average\n"))

print(f"""Your information:
{"Login:":>30}{login:>10}
{"ID:":>30}{student_id:>10}
{"Name:":>30}{lname + " " + fname:>10}
{"Average:":>30}{average:>10}
{"Grade:":>30}{grade:>10}""")