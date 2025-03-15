from django.urls import path
from django.contrib.auth.decorators import login_required
from apps.polls.list.views import PollListView
from apps.polls.vote.views import PollVoteView, RemoveVoteView

urlpatterns = [
    path("polls/", login_required(PollListView.as_view()), name="polls-list"),
    path("polls/vote/<int:id>/", login_required(PollVoteView.as_view()), name="poll-vote"),
    path('polls/remove_vote/<int:id>/', login_required(RemoveVoteView.as_view()), name='remove-vote'),

]
