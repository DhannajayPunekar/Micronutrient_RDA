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
    Vit_C_ID=27
    Vit_C_Dev1=Vit_C_ID*factor1
    Vit_C_Dev2=Vit_C_ID*factor2
    if Vit_C < Vit_C_Dev1:
        color = 'r'
        com_Vit_C = "Vitamin C is severely deficient in your food intake, consider eating more oranges/ guava/ papaya/ strawberry"
    elif Vit_C < Vit_C_Dev2:
        color = 'o'
        com_Vit_C = "Vitamin C is deficient in your food intake, consider eating more oranges/ guava/ papaya/ strawberry"
    elif Vit_C >= Vit_C_ID and Vit_C <= 400:
        color = 'g'
        com_Vit_C = "Vitamin C is adequate in the food intake. Citrus fruits and juices are particularly rich sources of vitamin C."
    elif Vit_C >= 400:
        color = 'r'
        com_Vit_C = "Vitamin C is too high in your food intake and can be toxic to health, reduce the intake of foods rich in Vitamin C"

elif Age >=1 and Age <=6:
    Vit_C_ID=30
    Vit_C_Dev1=Vit_C_ID*factor1
    Vit_C_Dev2=Vit_C_ID*factor2
    if Vit_C < Vit_C_Dev1:
        color = 'r'
        com_Vit_C = "Vitamin C is severely deficient in the food intake, consider eating more oranges/ guava/ papaya/ strawberry"
    elif Vit_C < Vit_C_Dev2:
        color = 'o'
        com_Vit_C = "Vitamin C is deficient in the food intake, consider eating more oranges/ guava/ papaya/ strawberry"
    elif Vit_C >= Vit_C_ID and Vit_C <=650:
        color = 'g'
        com_Vit_C = "Vitamin C is adequate in the food intake. Citrus fruits and juices are particularly rich sources of vitamin C."
    elif Vit_C >= 650:
        color = 'r'
        com_Vit_C = "Vitamin C is too high in the food intake and can be toxic to health, reduce the intake of foods rich in Vitamin C"
elif Age >=7 and Age <=18:
    Vit_C_ID=40
    Vit_C_Dev1=Vit_C_ID*factor1
    Vit_C_Dev2=Vit_C_ID*factor2
    if Vit_C < Vit_C_Dev1:
        color = 'r'
        com_Vit_C = "Vitamin C is severely deficient in the food intake, consider eating more oranges/ guava/ papaya/ strawberry"
    elif Vit_C < Vit_C_Dev2:
        color = 'o'
        com_Vit_C = "Vitamin C is deficient in the food intake, consider eating more oranges/ guava/ papaya/ strawberry"
    elif Vit_C >= Vit_C_ID and Vit_C<= 650:
        color = 'g'
        com_Vit_C = "Vitamin C is adequate in the food intake. Citrus fruits and juices are particularly rich sources of vitamin C."
    elif Vit_C >= 650:
        color = 'r'
        com_Vit_C = "Vitamin C is too high in the food intake and can be toxic to health, reduce the intake of foods rich in Vitamin C."
    
Avg_Vit_D=float(input("Enter the micro-gram/day intake of Vitamin D: "))
if Age >=0 and Age <=18:
    Vit_D_ID=5
    Vit_D_Dev1=Vit_D_ID*factor1
    Vit_D_Dev2=Vit_D_ID*factor2
    if Avg_Vit_D < Vit_D_Dev1:
        color = 'r'
        com_Vit_D = "Vitamin D is severely deficient in your food intake, consider including salmon/ sardines/ oysters/ shrimp/ egg yolk/ milk/ cereal/ oatmeal/ mushrooms."
    elif Avg_Vit_D < Vit_D_Dev2:
        color = 'o'
        com_Vit_D = "Vitamin D is deficient in your food intake, consider including salmon/ sardines/ oysters/ shrimp/ egg yolk/ milk/ cereal/ oatmeal/ mushrooms."
    elif Avg_Vit_D >= Vit_D_ID:
        color = 'g'
        com_Vit_D = "There is adequate intake of Vitamin D through food. Citrus fruits and juices are particularly rich sources of vitamin C."
      
Avg_Vit_E=float(input("Enter the mg/day intake of Vitamin E: "))
if Age >=1 and Age <=3:
    Vit_E_ID=6
    Vit_E_Dev1=Vit_E_ID*factor1
    Vit_E_Dev2=Vit_E_ID*factor2
    if Avg_Vit_E < Vit_E_Dev1:
        color = 'r'
        com_Vit_E = "Vitamin E is severely deficient in your food intake, consider including sun flower oil/ peanuts/ mango/ kiwi/ leafy vegetables/ fishes in your food."
    elif Avg_Vit_E < Vit_E_Dev2:
        color = 'o'
        com_Vit_E = "Vitamin E is deficient in your food intake, consider including sun flower oil/ peanuts/ mango/ kiwi/ leafy vegetables/ fishes in your food."
    elif Avg_Vit_E >= Vit_E_ID:
        color = 'g'
        com_Vit_E = "There is adequate intake of Vitamin E through food.  Vitamin E is a powerful antioxidant that may help slow the aging process of your cells."
