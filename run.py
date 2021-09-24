import requests
api = "https://www.clubhouseapi.com/api/"
usertoken = input ("Enter your Token : ")
action = input("Enter your action: ")
code = input("Enter channel code: ")
url = (api+action)

data = "{\r\n \"channel\":\"%s\"\r\n}" % code
for i in range(1):
 headers = {
 'CH-Languages': 'en-US',
 'CH-Locale': 'en_US',
 'Accept': 'application/json',
 'Accept-Encoding': 'gzip, deflate',
 'CH-AppBuild': '588',
 'CH-AppVersion': '1.0.10',
 'CH-UserID': '736014831',
 'User-Agent': 'clubhouse/588 (iPhone; iOS 15; Scale/2.00)',
 'Connection': 'close',
 'Content-Type': 'application/json; charset=utf-8',
 'Authorization': 'Token '+usertoken
 }
response = requests.request ("POST", url, headers=headers, data=data)
print (response.text)
