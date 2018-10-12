# python-qpid-proton
Local setup of Apache Qpid with Python 3 producers/consumers

Pre-requirements
Docker

Get Docker CE for Ubuntu: https://docs.docker.com/install/linux/docker-ce/ubuntu/
Install Docker for Mac: https://docs.docker.com/docker-for-mac/install/

AMQP 1.0
OASIS Specification: http://docs.oasis-open.org/amqp/core/v1.0/amqp-core-complete-v1.0.pdf
Apache python-qpid-proton: https://github.com/apache/qpid-proton/tree/master/python

Docker images
fedora/qpid https://hub.docker.com/r/fedora/qpid/

docker pull fedora/qpid

python:3.6 https://hub.docker.com/_/python/
docker pull python:3.6

qpidd configuration

docker run --detach --name qpidd \
--publish 5672:5672 fedora/qpid

Connect to fedora container
docker exec -it qpidd sh

Inslall qpid-config and create queue
yum install qpid-tools
qpid-config add queue testqueue
qpid-config list queue
