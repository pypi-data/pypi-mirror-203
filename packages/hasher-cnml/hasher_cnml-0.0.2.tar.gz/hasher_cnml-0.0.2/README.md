# Hasher

![GitHub](https://img.shields.io/github/license/cn-ml/hasher?logoColor=%23&style=for-the-badge)
![PyPI](https://img.shields.io/pypi/v/hasher-cnml?style=for-the-badge)

Command line interface to the hashlib library.

## Installation

Install hasher from [PyPI](https://pypi.org/project/hasher-cnml/).

```bash
pip install hasher-cnml
```
    
## Usage

Create a checksum (defaults to MD5) of the a sample file using:

```bash
python -m hasher file_to_hash.txt
```

Or instead specify the hash algorithm directly (all algorithms from hashlib that are available locally)

```bash
python -m hasher -a sha1 file_to_hash.txt
```

View the usage information:

```bash
python -m hasher -h
```

## Authors

- [@cn-ml](https://www.github.com/cn-ml)
