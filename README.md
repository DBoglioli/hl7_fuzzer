 This sctipt is to fuzz HL7 v2 protocol by injecting payloads in the message's fields.
 TODO: add feature to fuzz other Composites and Fields without edit the code. 

 Create the HL7 message
 Every line is a Segment, every segment is separated by a return character (x0d)
 Every segment consist in one or more Composites (Fields), separated by a pipe (x7c)
 A Composite can contain sub-composites, separated by a caret ^ (x5e)
 Messages can have different types, the type determine which health data are transmitted in the message and the segments that can be included. 
 This means that different message types have different Segments.

 Message types can be:

 ack  General acknowledgment 

 mcf  Delayed acknowledgment message. 

 qry  Query message. 

 dsr  Display response message. 

 udm  Unsolicited display message. 

 adt  Admissions, discharge, transfer. 

 orm  Order message. 

 orr  Order message response. 

 rxo  Pharmacy order. 

 rde  Pharmacy order information. 

 rds  Pharmacy dispense information. 

 rgv  Pharmacy dose information. 

 ras  Pharmacy administration information. 

 rre  Pharmacy encoded order history report. 

 rrd  Pharmacy dispense history report. 

 rrg  Pharmacy give history report. 

 rra  Pharmacy administration report. 

 orrRxo  Pharmacy order message response. 

 orrRde  Pharmacy encoded order message response. 

 orrRds  Pharmacy dispense message response. 

 orrRgv  Pharmacy give message response. 

 orrRas  Pharmacy administer message response. 

 bar  Add or change billing account. 

 dft  Detail financial transaction. 

 oru  Observation result - unsolicited. 

 orf  Observation result - solicited. 

 mfn  Master Files Notification 

 mfk  Master Files Acknowledgement 

 mfd  Master File Update Delayed Application Acknowledgement 

 mfq  Master Files Query 

 mfr Master Files Query Response

 More information about the protocol here http://www.hl7.org/documentcenter/private/standards/V251/HL7_Messaging_v251_PDF.zip