import sys
import requests
import re

username = 'username'
password = 'password'

# act as a web browser
header = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36' }
form_data = {'username': username,
    'password': password,
    'execution':'e1s1',
    '_eventId':'submit', 
    'submit':'Login',
    'lt':'' #string get from last post, do not know what does it mean
    }

# use requests, get session, do not need to worry about cookie
s = requests.session()

# first login in, get 'lt'
url = 'https://login.uconn.edu/cas/login'
resp = s.post(url,headers = header)

#<input type="hidden" name="lt" value="(?P<lt>.*)" />
lt = re.search('<input\s+?type="hidden"\s+?name="lt"\s+?value="(?P<lt>.*)"\s+?/>', resp.text)

# use lt to log in, the second time
form_data['lt'] = lt.group("lt") 
resp = s.post(url, data=form_data, allow_redirects=True,headers = header)

# save it in file
f = open('test','w')
f.write(resp.text)
f.close()

# log out
url = 'https://login.uconn.edu/cas/logout'
resp = s.post(url)
