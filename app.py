import streamlit as st
import mysql.connector
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

connect = mysql.connector.connect(
    host="localhost",
    user="root",
    password=os.getenv("DB_PASSWORD"),
    database="my_project",
    auth_plugin='mysql_native_password'
)

cursor = connect.cursor(buffered=True)

st.title("Restaurant Analysis Dashboard")


page = st.sidebar.selectbox("Choose Page", [
    "Restaurant Dashboard",
    "Restaurant Q&A",
    "Order Q&A"
])


if page == "Restaurant Dashboard":
    option = st.selectbox("Choose Analysis", [
        "Top Locations",
        "Online Order Analysis",
        "Table Booking Analysis"
    ])

    if option == "Top Locations":
        cursor.execute("""
            SELECT location, COUNT(*), AVG(rate)
            FROM restaurants
            GROUP BY location
        """)
        df = pd.DataFrame(cursor.fetchall(), columns=["Location", "Total", "Avg Rating"])
        st.dataframe(df)

    elif option == "Online Order Analysis":
        cursor.execute("""
            SELECT online_order, AVG(rate), COUNT(*)
            FROM restaurants
            GROUP BY online_order
        """)
        df = pd.DataFrame(cursor.fetchall(), columns=["Online Order", "Avg Rating", "Count"])
        st.dataframe(df)

    elif option == "Table Booking Analysis":
        cursor.execute("""
            SELECT book_table, AVG(rate), COUNT(*)
            FROM restaurants
            GROUP BY book_table
        """)
        df = pd.DataFrame(cursor.fetchall(), columns=["Table Booking", "Avg Rating", "Count"])
        st.dataframe(df)


elif page == "Restaurant Q&A":
    st.header("Restaurant Business Questions")

    qa_option = st.selectbox("Choose Question", [
        "Q1: Which locations have highest avg ratings?",
        "Q2: Which locations are over-saturated?",
        "Q3: Does online ordering improve ratings?",
        "Q4: Does table booking correlate with ratings?",
        "Q5: What price range delivers best satisfaction?",
        "Q6: Which cuisines are most common?",
        "Q7: Which cuisines have highest avg ratings?",
        "Q8: Which locations show high demand but lower ratings?",
        "Q9: Do restaurants with online ordering + table booking perform better?",
        "Q10: What combination of factors maximizes success?"
    ])

    if qa_option == "Q1: Which locations have highest avg ratings?":
        cursor.execute("""
            SELECT location, AVG(rate) AS avg_rating
            FROM restaurants
            GROUP BY location
            ORDER BY avg_rating DESC
            LIMIT 5
        """)
        df = pd.DataFrame(cursor.fetchall(), columns=["Location", "Avg Rating"])
        st.dataframe(df)

    elif qa_option == "Q2: Which locations are over-saturated?":
        cursor.execute("""
            SELECT location, COUNT(*) AS total_restaurants
            FROM restaurants
            GROUP BY location
            ORDER BY total_restaurants DESC
            LIMIT 5
        """)
        df = pd.DataFrame(cursor.fetchall(), columns=["Location", "Total Restaurants"])
        st.dataframe(df)

    elif qa_option == "Q3: Does online ordering improve ratings?":
        cursor.execute("""
            SELECT online_order, AVG(rate) AS avg_rating
            FROM restaurants
            GROUP BY online_order
        """)
        df = pd.DataFrame(cursor.fetchall(), columns=["Online Order", "Avg Rating"])
        st.dataframe(df)

    elif qa_option == "Q4: Does table booking correlate with ratings?":
        cursor.execute("""
            SELECT book_table, AVG(rate) AS avg_rating
            FROM restaurants
            GROUP BY book_table
        """)
        df = pd.DataFrame(cursor.fetchall(), columns=["Table Booking", "Avg Rating"])
        st.dataframe(df)

    
    elif qa_option == "Q5: What price range delivers best satisfaction?":
        cursor.execute("""
            SELECT 
                CASE 
                    WHEN cost <= 300 THEN 'Budget'
                    WHEN cost <= 600 THEN 'Mid'
                    WHEN cost <= 1000 THEN 'Premium'
                    ELSE 'Luxury'
                END AS price_segment,
                ROUND(AVG(rate), 2) AS avg_rating,
                COUNT(*) AS total_restaurants
            FROM restaurants
            GROUP BY price_segment
            ORDER BY avg_rating DESC
        """)
        df = pd.DataFrame(cursor.fetchall(), 
             columns=["Price Segment", "Avg Rating", "Total Restaurants"])
        st.dataframe(df)

    elif qa_option == "Q6: Which cuisines are most common?":
        cursor.execute("""
            SELECT cuisines, COUNT(*) AS total
            FROM restaurants
            GROUP BY cuisines
            ORDER BY total DESC
            LIMIT 5
        """)
        df = pd.DataFrame(cursor.fetchall(), columns=["Cuisine", "Total"])
        st.dataframe(df)

    elif qa_option == "Q7: Which cuisines have highest avg ratings?":
        cursor.execute("""
            SELECT cuisines, AVG(rate) AS avg_rating
            FROM restaurants
            GROUP BY cuisines
            ORDER BY avg_rating DESC
            LIMIT 5
        """)
        df = pd.DataFrame(cursor.fetchall(), columns=["Cuisine", "Avg Rating"])
        st.dataframe(df)

    elif qa_option == "Q8: Which locations show high demand but lower ratings?":
        cursor.execute("""
            SELECT location, COUNT(*) AS total_restaurants,
                   AVG(rate) AS avg_rating
            FROM restaurants
            GROUP BY location
            ORDER BY total_restaurants DESC
            LIMIT 10
        """)
        df = pd.DataFrame(cursor.fetchall(), columns=["Location", "Total Restaurants", "Avg Rating"])
        st.dataframe(df)

    elif qa_option == "Q9: Do restaurants with online ordering + table booking perform better?":
        cursor.execute("""
            SELECT online_order, book_table,
                   COUNT(*) AS total_restaurants,
                   AVG(rate) AS avg_rating
            FROM restaurants
            GROUP BY online_order, book_table
        """)
        df = pd.DataFrame(cursor.fetchall(), columns=["Online Order", "Table Booking", "Total", "Avg Rating"])
        st.dataframe(df)

    elif qa_option == "Q10: What combination of factors maximizes success?":
        cursor.execute("""
            SELECT location, cuisines, online_order, book_table,
                   cost, AVG(rate) AS avg_rating,
                   COUNT(*) AS total_restaurants
            FROM restaurants
            GROUP BY location, cuisines, online_order, book_table, cost
            ORDER BY avg_rating DESC
            LIMIT 10
        """)
        df = pd.DataFrame(cursor.fetchall(), columns=["Location", "Cuisine", "Online Order", "Table Booking", "Cost", "Avg Rating", "Total"])
        st.dataframe(df)


