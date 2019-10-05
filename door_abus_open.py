import time
import cookielib
import urllib2
import base64

login = urllib2.quote(base64.b64encode(b'LOGINNAME'))
password = urllib2.quote(base64.b64encode(b'PASSWORD'))
door = 3 # REPLACE

ts = time.time()

cookies = cookielib.LWPCookieJar()
handlers = [
    urllib2.HTTPHandler(),
    urllib2.HTTPSHandler(),
    urllib2.HTTPCookieProcessor(cookies)
    ]
opener = urllib2.build_opener(*handlers)

def fetch(uri):
    req = urllib2.Request(uri)
    return opener.open(req)

def dump():
    for cookie in cookies:
        print cookie.name, cookie.value
	return cookie.value

uri = 'http://abus/login.cgi?ts=' + str(int(ts)) + '&Source=Webpage&Username=' + login + '&Password=' + password + '&Action=Start'
response = fetch(uri)
the_page = response.read()
print (the_page)
session = dump() # Session ID

uri = 'http://abus/setRemoteAccess.cgi?ts=' + str(int(ts)) + '&Source=Webpage&LoxxId=' + str(door) + '&Action=Start'
response = fetch(uri)
the_page = response.read()
print (the_page)

uri = 'http://abus/logout.cgi?ts=' + str(int(ts)) + '&Source=Webpage&Session=' + session + '&Action=Start'
response = fetch(uri)
the_page = response.read()
