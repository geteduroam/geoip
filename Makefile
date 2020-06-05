geoip: geoip.py GeoLite2-City.mmdb
	pip install -r requirements.txt -t ./geoip/
	cp GeoLite2-City.mmdb geoip.py geoip/

run: geoip
	python geoip/geoip.py

geoip.zip: geoip
	cd geoip; rm ../geoip.zip; zip -9 -r ../geoip.zip .
