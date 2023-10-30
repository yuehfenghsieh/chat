#讀取檔案
def read_file(filename):
	lines = []
	with open(filename, 'r', encoding='utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return(lines)

#格式轉換
def convert(lines):
	count_Allen_words = 0
	count_Allen_sticker = 0 
	count_Allen_image = 0
	count_Viki_words = 0
	count_Viki_sticker = 0 
	count_Viki_image = 0
	for line in lines:
		s = line.split(' ')
		if s[1] == 'Allen':
			if s[2] == '圖片':
				count_Allen_image += 1
			elif s[2] == '貼圖':
				count_Allen_sticker += 1
			else:
				for w in s[2:]:
					count_Allen_words += len(w)

		elif s[1] == 'Viki':
			if s[2] == '圖片':
				count_Viki_image += 1
			elif s[2] == '貼圖':
				count_Viki_sticker += 1
			else:
				for w in s[2:]:
					count_Viki_words += len(w)
	print('Allen說了', count_Allen_words, '個字，傳了', count_Allen_image, '張圖片，傳了', count_Allen_sticker, '張貼圖')
	print('Viki說了', count_Viki_words, '個字，傳了', count_Viki_image, '張圖片，傳了', count_Viki_sticker, '張貼圖')

#寫入檔案
def write_file(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')

def main():
	lines = read_file('LINE-Viki.txt')
	lines = convert(lines)
	#write_file('output.txt', lines)


main()