from django.shortcuts import render, redirect, get_object_or_404
from .models import Supplier, SupplierImage
from django.contrib.auth.decorators import login_required
from .forms import SupplierProfileForm, SupplierImageForm

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

    supplier = request.user.supplier

    if request.method == "POST":

        # -------- IMAGE --------
        if request.FILES.get("image"):
            image_form = SupplierImageForm(request.POST, request.FILES)

            if image_form.is_valid():
                image = image_form.save(commit=False)
                image.supplier = supplier
                image.save()

            return redirect("supplier-profile")

        # -------- PROFILE --------
        form = SupplierProfileForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data

            def merge(old, new):
                old = old or []
                new = new or []
                return list(set(old + new))

            # LISTS → append
            if request.POST.get("fabric_types"):
                supplier.fabric_types = merge(
                    supplier.fabric_types,
                    data["fabric_types"]
                )

            if request.POST.get("colors_available"):
                supplier.colors_available = merge(
                    supplier.colors_available,
                    data["colors_available"]
                )

            if request.POST.get("processing"):
                supplier.processing = merge(
                    supplier.processing,
                    data["processing"]
                )

            # NUMBERS → only update if provided
            if request.POST.get("min_meters"):
                supplier.min_meters = data["min_meters"]

            if request.POST.get("number_of_pieces"):
                supplier.number_of_pieces = data["number_of_pieces"]

            # EMAIL
            if request.POST.get("contact_email"):
                supplier.contact_email = data["contact_email"]

            supplier.save()

        return redirect("supplier-profile")

    form = SupplierProfileForm()
    image_form = SupplierImageForm()

    return render(request, "suppliers/supplier-profile.html", {
        "profile_form": form,
        "image_form": image_form,
        "supplier": supplier,
        "images": supplier.images.all()
    })

@login_required
def delete_supplier_image(request, image_id):

    image = get_object_or_404(SupplierImage, id=image_id)

    # Security check same supplier requesting delete the image
    if image.supplier != request.user.supplier:
        return redirect("supplier-profile")

    image.delete()

    return redirect("supplier-profile")