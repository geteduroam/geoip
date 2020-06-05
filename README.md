# GeoIP

A simple webservice that returns the location of the user based on IP address

- Add GeoLite2-City.mmdb from maxmind.com (free account required)
- Install dependencies and start the server by running `make` 

		make run

## Running on Amazon Lambda

- Build a deployment .zip by running

		make geoip.zip

- Upload the zip to an S3 bucket (it's too big to upload to Lamba directly)
- In AWS, create an empty Lamba function
- In the section for Function code, pick your S3 url, Python 3.8 and set handler to `geoip.lambda_handler`
