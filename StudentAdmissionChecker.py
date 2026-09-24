name = input("Enter your name: ")
sscGpa = float(input("Enter your SSC GPA: "))
hscGpa = float(input("Enter your HSC GPA: "))
admissionScore = float(input("Enter your admission score: "))

isEligible = False

if sscGpa >= 2.50 and hscGpa >= 2.50:
    isEligible = True

    if admissionScore < 50:
        isEligible = False
    else:
        isEligible = True
else:
    isEligible = False

if not isEligible:
    print("Sorry, you are not eligible for the admission. Best of luck next time!")
else:
    print(f"Congratulations! You are eligible for the admission.\nName : {name}\nSSC GPA : {sscGpa:.2f}\nHSC GPA : {hscGpa:.2f}\nAdmission Score : {admissionScore:.2f}")