# Terminal Intro Card 
# Focus: print(), input(), comments, indentation, basic syntax, etc


# This is NOT meant to be a "hello world" demo. It's a small, real consoleprogram that renders a styled personal intro card in the terminal.

print("=" * 70)

print("TERMINAL", "INTRO", "CARD", sep=" ! ")

print("=" * 70)

# Personal Information
name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")

# Education
college = input("Enter your college: ")
course = input("Enter your course: ")
year = input("Enter the year of course completion: ")

# Professional Information
career_goal = input("Enter your career goal: ")
skills = input("Enter your main skills: ")
programming_language = input("Enter your favorite programming language: ")

# Projects Information
project = input("Enter your project name/link: ")
project_description = input("Briefly describe your project: ")

# Personal Intrests 
interests = input("Enter your interests/hobbies: ")

# Display Card 

print("\nPERSONAL INFORMATION")
print("-"*70)
print(f"Name                   : {name}")
print(f"Age                    : {age}")
print(f"City                   : {city}")

print("\nEducation")
print("-"*70)
print(f"College                : {college}")
print(f"Course                 : {course}")
print(f"Year of completion     : {year}")

print("\nProfessional Details")
print("-"*70)
print(f"Career Goals           : {career_goal}")
print(f"Skills                 : {skills}")
print(f"Programming Language   : {programming_language}")

print("\nPersonal Interests")
print("-"*70)
print(f"Interests              : {interests}")

print("\nProjects")
print("-"*70)
print(f"Project Name           : {project}")
print(f"Description            : {description}")


print("\n" + "=" * 70)
print("                  THANK YOU FOR INTRODUCING YOURSELF!")
print("=" * 70)
