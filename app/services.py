import urllib, urllib2, base64, json, datetime
import logging
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
			app.logger.error("Error: Invalid API credentials")
			#print "Error: Invalid API credentials";
		elif err.code == 404:
			app.logger.error("Error: The API endpoint is currently unavailable")
			#print "Error: The API endpoint is currently unavailable";
		else:
			print err
		return {};

def get_stations():
	# Request stations from API
	response = apiRequest("https://tahmoapi.mybluemix.net/v1/stations")
	decodedResponse	= json.loads(response)
	if bool(decodedResponse):
		if(decodedResponse['status'] == 'error'):
			app.logger.error("Error: %s" , decodedResponse['error'])
			return {}
			# Check if API responded with success
		elif(decodedResponse['status'] == 'success'):
			# Print the amount of stations that were retrieved in this API call
			app.logger.info("API call success: %d stations retrieved", len(decodedResponse['stations']))
			return decodedResponse['stations']
		else:
			return {}
def get_station(station_id):
	# Request stations from API
	startDate = datetime.datetime.strftime(datetime.datetime.utcnow()-datetime.timedelta(0.5),'%Y-%m-%dT%H:%M')
	response = apiRequest("https://tahmoapi.mybluemix.net/v1/timeseries/"+station_id+ "/hourly", { 'startDate': startDate})
	decodedResponse	= json.loads(response)
	# Check if API responded with an error
	if bool(decodedResponse):
		if(decodedResponse['status'] == 'error'):
			app.logger.error("Error: %s" , decodedResponse['error'])
			return {}
		# Check if API responded with success
		elif(decodedResponse['status'] == 'success'):
			app.logger.info("API call success, stations retrieved")
			return decodedResponse
	else:
		return {}


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
    	app.logger.error("Error: %s" , decodedResponse['error'])
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
