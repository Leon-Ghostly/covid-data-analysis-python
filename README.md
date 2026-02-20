# COVID-19 Data Cleaning and Automated Analysis with Python

This project demonstrates how to clean, process, and analyze real-world datasets using Python and pandas.

It simulates a real freelance data analysis task where a client provides a raw CSV file and needs:

- Cleaned data
- Statistical insights
- Aggregated results

---

## Technologies Used

- Python
- Pandas

---

## Dataset

Real COVID-19 dataset containing:

- Country
- Confirmed cases
- Deaths
- Recovered
- Active cases
- Incident rate
- Case fatality ratio

---

## Features

✔ Data loading from CSV  
✔ Intelligent data cleaning  
✔ Handling missing values  
✔ Removal of duplicates  
✔ Automated statistical summary  
✔ Top 10 countries by confirmed cases  
✔ Exporting cleaned dataset  

---

## Example Output

Top 10 countries by confirmed cases:

US  
India  
Brazil  
Russia  
France  
United Kingdom  
Turkey  
Italy  
Spain  
Germany  

---

## Data Cleaning Strategy

Instead of removing all missing values, the script keeps critical data and only removes rows where:

- Country is missing
- Confirmed cases are missing

This prevents data loss and keeps the dataset meaningful.

---

## How to Run

1. Clone this repository

git clone https://github.com/Leon-Ghostly/covid-data-analysis-python

2. Install dependencies

pip install pandas


3. Run the script

python csv_data_analyzer.py


---

## Output

The script generates:

cleaned_data.csv


A ready-to-use dataset for further analysis or reporting.

---

## Real-World Use Case

This type of solution can be used for:

- Sales reports
- Customer databases
- Financial data
- Marketing analytics
- Inventory datasets

---

##  Author

Python Data Analyst focused on:

- Data cleaning
- Automation
- Business insights
