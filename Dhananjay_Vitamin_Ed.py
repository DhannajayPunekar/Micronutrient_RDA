# def (Age, Gender,Vit_C,Avg_Vit_D,Avg_Vit_E,Vit_B_12,Avg_Iron,Gender,Vit_A,Vit_B_1,Gender,Avg_Zinc,Avg_Magne,Avg_Iod,Age):

# from Sug_Child import Age,gender,Vit_C,Avg_Vit_D,Avg_Vit_E,Vit_B_12,Avg_Iron,Vit_A,Vit_B_1,Avg_Zinc,Avg_Magne,Avg_Iod    
# gender = Gender

# Vit_C = 25
# Avg_Vit_D =45
# Avg_Vit_E =54
# Vit_B_12 =455
# Avg_Iron =45
# Vit_A =78
# Vit_B_1 =78
# Avg_Zinc =55
# Avg_Magne =12
# Avg_Iod =36
# Avg_Selen = 85

factor1 = 1/3
factor2 = 2/3
def Micr_plots(micronutrient,name,color):
    import matplotlib.pyplot as plt
    from col20 import All_colors
    fig, hscor = plt.subplots()  
    fig.set_size_inches(2,1.6)        
    plt.pie([100-micronutrient,micronutrient], colors=[All_colors[17][1],color], startangle = 270, )
    
    my_circle=plt.Circle( (0,0), 0.7, color='white')
    p = plt.gcf()
    p.gca().add_artist(my_circle)    
    plt.text(0,-0.2,"{}".format(micronutrient), ha ='center', size=18, family ='sans')
    plt.axis('equal')
    plt.text(0,1.15,name, ha ='center', size=10, family ='helvetica',  color='k')
    
    plt.savefig("{}.jpg".format(name), dpi=200)        
    plt.close()

# Vit_C=float(input("Enter the milli-grams/day intake of Vitamin C: "))
def get_Vit_C(Vit_C,Age):
    if Age >=0 and Age <=1:
        Vit_C_ID=27
        Vit_C_Dev1=Vit_C_ID*factor1
        Vit_C_Dev2=Vit_C_ID*factor2
        if Vit_C < Vit_C_Dev1:
            colMicr = 'r'
            com_Vit_C = "Vitamin C is severely deficient in your food intake, consider eating more oranges/ guava/ papaya/ strawberry"
        elif Vit_C < Vit_C_Dev2:
            colMicr = 'y'
            com_Vit_C = "Vitamin C is deficient in your food intake, consider eating more oranges/ guava/ papaya/ strawberry"
        elif Vit_C >= Vit_C_ID and Vit_C <= 400:
            colMicr = 'g'
            com_Vit_C = "Vitamin C is adequate in the food intake. Citrus fruits and juices are particularly rich sources of vitamin C."
        elif Vit_C >= 400:
            colMicr = 'r'
            com_Vit_C = "Vitamin C is too high in your food intake and can be toxic to health, reduce the intake of foods rich in Vitamin C"
        else:
            print("Condition is not satisfied")
        
    elif Age >=1 and Age <=6:
        Vit_C_ID=30
        Vit_C_Dev1=Vit_C_ID*factor1
        Vit_C_Dev2=Vit_C_ID*factor2
        if Vit_C < Vit_C_Dev1:
            colMicr = 'r'
            com_Vit_C = "Vitamin C is severely deficient in the food intake, consider eating more oranges/ guava/ papaya/ strawberry"
        elif Vit_C < Vit_C_Dev2:
            colMicr = 'y'
            com_Vit_C = "Vitamin C is deficient in the food intake, consider eating more oranges/ guava/ papaya/ strawberry"
        elif Vit_C >= Vit_C_ID and Vit_C <=650:
            colMicr = 'g'
            com_Vit_C = "Vitamin C is adequate in the food intake. Citrus fruits and juices are particularly rich sources of vitamin C."
        elif Vit_C >= 650:
            colMicr = 'r'
            com_Vit_C = "Vitamin C is too high in the food intake and can be toxic to health, reduce the intake of foods rich in Vitamin C"
        else:
            print("Condition is not satisfied")
            
    elif Age >=7 and Age <=18:
        Vit_C_ID=40
        Vit_C_Dev1=Vit_C_ID*factor1
        Vit_C_Dev2=Vit_C_ID*factor2
        if Vit_C < Vit_C_Dev1:
            colMicr = 'r'
            com_Vit_C = "Vitamin C is severely deficient in the food intake, consider eating more oranges/ guava/ papaya/ strawberry"
        elif Vit_C < Vit_C_Dev2:
            colMicr = 'y'
            com_Vit_C = "Vitamin C is deficient in the food intake, consider eating more oranges/ guava/ papaya/ strawberry"
        elif Vit_C >= Vit_C_ID and Vit_C<= 650:
            colMicr = 'g'
            com_Vit_C = "Vitamin C is adequate in the food intake. Citrus fruits and juices are particularly rich sources of vitamin C."
        elif Vit_C >= 650:
            colMicr = 'r'
            com_Vit_C = "Vitamin C is too high in the food intake and can be toxic to health, reduce the intake of foods rich in Vitamin C."
        else:
            print("Condition is not satisfied")
            
    temp = int(Vit_C/Vit_C_ID*100)
    if temp >99:
        temp=100
    Micr_plots(temp,"Vitamin C",colMicr)
    return(com_Vit_C,colMicr,650)
