import time
import urllib2
import simplejson

# Define search term
searchTerm = "eagle"

# Replace spaces ' ' in search term for '%20' in order to comply with request
searchTerm = searchTerm.replace(' ', '%20')


# Notice that the start changes for each iteration in order to
# request a new set of images for each loop
url = ('https://ajax.googleapis.com/ajax/services/search/images?' +
       'v=1.0&q=' + searchTerm + '&start=10' '&userip=MyIP')

request = urllib2.Request(url, None, {'Referer': 'testing'})
response = urllib2.urlopen(request)

# Get results using JSON
results = simplejson.load(response)
data = results['responseData']
dataInfo = data['results']

# Assign the first result of the search to a variable
myUrl = dataInfo

# Sleep for one second to prevent IP blocking from Google
time.sleep(1)
