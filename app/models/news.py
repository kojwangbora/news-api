class Source:
    '''Source class to define the ojects in Source'''

    def __init__(self, id,name):
        self.id =id
        self.name=name
    
    class Articles:
        def __init__(self,urlToImage,url,title,content,author,publishedAt):
            self.urlToImage=urlToImage
            self.url = url
            self.title=title
            self.content=content
            self.author=author
            self.publishedAt=publishedAt
            
            
            
           

         
