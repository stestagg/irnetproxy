irNetProxy
==========

A network proxy for RedRat irNetBox MK-III infra-red blaster modules.
Based on the protocol document: 

http://www.redrat.co.uk/products/IRNetBox_Comms-V3.X.pdf

This script allows many clients to connect to the device, and use the ports
concurrently.  **Note**, this only makes sense for the Asynchronous IO 
Output Commands, other commands will be run synchronously.

Usage
-----

```
$ irnetproxy -r <irNetBox address>
```

OR

```
$ irnetproxy --irnetbox-addresss <irNetBox address> --irnetbox-port 10001\
      --listen-port 10001 --listen-address 127.0.0.1 -vv
Listening for connections on 127.0.0.1:10001 
```