elif page == "Order Q&A":
    st.header("Order Data Analysis")

    order_option = st.selectbox("Choose Question", [
        "Q1: Which restaurant has the most orders?",
        "Q2: Total revenue per restaurant?",
        "Q3: Most popular payment method?",
        "Q4: Overall average order value?",
        "Q5: Which month had highest orders?",
        "Q6: Which restaurant has highest avg order value?",
        "Q7: Daily average order value?",
        "Q8: How many orders per year?"
    ])

    if order_option == "Q1: Which restaurant has the most orders?":
        cursor.execute("""
            SELECT restaurant_name, COUNT(*) AS total_orders
            FROM orders
            GROUP BY restaurant_name
            ORDER BY total_orders DESC
            LIMIT 10
        """)
        df = pd.DataFrame(cursor.fetchall(), columns=["Restaurant", "Total Orders"])
        st.dataframe(df)

    elif order_option == "Q2: Total revenue per restaurant?":
        cursor.execute("""
            SELECT restaurant_name, SUM(order_value) AS total_revenue
            FROM orders
            GROUP BY restaurant_name
            ORDER BY total_revenue DESC
            LIMIT 10
        """)
        df = pd.DataFrame(cursor.fetchall(), columns=["Restaurant", "Total Revenue"])
        st.dataframe(df)

    elif order_option == "Q3: Most popular payment method?":
        cursor.execute("""
            SELECT payment_method, COUNT(*) AS total_orders
            FROM orders
            GROUP BY payment_method
            ORDER BY total_orders DESC
        """)
        df = pd.DataFrame(cursor.fetchall(), columns=["Payment Method", "Total Orders"])
        st.dataframe(df)

    elif order_option == "Q4: Overall average order value?":
        cursor.execute("""
            SELECT ROUND(AVG(order_value), 2) AS avg_order_value
            FROM orders
        """)
        df = pd.DataFrame(cursor.fetchall(), columns=["Avg Order Value"])
        st.dataframe(df)

    elif order_option == "Q5: Which month had highest orders?":
        cursor.execute("""
            SELECT MONTHNAME(order_date) AS month,
                   COUNT(*) AS total_orders
            FROM orders
            GROUP BY MONTH(order_date), MONTHNAME(order_date)
            ORDER BY total_orders DESC
        """)
        df = pd.DataFrame(cursor.fetchall(), columns=["Month", "Total Orders"])
        st.dataframe(df)

    elif order_option == "Q6: Which restaurant has highest avg order value?":
        cursor.execute("""
            SELECT restaurant_name,
                   ROUND(AVG(order_value), 2) AS avg_order_value
            FROM orders
            GROUP BY restaurant_name
            ORDER BY avg_order_value DESC
            LIMIT 10
        """)
        df = pd.DataFrame(cursor.fetchall(), columns=["Restaurant", "Avg Order Value"])
        st.dataframe(df)

    elif order_option == "Q7: Daily average order value?":
        cursor.execute("""
            SELECT order_date,
                   ROUND(AVG(order_value), 2) AS avg_order_value
            FROM orders
            GROUP BY order_date
            ORDER BY order_date
        """)
        df = pd.DataFrame(cursor.fetchall(), columns=["Date", "Avg Order Value"])
        st.dataframe(df)

    elif order_option == "Q8: How many orders per year?":
        cursor.execute("""
            SELECT YEAR(order_date) AS year,
                   COUNT(*) AS total_orders
            FROM orders
            GROUP BY YEAR(order_date)
            ORDER BY year
        """)
        df = pd.DataFrame(cursor.fetchall(), columns=["Year", "Total Orders"])
        st.dataframe(df)