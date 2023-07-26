from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView, CreateView, UpdateView, ListView, DeleteView
from django.urls import reverse_lazy, reverse
from apps.forms import RegisterForm, UpdateForm
from apps.models import User
from httpx import get, post


# Create your views here.
class Home(LoginView):
    # redirect_authenticated_user = True
    template_name = 'index.html'

    def form_valid(self, form):
        user = form.get_user()
        if user is not None:
            login(self.request, user)
            return redirect(reverse_lazy('list'))

        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        return redirect(reverse_lazy('home'))


class Register(CreateView):
    model = User
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('list')


class Profile(View):
    def get(self, request, pk):
        a = User.objects.filter(id=pk).first()
        return render(request, 'bs5_edit_profile_account_details.html', {'user': a})

    def post(self, request, pk):
        if request.user.id == pk:
            a = User.objects.filter(id=request.user.id).first()
            if request.POST:
                data = UpdateForm(request.POST, request.FILES, instance=request.user)
                if data.is_valid():
                    portfolio = data.save(commit=False)
                    portfolio.user = a
                    portfolio.save()
                    return redirect(reverse('list'))
            return render(request, 'bs5_edit_profile_account_details.html', {'user': a})
        else:
            users = User.objects.all()
            return render(request, 'new_customer_list.html', {'users': users})


def listview(request):
    users = User.objects.all()
    return render(request, 'new_customer_list.html', {'users': users})


class Delete(View):
    def get(self, request, pk):
        if request.user.id == pk:
            a = User.objects.filter(id=request.user.id).delete()
            return redirect('list')
        else:
            users = User.objects.all()
            return render(request, 'new_customer_list.html', {'users': users})
