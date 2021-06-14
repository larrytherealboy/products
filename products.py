products = []
while True:
	 name = input('請輸入商品名稱: ')
	 if name == 'q':
	 	break
	 price = input('請輸入商品價格: ')
	 # 縮寫 p = [name, price]
	 # 縮寫 p.append(name)
	 # 縮寫 p.append(price) , p 為小清單
	 products.append([name, price]) # products 為大清單
print(products)

for p in products:
	print(p[0],'的價格是', p[1])