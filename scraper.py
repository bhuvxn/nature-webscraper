from bs4 import BeautifulSoup
import string
import requests
import os

headers = {'Accept-Language': 'en-US,en;q=0.5'}
url = ("https://www.nature.com/nature/articles?sort=PubDate&year=2020&page=") #base link without page number
saved_articles = []
base_dir = os.getcwd()

def get_url_status(url):
    # checks the HTTP Status of a given url
    response = requests.get(url)
    if response.status_code != 200:
        print(f'\nThe URL returned {response.status_code}!')
        return -1
    else:
        return 0


# function to write html content and return as string
def write_html(url):
    page_content = (requests.get(url)).content
    return page_content




# takes the link to news articles and saves them to file with title and the articles text
def get_link_write_news(link):
    url = f'https://www.nature.com{link}'
    article_soup = BeautifulSoup(write_html(url), 'html.parser')
    title = (article_soup.find(attrs={'class': 'c-article-magazine-title'})).getText()
    body = (article_soup.find(attrs={'class': 'article__teaser'})).getText()

    # removing punctuation from character
    for character in (string.punctuation):
        title = title.replace(character, "")
    # removing white space from title
    title = title.replace(" ", "_")
    with open(f'{title}.txt', "wb") as f:
        f.write(body.encode())
    return (f'{title}.txt')

#parsing using input for number of pages and article type
pages = input()
atype = input()

#going through each page and writing values of given type
for page_number in range(int(pages)):
    #appending page number to our base url
    current_page_url = f'{url}{str(page_number+1)}'
    #opening the current page we are on 
    soup = BeautifulSoup(write_html(current_page_url),'html.parser')
    #isolating data-test = "article.type"
    cleaned_soup = str(soup.find_all('article'))
    cleaned_soup = BeautifulSoup(cleaned_soup, 'html.parser')
    #removing all articles that are not of the given input type
    for article in cleaned_soup.find_all(attrs={'data-test':'article.type'}):
        if((article.getText()) != atype):
            #finding parent article and removing it from tree
            absolute_parent = article.find_parent('article')
            absolute_parent.decompose()
    #making directory corresponding to our current page number then changing to int
    new_dir = (f'Page_{str(page_number+1)}')
    os.mkdir(f'{base_dir}/{new_dir}')
    #changing to new directory
    os.chdir(f'{base_dir}/{new_dir}')
    #passing each link in the given page to get_link_write_news, and store it in a page_n directory
    for link in cleaned_soup.find_all('a'):
        get_link_write_news(link.get('href'))
    #changing back to base_dir once current page number is completed
    os.chdir(f'{base_dir}')


print("Saved all articles")
# old code below for reference

