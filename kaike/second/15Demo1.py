#本练习需要运用scrapy的知识，爬取豆瓣图书TOP250前2页的书籍（50本）的短评数据（包括书名、评论ID、短评内容），并存储成Excel。 网址链接：https://book.douban.com/top250 需要修改 cooments_spider.py 、items.py、settings.py、main.py文件


import scrapy,bs4
from items import DoubanCommentsItem

class DoubantopSpider(scrapy.Spider):
    name = 'douban_comments_spider'
    allowed_domains = ['book.douban.com']
    start_urls = []
    for x in range(2):
        url = 'https://book.douban.com/top250?start=' + str(x * 25)
        start_urls.append(url)

    def parse(self, response):
        soup = bs4.BeautifulSoup(response.text,'html.parser')
        datas = soup.find_all('tr',class_='item')
        for data in datas:
            book_url = data.find_all('a')[1]['href']
            comment_url = book_url+'comments/'
            yield scrapy.Request(comment_url,callback=self.parse_comment)

    def parse_comment(self,response):
        soup = bs4.BeautifulSoup(response.text,'html.parser')
        book_name = soup.find('div',id='content').text.split()[0]
        datas = soup.find_all('div',class_='comment')
        for data in datas:
            item = DoubanCommentsItem()
            item['book_name'] = book_name
            item['ID_name'] = data.find_all('a')[1].text
            item['comment'] = data.find('span',class_='short').text
            yield item