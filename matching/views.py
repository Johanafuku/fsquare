from django.shortcuts import render, get_object_or_404
from designs.models import Design
from .services import run_matching_pipeline
from .models import MatchResult
from django.contrib.auth.decorators import login_required

@login_required
def match_design(request, design_id):
    design = get_object_or_404(Design, id=design_id)
    
    if not MatchResult.objects.filter(design=design).exists():
        run_matching_pipeline(design)

    results = MatchResult.objects.filter(design=design).order_by('-score')

    return render(request, 'matching/selection.html', {
        'design': design,
        'results': results
    })

