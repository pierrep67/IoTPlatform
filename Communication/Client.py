from opcua import Client, ua, Subscription
from opcua.ua import ua_binary as uabin
from opcua.common.methods import call_method
from opcua.common.subscription import Subscription
from opcua.ua import VariantType

if __name__ == '__main__':

        ## Client creation and connection
        client = Client("opc.tcp://localhost:40840/iotproject/server/")
        client.connect()
        

        root = client.get_root_node() # The root node is got
        print("Root node is: ", root)
        print("Children of root are: ", root.get_children()) # The root node children are got
        objects = client.get_objects_node()
        print("Objects node is: ", objects) #Object nodes are listed
        
        # Now a variable is got using its browse path
        myvar = root.get_child(["0:Objects", "2:MyObject", "2:MyStringVariable"])
        print("myvar is: ", myvar) 
        
        # A string variable data value is got
        mystrg = myvar.get_data_value()
        print("Mystrg is :",mystrg)
        
        # A variable value is got, modified and checked
        myval = myvar.get_value()
        print("My value is :",myval)
        myvar.set_value("Good bye !")
        myval = myvar.get_value()
        print("My value is :",myval)