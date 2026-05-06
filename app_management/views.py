from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum
from django.utils import timezone
from .models import Aluno, Mensalidade, Evento
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


def dashboard(request):

    eventos = Evento.objects.all().order_by('data')


    return render(request, 'dashboard.html', {
        'eventos': eventos,
    })

def listar_mensalidades(request):
    total_alunos = Aluno.objects.count()
    total_pagas = Mensalidade.objects.filter(status='PAGO').count()
    total_pendentes = Mensalidade.objects.filter(status='PENDENTE').count()
    filtro = request.GET.get('filtro')

    mensalidades = Mensalidade.objects.all()
    total_recebido = Mensalidade.objects.filter(status='PAGO').aggregate(total=Sum('valor'))['total'] or 0
    total_pendente_valor = Mensalidade.objects.filter(status='PENDENTE').aggregate(total=Sum('valor'))['total'] or 0

    if filtro == 'pendentes':
        mensalidades = mensalidades.filter(status='PENDENTE')

    mensalidades = mensalidades.order_by('mes_referencia')

    return render(request, 'mensalidades.html', {
        'mensalidades': mensalidades,
        'total_alunos': total_alunos,
        'total_pagas': total_pagas,
        'total_pendentes': total_pendentes,
        'total_recebido': total_recebido,
        'total_pendente_valor': total_pendente_valor,
    })

def marcar_pago(request, id):

    mensalidade = get_object_or_404(Mensalidade, id=id)

    if mensalidade.status == 'PAGO':
        return redirect('mensalidades')
    
    mensalidade.status = 'PAGO'
    mensalidade.data_pagamento = timezone.now()
    mensalidade.save()

    return redirect('mensalidades')

def cadastrar_aluno(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        idade = request.POST.get('idade')
        telefone = request.POST.get('telefone')

        Aluno.objects.create(nome=nome, idade=idade, telefone=telefone)

        return redirect('dashboard')

    return render(request, 'cadastrar_aluno.html')
    
def listar_alunos(request):
    alunos = Aluno.objects.all()
    return render(request, 'listar_alunos.html', {'alunos': alunos})

def excluir_aluno(request, id):
    aluno = get_object_or_404(Aluno, id=id)
    aluno.delete()
    return redirect('listar_alunos')

def cadastrar_mensalidade(request):
    alunos = Aluno.objects.all()
    erro = None

    if request.method == 'POST':
        aluno_id = request.POST.get('aluno')
        valor = request.POST.get('valor')
        mes_referencia = request.POST.get('mes_referencia')

        if Mensalidade.objects.filter(aluno_id=aluno_id, mes_referencia=mes_referencia).exists():
            erro = "Já existe uma mensalidade para este aluno e mês de referência."
        else:
            Mensalidade.objects.create(
                aluno_id=aluno_id, 
                valor=valor, 
                mes_referencia=mes_referencia
            )
            return redirect('mensalidades')    
    

        return render(request, 'cadastrar_mensalidade.html', 
            {'alunos': alunos,
             'erro': erro}
        )

    alunos = Aluno.objects.all()
    return render(request, 'cadastrar_mensalidade.html', {'alunos': alunos})

def marcar_pendente(request, id):
    mensalidade = get_object_or_404(Mensalidade, id=id)
    mensalidade.status = 'PENDENTE'
    mensalidade.data_pagamento = None 
    mensalidade.save()

    return redirect('mensalidades')

def cadastrar_evento(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        data = request.POST.get('data')
        descricao = request.POST.get('descricao')
        localizacao = request.POST.get('localizacao') or None

        Evento.objects.create(
            nome=nome,
            data=data,
            descricao=descricao,
            local=localizacao
        )

        return redirect('dashboard')

    eventos = Evento.objects.all().order_by('data')

    return render(request, 'cadastrar_evento.html', {'eventos': eventos})

def detalhe_evento(request, id):
    evento = get_object_or_404(Evento, id=id)
    return render(request, 'detalhe_evento.html', {'evento': evento})

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Usuário ou senha inválidos.')

    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('login_user')

def quem_somos(request):
    return render(request, 'quem_somos.html')