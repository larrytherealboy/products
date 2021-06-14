products = []
while True:
	 name = input('請輸入商品名稱: ')
	 if name == 'q':
	 	break
	 price = input('請輸入商品價格: ')
	 price = int(price)
	 # 縮寫 p = [name, price]
	 # 縮寫 p.append(name)
	 # 縮寫 p.append(price) , p 為小清單
	 products.append([name, price]) # products 為大清單
print(products)

for p in products:
	print(p[0],'的價格是', p[1])

# 'abc' + '123' = 'abc123'
# 'abc' * 3 = 'abcabcabc'

# read 'r' 讀取模式
# write 'w' 寫入模式
with open('products.csv', 'w', encoding = 'utf-8') as f:  # 寫入檔案時加入 encoding = 'utf-8' 解決中文亂碼問題
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n') # csv 檔,通常用逗點做區隔
		                                       # f.write 寫入
		                                       # 因為字串無法與整數(price)做合併,所以price必須先轉換成字串str(p[1])

# open 完要 close,但 with 會幫你自動close, 且程式碼須寫在 with 架構裡面