from geoip import geoip_json

def lambda_handler(event, context):
	return {
		'statusCode': 200,
		'headers': {
			'Content-Type': 'application/json',
			'Cache-Control': 'no-store',
		},
		'body': geoip_json(event['requestContext']['http']['sourceIp']),
	}
