###
# Author : Emmanuel Essien
# Author Email : emmanuelessiens@outlook.com
# Maintainer By: Emmanuel Essien
# Maintainer Email: emmanuelessiens@outlook.com
# Created by Emmanuel Essien on 1/19/20.
###

import argparse
import locale
import os
import re
import sys
import time
import warnings
import traceback
from openpyweb import Version
from openpyweb.cmd import lang
from openpyweb.Core.requirement import requirement
from typing import Any, Callable, Dict, List, Pattern, Union
from random import randint
from typing import Any, Callable, Dict, List, Pattern, Union
from openpyweb.cmd.console import (  # type: ignore
    colorize, bold, red, green, turquoise, nocolor, color_terminal
)
from random import randint

try:
    import readline

    if readline.__doc__ and 'libedit' in readline.__doc__:
        readline.parse_and_bind("bind ^I rl_complete")
        USE_LIBEDIT = True
    else:
        readline.parse_and_bind("tab: complete")
        USE_LIBEDIT = False
except ImportError:
    USE_LIBEDIT = False



class ValidationError(Exception):
    """Raised for validation errors."""


def is_path(x: str) -> str:
    x = os.path.expanduser(x)
    if not os.path.isdir(x):
        raise ValidationError(__("Please enter a valid path name."))
    return x


def boolean(x: str) -> bool:
    if x.upper() not in ('Y', 'YES', 'N', 'NO'):
        raise ValidationError(__("Please enter either 'y' or 'n'."))
    return x.upper() in ('Y', 'YES')


def allow_empty(x: str) -> str:
    return x


def nonempty(x: str) -> str:
    if not x:
        raise ValidationError(__("Please enter some text."))
    return x


def __(mes_id):

    try:
        userlang = locale.getlocale()[0]

        l_ = mes_id
        for l in lang.lang:
            if l == str(userlang):
                getla = lang.lang.get(l, '')

                if getla != "":
                    l_ =  getla.get(mes_id, '')
                    if l_ != "":
                        l_ = getla.get(mes_id, '')
                    else:
                        l_ = mes_id
                else:
                    l_ = mes_id
    except Exception as arr:
        l_ = mes_id
    return l_

def doTraceBack():
    exc_type, exc_value, exc_traceback = sys.exc_info()
    traceback.print_tb(exc_traceback, limit=1, file=sys.stdout)
    traceback.print_exception(exc_type, exc_value, exc_traceback,
                              limit=2, file=sys.stdout)
    traceback.print_exc()



if sys.platform == 'win32':
    # On Windows, show questions as bold because of color scheme of PowerShell (refs: #5294).
    COLOR_QUESTION = 'bold'
else:
    COLOR_QUESTION = 'purple'

PROMPT_PREFIX = '> '


def do_prompt(text: str, default: str = None, validator: Callable[[str], Any] = nonempty) -> Union[str, bool]:  # NOQA

    while True:
        if default is not None:
            prompt = PROMPT_PREFIX + '%s [%s]: ' % (text, default)
        else:
            prompt = PROMPT_PREFIX + text + ': '
        if USE_LIBEDIT:
            # Note: libedit has a problem for combination of ``input()`` and escape
            # sequence (see #5335).  To avoid the problem, all prompts are not colored
            # on libedit.
            pass
        else:
            prompt = colorize(COLOR_QUESTION, prompt, input_mode=True)
        x = term_input(prompt).strip()
        if default and not x:
            x = default
        try:
            x = validator(x)
        except ValidationError as err:
            print(red('* ' + str(err)))
            continue
        break
    return x


def ask(d: Dict) -> None:

    print(bold(__('Welcome to the openpyweb MVC Framework %s.' % Version.VERSION_TEXT)))

    print(__(bold(red('PLEASE NOTE :'))+' This feature is use for installation of project requirments.'))

    d['step'] = do_prompt(__('Do you want install requirements  (y/n)'),'n', boolean)
    if d.get('step', '') == True:
        try:
            requirement().rf()
        except Exception as err:
            print(err)

    if d.get('step', '') is False:
        sys.exit(-1)




def term_input(prompt: str) -> str:
    if sys.platform == 'win32':

        print(prompt, end='')
        return input('')
    else:
        return input(prompt)


def get_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        usage='%(prog)s [OPTIONS] <PROJECT_DIR>',
        epilog=__("For more information, visit < https://openpyweb.readthedocs.io >."),
        description=__("""openpyweb is a python framework built to enhance web development
        fast and easy, also help web developers to build more apps with less codes.
        it uses expressive architectural pattern, structured on model view controller MVC
        and bundles of component to reuse while deploying the framework."""))

    parser.add_argument('-q', '--quit', action='store_true', dest='quit',
                        default=None,
                        help=__('quit mode'))
    parser.add_argument('--version', action='version', dest='show_version',
                        version='%%(prog)s %s' % Version.VERSION_TEXT)

    parser.add_argument('path', metavar='PROJECT_DIR', default='.', nargs='?',
                        help=__('project root'))

    return parser



def main(argv: List[str] = sys.argv[1:]) -> int:
    # parse options
    parser = get_parser()
    try:
        args = parser.parse_args(argv)

    except SystemExit as err:
        return err.code
    d = vars(args)
    ask(d)
    #path = str(os.getcwd())



if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))