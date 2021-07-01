from django.test import TestCase

# Create your tests here.
def test_get_news_today(self):
    today_news = Article.today_news()
    self.assertTrue(len(today_news)>0)
    
def test_get_news_by_date(self):
        test_date = '2017-03-17'
        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
        news_by_date = Article.days_news(date)
        self.assertTrue(len(news_by_date) == 0)