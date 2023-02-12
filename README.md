## DNS SERVER
dns server to test data structures.

run from teminal 
```
sudo python3 dns.py
```
the app needs to be run with sudo because it binds to port 53 to listen for requests.

To make a request use:
```
dig 'something.org' @127.0.0.1
```

the zone file only has one entry so you can only search for one domain. 
