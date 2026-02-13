student_name = "Jermaine"
current_gpa = 3.6
study_hours = 10
social_points = 30
stress_level = 50

# ========================================
# Decision 1: Course Load Selection
# ========================================

print("\nCourse Load Options:")
print("A - Light Load")
print("B - Standard Load")
print("C - Heavy Load")

choice = input("Choose your course load (A, B, or C): ")

# Check which option the user selected
if choice == "A":
    study_hours += 5
    stress_level -= 10
    social_points += 5
    print("You chose a Light Load.")

elif choice == "B":
    study_hours += 10
    stress_level += 5
    print("You chose a Standard Load.")

elif choice == "C":
    study_hours += 20

    # Heavy load affects students differently based on GPA
    if current_gpa >= 3.0:
        stress_level += 15
    else:
        stress_level += 30  # Lower GPA = more stress

    print("You chose a Heavy Load.")

else:
    print("Invalid choice. No changes made.")

# ========================================
# Decision 2: Study Strategy
# ========================================

print("\nStudy Strategy Options:")
print("A - Group Study")
print("B - Solo Study")
print("C - Balanced Study")

study_options = ["A", "B", "C"]

choice2 = input("Choose your study strategy (A, B, or C): ")

# Validate input using membership operator
if choice2 not in study_options:
    print("Invalid choice. No changes made.")

else:

    # Group Study
    if choice2 == "A":
        current_gpa += 0.2
        social_points += 10
        stress_level -= 5
        print("You chose Group Study.")

    # Solo Study
    elif choice2 == "B":
        current_gpa += 0.4
        social_points -= 5
        stress_level += 10
        print("You chose Solo Study.")

    # Balanced Study
    elif choice2 == "C":
        current_gpa += 0.3
        social_points += 5
        stress_level += 2
        print("You chose Balanced Study.")

    # Logical operator example
    # If stress is high AND study hours are high, GPA suffers
    if stress_level > 70 and study_hours > 20:
        current_gpa -= 0.3
        print("High stress and heavy workload lowered your GPA.")

    # Another logical example
    if social_points < 10 or stress_level > 80:
        print("Warning: Your balance is unhealthy.")

# ========================================
# Final Semester Assessment
# ========================================

print("\nFinal Semester Results")
print("GPA:", current_gpa)
print("Study Hours:", study_hours)
print("Social Points:", social_points)
print("Stress Level:", stress_level)

# Identity operator example
if type(current_gpa) is float:
    print("GPA is stored correctly as a float.")
else:
    print("Error: GPA is not stored as a float.")

# Nested conditionals for multiple endings
if current_gpa >= 3.8:
    if stress_level < 60:
        print("Ending: Dean's List and Balanced Life!")
    else:
        print("Ending: Dean's List but Extremely Stressed!")

elif current_gpa >= 3.0:
    if social_points > 40:
        print("Ending: Strong Student with Active Social Life!")
    else:
        print("Ending: Academically Stable but Socially Isolated.")

else:
    print("Ending: Academic Probation. Time to Improve Next Semester.")
