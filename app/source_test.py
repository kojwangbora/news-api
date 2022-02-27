import unittest
from models import source
Source = source.Source

class NewsTest(unittest.TestCase):
    '''Test Class to test the behavior of the News class'''

    def setUp(self):
        '''set up method that will run before every Test'''
        self.new_source = source("abc-news","ABC NEWS","Your trusted source for breaking news, analysis,executive interviews, headlines, and videos at ABCNews.com","https:/abcnews.go.com","general","us")
    
    def test_instance(self):
        self.assertTrue(isinstance(self.new_source, Source))


if __name__ == '__main__':
    unittest.main()


