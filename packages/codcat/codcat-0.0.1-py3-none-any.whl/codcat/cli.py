"""This module provides CLI interface."""

from pathlib import Path

import click
import pandas as pd
from nltk import (
    NLTKWordTokenizer,
    TweetTokenizer,
)

NAME2TOK = {"nltk": NLTKWordTokenizer(), "tweet": TweetTokenizer()}


def validate_input_dataframe(ctx, param, value):
    try:
        df = pd.read_csv(value)
    except pd.errors.ParserError:
        raise click.BadParameter("Input dataset must be in `csv` format.")

    if "code" not in df.columns or "language" not in df.columns:
        raise click.BadParameter(
            "Input dataframe must have `code` and `language` columns."
        )

    return df


def validate_tokenizer(ctx, param, value):
    value = value.lower()
    if value not in NAME2TOK:
        raise click.BadParameter(
            f"`{value}` is not one of {', '.join(NAME2TOK.keys())}."
        )
    return NAME2TOK[value]


@click.group()
def cli():
    pass


@click.command()
@click.argument(
    "dataset",
    type=click.Path(exists=True, path_type=Path),
    callback=validate_input_dataframe,
)
@click.option(
    "--output",
    "-o",
    type=click.Path(path_type=Path),
    help="Output to preprocessed data",
    default=Path.cwd().joinpath("preprocessed"),
)
@click.option(
    "--tokenizer",
    "-t",
    "tokenizer",
    callback=validate_tokenizer,
    help="Tokenizer name",
    default="nltk",
)
def preprocess(dataset, output, tokenizer):
    dataset["code"] = dataset["code"].apply(
        lambda x: " ".join(tokenizer.tokenize(x))
    )
    dataset.to_csv(output, index=None)


cli.add_command(preprocess)


if __name__ == "__main__":
    cli()
