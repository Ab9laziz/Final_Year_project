import requests
from  datetime import datetime
from requests.auth import HTTPBasicAuth
import json
from base64 import b64encode

consumer_key = "YjA61YtxaMTPhVldfG0OpfZRCEiwPxXU"
consumer_secret = "LpSZu8LmE8BmUGu1"
api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
Passkey = "bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919"
Shortcode = 174379


def get_token():
  r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
  token = r.json()
  return(token["access_token"])
token = get_token()


def get_time():
  now = str(datetime.now().strftime("%Y%m%d"))
  time = str(datetime.now().strftime("%H%M%S"))
  real = str(now+time)
  return real

current_time = get_time()
short = str(Shortcode)

def encoded_pass():
  pwd = (short+Passkey+current_time).encode('utf-8')
  pwd_enc = b64encode(pwd).decode('ascii')
  return pwd_enc

pass_enc = encoded_pass()

def index(cell, pesa):
  access_token = token
  api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
  headers = { "Authorization": "Bearer %s" % access_token }
  request = {
    "BusinessShortCode": Shortcode,
    "Password": pass_enc,
    "Timestamp": current_time,
    "TransactionType": "CustomerPayBillOnline",
    "Amount": pesa,
    "PartyA": cell,
    "PartyB":  Shortcode,
    "PhoneNumber": cell,
    "CallBackURL": "https://tngeene.com/",
    "AccountReference": " Pangani Youth Soccer Academy ",
    "TransactionDesc": " paying school fees"
  }

  response = requests.post(api_url, json = request, headers=headers)
  print (response.text)
  return response

# print (response.text)