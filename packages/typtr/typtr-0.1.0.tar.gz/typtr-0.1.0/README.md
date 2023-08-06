# TypTr

A transpiler for an idiomatic subset of typed Python into semantically similar
object-oriented languages.

## Details

Currently, TypTr can
[transpile](https://en.wikipedia.org/wiki/Source-to-source_compiler) carefully
type-annotated Python into:

* Java
* Javascript

"Carefully" means a small (and somewhat redundantly cast) subset of
type-annotated Python. _This is not a generic transpiler_. Python has too many
features for that, and for this reason there exist various transpilers for
various idiomatic selections of those. TypTr is but one such selection.

## Installation

To keep up with ongoing development, clone this repo and run `pip install -e .`
within it.

## Usage

    $ typtr -h

## Dependencies

[Mypy](https://pypi.org/project/mypy/) is recommended while working on a
transpilable code base.

## Supported Features

TypTr was originally a part of [TRLD](https://github.com/niklasl/trld). The
needs of that project pretty much dictates what features and idioms are
supported by TypTr at this point.
