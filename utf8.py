import argparse

def text_to_utf8_binary(text):
    # Encode text to UTF-8 bytes
    utf8_bytes = text.encode('utf-8')
    # Convert each byte to an 8-bit binary representation
    binary_str = ' '.join(f'{byte:08b}' for byte in utf8_bytes)
    return binary_str

def utf8_binary_to_text(binary_str):
    # Split the input on spaces to get individual byte strings
    bits = binary_str.strip().split()
    # Convert each 8-bit binary string to an integer, then to a byte
    byte_values = [int(b, 2) for b in bits]
    # Convert bytes back to UTF-8 encoded text
    text = bytes(byte_values).decode('utf-8')
    return text

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Convert text to/from UTF-8 binary representation."
    )
    
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--encode', '-e', metavar='TEXT', help="Text to encode into UTF-8 binary")
    group.add_argument('--decode', '-d', metavar='BINARY', help="UTF-8 binary to decode back into text")
    
    args = parser.parse_args()

    if args.encode:
        # Encode the provided text
        result = text_to_utf8_binary(args.encode)
    else:
        # Decode the provided binary string
        result = utf8_binary_to_text(args.decode)

    print(result)