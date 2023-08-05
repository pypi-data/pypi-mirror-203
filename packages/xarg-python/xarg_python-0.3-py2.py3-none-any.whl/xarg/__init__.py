#!/usr/bin/python3
# coding:utf-8
# Copyright (c) 2023 ZouMingzhe <zoumingzhe@qq.com>

__version__ = "0.3"

from argparse import ArgumentParser, Namespace, _SubParsersAction

prefix_chars = '-'


class ArgParser():
    '''
    ArgParser
    '''

    def __init__(self, parser: ArgumentParser):
        assert type(parser) is ArgumentParser
        self.__parser = parser

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

    @check_name_opt
    @check_nargs
    def add_opt(self, *name, **kwargs) -> None:
        '''
        add optional argument
        '''
        self.__parser.add_argument(*name, **kwargs)

    @check_name_opt
    def add_opt_on(self, *name, **kwargs) -> None:
        '''
        add boolean optional argument, default value is False
        '''
        kwargs.update({"action": 'store_true'})
        for key in ("type", "nargs", "const", "default", "choices"):
            assert key not in kwargs, f"'{key}' is an invalid argument"
        self.__parser.add_argument(*name, **kwargs)

    @check_name_opt
    def add_opt_off(self, *name, **kwargs) -> None:
        '''
        add boolean optional argument, default value is True
        '''
        kwargs.update({"action": 'store_false'})
        for key in ("type", "nargs", "const", "default", "choices"):
            assert key not in kwargs, f"'{key}' is an invalid argument"
        self.__parser.add_argument(*name, **kwargs)

    @check_name_pos
    @check_nargs
    def add_pos(self, name: str, **kwargs) -> None:
        '''
        add positional argument
        '''
        assert 'dest' not in kwargs,\
            "dest supplied twice for positional argument"
        self.__parser.add_argument(name, **kwargs)

    @check_nargs
    def add_argument(self, *args, **kwargs) -> None:
        '''
        add_argument
        '''
        self.__parser.add_argument(*args, **kwargs)

    def parse_args(self, *args, **kwargs) -> Namespace:
        '''
        parse_args
        '''
        args = self.__parser.parse_args(*args, **kwargs)
        return args


class ArgSubParser(ArgParser):
    '''
    ArgSubParser
    '''

    def __init__(self, name: str, parser: ArgumentParser):
        assert type(parser) is ArgumentParser
        ArgParser.__init__(self, parser)
        self.__parser = parser
        self.__name = name
        self.__xsub = None
        self.__subs = {}

    def add_subparsers(self, *args, **kwargs) -> "ArgSubParser":
        '''
        enable subparsers
        '''
        # subparser: cannot have multiple subparser arguments
        assert self.__xsub is None, "cannot have multiple subparser"
        kwargs.setdefault("dest", f"subcmd_{self.__name}")
        kwargs.setdefault("help", "sub-command list")
        self.__xsub = self.__parser.add_subparsers(*args, **kwargs)
        return self

    def add_parser(self, name: str, **kwargs) -> ArgParser:
        '''
        add sub parser
        '''
        assert type(self.__xsub) is _SubParsersAction
        if name in self.__subs:
            _sub = self.__subs[name]
            assert type(_sub) is ArgSubParser
            return _sub
        _sub_parser = self.__xsub.add_parser(name, **kwargs)
        return self.__subs.setdefault(name, ArgSubParser(name, _sub_parser))


class xarg(ArgSubParser):
    '''
    xarg
    '''

    def __init__(self, prog: str = None, **kwargs):
        kwargs.update({"prog": prog})
        self.__parser = ArgumentParser(**kwargs)
        name = "default" if prog is None else prog
        ArgSubParser.__init__(self, name, self.__parser)