elif Age >=4 and Age <=10:
    Vit_E_ID=7
    Vit_E_Dev1=Vit_E_ID*factor1
    Vit_E_Dev2=Vit_E_ID*factor2
    if Avg_Vit_E < Vit_E_Dev1:
        color = 'r'
        com_Vit_E = "Vitamin E is severely deficient in your food intake, consider including sun flower oil/ peanuts/ mango/ kiwi/ leafy vegetables/ fishes in your food."
    elif Avg_Vit_E < Vit_E_Dev2:
        color = 'o'
        com_Vit_E = "Vitamin E is deficient in your food intake, consider including sun flower oil/ peanuts/ mango/ kiwi/ leafy vegetables/ fishes in your food."
    elif Avg_Vit_E >= Vit_E_ID:
        color = 'g'
        com_Vit_E = "There is adequate intake of Vitamin E through food. Vitamin E is a powerful antioxidant that may help slow the aging process of your cells."
elif Age >=11 and Age <=18:
    Vit_E_ID=11
    Vit_E_Dev1=Vit_E_ID*factor1
    Vit_E_Dev2=Vit_E_ID*factor2
    if Avg_Vit_E < Vit_E_Dev1:
        color = 'r'
        com_Vit_E = "Vitamin E is severely deficient in your food intake, consider including sun flower oil/ peanuts/ mango/ kiwi/ leafy vegetables/ fishes in your food."
    elif Avg_Vit_E < Vit_E_Dev2:
        color = 'o'
        com_Vit_E = "Vitamin E is deficient in your food intake, consider including sun flower oil/ peanuts/ mango/ kiwi/ leafy vegetables/ fishes in your food."
    elif Avg_Vit_E >= Vit_E_ID:
        color = 'g'
        com_Vit_E = "There is adequate intake of Vitamin E through food. Vitamin E is a powerful antioxidant that may help slow the aging process of your cells."

     
Vit_B_12=float(input("Enter the micro gram/day intake of Vitamin B 12: "))
if Age >=1 and Age <=3:
    Vit_B_12_ID=0.9
    Vit_B_12_Dev1=Vit_B_12_ID*factor1
    Vit_B_12_Dev2=Vit_B_12_ID*factor2
    if Vit_B_12 < Vit_B_12_Dev1:
        color = 'r' 
        com_Vit_B = "Vitamin B-12 is severely deficient in your food, consider including milk/ cheese/ meat/ egg in your food."
    elif Vit_B_12 < Vit_B_12_Dev2:
        color = 'o'
        com_Vit_B = "Vitamin B-12 is deficient in your food, consider including milk/ cheese/ meat/ egg in your food."
    elif Vit_B_12 >= Vit_B_12_ID:
        color = 'g'
        com_Vit_B = "There is adequate intake of Vitamin B-12 through food. The best sources of Vitamin B-12 are milk and its products."
elif Age >=4 and Age <=6:
    Vit_B_12_ID=1.2
    Vit_B_12_Dev1=Vit_B_12_ID*factor1
    Vit_B_12_Dev2=Vit_B_12_ID*factor2
    if Vit_B_12 < Vit_B_12_Dev1:
        color = 'r'
        com_Vit_B = "Vitamin B-12 is severely deficient in your food, consider including milk/ cheese/ meat/ egg in your food."
    elif Vit_B_12 < Vit_B_12_Dev2:
        color = 'o'
        com_Vit_B = "Vitamin B-12 is deficient in your food, consider including milk/ cheese/ meat/ egg in your food."
    elif Vit_B_12 >= Vit_B_12_ID:
        color = 'g'
        com_Vit_B = "There is adequate intake of Vitamin B-12 through food. The best sources of Vitamin B-12 are milk and its products."
elif Age >=7 and Age <=9:
    Vit_B_12_ID=1.8
    Vit_B_12_Dev1=Vit_B_12_ID*factor1
    Vit_B_12_Dev2=Vit_B_12_ID*factor2
    if Vit_B_12 < Vit_B_12_Dev1:
        color = 'r'
        com_Vit_B = "Vitamin B-12 is severely deficient in your food, consider including milk/ cheese/ meat/ egg in your food."
    elif Vit_B_12 < Vit_B_12_Dev2:
        color = 'o'
        com_Vit_B = "Vitamin B-12 is deficient in your food, consider including milk/ cheese/ meat/ egg in your food."
    elif Vit_B_12 >= Vit_B_12_ID:
        color = 'g'
        com_Vit_B = "There is adequate intake of Vitamin B through food. The best sources of Vitamin B-12 are milk and its products."
