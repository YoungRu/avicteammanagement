from .forms import UserForm, SigninForm, TodoForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User, auth
from django.views.generic.edit import FormView, UpdateView
from django.views.generic import RedirectView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Todo, Signin
from django.views import generic
from .models import UserReg


# Create your views here.

class IndexView(generic.ListView):
    template_name = 'todo/index.html'
    context_object_name = 'todo_list'

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Todo.objects.filter(Checked=False).order_by('-Assign_Time')
        elif self.request.user.is_authenticated:
            urun = self.request.user
            return Todo.objects.filter(Checked=False, Assign=urun.userreg).order_by('-Assign_Time')
        else:
            pass
    # , Assign = self.request.user.userreg.Username

class DetailView(generic.DetailView):
    model = Todo
    template_name = 'todo/detail.html'

class SignUpView(FormView):
    template_name = 'authenticate/signup.html'
    form_class = UserForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name,{'form':form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            Username = request.POST['Username']
            Email = request.POST['Email']
            Password = request.POST['Password']
            Password2 = request.POST['Password2']
            if Password2 == Password:
                if User.objects.filter(email=Email).exists():
                    messages.info(request, 'Email already used, try another one')
                    return redirect('managementapp:signup')
                elif User.objects.filter(username=Username).exists():
                    messages.info(request, 'Username already used, try another one')
                else:
                    user = User.objects.create_user(username=Username, email=Email, password=Password)
                    obj.Id = User.objects.get(id=user.id)
                    obj.save()
                    user.save()
                    return redirect('managementapp:signin')
        return render(request, 'todo/signup.html')

class SignInpView(FormView):
    template_name = 'authenticate/signin.html'
    form_class = SigninForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name,{'form':form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            Username = request.POST['Username']
            Password = request.POST['Password']

            user = auth.authenticate(username=Username, password=Password)

            if user is not None:
                auth.login(request, user)
                return redirect('/')
            else:
                messages.info(request, 'Credentials Invalid')
                return redirect('managementapp:signin')
        else:
            return render(request, 'signin.html')

def SignOut(request):
    auth.logout(request)
    return redirect('managementapp:index')


class CreateView(FormView):
    template_name = 'todo/create.html'
    form_class = TodoForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name,{'form':form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            newform = form.save(commit=False)
            newform.Assign_By = request.user
            newform.save()
            form.save_m2m()
            return redirect('managementapp:index')
        else:
            return redirect('managementapp:createtodo')

class UpdateTodoView(UpdateView):
    model = Todo
    form_class = TodoForm
    template_name = 'todo/create.html'
    success_url = reverse_lazy('managementapp:index')


def Done(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == 'POST':
        todo.WorkDone = True
        todo.save()
        return redirect('managementapp:index')

def UnDone(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == 'POST':
        todo.WorkDone = False
        todo.save()
        return redirect('managementapp:index')

def Checked(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == 'POST':
        todo.Checked = True
        todo.save()
        return redirect('managementapp:index')

def Delete(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method =='GET':
        todo.delete()
        return redirect('managementapp:index')






