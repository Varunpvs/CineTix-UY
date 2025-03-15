from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from apps.polls.models import Poll, PollVote
from web_project import TemplateLayout


class PollListView(LoginRequiredMixin, TemplateView):
    template_name = "polls_list.html"

    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        polls = Poll.objects.all()

        for poll in polls:
            # Calculate the progress percentage
            poll.progress_percent = (
                (poll.yes_votes / poll.threshold) * 100 if poll.threshold > 0 else 0
            )

            # Check if the logged-in user has voted on this poll
            poll.has_voted = PollVote.objects.filter(user=self.request.user, poll=poll).exists()

        context['polls'] = polls
        return context
