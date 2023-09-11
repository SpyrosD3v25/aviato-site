from django.shortcuts import render
from django.contrib.auth.decorators import login_required  # Import login_required decorator
from .forms import ChatMessageForm
from .models import ChatMessage
from common.models import NormalUser

@login_required  # Apply the login_required decorator to the view
def chatbot(request):
    if request.method == 'POST':
        form = ChatMessageForm(request.POST)
        if form.is_valid():
            user = request.user  # Assuming the user is authenticated
            content = form.cleaned_data['content']
            print(f"User: {user}, Content: {content}")
            ChatMessage.objects.create(user=user, content=content)

    else:
        form = ChatMessageForm()
    
    chat_messages = ChatMessage.objects.all()
    
    return render(request, 'chatbot.html', {'form': form, 'chat_messages': chat_messages})
