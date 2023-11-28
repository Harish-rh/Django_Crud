from django.shortcuts import render, redirect
from .forms import UserForm
from django.contrib import messages
from .models import RegisterForm


def home(request):
    datas = RegisterForm.objects.all()

    if datas:
        return render(request, 'myApp/home.html', {"datas": datas})
    else:
        return render(request, 'myApp/home.html')


def insert(request):
    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Registration Success")
            return redirect('/')
        else:
            messages.error(request, "Please fill the full form")

    else:
        form = UserForm()

    return render(request, 'myApp/register.html', context={"form": form})


def update(request, id):
    data = RegisterForm.objects.get(id=id)

    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        email = request.POST['email']
        contact = request.POST['contact']
        address = request.POST['address']

        data.name = name
        data.age = age
        data.email = email
        data.contact = contact
        data.address = address
        data.save()
        messages.success(request, "Updated Successfully")
        return redirect("home")

    return render(request, "myApp/update.html", {"data": data})


def delete(request, id):
    data = RegisterForm.objects.get(id=id)
    data.delete()
    messages.error(request, "Deleted Successfully")
    return redirect("home")
