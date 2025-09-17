import matplotlib.pyplot as plt

# Sales data (in thousands)
sales_data = [25, 32, 29, 35, 41, 40, 45, 38, 50, 55, 60, 70]

# Month names
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

# 1. Calculate total sales using loop
total_sales = 0
for sale in sales_data:
    total_sales += sale

# 2. Calculate average sales
average_sales = total_sales / len(sales_data)

# 3. Find the month with the highest sales
highest_sales = sales_data[0]
highest_month_index = 0

for i in range(len(sales_data)):
    if sales_data[i] > highest_sales:
        highest_sales = sales_data[i]
        highest_month_index = i

highest_month = months[highest_month_index]

# Display results
print("Total Sales (in thousands):", total_sales)
print("Average Sales (in thousands):", round(average_sales, 2))
print("Highest Sales (in thousands):", highest_sales, "in", highest_month)

# 4. Plot sales data
plt.figure(figsize=(10, 6))
plt.plot(months, sales_data, marker="o", label="Monthly Sales")
plt.title("Monthly Sales Data")
plt.xlabel("Months")
plt.ylabel("Sales (in thousands)")
plt.grid(True)

# Highlight the highest sales month
plt.scatter(highest_month, highest_sales, color="red", s=120, label="Highest Sales")
plt.legend()

plt.show()
