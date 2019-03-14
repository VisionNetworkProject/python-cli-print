#!/usr/bin/env python
# encoding: utf-8

import sys
from colorama import (Fore, Back, Style)

wr = sys.stdout.write

STYLE_STEPS = Fore.LIGHTBLUE_EX
STYLE_PLAIN_TEXT = Fore.BLUE
STYLE_SUCCESS = Fore.GREEN
STYLE_ERROR = Back.RED + Fore.LIGHTWHITE_EX
STYLE_VALUE = Fore.LIGHTCYAN_EX
STYLE_JOB = Back.BLUE + Fore.LIGHTWHITE_EX
STYLE_ABOUT_TO = Fore.LIGHTYELLOW_EX
STYLE_GETTING = Fore.LIGHTYELLOW_EX
STYLE_WATCHING = Fore.LIGHTYELLOW_EX

PREVIOUS_LINE = '\x1b[1A'
ERASE_LINE = '\x1b[2K'


def spaces(n: int = 1):
    """
    Print several spaces.

    :param int n: Number of spaces.
    :return: None
    """
    wr(' ' * n)
    sys.stdout.flush()
    return


def space():
    """
    Print one space.

    :return: None
    """
    spaces(1)
    return


def lx(n: int = 2):
    """
    Print several blank lines.

    :param int n: Number of lines
    :return: None
    """
    for i in range(0, n):
        print()
    return


def ex(n: int = 2):
    """
    Print several blank lines, and exit()

    :param int n: Number of lines
    :return: None
    """
    lx(n=n)
    exit()
    return


def fi(inline: bool = True):
    """
    Reset stdout style.

    :param bool inline: Whether print as inline, or end with a `\n`.
    :return: None
    """
    if inline:
        wr(Style.RESET_ALL)
    else:
        print(Style.RESET_ALL)
    sys.stdout.flush()
    return


def fx(n: int = 1):
    """
    Reset stdout style, and end this line, if n > 1, print blank lines extra.

    :return: None
    """
    print(Style.RESET_ALL)
    sys.stdout.flush()
    if n > 1:
        lx(n - 1)
    return


def previous_line(clear: bool = False):
    """
    Back to previous line.

    :param bool clear: Whether clear the line.
    :return: None
    """
    wr(PREVIOUS_LINE)
    if clear:
        wr(ERASE_LINE)
    fi()
    return


def steps(n: int = 1, with_spaces: int = 0):
    """
    Print several step chars, allow spaces as suffix.

    :param int n: Number of steps
    :param int with_spaces: Number of suffix spaces
    :return: None
    """
    wr(STYLE_STEPS + '>' * n)
    if with_spaces:
        spaces(with_spaces)
    fi()
    return


def step(with_spaces: int = 0):
    """
    Print one step char, allow spaces as suffix.

    :param int with_spaces: Number of suffix spaces
    :return: None
    """
    steps(1, with_spaces=with_spaces)
    return


def plain_text(text: str):
    """
    Print plain text.
    :param str text: Plain text.
    :return: None
    """
    wr(STYLE_PLAIN_TEXT + text)
    fx()
    return


def success(text='success.', inline: bool = False):
    """
    Print success text.

    :param text: Success text
    :param bool inline: Whether print as inline, or end with a `\n`.
    :return: None
    """
    wr(STYLE_SUCCESS + '{}'.format(text))
    fi(inline=inline)
    return


def error(text, inline: bool = False):
    """
    Print error text.

    :param text: Error text
    :param bool inline: Whether print as inline, or end with a `\n`.
    :return: None
    """
    wr(STYLE_ERROR + ' {} '.format(text))
    fi(inline=inline)
    return


def value(val, inline: bool = False):
    """
    Print a value.

    :param str val: Value
    :param bool inline: Whether print as inline, or end with a `\n`.
    :return: None
    """
    wr(STYLE_VALUE + str(val))
    fi(inline=inline)
    return


def job(text: str):
    """
    Print a job.

    :param str text: Job name
    :return: None
    """
    print()
    wr(STYLE_JOB + ' - {} - '.format(text))
    fx(2)
    return


def about_to(text: str, val: str = None, suffix: str = None, inline: bool = False):
    """
    Print a tip for "about to do sth. ..."

    :param str text: Task name
    :param str val: Value
    :param str suffix: Suffix
    :param bool inline: Whether print as inline, or end with a `\n`.
    :return: None
    """
    step(with_spaces=1)
    wr(STYLE_ABOUT_TO + text)

    if val:
        wr(STYLE_VALUE + ' {}'.format(val))

    if suffix:
        wr(STYLE_ABOUT_TO + ' {}'.format(suffix))

    if inline:
        wr(Fore.LIGHTBLUE_EX + ' ... ')

    fi(inline=inline)
    return


def about_t(text: str, val=None, suffix=None):
    """
    Print a hint for "about to do sth. ...", inline mode.

    :param str text: Task name
    :param str val: Value
    :param str suffix: Suffix
    :return: None
    """
    about_to(text=text, val=val, suffix=suffix, inline=True)
    return


def getting(text: str, inline: bool = True):
    """
    Print a hint for "getting sth. > |"

    :param str text: Name
    :param bool inline: Whether print as inline, or end with a `\n`. Default: True
    :return: None
    """
    step(with_spaces=1)
    wr(STYLE_GETTING + text)
    space()
    step(with_spaces=1)
    fi(inline=inline)
    return


def watching(text: str, inline: bool = True):
    """
    Print a hint for "watching sth. >>>"

    :param str text: Name
    :param bool inline: Whether print as inline, or end with a `\n`. Default: True
    :return: None
    """
    step(with_spaces=1)
    wr(STYLE_WATCHING + str(text))
    space()
    step()
    fi(inline=inline)
    return
