from django.shortcuts import render


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'new message from {name}({email}): {message}')

    return render(request, 'contacts.html')


def home(request):
    return render(request, 'home.html')
