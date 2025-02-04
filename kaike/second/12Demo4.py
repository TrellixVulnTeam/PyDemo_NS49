from gevent import monkey
monkey.patch_all()
import gevent,time,requests
from bs4 import BeautifulSoup
from gevent.queue import Queue
import csv
csv_file = open('books.csv','w',newline='',encoding='utf-8')
writer = csv.writer(csv_file)

url = 'https://book.douban.com/top250'
pageSize = 25
startPage = 0
start = time.time()
headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
work = Queue()
for i in range(3):
    params = {
        'start': startPage + i * pageSize
    }
    work.put_nowait(params)
def crawler():
    while not work.empty():
        param = work.get_nowait()
        res = requests.get(url, params=param, headers=headers)
        res.encoding='utf-8'
        books_html = BeautifulSoup(res.text, 'html.parser')
        indent_div = books_html.find('div',class_='indent')
        list_books = indent_div.find_all('table')
        for book in list_books:
            title_div = book.find('div',class_='pl2')
            tag_a = title_div.find('a')
            title = tag_a.text.replace(' ', '').replace('\n', '')
            tag_p = book.find('p',class_='pl')
            author = tag_p.text.replace(' ', '').replace('\n', '')
            tag_span = book.find('span',class_='rating_nums')
            rating_nums = tag_span.text.replace(' ', '').replace('\n', '')
            print(title, author, rating_nums)
            writer.writerow([title, author, rating_nums])
tasks_list  = [ ]
for x in range(3):
    task = gevent.spawn(crawler)
    tasks_list.append(task)
gevent.joinall(tasks_list)
end = time.time()
print(end-start)
csv_file.close()