# Avg_Vit_D=float(input("Enter the micro-gram/day intake of Vitamin D: "))
def get_Vit_D(Avg_Vit_D,Age):
    if Age >=0 and Age <=18:
        Vit_D_ID=5
        Vit_D_Dev1=Vit_D_ID*factor1
        Vit_D_Dev2=Vit_D_ID*factor2
        if Avg_Vit_D < Vit_D_Dev1:
            colMicr = 'r'
            com_Vit_D = "Vitamin D is severely deficient in your food intake, consider including salmon/ sardines/ oysters/ shrimp/ egg yolk/ milk/ cereal/ oatmeal/ mushrooms."
        elif Avg_Vit_D < Vit_D_Dev2:
            colMicr = 'y'
            com_Vit_D = "Vitamin D is deficient in your food intake, consider including salmon/ sardines/ oysters/ shrimp/ egg yolk/ milk/ cereal/ oatmeal/ mushrooms."
        elif Avg_Vit_D >= Vit_D_Dev2:
            colMicr = 'g'
            com_Vit_D = "There is adequate intake of Vitamin D through food. Citrus fruits and juices are particularly rich sources of vitamin C."
        else:
            print("Condition is not satisfied")
            
    temp = int(Avg_Vit_D/Vit_D_ID*100)
    if temp >99:
        temp=100
    Micr_plots(temp,"Vitamin D",colMicr)
    return (com_Vit_D,colMicr,Vit_D_ID)      
# Avg_Vit_E=float(input("Enter the mg/day intake of Vitamin E: "))
def get_Vit_E(Avg_Vit_E,Age):
    if Age >=1 and Age <=3:
        Vit_E_ID=6
        Vit_E_Dev1=Vit_E_ID*factor1
        Vit_E_Dev2=Vit_E_ID*factor2
        if Avg_Vit_E < Vit_E_Dev1:
            colMicr = 'r'
            com_Vit_E = "Vitamin E is severely deficient in your food intake, consider including sun flower oil/ peanuts/ mango/ kiwi/ leafy vegetables/ fishes in your food."
        elif Avg_Vit_E < Vit_E_Dev2:
            colMicr = 'y'
            com_Vit_E = "Vitamin E is deficient in your food intake, consider including sun flower oil/ peanuts/ mango/ kiwi/ leafy vegetables/ fishes in your food."
        elif Avg_Vit_E >= Vit_E_Dev2:
            colMicr = 'g'
            com_Vit_E = "There is adequate intake of Vitamin E through food.  Vitamin E is a powerful antioxidant that may help slow the aging process of your cells."
        else:
            print("Condition is not satisfied")
            
    elif Age >=4 and Age <=10:
        Vit_E_ID=7
        Vit_E_Dev1=Vit_E_ID*factor1
        Vit_E_Dev2=Vit_E_ID*factor2
        if Avg_Vit_E < Vit_E_Dev1:
            colMicr = 'r'
            com_Vit_E = "Vitamin E is severely deficient in your food intake, consider including sun flower oil/ peanuts/ mango/ kiwi/ leafy vegetables/ fishes in your food."
        elif Avg_Vit_E < Vit_E_Dev2:
            colMicr = 'y'
            com_Vit_E = "Vitamin E is deficient in your food intake, consider including sun flower oil/ peanuts/ mango/ kiwi/ leafy vegetables/ fishes in your food."
        elif Avg_Vit_E >= Vit_E_Dev2:
            colMicr = 'g'
            com_Vit_E = "There is adequate intake of Vitamin E through food. Vitamin E is a powerful antioxidant that may help slow the aging process of your cells."
        else:
            print("Condition is not satisfied")
            
    elif Age >=11 and Age <=18:
        Vit_E_ID=11
        Vit_E_Dev1=Vit_E_ID*factor1
        Vit_E_Dev2=Vit_E_ID*factor2
        if Avg_Vit_E < Vit_E_Dev1:
            colMicr = 'r'
            com_Vit_E = "Vitamin E is severely deficient in your food intake, consider including sun flower oil/ peanuts/ mango/ kiwi/ leafy vegetables/ fishes in your food."
        elif Avg_Vit_E < Vit_E_Dev2:
            colMicr = 'y'
            com_Vit_E = "Vitamin E is deficient in your food intake, consider including sun flower oil/ peanuts/ mango/ kiwi/ leafy vegetables/ fishes in your food."
        elif Avg_Vit_E >= Vit_E_Dev2:
            colMicr = 'g'
            com_Vit_E = "There is adequate intake of Vitamin E through food. Vitamin E is a powerful antioxidant that may help slow the aging process of your cells."
        else:
            print("Condition is not satisfied")
    temp = int(Avg_Vit_E/Vit_E_ID*100)
    if temp >99:
        temp=100
    elif temp < 1:
        import random
        temp = int(10 + random.random()*2)
    Micr_plots(temp,"Vitamin E",colMicr)
    return(com_Vit_E,colMicr,Vit_E_ID)        
     
