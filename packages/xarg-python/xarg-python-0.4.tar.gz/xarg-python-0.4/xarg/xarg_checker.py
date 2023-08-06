#!/usr/bin/python3
# coding:utf-8
# Copyright (c) 2023 ZouMingzhe <zoumingzhe@qq.com>

prefix_chars = '-'


def check_name_opt(fn):
    '''
    check optional argument name
    '''

    def inner(self, *name, **kwargs):
        # 1. check short form optional argument ('-x')
        # 2. check long form optional argument ('--xx')
        # 3. only short form or long form or short form + long form
        # 模棱两可的数据（-1可以是一个负数的位置参数）
        for n in name:
            assert type(n) is str and n[0] in prefix_chars,\
                f"{n} is not an optional argument name"
        return fn(self, *name, **kwargs)

    return inner


def check_name_pos(fn):
    '''
    check positional argument name
    '''

    def inner(self, name: str, **kwargs):
        assert type(name) is str and name[0] not in prefix_chars,\
            "{name} is not a positional argument name"
        return fn(self, name, **kwargs)

    return inner


def check_nargs(fn):
    '''
    nargs hook function:
        nargs < -1: using '?', 0 or 1 argument, default value
        nargs = -1: using '+', arguments list, at least 1
        nargs = 0: using '*', arguments list, allow to be empty
        nargs = 1: redirect to '?', 0 or 1 argument
        nargs > 1: N arguments list
    '''

    def inner(self, *args, **kwargs):
        _nargs = kwargs.get("nargs", -2)
        if type(_nargs) is int and _nargs < 2:
            _nargs = {1: '?', 0: '*', -1: '+'}.get(_nargs, '?')
        kwargs.update({"nargs": _nargs})
        return fn(self, *args, **kwargs)

    return inner
