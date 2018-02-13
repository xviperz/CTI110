#CTI-110
#P2HW2 - Tip Tax Total
#Ross Wilson
#02132018

foodCost=float(input("Enter the charge for the food :"))



tip=foodCost *.18



saleTax=foodCost *.07



totalCost=( foodCost+tip+saleTax)



print('Amount of food cost :',format(foodCost,',.2f'))



print ("Tip amount :",format(tip ,',.2f'))



print("Amount of sales tax :",format(saleTax,',.2f'))



print("total purchased :",format(totalCost,',.2f'))

