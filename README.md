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

Features
--------

 - Session multiplexing: irnetproxy dynamically maps Asyncronous Sequence IDs
 on the fly, meaning that multiple clients can use the same Sequence ID
 concurrently, and the irnet box will continue to work.  Both the command
 acknowledgement, and the subsequent Async complete message are always routed
 to the correct client.

 - On/Off management: irnetproxy will silently accept the on and off messages
 (5 and 6).  A standard ACK response is returned to the client, but the command
 is never sent to the device. This allows multiple scripts to try to turn off
 the device while other devices use it.  irnetproxy issues the ON command when 
 it connects, and issues an OFF command when it is stopped.
