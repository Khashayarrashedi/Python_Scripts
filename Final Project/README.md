# **BMI INDEX CALCULATOR**
---
#### Video Demo: [link](https://youtu.be/a2ys34K-p4A)
---
#### Description:
The function of this project is to calculate the **Body Mass Index (BMI)** of the users and show them a graphical view of their BIM range.
As a result it provide them with both qualitative and quantitative expressions.

The code contains 3 functions that each function act as bellow:

1. The first function is ***get_input*** which is responsible of checking the input validity of the input data.
the height and the weight of the user should be an integer numbers. If the user enter incorrect type of input, the application show him a warning and continue asking for the correct input until they input correct type of characters.
It finally returns the name, weight and height of the user to the main section.

2. The second function is to evaluate the BIM_index according to the height and weight entered by the user.
BMI index calculated by deviding weight in kilogram over squared height in meter.
This function finally return the amount of BIM index to 2 decimal places to the main section.

3. the third function named graphical_view, shows different range of numbers and categoraised BIM indexes.
This application shows result in 4 different ranges:
1. ***underweight*** shown in yellow (below 18.5)
2. ***healthy*** weight shown in green (18.5 to 24.9)
3. ***overweight*** shown in yellow (25 to 29.9)
4. ***obese*** shown in red (30 or over)

It also offer user to meet the doctor in case of serious status of Obesity.