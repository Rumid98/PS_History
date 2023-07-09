n = int(input())
book_dic = {}
max_sell = 0
tmp_list = []

for _ in range(n):
    book_title = input().strip()
    if book_title in book_dic:
        book_dic[book_title] += 1
    else:
        book_dic[book_title] = 1

book_title_list = list(book_dic.keys())
for title in book_title_list:
    tmp_list.append((title, book_dic[title]))
tmp_list.sort(key=lambda x: x[0])  # 제목으로 먼저 sort
tmp_list.sort(key=lambda x: -x[1])  # 이후 팔린 개수로 sort
print(tmp_list[0][0])
