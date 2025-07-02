import pandas as pd
import numpy as np

num_product = int(input("Enter number of product : "))
empty = []

for i in range(num_product):
     print(f'You have entered {i + 1} Products')
     product_name = input("Enter product name :")
     product_price = int(input("Enter product price :"))
     product_stock = int(input("Enter Product Stock :"))

     sham = {
          "product_name" : product_name,
          "product_price" : product_price,
          "product_stock" : product_stock
      }
     empty.append(sham)


shankar = pd.DataFrame(empty, index=range(num_product))
print(shankar)