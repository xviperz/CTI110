#CTI-110
#P2T1 -Sales Prediction
#Ross Wilson
#2/12/2018


#Get the total sales

projectedTotalSale=float(input("Enter the projected amount of total sales: "))

#calculate the total profit

profit= projectedTotalSale * 0.23

#display the profit
print ("The profit is $" , format(profit, ',.2f'))
