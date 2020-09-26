from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from ..models import Challenge
from TWT.context import get_discord_context


class EndView(View):
    """View for ending a challenge"""

    def get_context(self, request: WSGIRequest) -> dict:
        return get_discord_context(request=request)

    def post(self, request: WSGIRequest, challenge_id: int):
        if not request.user.is_authenticated:
            return redirect('/')

        context = self.get_context(request=request)
        if not context["is_admin"]:
            return redirect('/')

        challenge = Challenge.objects.get(id=challenge_id)
        challenge.ended = True
        challenge.save()
        return redirect('/')