# This program takes user input of assignment/exam grades, including weighted 
# grades, and outputs the user's current grade and whether they are passing or 
# failing.

# Initialize
readyForGrade = False
currentStep = 1
currentAssignmentNumber = 1
earnedPointsList = []
maxPointsList = []
weightsList = []

# Functions to print error messages used throughout.
def yes_or_no():
  print("Please enter yes or no. ")

def pos_num():
  print("Please enter a positive number. ")

# While loop that's the point of entry
while (readyForGrade == False):

# User enters points they earned
  if (currentStep == 1):
    earnedPoints = input("Enter the number of points earned on assignment #{}: ".format(currentAssignmentNumber))
    try:
      if (float(earnedPoints) > 0):
        earnedPointsList.append(float(earnedPoints))
        currentStep = 2
      else:
        pos_num()
    except ValueError:
      pos_num()

# User enters maximum total points
  if (currentStep == 2):
    maxPoints = input("Enter the maximum total points possible for assignment #{}: ".format(currentAssignmentNumber))
    try:
      if (float(maxPoints) > 0):
        maxPointsList.append(float(maxPoints))
        currentStep = 3
      else:
        pos_num()
    except ValueError:
      pos_num()

# User indicates whether assignment is weighted; if yes, goes to step 4. If not,
# skips step 4.
  if (currentStep == 3):
    try:
      isWeighted = input("Is the grade for assignment #{} weighted? ".format(currentAssignmentNumber))
      if (isWeighted.lower().strip() == "no"):
        weight = 1
        weightsList.append(float(weight))
        currentStep = 5
      elif (isWeighted.lower().strip() == "yes"):
        currentStep = 4
      else:
        yes_or_no()
    except ValueError:
      yes_or_no()
  
  # User inputs how much assignment is weighted by.
  if (currentStep == 4):
    weight = input("How much is assignment #{} weighted by? (Example: If it is weighted 2.5 times more than other assignments, enter 2.5.): ".format(currentAssignmentNumber))
    try:
      if (float(weight) > 0):
        weightsList.append(float(weight))
        currentStep = 5
      else:
        pos_num()
    except ValueError:
      pos_num()

# Asks if user wants to add another assignment grade. If yes, loops back to 
# beginning of while loop. If not, moves onto grading.
  if (currentStep == 5):
    addAnotherAssignment = input("Do you want to input another assignment? ")
    try:
      if (addAnotherAssignment.lower().strip() == "yes"):
        currentAssignmentNumber += 1
        currentStep = 1
      elif (addAnotherAssignment.lower().strip() == "no"):
        readyForGrade = True
      else:
        yes_or_no()
    except ValueError:
      yes_or_no()

# Initialize for grading calculations
earnedPointsTotal = []
maxPointsTotal = []

# Calculates points if user input more than one assignment
if len(earnedPointsList) > 1:
  for i in range(len(earnedPointsList)):
    earnedPointsCalc = earnedPointsList[i] * weightsList[i]
    earnedPointsTotal.append(earnedPointsCalc)
    maxPointsCalc = maxPointsList[i] * weightsList[i]
    maxPointsTotal.append(maxPointsCalc)

# Calculates points if user only input one assignment
else:
  earnedPointsTotal.append(earnedPointsList[0] * weightsList[0])
  maxPointsTotal.append(maxPointsList[0] * weightsList[0])

# Calculates current grade
currentGrade = sum(earnedPointsTotal) / sum(maxPointsTotal)
print("----------")

# Final result: the user's current grade
if (currentGrade >= 0.7):
  print("Your current grade is {:.1%}. You're passing!".format(currentGrade))
else:
  print("Your current grade is {:.1%}. You're failing. :(".format(currentGrade))