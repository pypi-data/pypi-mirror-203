#!/usr/bin/env python
# -*- coding:utf-8 -*-
from threading import RLock
from typing import Any

from ..generic import T


class _DecoratorsCache(object):
    __CACHE = {}
    __LOCK = RLock()
    __INSTANCE = None

    def __new__(cls, *args, **kwargs):
        with cls.__LOCK:
            if not cls.__INSTANCE:
                cls.__INSTANCE = object.__new__(cls)
        return cls.__INSTANCE

    @staticmethod
    def get(key: Any, default: T = None) -> T:
        """
        get origin data

        """
        with _DecoratorsCache.__LOCK:
            return _DecoratorsCache.__CACHE.get(key, default)

    @staticmethod
    def put(key: Any, data: T):
        """
        add cache
        """
        with _DecoratorsCache.__LOCK:
            _DecoratorsCache.__CACHE[key] = data

    @staticmethod
    def has_cache(key: Any) -> bool:
        """
        check has cache
        """
        with _DecoratorsCache.__LOCK:
            return key in _DecoratorsCache.__CACHE
