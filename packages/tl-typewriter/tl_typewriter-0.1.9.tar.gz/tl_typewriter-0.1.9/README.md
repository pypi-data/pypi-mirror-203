# tl_typewriter

## Installation
Run in command line:

```commandline
pip3 install tl_typewriter
```

## Running in the background

```commandline
tl_typewriter -w <your txt file path>
```

## Usage
z key: page + 1
spacebar key: picture + 1
b key: bubblt + 1
x key: box + 1
t key: text + 1

## update to pip
### 1. Create distribution folder
```commandline
python setup.py sdist bdist_wheel
```

### 2. Upload to pip
```commandline
twine upload dist/*
```

### to try install locally
```commandline
pip3 install dist/tl_typewriter-0.1.8-py3-none-any.whl 
```