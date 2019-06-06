import requests
headers = {}
headers['Authorization'] = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTU5NDg1NzMyLCJqdGkiOiJhZThiNTcxNGI2OTQ0YmU4YTdmNzlkYjUyM2U1YmI4NyIsInVzZXJfaWQiOjF9.dmuI6awzWWOyHn1SI3mc28AAnBnhh7toVrfydzjXkPo'

r =requests.get('http://127.0.0.1:8000/paradigm/', headers=headers)

print(r.text)