
def read_file(filename):
    chat = []
    with open(filename, 'r', encoding='utf-8-sig') as f:  
        for line in f:
            chat.append(line.strip())
    return chat


def convert(chat):
    new_chat = []  
    Allen_word_count = 0  # Allen所打的字的計數
    Allen_sticker_count = 0 # 所用的貼圖計數
    Allen_image_count = 0  # 所用的圖片計數
    Viki_word_count = 0
    Viki_sticker_count =0
    Viki_image_count =0
    for line in chat:
        s = line.split(' ')  # 將資料用空格來做切割
        time = s[0]
        name = s[1]
        if name == 'Allen':
            if s[2] == '貼圖':
                Allen_sticker_count += 1
            elif s[2] == '圖片':
                Allen_image_count +=1
            else:
                for d in s[2:]:
                    Allen_word_count += len(d)
        elif name == 'Viki':
            if s[2] == '貼圖':
                Viki_sticker_count += 1
            elif s[2] == '圖片':
                Viki_image_count +=1
            else:
                for d in s[2:]:
                    Viki_word_count += len(d)
    print('Allen說了', Allen_word_count, '個字,傳了', Allen_sticker_count, '張貼圖和', Allen_image_count, '張圖片')
    print('Viki說了', Viki_word_count, '個字,傳了', Viki_sticker_count, '張貼圖和', Viki_image_count, '張圖片')


def main():
    chat = read_file('LINE-Viki.txt')
    convert(chat)


main()