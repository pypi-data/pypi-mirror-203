#!/Users/christmas/opt/anaconda3/bin/python3
# -*- coding: utf-8 -*-
#  日期 : 2023/4/12 16:45
#  作者 : Christmas
#  邮箱 : 273519355@qq.com
#  项目 : Cprintf
#  版本 : python 3
#  摘要 :
"""

"""
import os

__all__ = ['Blogging', 'DEBUG', 'SUCCESS', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']

BLACK = '\033[30m'  # 黑色
RED = '\033[31m'  # 红色
GREEN = '\033[32m'  # 绿色
YELLOW = '\033[33m'  # 黄色
BLUE = '\033[34m'  # 蓝色
PURPLE = '\033[35m'  # 紫色
CYAN = '\033[36m'  # 蓝绿色
WHITE = '\033[37m'  # 白色

BOLD = '\033[1m'  # 加粗
UNDERLINE = '\033[4m'  # 下划线
BLINK = '\033[5m'  # 闪烁
REVERSE = '\033[7m'  # 反显
HIDE = '\033[8m'  # 隐藏
R_ec = '\033[0m'  # 重置颜色

debug = 10
success = 20
info = 30
warning = 40
error = 50
critical = 60

default_level = warning


class Blogging:
    def __init__(self, _LEVEL=warning, _log_file=None, _log_de_print=True, _status_format=BOLD):
        self.name = 'Christmas'
        self.level = _LEVEL
        self.log_file = _log_file
        self.log_de_print = _log_de_print
        self.status_format = _status_format

    def DEBUG(self, _str, _voice=False, _color=WHITE):  # 紫色
        if self.level <= 10:
            DEBUG(_str, _voice, _color, LEVEL=self.level, _file=self.log_file, log_de_print=self.log_de_print, _status_format=self.status_format)

    def SUCCESS(self, _str, _voice=False, _color=GREEN):  # 绿色
        if self.level <= 20:
            SUCCESS(_str, _voice, _color, LEVEL=self.level, _file=self.log_file, log_de_print=self.log_de_print, _status_format=self.status_format)

    def INFO(self, _str, _voice=False, _color=BLUE):  # 蓝色
        if self.level <= 30:
            INFO(_str, _voice, _color, LEVEL=self.level, _file=self.log_file, log_de_print=self.log_de_print, _status_format=self.status_format)

    def WARNING(self, _str, _voice=False, _color=YELLOW):  # 黄色
        if self.level <= 40:
            WARNING(_str, _voice, _color, LEVEL=self.level, _file=self.log_file, log_de_print=self.log_de_print, _status_format=self.status_format)

    def ERROR(self, _str, _voice=True, _color=RED):  # 红色
        if self.level <= 50:
            ERROR(_str, _voice, _color, LEVEL=self.level, _file=self.log_file, log_de_print=self.log_de_print, _status_format=self.status_format)

    def CRITICAL(self, _str, _voice=True, _color=PURPLE):  # 白色
        if self.level <= 60:
            CRITICAL(_str, _voice, _color, LEVEL=self.level, _file=self.log_file, log_de_print=self.log_de_print, _status_format=self.status_format)


def DEBUG(_str, _voice=False, _color=WHITE, LEVEL=default_level, _file=None, log_de_print=True, _status_format=BOLD):  # 紫色
    if LEVEL <= 10:
        echo_log('DEBUG', _str, _voice, _color, _file=_file, log_de_print=log_de_print, _status_format=BOLD)


def SUCCESS(_str, _voice=False, _color=GREEN, LEVEL=default_level, _file=None, log_de_print=True, _status_format=BOLD):  #
    if LEVEL <= 20:
        echo_log('SUCCESS', _str, _voice, _color, _file=_file, log_de_print=log_de_print, _status_format=BOLD)


def INFO(_str, _voice=False, _color=BLUE, LEVEL=default_level, _file=None, log_de_print=True, _status_format=BOLD):  # 蓝色
    if LEVEL <= 30:
        echo_log('INFO', _str, _voice, _color, _file=_file, log_de_print=log_de_print, _status_format=BOLD)


def WARNING(_str, _voice=False, _color=YELLOW, LEVEL=default_level, _file=None, log_de_print=True, _status_format=BOLD):  # 黄色
    if LEVEL <= 40:
        echo_log('WARNING', _str, _voice, _color, _file=_file, log_de_print=log_de_print, _status_format=BOLD)


def ERROR(_str, _voice=True, _color=RED, LEVEL=default_level, _file=None, log_de_print=True, _status_format=BOLD):  # 红色
    if LEVEL <= 50:
        echo_log('ERROR', _str, _voice, _color, _file=_file, log_de_print=log_de_print, _status_format=BOLD)


def CRITICAL(_str, _voice=True, _color=PURPLE, LEVEL=default_level, _file=None, log_de_print=True, _status_format=BOLD):  # 白色
    if LEVEL <= 60:
        echo_log('CRITICAL', _str, _voice, _color, _file=_file, log_de_print=log_de_print, _status_format=BOLD)


def echo_log(_status, _str, _voice, _color, _e=False, _file=None, log_de_print=True, _status_format=BOLD):
    if _file is None:
        if _e:
            if _voice:
                os.system(f'echo -e `date "+%Y-%m-%d %T"` "---> {_color}{_status_format}[{_status}]{R_ec} {_color}{_str}{R_ec}\a"')
            else:
                os.system(f'echo -e `date "+%Y-%m-%d %T"` "---> {_color}{_status_format}[{_status}]{R_ec} {_color}{_str}{R_ec}"')
        elif _voice:
            os.system(f'echo `date "+%Y-%m-%d %T"` "---> {_color}{_status_format}[{_status}]{R_ec} {_color}{_str}{R_ec}\a"')
        else:
            os.system(f'echo `date "+%Y-%m-%d %T"` "---> {_color}{_status_format}[{_status}]{R_ec} {_color}{_str}{R_ec}"')
    elif log_de_print:
        if _e:
            if _voice:
                os.system(f'echo -e `date "+%Y-%m-%d %T"` "---> {_color}{_status_format}[{_status}]{R_ec} {_color}{_str}{R_ec}\a"')
            else:
                os.system(f'echo -e `date "+%Y-%m-%d %T"` "---> {_color}{_status_format}[{_status}]{R_ec} {_color}{_str}{R_ec}"')
        elif _voice:
            os.system(f'echo `date "+%Y-%m-%d %T"` "---> {_color}{_status_format}[{_status}]{R_ec} {_color}{_str}{R_ec}\a"')
        else:
            os.system(f'echo `date "+%Y-%m-%d %T"` "---> {_color}{_status_format}[{_status}]{R_ec} {_color}{_str}{R_ec}"')
    else:
        os.system(f'echo `date "+%Y-%m-%d %T"` "---> [{_status}] {_str}" >> {_file}')


if __name__ == '__main__':
    myblog = Blogging()
    print(myblog)
