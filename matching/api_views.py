from django.http import JsonResponse
from .models import MatchResult


def matching_results_api(request, design_id):
   
    results = (
        MatchResult.objects
        .filter(design_id=design_id)
        .select_related("supplier")
        .order_by("-score")
    )

    data = []

    for result in results:

        supplier = result.supplier

        data.append({
            "id": result.id,

            # Current score is out of 15
            "score": result.score,

            # Convert score to percentage
            "percentage": round((result.score / 15) * 100),

            "supplier": {
                "id": supplier.id,
                "name": supplier.name,
                "fabric_types": supplier.fabric_types or [],
                "colors_available": supplier.colors_available or [],
                "processing": supplier.processing or [],
                "min_meters": supplier.min_meters or 0,
                "number_of_pieces": supplier.number_of_pieces or 0,
                "contact_email": supplier.contact_email,
            },

          
            "ai_analysis": result.ai_analysis,
        })

    return JsonResponse({
        "design_id": design_id,
        "results": data,
    })
