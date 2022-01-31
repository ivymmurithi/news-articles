class Source:

    def __init__(self,name,url,description,urlToImage,author,title):
        self.name = name
        self.url = url
        self.description = description
        self.urlToImage = urlToImage
        self.author = author
        self.title = title

class Articles:
    def __init__(self,name,title,url,author,description,publishedAt,content,urlToImage):
        self.name = name
        self.title = title
        self.url = url
        self.author = author
        self.description = description
        self.publishedAt = publishedAt
        self.content = content
        self.urlToImage = urlToImage