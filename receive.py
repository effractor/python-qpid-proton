from proton import Message
from proton.utils import BlockingConnection
from proton.handlers import IncomingMessageHandler

QPIDD_HOST = '172.17.0.2:5672'
QUEUE = 'testqueue'

conn = BlockingConnection(QPIDD_HOST)
receiver = conn.create_receiver(QUEUE)
msg = receiver.receive(timeout=30)
print(msg.body)
receiver.accept()
conn.close()
