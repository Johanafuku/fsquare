import openai
from suppliers.models import Supplier
from .models import MatchResult
from django.conf import settings
from openai import OpenAI
import json
import base64


client =  OpenAI(api_key=settings.OPENAI_API_KEY)

def analyze_design_with_ai(design):
    """
    This function sends image + text to AI
    and returns structured data.
    """
    with open(design.image.path, "rb") as img_file:
        base64_image = base64.b64encode(img_file.read()).decode("utf-8")

    # create prompt
    prompt = f"""
    Analyze the following fashion design requirements:
    Fabric: {design.fabric_type}
    Color: {design.color}
    Texture: {design.texture}
    Quantity: {design.quantity_meters} meters
    Pieces: {design.pieces}

    Normalize the data and return ONLY valid JSON like this:
    {{
        "normalize_fabric": "",
        "normalize_color": "",
        "normalize_texture": "",
        "quantity": number,
        "pieces": number,

    }}
    """

    # Example using OpenAI (pseudo)
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role":"user",
                "content":[
                    {"type":"text","text":prompt},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}"
                        },
                    },
                ],
            }
        ],
        temperature=0
    )

    ai_text = response.choices[0].message.content
    #convert to json
    try: 
        raw_data = json.loads(ai_text)
    except json.JSONDecodeError:
        raw_data = {}

    structured_data = {
        "normalized_fabric": raw_data.get("normalize_fabric") or design.fabric_type.lower(),
        "normalized_color": raw_data.get("normalize_color") or design.color.lower(),
        "normalized_texture": raw_data.get("normalize_texture") or design.texture.lower(),
        "quantity": raw_data.get("quantity") or design.quantity_meters or 0,
        "pieces": raw_data.get("pieces") or design.pieces or 0,
        }

    return structured_data


def compute_match_score(ai_data, supplier):
    score = 0

    fabric_types = supplier.fabric_types or []
    colors = supplier.colors_available or []
    processing = supplier.processing or []
    min_meters =  supplier.min_meters or 0
    number_of_pieces = supplier.number_of_pieces or 0

    if ai_data["normalized_fabric"] in fabric_types:
        score += 3

    if ai_data["normalized_color"] in colors:
        score += 3

    if ai_data["normalized_texture"] in processing:
        score += 3

    if ai_data["quantity"] >= min_meters:
        score += 3

    if ai_data["pieces"] >= number_of_pieces:
        score += 3

    return score


def run_matching_pipeline(design):
    ai_data = analyze_design_with_ai(design)

    suppliers = Supplier.objects.all()

    for supplier in suppliers:
        score = compute_match_score(ai_data, supplier)

        if score > 0:
            MatchResult.objects.create(
                design=design,
                supplier=supplier,
                score=score,
                ai_analysis=ai_data
            )