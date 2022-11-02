def auth_header():
    return {
        "x-api-key": "live_MhXwjew5ges6i6eWXn9CDk56UX08g37L8A3nkPnrlLcDPouOitL2bChxOHDoBvOF"
    }


def extract_cat_details(i):
    return {
        "id": i["id"],
        "name": i["name"],
        "temperament": i["temperament"],
        "origin": i["origin"],
        "description": i["description"],
        "life_span": i["life_span"],
        "adaptability": i["adaptability"],
        "affection_level": i["affection_level"],
        "child_friendly": i["child_friendly"],
        "grooming": i["grooming"],
        "health_issues": i["health_issues"],
        "intelligence": i["intelligence"],
        "social_needs": i["social_needs"],
        "stranger_friendly": i["stranger_friendly"],
        "wikipedia_url": i["wikipedia_url"],
        "image": i["image"],
    }
    
def extract_breed_details(i):
    return {
        "id": i["id"],
        "name": i["name"],
    }
