from proton import Message
from proton.utils import BlockingConnection
from proton.handlers import IncomingMessageHandler

QPIDD_HOST = '172.17.0.2:5672'
QUEUE = 'testqueue'

conn = BlockingConnection(QPIDD_HOST)
sender = conn.create_sender(QUEUE)
sender.send(Message(body='Hello World!'))
conn.close()
