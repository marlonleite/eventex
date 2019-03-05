from django.shortcuts import render

from .forms import SubscriptionForm


def subscribe(resquest):
    context = {'form': SubscriptionForm()}
    return render(resquest, 'subscriptions/subscription_form.html', context)
