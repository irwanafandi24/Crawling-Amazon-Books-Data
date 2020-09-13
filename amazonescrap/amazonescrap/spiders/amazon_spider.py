import scrapy
from ..items import AmazonescrapItem

def get_price(array):
    return ("".join(array))
def get_rating(str):
    return str[:3]

class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon_spider'
    page_number = 2
    # allowed_domains = ['amazon.com']
    start_urls = [
        'https://www.amazon.com/s?bbn=283155&rh=n%3A283155%2Cp_n_publication_date%3A1250226011&dc&fst=as%3Aoff&qid=1599862971&rnid=1250225011&ref=lp_283155_nr_p_n_publication_date_0'
    ]
    def parse(self, response):
        items = AmazonescrapItem()
        books = response.css(".s-include-content-margin.s-border-bottom.s-latency-cf-section")
        for idx, data in enumerate (books):
            title = data.css(".a-color-base.a-text-normal::text").extract()
            author = data.css(".a-color-secondary .a-size-base.a-link-normal").css("::text").extract()
            rating = data.css("i.a-icon.a-icon-star-small span.a-icon-alt::text").extract()
            price = data.css(".a-spacing-top-small .a-price-fraction , .a-spacing-top-small .a-price-whole").css("::text").extract()
            image_url = data.css('.s-image-fixed-height img::attr(src)').extract()

            items['titles'] = title
            items['authors'] = get_price(author).strip()
            if len(rating) != 0:
                items['ratings'] = get_rating(rating[0])
            # items['ratings'] = rating
            items['prices'] = get_price(price)
            items['image_urls'] = image_url

            yield items
            next_page = 'https://www.amazon.com/s?i=stripbooks&bbn=283155&rh=n%3A283155%2Cp_n_publication_date%3A1250226011&dc&page='+str(self.page_number)+'&fst=as%3Aoff&qid=1599928796&rnid=1250225011&ref=sr_pg_2'
            if self.page_number <= 75:
                self.page_number += 1
                yield response.follow(next_page,callback=self.parse)