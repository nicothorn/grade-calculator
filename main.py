# This program takes user input of assignment/exam grades, including
# weighted grades, and outputs the user's current grade and whether they # are passing or failing.

# Initialize
readyForGrade = False
currentStep = 1
currentAssignmentNumber = 1
earnedPointsList = []
maxPointsList = []
weightsList = []


# Functions for printing repeated error messages
def yes_or_no():
  print("Please enter yes or no.")


def pos_num():
  print("Please enter a positive number or zero.")


# Point of entry for the user to enter assignment grades; loop until user
# is done entering their grades
while (readyForGrade == False):

  # Prompt user to enter points earned for assignment
  if (currentStep == 1):
    earnedPoints = input(
      "Enter the number of points earned on assignment #{}: ".format(
        currentAssignmentNumber))
    # Check if input is a valid positive number
    try:
      # Check if input is a number greater than 0.
      if (float(earnedPoints) >= 0):
        earnedPointsList.append(float(earnedPoints))
        currentStep = 2
      else:
        pos_num()
    except ValueError:
      pos_num()

  # Prompt user to enter maximum total points
  if (currentStep == 2):
    maxPoints = input(
      "Enter the maximum total points possible for assignment #{}: ".format(
        currentAssignmentNumber))
    # Check if input is a valid positive number
    try:
      if (float(maxPoints) >= 0):
        maxPointsList.append(float(maxPoints))
        currentStep = 3
      else:
        pos_num()
    except ValueError:
      pos_num()

  # Prompt user whether assignment is weighted
  if (currentStep == 3):
    # Check if input was yes or no
    try:
      isWeighted = input("Is the grade for assignment #{} weighted? ".format(
        currentAssignmentNumber))
      # Check if answer is "no"
      if (isWeighted.lower().strip() == "no"):
        weight = 1
        weightsList.append(float(weight))
        currentStep = 5
      # Check if answer is "yes"
      elif (isWeighted.lower().strip() == "yes"):
        currentStep = 4
      else:
        yes_or_no()
    except ValueError:
      yes_or_no()

  # Prompt user how much assignment is weighted by
  if (currentStep == 4):
    weight = input(
      "How much is assignment #{} weighted by? (Example: If it is weighted 2.5 times more than other assignments, enter 2.5.): "
      .format(currentAssignmentNumber))
    # Check if input is a valid positive number
    try:
      if (float(weight) > 0):
        weightsList.append(float(weight))
        currentStep = 5
      else:
        print("Please enter a positive number.")
    except ValueError:
      print("Please enter a positive number.")

  # Prompt user if they want to add another assignment grade. If yes,
  # loop back to beginning of while loop. If not, move onto grading.
  if (currentStep == 5):
    addAnotherAssignment = input("Do you want to input another assignment? ")
    # Check if user needs to input more assignments
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

# Function to calculate and display current grade
def get_current_grade():
  # Calculate current grade in decimal format
  currentGrade = sum(earnedPointsTotal) / sum(maxPointsTotal)
  print("----------")
  # Display final result as a percentage and determine if the user is
  # passing
  if (currentGrade >= 0.7):
    print("Your current grade is {:.1%}. You're passing!".format(currentGrade))
  else:
    print(
      "Your current grade is {:.1%}. You're failing. :(".format(currentGrade))


# Print error if max points input is 0 because cannot divide by 0
if sum(maxPointsList) == 0:
  print(
    "Cannot calculate current grade if maximum total points entered is zero for all assignments. Please restart program and input valid maximum points."
  )

# Calculate points if user input more than one assignment
elif len(earnedPointsList) > 1:
  # Calculate weighted points and add them to the appropriate list
  for i in range(len(earnedPointsList)):
    earnedPointsCalc = earnedPointsList[i] * weightsList[i]
    earnedPointsTotal.append(earnedPointsCalc)
    maxPointsCalc = maxPointsList[i] * weightsList[i]
    maxPointsTotal.append(maxPointsCalc)
  get_current_grade()

# Calculate points if user only input one assignment
else:
  earnedPointsTotal.append(earnedPointsList[0] * weightsList[0])
  maxPointsTotal.append(maxPointsList[0] * weightsList[0])
  get_current_grade()
