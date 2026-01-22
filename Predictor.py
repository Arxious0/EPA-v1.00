# I am going to document and comment this code for my own learning
# This will be a Grade Predictor / Smart Learning Project that may make use
# of machine learning at later stages, It will be documented thoroughly.

# Create a function, return_predicted() that takes two parameters. 
# raw_marks, as a list where each element is a past paper of the same subject
# boundaries, where each a grade corresponds to a mark threshold as a dictionary.
# 

# Now I will create the test data.

studentScores = [103,104,105,106,109,100]
subjectBoundaries = {
    'A': 131,
    'B': 103,
    'C': 93,
    'D': 78,
    'E': 69,
    'U': 0
}

# Now to create the function
def return_predicted(raw_marks, boundaries):
    # Start with a simple mean average
    average = sum(studentScores) / len(studentScores)
    grade = None
    for key,value in subjectBoundaries.items():
        if average >= value:
            grade = key
            break
    return grade, average

# The next subroutine should take some data. To figure out where they went wrong.'
# In order to do this, there must be a mark breakdown, that is represented within a specific format.
# In the future, I plan to make a GUI that lets you input these directly without any hassle, But the overall structure of the paper must be recognized.
# For now, I plan to incorporate the edexcel mathematics papers, just as a tool for myself to predict my next grades.
# I also plan to make notable additions, for example, If you did badly in applied, and have now mastered it for the next exam,
# The algorithm will take it into account.

# For this, I plan to use some object oriented techniques.

class ExamPaper:
    def __init__(self, Questions: list[Question]): # Questions will be a list where elements will be of the object type "Question" ordered alphabetically.
        pass

class Question:
    def __init__(self, numberHeader: int, TopicHeader: str, IsMultiPart: bool, TotalMarks):
        pass

        

predictedGrade, average = return_predicted(studentScores, subjectBoundaries)
print(predictedGrade, average)