elif Age >=10 and Age <=18:
    Vit_B_12_ID=2.4
    Vit_B_12_Dev1=Vit_B_12_ID*factor1
    Vit_B_12_Dev2=Vit_B_12_ID*factor2
    if Vit_B_12 < Vit_B_12_Dev1:
        color = 'r'
        com_Vit_B = "Vitamin B-12 is severely deficient in your food, consider including milk/ cheese/ meat/ egg in your food."
    elif Vit_B_12 < Vit_B_12_Dev2:
        color = 'o'
        com_Vit_B = "Vitamin B-12 is deficient in your food, consider including milk/ cheese/ meat/ egg in your food."
    elif Vit_B_12 >= Vit_B_12_ID:
        color = 'g'
        com_Vit_B = "There is adequate intake of Vitamin B through food. The best sources of Vitamin B-12 are milk and its products."


        
Avg_Iron=float(input("Enter the micro gram/day intake of Iron in food: "))
if Age >=1 and Age <=3:
    Iron_ID=7
    Iron_Dev1=Iron_ID*factor1
    Iron_Dev2=Iron_ID*factor2
    if Avg_Iron < Iron_Dev1:
        color = 'r'
        com_Iron = "Iron is severely deficient in your food, consider including spinach/ chicken/ fish/ dark chocolate/ cashew/ raisins/ dry apricots in your food."
    elif Avg_Iron < Iron_Dev2:
        color = 'o'
        com_Iron = "Iron is deficient in your food, consider including spinach/ chicken/ fish/ dark chocolate/ cashew/ raisins/ dry apricots in your food."
    elif Avg_Iron >= Iron_ID:
        color = 'g'
        com_Iron = "There is adequate intake of Iron through food. Adequate level of iron is required for maintaining proper hemoglobin level."
elif Age >=4 and Age <=6:
    Iron_ID=10
    Iron_Dev1=Iron_ID*factor1
    Iron_Dev2=Iron_ID*factor2
    if Avg_Iron < Iron_Dev1:
        color = 'r'
        com_Iron = "Iron is severely deficient in your food, consider including spinach/ chicken/ fish/ dark chocolate/ cashew/ raisins/ dry apricots in your food."
    elif Avg_Iron < Iron_Dev2:
        color = 'o'
        com_Iron = "Iron is deficient in your food, consider including spinach/ chicken/ fish/ dark chocolate/ cashew/ raisins/ dry apricots in your food."
    elif Avg_Iron >= Iron_ID:
        color = 'g'
        com_Iron = "There is adequate intake of Iron through food. Adequate level of iron is required for maintaining proper hemoglobin level. "
elif Age >=7 and Age <=9:
    Iron_ID=8
    Iron_Dev1=Iron_ID*factor1
    Iron_Dev2=Iron_ID*factor2
    if Avg_Iron < Iron_Dev1:
        color = 'r'
        com_Iron = "Iron is severely deficient in your food, consider including spinach/ chicken/ fish/ dark chocolate/ cashew/ raisins/ dry apricots in your food."
    elif Avg_Iron < Iron_Dev2:
        color = 'o'
        com_Iron = "Iron is deficient in your food, consider including spinach/ chicken/ fish/ dark chocolate/ cashew/ raisins/ dry apricots in your food."
    elif Avg_Iron >= Iron_ID:
        color = 'g'
        com_Iron = "There is adequate intake of Iron through food. Adequate level of iron is required for maintaining proper hemoglobin level."
         
elif Age >=10 and Age <=18:
    Gender= input("Please enter the gender M/F: ")
    if Gender == 'M':
        Iron_ID=11
        Iron_Dev1=Iron_ID*factor1
        Iron_Dev2=Iron_ID*factor2
        if Avg_Iron < Iron_Dev1:
            color = 'r'
            com_Iron = "Iron is severely deficient in your food, consider including spinach/ chicken/ fish/ dark chocolate/ cashew/ raisins/ dry apricots in your food."
        elif Avg_Iron < Iron_Dev2:
            color = 'o'
            com_Iron = "Iron is deficient in your food, consider including spinach/ chicken/ fish/ dark chocolate/ cashew/ raisins/ dry apricots in your food."
        elif Avg_Iron >= Iron_ID:
            color = 'g'
            com_Iron = "There is adequate intake of Iron through food. Adequate level of iron is required for maintaining proper hemoglobin level."
    elif Gender == 'F':
        Iron_ID=15
        Iron_Dev1=Iron_ID*factor1
        Iron_Dev2=Iron_ID*factor2
        if Avg_Iron < Iron_Dev1:
            color = 'r'
            com_Iron = "Iron is severely deficient in your food, consider including spinach/ chicken/ fish/ dark chocolate/ cashew/ raisins/ dry apricots in your food."
        elif Avg_Iron < Iron_Dev2:
            color = 'o'
            com_Iron = "Iron is deficient in your food, consider including spinach/ chicken/ fish/ dark chocolate/ cashew/ raisins/ dry apricots in your food."
        elif Avg_Iron >= Iron_ID:
            color = 'g'
            com_Iron = "There is adequate intake of Iron through food. Adequate level of iron is required for maintaining proper hemoglobin level."
             
            
