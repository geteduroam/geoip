geoip: geoip.py GeoLite2-City.mmdb
	pip3 install --upgrade -r requirements.txt -t ./geoip/
	cp GeoLite2-City.mmdb geoip.py geoip/

run: geoip
	python3 geoip/geoip.py

geoip.zip: lambda_function.py geoip
	cp lambda_function.py GeoLite2-City.mmdb geoip/
	cd geoip; rm -f ../geoip.zip && zip -9 -r ../geoip.zip .
