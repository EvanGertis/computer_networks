from pubnub.callbacks import SubscribeCallback
from pubnub.enums import PNStatusCategory
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub
import time
import os

pnconfig = PNConfiguration()

pnconfig.publish_key   = os.environ['PUBNUB_PUBLISH_KEY']
pnconfig.subscribe_key = os.environ['PUBNUB_SUBSCRIBE_KEY']
pnconfig.ssl = True
print(f"{pnconfig.publish_key}")
print(f"{pnconfig.subscribe_key}")

pubnub = PubNub(pnconfig)

def my_publish_callback(envelope, status):
    # Check whether request successfully completed or not
    if not status.is_error():
        pass

class MySubscribeCallback(SubscribeCallback):
    def presence(self, pubnub, presence):
        pass
    def status(self, pubnub, status):
        pass
    def message(self, pubnub, message):
        print(f'from device 1: "${message.message}')

pubnub.add_listener(MySubscribeCallback())
pubnub.subscribe().channels("chan-1").execute()

## publish a message
while True:
    msg = input("Input a message to publish: ")
    if msg == 'exit': os._exit(1)
    pubnub.publish().channel("chan-1").message(str(msg)).pn_async(my_publish_callback)
