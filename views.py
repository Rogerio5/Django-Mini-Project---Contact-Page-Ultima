from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Mensagem
from .forms import ReservaForm


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


def reserva_view(request):
    if request.method == "POST":
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Reserva efetuada com sucesso!")
            return redirect("reserva")
    else:
        form = ReservaForm()

    return render(request, "reserva.html", {"form": form})
