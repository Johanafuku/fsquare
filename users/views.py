from django.shortcuts import render, redirect
from .forms import DesignerRegisterForm, SupplierRegisterForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

def register_designer(request):
    form = DesignerRegisterForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('login')

    return render(request, 'users/register_designer.html', {"form": form})


def register_supplier(request):
    form = SupplierRegisterForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('login')

    return render(request, 'users/register_supplier.html', {"form": form})



class CustomLoginView(LoginView):
    template_name = 'general/login.html'

    def get_success_url(self):
        user = self.request.user

        if hasattr(user, 'designer'):
            return reverse_lazy('designer-dashboard')

        elif hasattr(user, 'supplier'):
            return reverse_lazy('supplier-dashboard')

        return reverse_lazy('home')