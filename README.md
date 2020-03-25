# DroneCode
Python script for controlling ANAFI Parrot drone.


### For test server
1. Move to branch test-server locally.
2. Run command: `$env:FLASK_APP = "rest_controller.py"`
3. To start server run command: `flask run --host=0.0.0.0`

#### Flask REST API doc
Note: Urls are case sensitive! All HTTP request have method POST.

**Connect to drone**
URL: `localhost:PORT/connectToDrone` 


**Disconnect from drone**
URL: `localhost:PORT/abort` 


**Take off**
URL: `localhost:PORT/takeOff` 


**Land**
URL: `localhost:PORT/land` 


**Move to gps coordinate**
URL: `localhost:PORT/moveTo` 

Body example:
```json
{
    "latitiude": 69,
    "longitude": 69,
    "altitude": 69
}
```
