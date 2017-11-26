from opcua import Client, ua, Subscription
from opcua.ua import ua_binary as uabin
from opcua.common.methods import call_method
from opcua.common.subscription import Subscription
from opcua.ua import VariantType


if __name__ == '__main__':

        client = Client("opc.tcp://localhost:40840/iotproject/server/")
        root = client.get_root_node()
        print("Root node is: ", root)
        objects = client.get_objects_node()
        print("Objects node is: ", objects)
        var = client.get_node(ua.NodeId(1002, 2))
        var.set_data_value(9999,ua.VariantType.Int64)
        print(var)
