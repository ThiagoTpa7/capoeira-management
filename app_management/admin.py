from django.contrib import admin
from .models import Aluno, Evento, Mensalidade

# Register your models here.
admin.site.register(Aluno)
admin.site.register(Evento)
admin.site.register(Mensalidade)