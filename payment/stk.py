import requests
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .mpesa_credentials import LipaNaMpesa, MpesaAccessToken

# mpesa variables
mpesa_access_token = MpesaAccessToken.validated_mpesa_access_token
# print(f"access token is {access_token}")
mpesa_api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"

@csrf_exempt
def register_urls(request):
    access_token = MpesaAccessToken.validated_mpesa_access_token
    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"
    headers = {"Authorization": "Bearer %s" % access_token}
    options = {"ShortCode": LipaNaMpesa.business_shortcode,
               "ResponseType": "Completed",
               "ConfirmationURL": "http://127.0.0.1:8000/c2b/confirmation",
               "ValidationURL": "http://127.0.0.1:8000/c2b/validation"}
    response = requests.post(api_url, json=options, headers=headers)
    return HttpResponse(response.text)

@csrf_exempt
def validation(request):
    context = {
        "ResultCode": 0,
        "ResultDesc": "Accepted"
    }
    return JsonResponse(dict(context))

def make_payment(phone_number, amount):
    access_token = mpesa_access_token
    api_url = mpesa_api_url
    headers = {"Authorization": "Bearer %s" % access_token}
    request = {
        "BusinessShortCode": LipaNaMpesa.business_shortcode,
        "Password": LipaNaMpesa.decode_password,
        "Timestamp": LipaNaMpesa.lipa_time,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": amount,
        # phone number getting stk push
        "PartyA": phone_number,
        "PartyB": LipaNaMpesa.business_shortcode,  # business till no.or paybill
        # phone number getting stk push same as party A
        "PhoneNumber": phone_number,
        "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
        "AccountReference": "Pangani Youth Soccer Academy",
        "TransactionDesc": "Paying Academy Fees"
    }

    response = requests.post(api_url, json=request, headers=headers)
    print(response.json())
    return HttpResponse('success')

