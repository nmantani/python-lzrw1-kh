# python-lzrw1-kh

This is a pure Python implementation of LZRW1/KH compression algorithm.
Python 2 and Python 3 are supported.
This implementation is based on [the C implementation by Kurt Haenen](http://www.dcee.net/Files/Programm/Packing/lzrw.arj) and [the Delphi implementation by Danny Heijl](https://www.sac.sk/download/pack/tlzrw1.zip).

This implementation is slow and not suitable for large files.

## Installation
```
pip3 install python-lzrw1-kh
```

```
pip3 install https://github.com/nmantani/python-lzrw1-kh/archive/refs/heads/master.zip
```

## Usage
lzrw1_kh.compress() and lzrw1_kh.decompress() take bytes as an argument and return compressed / decompressed bytes.

```python
>>> import lzrw1_kh
>>> lzrw1_kh.compress(b'AAAAAAAABBBBBBBBCCCCCCCC')
b'\x0c\x00@T\x00A\x00\x14B\x00\x14C\x00\x14'
>>> lzrw1_kh.decompress(b'\x0c\x00@T\x00A\x00\x14B\x00\x14C\x00\x14')
b'AAAAAAAABBBBBBBBCCCCCCCC'
>>> 
```

```python
>>> import hashlib
>>> import lzrw1_kh
>>> data = b"\x90"*1024
>>> hashlib.md5(data).hexdigest()
'e03067ea0b33933f67508ff1f8d0d4d0'
>>> compressed = lzrw1_kh.compress(data)
>>> len(compressed)
9
>>> decompressed = lzrw1_kh.decompress(compressed)
>>> len(decompressed)
1024
>>> hashlib.md5(decompressed).hexdigest()
'e03067ea0b33933f67508ff1f8d0d4d0'
>>> 
```

## Author
Nobutaka Mantani (Twitter: @nmantani)

## License
The BSD 2-Clause License (http://opensource.org/licenses/bsd-license.php)
