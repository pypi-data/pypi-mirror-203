import logging
from pathlib import Path

import click

from . import __version__, main


_dir_existing = click.Path(exists=True, dir_okay=True, file_okay=False)
_dir_optional = click.Path(exists=False)
_fileordir_existing = click.Path(exists=True, dir_okay=True, file_okay=True)
verbose_help = 'Enable verbose output.'


@click.group()
@click.version_option(__version__, '-V', '--version', prog_name='talqual')
@click.option('-v', '--verbose', is_flag=True, help=verbose_help)
def cli(verbose):
    if verbose:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)


@cli.command()
@click.argument('src', type=_dir_existing, required=True)
@click.argument('dst', type=_dir_optional, required=False)
@click.option('--data', type=_fileordir_existing, required=False,
              help='defaults to src/_data or src/_data.yaml',
              metavar='data_src')
@click.option('--locales', type=_dir_existing, required=False,
              help='defaults to src/_locales',
              metavar='locales_src')
def build(src, dst, data, locales):
    """Builds SRC to DST

    SRC is a directory of templates

    DST defaults to SRC/_build
    """
    src = Path(src)
    if dst is None:
        dst = src / '_build'
    else:
        dst = Path(dst)
    if data is None:
        data = src / '_data'
        if not data.exists():
            data = src / '_data.yaml'
            if not data.exists():
                data = None
    else:
        data = Path(data)

    if locales is None:
        locales = src / '_locales'
        if not locales.exists():
            locales = None

    main.build(src, dst, data, locales)
