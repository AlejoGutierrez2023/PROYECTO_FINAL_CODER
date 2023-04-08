from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Message
from .forms import MessageForm
from django.db.models import Q
@login_required
def message_create(request): #Si el formulario es válido, se guarda el mensaje con el usuario actual como remitente y se redirige a la lista de mensajes con un mensaje de éxito.
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.save()
            messages.success(request, 'Message sent.')
            return redirect('messages_list')
    else:
        form = MessageForm()
    return render(request, 'message_create.html', {'form': form})

@login_required
def messages_list(request):
    messages = Message.objects.filter(Q(receiver=request.user) | Q(sender=request.user))
    return render(request, 'messages_list.html', {'messages': messages})