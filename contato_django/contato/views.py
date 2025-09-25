from django.shortcuts import render, redirect
from .models import Mensagem

def contato_view(request):
    if request.method == "POST":
        nome = request.POST.get("nome")
        email = request.POST.get("email")
        mensagem = request.POST.get("mensagem")

        if nome and email and mensagem:
            Mensagem.objects.create(
                nome=nome,
                email=email,
                mensagem=mensagem
            )
            return render(request, "contato.html", {"sucesso": True})

    return render(request, "contato.html")
