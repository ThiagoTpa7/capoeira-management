from django.urls import path
from app_management import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('mensalidades/', views.listar_mensalidades, name='mensalidades'),
    path('mensalidades/<int:id>/', views.marcar_pago, name='marcar_pago'),
    path('cadastrar-aluno/', views.cadastrar_aluno, name='cadastrar_aluno'),
    path('alunos/', views.listar_alunos, name='listar_alunos'),
    path('excluir/<int:id>/', views.excluir_aluno, name='excluir_aluno'),
    path('cadastrar-mensalidade/', views.cadastrar_mensalidade, name='cadastrar_mensalidade'),
    path('pendente/<int:id>/', views.marcar_pendente, name='marcar_pendente'),
    path('cadastrar-evento/', views.cadastrar_evento, name='cadastrar_evento'),
    path('login/', views.login_user, name='login_user'),
    path('logout/', views.logout_user, name='logout_user'),
    path('evento/<int:id>/', views.detalhe_evento, name='detalhe_evento'),
    path('quem-somos/', views.quem_somos, name='quem_somos'),
]