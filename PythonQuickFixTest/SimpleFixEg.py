# Each administrative or application message is preceded by a standard header. 
# The header identifies the message type, length, destination, sequence number, 
# origination point and time
# Link:- https://www.onixs.biz/fix-dictionary/4.4/compblock_standardheader.html

# FIX 4.4: Fields by Tag – FIX Dictionary
# Link:- https://www.onixs.biz/fix-dictionary/4.4/fields_by_tag.html


import simplefix

def standard_headers():
    message = simplefix.FixMessage()

    # Standard Headers 
    message.append_pair(8, "FIX.4.4")
    message.append_pair(9, 10)
    message.append_pair(35, 0)
    message.append_pair(49, "SENDER")
    message.append_pair(56, "TARGET")
    message.append_pair(34, 4684)
    message.append_time(52, 0)
    message.append_pair(43, 'N')
    message.append_pair(122, "TR0003692")
    message.append_pair(97, 'Y')

    return message

def logon():
    message = standard_headers()

    # Logon
    message.append_pair(98, 1)
    message.append_pair(108, 0)
    message.append_pair(141, 'Y')
    message.append_pair(383, 25)

    # Standard message Trailer 
    message.append_pair(57, 'ADMIN')
    message.append_pair(10, 'E4JK')

    return message

print("\nLogon:\n",logon())


def heartbeat():
    message = standard_headers()

    # Heartbeat
    message.append_pair(112, 'EKJL')

    # Standard message Trailer 
    message.append_pair(57, 'ADMIN')
    message.append_pair(10, 'E4JK')

    return message

print("\nHeartbeat:\n",heartbeat())


def test_request():
    message = standard_headers()

    # Test Request
    message.append_pair(112, 'KLMAO')

    # Standard message Trailer 
    message.append_pair(57, 'ADMIN')
    message.append_pair(10, 'E4JK')

    return message

print("\nTest Request:\n",test_request())


def resend_request():
    message = standard_headers()

    # Resend Request
    message.append_pair(7, 10)
    message.append_pair(16, 0)

    # Standard message Trailer 
    message.append_pair(57, 'ADMIN')
    message.append_pair(10, 'E4JK')

    return message

print("\nResend Request:\n",resend_request())


def fix_protocol_error():
    message = standard_headers()

    # FIX Protocol Error / Reject
    message.append_pair(45, 897676556)
    message.append_pair(371, 43)
    message.append_pair(372, 'U2')
    message.append_pair(373, 99)
    message.append_pair(58, 'Err')

    # Standard message Trailer 
    message.append_pair(57, 'ADMIN')
    message.append_pair(10, 'E4JK')

    return message

print("\nFix Error:\n",fix_protocol_error())


def sequence_reset():
    message = standard_headers()

    # Sequence Reset
    message.append_pair(123, 'N')
    message.append_pair(36, 3245)

    # Standard message Trailer 
    message.append_pair(57, 'ADMIN')
    message.append_pair(10, 'E4JK')

    return message

print("\nSequence Reset:\n",sequence_reset())


def logout():
    message = standard_headers()

    # Logout
    message.append_pair(58, 'Logging Out...')

    # Standard message Trailer 
    message.append_pair(57, 'ADMIN')
    message.append_pair(10, 'E4JK')

    return message

print("\nLogout:\n",logout())


def order_cancel():
    message = standard_headers()

    # Order cancel request 
    message.append_pair(41, 'Jkil90j')
    message.append_pair(37, 'klmnhj')
    message.append_pair(11, 'KLM')
    message.append_pair(38, 50)
    message.append_pair(167, 'BA')
    message.append_pair(55, "[N/A]")
    message.append_pair(201, 0)
    message.append_pair(202, '$20')
    message.append_pair(200, '202205')
    message.append_pair(205, '25')
    message.append_pair(206, 'HKSE')
    message.append_pair(54, 1)

    # Standard message Trailer 
    message.append_pair(57, 'ADMIN')
    message.append_pair(10, 'E4JK')

    return message

print("\nOrder Cancel Request:\n",order_cancel())


def encode_message():
    # To create a FIX message, first create an instance of the FixMessage class.
    message = simplefix.FixMessage()

    # For most tags, using append_pair() is the easiest way to add a field to the message.
    # message.append_pair(1, "MC435967")
    # message.append_pair(54, 1)
    # message.append_pair(44, 37.0582)

    # If header set to True, after encoding header=True fields will be set to top 
    message.append_pair(8, "FIX.4.4")
    message.append_pair(35, 0)
    message.append_pair(49, "SENDER", header=True)
    message.append_pair(56, "TARGET")
    message.append_pair(112, "TR0003692")
    message.append_pair(34, 4684, header=True)
    message.append_time(52, header=True)
    message.append_pair(1, "MC435967")
    message.append_pair(54, 1)
    message.append_pair(44, 37.0582)

    # If we want to insert one or more strings to message
    # BEGIN_STRING = "8=FIX.4.2"
    # message.append_string(BEGIN_STRING)
    # STR_SEQ = ["49=SENDER", "56=TARGET"]
    # message.append_strings(STR_SEQ, header=True)

    # The FIX protocol defines four time types: UTCTimestamp, UTCTimeOnly, TZTimestamp, 
    # and TZTimeOnly
    # message.append_utc_timestamp(52, precision=6, header=True)
    # message.append_tz_timestamp(1132, my_datetime)
    # message.append_utc_time_only(1495, start_time)
    # message.append_tz_time_only(1079, maturity_time)

    # 95=17 is the len("RAW DATA \x00\x01 VALUE")
    message.append_data(95, 96, "RAW DATA \x00\x01 VALUE")

    return message

def decode_message(encoded_message):
    byte_buffer = encoded_message.encode(True)
    return byte_buffer

# enc = encode_message()
# print("Encoded Message:\n",enc)

# dec = decode_message(enc)
# print("\nDecoded Message:\n",dec)