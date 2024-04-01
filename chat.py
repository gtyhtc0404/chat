# txt,wore,記事本,subline檔案在儲存的時候會存入'有關於編碼'的資料(看不出來 印出會多'\ufeff') 所以要加上'-sig'來去掉
def read_file(filename):
    chat = []
    with open(filename, 'r', encoding='utf-8-sig') as f:  
        for line in f:
            chat.append(line.strip())
    return chat

# 先宣告person(None=尚沒有值)避免讀取的txt對話第一行不是人名 而使程式當掉
def convert(chat):
    new_chat = []
    person = None  
    for line in chat:
        if line == 'Allen':
            person = 'Allen'
            continue
        elif line == 'Tom':
            person = 'Tom'
            continue
        if person:  # person有值才會繼續執行(None=尚沒有值 不會繼續執行)
            new_chat.append(person + ':' + line)
    return new_chat

def write_file(filename, chat):
    with open(filename, 'w') as f:
        for line in chat:
            f.write(line + '\n')


def main():
    chat = read_file('input.txt')
    chat = convert(chat)
    write_file('output.txt', chat)

main()