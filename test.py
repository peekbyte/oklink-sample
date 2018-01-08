import requests
import hmac
import hashlib
import base64
import json

#prod
# api_url = "https://www.oklink.com"

#test
api_url = "http://test.oklink.com"


ticker_url = "/api/v2/ticker.do"
country_url = "/api/v2/country.do"
detail_url = "/api/v2/detail_info.do"
create_remittance = "/api/v2/create_remittance.do"
remit_info = "/api/v2/remittance_info.do"
remit_list = "/api/v2/remittance_list.do"
pay_info = "/api/v2/pay_info.do"
pay = "/api/v2/pay.do"
accept = "/api/v2/accept.do"
reject_info = "/api/v2/reject_info.do"
reject = "/api/v2/reject.do"
refund = "/api/v2/refund.do"
refund_info = "/api/v2/refund_info.do"
receive_info = "/api/v2/receive_info.do"
receive = "/api/v2/receive.do"
user_info = "/api/v2/user_info.do"
notice = "/api/v2/notice.do"
detail_info = "/api/v2/business/detail_info.do"

#test UK
# api_key ="befb6850-123b-4c1d-8fc4-4234dc28ca54"
# secret_key = b"868C767D57DD10D7F48678BD9ACA075F"

#test CA
api_key ="9c7493dd-7acc-431e-8565-a811ec7c2030"
secret_key = b"C2582377053B5F7DCEB3D8F00479C662"

def create_token(message, secret_key):

    return hmac.new(secret_key, message.encode('utf-8'), hashlib.sha256).hexdigest()

def create_header(url, nonce, payload= None):
    payload = "" if payload is None else json.dumps(payload)
    print (nonce + url + payload)
    signature = create_token(nonce + url + payload, secret_key)
    headers = {'KEY': api_key, "NONCE": nonce, "SIGNATURE": signature, "contentType": "application/json"}
    return headers

def get_user_info(nonce, payload = None):
    r = requests.post(api_url + user_info, headers=create_header(user_info, nonce))
    print(r.text)

def get_detail_info(nonce, payload = None):
    r = requests.post(api_url + detail_info, headers=create_header(detail_info, nonce))
    print(r.text)


def create_remittance(nonce, payload = None):
    r = requests.post(api_url + create_remittance, headers=create_header(create_remittance, nonce))
    print(r.text)

def get_notices(nonce):
    r = requests.post(api_url + notice, headers=create_header(notice, nonce))
    print(r.text)

def get_ticker_info(nonce, payload = None):
    r = requests.post(api_url + ticker_url, headers=create_header(ticker_url, nonce, payload), json=payload)
    print(r.text)

def get_country_info(nonce, payload = None):
    r = requests.post(api_url + country_url, headers=create_header(country_url, nonce, payload), json=payload)
    print(r.text)

def get_reaponse(url, nonce, payload = None):
    r = requests.post(api_url + url, headers=create_header(url, nonce, payload), json=payload)
    print(r.text)

# get_ticker_info("123", {'symbol': 'EXRATE'})

# get_notices("123")


get_detail_info("123", {'country_id': '143', 'pay_mode': '1'})

# create_remittance("123", {'fcountry_id': '78', '143': 'EXRATE', 'pay_mode': '2'})

# get_detail_info("123", {'symbol': 'EXRATE'})

#get_country_info("123", {'scope': 'delivery'})

# {"country_code":"PH","country_name":"Philippines","currency":"PHP","country_id":143}

# + json.dumps(payload)

# get_reaponse(detail_url ,'3232', {'fcountry_id': 10, 'tcountry_id': 143, 'pay_mode': 1})







































#
#
# nonce = "12"
# # url= api_url + 'user_info.do'
#
#
# # payload = {'number': 12524, 'type': 'issue', 'action': 'show'}
# payload = {}
# payload_text = json.dumps(payload)
#
#
# # sig = nonce + url + payload_text
#
# # '1323232http://test.oklink.com/api/v2/user_info{"number": 12524, "action": "show", "type": "issue"}'
# message = b'12/api/v2/user_info.do'
#
# signature = hmac.new(secret_key, message, hashlib.sha256).hexdigest()
#
#
# headers = {'KEY':api_key, "NONCE": nonce , "SIGNATURE": signature, "contentType": "application/json"}
#
# headers_text = json.dumps(headers)
#
#
# r = requests.post('https://www.oklink.com/api/v2/user_info.do', headers=headers)
#
# print(r.text)
# dd = 333
# # Oklink
#

#contentType:application/json
#url: https://www.oklink.com/api/v2
#test url: http://test.oklink.com/api/v2

#callback
#post parameters

#user_id 、remit_id 、event_type 、message

#respond 'OK'

