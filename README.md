# python-lzrw1-kh

This is a pure Python implementation of LZRW1/KH compression algorithm.
Python 2 and Python 3 are supported.
This implementation is based on [the C implementation by Kurt Haenen](http://www.dcee.net/Files/Programm/Packing/lzrw.arj) and [the Delphi implementation by Danny Heijl](https://www.sac.sk/download/pack/tlzrw1.zip).

This implementation is slow and not suitable for large files.

## Installation
```
pip3 install python-lzrw1-kh
```

or

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
>>> lzrw1_kh.compress(b'Hello, world!')
b'\x0e\x00\x80Hello, world!'
>>> lzrw1_kh.decompress(b'\x0e\x00\x80Hello, world!')
b'Hello, world!'
>>>
```

## Author
Nobutaka Mantani (Twitter: @nmantani)

## License
The BSD 2-Clause License (http://opensource.org/licenses/bsd-license.php)
