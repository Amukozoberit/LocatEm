from datetime import datetime
from unicodedata import category
from neigbouhood.models import BussinessClass, Category, Location, NeigbourHood, News, Profile
from django.test import TestCase
from django.contrib.auth.models import User
import tempfile
# Create your tests here.
class ProfileTestClass(TestCase):

    def setUp(self):

        self.loc=Location(name='Nakuru')
        admin=User(username="peter",email='mwasheberit@gmail.com',password='parapara',is_staff='True')
        user=User(username="peter",email='mwasheberit@gmail.com',password='parapara')
        self.nei=NeigbourHood(name='shabe',occupantsCount=50,users=user,admin=admin,NeiLocation=self.loc)

        self.loc=Location(name='Nakuru')



        user=User(username="peter",email='mwasheberit@gmail.com',password='parapara')
        profile_img=tempfile.NamedTemporaryFile().name
        neID=self.nei
        locationID=self.loc
        self.profile=Profile(user=user,neID=self.nei,locationID=self.loc,profile_img=profile_img)
    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))

class locationTestClass(TestCase):
    def setUp(self):
        self.loc=Location(name='Nakuru')
    def test_instance(self):
        self.assertTrue(isinstance(self.loc,Location))


class NeigbourHoodTestclass(TestCase):
    
    def setUp(self):
        loc=Location(name='Nakuru')
        admin=User(username="peter",email='mwasheberit@gmail.com',password='parapara',is_staff='True')
        user=User(username="peter",email='mwasheberit@gmail.com',password='parapara')
        self.nei=NeigbourHood(name='shabe',occupantsCount=50,users=user,admin=admin,NeiLocation=loc)

    
    def test_instance(self):
        self.assertTrue(isinstance(self.nei,NeigbourHood))


class CategoryTestClass(TestCase):
    def setUp(self):
        user=User(username="peter",email='mwasheberit@gmail.com',password='parapara',is_staff='True')
        name='music'
        self.category=Category(user=user,name=name)
    
    def test_instance(self):
        self.assertTrue(isinstance(self.category,Category))
   
   
class NewsTestClass(TestCase):
    def setUp(self):

        self.loc=Location(name='Nakuru')
        admin=User(username="peter",email='mwasheberit@gmail.com',password='parapara',is_staff='True')
        user=User(username="peter",email='mwasheberit@gmail.com',password='parapara')
        self.nei=NeigbourHood(name='shabe',occupantsCount=50,users=user,admin=admin,NeiLocation=self.loc)

        writer=User(username="peter",email='mwasheberit@gmail.com',password='parapara',is_staff='True')
        newsTitle='music'
        newsImage=tempfile.NamedTemporaryFile().name
        newsDescription='Music is life'
        pub_date=datetime.now
        loc=Location(name='Nakuru')
        self.news=News(writer=writer,newsTitle=newsTitle,newsImage=newsImage,newsDescription=newsDescription,pub_date=pub_date,location=loc)
    
    def test_instance(self):
        self.assertTrue(isinstance(self.news,News))
    
class BussinessClassTestCase(TestCase):
    def setUp(self):
        self.loc=Location(name='Nakuru')
        admin=User(username="peter",email='mwasheberit@gmail.com',password='parapara',is_staff='True')
        user=User(username="peter",email='mwasheberit@gmail.com',password='parapara')
        self.nei=NeigbourHood(name='shabe',occupantsCount=50,users=user,admin=admin,NeiLocation=self.loc)

        u=User(username="peter",email='mwasheberit@gmail.com',password='parapara',is_staff='True')
        name='music'
        self.category=Category(u=user,name=name)


        Bname='sampa'
        owner=User(username="peter",email='mwasheberit@gmail.com',password='parapara')
        neiD=self.nei
        Bmail='sampa@gmail.com'
        category=self.category
        Bimage=tempfile.NamedTemporaryFile().name
        self.biz=BussinessClass(Bname=Bname,owner=owner,neiD=neiD,Bmail=Bmail,Bimage=Bimage,category=category)
        

        def test_instance(self):
            self.assertTrue(isinstance(self.news,News))

    def tearDown(self):
        User.objects.all().delete()
        Profile.objects.all().delete()
        NeigbourHood.objects.all().delete()
        Category.objects.all().delete()
        News.objects.all().delete()
        BussinessClass.objects.all().delete()




