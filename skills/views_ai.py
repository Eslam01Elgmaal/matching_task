from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import JsonResponse
import json
from django.conf import settings


from langchain.chat_models import init_chat_model


llm = init_chat_model(
    "gemini-2.5-flash",
    model_provider="google_genai",
    api_key=settings.GOOGLE_API_KEY
)

@csrf_exempt
def match_skills_ai(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            track = data.get("track")
            description = data.get("description", "")
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

        skills_db = {
            "FE": ["HTML", "CSS", "JavaScript", "React", "Git"],
            "BE": ["Python", "Django", "REST API", "PostgreSQL", "Git"],
        }

        matched_skills = [s for s in skills_db.get(track, []) if s.lower() in description.lower()]
        missing_skills = [s for s in skills_db.get(track, []) if s.lower() not in description.lower()]


        score = round(len(matched_skills) / len(skills_db.get(track, [])) * 100) if skills_db.get(track) else 0


        prompt = f"""
        You are a career advisor. 
        Track: {track}
        Matched skills: {', '.join(matched_skills)}
        Missing skills: {', '.join(missing_skills)}
        Score: {score}%

        Write a very short advice in English (no more than 2 sentences) focusing on what the user should do next to improve.
        """

        advice = llm.predict(prompt)


        return JsonResponse({
            "matched_skills": matched_skills,
            "missing_skills": missing_skills,
            "score": score,
            "advice": advice
        })

    return JsonResponse({"error": "Only POST requests are allowed."}, status=405)
