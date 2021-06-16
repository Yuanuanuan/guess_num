import random
start = input('請輸入開始值')
end = input('請輸入結束值')
start = int(start)
end = int(end)
r = random.randint(start, end)
count = 0
while True:
	num = input('請猜數字')
	num = int(num)
	count += 1
	if num == r:
		print('你猜對了!')
		print('這是你猜的第', count, '次') 
		break
	elif num > r:
		print('太大了')
	elif num < r:
		print('太小了')
	print('這是你猜的第', count, '次') 