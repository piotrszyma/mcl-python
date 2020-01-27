# mcl-python

`mcl-python` is a Python library that creates bindings for [mcl](https://github.com/herumi/mcl) library by 光成滋生 MITSUNARI Shigeo(herumi@nifty.com).

## Supported curves

For now the only supported curve is `BLS12_384` (named in library `BN384_256`)

## Installation

**This package requires [mcl](https://github.com/herumi/mcl) to be preinstalled.**

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install mcl-python.

```bash
pip install mcl
```

## Usage

```python
import mcl

fr = new mcl.Fr()
fr.setByCSPRNG()
```

For more examples, please check [tests](tests/).

## Tests

Tests are written in `unittest`.

```
python3 -m unittest discover tests/
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)