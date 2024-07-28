import unittest
import pandas as pd
from app import load_data, prepare_data, compute_monthly_revenue, compute_product_revenue, compute_customer_revenue, top_10_customers_by_revenue

class TestApp(unittest.TestCase):
    def setUp(self):
        # sample data for testing
        data = {
            'order_id': [1, 2, 3, 4],
            'customer_id': [1, 1, 2, 2],
            'order_date': ['01-01-2023', '15-02-2023', '10-03-2023', '25-04-2023'],
            'product_id': [101, 102, 103, 104],
            'product_name': ['Product A', 'Product B', 'Product C', 'Product D'],
            'product_price': [100, 200, 300, 400],
            'quantity': [2, 1, 3, 4]
        }
        self.df = pd.DataFrame(data)
        self.df = prepare_data(self.df)
    
    def test_load_data(self):
        df = load_data('orders.csv')
        self.assertIsNotNone(df)

    def test_prepare_data(self):
        self.assertIn('total_revenue', self.df.columns)
    
    def test_compute_monthly_revenue(self):
        monthly_revenue = compute_monthly_revenue(self.df)
        self.assertEqual(monthly_revenue.shape[0], 4)
    
    def test_compute_product_revenue(self):
        product_revenue = compute_product_revenue(self.df)
        self.assertEqual(product_revenue.shape[0], 4)
    
    def test_compute_customer_revenue(self):
        customer_revenue = compute_customer_revenue(self.df)
        self.assertEqual(customer_revenue.shape[0], 2)
    
    def test_top_10_customers_by_revenue(self):
        customer_revenue = compute_customer_revenue(self.df)
        top_customers = top_10_customers_by_revenue(customer_revenue)
        self.assertEqual(top_customers.shape[0], 2)

if __name__ == '__main__':
    unittest.main()
