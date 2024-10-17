import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv("resources\sales_data.csv")
print(df.keys())
profitlist = df['total_profit'].tolist()
monthlist = df['month_number'].tolist()
toothpastelist = df['toothpaste'].tolist()
bathingsoaplist = df['bathingsoap'].tolist()
facecreamlist = df['facecream'].tolist()

plt.plot(monthlist,profitlist,'r-',monthlist,facecreamlist,'g-',linewidth =3,marker='o',markerfacecolor='k')
plt.ylabel("Profit las year")
plt.savefig("prova.png")
#plt.show()

plt.scatter(monthlist,toothpastelist)
#plt.show()

plt.bar(monthlist,bathingsoaplist)
#plt.show()

plt.hist(profitlist)
#plt.show()




