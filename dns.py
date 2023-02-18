import socket, glob, json

port = 53
ip = "127.0.0.1"


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((ip, port))

#add data structures for testing.
def load_zones():

    j_zone = {}
    zonefiles = glob.glob('zone/*.zone')
    
    for zone in zonefiles:
        with open(zone) as zonedata:
            data = json.load(zonedata)
            zonename = data["$origin"]
            j_zone[zonename] = data
    return j_zone
zonedata = load_zones()
print('zone loaded')

def getflags(flags):
    b1, b2 = bytes(flags[:1]), bytes(flags[1:2])
    rflags = ""
    qr = '1'
    opcode = ""
    for bit in range(1, 5):
        opcode += str(ord(b1) & (1 << bit))
    AA = "1"  # athoritative answer
    TC = "0"  # truncation
    RD = "0"  # recursion
    RA = "0"  # recursion avalible
    Z = "0000"  #
    RCODE = "0000"  #
    return int(qr + opcode + AA + TC + RD, 2).to_bytes(1, byteorder="big") + int(
        RA + Z + RCODE, 2
    ).to_bytes(1, byteorder="big")

def get_query(data):
          
    state = 0
    expectedlength = 0
    domainstring = ''
    domainparts = []
    x = 0
    y = 0
    for byte in data:
        if state == 1:
            if byte != 0:
                domainstring += chr(byte)
            x += 1
            if x == expectedlength:
                domainparts.append(domainstring)
                domainstring = ''
                state = 0
                x = 0
            if byte == 0:
                domainparts.append(domainstring)
                break
        else:
            state = 1
            expectedlength = byte
        y += 1

    questiontype = data[y:y+2]

    return (domainparts, questiontype)


    return (domainparts, questiontype)
def getzone(domain):
    global zonedata
    zone_name = '.'.join(domain)
    return zonedata[zone_name]

def get_rec(data):
    domain, questiontype = get_query(data)
    qt = ''
    print(domain, questiontype, )

    if questiontype == b'\x00\x01':
        qt = 'a'
    zone = getzone(domain)
    return (zone[qt], qt, domain)

def build_question(domain, rectype):
    qbytes = b''

    for part in domain:
        length = len(part)
        qbytes += bytes([length])

        for char in part:
            qbytes += ord(char).to_bytes(1, byteorder='big')
    if rectype == 'a':
        qbytes += (1).to_bytes(2, byteorder='big')
    qbytes += (1).to_bytes(2, byteorder='big')
    return qbytes

def rectobytes(domain, rectype, recttl, recval):
    
    rbytes = b'\xc0\xc0'
    
    if rectype == 'a':
        rbytes = rbytes + bytes([0]) + bytes([1])
   
    rbytes = rbytes + bytes([0]) + bytes([1])
    rbytes += int(recttl).to_bytes(4, byteorder='big')

    if rectype == 'a':
        rbytes =  bytes([0]) + bytes([4])
        for part in recval.split('.'):
            rbytes += bytes([int(part)])
    return rbytes

def buildresponse(data):

    transactionID = data[:2]
    flags = getflags(data[2:4])
    
    qd_count = b'\x00\x01'
    ancount = len(get_rec(data[12:])[0]).to_bytes(2, byteorder='big')
    nscount = (0).to_bytes(2, byteorder='big')
    arcount = (0).to_bytes(2, byteorder='big')

    dns_header = transactionID+flags+qd_count+ancount+nscount+arcount
    #create dns body
    dnsbody = b''
    records, rectype, domain = get_rec(data[12:])
    dnsquestion = build_question(domain, rectype)
    for record in records:
        dnsbody += rectobytes(domain, rectype, record['ttl'], record['value'])
    print(dnsbody)
    return dns_header + dnsquestion + dnsbody




while True:
    data, addr = sock.recvfrom(512)
    r = buildresponse(data)
    sock.sendto(r, addr)
