class ProductAnalyzer:
    def __init__(self, sales_data):
        self.sales_data = sales_data

    def total_sales_per_day(self):
        sales_per_day = {}
        for sale in self.sales_data:
            day = sale['date']
            if day not in sales_per_day:
                sales_per_day[day] = 0
            sales_per_day[day] += sale['quantity']
        return sales_per_day

    def most_sold_product(self):
        product_sales = {}
        for sale in self.sales_data:
            product = sale['product']
            if product not in product_sales:
                product_sales[product] = 0
            product_sales[product] += sale['quantity']
        most_sold = max(product_sales, key=product_sales.get)
        return most_sold

    def highest_spending_customer(self):
        customer_spending = {}
        for sale in self.sales_data:
            customer = sale['customer']
            spending = sale['quantity'] * sale['price']
            if customer not in customer_spending:
                customer_spending[customer] = 0
            customer_spending[customer] += spending
        highest_spender = max(customer_spending, key=customer_spending.get)
        return highest_spender

    def products_sold_above_quantity(self, threshold=1):
        above_threshold_products = set()
        for sale in self.sales_data:
            product = sale['product']
            quantity = sale['quantity']
            if quantity > threshold:
                above_threshold_products.add(product)
        return list(above_threshold_products)
