
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db import models
from django.db.models.signals import post_save

class Location(models.Model):
    name=models.CharField(max_length=40)

    def __str__(self):
       return self.name 
class NeigbourHood(models.Model):
    name=models.CharField(max_length=40)
    NeiLocation=models.ForeignKey(Location,on_delete=models.CASCADE);
    occupantsCount=models.IntegerField(blank=True)
    users=models.ForeignKey(User,on_delete=models.CASCADE, related_name='users')
    admin=models.ForeignKey(User,on_delete=models.CASCADE,limit_choices_to={'is_staff':True},related_name='admin')

    # admin=models.ForeignKey(NeiAdmin,on_delete=models.CASCADE)

    @classmethod
    def create_neigb(cls):
        nei=cls.save()
        return nei
        

    # @classmethod
    # def delete_nei(cls,id):

    #     P=cls.objects.get(id=id)
    #     return P.delete()
        

    @classmethod
    def find_nei(cls,search_term):
        nei=cls.objects.filter(name__icontains=search_term)
        return nei
    

    @classmethod
    def update_nei(cls,id,search_term):
        return cls.objects.filter(id=id).update(caption=search_term)



    def __str__(self):
       return self.name 

class Category(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE ,limit_choices_to={'is_staff':True})
    name=models.CharField(max_length=55)

    def __str__(self):
       return self.name 

    
class News(models.Model):
    writer=models.ForeignKey(User,on_delete=models.CASCADE,limit_choices_to={'is_staff':True})
    newsTitle=models.CharField(max_length=55)
    newsImage=models.ImageField(upload_to='news')
    newsDescription=models.TextField(max_length=1000)
    pub_date = models.DateTimeField(auto_now_add=True)
    location=models.ForeignKey(Location,on_delete=models.CASCADE,blank=True,default=1)
    neiba=models.ForeignKey(NeigbourHood,on_delete=models.CASCADE,blank=True,default=1)
class BussinessClass(models.Model):
    Bname=models.CharField(max_length=40)
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    neID=models.ForeignKey(NeigbourHood,on_delete=models.CASCADE)
    Bmail=models.CharField(max_length=40)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    Bimage=models.ImageField(upload_to='biz', blank=True)


    def __str__(self):
       return self.name 
    @classmethod
    def create_business(CLS):
        biz=cls.save()
        return biz

    @classmethod
    def delete_business(cls):
         P=cls.objects.get(id=id)
         return P.delete()
        

    @classmethod
    def search_by_title(cls,search_term,id):
        biz=cls.objects.filter(Bname__icontains=search_term,neID=id)
        return biz
    @classmethod
    def update_business(cls ,search_term):
        return cls.objects.filter(id=id).update(caption=search_term)
    
    
    
    def __str__(self):
       return self.Bname 






class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    # name=models.CharField(max_length=40)
    neID=models.ForeignKey(NeigbourHood,on_delete=models.CASCADE, default=1)
    # email=models.CharField(max_length=300)
    
    locationID=models.ForeignKey(Location,on_delete=models.CASCADE,default=1)
    profile_img=models.ImageField(upload_to='profile_pics',blank=True)


    @receiver(post_save,sender=User)
    def create_user_profile(sender,instance,created,**kwargs):
        if created:
            Profile.objects.create(user=instance)


   