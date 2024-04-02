chat = []
with open('3.txt', 'r', encoding='utf-8-sig') as f:
    for line in f:
        chat.append(line.strip())
for d in chat:
    s = d.split(' ')  # 資料split之後會自動變成一份清單>>s現在是一份清單
    time = s[0][:5]  # 清單內容為一組字串，字串可以當清單用，故擷取s[0]的前五個字當time
    name = s[0][5:]  # 故擷取s[0]的第五個字以後的資料當name
    print(name)
