# Calcium implementation
Calcium language implementation using the Alchemist compiler infrastructure

## Dependencies
- [alchemist-compiler/front](https://github.com/alchemist-compiler/front)
- [calcium-lang/spec](https://github.com/calcium-lang/spec)

To install the dependencies, run:

```shell
git clone https://github.com/alchemist-compiler/front.git alchemist-front
git clone https://github.com/calcium-lang/spec.git calcium-spec
```

## Building
To build the most recent parser.py file, first make sure you have [`cog`](https://pypi.org/project/cogapp) installed:

```shell
pip3 install cogapp
```

Once you have installed all requirements, run:

```shell
cog -I./:./alchemist-front:./calcium-spec -r calcium/parser.py
```
