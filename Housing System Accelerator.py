


# Project: Housing System Accelerator
# Students are awarded a number of points based on specific factors.
# The larger the points a student has, the earlier they get to select their room for next year.


# In my Project, points will be given based on 3 factors : Class Year, GPA, Students with disability


# CLASS YEAR

# variable declaration
point = 0
# Asking for userinput
userInput = input("What class year?: Please reply with freshman, sophomor, junior or senior:")
# If the user inputs freshman, add one point
if (userInput == "freshman") :
    '''
    you do not need to use () when assigning new values to variables.
    '''
    point = (point+1)
# If the user inputs sophomore, add two points
elif (userInput == "sophomore"):
    point = (point+2)
# If the user inputs junior, add three points 
elif (userInput == "junior"):
    point = (point+3)
# If the user inputs senior, add four points
elif (userInput == "senior"):
    point = (point+4)
# If the user inputs anything except those years, nothing will be added
else: 
    point = point
    
#for GPA

# Asking for userinput
userInput = input("What is your GPA ?: Please reply with GPA 4.0, GPA 3.0 or GPA 2.0:")

# If the user inputs less than or equal 2.0,  add one point
if (float(userInput) <= 2.0) :
    point = (point+1)
# If the user less than or equal 3.0, add two points
elif (2.0< float(userInput) <= 3.0):
    point = (point+2)
# If the user inputs GPA 4.0, add four points
elif (3.0< float(userInput) <= 4.0):
    point = (point+4)
# If the user inputs anything except those GPAs, nothing will be added
else: 
    point = (point)
    
# Students with disability

# Asking for userinput
userInput = input("Do you have disability? Please reply with yes or no:")
# If the user inputs yes, add 4 points
if (userInput == "yes"):
    point = (point+4)
# if the user inputs no, add 2 pounts
elif (userInput == "no"):
    point = (point+2)
# if the user inputs anything except yes and no, nothing will be added
else:
    point = (point)
    
# print

print("total points = ",(point))