# python-qpid-proton
Local setup of Apache Qpid with Python 3 producers/consumers

## Pre-requirements
### Docker

Get Docker CE for Ubuntu: https://docs.docker.com/install/linux/docker-ce/ubuntu/
Install Docker for Mac: https://docs.docker.com/docker-for-mac/install/

### AMQP 1.0
OASIS Specification: http://docs.oasis-open.org/amqp/core/v1.0/amqp-core-complete-v1.0.pdf
Apache python-qpid-proton: https://github.com/apache/qpid-proton/tree/master/python

### Docker images
fedora/qpid https://hub.docker.com/r/fedora/qpid/

docker pull fedora/qpid

python:3.6 https://hub.docker.com/_/python/
```
docker pull python:3.6
```

## qpidd configuration

```
docker run --detach --name qpidd \
--publish 5672:5672 fedora/qpid
```

### Connect to fedora container
```
docker exec -it qpidd sh
```
### Inslall qpid-config and create queue
```
yum install qpid-tools
qpid-config add queue testqueue
qpid-config list queue
```

### Start python:3.6 container
```
docker run --name qpid-client -it python:3.6 sh
pip install python-qpid-proton
```

### Check if SSL is present in proton:

```
# python
>>> import proton
>>> proton.SSL.present() 
True
```

### Copy python examples:

```
docker cp send.py qpid-client:/home/
docker cp receive.py qpid-client:/home/
```

### Start python 3.6
```
docker start -i qpid-client
cd /home/
# python send.py
# python receive.py
Hello World!
```

__Note: you need to set correct IP address of qpidd container in the QPIDD_HOST var:__
QPIDD_HOST = '172.17.0.2:5672'

Docker IP address cen be faund like this:

docker inspect qpidd

check Networks->bridge->IPAddress attribute
