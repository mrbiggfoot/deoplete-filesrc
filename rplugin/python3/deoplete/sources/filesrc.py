# ============================================================================
# FILE: filesrc.py
# AUTHOR: Andrew Pyatkov <andrew.pyatkov at gmail.com>
# License: MIT license
# ============================================================================

from .base import Base
from os.path import exists, getmtime


class Source(Base):

    def __init__(self, vim):
        super().__init__(vim)

        self.name = 'filesrc'
        self.mark = '[f]'

        self.__cache = []
        self.__mtime = 0

    def on_init(self, context):
        self.__filepath = context['vars'].get(
            'deoplete#filesrc#path', '')

    def on_event(self, context):
        self.__cache = []
        if not exists(self.__filepath):
            return

        mtime = getmtime(self.__filepath)
        if mtime == self.__mtime:
            return

        self.__mtime = mtime
        f = open(self.__filepath, 'r')
        self.__cache = list(f.read().split())

    def gather_candidates(self, context):
        return self.__cache
