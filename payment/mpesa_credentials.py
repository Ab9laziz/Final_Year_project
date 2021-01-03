import requests
import json
from requests.auth import HTTPBasicAuth
from  datetime import datetime
from django.conf import settings
from base64 import b64encode, encode



class MpesaC2bCredentials:
    consumer_key = settings.MPESA_CONSUMER_KEY
    consumer_secret = settings.MPESA_CONSUMER_SECRET
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'


class MpesaAccessToken:
    r = requests.get(MpesaC2bCredentials.api_URL,
        auth=HTTPBasicAuth(MpesaC2bCredentials.consumer_key,
            MpesaC2bCredentials.consumer_secret))
    mpesa_access_token = r.json()
    validated_mpesa_access_token = mpesa_access_token['access_token']


class LipaNaMpesa:
    lipa_time = datetime.now().strftime('%Y%m%d%H%M%S')
    business_shortcode = settings.MPESA_EXPRESS_SHORTCODE
    passkey = settings.MPESA_PASSKEY
    test_c2b_shortcode = settings.MPESA_SHORTCODE
    data_to_encode = business_shortcode + passkey + lipa_time

    online_password = b64encode(data_to_encode.encode())
    decode_password = online_password.decode('utf-8')

