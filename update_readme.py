#!/usr/bin/env python3

import yaml
import pathlib

header_md = """
### A collection of bioinformatics tools for use with [Galaxy](https://galaxyproject.org/) written at Quadram Institute

[![Build Status](https://travis-ci.com/quadram-institute-bioscience/galaxy-tools.svg?branch=master)](https://travis-ci.com/quadram-institute-bioscience/galaxy-tools)
"""

def update(path="tools"):
    print(path)
    shed_files = pathlib.Path(path).glob("*/.shed.yml")
    _holder = []
    with open("README.md", "w") as fh:
        fh.write(header_md)
        for shed_file in shed_files:
            _shed_content = yaml.load(open(shed_file,'r'))
            _holder.append(
                {
                    "name": _shed_content["name"],
                    "description": _shed_content["description"],
                    "homepage_url": _shed_content["homepage_url"]
                }
            )
            _sorted_holder = sorted(_holder, key = lambda i: i['name'])
        
        for item in _sorted_holder:
            _str_line = "- **[{0}]({1})** {2}\n".format(item["name"], item["homepage_url"], item["description"])
            fh.write(_str_line)

if __name__ == "__main__":
    update()