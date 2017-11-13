from opcua import Client, ua
from opcua.ua import ua_binary as uabin
from opcua.common.methods import call_method


class Client:
    def __init__(self, endpoint):
        self.client = Client(endpoint)

    def __enter__(self):
        self.client.connect()
        return self.client

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.client.disconnect()

if __name__ == '__main__':

    with Client("opc.tcp://localhost:40840/iotproject/server/") as client:
        root = client.get_root_node()
        print("Root node is: ", root)
        objects = client.get_objects_node()
        print("Objects node is: ", objects)
        
        # get a specific node knowing its node id
        var = client.get_node("ns=2;i=1")
        print("Variable : ", var)
        
        name = var.get_display_name()
        print("Name :", name)
        
        text = var.get_browse_name()
        print("Text", text)
        
        children = var.get_children()
        print("Children : ", children)