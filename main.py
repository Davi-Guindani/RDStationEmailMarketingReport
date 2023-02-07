import requests
import datetime as dt
import smtplib
import config
import time
from email.message import EmailMessage
from client import Client
from graphic import Graphic


s = smtplib.SMTP('smtp.gmail.com', 587)
s.ehlo()
s.starttls()
s.login(config.email_login, config.email_password)

email = EmailMessage()
email['Subject'] = 'Relatórios email marketing'
email['From'] = 'idea@objectopublicidade.com.br'
email['To'] = 'idea@objectopublicidade.com.br'

clients = []
error_list = [{'error_description': 'The access token is invalid or has expired', 'error': 'invalid_token'},
              {'error': 'invalid_token', 'error_description': 'The access token is invalid or has expired'}]


def get_email_metrics(days: int, client: Client):
    base_url = "https://api.rd.services/platform/analytics/emails?"
    start_date = str(dt.date.today() - dt.timedelta(days=days))
    end_date = str(dt.date.today())

    url = base_url + "start_date=" + start_date + "&end_date=" + end_date
    headers = {
        "accept": "application/json",
        "authorization": "Bearer " + client.access_token
    }
    return requests.get(url, headers=headers)


def refresh_token(client: Client):
    url = "https://api.rd.services/auth/token"
    payload = {
        "client_id": client.CLIENT_ID,
        "client_secret": client.CLIENT_SECRET,
        "refresh_token": client.REFRESH_TOKEN
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json"
    }
    response = requests.post(url, json=payload, headers=headers)
    client.access_token = response.json()["access_token"]


for client in config.clients_list:
    c = Client(client['name'], client['client_id'], client['client_secret'],
               client['code'], client['refresh_token'], client['background_color'],
               client['first_color'], client['second_color'], client['bar_label_color'])
    days = 44
    resp = get_email_metrics(days, c)
    while resp.json() in error_list:
        refresh_token(c)
        resp = get_email_metrics(days, c)

    for campaign in resp.json()['emails']:
        divider = 1
        while (campaign['contacts_count'] / divider) > 10:
            divider *= 10
        tick = int(round(campaign['contacts_count'] / divider) * divider)

        graphic_list = [Graphic(
            ['contatos', 'enviados'],
            [0, int(tick / 4), int(tick * 2 / 4), int(tick * 3 / 4), tick],
            ['contatos', 'enviados'],
            [campaign['contacts_count'], campaign['contacts_count'] - campaign['email_dropped_count']],
            ['contatos', 'enviados'],
            [0, int(tick / 4), int(tick * 2 / 4), int(tick * 3 / 4), tick],
            'Métricas',
            "Envios"
        ), Graphic(
            ['tx de entrega', 'tx de abertura', 'tx de clique', 'tx de denúncia', 'desinscrições'],
            [round(campaign['email_delivered_rate'], 1), round(campaign['email_opened_rate'], 1),
             round(campaign['email_clicked_rate'], 1), round(campaign['email_spam_reported_rate'], 1),
             round(campaign['email_unsubscribed_count'] / campaign['email_delivered_count'], 1)],
            ['tx de entrega', 'tx de abertura', 'tx de clique', 'tx de denúncia', 'desinscrições'],
            [round(campaign['email_delivered_rate'], 1), round(campaign['email_opened_rate'], 1),
             round(campaign['email_clicked_rate'], 1), round(campaign['email_spam_reported_rate'], 1),
             round(campaign['email_unsubscribed_count'] / campaign['email_delivered_count'], 1)],
            ['tx de entrega', 'tx de abertura', 'tx de clique', 'tx de denúncia', 'desinscrições'],
            [0, 20, 40, 60, 80, 100],
            'Métricas',
            'Taxas'
        )]

        for graphic in graphic_list:
            fname = graphic.set_graphics_settings(campaign, c)

            with open(fname, 'rb') as content_file:
                content = content_file.read()
                email.add_attachment(content, maintype='application', subtype='png', filename=fname)

s.send_message(email)
print('Email enviado')
time.sleep(5)
s.quit()
