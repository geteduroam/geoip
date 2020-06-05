testvenv:
	test -n "$$VIRTUAL_ENV"
	make run

pip:
	pip install -r requirements.txt

run: pip
	python geoip.py

.PHONY: testvenv pip run