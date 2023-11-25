#CalcuSync
#Created by Aidan Chen 
#Github - CalcuSync
#Divider---------------------------------------------------------------------------------------------------------

#MIT License

#Copyright (c) 2023 Aidan Chen

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#SOFTWARE.

#Divider---------------------------------------------------------------------------------------------------------

#Modules needed
import math

#Divider------------------------------------------------------------------------------------------------------
def Introduction():
#Intro
    print("* ========================================================================================================== *")
    print("* CalcuSync is created by Aidan.                                                                             *")                                   
    print("* Welcome to the CalcuSync. Press the key you will need to complete your calculation.                        *")
    print("* Everything is listed in alphabetical order.                                                                *")
    print("* Press 'I' for information on each calculation or if you are unsure of what a calculation does.             *")
    print("* Press 'H' for help.                                                                                        *")
    print("*                                                                                                            *")
    print("* ↓↓↓ List of commands ↓↓↓                                                                                   *") 
    print("*                                                                                                            *")                                
    print("* Key: a - Addition                                                                                          *")
    print("* Key: c - Cube Root                                                                                         *")
    print("* Key: d - Division                                                                                          *")
    print("* Key: ds - Distance 2D                                                                                      *")
    print("* Key: ds3 - Distance 3D                                                                                     *")
    print("* Key: e - Exponent                                                                                          *")
    print("* Key: h - Hypotenuse                                                                                        *")
    print("* Key: md - Midpoint 2D                                                                                      *")
    print("* Key: m - Multiplication                                                                                    *")
    print("* Key: sl - Slope                                                                                            *")
    print("* Key: sq - Square Root                                                                                      *")
    print("* Key: s - Subtraction                                                                                       *")
    print("* ========================================================================================================== *")
#Divider---------------------------------------------------------------------------------------------------------
def Information(calcType):
#Information on the calculations
    if calcType == "I":
        print()
        print("↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓")
        print("The following are what each calculation does as well as what happens when you select each calculation.")
        print("-----------------------------------------------------------------------------------------------------------------------")
        print("Addition - Lets you input 2 numbers. Adds 2 numbers. Example: 3 + 7.9 = 10.9 (x + y = z)")
        print("-----------------------------------------------------------------------------------------------------------------------")
        print("Division - Lets you input 2 numbers. Divides 2 numbers. Example: 9 ÷ 2 = 4.5 (x ÷ y = z)")
        print("-----------------------------------------------------------------------------------------------------------------------")
        print("Distance 2D - Lets you input 2 coordinate points (x₁,y₁) (x₂,y₂). Finds the distance between the points.")
        print("Example: √((3 - 4)² + (-1 - 9)²) ≈ 10.05 (√((x₂ - x₁)² + (y₂ - y₁)²))")
        print("-----------------------------------------------------------------------------------------------------------------------")
        print("Distance 3D - Lets you input 2 coordinate points (x₁,y₁,z₁) (x₂,y₂,c₂). Finds the distance between the points.")
        print("Example: √((9.9 - 2)² + (345 - 923.3)² + (23 - 98)²) ≈ 583.2 (√((x₂ - x₁)² + (y₂ - y₁)² + (z₂ - z₁)))")
        print("-----------------------------------------------------------------------------------------------------------------------")
        print("Exponent - Lets you input a base number and then input an exponent. Example: 3³ = 27 (xⁿ = y)")
        print("-----------------------------------------------------------------------------------------------------------------------")
        print("Hypotenuse - Lets you input 2 numbers ( Length of each side of the right triangle). Find the hypotenuse.")
        print("Example: 3² + 7² = √58 or ≈ 7.616² (a² + b² = c²)")
        print("-----------------------------------------------------------------------------------------------------------------------")
        print("Midpoint 2D - Lets you input 2 coordinate points (x₁,y₁) (x₂,y₂). Finds the midpoint between the points.")
        print("Example: (4.5 + 16) / 2 = 10.25 | (71 + 38) / 2 = 54.5 | Answer : (10.25,54.5) (x₁ + x₂) / 2 | (y₁ + y₂) / 2")
        print("-----------------------------------------------------------------------------------------------------------------------")
        print("Multiplication - Lets you input 2 numbers. Multiplies 2 numbers. Example: 2.1 × 6.7 = 14.07 (x × y = z)")
        print("-----------------------------------------------------------------------------------------------------------------------")
        print("Slope - Lets you input 2 coordinate points (x₁,y₁) (x₂,y₂). Finds the slope of the 2 points.")
        print("Example: (28 - 93) / (12 - 4) = -8.125 (y₂ - y₁ / x₂ - x₁)")
        print("-----------------------------------------------------------------------------------------------------------------------")
        print("Square Root - Lets you input 1 number. Finds the square root of a number. Example: √9 = 3 (√x = y)")
        print("-----------------------------------------------------------------------------------------------------------------------")
        print("Subtraction - Lets you input 2 numbers. Subtracts 2 numbers. Example: 10 - 4.4 = 5.6 (x - y = z)")
        print("-----------------------------------------------------------------------------------------------------------------------")
        print("-----------------------------------------------------------------------------------------------------------------------")
        calcType = input("Press the key needed to complete your calculation.")
        print()
