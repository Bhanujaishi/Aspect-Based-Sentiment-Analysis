# Importing Scrapy Library
import os
import scrapy

# Creating a new class to implement Spide
class AmazonReviewsSpider(scrapy.Spider):
    # Spider name
    name = 'amazon_reviews'

    # Domain names to scrape
    allowed_domains = ['amazon.in']
    
    os.system("rm C:/Users/HP/SE_Project1/sentimental_analysis/reviews.json")
    my_file_handle = open('C:/Users/HP/SE_Project1/Amazon_Comments_Scrapper/amazon_reviews_scraping/amazon_reviews_scraping/spiders/ProductAnalysis.txt')
    myBaseUrl = my_file_handle.read()

    start_urls = []

    # Creating list of urls to be scraped by appending page number a the end of base url
    for i in range(1, 121):
        start_urls.append(myBaseUrl + str(i))

    # Defining a Scrapy parser
    def parse(self, response):
        data = response.css('#cm_cr-review_list')

            # Collecting product star ratings
        star_rating = data.css('.review-rating')

            # Collecting user reviews
        comments = data.css('.review-text')
        count = 0

            # Combining the results
        for review in star_rating:
            yield{'stars': ''.join(review.xpath('.//text()').extract()),
                  'comment': ''.join(comments[count].xpath(".//text()").extract())
            }
            count=count+1
