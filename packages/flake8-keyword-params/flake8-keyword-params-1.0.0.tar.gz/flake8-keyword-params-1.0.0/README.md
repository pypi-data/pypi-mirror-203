# [flake8-keyword-params](https://github.com/plinss/flake8-keyword-params)

flake8 plugin to require that optional parameters are keyword-only.

## Installation

Standard python package installation:

    pip install flake8-keyword-params


## Options

`keyword-params-include-name`
: Include plugin name in messages

`keyword-params-no-include-name`
: Do not include plugin name in messages (default setting)

All options may be specified on the command line with a `--` prefix,
or can be placed in your flake8 config file.



## Error Codes

| Code   | Message |
|--------|---------|
| KWP001 | Optional parameter 'param' should be keyword only


## Examples

```
def foo(x = None):  <-- KWP001
```