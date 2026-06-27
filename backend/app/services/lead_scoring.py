def score_lead(interest: str):
    interest = interest.lower()

    if "artificial intelligence" in interest or "ai" in interest:
        return 95, "HOT"

    elif "data science" in interest:
        return 90, "HOT"

    elif "full stack" in interest:
        return 85, "HOT"

    elif "python" in interest:
        return 80, "WARM"

    elif "java" in interest:
        return 75, "WARM"

    elif "web development" in interest:
        return 70, "WARM"

    else:
        return 50, "COLD"