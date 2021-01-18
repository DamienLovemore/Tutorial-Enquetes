import datetime
from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text=models.CharField(max_length=200)
    pub_date=models.DateTimeField('date published')#Neste exemplo nós definimos um nome legível para humanos. Para todos os outros campos neste modelo, o nome legível para máquina será utilizado como nome legível para humanos.

    def was_published_recently(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(days=1)) and self.pub_date <= timezone.now() #Verifica se a data de publicação é maior ou igual a um dia anterior a hoje, e se ela não ocorre em uma data futura a data de hoje. Ou seja se foi postado ontem, ou hoje.
    was_published_recently.admin_order_field='pub_date' #Normalmente a edição /admin em funções não é possível ordenar pelo resultado em ordem crescente ou decrescente. Mas como nesse caso ele especifica que essa função na ordenação deve-se ordernar pelo campo "pub_date", essa função fica disponível.
    was_published_recently.boolean=True #Especifica que essa função retorna um valor do tipo booleano. E apresenta ícones de errado e correto, no lugar de aparecer escrito True e False na edição no /admin.
    was_published_recently.short_description='Published Recently?' #Especifica o nome que deve aparecer quando essa função aparecer no /admin, caso seja especificada em "list_display". Ao invés de aparecer o nome da função.

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text=models.CharField(max_length=200)
    votes=models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text