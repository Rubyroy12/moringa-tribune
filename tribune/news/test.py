from django.test import TestCase
from .models import Editor,Article,tags

class EditorTestClass(TestCase):
    #set up method
    def setUp(self):
        self.james=Editor(first_name='James',last_name='Muriuki',email='james@moringaschool')
    #testing instance method
    def test_instance(self):
        self.assertTrue(isinstance(self.james,Editor)) 
    #testing saving method
    def test_save_method(self):
        self.james.save_editor()
        editors=Editor.objects.all()
        self.assertTrue(len(editors)>0)

    # def test_delete_method(self):
    #     self.james.delete_editor()


class ArticleTestClass(TestCase):
    def setUp(self):
        self.james = Editor(first_name='James',last_name='Muriuki',email='muriuki@gmail.com')
        self.james.save_editor()

        self.new_tag= tags(name='testing')
        self.new_tag.save()


        self.new_article=Article(title=' Test Article',post='This is a random test post',editor=self.james)
        self.new_article.save()

        self.new_article.tags.add(self.new_tag)

    def tearDown(self):
        Editor.objects.all().delete
        tags.objects.all().delete
        article.objects.all().delete

        