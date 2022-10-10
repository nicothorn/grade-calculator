readyForGrade = False
currentStep = 1
currentAssignmentNumber = 1
earnedPointsList = []
maxPointsList = []
weightsList = []

def yes_or_no():
  print("Please enter yes or no.")

def pos_num():
  print("Please enter a positive number.")

while (readyForGrade == False):

  if (currentStep == 1):
    earnedPoints = input("Enter the number of points earned on assignment #{}: ".format(currentAssignmentNumber))
    try:
      if (float(earnedPoints) > 0):
        earnedPointsList.append(float(earnedPoints))
        currentStep = 2
      else:
        pos_num()
        continue
    except ValueError:
      pos_num()
      continue

  if (currentStep == 2):
    maxPoints = input("Enter the maximum total points possible for assignment #{}: ".format(currentAssignmentNumber))
    try:
      if (float(maxPoints) > 0):
        maxPointsList.append(float(maxPoints))
        currentStep = 3
      else:
        pos_num()
        continue
    except ValueError:
      pos_num()
      continue

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
        continue
    except ValueError:
      yes_or_no()
      continue
  if (currentStep == 4):
    weight = input("How much is assignment #{} weighted by? (Example: If it is weighted 2.5 times more than other assignments, enter 2.5.): ".format(currentAssignmentNumber))
    try:
      if (float(weight) > 0):
        weightsList.append(float(weight))
        currentStep = 5
      else:
        pos_num()
        continue
    except ValueError:
      pos_num()
      continue

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
        continue
    except ValueError:
      yes_or_no()
      continue

earnedPointsTotal = []
maxPointsTotal = []

if len(earnedPointsList) > 1:
  for i in range(len(earnedPointsList)):
    earnedPointsCalc = earnedPointsList[i] * weightsList[i]
    earnedPointsTotal.append(earnedPointsCalc)
    maxPointsCalc = maxPointsList[i] * weightsList[i]
    maxPointsTotal.append(maxPointsCalc)

else:
  earnedPointsTotal.append(earnedPointsList[0] * weightsList[0])
  maxPointsTotal.append(maxPointsList[0] * weightsList[0])

currentGrade = sum(earnedPointsTotal) / sum(maxPointsTotal)

print("----------")

if (currentGrade >= 0.7):
  print("Your current grade is {:.1%}. You're passing!".format(currentGrade))
else:
  print("Your current grade is {:.1%}. You're failing. :(".format(currentGrade))