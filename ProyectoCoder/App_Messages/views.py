from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView
from .models import Message
from .forms import MessageForm
from django.db.models import Q

# @login_required
# class MessageListView(ListView): #mostrar la lista de mensajes recibidos por el usuario, ordenados por fecha de creación.
#     model = Message
#     template_name = 'message_list.html'
#     context_object_name = 'messages'
#     paginate_by = 10

#     def get_queryset(self):
#         queryset = super().get_queryset()
#         return queryset.filter(receiver=self.request.user).order_by('-timestamp')
# @login_required
# class MessageDetailView(DetailView): # mostrar los detalles de un mensaje específico, que solo el remitente o el destinatario pueden ver.
#     model = Message
#     template_name = 'message_detail.html'
#     context_object_name = 'message'

#     def get_object(self):
#         queryset = self.get_queryset()
#         obj = queryset.filter(sender=self.request.user) | queryset.filter(receiver=self.request.user)
#         return get_object_or_404(obj, pk=self.kwargs.get('pk'))

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

class MessageDeleteView(DeleteView):
    model = Message
    success_url = reverse_lazy('message_list')
    template_name = 'message_confirm_delete.html'
    context_object_name = 'message'
    pk_url_kwarg = 'message_pk'

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Message deleted.')
        return super().delete(request, *args, **kwargs)

