# DrawGly

DrawGly is a Python library for drawing **Symbol Nomenclature for Glycans (SNFG)**, using 
[GlyConnect API](https://glyconnect.expasy.org/).

## Requirements
```bash
python >= 3.9
```

## Installation

```bash
python -m pip install drawgly
```


## Usage
Using `get_cartoon()` to get the cartoon and saving the image. 
More information can be found in the docstring.

Note: This function uses [GlyConnect API](https://glyconnect.expasy.org/) to get the cartoons,
please make sure you have an internet connection.

```python
from drawgly import get_cartoon

struct_format = "gws"
structure = "freeEnd--?a1D-GalNAc,p(--3b1D-Gal,p--??2D-NeuAc,p)--6b1D-GlcNAc," \
            "p--??1D-Gal,p--??2D-NeuAc,p}--??1Ac$MONO,Und,0,0,freeEnd"
output_path = "output.png"

get_cartoon(struct_format, structure, output_path)
```

Example output:
![test](https://user-images.githubusercontent.com/65430559/232362952-30df9563-105e-4f6b-9740-f496cd969915.svg)

## License
This project is licensed under the MIT License. See the LICENSE file for more information.
