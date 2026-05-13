# Sales records
sales_data = [
    ('Marcus Webb', 'East', 4250.00),
    ('Priya Sharma', 'West', 5875.50),
    ('DeShawn Carter', 'East', 3100.75),
    ('LaTonya Rivers', 'South', 6420.00),
    ('Bob Nguyen', 'West', 4980.25),
]

# Variable to track total sales
total_sales = 0

# Loop through sales records
for name, region, sales in sales_data:

    # Print formatted summary
    print(f"{name} ({region}): ${sales:,.2f}")

    # Check for top performers
    if sales > 5000:
        print("^ Top performer!")

    # Add sales to total
    total_sales += sales

# Print overall total sales
print(f"\nOverall Total Sales: ${total_sales:,.2f}")