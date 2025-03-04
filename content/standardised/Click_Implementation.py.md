https://github.com/rhyslwells/ML_Tools/tree/main/Explorations\Utilities\Click_Implementation.py

This script implements a command-line interface (CLI) tool using Python's `click` library. The CLI allows users to interact with a JSON file, enabling them to view keys, retrieve values, and update key-value pairs.

## Functionality Overview

1. CLI Initialization (`cli` function)
    - Serves as the main command group.
    - Accepts a JSON file (`document`) as an argument.
    - Reads the JSON file and stores its content in `ctx.obj`, making it accessible to all subcommands.

2. Displaying Keys (`show_keys` command)
    - Lists all top-level keys in the JSON document.

3. Retrieving a Value (`get_value` command)
    - Accepts a key as an argument.
    - Prints the corresponding value if the key exists; otherwise, prints `"Key not found"`.

4. Updating a Value (`update_value` command)
    - Requires `-k/--key` (key to update) and `-v/--value` (new value).
    - Updates the key’s value in memory.
    - Saves the updated JSON data back to the file.

## Example Usage

### 1. Viewing Keys

```sh
python script.py data.json show_keys
```

Example Output (if `data.json` contains `{"name": "Alice", "age": 30}`):

```
Keys: ['name', 'age']
```

### 2. Retrieving a Value

```sh
python script.py data.json get_value name
```

Output:

```
Alice
```

### 3. Updating a Value

```sh
python script.py data.json update_value -k name -v Bob
```

Modifies `data.json` to:

```json
{
    "name": "Bob",
    "age": 30
}
```

