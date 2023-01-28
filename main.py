import socket
import argparse
import csv


# Parse the command line arguments, server and port and payload file
# If no arguments are provided, use the default values
parser = argparse.ArgumentParser()
parser.add_argument("-s", "--server", help="Server IP address", default="192.168.165.130")
parser.add_argument("-p", "--port", help="Server port", default=6661)
parser.add_argument("--payload-file", help="Payload file" , default="payload.txt")


# Read the payload file reading the argparse and stores every line in a list
with open(parser.parse_args().payload_file) as f:
    payloads = f.readlines()


def create_hl7_message(family_name):
    # Create ADT^A04 message base > This represents a patient admission
    #
    # Segment types that this script creates are:
    # MSH /* Message Header */
    # PID /* Patient Identification */
    # PV1 /* Patient Visit */
    # NK1 /* Next of Kin / Associated Parties */
    hl7_msg1 = """MSH|^~\&|HL7Soup|Instance1|HL7Soup|Instance2|201407271408||ADT^A04|1817457|D|2.5.1|123456||AL"""
    hl7_msg2 = f"""PID||0797675^^^^MR|454721||{family_name}^Sam^^^^^B|Smith^Mary^^^^|19780203|M||2106-3|254 East St^^Howick^OH^3252^USA||(216)671-4859|||S|AGN|400003603~1629086|999-8888|"""
    hl7_msg3 = """NK1||Brown^Mary^^^^|MTH||(216)891-3459||EC|||||||||||||||||||||||||||"""
    hl7_msg4 = """PV1||O|O/R|A|||060277^Allen^Katrina^J^^^|||||||||| ||2668684|||||||||||||||||||||||||201407271408|"""

    separator = b'\x0d'
    hl7_msg = hl7_msg1.encode() + separator + hl7_msg2.encode() + separator + hl7_msg3.encode() + separator + hl7_msg4.encode()

    # Add MLLP start and end characters
    hl7_msg = b'\x0b' + hl7_msg + b'\x1c\x0d'

    return hl7_msg

def send_hl7_message(hl7_msg):
    # Create a socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Get the server and port from the command line arguments
    args = parser.parse_args()
    server = args.server
    port = args.port
    # Connect to the server
    s.connect((server, port))

    # Send the HL7 message
    s.sendall(hl7_msg)

    return s

def receive_response(s):
    # Receive the response with timeout
    s.settimeout(2)
    response = s.recv(1024)

    # Close the socket
    s.close()

    return response


if __name__ == "__main__":
    for payload in payloads:
        # Remove the trailing newline from the payload
        payload = payload[:-1]
        hl7_msg = create_hl7_message(payload)
        s = send_hl7_message(hl7_msg)
        try:
            response = receive_response(s)
            # Save the payload and the response in a csv file using csv library
            with open('responses.csv', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([payload, repr(response)])
        except socket.timeout:
            print('No response received')
            with open('responses.csv', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([payload, "NO RESPONSE RECEIVED"]) 
