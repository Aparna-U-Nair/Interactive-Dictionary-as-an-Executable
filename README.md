## English Dictionary

This is a python based interactive dictionary in which you can get the meaning of any existing english word and it will also suggest the words in case of typos. The dictionary is generated with 2 different approaches, one taking the vocabulary data from a JSON file and the other from a DB (mysql-connector is used here)

Along with this, the python scripts are shared as exceutables too, so that any one can simply download the build folder and use the dictionary in their terminal (even if python is not present in their system). For this we can use the python library 'cx_freeze'.

To create an executable use the setup.py file and provide the name of the python file in executables.

### Requirements
```sh
pip install cx-Freeze
pip install mysql-connector-python
```
### Getting Started
```sh
python interactive_dict.py
python interactive_dict_withDB.py
python setup.py build  #to build the exe file.
```