Vit_A=float(input("Enter the micro gram/day intake of Vitamin A in food: "))
if Age >=1 and Age <=3:
    Vit_A_ID=200
    Vit_A_Dev1=Vit_A_ID*factor1
    Vit_A_Dev2=Vit_A_ID*factor2
    if Vit_A < Vit_A_Dev1:
        color = 'r'
        com_Vit_A = "Intake of Vitamin A in the food is VERY low, consider increasing the intake of milk and dairy products/ green leafy vegetables/ carrots/ mango/ papaya."
    elif Vit_A < Vit_A_Dev2:
        color = 'o'
        com_Vit_A = "Intake of Vitamin A in the food is low, consider increasing the intake of milk and dairy products/ green leafy vegetables/ carrots/ mango/ papaya."
    elif Vit_A >= Vit_A_ID:
        color = 'g'
        com_Vit_A = "There is adequate intake of Vitamin A through food. Vitamin A functions to maintain teeth, bones, soft tissue, white blood cells and the immune system."
elif Age >=4 and Age <=6:
    Vit_A_ID=200
    Vit_A_Dev1=Vit_A_ID*factor1
    Vit_A_Dev2=Vit_A_ID*factor2
    if Vit_A < Vit_A_Dev1:
        color = 'r'
        com_Vit_A = "Intake of Vitamin A in the food is VERY low, consider increasing the intake of milk and dairy products/ green leafy vegetables/ carrots/ mango/ papaya."
    elif Vit_A < Vit_A_Dev2:
        color = 'o'
        com_Vit_A = "Intake of Vitamin A in the food is low, consider increasing the intake of milk and dairy products/ green leafy vegetables/ carrots/ mango/ papaya."
    elif Vit_A >= Vit_A_ID:
        color = 'g'
        com_Vit_A = "There is adequate intake of Vitamin A through food. Vitamin A functions to maintain teeth, bones, soft tissue, white blood cells and the immune system."
elif Age >=7 and Age <=9:
    Vit_A_ID=250
    Vit_A_Dev1=Vit_A_ID*factor1
    Vit_A_Dev2=Vit_A_ID*factor2
    if Vit_A < Vit_A_Dev1:
        color = 'r'
        com_Vit_A = "Intake of Vitamin A in the food is VERY low, consider increasing the intake of milk and dairy products/ green leafy vegetables/ carrots/ mango/ papaya."
    elif Vit_A < Vit_A_Dev2:
        color = 'o'
        com_Vit_A = "Intake of Vitamin A in the food is low, consider increasing the intake of milk and dairy products/ green leafy vegetables/ carrots/ mango/ papaya."
    elif Vit_A >= Vit_A_ID:
        color = 'g'
        com_Vit_A = "There is adequate intake of Vitamin A through food. Vitamin A functions to maintain teeth, bones, soft tissue, white blood cells and the immune system."
if Age >=10 and Age <=18:
    Vit_A_ID=370
    Vit_A_Dev1=Vit_A_ID*factor1
    Vit_A_Dev2=Vit_A_ID*factor2
    if Vit_A < Vit_A_Dev1:
        color = 'r'
        com_Vit_A = "Intake of Vitamin A in the food is VERY low, consider increasing the intake of milk and dairy products/ green leafy vegetables/ carrots/ mango/ papaya."
    elif Vit_A < Vit_A_Dev2:
        color = 'o'
        com_Vit_A = "Intake of Vitamin A in the food is low, consider increasing the intake of milk and dairy products/ green leafy vegetables/ carrots/ mango/ papaya."
    elif Vit_A >= Vit_A_ID:
        color = 'g'
        com_Vit_A = "There is adequate intake of Vitamin A through food. Vitamin A functions to maintain teeth, bones, soft tissue, white blood cells and the immune system."
     

Vit_B_1= float(input("Enter the milli-gram/day intake of Vitamin B1 in food: "))
if Age >=1 and Age <=3:
    Vit_B_1_ID=0.5
    Vit_B_1_Dev1=Vit_B_1_ID*factor1
    Vit_B_1_Dev2=Vit_B_1_ID*factor2
    if Vit_B_1 < Vit_B_1_Dev1:
        color = 'r'
        com_Vit_B1 = "Intake of Vitamin B1 (commonly called as Thiamin) is VERY low, consider increasing the intake of ..."
    elif Vit_B_1 < Vit_B_1_Dev1:
        color = 'o'
        com_Vit_B1 = "Intake of Vitamin B1 (commonly called as Thiamin) is low, consider increasing the intake of ..."
    elif Vit_B_1 >= Vit_B_1_ID:
        color = 'g'
        com_Vit_B1 = "There is adequate intake of Vitamib B1 (Thiamin) through food"
