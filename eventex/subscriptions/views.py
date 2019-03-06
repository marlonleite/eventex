from django.contrib import messages
from django.core import mail
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string

from .forms import SubscriptionForm


def subscribe(resquest):
    if resquest.method == 'POST':

        form = SubscriptionForm(resquest.POST)

        if form.is_valid():
            body = render_to_string('subscriptions/subscription_email.txt',
                                    form.cleaned_data)

            mail.send_mail('Confirmação de Inscrição',
                           body,
                           'contato@eventex.com.br',
                           ['contato@eventex.com.br', form.cleaned_data['email']])
            
            messages.success(resquest, 'Inscrição realizada com sucesso!')

            return HttpResponseRedirect('/inscricao/')
        else:
            return render(resquest, 'subscriptions/subscription_form.html', 
                          {'form': form})
    else:
        context = {'form': SubscriptionForm()}
        return render(resquest, 'subscriptions/subscription_form.html', context)
