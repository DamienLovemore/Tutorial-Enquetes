from django.contrib import admin
from .models import Question, Choice

class ChoiceInLine(admin.TabularInline):
    model=Choice
    extra=3 #Por padrão fornece campos suficientes a 3(três) escolhas.

class QuestionAdmin(admin.ModelAdmin):
    fieldsets=[
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}), #'classes':['collapse'] especifica que o fieldset pode ser minimizado (Escondido e mostrado).
    ]
    inlines=[ChoiceInLine]

    list_display=('question_text','pub_date','was_published_recently') #Especifica quais campos deverão ser apresentados na lista de edição dos modelos. Ao invés do __str__ convencional.
    list_filter=['pub_date'] #Especifica por qual campo os resultados da lista de edição deverão ser filtrado na página inicial de listagem de modelos no /admin. Comom essa campo é do tipo data, ele reconhece isso e aplica opções de filtragem relacionados a data.
    search_fields=['question_text'] #Adiciona uma barra de pesquisa acima da lista de edição dos modelos, onde pode-se pesquisar os modelos apartir desse campo.(Mais de um campo podem ser indicados para pesquisa, porém é recomendado que quanto menos campos forem utilizados para pesquisa mais rápido e melhor é)

admin.site.register(Question, QuestionAdmin)
