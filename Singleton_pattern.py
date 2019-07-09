#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 单例模式


class SingletonPattern(object):
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            obj = super(SingletonPattern, cls).__new__(cls)
            cls.instance = obj
        return cls.instance

    def __init__(self, name, age):
        self.name = name
        self.age = age


sp1 = SingletonPattern('小明', 18)
sp2 = SingletonPattern('小红', 19)

print('id:', id(sp1), 'name:', sp1.name, 'age:', sp1.age)
print('id:', id(sp2), 'name:', sp2.name, 'age:', sp2.age)
