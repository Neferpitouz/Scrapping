import bs4
import requests
import fake_headers

if __name__ == '__main__':
    KEYWORDS = ['DIY или Сделай сам', 'Карьера в IT-индустрии', 'IT-эмиграция']
    headers = fake_headers.Headers(os="lin", headers=True).generate()
    base_url = "https://habr.com"
    url = base_url + "/ru/all/"
    response = requests.get(url, headers=headers)

    text = response.text
    soup = bs4.BeautifulSoup(text, features="html.parser")

    articles = soup.find_all("article")
    for article in articles:
        hashtags = article.find_all(class_="tm-article-snippet__hubs-item")
        hashtags = [hashtag.text.strip() for hashtag in hashtags]
        for hashtag in hashtags:
            if hashtag in KEYWORDS:
                date_time = article.find("time").attrs.get('title')
                print(date_time)
                title = article.find("h2").find("span").text
                print(title)
                href = article.find(class_="tm-article-snippet__title-link").attrs.get('href')
                link = base_url + href
                print(link)
                print()

