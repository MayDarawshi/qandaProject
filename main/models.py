from django.db import models
from django.utils.text import slugify

# Create your models here.





class users(models.Model):
    user_id=models.IntegerField(null=False,unique=True)
    user_name=models.CharField(max_length=100)
    grade=models.CharField(max_length=7)
    password=models.CharField(max_length=16)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=10)
    school=models.CharField(max_length=50)  
 
    

    def __str__(self) -> str:
        return super().__str__()

class teachers(models.Model):
    user_name=models.CharField(max_length=100)
    degree=models.CharField(max_length=100)
    password=models.CharField(max_length=16)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=10)
    author_id=models.IntegerField(unique=True,default=0)

    def __str__(self) -> str:
        return super().__str__()




class questions(models.Model):
    id=models.AutoField(primary_key=True)
    question=models.CharField(max_length=10000)
    difficulty=models.CharField(max_length=1)
    grade=models.CharField(max_length=2)
    type=models.CharField(max_length=25)
    title=models.CharField(max_length=100)
    author_id=models.IntegerField(default=0)
    diffi = models.CharField(max_length=7)
    


    # q_image=models.ImageField(null=True,blank=True,upload_to="images/")

    def __str__(self) -> str:
        return super().__str__()

class Answer(models.Model):
    aid = models.AutoField(primary_key=True)
    answer_text = models.TextField(max_length=50000)
    q_image=models.ImageField(null=True,blank=True,upload_to="images/")
    checked = models.BooleanField(default=False)
    q_id = models.CharField(null=False,max_length=1000)
    grade =  models.CharField(null=True,max_length=3,default=1)
    user_id = models.CharField(null=False,max_length=10)
   


    def __str__(self) -> str:
        return super().__str__()



    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''    

        return self._foo 


class difficulty_tbl(models.Model):
    
    qid=models.IntegerField(default=3)
    diff=models.IntegerField(default=0)


# class exam_answers(models.Model):
#     user_id=models.IntegerField(null=False)
#     answer_image=models.ImageField(null=True,blank=True,upload_to="imagesExams/")
#     checked=models.BooleanField(default=False)
#     grade =  models.CharField(null=True,max_length=3,default=0)
    
