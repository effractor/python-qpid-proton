# python-qpid-proton
Local setup of Apache Qpidd with Python 3.6 producers/consumers.

## Pre-requirements
### Docker

* [Docker CE for Ubuntu](https://docs.docker.com/install/linux/docker-ce/ubuntu/)
* [Docker for Mac](https://docs.docker.com/docker-for-mac/install/)

### AMQP 1.0

* [OASIS Specification](http://docs.oasis-open.org/amqp/core/v1.0/amqp-core-complete-v1.0.pdf)
* [Apache python-qpid-proton](https://github.com/apache/qpid-proton/tree/master/python)

### Docker images

#### [fedora/qpid](https://hub.docker.com/r/fedora/qpid/)

```
$ docker pull fedora/qpid
```

#### [python:3.6](https://hub.docker.com/_/python/)

```
$ docker pull python:3.6
```

## `qpidd` configuration

### Start `qpidd` container
```
$ docker run --detach --name qpidd \
  --publish 5672:5672 fedora/qpid
```

### Connect to `qpidd` container

```
$ docker exec -it qpidd sh
```

### Inslall `qpid-config` and create queue

```
# yum install qpid-tools
# qpid-config add queue testqueue
# qpid-config list queue
```

## Setup Python producer & consumer

### Start `python:3.6` container

```
$ docker run --name qpid-client -it python:3.6 sh
```

### Install `qpid-proton`

```
# pip install python-qpid-proton
```

### Check if `SSL` is present in proton

```
# python
>>> import proton
>>> proton.SSL.present() 
True
```

### Copy Python examples:

```
$ docker cp send.py qpid-client:/home/
$ docker cp receive.py qpid-client:/home/
```

### Start (if needed) container with a Python code

```
$ docker start -i qpid-client
```

### Test if producer & consumer works

```
# cd /home/
# python send.py
# python receive.py
Hello World!
```

__Note: you may need to set correct IP address of qpidd container:__

```
QPIDD_HOST = '172.17.0.2:5672'
```

Docker IP address cen be found by using `docker inspect`:

```
docker inspect qpidd
```

IP address is in the `Networks->bridge->IPAddress` attribute.
