

build-mdms-image:
	docker build -t mdms-mqtt ./MDMS/

build-sm-image:
	docker build -t sm-mqtt ./SM/

setup-requirement:
	pip3 install paho-mqtt

run-compose:
	docker-compose up -d

