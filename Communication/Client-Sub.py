from opcua import ua, Client
from opcua.common import manage_nodes
import time

#Receive and digest events
class SubHandler(object):
    def data_change(self, handle, node, val, attr):
        print("New data change event", handle, node, val, attr)
    
    def event(self, handle, event):
        print("New event", handle, event)

if __name__ == "__main__": 
    client = Client("opc.tcp://localhost:40840/iotproject/server/")
    client.connect()
    
    root = client.get_root_node()
   
    objects = client.get_objects_node()
    var = client.get_node(ua.NodeId(1002, 3))
    print(var)

    #subscribing to data change event to our variable
    handler = SubHandler()
    sub = client.create_subscription(500, handler)
    handle = sub.subscribe_data_change(var)
    
    print("This client has subscribe to a node data value modification")
    
    time.sleep(30)
    client.disconnect()