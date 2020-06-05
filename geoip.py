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
		try:
			response = reader.city(web.ctx.ip)
			return json.dumps({
				'country': response.country.iso_code,
				'geo': {
					'lat': response.location.latitude,
					'lon': response.location.longitude,
				}
			})
		except geoip2.errors.AddressNotFoundError as e:
			return json.dumps({'err': str(e)})

if __name__ == "__main__":
	app.run()
