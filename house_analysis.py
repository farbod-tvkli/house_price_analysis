import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("house.csv")

print(df.head())
print(df["Price"].mean())
print(df["Price"].max())
print(df["Price"].min())


city_mean = df.groupby("City")["Price"].mean().sort_values(ascending=False)


house_count = df["City"].value_counts()


plt.figure()
plt.scatter(df["Area"], df["Price"])
plt.title("The relationshib between house size and house price")
plt.xlabel("City")
plt.ylabel("Price")
plt.savefig("Relation_Area_Price.png")
plt.show()


plt.figure()
plt.scatter(df["Age"], df["Price"])
plt.title("The relationship between house age and house price ")
plt.xlabel("Age")
plt.ylabel("price")
plt.savefig("Relation_Age_Price.png")
plt.show()


plt.figure()
city_mean.plot(kind="bar")
plt.title("Housing prices in each city")
plt.xlabel("City")
plt.ylabel("Price")
plt.savefig("House_Price_city.png")
plt.show()

plt.figure()
house_count.plot(kind="bar")
plt.title("Number of housing in each city")
plt.xlabel("City")
plt.ylabel("Number")
plt.savefig("House_count_city.png")
plt.show()



