"""
Operation recipes for managing the projects and execution environment.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.

This file is present within multiple projects, simplifying dependency.
"""



from os import environ
from pathlib import Path
from re import MULTILINE
from re import findall as re_findall
from re import sub as re_sub
from sys import stdout
from typing import Literal
from typing import Optional

from yaml import SafeLoader
from yaml import load



CONTAINER = Path(__file__).parent

PROJECT_YAML = load(
    (CONTAINER
     .joinpath('collection/galaxy.yml')
     .read_text()),
    SafeLoader)

PROJECT = (
    (PROJECT_YAML['name']
     .strip()))

PROJECT = f'ansible-{PROJECT}'

VERSION = (
    PROJECT_YAML['version']
    .strip())

COLOR = environ.get('COLOR', 7)

PREFIX = Literal[
    'text', 'base', 'more']



def makeout(
    string: str,
    prefix: Optional[PREFIX] = None,
) -> None:
    """
    Print the ANSI colorized string to the standard output.

    .. note::
       This function is forgiving due to use with Makefile.

    :param string: String processed using inline directives.
    :param prefix: Determine if and which prefix prepended.
    """

    pattern = r'\<c([\d\;]+)\>'
    replace = r'\033[0;\1m'


    if prefix is not None:

        string = string.lstrip(' ')

        padding = 3
        _prefix = ''

        if prefix == 'base':
            padding = 0
            _prefix = '<cL>>>><c0>'

        elif prefix == 'more':
            padding = 2
            _prefix = '<cL>●<c0>'

        space: str = ' '

        string = (
            f'{space * padding}'
            f'{_prefix} {string}')


    string = (
        f'{string}\n'
        .replace('<cD>', f'<c3{COLOR}>')
        .replace('<cL>', f'<c9{COLOR}>'))

    stdout.write(
        re_sub(pattern, replace, string))



def makeread(
    path: str,
) -> str:
    """
    Return the contents using the provided filesystem path.

    :param path: Complete or relative path to the makefile.
    :returns: Contents using the provided filesystem path.
    """

    return (
        Path(path)
        .read_text(encoding='utf-8'))



def makefile(
    path: str = 'Makefile',
) -> None:
    """
    Print the Makefile summary in the human friendly format.

    :param path: Complete or relative path to the makefile.
    """

    contents = makeread(path)

    pattern = (
        r'\n([a-z]\S+)\:(\s+\\\n)?'
        r'((\s+[^\n]+){1,2})?\n'
        r'\s+\@##\s([^\n]+)?\n')

    matches = re_findall(
        pattern, contents, MULTILINE)

    if len(matches) == 0:
        return

    for match in matches:
        makeout(
            f'  <c9{COLOR}>{match[0]}'
            f'  <c0>{match[4]}')



if __name__ == '__main__':

    makeout(
        f' <c97>{PROJECT}/<c0>'
        f'<c37>{VERSION}<c0>'
        f' <c90>Makefile<c0>\n')

    makefile()
