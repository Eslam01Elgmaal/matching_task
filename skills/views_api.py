# skills/views_api.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Skill, UserInput
from .serializers import SkillSerializer, UserInputSerializer
import re

class MatchSkillsAPIView(APIView):
    def post(self, request):
        track = request.data.get("track")
        description = request.data.get("description", "").lower()

        if not track or not description:
            return Response({"error": "Please provide both track and description."},
                            status=status.HTTP_400_BAD_REQUEST)

        # Save user input
        user_input = UserInput.objects.create(track=track, description=description)

        # Fetch skills for the track
        skills = Skill.objects.filter(track=track)
        matched_skills = []
        missing_skills = []

        # Tokenize description (split into words)
        words = re.findall(r'\w+', description)

        for skill in skills:
            skill_name = skill.name.lower()

            # Match if any word in description is close to skill name
            if any(skill_name in word or word in skill_name for word in words):
                matched_skills.append(skill.name)
            else:
                missing_skills.append(skill.name)

        return Response({
            "user_input": UserInputSerializer(user_input).data,
            "matched_skills": matched_skills,
            "missing_skills": missing_skills
        }, status=status.HTTP_200_OK)
