# thule [t-OOL-ee]

A dumb, yet useful, file walker.


![Cat](./thule.png?raw=true "thule")

## Usage

1. Import `from thule import Actions, Walker`
2. Subclass Actions for your use case (e.g. `class JSONtoYAML(Actions):`)
3. Define in your class any or all of the following:
    - one or more functions suffixed with `_directory`, will run on any directory (or subdirectory) under the path passed to the walker's accept method
    - one or more functions suffixed with `_file`, will run on every file contained in any directory (or any subdirectory) under the path passed to the walker's accept method
    - one or more functions suffixed with `_final`, will run after all directories, subdirectories, and files have been visited under the path passed to the walker's accept method
4. Instantiate the subclassed Actions (e.g. `converter = JSONtoYAML()`)
5. Instantiate a Walker (e.g. `walker = Walker()`)
6. Call accept on the walker (e.g. `walker.accept(<path>, converter)`)

## Example
### JSON to YAML Converter

Starting data

```shell
├── dir1
│   ├── file2.json
│   ├── sub1
│   │   ├── file3.json
│   │   └── file4.json
│   └── sub2
│       └── file5.json
├── dir2
│   └── sub3
│       └── file6.json
├── dir3
│   ├── sub4
│   │   └── file7.json
│   └── sub5
│       ├── file8.json
│       └── file9.json
└── file1.json
```

Thule Script to convert JSON to YAML

```python
"""
json_to_yaml.py
converts all json files
in nested directories to yaml files
removes old json files
"""
import os
import sys
import json
import yaml
from thule import Actions, Walker

class JSONtoYAML(Actions):

  def __init__(self):
    self.num_processed = 0

  def print_directory(self, dir_path):
    print(f"processing files in {dir_path}")

  def convert_file(self, dir_path, file_name):
    if file_name.endswith(".json"):
      try:
        print(f"  converting {file_name}....", end="", flush=True)
        file_path = os.path.join(dir_path, file_name)
        with open(file_path, 'r') as jf:
            data = json.load(jf)
        with open(file_path.replace(".json", ".yaml"), 'w') as yf:
            yaml.dump(data, yf)
        os.remove(file_path)
        self.num_processed += 1
      except Exception:
        print("[failed]")
      else:
        print("[done]")

  def total_converted_final(self):
    print(f"{self.num_processed} files in total were converted from JSON to YAML")


if __name__ == "__main__":

  cwd = os.getcwd()
  if len(sys.argv) > 2:
    print("usage: python example.py <relative path to root dir>")
    exit(1)

  rel_path = sys.argv[1]
  abs_path = os.path.join(cwd, rel_path)

  converter = JSONtoYAML()
  walker = Walker()
  walker.accept(abs_path, converter)
```

Run the script as follows: `python json_to_yaml.py relative/path/test_json`

Script Output

```
processing files in cwd/relative/path/test_json
  converting file1.json....[done]
processing files in cwd/relative/path/test_json/dir2
processing files in cwd/relative/path/test_json/dir2/sub3
  converting file6.json....[done]
processing files in cwd/relative/path/test_json/dir3
processing files in cwd/relative/path/test_json/dir3/sub5
  converting file9.json....[done]
  converting file8.json....[done]
processing files in cwd/relative/path/test_json/dir3/sub4
  converting file7.json....[done]
processing files in cwd/relative/path/test_json/dir1
  converting file2.json....[done]
processing files in cwd/relative/path/test_json/dir1/sub1
  converting file4.json....[done]
  converting file3.json....[done]
processing files in cwd/relative/path/test_json/dir1/sub2
  converting file5.json....[done]
9 files in total were converted from JSON to YAML
```

Resulting Data

```shell
├── dir1
│   ├── file2.yaml
│   ├── sub1
│   │   ├── file3.yaml
│   │   └── file4.yaml
│   └── sub2
│       └── file5.yaml
├── dir2
│   └── sub3
│       └── file6.yaml
├── dir3
│   ├── sub4
│   │   └── file7.yaml
│   └── sub5
│       ├── file8.yaml
│       └── file9.yaml
└── file1.yaml
```
