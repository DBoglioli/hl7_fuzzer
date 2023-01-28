
## HL7 Protocol fuzzer
> **Warning**
> Using this tools to hack systems without authorization is illegal and can result in severe penalties including fines and imprisonment. It also poses a serious risk to individuals' life as it can have direct life-threatening consequences if messes up with critical patient data such as allergies and insulin administration.

This sctipt is to fuzz HL7 v2 protocol by injecting payloads in the message's fields. 



## HL7 Protocol basics

HL7 (Health Level Seven) is a set of standards for the exchange of electronic health information. It is considered insecure because it is based on unencrypted, plain text messaging protocols, which makes it vulnerable to eavesdropping and tampering. Additionally, HL7 messages often contain sensitive patient information.

MLLP (Minimum Lower Layer Protocol) is an application layer protocol used to transport HL7 messages over TCP/IP networks. MLLP is a simple protocol that provides a basic framework for transmitting HL7 messages between systems. It is insecure as well.

HL7 security is based on a lower layer protocol in which it is encapsulated or on custom implementations. HL7 information can be transmitted over a secure protocol such as HTTPS.

## HL7 message
 - Every line is a Segment, every segment is separated by a return character (x0d)
 - Every segment consist in one or more Composites (Fields), separated by a pipe (x7c)
 - A Composite can contain sub-composites, separated by a caret ^ (x5e)
 - 
 Messages can have different types, the type determine which health data are transmitted in the message and the segments that can be included. This means that different message types have different Segments.

 Message types can be:
 - ACK  General acknowledgment 
 - MCF  Delayed acknowledgment message. 
 - QRY  Query message. 
 - DSR  Display response message. 
 - UDM  Unsolicited display message. 
 - ADT  Admissions, discharge, transfer. 
 - ORM  Order message. 
 - ORR  Order message response. 
 - RXO  Pharmacy order. 
 - RDE  Pharmacy order information. 
 - RDS  Pharmacy dispense information. 
 - RGV  Pharmacy dose information. 
 - RAS  Pharmacy administration information. 
 - RRE  Pharmacy encoded order history report. 
 - RRD  Pharmacy dispense history report. 
 - RRG  Pharmacy give history report. 
 - RRA  Pharmacy administration report. 
 - orrRxo  Pharmacy order message response. 
 - orrRde  Pharmacy encoded order message response. 
 - orrRds  Pharmacy dispense message response. 
 - orrRgv  Pharmacy give message response. 
 - orrRas  Pharmacy administer message response. 
 - BAR  Add or change billing account. 
 - DFT  Detail financial transaction. 
 - ORU  Observation result - unsolicited. 
 - ORF  Observation result - solicited. 
 - MFN  Master Files Notification 
 - MFK  Master Files Acknowledgement 
 - MFD  Master File Update Delayed Application Acknowledgement 
 - MFQ  Master Files Query 
 - MFR Master Files Query Response

 More information about the protocol here --> http://www.hl7.org/documentcenter/private/standards/V251/HL7_Messaging_v251_PDF.zip
## Example


```sh
MSH|^~\&|EPIC|EPICADT|SMS|SMSADT|199912271408|CHARRIS|ADT^A04|1817457|D|2.5|
PID||0493575^^^2^ID 1|454721||DOE^JOHN^^^^|DOE^JOHN^^^^|19480203|M||B|254 MYSTREET AVE^^MYTOWN^OH^44123^USA||(216)123-4567|||M|NON|400003403~1129086|
NK1||ROE^MARIE^^^^|SPO||(216)123-4567||EC|||||||||||||||||||||||||||
PV1||O|168 ~219~C~PMA^^^^^^^^^||||277^ALLEN MYLASTNAME^BONNIE^^^^|||||||||| ||2688684|||||||||||||||||||||||||199912271408||||||002376853
```


## Usage
```sh
python3 main.py -p[port] -[targetIP] --payload-file[payload_file]
```


## TODO
Add feature to fuzz other Composites and Fields without editing the code.


