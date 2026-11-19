from django.views import View
from django.shortcuts import render, redirect
from designs.forms import DesignForm
from matching.services import run_matching_pipeline
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@login_required
def designer_dashboard(request):
    return render(request, 'designers/designer-dashboard.html')

@method_decorator(login_required, name="dispatch")
class UploadView(View):

    def get(self, request):
        form = DesignForm()
        return render(request, "designs/upload.html", {"form": form})

    def post(self, request):
        form = DesignForm(request.POST, request.FILES)

        if form.is_valid():
            design = form.save(commit=False)
            design.designer = request.user.designer
            design.save()

            # Run AI matching
            run_matching_pipeline(design)

            # Redirect to results
            return redirect("match-design", design_id=design.id)

        return render(request, "designs/upload.html", {"form": form})