# Vit_B_12=float(input("Enter the micro gram/day intake of Vitamin B 12: "))
def get_Vit_B12(Vit_B_12,Age):
    if Age >=1 and Age <=3:
        Vit_B_12_ID=0.9
        Vit_B_12_Dev1=Vit_B_12_ID*factor1
        Vit_B_12_Dev2=Vit_B_12_ID*factor2
        if Vit_B_12 < Vit_B_12_Dev1:
            colMicr = 'r' 
            com_Vit_B = "Vitamin B-12 is severely deficient in your food, consider including milk/ cheese/ meat/ egg in your food."
        elif Vit_B_12 < Vit_B_12_Dev2:
            colMicr = 'y'
            com_Vit_B = "Vitamin B-12 is deficient in your food, consider including milk/ cheese/ meat/ egg in your food."
        elif Vit_B_12 >= Vit_B_12_Dev2:
            colMicr = 'g'
            com_Vit_B = "There is adequate intake of Vitamin B-12 through food. The best sources of Vitamin B-12 are milk and its products."
        else:
            print("Condition is not satisfied")
            
    elif Age >=4 and Age <=6:
        Vit_B_12_ID=1.2
        Vit_B_12_Dev1=Vit_B_12_ID*factor1
        Vit_B_12_Dev2=Vit_B_12_ID*factor2
        if Vit_B_12 < Vit_B_12_Dev1:
            colMicr = 'r'
            com_Vit_B = "Vitamin B-12 is severely deficient in your food, consider including milk/ cheese/ meat/ egg in your food."
        elif Vit_B_12 < Vit_B_12_Dev2:
            colMicr = 'y'
            com_Vit_B = "Vitamin B-12 is deficient in your food, consider including milk/ cheese/ meat/ egg in your food."
        elif Vit_B_12 >= Vit_B_12_Dev2:
            colMicr = 'g'
            com_Vit_B = "There is adequate intake of Vitamin B-12 through food. The best sources of Vitamin B-12 are milk and its products."
        else:
            print("Condition is not satisfied")
            
    elif Age >=7 and Age <=9:
        Vit_B_12_ID=1.8
        Vit_B_12_Dev1=Vit_B_12_ID*factor1
        Vit_B_12_Dev2=Vit_B_12_ID*factor2
        if Vit_B_12 < Vit_B_12_Dev1:
            colMicr = 'r'
            com_Vit_B = "Vitamin B-12 is severely deficient in your food, consider including milk/ cheese/ meat/ egg in your food."
        elif Vit_B_12 < Vit_B_12_Dev2:
            colMicr = 'y'
            com_Vit_B = "Vitamin B-12 is deficient in your food, consider including milk/ cheese/ meat/ egg in your food."
        elif Vit_B_12 >= Vit_B_12_Dev2:
            colMicr = 'g'
            com_Vit_B = "There is adequate intake of Vitamin B through food. The best sources of Vitamin B-12 are milk and its products."
        else:
            print("Condition is not satisfied")
            
    elif Age >=10 and Age <=18:
        Vit_B_12_ID=2.4
        Vit_B_12_Dev1=Vit_B_12_ID*factor1
        Vit_B_12_Dev2=Vit_B_12_ID*factor2
        if Vit_B_12 < Vit_B_12_Dev1:
            colMicr = 'r'
            com_Vit_B = "Vitamin B-12 is severely deficient in your food, consider including milk/ cheese/ meat/ egg in your food."
        elif Vit_B_12 < Vit_B_12_Dev2:
            colMicr = 'y'
            com_Vit_B = "Vitamin B-12 is deficient in your food, consider including milk/ cheese/ meat/ egg in your food."
        elif Vit_B_12 >= Vit_B_12_Dev2:
            colMicr = 'g'
            com_Vit_B = "There is adequate intake of Vitamin B through food. The best sources of Vitamin B-12 are milk and its products."
        else:
            print("Condition is not satisfied")
    temp = int(Vit_B_12/Vit_B_12_ID*100)
    if temp >99:
        temp=100
    Micr_plots(temp,"Vitamin B12",colMicr)
    return(com_Vit_B,colMicr,Vit_B_12_ID)        

        
# Avg_Iron=float(input("Enter the micro gram/day intake of Iron in food: "))
def get_Iron(Avg_Iron,Age,Gender):
    if Age >=1 and Age <=3:
        Iron_ID=7
        Iron_Dev1=Iron_ID*factor1
        Iron_Dev2=Iron_ID*factor2
        if Avg_Iron < Iron_Dev1:
            colMicr = 'r'
            com_Iron = "Iron is severely deficient in your food, consider including spinach/ chicken/ fish/ dark chocolate/ cashew/ raisins/ dry apricots in your food."
        elif Avg_Iron < Iron_Dev2:
            colMicr = 'y'
            com_Iron = "Iron is deficient in your food, consider including spinach/ chicken/ fish/ dark chocolate/ cashew/ raisins/ dry apricots in your food."
        elif Avg_Iron >= Iron_Dev2:
            colMicr = 'g'
            com_Iron = "There is adequate intake of Iron through food. Adequate level of iron is required for maintaining proper hemoglobin level."
        else:
            print("Condition is not satisfied")
            
    elif Age >=4 and Age <=6:
        Iron_ID=10
        Iron_Dev1=Iron_ID*factor1
        Iron_Dev2=Iron_ID*factor2
        if Avg_Iron < Iron_Dev1:
            colMicr = 'r'
            com_Iron = "Iron is severely deficient in your food, consider including spinach/ chicken/ fish/ dark chocolate/ cashew/ raisins/ dry apricots in your food."
        elif Avg_Iron < Iron_Dev2:
            colMicr = 'y'
            com_Iron = "Iron is deficient in your food, consider including spinach/ chicken/ fish/ dark chocolate/ cashew/ raisins/ dry apricots in your food."
        elif Avg_Iron >= Iron_Dev2:
            colMicr = 'g'
            com_Iron = "There is adequate intake of Iron through food. Adequate level of iron is required for maintaining proper hemoglobin level. "
        else:
            print("Condition is not satisfied")
            
    elif Age >=7 and Age <=9:
        Iron_ID=8
        Iron_Dev1=Iron_ID*factor1
        Iron_Dev2=Iron_ID*factor2
        if Avg_Iron < Iron_Dev1:
            colMicr = 'r'
            com_Iron = "Iron is severely deficient in your food, consider including spinach/ chicken/ fish/ dark chocolate/ cashew/ raisins/ dry apricots in your food."
        elif Avg_Iron < Iron_Dev2:
            colMicr = 'y'
            com_Iron = "Iron is deficient in your food, consider including spinach/ chicken/ fish/ dark chocolate/ cashew/ raisins/ dry apricots in your food."
        elif Avg_Iron >= Iron_Dev2:
            colMicr = 'g'
            com_Iron = "There is adequate intake of Iron through food. Adequate level of iron is required for maintaining proper hemoglobin level."
        else:
            print("Condition is not satisfied")
            
    elif Age >=10 and Age <=18:
        # Gender= input("Please enter the gender M/F: ")
        
        if Gender == 'M':
            Iron_ID=11
            Iron_Dev1=Iron_ID*factor1
            Iron_Dev2=Iron_ID*factor2
            if Avg_Iron < Iron_Dev1:
                colMicr = 'r'
                com_Iron = "Iron is severely deficient in your food, consider including spinach/ chicken/ fish/ dark chocolate/ cashew/ raisins/ dry apricots in your food."
            elif Avg_Iron < Iron_Dev2:
                colMicr = 'y'
                com_Iron = "Iron is deficient in your food, consider including spinach/ chicken/ fish/ dark chocolate/ cashew/ raisins/ dry apricots in your food."
            elif Avg_Iron >= Iron_Dev2:
                colMicr = 'g'
                com_Iron = "There is adequate intake of Iron through food. Adequate level of iron is required for maintaining proper hemoglobin level."
            else:
                print("Condition is not satisfied")
            
        elif Gender == 'F':
            Iron_ID=15
            Iron_Dev1=Iron_ID*factor1
            Iron_Dev2=Iron_ID*factor2
            if Avg_Iron < Iron_Dev1:
                colMicr = 'r'
                com_Iron = "Iron is severely deficient in your food, consider including spinach/ chicken/ fish/ dark chocolate/ cashew/ raisins/ dry apricots in your food."
            elif Avg_Iron < Iron_Dev2:
                colMicr = 'y'
                com_Iron = "Iron is deficient in your food, consider including spinach/ chicken/ fish/ dark chocolate/ cashew/ raisins/ dry apricots in your food."
            elif Avg_Iron >= Iron_Dev2:
                colMicr = 'g'
                com_Iron = "There is adequate intake of Iron through food. Adequate level of iron is required for maintaining proper hemoglobin level."
            else:
                print("Condition is not satisfied")
    temp = int(Avg_Iron/Iron_ID*100)
    if temp >99:
        temp=100
    Micr_plots(temp,"Iron",colMicr)
    return(com_Iron,colMicr,Iron_ID)         

