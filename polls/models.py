import datetime
from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text=models.CharField(max_length=200)
    pub_date=models.DateTimeField('date published')#Neste exemplo nós definimos um nome legível para humanos. Para todos os outros campos neste modelo, o nome legível para máquina será utilizado como nome legível para humanos.

    def was_published_recently(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(days=1)) #Verifica se a data de publicação é maior ou igual a um dia anterior a hoje. Ou seja se foi postado ontem, ou depois disso.

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text=models.CharField(max_length=200)
    votes=models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text