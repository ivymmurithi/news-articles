import unittest
from models import articles

Articles = articles.Articles

class articlesTest(unittest.TestCase):

    def setUp(self):
        self.new_articles = Articles(
        'BBC',
        'Python is crazy',
        'http://www.bbc.co.uk/news/world-60177933',
        'BBC',
        'Reasons why python is crazy',
        '2022-01-29:22:21',
        '6 reasons why you should learn python',
        'https://ichef.bbci.co.uk/news/1024/branded_news/11D68/production/_123046037_mediaitem123046033.jpg'
        )

    def test_init(self):
        self.assertEqual(self.new_articles.name,'BBC')
        self.assertEqual(self.new_articles.title,'Python is crazy')
        self.assertEqual(self.new_articles.url,'http://www.bbc.co.uk/news/world-60177933')
        self.assertEqual(self.new_articles.author,'BBC')
        self.assertEqual(self.new_articles.description,'Reasons why python is crazy')
        self.assertEqual(self.new_articles.publishedAt,'2022-01-29:22:21')
        self.assertEqual(self.new_articles.content, '6 reasons why you should learn python')
        self.assertEqual(self.new_articles.urlToImage,'https://ichef.bbci.co.uk/news/1024/branded_news/11D68/production/_123046037_mediaitem123046033.jpg')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_articles,Articles))


if __name__ == '__main__':
    unittest.main()
