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

Tests can be run with from with in a  virtural envirnment with these comands
```
source venv/bin/activate
pip3 install pytest
pytest
```
There is an error in the body of the code that adds an extra byte to the resposne.
I am hoping that I can get the test to measure the diffrent data structures to produce some data for graphs. 