get_Iron(9,9,'M')            

# Vit_A=float(input("Enter the micro gram/day intake of Vitamin A in food: "))
def get_Vit_A(Vit_A,Age):
    if Age >=1 and Age <=3:
        Vit_A_ID=200
        Vit_A_Dev1=Vit_A_ID*factor1
        Vit_A_Dev2=Vit_A_ID*factor2
        if Vit_A < Vit_A_Dev1:
            colMicr = 'r'
            com_Vit_A = "Intake of Vitamin A in the food is VERY low, consider increasing the intake of milk and dairy products/ green leafy vegetables/ carrots/ mango/ papaya."
        elif Vit_A < Vit_A_Dev2:
            colMicr = 'y'
            com_Vit_A = "Intake of Vitamin A in the food is low, consider increasing the intake of milk and dairy products/ green leafy vegetables/ carrots/ mango/ papaya."
        elif Vit_A >= Vit_A_Dev2:
            colMicr = 'g'
            com_Vit_A = "There is adequate intake of Vitamin A through food. Vitamin A functions to maintain teeth, bones, soft tissue, white blood cells and the immune system."
        else:
            print("Condition is not satisfied")
    elif Age >=4 and Age <=6:
        Vit_A_ID=200
        Vit_A_Dev1=Vit_A_ID*factor1
        Vit_A_Dev2=Vit_A_ID*factor2
        if Vit_A < Vit_A_Dev1:
            colMicr = 'r'
            com_Vit_A = "Intake of Vitamin A in the food is VERY low, consider increasing the intake of milk and dairy products/ green leafy vegetables/ carrots/ mango/ papaya."
        elif Vit_A < Vit_A_Dev2:
            colMicr = 'y'
            com_Vit_A = "Intake of Vitamin A in the food is low, consider increasing the intake of milk and dairy products/ green leafy vegetables/ carrots/ mango/ papaya."
        elif Vit_A >= Vit_A_Dev2:
            colMicr = 'g'
            com_Vit_A = "There is adequate intake of Vitamin A through food. Vitamin A functions to maintain teeth, bones, soft tissue, white blood cells and the immune system."
        else:
            print("Condition is not satisfied")
    elif Age >=7 and Age <=9:
        Vit_A_ID=250
        Vit_A_Dev1=Vit_A_ID*factor1
        Vit_A_Dev2=Vit_A_ID*factor2
        if Vit_A < Vit_A_Dev1:
            colMicr = 'r'
            com_Vit_A = "Intake of Vitamin A in the food is VERY low, consider increasing the intake of milk and dairy products/ green leafy vegetables/ carrots/ mango/ papaya."
        elif Vit_A < Vit_A_Dev2:
            colMicr = 'y'
            com_Vit_A = "Intake of Vitamin A in the food is low, consider increasing the intake of milk and dairy products/ green leafy vegetables/ carrots/ mango/ papaya."
        elif Vit_A >= Vit_A_Dev2:
            colMicr = 'g'
            com_Vit_A = "There is adequate intake of Vitamin A through food. Vitamin A functions to maintain teeth, bones, soft tissue, white blood cells and the immune system."
        else:
            print("Condition is not satisfied")
    if Age >=10 and Age <=18:
        Vit_A_ID=370
        Vit_A_Dev1=Vit_A_ID*factor1
        Vit_A_Dev2=Vit_A_ID*factor2
        if Vit_A < Vit_A_Dev1:
            colMicr = 'r'
            com_Vit_A = "Intake of Vitamin A in the food is VERY low, consider increasing the intake of milk and dairy products/ green leafy vegetables/ carrots/ mango/ papaya."
        elif Vit_A < Vit_A_Dev2:
            colMicr = 'y'
            com_Vit_A = "Intake of Vitamin A in the food is low, consider increasing the intake of milk and dairy products/ green leafy vegetables/ carrots/ mango/ papaya."
        elif Vit_A >= Vit_A_Dev2:
            colMicr = 'g'
            com_Vit_A = "There is adequate intake of Vitamin A through food. Vitamin A functions to maintain teeth, bones, soft tissue, white blood cells and the immune system."
        else:
            print("Condition is not satisfied")
    temp = int(Vit_A/Vit_A_ID*100)
    if temp >99:
        temp=100
    Micr_plots(temp,"Vitamin A",colMicr)
    return(com_Vit_A,colMicr,Vit_A_ID)     

