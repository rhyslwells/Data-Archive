---
aliases: []
category: DEVOPS
date modified: 1-08-2025
tags: [python]
---
Python Click, or "[[Command Line]] Interface Creation Kit," is a library for building command-line interfaces (CLIs). It supports arbitrary nesting of commands, automatic help page generation, and lazy loading of subcommands. 

In [[ML_Tools]] see: [[Click_Implementation.py]]
## Installation

To install Click, use pip:

```sh
pip install click
```

## Creating a Command Group

Click uses groups to organize related commands. A group serves as a container for multiple commands.

```python
import click
import json

@click.group("cli")
@click.pass_context
@click.argument("document")
def cli(ctx, document):
    """An example CLI for interfacing with a document"""
    with open(document) as _stream:
        _dict = json.load(_stream)
    ctx.obj = _dict

def main():
    cli(prog_name="cli")

if __name__ == '__main__':
    main()
```

Running `python script.py --help` generates an automatic help page.

## Adding Commands

Commands can be added to a Click group using the `@<group>.command` decorator.

### Checking Context Object

```python
import pprint

@cli.command("check_context_object")
@click.pass_context
def check_context(ctx):
    pprint.pprint(type(ctx.obj))
```

### Custom Pass Decorator

A pass decorator allows passing specific objects through context.

```python
pass_dict = click.make_pass_decorator(dict)
```

### Retrieving Keys from Context

```python
@cli.command("get_keys")
@pass_dict
def get_keys(_dict):
    keys = list(_dict.keys())
    click.secho("The keys in our dictionary are", fg="green")
    click.echo(click.style(str(keys), fg="blue"))
```

### Retrieving a Specific Key

```python
@cli.command("get_key")
@click.argument("key")
@click.pass_context
def get_key(ctx, key):
    if key in ctx.obj:
        pprint.pprint(ctx.obj[key])
    else:
        click.echo(f"Key '{key}' not found in document.", err=True)
```

### Arbitrary Nesting of Commands

```python
@cli.command("get_summary")
@click.pass_context
def get_summary(ctx):
    ctx.invoke(get_key, key="summary")
```

## Adding Optional Parameters

Optional parameters can be defined using the `@click.option` decorator.

```python
@cli.command("get_results")
@click.option("-d", "--download", is_flag=True, help="Download the result to a JSON file")
@click.option("-k", "--key", help="Specify a key from the results")
@click.pass_context
def get_results(ctx, download, key):
    results = ctx.obj.get('results', [])
    if key:
        results = {key: sum(entry.get(key, 0) for entry in results)}
    if download:
        filename = f"{key or 'results'}.json"
        with open(filename, 'w') as w:
            json.dump(results, w)
        click.echo(f"File saved to {filename}")
    else:
        pprint.pprint(results)
```

## Using `@click.pass_obj`

`@click.pass_obj` passes only `ctx.obj` instead of the full context.

```python
@cli.command("get_text")
@click.option("-s", "--sentences", is_flag=True, help="Return sentences")
@click.option("-p", "--paragraphs", is_flag=True, help="Return paragraphs")
@click.option("-d", "--download", is_flag=True, help="Download as JSON file")
@click.pass_obj
def get_text(_dict, sentences, paragraphs, download):
    results = _dict.get('results', [])
    text = {} if paragraphs else {'text': ''}
    for idx, entry in enumerate(results):
        if paragraphs:
            text[idx] = entry.get('text', '')
        else:
            text['text'] += entry.get('text', '')
    if sentences:
        text = {i: s for i, s in enumerate(text.get('text', '').split('.')) if s}
    pprint.pprint(text)
    if download:
        filename = "paragraphs.json" if paragraphs else "text.json"
        with open(filename, 'w') as w:
            json.dump(text, w)
        click.echo(f"File saved to {filename}")
```

## Handling User Input

Click provides `@click.prompt` to interact with users.

```python
@cli.command("prompt_user")
@click.pass_context
def prompt_user(ctx):
    name = click.prompt("Enter your name")
    age = click.prompt("Enter your age", type=int)
    click.echo(f"Hello {name}, you are {age} years old!")
```

## Handling Confirmation

Use `@click.confirm` to get user confirmation before proceeding.

```python
@cli.command("confirm_action")
@click.pass_context
def confirm_action(ctx):
    if click.confirm("Do you want to proceed?"):
        click.echo("Proceeding with action...")
    else:
        click.echo("Action canceled.")
```

## Conclusion

Python Click simplifies CLI creation with its decorators and built-in features like automatic help generation and context passing. This guide provides a foundation for building more advanced command-line applications. Additionally, handling user input and confirmations enhances the interactivity of CLI applications.