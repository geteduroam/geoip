import geoip2.database
import web
import json

reader = geoip2.database.Reader('GeoLite2-City.mmdb')

urls = (
	'/geolocate', 'geoip'
)
app = web.application(urls, globals())

class geoip:
	def GET(self):
		web.header('Content-Type', 'application/json')
		return geoip_json(web.ctx.ip)

def geoip_json(ip):
	try:
		response = reader.city(ip)
		return json.dumps({
			'country': response.country.iso_code,
			'city': response.city.name,
			'postal': response.postal.code,
			'geo': {
				'lat': response.location.latitude,
				'lon': response.location.longitude,
			}
		})
	except geoip2.errors.AddressNotFoundError as e:
		return json.dumps({'err': str(e)})

def lambda_handler(event, context):
	return {
		'statusCode': 200,
		'headers': {
			'Content-Type': 'application/json'
		},
		'body': geoip_json(event['requestContext']['http']['sourceIp'])
	}

if __name__ == "__main__":
	app.run()