# Vit_B_1= float(input("Enter the milli-gram/day intake of Vitamin B1 in food: "))
def get_Vit_B1(Vit_B_1,Age,Gender):
    if Age >=1 and Age <=3:
        Vit_B_1_ID=0.5
        Vit_B_1_Dev1=Vit_B_1_ID*factor1
        Vit_B_1_Dev2=Vit_B_1_ID*factor2
        if Vit_B_1 < Vit_B_1_Dev1:
            colMicr = 'r'
            com_Vit_B1 = "Intake of Vitamin B1 (commonly called as Thiamin) is VERY low, consider increasing the intake of ..."
        elif Vit_B_1 < Vit_B_1_Dev1:
            colMicr = 'y'
            com_Vit_B1 = "Intake of Vitamin B1 (commonly called as Thiamin) is low, consider increasing the intake of ..."
        elif Vit_B_1 >= Vit_B_1_Dev2:
            colMicr = 'g'
            com_Vit_B1 = "There is adequate intake of Vitamib B1 (Thiamin) through food"
        else:
            print("Condition is not satisfied")
    if Age >=4 and Age <=6:
        Vit_B_1_ID=0.6
        Vit_B_1_Dev1=Vit_B_1_ID*factor1
        Vit_B_1_Dev2=Vit_B_1_ID*factor2
        if Vit_B_1 < Vit_B_1_Dev1:
            colMicr = 'r'
            com_Vit_B1 = "Intake of Vitamin B1 (commonly called as Thiamin) is VERY low, consider increasing the intake of ..."
        elif Vit_B_1 < Vit_B_1_Dev1:
            colMicr = 'y'
            com_Vit_B1 = "Intake of Vitamin B1 (commonly called as Thiamin) is low, consider increasing the intake of ..."
        elif Vit_B_1 >= Vit_B_1_Dev2:
            colMicr = 'g'
            com_Vit_B1 = "There is adequate intake of Vitamib B1 (Thiamin) through food"
        else:
            print("Condition is not satisfied")
    elif Age >=7 and Age <=9:
        Vit_B_1_ID=0.9
        Vit_B_1_Dev1=Vit_B_1_ID*factor1
        Vit_B_1_Dev2=Vit_B_1_ID*factor2
        if Vit_B_1 < Vit_B_1_Dev1:
            colMicr = 'r'
            com_Vit_B1 = "Intake of Vitamin B1 (commonly called as Thiamin) is VERY low, consider increasing the intake of ..."
        elif Vit_B_1 < Vit_B_1_Dev1:
            colMicr = 'y'
            com_Vit_B1 = "Intake of Vitamin B1 (commonly called as Thiamin) is low, consider increasing the intake of ..."
        elif Vit_B_1 >= Vit_B_1_Dev2:
            colMicr = 'g'
            com_Vit_B1 = "There is adequate intake of Vitamib B1 (Thiamin) through food"
        else:
            print("Condition is not satisfied")
    elif Age >=10 and Age <=18:
        # Gender= input("Please enter the gender M/F: ")
        if Gender == 'M':
            Vit_B_1_ID=1.2
            Vit_B_1_Dev1=Vit_B_1_ID*factor1
            Vit_B_1_Dev2=Vit_B_1_ID*factor2
            if Vit_B_1 < Vit_B_1_Dev1:
                colMicr = 'r'
                com_Vit_B1 = "Intake of Vitamin B1 (commonly called as Thiamin) is VERY low, consider increasing the intake of ..."
            elif Vit_B_1 < Vit_B_1_Dev1:
                colMicr = 'y'
                com_Vit_B1 = "Intake of Vitamin B1 (commonly called as Thiamin) is low, consider increasing the intake of ..."
            elif Vit_B_1 >= Vit_B_1_Dev2:
                colMicr = 'g'
                com_Vit_B1 = "There is adequate intake of Vitamib B1 (Thiamin) through food"
            else:
                print("Condition is not satisfied")
        elif Gender == 'F':
            Vit_B_1_ID=1.1
            Vit_B_1_Dev1=Vit_B_1_ID*factor1
            Vit_B_1_Dev2=Vit_B_1_ID*factor2
            if Vit_B_1 < Vit_B_1_Dev1:
                colMicr = 'r'
                com_Vit_B1 = "Intake of Vitamin B1 (commonly called as Thiamin) is VERY low, consider increasing the intake of ..."
            elif Vit_B_1 < Vit_B_1_Dev1:
                colMicr = 'y'
                com_Vit_B1 = "Intake of Vitamin B1 (commonly called as Thiamin) is low, consider increasing the intake of ..."
            elif Vit_B_1 >= Vit_B_1_Dev2:
                colMicr = 'g'
                com_Vit_B1 = "There is adequate intake of Vitamib B1 (Thiamin) through food"
            else:
                print("Condition is not satisfied")
    temp = int(Vit_B_1/Vit_B_1_ID*100)
    if temp >99:
        temp=100
    Micr_plots(temp,"Vitamin B1",colMicr)
    return(com_Vit_B1,colMicr,Vit_B_1_ID)            
    