#Divider---------------------------------------------------------------------------------------------------------
def Help(calcType):
#Help
    if calcType == "H":
        print()
        print("-----------------------------------------------------------------------------------------------------------------------")
        print("Press 'Enter' or click the 'X' on the top right side to exit the program.")
        print("-----------------------------------------------------------------------------------------------------------------------")
        print("-----------------------------------------------------------------------------------------------------------------------")
        calcType = input("Press the key needed to complete your calculation.")
        print("-----------------------------------------------------------------------------------------------------------------------")
        print()
#Divider---------------------------------------------------------------------------------------------------------
def Addition(calcType):
#Addition
    if calcType == "a":
        print("You selected the Addition calculation.")
        number1=input("Type in the first number.")
        number2=input("Type in the second number.")
    
        answer1=float(number1)+float(number2)
        print("Your answer is "+str(answer1)+".")
        reader=input("Press Enter to close.")
#Divider---------------------------------------------------------------------------------------------------------
def Division(calcType):
#Division
    if calcType == "d":
        print("You selected the Division calculation.")
        number7=input("Type the number you want to divide from.")
        number8=input("Type in the amount divided.")
        answer4=float(number7)/float(number8)
        print("Your answer is "+str(answer4)+".")
        reader=input("Press Enter to close.")
#Divider---------------------------------------------------------------------------------------------------------
def Subtraction(calcType):
#Subtraction
    if calcType == "s":
        print("You have selected the Subtraction calculation.")
        number3=input("Type in the number to be subtracted from.")
        number4=input("Type in the amount to subtract.")
        answer2=float(number3)-float(number4)
        print("Your answer is "+str(answer2)+".")
        reader=input("Press Enter to close.")
#Divider---------------------------------------------------------------------------------------------------------
def Multiplication(calcType):
#Multiplication
    if calcType == "m":
        print("You selected the Multiplication calculation.")
        number5=input("Type in the first number.")
        number6=input("Type in the second number.")
        answer3=float(number5)*float(number6)
        print("Your answer is "+str(answer3)+".")
        reader=input("Press Enter to close. ")
#Divider---------------------------------------------------------------------------------------------------------
def Exponent(calcType):
#Exponent
    if calcType == "e":
        print("You have selected the Exponent calculation.")    
        number9=input("Type in the base number.")
        number10=input("Type in the exponent.")
        answer5=float(number9)**float(number10)
        print("Your answer is "+str(answer5)+".")
        reader=input("Press Enter to close.")
#Divider---------------------------------------------------------------------------------------------------------
def Square_Root(calcType):
#Square Root
    if calcType == "sq":
        print("You have selected the Square Root calculation.")
        number11=input("Type in the number you want to find the square root of.")
        answer6=math.sqrt(float(number11))
        print("Your answer is "+str(answer6)+".")
        reader=input("Press Enter to close.")
#Divider---------------------------------------------------------------------------------------------------------
def Cube_Root(calcType):
#Cube Root
    if calcType == "c":
        print("You have selected the Cube Root calculation.")
        number12=input("Type in the number you want to find the cube root of.")
        answer7=float(number12) ** (1 / 3)
        print("The cube root of "+str(number12)+" is " +str(answer7)+".")
        reader=input("Press Enter to close.")
