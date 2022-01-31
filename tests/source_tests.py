import unittest
from app.models import Source


class NewsTest(unittest.TestCase):
    def setUp(self):
        self.new_source = Source('BBC','http://www.bbc.co.uk/news/world-60177933','Why we love python')

    def test_init(self):
        self.assertEqual(self.new_source.name,'BBC')
        self.assertEqual(self.new_source.url,'http://www.bbc.co.uk/news/world-60177933')
        self.assertEqual(self.new_source.description,'Why we love python')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))


if __name__ == '__main__':
    unittest.main()