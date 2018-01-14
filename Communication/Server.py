import sys
import time
from opcua import ua, Server

if __name__ == "__main__":

    ## The server is set up
    server = Server()
    server.set_endpoint("opc.tcp://localhost:40840/iotproject/server/") #endpoint url : where the webservice can be accessed by a client application
    
    uri = "http://iotproject.communication"  #"URI : a Uniform Resource Identifier (URI) is a string of characters used to identify a resource."
    idx = server.register_namespace(uri) #"namespace : set of symbols that are used to organize objects of various kinds, so that these objects may be referred to by name"

    objects = server.get_objects_node() #this is where we should put our nodes

    myobj = objects.add_object(idx, "MyObject") #Object creation
    myvar = myobj.add_variable(idx, "MyVariable", 1.0) #Variable creation
    myvar.set_writable()  #The previous variable is defined as writable
    mystring  = myobj.add_variable(idx, "MyStringVariable", "Hello world !") #A string variable is added to the object "myobj"
    mystring.set_writable() #The string variable is defined as writable

    ## The server is started
    server.start()
    print("Server started !")
    
    ##The server is running
    try:
        while True:
            time.sleep(1)
    finally:
        server.stop()
        print('Server stopped !')
