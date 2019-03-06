from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name="Marlon Leite", cpf="12345678901",
                    email="marlonleite@gmail.com", phone="82-99609-9655")
        self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_email_object(self):
        expect = 'Confirmação de Inscrição'

        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventex.com.br', 'marlonleite@gmail.com']

        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = [
            'Marlon Leite',
            '12345678901',
            'marlonleite@gmail.com',
            '82-99609-9655',
        ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
