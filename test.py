import requests
from requests import Request, Session
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
create_remittance_url = "/api/v2/create_remittance.do"
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
# detail_info = "/api/v2/business/detail_info.do"
detail_info = "/api/v2/detail_info.do"

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
    r = requests.post(api_url + detail_info, headers=create_header(detail_info, nonce, payload), json=payload)
    print(r.text)

def create_remittance(nonce, payload = None):
    r = requests.post(api_url + create_remittance_url, headers=create_header(create_remittance_url, nonce, payload), json=payload)
    print(r.text)
    # prepped = r.prepare()
    # print(prepped.headers)

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


# get_detail_info("1233", {'country_id': '143', 'pay_mode': '1'})


payload_r = {'country_id': '143','pay_mode': '2', 'transfer_network': '1', 'transfer_network': '1',
                          'transfer_network': '1', 'send_amount': '10000', 'remit_fee': '0', 'is_create': '1',
                          'detail_info': json.dumps( {
                                            'bank_acc_number': '6214830128503751',
                                            'account_type': 'Savings',
                                            'bank_id': '41',
                                            'beneficiary': {
                                                'email': 'b@test.com',
                                                'mobile_number': '+86,150000001',
                                                'address': "address",
                                                'city': "bangkok",
                                                'full_name': "fdsfsdfdf",
                                                'first_name': "a",
                                                'last_name': "b",
                                                'purpose': "Saving",
                                                'state': "bangkok"

                                            },
                                            'remitter': {
                                                'email': 'a@test.com',
                                                'full_name': 'John',
                                                'mobile_number': '+86,150000001'
                                            }
                                        })
                          }

# payload_r = {"country_id":143,
#              "remit_fee":0,
#              "pay_mode":2,
#              "transfer_network":1,
#              "receive_amount":100,
#              "detail_info":"{\"bank_id\":\"69\",\"bank_acc_number\":\"1232132212321\",\"beneficiary\":{\"full_name\":\"jimmy.yu\",\"mobile_number\":\"86,186000001\",\"email\":\"b@test.com\"},\"remitter\":{\"full_name\":\"rldrich\",\"mobile_number\":\"86,186000002\",\"email\":\"a@test.com\"}}",
#              "is_create":1}

create_remittance("123", payload_r)


def pretty_print_POST(req):
    """
    At this point it is completely built and ready
    to be fired; it is "prepared".

    However pay attention at the formatting used in
    this function because it is programmed to be pretty
    printed and may differ from the actual request.
    """
    print('{}\n{}\n{}\n\n{}'.format(
        '-----------START-----------',
        req.method + ' ' + req.url,
        '\n'.join('{}: {}'.format(k, v) for k, v in req.headers.items()),
        req.body,
    ))

# get_detail_info("123", {'symbol': 'EXRATE'})

# get_country_info("34", {'scope': 'delivery'})

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

