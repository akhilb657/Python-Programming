mathsMarks = int(input("Enter Student marks in Maths"))
physicsMarks = int(input("Enter Student marks in Physics"))
chemistryMarks = int(input("Enter Student marks in Chemistry"))

if (mathsMarks >= 35 and physicsMarks >= 35 and chemistryMarks >= 35):
    avg = (mathsMarks + physicsMarks + chemistryMarks) // 3
    if(avg <= 59):
        print("Student got C grade")
    elif(avg <= 69):
        print("Student got B grade")
    else:
        print("Student got A grade")

else:
    print("Student Failed")