if Age >=4 and Age <=6:
    Vit_B_1_ID=0.6
    Vit_B_1_Dev1=Vit_B_1_ID*factor1
    Vit_B_1_Dev2=Vit_B_1_ID*factor2
    if Vit_B_1 < Vit_B_1_Dev1:
        color = 'r'
        com_Vit_B1 = "Intake of Vitamin B1 (commonly called as Thiamin) is VERY low, consider increasing the intake of ..."
    elif Vit_B_1 < Vit_B_1_Dev1:
        color = 'o'
        com_Vit_B1 = "Intake of Vitamin B1 (commonly called as Thiamin) is low, consider increasing the intake of ..."
    elif Vit_B_1 >= Vit_B_1_ID:
        color = 'g'
        com_Vit_B1 = "There is adequate intake of Vitamib B1 (Thiamin) through food"
elif Age >=7 and Age <=9:
    Vit_B_1_ID=0.9
    Vit_B_1_Dev1=Vit_B_1_ID*factor1
    Vit_B_1_Dev2=Vit_B_1_ID*factor2
    if Vit_B_1 < Vit_B_1_Dev1:
        color = 'r'
        com_Vit_B1 = "Intake of Vitamin B1 (commonly called as Thiamin) is VERY low, consider increasing the intake of ..."
    elif Vit_B_1 < Vit_B_1_Dev1:
        color = 'o'
        com_Vit_B1 = "Intake of Vitamin B1 (commonly called as Thiamin) is low, consider increasing the intake of ..."
    elif Vit_B_1 >= Vit_B_1_ID:
        color = 'g'
        com_Vit_B1 = "There is adequate intake of Vitamib B1 (Thiamin) through food"
elif Age >=10 and Age <=18:
    Gender= input("Please enter the gender M/F: ")
    if Gender == 'M':
        Vit_B_1_ID=1.2
        Vit_B_1_Dev1=Vit_B_1_ID*factor1
        Vit_B_1_Dev2=Vit_B_1_ID*factor2
        if Vit_B_1 < Vit_B_1_Dev1:
            color = 'r'
            com_Vit_B1 = "Intake of Vitamin B1 (commonly called as Thiamin) is VERY low, consider increasing the intake of ..."
        elif Vit_B_1 < Vit_B_1_Dev1:
            color = 'o'
            com_Vit_B1 = "Intake of Vitamin B1 (commonly called as Thiamin) is low, consider increasing the intake of ..."
        elif Vit_B_1 >= Vit_B_1_ID:
            color = 'g'
            com_Vit_B1 = "There is adequate intake of Vitamib B1 (Thiamin) through food"
    elif Gender == 'F':
        Vit_B_1_ID=1.1
        Vit_B_1_Dev1=Vit_B_1_ID*factor1
        Vit_B_1_Dev2=Vit_B_1_ID*factor2
        if Vit_B_1 < Vit_B_1_Dev1:
            color = 'r'
            com_Vit_B1 = "Intake of Vitamin B1 (commonly called as Thiamin) is VERY low, consider increasing the intake of ..."
        elif Vit_B_1 < Vit_B_1_Dev1:
            color = 'o'
            com_Vit_B1 = "Intake of Vitamin B1 (commonly called as Thiamin) is low, consider increasing the intake of ..."
        elif Vit_B_1 >= Vit_B_1_ID:
            color = 'g'
            com_Vit_B1 = "There is adequate intake of Vitamib B1 (Thiamin) through food"

    

Avg_Zinc= float(input("Enter the milli-gram/day intake of Zinc in food: "))
if Age >=1 and Age <=3:
    Zinc_ID=3
    Zinc_Dev1=Zinc_ID*factor1
    Zinc_Dev2=Zinc_ID*factor2
    if Avg_Zinc < Zinc_Dev1:
        color = 'r'
        com_Zinc = "Intake of Zinc in the food is VERY low, consider increasing the intake of pumpkin-seeds/ mushroom/ chicken/ yogurt/ spinach/ cashews/ watermelon-seeds/ legumes."
    elif Avg_Zinc < Zinc_Dev2:
        color = 'o'
        com_Zinc = "Intake of Zinc in the food is low, consider increasing the intake of pumpkin-seeds/ mushroom/ chicken/ yogurt/ spinach/ cashews/ watermelon-seeds/ legumes."
    elif Avg_Zinc >= Zinc_ID:
        color = 'g'
        com_Zinc = "There is adequate intake of Zinc through food. Zinc functions to prevent stunted growth, slow wound healing and improves immunity."
