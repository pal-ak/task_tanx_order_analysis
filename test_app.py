import os
import sys
import pandas as pd

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../app')))

from app import load_data, prepare_data, compute_monthly_revenue, compute_product_revenue, compute_customer_revenue, top_10_customers_by_revenue

def test_monthly_revenue():
    try:
        orders_df = prepare_data(load_data('app/orders.csv'))
        monthly_revenue = compute_monthly_revenue(orders_df)
        print(monthly_revenue)  # Debugging: Print calculated monthly revenue
        assert monthly_revenue[monthly_revenue['month_year'] == pd.Period('2023-01', freq='M')]['total_revenue'].values[0] == 1250
        assert monthly_revenue[monthly_revenue['month_year'] == pd.Period('2023-02', freq='M')]['total_revenue'].values[0] == 600
        assert monthly_revenue[monthly_revenue['month_year'] == pd.Period('2023-03', freq='M')]['total_revenue'].values[0] == 1600
        assert monthly_revenue[monthly_revenue['month_year'] == pd.Period('2023-04', freq='M')]['total_revenue'].values[0] == 1450
        print("test_monthly_revenue: PASSED")
    except AssertionError as e:
        print("test_monthly_revenue: FAILED")
        raise e

def test_product_revenue():
    try:
        orders_df = prepare_data(load_data('app/orders.csv'))
        product_revenue = compute_product_revenue(orders_df)
        print(product_revenue)  # Debugging: Print calculated product revenue
        assert product_revenue[product_revenue['product_id'] == 101]['total_revenue'].values[0] == 700
        assert product_revenue[product_revenue['product_id'] == 102]['total_revenue'].values[0] == 900
        assert product_revenue[product_revenue['product_id'] == 103]['total_revenue'].values[0] == 1800
        assert product_revenue[product_revenue['product_id'] == 104]['total_revenue'].values[0] == 1500
        print("test_product_revenue: PASSED")
    except AssertionError as e:
        print("test_product_revenue: FAILED")
        raise e

def test_customer_revenue():
    try:
        orders_df = prepare_data(load_data('app/orders.csv'))
        customer_revenue = compute_customer_revenue(orders_df)
        print(customer_revenue)  # Debugging: Print calculated customer revenue
        assert customer_revenue[customer_revenue['customer_id'] == 1]['total_revenue'].values[0] == 1100
        assert customer_revenue[customer_revenue['customer_id'] == 2]['total_revenue'].values[0] == 950
        assert customer_revenue[customer_revenue['customer_id'] == 3]['total_revenue'].values[0] == 700
        assert customer_revenue[customer_revenue['customer_id'] == 4]['total_revenue'].values[0] == 1050
        assert customer_revenue[customer_revenue['customer_id'] == 5]['total_revenue'].values[0] == 1100  # Corrected value
        print("test_customer_revenue: PASSED")
    except AssertionError as e:
        print("test_customer_revenue: FAILED")
        raise e

def test_top_10_customers():
    try:
        orders_df = prepare_data(load_data('app/orders.csv'))
        customer_revenue = compute_customer_revenue(orders_df)
        top_10_customers = top_10_customers_by_revenue(customer_revenue)
        print(top_10_customers)  # Debugging: Print top 10 customers by revenue
        assert top_10_customers.iloc[0]['customer_id'] == 1
        assert top_10_customers.iloc[1]['customer_id'] == 5
        assert top_10_customers.iloc[2]['customer_id'] == 4
        assert top_10_customers.iloc[3]['customer_id'] == 2
        assert top_10_customers.iloc[4]['customer_id'] == 3
        print("test_top_10_customers: PASSED")
    except AssertionError as e:
        print("test_top_10_customers: FAILED")
        raise e

if __name__ == "__main__":
    test_monthly_revenue()
    test_product_revenue()
    test_customer_revenue()
    test_top_10_customers()
