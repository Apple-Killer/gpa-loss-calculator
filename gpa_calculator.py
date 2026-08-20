print("welcome to REVERSED GPA calculator")
Terms_Num = int(input("How many terms ?"))
Terms_And_Subject_Scores = {}
Terms_GPA_Losses = []
Total_GPA_Loss = []

for i in range (1 , Terms_Num + 1) :
    Terms_And_Subject_Scores[i] = []
    credits_Of_Term = float(input(f"Let's check term {i} , How many credits do we have ?"))

    Subjet_Num = int(input("Well , How many subjet are we gonna check in this term ?"))

    for j in range (1 , Subjet_Num + 1) :
        Subjet_Score = float(input(f"Enter score loss of subject {j} in term {i} :"))
        Terms_And_Subject_Scores[i].append(Subjet_Score)
        Subject_credit = float(input("Now enter the credit of this subject :"))
        Terms_And_Subject_Scores[i].append(Subject_credit)

    Terms_And_Subject_Scores[i].append(credits_Of_Term)

for i in range (1 , len(Terms_And_Subject_Scores) + 1) :

    term_Data = Terms_And_Subject_Scores[i]
    Score_To_Semester = 0

    for j in range(0 , len(Terms_And_Subject_Scores[i]) -1 , 2):

        Score_To_Semester +=  term_Data[j] * term_Data[j + 1]


    GPA_In_Term = Score_To_Semester/term_Data[-1]
    Terms_GPA_Losses.append(GPA_In_Term)
    Terms_GPA_Losses.append(term_Data[-1])
    print(f"You have {GPA_In_Term:.2f} GPA loss in term {i} till now , it mean you're {20 - GPA_In_Term:.2f} now")
        

for i in range(0 , len(Terms_GPA_Losses), 2):
    Semester_To_GPA = Terms_GPA_Losses[i] * Terms_GPA_Losses[i+1]
    Total_GPA_Loss.append(Semester_To_GPA)

Sum_Semester = 0

for i in range(1 , len(Terms_GPA_Losses), 2):
    Sum_Semester += Terms_GPA_Losses[i]


Total_GPA = sum(Total_GPA_Loss) / Sum_Semester
print(f"You totally have {Total_GPA:.2f} loss in your GPA and you're now {20 - Total_GPA:.2f}")
