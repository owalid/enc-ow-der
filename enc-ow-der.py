import argparse as ap
import base64
from argparse import RawTextHelpFormatter

def enc_ow_der(payload, b64=False, from_char_code=False, uni=False, verbose=False):
    args = parser.parse_args()
    payload = args.input

    if verbose:
        print('[+] Input: ' + payload)

    if b64:
        payload = base64.b64encode(payload.encode('utf-8')).decode('utf-8')
        if verbose:
            print('[+] Base64 encoded: ' + payload)

    if from_char_code:
        res = 'String.fromCharCode('
        for i in range(len(payload)):
            res += str(ord(payload[i])) + ','
        res = res[:-1] + ')'
        payload = res
    elif not b64:
        res = ''
        for i in range(len(payload)):
            res += '\\x' + hex(ord(payload[i]))[2:]
        payload = res

    return payload

if __name__ == '__main__':
    parser = ap.ArgumentParser(formatter_class=RawTextHelpFormatter)
    parser.add_argument("-i", "--input", required=True, type=str, help='input string')
    parser.add_argument("-b64", "--base-64", required=False, action='store_true', default=False, help='encode as base64')
    parser.add_argument("-fchar", "--from-char-code", required=False, action='store_true', default=False, help='output the result with fromCharCode function')
    parser.add_argument("-v", "--verbose", required=False, action='store_true', default=False, help='verbose')
    
    args = parser.parse_args()
    payload = enc_ow_der(args.input, b64=args.base_64, from_char_code=args.from_char_code, verbose=args.verbose)

    if args.verbose:
        print('\n[+] Output:')
    print(payload)
    
