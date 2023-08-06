#!/usr/bin/python3
# coding:utf-8
# Copyright (c) 2023 ZouMingzhe <zoumingzhe@qq.com>

__version__ = "0.4"

from argparse import ArgumentParser, Namespace, _SubParsersAction
from typing import Dict, List, Optional

from .xarg_checker import check_name_opt, check_name_pos, check_nargs


class ArgParser():
    '''
    ArgParser
    '''

    def __init__(self, parser: ArgumentParser):
        assert type(parser) is ArgumentParser
        self.__parser = parser

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

    def parse_args(self,
                   args: Optional[List[str]] = None,
                   namespace=None) -> Namespace:
        '''
        parse_args
        '''
        args = self.__parser.parse_args(args, namespace)
        return args


class ArgSubParser(ArgParser):
    '''
    ArgSubParser
    '''

    def __init__(self, name: str, parser: ArgumentParser):
        assert type(parser) is ArgumentParser
        ArgParser.__init__(self, parser)
        self.__parser = parser
        self.__name: str = name
        self.__xsub: Optional[_SubParsersAction] = None
        self.__subs: Dict[str, ArgSubParser] = {}

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

    def add_parser(self, name: str, **kwargs) -> "ArgSubParser":
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

    def __init__(self, prog: Optional[str] = None, **kwargs):
        kwargs.update({"prog": prog})
        self.__parser = ArgumentParser(**kwargs)
        name = "default" if prog is None else prog
        ArgSubParser.__init__(self, name, self.__parser)
