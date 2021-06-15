#檢查檔案在不在,如果在,就讀取
import os # operating system 作業系統

# 以filename為參數, 取代 'products.csv', 以利讀取不同檔案
def read_file(filename):  
	products = []  # 不管有沒有讀到檔案,都必須要有空清單,因為等一下會用到
	with open(filename, 'r', encoding = 'utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue            # continue 跟 break 依樣只能寫在迴圈裡,continue 是跳到下一迴的意思
			name, price = line.strip().split(',') # split 切割完的結果是清單
			products.append([name, price]) #將小清單 [name, price] 裝入大清單 products	
	return products
			
			#11 縮寫 s = line.strip().split(',')  s 為清單
			#   縮寫 name = s[0]
			#   縮寫 price = s[1] 

#讓使用者輸入
def user_input(products):
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
	return products

#印出購買紀錄
def print_products(products):
	for p in products:
		print(p[0],'的價格是', p[1])

#寫入檔案
# read 'r' 讀取模式
# write 'w' 寫入模式
def write_file(filename, products):
	with open(filename, 'w', encoding = 'utf-8') as f:  # 寫入檔案時加入 encoding = 'utf-8' 解決中文亂碼問題
		f.write('商品,價格\n')
		for p in products:
			f.write(p[0] + ',' + str(p[1]) + '\n') # csv 檔,通常用逗點做區隔
			                                       # f.write 寫入
			                                       # 因為字串無法與整數(price)做合併,所以price必須先轉換成字串str(p[1])

	# open 完要 close,但 with 會幫你自動close, 且程式碼須寫在 with 架構裡面

# main function 主要的執行程式碼
def main():
	filename = 'products.csv'
	if os.path.isfile(filename):  #相同資料夾下，有無 'products.csv' 檔案
		products = read_file(filename)	
		print('yeah! 找到檔案了!')
	else:
		print('找不到檔案...')

	products = user_input(products)
	print_products(products)
	write_file('products.csv', products)

main()

# 重點: 
# 理想的 function 應該"只做一件事", 所以 refactor(重構程式)的核心概念, 就是把程式不斷改寫, 寫成越來越小的function, 讓 function "盡量"只做一件事
