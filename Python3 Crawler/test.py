import requests
response = requests.get("http://books.toscrape.com/")

if response.ok:
    ...

else:
    print("Request Failure")

# if response.status_code >= 200 and response.status_code < 400:
#     ...
# elif response.status_code >= 400 and response.status_code < 500:
#     print("Request failed, Client-side error")
# elif response.status_code >= 500:
#     print("Request failed, Server-side error")