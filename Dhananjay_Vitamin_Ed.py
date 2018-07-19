# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 11:43:01 2018

@author: Dhananjay Punekar
"""

Age=float(input("Enter the age: "))
factor1 = 1/3
factor2 = 2/3

Vit_C=float(input("Enter the milli-grams/day intake of Vitamin C: "))
if Age >=0 and Age <=1:
    Vit_C_Dev1=27*factor1
    Vit_C_Dev2=27*factor2
    if Vit_C < Vit_C_Dev1:
        color = 'r'
        com_Vit_C = "Vitamin C is severely deficient in the food intake, consider eating more oranges/ guava/ papaya/ strawberry"
    elif Vit_C < Vit_C_Dev2:
        color = 'o'
        com_Vit_C = "Vitamin C is severely deficient in the food intake, consider eating more oranges/ guava/ papaya/ strawberry"
    elif Vit_C >= 27:
        color = 'g'
        com_Vit_C = "Vitamin C is adequate in the food intake"
elif Age >=1 and Age <=6:
    Vit_C_Dev1=30*factor1
    Vit_C_Dev2=30*factor2
    if Vit_C < Vit_C_Dev1:
        color = 'r'
        com_Vit_C = "Vitamin C is severely deficient in the food intake, consider eating more oranges/ guava/ papaya/ strawberry"
    elif Vit_C < Vit_C_Dev2:
        color = 'o'
        com_Vit_C = "Vitamin C is severely deficient in the food intake, consider eating more oranges/ guava/ papaya/ strawberry"
    elif Vit_C >= 30:
        color = 'g'
        com_Vit_C = "Vitamin C is adequate in the food intake"
elif Age >=7 and Age <=18:
    Vit_C_Dev1=40*factor1
    Vit_C_Dev2=40*factor2
    if Vit_C < Vit_C_Dev1:
         color = 'r'
         com_Vit_C = "Vitamin C is severely deficient in the food intake, consider eating more oranges/ guava/ papaya/ strawberry"
    elif Vit_C < Vit_C_Dev2:
         color = 'o'
         com_Vit_C = "Vitamin C is severely deficient in the food intake, consider eating more oranges/ guava/ papaya/ strawberry"
    elif Vit_C >= 40:
         color = 'g'
         com_Vit_C = "Vitamin C is adequate in the food intake"
    
Vit_D=float(input("Enter the micro-gram/day intake of Vitamin D: "))
if Age >=0 and Age <=18:
    Vit_D_Dev1=5*factor1
    Vit_D_Dev2=5*factor2
    if Vit_D < Vit_D_Dev1:
         color = 'r'
         com_Vit_D = "Vitamin D is severely deficient in your food intake, consider including salmon/ sardines/ oysters/ shrimp/ egg yolk/ milk/ cereal/ oatmeal/ mushrooms."
    elif Vit_D < Vit_D_Dev2:
         color = 'o'
         com_Vit_D = "Vitamin D is severely deficient in your food intake, consider including salmon/ sardines/ oysters/ shrimp/ egg yolk/ milk/ cereal/ oatmeal/ mushrooms."
    elif Vit_D >= 5:
         color = 'g'
         com_Vit_D = "There is adequate intake of Vitamin D through food."
      
Vit_E=float(input("Enter the mg/day intake of Vitamin E: "))
if Age >=1 and Age <=3:
    Vit_E_Dev1=6*factor1
    Vit_E_Dev2=6*factor2
    if Vit_E < Vit_E_Dev1:
         color = 'r'
         com_Vit_E = "Vitamin E is severely deficient in your food intake, consider including sun flower oil/ peanuts/ mango/ kiwi/ leafy vegetables/ fishes in your food."
    elif Vit_E < Vit_E_Dev2:
         color = 'o'
         com_Vit_E = "Vitamin E is deficient in your food intake, consider including sun flower oil/ peanuts/ mango/ kiwi/ leafy vegetables/ fishes in your food."
    elif Vit_E >= 6:
         color = 'g'
         com_Vit_E = "There is adequate intake of Vitamin E through food."
elif Age >=4 and Age <=10:
    Vit_E_Dev1=7*factor1
    Vit_E_Dev2=7*factor2
    if Vit_E < Vit_E_Dev1:
         color = 'r'
         com_Vit_E = "Vitamin E is severely deficient in your food intake, consider including sun flower oil/ peanuts/ mango/ kiwi/ leafy vegetables/ fishes in your food."
    elif Vit_E < Vit_E_Dev2:
         color = 'o'
         com_Vit_E = "Vitamin E is deficient in your food intake, consider including sun flower oil/ peanuts/ mango/ kiwi/ leafy vegetables/ fishes in your food."
    elif Vit_E >= 6:
         color = 'g'
         com_Vit_E = "There is adequate intake of Vitamin E through food."
elif Age >=11 and Age <=18:
    Vit_E_Dev1=11*factor1
    Vit_E_Dev2=11*factor2
    if Vit_E < Vit_E_Dev1:
         color = 'r'
         com_Vit_E = "Vitamin E is severely deficient in your food intake, consider including sun flower oil/ peanuts/ mango/ kiwi/ leafy vegetables/ fishes in your food."
    elif Vit_E < Vit_E_Dev2:
         color = 'o'
         com_Vit_E = "Vitamin E is deficient in your food intake, consider including sun flower oil/ peanuts/ mango/ kiwi/ leafy vegetables/ fishes in your food."
    elif Vit_E >= 11:
         color = 'g'
         com_Vit_E = "There is adequate intake of Vitamin E through food."

     
Vit_B_12=float(input("Enter the micro gram/day intake of Vitamin B 12: "))
if Age >=1 and Age <=3:
    Vit_B_12_Dev1=0.9*factor1
    Vit_B_12_Dev2=0.9*factor2
    if Vit_B_12 < Vit_B_12_Dev1:
         color = 'r' 
         com_Vit_B = "Vitamin B12 is severely deficient in your food, consider including milk/ cheese/ meat/ egg in your food."
    elif Vit_B_12 < Vit_B_12_Dev2:
         color = 'o'
         com_Vit_B = "Vitamin B12 is deficient in your food, consider including milk/ cheese/ meat/ egg in your food."
    elif Vit_B_12 >= 0.9:
         color = 'g'
         com_Vit_B = "There is adequate intake of Vitamin B through food."
elif Age >=4 and Age <=6:
    Vit_B_12_Dev1=1.2*factor1
    Vit_B_12_Dev2=1.2*factor2
    if Vit_B_12 < Vit_B_12_Dev1:
         color = 'r'
         com_Vit_B = "Vitamin B12 is severely deficient in your food, consider including milk/ cheese/ meat/ egg in your food."
    elif Vit_B_12 < Vit_B_12_Dev2:
         color = 'o'
         com_Vit_B = "Vitamin B12 is deficient in your food, consider including milk/ cheese/ meat/ egg in your food."
    elif Vit_B_12 >= 1.2:
         color = 'g'
         com_Vit_B = "There is adequate intake of Vitamin B through food"
elif Age >=7 and Age <=9:
    Vit_B_12_Dev1=1.8*factor1
    Vit_B_12_Dev2=1.8*factor2
    if Vit_B_12 < Vit_B_12_Dev1:
         color = 'r'
         com_Vit_B = "Vitamin B12 is severely deficient in your food, consider including milk/ cheese/ meat/ egg in your food."
    elif Vit_B_12 < Vit_B_12_Dev2:
         color = 'o'
         com_Vit_B = "Vitamin B12 is deficient in your food, consider including milk/ cheese/ meat/ egg in your food."
    elif Vit_B_12 >= 1.8:
         color = 'g'
         com_Vit_B = "There is adequate intake of Vitamin B through food"
elif Age >=10 and Age <=18:
    Vit_B_12_Dev1=2.4*factor1
    Vit_B_12_Dev2=2.4*factor2
    if Vit_B_12 < Vit_B_12_Dev1:
         color = 'r'
         com_Vit_B = "Vitamin B12 is severely deficient in your food, consider including milk/ cheese/ meat/ egg in your food."
    elif Vit_B_12 < Vit_B_12_Dev2:
         color = 'o'
         com_Vit_B = "Vitamin B12 is deficient in your food, consider including milk/ cheese/ meat/ egg in your food."
    elif Vit_B_12 >= 2.4:
         color = 'g'
         com_Vit_B = "There is adequate intake of Vitamin B through food"


        
Iron=float(input("Enter the micro gram/day intake of Iron in food: "))
if Age >=1 and Age <=3:
    Iron_Dev1=7*factor1
    Iron_Dev2=7*factor2
    if Iron < Iron_Dev1:
         color = 'r'
         com_Iron = "Iron is severely deficient in your food, consider including spinach/ chicken/ fish/ dark chocolate/ cashew/ raisins/ dry apricots in your food."
    elif Iron < Iron_Dev2:
         color = 'o'
         com_Iron = "Iron is deficient in your food, consider including spinach/ chicken/ fish/ dark chocolate/ cashew/ raisins/ dry apricots in your food."
    elif Iron >= 7:
         color = 'g'
         com_Iron = "There is adequate intake of Iron through food."
elif Age >=4 and Age <=6:
    Iron_Dev1=10*factor1
    Iron_Dev2=10*factor2
    if Iron < Iron_Dev1:
         color = 'r'
         com_Iron = "Iron is severely deficient in your food, consider including spinach/ chicken/ fish/ dark chocolate/ cashew/ raisins/ dry apricots in your food."
    elif Iron < Iron_Dev2:
         color = 'o'
         com_Iron = "Iron is deficient in your food, consider including spinach/ chicken/ fish/ dark chocolate/ cashew/ raisins/ dry apricots in your food."
    elif Iron >= 10:
         color = 'g'
         com_Iron = "There is adequate intake of Irom through food."
elif Age >=7 and Age <=9:
    Iron_Dev1=8*factor1
    Iron_Dev2=8*factor2
    if Iron < Iron_Dev1:
         color = 'r'
         com_Iron = "Iron is severely deficient in your food, consider including spinach/ chicken/ fish/ dark chocolate/ cashew/ raisins/ dry apricots in your food."
    elif Iron < Iron_Dev2:
         color = 'o'
         com_Iron = "Iron is deficient in your food, consider including spinach/ chicken/ fish/ dark chocolate/ cashew/ raisins/ dry apricots in your food."
    elif Iron >= 8:
         color = 'g'
         com_Iron = "There is adequate intake of Irom through food."
         
elif Age >=10 and Age <=18:
    Gender= input("Please enter the gender M/F: ")
    if Gender == 'M':
        Iron_Dev1=11*factor1
        Iron_Dev2=11*factor2
        if Iron < Iron_Dev1:
             color = 'r'
             com_Iron = "Iron is severely deficient in your food, consider including spinach/ chicken/ fish/ dark chocolate/ cashew/ raisins/ dry apricots in your food."
        elif Iron < Iron_Dev2:
             color = 'o'
             com_Iron = "Iron is deficient in your food, consider including spinach/ chicken/ fish/ dark chocolate/ cashew/ raisins/ dry apricots in your food."
        elif Iron >= 11:
             color = 'g'
             com_Iron = "There is adequate intake of Irom through food."
    elif Gender == 'F':
        Iron_Dev1=15*factor1
        Iron_Dev2=15*factor2
        if Iron < Iron_Dev1:
             color = 'r'
             com_Iron = "Iron is severely deficient in your food, consider including spinach/ chicken/ fish/ dark chocolate/ cashew/ raisins/ dry apricots in your food."
        elif Iron < Iron_Dev2:
             color = 'o'
             com_Iron = "Iron is deficient in your food, consider including spinach/ chicken/ fish/ dark chocolate/ cashew/ raisins/ dry apricots in your food."
        elif Iron >= 15:
             color = 'g'
             com_Iron = "There is adequate intake of Irom through food."
             
            
Vit_A=float(input("Enter the micro gram/day intake of Vitamin A in food: "))
if Age >=1 and Age <=3:
    Vit_A_Dev1=200*factor1
    Vit_A_Dev2=200*factor2
    if Vit_A < Vit_A_Dev1:
         color = 'r'
         com_Vit_A = "Intake of Vitamin A in the food is VERY low, consider increasing the intake of milk and dairy products/ green leafy vegetables/ carrots/ mango/ papaya."
    elif Vit_A < Vit_A_Dev2:
         color = 'o'
         com_Vit_A = "Intake of Vitamin A in the food is low, consider increasing the intake of milk and dairy products/ green leafy vegetables/ carrots/ mango/ papaya."
    elif Vit_A >= 200:
         color = 'g'
         com_Vit_A = "There is adequate intake of Vitamin A through food."
elif Age >=4 and Age <=6:
    Vit_A_Dev1=200*factor1
    Vit_A_Dev2=200*factor2
    if Vit_A < Vit_A_Dev1:
         color = 'r'
         com_Vit_A = "Intake of Vitamin A in the food is VERY low, consider increasing the intake of milk and dairy products/ green leafy vegetables/ carrots/ mango/ papaya."
    elif Vit_A < Vit_A_Dev2:
         color = 'o'
         com_Vit_A = "Intake of Vitamin A in the food is low, consider increasing the intake of milk and dairy products/ green leafy vegetables/ carrots/ mango/ papaya."
    elif Vit_A >= 200:
         color = 'g'
         com_Vit_A = "There is adequate intake of Vitamin A through food."
elif Age >=7 and Age <=9:
    Vit_A_Dev1=250*factor1
    Vit_A_Dev2=250*factor2
    if Vit_A < Vit_A_Dev1:
         color = 'r'
         com_Vit_A = "Intake of Vitamin A in the food is VERY low, consider increasing the intake of milk and dairy products/ green leafy vegetables/ carrots/ mango/ papaya."
    elif Vit_A < Vit_A_Dev2:
         color = 'o'
         com_Vit_A = "Intake of Vitamin A in the food is low, consider increasing the intake of milk and dairy products/ green leafy vegetables/ carrots/ mango/ papaya."
    elif Vit_A >= 250:
         color = 'g'
         com_Vit_A = "There is adequate intake of Vitamin A through food."
if Age >=10 and Age <=18:
    Vit_A_Dev1=370*factor1
    Vit_A_Dev2=370*factor2
    if Vit_A < Vit_A_Dev1:
         color = 'r'
         com_Vit_A = "Intake of Vitamin A in the food is VERY low, consider increasing the intake of milk and dairy products/ green leafy vegetables/ carrots/ mango/ papaya."
    elif Vit_A < Vit_A_Dev2:
         color = 'o'
         com_Vit_A = "Intake of Vitamin A in the food is low, consider increasing the intake of milk and dairy products/ green leafy vegetables/ carrots/ mango/ papaya."
    elif Vit_A >= 370:
         color = 'g'
         com_Vit_A = "There is adequate intake of Vitamin A through food."
     

Vit_B_1= float(input("Enter the milli-gram/day intake of Vitamin B1 in food: "))
if Age >=1 and Age <=3:
    Vit_B_1_Dev1=0.5*factor1
    Vit_B_1_Dev2=0.5*factor2
    if Vit_B_1 < Vit_B_1_Dev1:
         color = 'r'
         com_Vit_B1 = "Intake of Vitamin B1 (commonly called as Thiamin) is VERY low, consider increasing the intake of ..."
    elif Vit_B_1 < Vit_B_1_Dev1:
         color = 'o'
         com_Vit_B1 = "Intake of Vitamin B1 (commonly called as Thiamin) is low, consider increasing the intake of ..."
    elif Vit_B_1 >= 0.5:
         color = 'g'
         com_Vit_B1 = "There is adequate intake of Vitamib B1 (Thiamin) through food"
if Age >=4 and Age <=6:
    Vit_B_1_Dev1=0.6*factor1
    Vit_B_1_Dev2=0.6*factor2
    if Vit_B_1 < Vit_B_1_Dev1:
         color = 'r'
         com_Vit_B1 = "Intake of Vitamin B1 (commonly called as Thiamin) is VERY low, consider increasing the intake of ..."
    elif Vit_B_1 < Vit_B_1_Dev1:
         color = 'o'
         com_Vit_B1 = "Intake of Vitamin B1 (commonly called as Thiamin) is low, consider increasing the intake of ..."
    elif Vit_B_1 >= 0.6:
         color = 'g'
         com_Vit_B1 = "There is adequate intake of Vitamib B1 (Thiamin) through food"
elif Age >=7 and Age <=9:
    Vit_B_1_Dev1=0.9*factor1
    Vit_B_1_Dev2=0.9*factor2
    if Vit_B_1 < Vit_B_1_Dev1:
         color = 'r'
         com_Vit_B1 = "Intake of Vitamin B1 (commonly called as Thiamin) is VERY low, consider increasing the intake of ..."
    elif Vit_B_1 < Vit_B_1_Dev1:
         color = 'o'
         com_Vit_B1 = "Intake of Vitamin B1 (commonly called as Thiamin) is low, consider increasing the intake of ..."
    elif Vit_B_1 >= 0.9:
         color = 'g'
         com_Vit_B1 = "There is adequate intake of Vitamib B1 (Thiamin) through food"
elif Age >=10 and Age <=18:
    Gender= input("Please enter the gender M/F: ")
    if Gender == 'M':
        Vit_B_1_Dev1=1.2*factor1
        Vit_B_1_Dev2=1.2*factor2
        if Vit_B_1 < Vit_B_1_Dev1:
             color = 'r'
             com_Vit_B1 = "Intake of Vitamin B1 (commonly called as Thiamin) is VERY low, consider increasing the intake of ..."
        elif Vit_B_1 < Vit_B_1_Dev1:
             color = 'o'
             com_Vit_B1 = "Intake of Vitamin B1 (commonly called as Thiamin) is low, consider increasing the intake of ..."
        elif Vit_B_1 >= 1.2:
             color = 'g'
             com_Vit_B1 = "There is adequate intake of Vitamib B1 (Thiamin) through food"
    elif Gender == 'F':
        Vit_B_1_Dev1=1.1*factor1
        Vit_B_1_Dev2=1.1*factor2
        if Vit_B_1 < Vit_B_1_Dev1:
             color = 'r'
             com_Vit_B1 = "Intake of Vitamin B1 (commonly called as Thiamin) is VERY low, consider increasing the intake of ..."
        elif Vit_B_1 < Vit_B_1_Dev1:
             color = 'o'
             com_Vit_B1 = "Intake of Vitamin B1 (commonly called as Thiamin) is low, consider increasing the intake of ..."
        elif Vit_B_1 >= 1.1:
             color = 'g'
             com_Vit_B1 = "There is adequate intake of Vitamib B1 (Thiamin) through food"

    

Zinc= float(input("Enter the milli-gram/day intake of Zinc in food: "))
if Age >=1 and Age <=3:
    Zinc_Dev1=3*factor1
    Zinc_Dev2=3*factor2
    if Zinc < Zinc_Dev1:
         color = 'r'
         com_Zinc = "Intake of Zinc in the food is VERY low, consider increasing the intake of pumpkin-seeds/ mushroom/ chicken/ yogurt/ spinach/ cashews/ watermelon-seeds/ legumes."
    elif Zinc < Zinc_Dev2:
         color = 'o'
         com_Zinc = "Intake of Zinc in the food is low, consider increasing the intake of pumpkin-seeds/ mushroom/ chicken/ yogurt/ spinach/ cashews/ watermelon-seeds/ legumes."
    elif Zinc >= 3:
         color = 'g'
         com_Zinc = "There is adequate intake of Zinc through food"
elif Age >=4 and Age <=6:
    Zinc_Dev1=5*factor1
    Zinc_Dev2=5*factor2
    if Zinc < Zinc_Dev1:
         color = 'r'
         com_Zinc = "Intake of Zinc in the food is VERY low, consider increasing the intake of pumpkin-seeds/ mushroom/ chicken/ yogurt/ spinach/ cashews/ watermelon-seeds/ legumes."
    elif Zinc < Zinc_Dev2:
         color = 'o'
         com_Zinc = "Intake of Zinc in the food is low, consider increasing the intake of pumpkin-seeds/ mushroom/ chicken/ yogurt/ spinach/ cashews/ watermelon-seeds/ legumes."
    elif Zinc >= 5:
         color = 'g'
         com_Zinc = "There is adequate intake of Zinc through food"
elif Age >=7 and Age <=9:
    Zinc_Dev1=8*factor1
    Zinc_Dev2=8*factor2
    if Zinc < Zinc_Dev1:
         color = 'r'
         com_Zinc = "Intake of Zinc in the food is VERY low, consider increasing the intake of pumpkin-seeds/ mushroom/ chicken/ yogurt/ spinach/ cashews/ watermelon-seeds/ legumes."
    elif Zinc < Zinc_Dev2:
         color = 'o'
         com_Zinc = "Intake of Zinc in the food is low, consider increasing the intake of pumpkin-seeds/ mushroom/ chicken/ yogurt/ spinach/ cashews/ watermelon-seeds/ legumes."
    elif Zinc >= 8:
         color = 'g'
         com_Zinc = "There is adequate intake of Zinc through food"
elif Age >=10 and Age <=18:
    Zinc_Dev1=11*factor1
    Zinc_Dev2=11*factor2
    if Zinc < Zinc_Dev1:
         color = 'r'
         com_Zinc = "Intake of Zinc in the food is VERY low, consider increasing the intake of pumpkin-seeds/ mushroom/ chicken/ yogurt/ spinach/ cashews/ watermelon-seeds/ legumes."
    elif Zinc < Zinc_Dev2:
         color = 'o'
         com_Zinc = "Intake of Zinc in the food is low, consider increasing the intake of pumpkin-seeds/ mushroom/ chicken/ yogurt/ spinach/ cashews/ watermelon-seeds/ legumes."
    elif Zinc >= 11:
         color = 'g'
         com_Zinc = "There is adequate intake of Zinc through food"


Mg= float(input("Enter the milli-gram/day intake of Magnesium in food: "))
if Age >=1 and Age <=3:
    Mg_Dev1=60*factor1
    Mg_Dev2=60*factor2
    if Mg < Mg_Dev1:
         color = 'r'
         com_Mg = "Intake of Magnesium in the food is VERY low, consider increasing the intake of peas/ beans/ legume seeds/ shell fish/ soya flour."
    elif Mg < Mg_Dev2:
         color = 'o'
         com_Mg = "Intake of Magnesium in the food is low, consider increasing the intake of peas/ beans/ legume seeds/ shell fish/ soya flour."
    elif Mg >= 60:
         color = 'g'
         com_Mg = "There is adequate intake of Magnesium through food"
if Age >=4 and Age <=6:
    Mg_Dev1=76*factor1
    Mg_Dev2=76*factor2
    if Mg < Mg_Dev1:
         color = 'r'
         com_Mg = "Intake of Magnesium in the food is VERY low, consider increasing the intake of peas/ beans/ legume seeds/ shell fish/ soya flour."
    elif Mg < Mg_Dev2:
         color = 'o'
         com_Mg = "Intake of Magnesium in the food is low, consider increasing the intake of peas/ beans/ legume seeds/ shell fish/ soya flour."
    elif Mg >= 76:
         color = 'g'
         com_Mg = "There is adequate intake of Magnesium through food"
if Age >=7 and Age <=9:
    Mg_Dev1=100*factor1
    Mg_Dev2=100*factor2
    if Mg < Mg_Dev1:
         color = 'r'
         com_Mg = "Intake of Magnesium in the food is VERY low, consider increasing the intake of peas/ beans/ legume seeds/ shell fish/ soya flour."
    elif Mg < Mg_Dev2:
         color = 'o'
         com_Mg = "Intake of Magnesium in the food is low, consider increasing the intake of peas/ beans/ legume seeds/ shell fish/ soya flour."
    elif Mg >= 100:
         color = 'g'
         com_Mg = "There is adequate intake of Magnesium through food"
if Age >=10 and Age <=18:
    if Gender == 'M':
        Mg_Dev1=230*factor1
        Mg_Dev2=230*factor2
        if Mg < Mg_Dev1:
             color = 'r'
             com_Mg = "Intake of Magnesium in the food is VERY low, consider increasing the intake of peas/ beans/ legume seeds/ shell fish/ soya flour."
        elif Mg < Mg_Dev2:
             color = 'o'
             com_Mg = "Intake of Magnesium in the food is low, consider increasing the intake of peas/ beans/ legume seeds/ shell fish/ soya flour."
        elif Mg >= 230:
             color = 'g'
             com_Mg = "There is adequate intake of Magnesium through food"
    if Gender == 'F':
        Mg_Dev1=220*factor1
        Mg_Dev2=220*factor2
        if Mg < Mg_Dev1:
             color = 'r'
             com_Mg = "Intake of Magnesium in the food is VERY low, consider increasing the intake of peas/ beans/ legume seeds/ shell fish/ soya flour."
        elif Mg < Mg_Dev2:
             color = 'o'
             com_Mg = "Intake of Magnesium in the food is low, consider increasing the intake of peas/ beans/ legume seeds/ shell fish/ soya flour."
        elif Mg >= 220:
             color = 'g'
             com_Mg = "There is adequate intake of Magnesium through food"