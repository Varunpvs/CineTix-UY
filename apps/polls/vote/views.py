from django.contrib.auth.models import User
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.polls.models import Poll, PollVote


class PollVoteView(LoginRequiredMixin, TemplateView):

    def post(self, request, id):
        poll = get_object_or_404(Poll, id=id)

        # Check if the user has already voted for this poll
        if PollVote.objects.filter(user=request.user, poll=poll).exists():
            messages.warning(request, "You have already voted for this poll.")
            return redirect('polls-list')

        # Record the user's vote
        PollVote.objects.create(user=request.user, poll=poll, vote=True)

        poll.vote()  # Increment the vote count
        messages.success(request, f'Your vote for "{poll.movie.title}" has been recorded!')
        return redirect('polls-list')



class RemoveVoteView(LoginRequiredMixin, TemplateView):

    def post(self, request, id):
        poll = get_object_or_404(Poll, id=id)

        # Check if the user has voted for this poll
        try:
            # Find the user's vote for this poll
            user_vote = PollVote.objects.get(user=request.user, poll=poll)
            user_vote.delete()  # Remove the vote
            poll.vote()  # Recalculate the votes and check if the poll needs to be finalized
            messages.success(request, f'Your vote for "{poll.movie.title}" has been removed.')
        except PollVote.DoesNotExist:
            messages.warning(request, "You have not voted for this poll.")

        return redirect('polls-list')
