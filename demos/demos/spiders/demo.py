import scrapy

class DemoSpider(scrapy.Spider):
    name = 'demo'
    # allowed_domains = ['python123.io']
    # start_urls = ['http://python123.io/ws/demo.html']

    def start_requests(self):
        urls = [
            # 'https://www.baidu.com/'
            'http://quote.eastmoney.com/center/gridlist.html'
        ]

        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse,headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'})

    def parse(self,response):
        for href in response.css('a::attr(href)').extract():
            print(href)
        fname = response.url.split('/')[-1]
        print(fname,response.url)
        with open(fname,'wb') as f:
            f.write(response.body)
        self.log('Saved file %s.' % fname)

    def gen(self,n):
        for i in range(n):
            yield i**2

if __name__ == '__main__':
    demo = DemoSpider()
    # for i in demo.gen(5):
    #     print(i, '', end='')
        # demo.parse()