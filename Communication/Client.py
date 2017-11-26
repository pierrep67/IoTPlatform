from opcua import Client, ua, Subscription
from opcua.ua import ua_binary as uabin
from opcua.common.methods import call_method
from opcua.common.subscription import Subscription
from opcua.ua import VariantType

import sys
sys.path.insert(0, "..")

if __name__ == '__main__':

        client = Client("opc.tcp://localhost:40840/iotproject/server/")
        client.connect()
        
        root = client.get_root_node()
        print("Root node is: ", root)
        print("Children of root are: ", root.get_children())
        objects = client.get_objects_node()
        print("Objects node is: ", objects)
        
        # Now getting a variable node using its browse path
        myvar = root.get_child(["0:Objects", "2:MyObject", "2:MyStringVariable"])
        
        print("myvar is: ", myvar)
        mystrg = myvar.get_data_value()
        print("Mystrg is :",mystrg)
        
        myval = myvar.get_value()
        print("My value is :",myval)
        
        myvar.set_value("Good bye !")
        
        myval = myvar.get_value()
        print("My value is :",myval)
        
        print("node :",client.get_node(ua.NodeId(1003, 2)))