# Quantium Software Engineering Simulation

## Overview
This project was completed as part of the Quantium Software Engineering Virtual Experience.
The aim was to explore how a price increase affected sales of Pink Morsels. Starting from raw CSV files, I processed the data, built a simple dashboard using Dash and used it to visualise trends over time.

---

## What it does
- Combines and cleans multiple CSV files using pandas  
- Filters for Pink Morsel sales and calculates total sales  
- Displays sales trends over time in a Dash dashboard  
- Lets you filter the data by region (North, East, South, West, or All)  
- Includes a small test suite to check the app is working as expected  

---

## Key finding
Sales were noticeably higher after the price increase on January 15, 2021, suggesting that the higher price didn’t reduce demand and may have improved overall revenue.

---

## Setup
- Python 3.9 virtual environment  
- Installed dependencies:
  - dash  
  - pandas  
  - dash[testing]  
  - pytest  

---

## Running the app
```bash
python app.py
