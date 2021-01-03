import requests
from .mpesa_credentials import LipaNaMpesa, MpesaAccessToken


# mpesa variables
mpesa_access_token = MpesaAccessToken.validated_mpesa_access_token
# print(f"access token is {access_token}")
mpesa_api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"

def index(cell, pesa):
    access_token = mpesa_access_token
    api_url = mpesa_api_url
    headers = {"Authorization": "Bearer %s" % access_token}
    request = {
        "BusinessShortCode": LipaNaMpesa.business_shortcode,
        "Password": LipaNaMpesa.decode_password,
        "Timestamp": LipaNaMpesa.lipa_time,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": pesa,
        # phone number getting stk push
        "PartyA": cell,
        "PartyB": LipaNaMpesa.business_shortcode,  # business till no.or paybill
        # phone number getting stk push same as party A
        "PhoneNumber": cell,
        "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
        "AccountReference": "Pangani Youth Soccer Academy",
        "TransactionDesc": "Paying Academy Fees"
    }

    response = requests.post(api_url, json=request, headers=headers)
    print(response.text)
    return response

