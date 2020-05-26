# Low-Compiler (by Alejandro Lozano)

## Requirements
- Python 3.7
- ANTLR 4.8

## Installation
To install ANTLR4 use the following command:

```bash
$ cd /usr/local/lib
$ sudo curl -O https://www.antlr.org/download/antlr-4.8-complete.jar
$ export CLASSPATH=".:/usr/local/lib/antlr-4.8-complete.jar:$CLASSPATH"
$ alias antlr4='java -jar /usr/local/lib/antlr-4.8-complete.jar'
$ alias grun='java org.antlr.v4.gui.TestRig'
```
You should also install ANTLR4 python runtime in PIP:

```bash
pip install antlr4-python3-runtime
```

## Development
After installing ANTLR you can recompile the grammar by running:

```bash
$ antlr4 -Dlanguage=Python3 grammar/low.g4
```

To test a program's grammar run:

```bash
$ python3 main.py test1.txt
```
