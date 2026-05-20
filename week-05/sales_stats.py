import statistics

# User-defined function
def analyze_sales(analyst, region, sales):

    mean = statistics.mean(sales)
    median = statistics.median(sales)
    mode = statistics.mode(sales)
    stdev = statistics.stdev(sales)

    total = sum(sales)
    high = max(sales)
    low = min(sales)

    return mean, median, mode, stdev, total, high, low


# Collect user input
analyst = input("Analyst name: ")
region = input("Region: ")

print("Enter daily sales for 7 days:")

sales = [float(input(f" Day {i+1}: $")) for i in range(7)]


# Call function
mean, median, mode, stdev, total, high, low = analyze_sales(
    analyst, region, sales
)


# Print report using f-string
print(f"""
======= Weekly Sales Statistics Report =======

Analyst : {analyst}
Region  : {region}

Data : {sales}

-----------------------------------------------

Total Revenue : ${total:.2f}
Mean Average  : ${mean:.2f}
Median        : ${median:.2f}
Mode          : ${mode:.2f}
Std Deviation : ${stdev:.2f}
Highest Day   : ${high:.2f}
Lowest Day    : ${low:.2f}

===============================================
""")