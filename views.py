from django.shortcuts import render, redirect

people = []

class Person:
    def __init__(self, username, password):
        self.username = username
        self.password = password

def add_person(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        person = Person(username=username, password=password)
        people.append(person)
        return redirect('people_list')
    return render(request, 'add.html')

def people_list(request):
    return render(request, 'list.html', {'people': people})