# Avg_Zinc= float(input("Enter the milli-gram/day intake of Zinc in food: "))
def get_Zinc(Avg_Zinc,Age):
    if Age >=1 and Age <=3:
        Zinc_ID=3
        Zinc_Dev1=Zinc_ID*factor1
        Zinc_Dev2=Zinc_ID*factor2
        if Avg_Zinc < Zinc_Dev1:
            colMicr = 'r'
            com_Zinc = "Intake of Zinc in the food is VERY low, consider increasing the intake of pumpkin-seeds/ mushroom/ chicken/ yogurt/ spinach/ cashews/ watermelon-seeds/ legumes."
        elif Avg_Zinc < Zinc_Dev2:
            colMicr = 'y'
            com_Zinc = "Intake of Zinc in the food is low, consider increasing the intake of pumpkin-seeds/ mushroom/ chicken/ yogurt/ spinach/ cashews/ watermelon-seeds/ legumes."
        elif Avg_Zinc >= Zinc_Dev2:
            colMicr = 'g'
            com_Zinc = "There is adequate intake of Zinc through food. Zinc functions to prevent stunted growth, slow wound healing and improves immunity."
        else:
            print("Condition is not satisfied")
    elif Age >=4 and Age <=6:
        Zinc_ID=5
        Zinc_Dev1=Zinc_ID*factor1
        Zinc_Dev2=Zinc_ID*factor2
        if Avg_Zinc < Zinc_Dev1:
            colMicr = 'r'
            com_Zinc = "Intake of Zinc in the food is VERY low, consider increasing the intake of pumpkin-seeds/ mushroom/ chicken/ yogurt/ spinach/ cashews/ watermelon-seeds/ legumes."
        elif Avg_Zinc < Zinc_Dev2:
            colMicr = 'y'
            com_Zinc = "Intake of Zinc in the food is low, consider increasing the intake of pumpkin-seeds/ mushroom/ chicken/ yogurt/ spinach/ cashews/ watermelon-seeds/ legumes."
        elif Avg_Zinc >= Zinc_Dev2:
            colMicr = 'g'
            com_Zinc = "There is adequate intake of Zinc through food. Zinc functions to prevent stunted growth, slow wound healing and improves immunity."
        else:
            print("Condition is not satisfied")
    elif Age >=7 and Age <=9:
        Zinc_ID=8
        Zinc_Dev1=Zinc_ID*factor1
        Zinc_Dev2=Zinc_ID*factor2
        if Avg_Zinc < Zinc_Dev1:
            colMicr = 'r'
            com_Zinc = "Intake of Zinc in the food is VERY low, consider increasing the intake of pumpkin-seeds/ mushroom/ chicken/ yogurt/ spinach/ cashews/ watermelon-seeds/ legumes."
        elif Avg_Zinc < Zinc_Dev2:
            colMicr = 'y'
            com_Zinc = "Intake of Zinc in the food is low, consider increasing the intake of pumpkin-seeds/ mushroom/ chicken/ yogurt/ spinach/ cashews/ watermelon-seeds/ legumes."
        elif Avg_Zinc >= Zinc_Dev2:
            colMicr = 'g'
            com_Zinc = "There is adequate intake of Zinc through food. Zinc functions to prevent stunted growth, slow wound healing and improves immunity."
        else:
            print("Condition is not satisfied")
    elif Age >=10 and Age <=18:
        Zinc_ID=11
        Zinc_Dev1=Zinc_ID*factor1
        Zinc_Dev2=Zinc_ID*factor2
        if Avg_Zinc < Zinc_Dev1:
            colMicr = 'r'
            com_Zinc = "Intake of Zinc in the food is VERY low, consider increasing the intake of pumpkin-seeds/ mushroom/ chicken/ yogurt/ spinach/ cashews/ watermelon-seeds/ legumes."
        elif Avg_Zinc < Zinc_Dev2:
            colMicr = 'y'
            com_Zinc = "Intake of Zinc in the food is low, consider increasing the intake of pumpkin-seeds/ mushroom/ chicken/ yogurt/ spinach/ cashews/ watermelon-seeds/ legumes."
        elif Avg_Zinc >= Zinc_Dev2:
            colMicr = 'g'
            com_Zinc = "There is adequate intake of Zinc through food. Zinc functions to prevent stunted growth, slow wound healing and improves immunity."
        else:
            print("Condition is not satisfied")
    temp = int(Avg_Zinc/Zinc_ID*100)
    if temp >99:
        temp=100
    Micr_plots(temp,"Zinc",colMicr)
    return(com_Zinc,colMicr,Zinc_ID)        