#Divider---------------------------------------------------------------------------------------------------------
def Hypotenuse(calcType):
#Hypotenuse
    if calcType == "h":
        print("You have selected the Hypotenuse calculation.")
        number13=input("Type in the first side length.")
        number14=input("Type in the second side length.")
        answer8=(pow(float(number13), exp=2))+(pow(float(number14), exp=2))
        answer9=math.sqrt(float(answer8))
        print("The length of the third side is "+str(answer9)+".")
        reader=input("Press Enter to close.")
#Divider---------------------------------------------------------------------------------------------------------
def Distance_2D(calcType):
#Distance 2D
    if calcType == "ds":
        print("You have selected the Distance 2D calculation.")
        number15=input("Type in the x coordinate of the first point.")
        number16=input("Type in the y coordinate of the first point.")
        number17=input("Type in the x coordinate of the second point.")
        number18=input("Type in the y coordinate of the second point.")
        answer10=float(float(number17)-float(number15))
        answer11=pow(float(answer10), exp=2)
        answer12=float(float(number18)-float(number16))
        answer13=pow(float(answer12), exp=2)
        answer14=float(answer11)+float(answer13)
        answer15=math.sqrt(float(answer14))
        print("Your distance is "+str(answer15)+".")  
        reader=input("Press Enter to close.")
#Divider---------------------------------------------------------------------------------------------------------
def Slope(calcType):
#Slope
    if calcType == "sl":
        print("You have selected the Slope calculation.")
        number19=input("Type in the x coordinate of the first point.")
        number20=input("Type in the y coordinate of the first point.")
        number21=input("Type in the x coordinate of the second point.")
        number22=input("Type in the y coordinate of the second point.")
        answer16=float(number22)-float(number20)
        answer17=float(number21)-float(number19)
        answer18=float(answer16)/float(answer17)
        print("The slope is "+str(answer18)+".")
        reader=input("Press Enter to close.")
#Divider---------------------------------------------------------------------------------------------------------
def Midpoint(calcType):
#Midpoint
    if calcType == "md":
        print("You have selected the Midpoint 2D calculation.")
        number23=input("Type in the x coordinate of the first point.")
        number24=input("Type in the y coordinate of the first point.")
        number25=input("Type in the x coordinate of the second point.")
        number26=input("Type in the y coordinate of the second point.")
        answer19=(float(number25)+float(number23))/2
        answer20=(float(number26)+float(number24))/2
        print("Your midpoint is "+str(answer19)+","+str(answer20)+".")
        reader=input("Press Enter to close.")
#Divider---------------------------------------------------------------------------------------------------------
def Distance_3D(calcType):
#Distance 3D
    if calcType == "ds3":
        print("You have selected the Distance 3D calculation.")
        number27=input("Type in the x coordinate of the first point.")
        number28=input("Type in the y coordinate of the first point.")
        number29=input("Type in the z coordinate of the first point.")
        number30=input("Type in the x coordinate of the second point.")
        number31=input("Type in the y coordinate of the second point.")
        number32=input("Type in the z coordinate of the second point.")
        answer21=float(float(number30)-float(number27))
        answer22=pow(float(answer21), exp=2)
        answer23=float(float(number31)-float(number28))
        answer24=pow(float(answer23), exp=2)
        answer25=float(float(number32)-float(number29))
        answer26=pow(float(answer25), exp=2)
        answer27=float(answer22)+float(answer24)+float(answer26)
        answer28=math.sqrt(float(answer27))
        print("Your distance is "+str(answer28)+".")  
        reader=input("Press Enter to close.")
#Divider---------------------------------------------------------------------------------------------------------
Introduction()
#Divider---------------------------------------------------------------------------------------------------------
#User Input
calcType = input("Press the key you will need to complete your calculation.")
#Divider---------------------------------------------------------------------------------------------------------

Information(calcType)
Help(calcType)
Addition(calcType)
Subtraction(calcType)
Multiplication(calcType)
Division(calcType)
Exponent(calcType)
Square_Root(calcType)
Cube_Root(calcType)
Hypotenuse(calcType)
Distance_2D(calcType)
Slope(calcType)
Midpoint(calcType)
Distance_3D(calcType)