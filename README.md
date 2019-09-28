# Summary
This is a basic Python based tool that merges two Apache Cassandra YAML config files. It uses the concept of [symmetric difference](https://en.wikipedia.org/wiki/Symmetric_difference) in sets to merge the files. The tool will also detect whether both files are identical (e.g. config files contain identical keys or key/value property pairs). 

## Requirements
- Python 2.7 or higher
- PyYAML 3.10
- Apache Cassandra YAML configuration files

## Installation

The recommended way of installing this tool is to use [virtualenv](https://virtualenv.pypa.io/en/stable/) to create an isolated Python environment.

0. Assuming pip is installed - install the required dependencies -
``` 
pip install -r cassandra_config/requirements.txt
```

## Usage
0. Run driver.py in cassandra_config - this will display a helper detailing how to run the application
0. To merge two Cassandra config files run the following: 
```
driver.py --current-yaml-config cassandra_current.yaml --new-yaml-config cassandra_new.yaml --merged-yaml-config cassandra_merged.yaml
```
