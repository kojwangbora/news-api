class Source:
    '''Source class to define the ojects in Source'''

    def __init__(self, id,name):
        self.id =id
        self.name=name
    
    class Articles:
        def __init__(self, publishedAt, urlToImage,title,content,author,url):
            self.publishedAt=publishedAt
            self.urlToImage=urlToImage
            self.content=content
            self.author=author

         
