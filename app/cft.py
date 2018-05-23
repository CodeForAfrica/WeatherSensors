import urllib, urllib2, base64, json, datetime
import logging
from app import app
import os

# basicAuthString = base64.encodestring('%s:%s' % (os.getenv("API_ID"), os.getenv("API_SECRET"))).replace('\n', '')
basicAuthString = os.getenv("API_TOKEN")
# Function to request data from API
def apiRequest (url, params = {}):
	# Encode optional parameters
	encodedParams = urllib.urlencode(params)
	# Set API endpoint
	request = urllib2.Request(url + '?' + encodedParams)
	# Add authorization header to the request
	request.add_header("Authorization", "Token %s" % basicAuthString)
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
		return {}

def get_stations():
	# Request stations from API
	# tahmo = apiRequest("https://tahmoapi.mybluemix.net/v1/stations")
	response = apiRequest("https://api.airquality.codeforafrica.org/v1/sensor")
	
	# decodedResponse	= json.loads(cft)

	if bool(response):
		# app.logger.info(decodedResponse)
		if response is None:
			app.logger.error("Error: %s" , response)
			return {}
			# Check if API responded with success
		elif(response):
			# Print the amount of stations that were retrieved in this API call
			app.logger.info("API call success: %d stations retrieved", len(response))
			return response
		else:
			return {}
def get_station(node_id):
	# Request stations from API
	startDate = datetime.datetime.strftime(datetime.datetime.utcnow()-datetime.timedelta(0.5),'%Y-%m-%dT%H:%M')
	response = apiRequest("https://api.airquality.codeforafrica.org/v1/node/"+node_id)
	
	# decodedResponse = json.loads(response)
	
	# Check if API responded with an error
	if bool(response):
		if response is None:
			app.logger.error("Error: %s" , response)
			return {}
		# Check if API responded with success
		elif(response):
			app.logger.info("API call success, stations retrieved")
			return response
	else:
		return {}


def get_timeseries(node_id, startDate, endDate):
    stationId = node_id
    # Generate timestamp of 48 hours ago (e.g. 2016-03-25T14:00)
    #if not startDate:
    #    startDate = datetime.datetime.strftime(datetime.datetime.utcnow()-datetime.timedelta(2),'%Y-%m-%dT%H:%M')
    # Request stations from API
    response = apiRequest("https://api.airquality.codeforafrica.org/v1/node"+node_id)
    # decodedResponse	= json.loads(response)
    # Check if API responded with an error

    if response is None:
    	app.logger.error("Error: %s" , response)
    # Check if API responded with success
    elif(response):
    	# Print the amount of stations that were retrieved in this API call
    	print "API call success:", "Station", response['uuid'], response['location']['location'], "timeseries retrieved"
    	print "Timeseries available for ", ", ".join(response['last_data_push'])

    	# Loop through temperature timeseries and print values
    	# try:
    	# 	if decodedResponse['timeseries']['temperature']:
    	# 		val = "\nTemperature measurements during last two days: \n"

    	# 		for timestamp, value in sorted(decodedResponse['timeseries']['temperature'].items()):
    	# 			val += timestamp + "," + value + "\n"
        #         return val

    	# except:
    	# 	print "Temperature timeserie starting at " + startDate + " unavailable"
    	# 	return {}
