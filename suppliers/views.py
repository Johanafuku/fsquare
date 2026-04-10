from django.shortcuts import render, redirect
from .models import Supplier
from django.contrib.auth.decorators import login_required
from .forms import SupplierProfileForm

@login_required
def supplier_dashboard(request):
    return render(request, 'suppliers/supplier-dashboard.html')


def supplier_list(request):
    # Get all suppliers from the database
    suppliers = Supplier.objects.all()

    # Send them to the template
    return render(request, 'suppliers/supplier_list.html', {
        'suppliers': suppliers
    })


@login_required
def supplier_profile(request):

    supplier = request.user.supplier  # get logged supplier

    if request.method == "POST":
        form = SupplierProfileForm(request.POST, instance=supplier)

        if form.is_valid():
            form.save()
            return redirect('supplier-dashboard')

    else:
        form = SupplierProfileForm(instance=supplier)

    return render(request, 'suppliers/supplier-profile.html', {"form": form})