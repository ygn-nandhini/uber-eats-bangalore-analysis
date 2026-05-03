# Uber Eats Bangalore Restaurant Analysis

## Project Overview
This project analyzes Uber Eats Bangalore restaurant data 
to build a decision support system that answers critical 
business questions using Python and SQL, presenting results 
as clean tabular DataFrame outputs in Streamlit.

## Tech Stack
- Python
- MySQL
- Streamlit
- Pandas

## Project Structure
streamlit_project/
├── app.py
├── .env (not uploaded - contains password)
├── .gitignore
└── README.md

## How to Run

### 1. Install Libraries:
pip install streamlit mysql-connector-python pandas python-dotenv

### 2. Create .env file:
DB_PASSWORD=your_password

### 3. Run App:
streamlit run app.py

## Business Questions Answered

### Restaurant Analysis:
1. Which locations have highest avg ratings?
2. Which locations are over-saturated?
3. Does online ordering improve ratings?
4. Does table booking correlate with ratings?
5. What price range delivers best satisfaction?
6. Which cuisines are most common?
7. Which cuisines have highest avg ratings?
8. Which locations show high demand but lower ratings?
9. Do restaurants with online ordering and table booking perform better?
10. What combination of factors maximizes success?

### Order Analysis:
1. Which restaurant has most orders?
2. Total revenue per restaurant?
3. Most popular payment method?
4. Overall average order value?
5. Which month had highest orders?
6. Which restaurant has highest avg order value?
7. Daily average order value?
8. How many orders per year?

## Dataset
- Source: Uber Eats Bangalore Dataset
- Restaurants: 23,012 records
- Orders: 25,000 records

## Key Findings
- Luxury restaurants highest rating: 4.18
- Mid range most popular segment
- Online ordering improves ratings
- UPI most popular payment method