elif Age >=4 and Age <=6:
    Zinc_ID=5
    Zinc_Dev1=Zinc_ID*factor1
    Zinc_Dev2=Zinc_ID*factor2
    if Avg_Zinc < Zinc_Dev1:
        color = 'r'
        com_Zinc = "Intake of Zinc in the food is VERY low, consider increasing the intake of pumpkin-seeds/ mushroom/ chicken/ yogurt/ spinach/ cashews/ watermelon-seeds/ legumes."
    elif Avg_Zinc < Zinc_Dev2:
        color = 'o'
        com_Zinc = "Intake of Zinc in the food is low, consider increasing the intake of pumpkin-seeds/ mushroom/ chicken/ yogurt/ spinach/ cashews/ watermelon-seeds/ legumes."
    elif Avg_Zinc >= Zinc_ID:
        color = 'g'
        com_Zinc = "There is adequate intake of Zinc through food. Zinc functions to prevent stunted growth, slow wound healing and improves immunity."
elif Age >=7 and Age <=9:
    Zinc_ID=8
    Zinc_Dev1=Zinc_ID*factor1
    Zinc_Dev2=Zinc_ID*factor2
    if Avg_Zinc < Zinc_Dev1:
        color = 'r'
        com_Zinc = "Intake of Zinc in the food is VERY low, consider increasing the intake of pumpkin-seeds/ mushroom/ chicken/ yogurt/ spinach/ cashews/ watermelon-seeds/ legumes."
    elif Avg_Zinc < Zinc_Dev2:
        color = 'o'
        com_Zinc = "Intake of Zinc in the food is low, consider increasing the intake of pumpkin-seeds/ mushroom/ chicken/ yogurt/ spinach/ cashews/ watermelon-seeds/ legumes."
    elif Avg_Zinc >= Zinc_ID:
        color = 'g'
        com_Zinc = "There is adequate intake of Zinc through food. Zinc functions to prevent stunted growth, slow wound healing and improves immunity."
elif Age >=10 and Age <=18:
    Zinc_ID=11
    Zinc_Dev1=Zinc_ID*factor1
    Zinc_Dev2=Zinc_ID*factor2
    if Avg_Zinc < Zinc_Dev1:
        color = 'r'
        com_Zinc = "Intake of Zinc in the food is VERY low, consider increasing the intake of pumpkin-seeds/ mushroom/ chicken/ yogurt/ spinach/ cashews/ watermelon-seeds/ legumes."
    elif Avg_Zinc < Zinc_Dev2:
        color = 'o'
        com_Zinc = "Intake of Zinc in the food is low, consider increasing the intake of pumpkin-seeds/ mushroom/ chicken/ yogurt/ spinach/ cashews/ watermelon-seeds/ legumes."
    elif Avg_Zinc >= Zinc_ID:
        color = 'g'
        com_Zinc = "There is adequate intake of Zinc through food. Zinc functions to prevent stunted growth, slow wound healing and improves immunity."


Avg_Magne= float(input("Enter the milli-gram/day intake of Magnesium in food: "))
if Age >=1 and Age <=3:
    Magne_ID=60
    Mg_Dev1=Magne_ID*factor1
    Mg_Dev2=Magne_ID*factor2
    if Avg_Magne < Mg_Dev1:
        color = 'r'
        com_Mg = "Intake of Magnesium in the food is VERY low, consider increasing the intake of peas/ beans/ legume seeds/ shell fish/ soya flour."
    elif Avg_Magne < Mg_Dev2:
        color = 'o'
        com_Mg = "Intake of Magnesium in the food is low, consider increasing the intake of peas/ beans/ legume seeds/ shell fish/ soya flour."
    elif Avg_Magne >= Magne_ID:
        color = 'g'
        com_Mg = "There is adequate intake of Magnesium through food. Adequate magnesium intake has been associated with a lower risk of atherosclerosis, hypertension."
if Age >=4 and Age <=6:
    Magne_ID=76
    Mg_Dev1=Magne_ID*factor1
    Mg_Dev2=Magne_ID*factor2
    if Avg_Magne < Mg_Dev1:
        color = 'r'
        com_Mg = "Intake of Magnesium in the food is VERY low, consider increasing the intake of peas/ beans/ legume seeds/ shell fish/ soya flour."
    elif Avg_Magne < Mg_Dev2:
        color = 'o'
        com_Mg = "Intake of Magnesium in the food is low, consider increasing the intake of peas/ beans/ legume seeds/ shell fish/ soya flour."
    elif Avg_Magne >= Magne_ID:
        color = 'g'
        com_Mg = "There is adequate intake of Magnesium through food. Adequate magnesium intake has been associated with a lower risk of atherosclerosis, hypertension."
