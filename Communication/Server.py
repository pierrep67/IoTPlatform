import sys
sys.path.insert(0, "..")
import time

from opcua import ua, Server

if __name__ == "__main__":

    # setup our server
    server = Server()
    server.set_endpoint("opc.tcp://localhost:40840/iotproject/server/")
    
    # setup our own namespace, not really necessary but should as spec
    uri = "http://iotproject.communication"
    idx = server.register_namespace(uri)

    # get Objects node, this is where we should put our nodes
    objects = server.get_objects_node()

    # populating our address space
    myobj = objects.add_object(idx, "MyObject")
    myvar = myobj.add_variable(idx, "MyVariable", 6.7)
    myvar.set_writable(True)   

    # starting!
    server.start()
    
    #The server is running
    try:
        count = 0
        while True:
            time.sleep(1)
            count += 0.1
            myvar.set_value(count)
            
    finally:
        server.stop()
        print('Server stopped !')
