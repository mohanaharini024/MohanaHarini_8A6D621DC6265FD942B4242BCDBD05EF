def linearSearchProduct(productList, targetProduct):
  indices = []
  for index, product in enumerate(productList):
   if product == targetProduct: 
    indices. append(index)
  return indices 

#Example usage:
products = ["shoes","boots","loafers","shoes","sandals","shoes"]
target = "shoes"
target2 = 'apple'
result = linearSearchProduct(products, target)
print(result) 
