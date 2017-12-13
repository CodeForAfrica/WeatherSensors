import urllib, urllib2, base64, json, datetime
from app import app

basicAuthString = base64.encodestring('%s:%s' % (app.config['API_ID'], app.config['API_SECRET'])).replace('\n', '')
# Function to request data from API
def apiRequest (url, params = {}):
	# Encode optional parameters
	encodedParams = urllib.urlencode(params)
	# Set API endpoint
	request = urllib2.Request(url + '?' + encodedParams)
	# Add authorization header to the request
	request.add_header("Authorization", "Basic %s" % basicAuthString)
	try:
		response = urllib2.urlopen(request)
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
    response = apiRequest("https://tahmoapi.mybluemix.net/v1/stations")
    decodedResponse	= json.loads(response)
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
    response = apiRequest("https://tahmoapi.mybluemix.net/v1/stations/"+station_id)
    decodedResponse	= json.loads(response)
# Check if API responded with an error
    if(decodedResponse['status'] == 'error'):
    	print "Error:", decodedResponse['error']
        return {}
    # Check if API responded with success
    elif(decodedResponse['status'] == 'success'):
    	print "API call success, stations retrieved"
        return decodedResponse


def get_timeseries(station_id, startDate, endDate):
    stationId = station_id
    # Generate timestamp of 48 hours ago (e.g. 2016-03-25T14:00)
    #if not startDate:
    #    startDate = datetime.datetime.strftime(datetime.datetime.utcnow()-datetime.timedelta(2),'%Y-%m-%dT%H:%M')
    # Request stations from API
    response = apiRequest("https://tahmoapi.mybluemix.net/v1/timeseries/" + stationId + "/hourly", { 'startDate': startDate, 'endDate' : endDate })
    decodedResponse	= json.loads(response)
    # Check if API responded with an error
    if(decodedResponse['status'] == 'error'):
    	print "Error:", decodedResponse['error']
    # Check if API responded with success
    elif(decodedResponse['status'] == 'success'):
    	# Print the amount of stations that were retrieved in this API call
    	print "API call success:", "Station", decodedResponse['station']['id'], decodedResponse['station']['name'], "timeseries retrieved"
    	print "Timeseries available for ", ", ".join(decodedResponse['station']['variables'])

    	# Loop through temperature timeseries and print values
    	try:
    		if decodedResponse['timeseries']['temperature']:
    			val = "\nTemperature measurements during last two days: \n"

    			for timestamp, value in sorted(decodedResponse['timeseries']['temperature'].items()):
    				val += timestamp + "," + value + "\n"
                return val

    	except:
    		print "Temperature timeserie starting at " + startDate + " unavailable"
    		return {}
