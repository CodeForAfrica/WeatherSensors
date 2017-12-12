import urllib, urllib2, base64, json
from django.conf import settings
# Generating base64 encoded authorization string
basicAuthString 	= base64.encodestring('%s:%s' % (settings.API_ID, settings.API_SECRET)).replace('\n', '')
# Function to request data from API
def apiRequest (url, params = {}):
	# Encode optional parameters
	encodedParams 		= urllib.urlencode(params)
	# Set API endpoint
	request 			= urllib2.Request(url + '?' + encodedParams)
	# Add authorization header to the request
	request.add_header("Authorization", "Basic %s" % basicAuthString)

	try:
		response 		= urllib2.urlopen(request)
		return response.read()
	except urllib2.HTTPError, err:
		if err.code == 401:
			print "Error: Invalid API credentials";
			quit()
		elif err.code == 404:
			print "Error: The API endpoint is currently unavailable";
			quit()
		else:
			print err
			quit()

def get_stations():
# Request stations from API
    response 				= apiRequest("https://tahmoapi.mybluemix.net/v1/stations")
    decodedResponse			= json.loads(response)

# Check if API responded with an error
    if(decodedResponse['status'] == 'error'):
    	print "Error:", decodedResponse['error']
        return {}
    # Check if API responded with success
    elif(decodedResponse['status'] == 'success'):
    	# Print the amount of stations that were retrieved in this API call
    	print "API call success:", len(decodedResponse['stations']), "stations retrieved"
        return decodedResponse['stations']



def get_station(station_id):
# Request stations from API
    response 				= apiRequest("https://tahmoapi.mybluemix.net/v1/stations/"+station_id)
    decodedResponse			= json.loads(response)

# Check if API responded with an error
    if(decodedResponse['status'] == 'error'):
    	print "Error:", decodedResponse['error']
        return {}
    # Check if API responded with success
    elif(decodedResponse['status'] == 'success'):
    	# Print the amount of stations that were retrieved in this API call
    	#print "API call success:", decodedResponse, "stations retrieved"
        return decodedResponse