if Age >=7 and Age <=9:
    Magne_ID=100
    Mg_Dev1=Magne_ID*factor1
    Mg_Dev2=Magne_ID*factor2
    if Avg_Magne < Mg_Dev1:
        color = 'r'
        com_Mg = "Intake of Magnesium in the food is VERY low, consider increasing the intake of peas/ beans/ legume seeds/ shell fish/ soya flour."
    elif Avg_Magne < Mg_Dev2:
        color = 'o'
        com_Mg = "Intake of Magnesium in the food is low, consider increasing the intake of peas/ beans/ legume seeds/ shell fish/ soya flour."
    elif Avg_Magne >= Magne_ID:
        color = 'g'
        com_Mg = "There is adequate intake of Magnesium through food. Adequate magnesium intake has been associated with a lower risk of atherosclerosis, hypertension."
if Age >=10 and Age <=18:
    if Gender == 'M':
        Magne_ID=230
        Mg_Dev1=Magne_ID*factor1
        Mg_Dev2=Magne_ID*factor2
        if Avg_Magne < Mg_Dev1:
            color = 'r'
            com_Mg = "Intake of Magnesium in the food is VERY low, consider increasing the intake of peas/ beans/ legume seeds/ shell fish/ soya flour."
        elif Avg_Magne < Mg_Dev2:
            color = 'o'
            com_Mg = "Intake of Magnesium in the food is low, consider increasing the intake of peas/ beans/ legume seeds/ shell fish/ soya flour."
        elif Avg_Magne >= Magne_ID:
            color = 'g'
            com_Mg = "There is adequate intake of Magnesium through food. Adequate magnesium intake has been associated with a lower risk of atherosclerosis, hypertension."
    if Gender == 'F':
        Magne_ID=220
        Mg_Dev1=Magne_ID*factor1
        Mg_Dev2=Magne_ID*factor2
        if Avg_Magne < Mg_Dev1:
            color = 'r'
            com_Mg = "Intake of Magnesium in the food is VERY low, consider increasing the intake of peas/ beans/ legume seeds/ shell fish/ soya flour."
        elif Avg_Magne < Mg_Dev2:
            color = 'o'
            com_Mg = "Intake of Magnesium in the food is low, consider increasing the intake of peas/ beans/ legume seeds/ shell fish/ soya flour."
        elif Avg_Magne >= Magne_ID:
            color = 'g'
            com_Mg = "There is adequate intake of Magnesium through food. Adequate magnesium intake has been associated with a lower risk of atherosclerosis, hypertension."

Avg_Iod= float(input("Enter the micro-gram/day intake of Iodine in food: "))
if Age >=1 and Age <=3:
    Iod_ID=6
    Iod_Dev1=Iod_ID*factor1
    Iod_Dev2=Iod_ID*factor2
    if Avg_Iod < Iod_Dev1:
        color = 'r'
        com_Mg = "Intake of Iodine in the food is VERY low, consider increasing the intake of egg/ iodised salt/ dairy."
    elif Avg_Iod < Iod_Dev2:
        color = 'o'
        com_Mg = "Intake of Iodine in the food is low, consider increasing the intake of egg/ iodised salt/ dairy."
    elif Avg_Iod >= Iod_ID:
        color = 'g'
        com_Mg = "There is adequate intake of Iodine through food. Iodine is used in the thyroid gland to make hormones."
if Age >=4 and Age <=6:
    Iod_ID=4
    Iod_Dev1=Iod_ID*factor1
    Iod_Dev2=Iod_ID*factor2
    if Avg_Iod < Iod_Dev1:
        color = 'r'
        com_Mg = "Intake of Iodine in the food is VERY low, consider increasing the intake of egg/ iodised salt/ dairy."
    elif Avg_Iod < Iod_Dev2:
        color = 'o'
        com_Mg = "Intake of Iodine in the food is low, consider increasing the intake of egg/ iodised salt/ dairy."
    elif Avg_Iod >= Iod_ID:
        color = 'g'
        com_Mg = "There is adequate intake of Iodine through food. Iodine is used in the thyroid gland to make hormones."
if Age >=7 and Age <=12:
    Iod_ID=4
    Iod_Dev1=Iod_ID*factor1
    Iod_Dev2=Iod_ID*factor2
    if Avg_Iod < Iod_Dev1:
        color = 'r'
        com_Mg = "Intake of Iodine in the food is VERY low, consider increasing the intake of egg/ iodised salt/ dairy."
    elif Avg_Iod < Iod_Dev2:
        color = 'o'
        com_Mg = "Intake of Iodine in the food is low, consider increasing the intake of egg/ iodised salt/ dairy."
    elif Avg_Iod >= Iod_ID:
        color = 'g'
        com_Mg = "There is adequate intake of Iodine through food. Iodine is used in the thyroid gland to make hormones."
if Age >12:
    Iod_ID=2
    Iod_Dev1=Iod_ID*factor1
    Iod_Dev2=Iod_ID*factor2
    if Avg_Iod < Iod_Dev1:
        color = 'r'
        com_Mg = "Intake of Iodine in the food is VERY low, consider increasing the intake of egg/ iodised salt/ dairy."
    elif Avg_Iod < Iod_Dev2:
        color = 'o'
        com_Mg = "Intake of Iodine in the food is low, consider increasing the intake of egg/ iodised salt/ dairy."
    elif Avg_Iod >= Iod_ID:
        color = 'g'
        com_Mg = "There is adequate intake of Iodine through food. Iodine is used in the thyroid gland to make hormones."