# Avg_Magne= float(input("Enter the milli-gram/day intake of Magnesium in food: "))
def get_Mg(Avg_Magne,Age,Gender):
    if Age >=1 and Age <=3:
        Magne_ID=60
        Mg_Dev1=Magne_ID*factor1
        Mg_Dev2=Magne_ID*factor2
        if Avg_Magne < Mg_Dev1:
            colMicr = 'r'
            com_Mg = "Intake of Magnesium in the food is VERY low, consider increasing the intake of peas/ beans/ legume seeds/ shell fish/ soya flour."
        elif Avg_Magne < Mg_Dev2:
            colMicr = 'y'
            com_Mg = "Intake of Magnesium in the food is low, consider increasing the intake of peas/ beans/ legume seeds/ shell fish/ soya flour."
        elif Avg_Magne >= Mg_Dev2:
            colMicr = 'g'
            com_Mg = "There is adequate intake of Magnesium through food. Adequate magnesium intake has been associated with a lower risk of atherosclerosis, hypertension."
        else:
            print("Condition is not satisfied")
    if Age >=4 and Age <=6:
        Magne_ID=76
        Mg_Dev1=Magne_ID*factor1
        Mg_Dev2=Magne_ID*factor2
        if Avg_Magne < Mg_Dev1:
            colMicr = 'r'
            com_Mg = "Intake of Magnesium in the food is VERY low, consider increasing the intake of peas/ beans/ legume seeds/ shell fish/ soya flour."
        elif Avg_Magne < Mg_Dev2:
            colMicr = 'y'
            com_Mg = "Intake of Magnesium in the food is low, consider increasing the intake of peas/ beans/ legume seeds/ shell fish/ soya flour."
        elif Avg_Magne >= Mg_Dev2:
            colMicr = 'g'
            com_Mg = "There is adequate intake of Magnesium through food. Adequate magnesium intake has been associated with a lower risk of atherosclerosis, hypertension."
        else:
            print("Condition is not satisfied")
    if Age >=7 and Age <=9:
        Magne_ID=100
        Mg_Dev1=Magne_ID*factor1
        Mg_Dev2=Magne_ID*factor2
        if Avg_Magne < Mg_Dev1:
            colMicr = 'r'
            com_Mg = "Intake of Magnesium in the food is VERY low, consider increasing the intake of peas/ beans/ legume seeds/ shell fish/ soya flour."
        elif Avg_Magne < Mg_Dev2:
            colMicr = 'y'
            com_Mg = "Intake of Magnesium in the food is low, consider increasing the intake of peas/ beans/ legume seeds/ shell fish/ soya flour."
        elif Avg_Magne >= Mg_Dev2:
            colMicr = 'g'
            com_Mg = "There is adequate intake of Magnesium through food. Adequate magnesium intake has been associated with a lower risk of atherosclerosis, hypertension."
        else:
            print("Condition is not satisfied")
    if Age >=10 and Age <=18:
        if Gender == 'M':
            Magne_ID=230
            Mg_Dev1=Magne_ID*factor1
            Mg_Dev2=Magne_ID*factor2
            if Avg_Magne < Mg_Dev1:
                colMicr = 'r'
                com_Mg = "Intake of Magnesium in the food is VERY low, consider increasing the intake of peas/ beans/ legume seeds/ shell fish/ soya flour."
            elif Avg_Magne < Mg_Dev2:
                colMicr = 'y'
                com_Mg = "Intake of Magnesium in the food is low, consider increasing the intake of peas/ beans/ legume seeds/ shell fish/ soya flour."
            elif Avg_Magne >= Mg_Dev2:
                colMicr = 'g'
                com_Mg = "There is adequate intake of Magnesium through food. Adequate magnesium intake has been associated with a lower risk of atherosclerosis, hypertension."
            else:
                print("Condition is not satisfied")
        if Gender == 'F':
            Magne_ID=220
            Mg_Dev1=Magne_ID*factor1
            Mg_Dev2=Magne_ID*factor2
            if Avg_Magne < Mg_Dev1:
                colMicr = 'r'
                com_Mg = "Intake of Magnesium in the food is VERY low, consider increasing the intake of peas/ beans/ legume seeds/ shell fish/ soya flour."
            elif Avg_Magne < Mg_Dev2:
                colMicr = 'y'
                com_Mg = "Intake of Magnesium in the food is low, consider increasing the intake of peas/ beans/ legume seeds/ shell fish/ soya flour."
            elif Avg_Magne >= Mg_Dev2:
                colMicr = 'g'
                com_Mg = "There is adequate intake of Magnesium through food. Adequate magnesium intake has been associated with a lower risk of atherosclerosis, hypertension."
            else:
                print("Condition is not satisfied")
    temp = int(Avg_Magne/Magne_ID*100)
    if temp >99:
        temp=100
    Micr_plots(temp,"Magnesium",colMicr)
    return(com_Mg,colMicr,Magne_ID)            
# Avg_Iod= float(input("Enter the micro-gram/day intake of Iodine in food: "))
def get_Iod(Avg_Iod,Age):
    if Age >=1 and Age <=3:
        Iod_ID=6
        Iod_Dev1=Iod_ID*factor1
        Iod_Dev2=Iod_ID*factor2
        if Avg_Iod < Iod_Dev1:
            colMicr = 'r'
            com_Iod = "Intake of Iodine in the food is VERY low, consider increasing the intake of egg/ iodised salt/ dairy."
        elif Avg_Iod < Iod_Dev2:
            colMicr = 'y'
            com_Iod = "Intake of Iodine in the food is low, consider increasing the intake of egg/ iodised salt/ dairy."
        elif Avg_Iod >= Iod_Dev2:
            colMicr = 'g'
            com_Iod = "There is adequate intake of Iodine through food. Iodine is used in the thyroid gland to make hormones."
        else:
            print("Condition is not satisfied")
    if Age >=4 and Age <=6:
        Iod_ID=4
        Iod_Dev1=Iod_ID*factor1
        Iod_Dev2=Iod_ID*factor2
        if Avg_Iod < Iod_Dev1:
            colMicr = 'r'
            com_Iod = "Intake of Iodine in the food is VERY low, consider increasing the intake of egg/ iodised salt/ dairy."
        elif Avg_Iod < Iod_Dev2:
            colMicr = 'y'
            com_Iod = "Intake of Iodine in the food is low, consider increasing the intake of egg/ iodised salt/ dairy."
        elif Avg_Iod >= Iod_Dev2:
            colMicr = 'g'
            com_Iod = "There is adequate intake of Iodine through food. Iodine is used in the thyroid gland to make hormones."
        else:
            print("Condition is not satisfied")
    if Age >=7 and Age <=12:
        Iod_ID=4
        Iod_Dev1=Iod_ID*factor1
        Iod_Dev2=Iod_ID*factor2
        if Avg_Iod < Iod_Dev1:
            colMicr = 'r'
            com_Iod = "Intake of Iodine in the food is VERY low, consider increasing the intake of egg/ iodised salt/ dairy."
        elif Avg_Iod < Iod_Dev2:
            colMicr = 'y'
            com_Iod = "Intake of Iodine in the food is low, consider increasing the intake of egg/ iodised salt/ dairy."
        elif Avg_Iod >= Iod_Dev2:
            colMicr = 'g'
            com_Iod = "There is adequate intake of Iodine through food. Iodine is used in the thyroid gland to make hormones."
        else:
            print("Condition is not satisfied")
    if Age >12:
        Iod_ID=2
        Iod_Dev1=Iod_ID*factor1
        Iod_Dev2=Iod_ID*factor2
        if Avg_Iod < Iod_Dev1:
            colMicr = 'r'
            com_Iod = "Intake of Iodine in the food is VERY low, consider increasing the intake of egg/ iodised salt/ dairy."
        elif Avg_Iod < Iod_Dev2:
            colMicr = 'y'
            com_Iod = "Intake of Iodine in the food is low, consider increasing the intake of egg/ iodised salt/ dairy."
        elif Avg_Iod >= Iod_Dev2:
            colMicr = 'g'
            com_Iod = "There is adequate intake of Iodine through food. Iodine is used in the thyroid gland to make hormones."
        else:
            print("Condition is not satisfied")
    temp = int(Avg_Iod/Iod_ID*100)
    if temp >99:
        temp=100
    Micr_plots(temp,"Iodine",colMicr)
    return(com_Iod,colMicr,Iod_ID)        
