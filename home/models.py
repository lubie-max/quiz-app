from django.db import models
import uuid

from django.db.models.deletion import CASCADE
# Create your models here.


class BaseModel(models.Model):
        uid= models.UUIDField(default=uuid.uuid4)
        created_at= models.DateField(auto_now_add=True)
        updated_at= models.DateField(auto_now=True)

        class  Meta:
            abstract= True


import random

class Category(BaseModel):
    category_name= models.CharField(max_length=100)
    def __str__(self):
        return self.category_name

class Question(BaseModel):
    category= models.ForeignKey(Category, on_delete=models.CASCADE, related_name='rel_category')
    question= models.CharField(max_length=100)
    marks= models.IntegerField()
    def __str__(self):
        return self.question

    def get_options(self):
        obj_options= list(Option.objects.filter(question=self))
        options= []
        random.shuffle(obj_options)
        for obj in obj_options:
            options.append({
                'option': obj.option,
                'is_correct': obj.is_correct
            

            })

        return options


class Option(BaseModel):
    question= models.ForeignKey(Question, on_delete=CASCADE, related_name='rel_question')
    option= models.CharField(max_length=100)
    is_correct= models.BooleanField(default=False) 
    def __str__(self):
        return self.option



