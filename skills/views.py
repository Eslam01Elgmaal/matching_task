from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import JsonResponse
import json
from .models import Skill, UserInput

@csrf_exempt
def match_skills(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            track = data.get("track")
            description = data.get("description")
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

        if not track or not description:
            return JsonResponse({"error": "Please provide both track and description."}, status=400)

    
        user_input = UserInput.objects.create(track=track, description=description)


        skills = Skill.objects.filter(track=track)
        matched_skills = []
        missing_skills = []

        for skill in skills:
            if skill.name.lower() in description.lower():
                matched_skills.append(skill.name)
            else:
                missing_skills.append(skill.name)

        total_skills = len(skills)
        if total_skills > 0:
            score = round((len(matched_skills) / total_skills) * 100)
        else:
            score = 0

        return JsonResponse({
            "user_input": {"track": track, "description": description},
            "matched_skills": matched_skills,
            "missing_skills": missing_skills,
            "score": score
        })

    return JsonResponse({"error": "Only POST requests are allowed."}, status=405)



def index(request):
    tracks = Skill.objects.values_list('track', flat=True).distinct()
    TRACK_LABELS = dict(Skill.TRACK_CHOICES)
    track_options = Skill.TRACK_CHOICES 
    return render(request, 'skills/index.html', {'track_options': track_options})