# Avg_Selen=float(input("Enter the micro-gram/day intake of Selenium in food: "))
def get_Selen(Avg_Selen,Age,Gender):
    if Age >=1 and Age <=3:
        Selen_ID=17
        Selen_Dev1=Selen_ID*factor1
        Selen_Dev2=Selen_ID*factor2
        if Avg_Selen < Selen_Dev1:
            colMicr = 'r'
            com_Selen = "Intake of Selenium in the food is VERY low, consider increasing the intake of eggs/ sardines/ fish/ shellfish/ legumes/ poultry/  soy products/ pork."
        elif Avg_Selen < Selen_Dev2:
            colMicr = 'y'
            com_Selen = "Intake of Selenium in the food is low, consider increasing the intake of eggs/ sardines/ fish/ shellfish/ legumes/ poultry/  soy products/ pork."
        elif Avg_Selen >= Selen_Dev2:
            colMicr = 'g'
            com_Selen = "There is adequate intake of Selenium through food. Selenium may help prevent cardiovascular disease, thyroid problems, disorders related to thinking and cancer."
        else:
            print("Condition is not satisfied")
    if Age >=4 and Age <=6:
        Selen_ID=22
        Selen_Dev1=Selen_ID*factor1
        Selen_Dev2=Selen_ID*factor2
        if Avg_Selen < Selen_Dev1:
            colMicr = 'r'
            com_Selen = "Intake of Selenium in the food is VERY low, consider increasing the intake of eggs/ sardines/ fish/ shellfish/ legumes/ poultry/  soy products/ pork."
        elif Avg_Selen < Selen_Dev2:
            colMicr = 'y'
            com_Selen = "Intake of Selenium in the food is low, consider increasing the intake of eggs/ sardines/ fish/ shellfish/ legumes/ poultry/  soy products/ pork."
        elif Avg_Selen >= Selen_Dev2:
            colMicr = 'g'
            com_Selen = "There is adequate intake of Selenium through food. Selenium may help prevent cardiovascular disease, thyroid problems, disorders related to thinking and cancer."
        else:
            print("Condition is not satisfied")
    if Age >=7 and Age <=9:
        Selen_ID=21
        Selen_Dev1=Selen_ID*factor1
        Selen_Dev2=Selen_ID*factor2
        if Avg_Selen < Selen_Dev1:
            colMicr = 'r'
            com_Selen = "Intake of Selenium in the food is VERY low, consider increasing the intake of eggs/ sardines/ fish/ shellfish/ legumes/ poultry/  soy products/ pork."
        elif Avg_Selen < Selen_Dev2:
            colMicr = 'y'
            com_Selen = "Intake of Selenium in the food is low, consider increasing the intake of eggs/ sardines/ fish/ shellfish/ legumes/ poultry/  soy products/ pork."
        elif Avg_Selen >= Selen_Dev2:
            colMicr = 'g'
            com_Selen = "There is adequate intake of Selenium through food. Selenium may help prevent cardiovascular disease, thyroid problems, disorders related to thinking and cancer."
        else:
            print("Condition is not satisfied")
    if Age >=10 and Age <=18:
        if Gender == 'M':
            Selen_ID=32
            Selen_Dev1=Selen_ID*factor1
            Selen_Dev2=Selen_ID*factor2
            if Avg_Selen < Selen_Dev1:
                colMicr = 'r'
                com_Selen = "Intake of Selenium in the food is VERY low, consider increasing the intake of eggs/ sardines/ fish/ shellfish/ legumes/ poultry/  soy products/ pork."
            elif Avg_Selen < Selen_Dev2:
                colMicr = 'y'
                com_Selen = "Intake of Selenium in the food is low, consider increasing the intake of eggs/ sardines/ fish/ shellfish/ legumes/ poultry/  soy products/ pork."
            elif Avg_Selen >= Selen_Dev2:
                colMicr = 'g'
                com_Selen = "There is adequate intake of Selenium through food. Selenium may help prevent cardiovascular disease, thyroid problems, disorders related to thinking and cancer."
            else:
                print("Condition is not satisfied")
        if Gender == 'F':
            Selen_ID=26
            Selen_Dev1=Selen_ID*factor1
            Selen_Dev2=Selen_ID*factor2
            if Avg_Selen < Selen_Dev1:
                colMicr = 'r'
                com_Selen = "Intake of Selenium in the food is VERY low, consider increasing the intake of eggs/ sardines/ fish/ shellfish/ legumes/ poultry/  soy products/ pork."
            elif Avg_Selen < Selen_Dev2:
                colMicr = 'y'
                com_Selen = "Intake of Selenium in the food is low, consider increasing the intake of eggs/ sardines/ fish/ shellfish/ legumes/ poultry/  soy products/ pork."
            elif Avg_Selen >= Selen_Dev2:
                colMicr = 'g'
                com_Selen = "There is adequate intake of Selenium through food. Selenium may help prevent cardiovascular disease, thyroid problems, disorders related to thinking and cancer."
            else:
                print("Condition is not satisfied")
    temp = int(Avg_Selen/Selen_ID*100)
    if temp >99:
        temp=100
    Micr_plots(temp,"Selenium",colMicr)
    return(com_Selen,colMicr,Selen_ID)            