from geoip import geoip_json

def lambda_handler(event, context):
	# event['requestContext']['http']['sourceIp']
	# event['requestContext']['identity']['sourceIp']
	# event['headers']['X-Forwarded-For']
	e = event
	e = e.get('headers', e)
	e = e.get('requestContext', e)
	e = e.get('http', e)
	e = e.get('identity', e)
	ip = e.get('sourceIp', None) or e.get('X-Forwarded-For', '').split(',')[0]

	return {
		'statusCode': 200,
		'headers': {
			'Content-Type': 'application/json',
			'Cache-Control': 'no-store',
		},
		'body': geoip_json(ip),
	} if ip else {
		'statusCode': 400,
		'headers': {
			'Content-Type': 'text/plain',
			'Cache-Control': 'no-store',
		},
		'body': 'Unable to find client IP address in event object',
	}
