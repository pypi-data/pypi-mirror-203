# OME Schema Python Package

This Python package contains a copy of the OME (Open Microscopy Environment) XML schema, which is used to define the structure of OME-XML metadata for biological imaging data.

## Contents

- `ome.xsd`: The OME XML schema definition file.
- `LICENSE.txt`: The license file for the content of this repository.
- `README.md`: This README file, containing information about the repository and its contents.
- `ome-schema.py`: The main Python script to access the OME schema path.

## License

### Python Package

This Python package is licensed under the [MIT License](https://opensource.org/licenses/MIT). For more information, please see the `LICENSE` file.

### OME XML Schema

The OME XML schema (`2016-06/ome.xsd`) is licensed under the [Creative Commons Attribution 3.0 Unported License](https://creativecommons.org/licenses/by/3.0/). You are free to share and adapt the schema, as long as you provide appropriate attribution. For more information see the schema document for details.

## Attribution

The OME XML schema is developed and maintained by the [OME Consortium](https://www.openmicroscopy.org/). The original source of the schema can be found at the [OME Model and Formats GitHub repository](https://github.com/ome/ome-model).

## Usage

To use the OME XML schema in your Python project, install the `ome-schema` package and use the `get_ome_schema_path()` function from the `ome-schema` module:

```python
from omeschema import get_ome_schema_path

schema_path = get_ome_schema_path()
```
For more information about OME-XML and working with the schema, please refer to the [OME Data Model and File Formats documentation](https://docs.openmicroscopy.org/ome-model/)

## Installation

To install the ome-schema package, use pip:

```bash
pip install ome-schema
```

## Contributing

This repository is a mirror of the OME XML schema from the [OME Model and Formats GitHub repository](https://github.com/ome/ome-model). If you would like to contribute to the development of the schema, please visit the original repository and follow their contribution guidelines.