Avg_Selen=float(input("Enter the micro-gram/day intake of Selenium in food: "))
if Age >=1 and Age <=3:
    Selen_ID=17
    Selen_Dev1=Selen_ID*factor1
    Selen_Dev2=Selen_ID*factor2
    if Avg_Selen < Selen_Dev1:
        color = 'r'
        com_Mg = "Intake of Selenium in the food is VERY low, consider increasing the intake of eggs/ sardines/ fish/ shellfish/ legumes/ poultry/  soy products/ pork."
    elif Avg_Selen < Selen_Dev2:
        color = 'o'
        com_Mg = "Intake of Selenium in the food is low, consider increasing the intake of eggs/ sardines/ fish/ shellfish/ legumes/ poultry/  soy products/ pork."
    elif Avg_Selen >= Selen_ID:
        color = 'g'
        com_Mg = "There is adequate intake of Selenium through food. Selenium may help prevent cardiovascular disease, thyroid problems, disorders related to thinking and cancer."
if Age >=4 and Age <=6:
    Selen_ID=22
    Selen_Dev1=Selen_ID*factor1
    Selen_Dev2=Selen_ID*factor2
    if Avg_Selen < Selen_Dev1:
        color = 'r'
        com_Mg = "Intake of Selenium in the food is VERY low, consider increasing the intake of eggs/ sardines/ fish/ shellfish/ legumes/ poultry/  soy products/ pork."
    elif Avg_Selen < Selen_Dev2:
        color = 'o'
        com_Mg = "Intake of Selenium in the food is low, consider increasing the intake of eggs/ sardines/ fish/ shellfish/ legumes/ poultry/  soy products/ pork."
    elif Avg_Selen >= Selen_ID:
        color = 'g'
        com_Mg = "There is adequate intake of Selenium through food. Selenium may help prevent cardiovascular disease, thyroid problems, disorders related to thinking and cancer."
if Age >=7 and Age <=9:
    Selen_ID=21
    Selen_Dev1=Selen_ID*factor1
    Selen_Dev2=Selen_ID*factor2
    if Avg_Selen < Selen_Dev1:
        color = 'r'
        com_Mg = "Intake of Selenium in the food is VERY low, consider increasing the intake of eggs/ sardines/ fish/ shellfish/ legumes/ poultry/  soy products/ pork."
    elif Avg_Selen < Selen_Dev2:
        color = 'o'
        com_Mg = "Intake of Selenium in the food is low, consider increasing the intake of eggs/ sardines/ fish/ shellfish/ legumes/ poultry/  soy products/ pork."
    elif Avg_Selen >= Selen_ID:
        color = 'g'
        com_Mg = "There is adequate intake of Selenium through food. Selenium may help prevent cardiovascular disease, thyroid problems, disorders related to thinking and cancer."
if Age >=10 and Age <=18:
    if gender == 'M':
        Selen_ID=32
        Selen_Dev1=Selen_ID*factor1
        Selen_Dev2=Selen_ID*factor2
        if Avg_Selen < Selen_Dev1:
            color = 'r'
            com_Mg = "Intake of Selenium in the food is VERY low, consider increasing the intake of eggs/ sardines/ fish/ shellfish/ legumes/ poultry/  soy products/ pork."
        elif Avg_Selen < Selen_Dev2:
            color = 'o'
            com_Mg = "Intake of Selenium in the food is low, consider increasing the intake of eggs/ sardines/ fish/ shellfish/ legumes/ poultry/  soy products/ pork."
        elif Avg_Selen >= Selen_ID:
            color = 'g'
            com_Mg = "There is adequate intake of Selenium through food. Selenium may help prevent cardiovascular disease, thyroid problems, disorders related to thinking and cancer."
    if gender == 'F':
        Selen_ID=26
        Selen_Dev1=Selen_ID*factor1
        Selen_Dev2=Selen_ID*factor2
        if Avg_Selen < Selen_Dev1:
            color = 'r'
            com_Mg = "Intake of Selenium in the food is VERY low, consider increasing the intake of eggs/ sardines/ fish/ shellfish/ legumes/ poultry/  soy products/ pork."
        elif Avg_Selen < Selen_Dev2:
            color = 'o'
            com_Mg = "Intake of Selenium in the food is low, consider increasing the intake of eggs/ sardines/ fish/ shellfish/ legumes/ poultry/  soy products/ pork."
        elif Avg_Selen >= Selen_ID:
            color = 'g'
            com_Mg = "There is adequate intake of Selenium through food. Selenium may help prevent cardiovascular disease, thyroid problems, disorders related to thinking and cancer."