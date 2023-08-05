#!/usr/bin/python3
# -*- coding: utf-8 -*-

from slpkg.utilities import Utilities


class Requires:
    """ Creates a list of dependencies with
    the right order to install. """

    def __init__(self, data: dict, name: str):
        __slots__ = 'data', 'name'
        self.data: dict = data
        self.name: str = name

        self.utils = Utilities()

    def resolve(self) -> list:
        """ Resolve the dependencies. """
        requires: list[str] = self.data[self.name][7].split()

        for req in requires:

            # Remove requirements that are included as dependencies,
            # but are not included in the repository.
            if req not in list(self.data.keys()) or self.utils.blacklist_pattern(req):
                requires.remove(req)
                continue

            if req:
                sub_requires: list[str] = self.data[req][7].split()
                for sub in sub_requires:
                    requires.append(sub)

        requires.reverse()

        return list(dict.fromkeys(requires))
