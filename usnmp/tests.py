import usnmp

#convert a packet copied from wireshark ... as a Hex Stream
#to a bytearray
def ws2ba(s):
    b = bytearray()
    ptr = 0
    while ptr<len(s):
        b.append(int(s[ptr:ptr+2],16))
        ptr += 2
    return b

#FAILS, current code

#single item get-request
s="30260201000403414643a01c020433783ac0020100020100300e300c06082b060102010101000500"
s=ws2ba(s)
s==pack(unpack(s))

#single item get-response, long string
s="3081ea0201000403414643a281df020433783ac00201000201003081d03081cd06082b060102010101000481c0436973636f20494f5320536f6674776172652c20433337353020536f667477617265202843333735302d414456495053455256494345534b392d4d292c2056657273696f6e2031322e322834362953452c2052454c4541534520534f4654574152452028666332290d0a436f707972696768742028632920313938362d3230303820627920436973636f2053797374656d732c20496e632e0d0a436f6d70696c6564205468752032312d4175672d30382031353a3433206279206e616368656e"
s=ws2ba(s)
s==pack(unpack(s))

#single item get-response, OID
s="302f0201000403414643a225020433783ac30201000201003017301506082b0601020101020006092b0601040109018404"
s=ws2ba(s)
s==pack(unpack(s))

#single item get-response, timeticks
s="302a0201000403414643a220020433783ac60201000201003012301006082b06010201010300430415f8605a"
s=ws2ba(s)
s==pack(unpack(s))

#multi item get-response (response to prior get-next-request)
s="3081d20201000403414643a281c702043821eea10201000201003081b8300f060a2b0601020102020101010201013013060a2b0601020102020102010405566c616e31300f060a2b0601020102020103010201353010060a2b060102010202010401020205dc3012060a2b06010201020201050142043b9aca003014060a2b0601020102020106010406001b8ff4d1c0300f060a2b060102010202010701020102300f060a2b0601020102020108010201023010060a2b06010201020201090143022c06300f060a2b060102010202010a01410100"
s=ws2ba(s)
s==pack(unpack(s))

#FAILS, current code

#multi item get-next-request
s="3081b00201000403414643a181a5020433783ac9020100020100308196300d06092b06010201020201010500300d06092b06010201020201020500300d06092b06010201020201030500300d06092b06010201020201040500300d06092b06010201020201050500300d06092b06010201020201060500300d06092b06010201020201070500300d06092b06010201020201080500300d06092b06010201020201090500300d06092b060102010202010a0500"
s=ws2ba(s)
s==pack(unpack(s))
