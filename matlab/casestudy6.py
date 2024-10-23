#Exercise 6: Read sales data of bathing soap of all months and show it
#using a bar chart. Save this plot to your hard disk
import pandas as pd
import matplotlib.pyplot as plt  

df = pd.read_csv("company_sales_data.csv")
monthList  = df ['month_number'].tolist()
bathingsoapSalesData   = df ['bathingsoap'].tolist()
plt.bar(monthList, bathingsoapSalesData)
plt.xlabel('Month Number')
plt.ylabel('Sales units in number')
plt.title(' Sales data')
plt.xticks(monthList)
plt.grid(True, linewidth= 1, linestyle="--")
plt.title('bathingsoap sales data')
plt.savefig('I:\irfan-programming\pythonprg\matplotlib\sales_data_of_bathingsoap.png', dpi=150)
plt.show()
