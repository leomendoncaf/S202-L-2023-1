from database import Database
from writeAJson import writeAJson
import ProductAnalyzer
import dataset

# Exemplo de dados de vendas
sales_data = [dataset]

# Criar uma instância da classe ProductAnalyzer
analyzer = ProductAnalyzer(sales_data)

# Exemplo de uso das funções
total_sales_by_day = analyzer.total_sales_per_day()
most_sold_product = analyzer.most_sold_product()
highest_spending_customer = analyzer.highest_spending_customer()
above_threshold_products = analyzer.products_sold_above_quantity(1)

print("Total de vendas por dia:", total_sales_by_day)
print("Produto mais vendido:", most_sold_product)
print("Cliente que mais gastou:", highest_spending_customer)
print("Produtos com quantidade vendida acima de 1 unidade:", above_threshold_products)
