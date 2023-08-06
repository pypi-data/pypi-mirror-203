# doc2python

Extracts the text from .doc files as a string. This Project is early in development and only has very limited functionality

## Installation
```bash
    pip install doc2python
```

## Use

``` python
from doc2python import reader

text = reader.toString('path/to/file.doc')
```
'doc2python' reads the UTF-8 encoded bitstream contained in the file and converts it to a readable string.
At this point in time some special characters are not supported and metadata might get extracted alongside the text.

## Roadmap
- support for more special characters
- add a parameter, which allows for user input of byte -> character conversion sheets