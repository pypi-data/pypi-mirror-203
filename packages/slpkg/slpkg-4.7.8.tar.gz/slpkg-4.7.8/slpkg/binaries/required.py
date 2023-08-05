#!/usr/bin/python3
# -*- coding: utf-8 -*-

from slpkg.utilities import Utilities
from slpkg.repositories import Repositories


class Required:
    """ Creates a list of dependencies with
    the right order to install. """

    def __init__(self, data: dict, name: str, repo: str):
        __slots__ = 'data', 'name,' 'repo'
        self.data: dict = data
        self.name: str = name
        self.repo: str = repo
        self.repos = Repositories()
        self.utils = Utilities()

        self.special_repos: list = [
            self.repos.salixos_repo_name,
            self.repos.salixos_extra_repo_name,
            self.repos.slackel_repo_name,
            self.repos.slint_repo_name
        ]

    def resolve(self) -> list:
        """ Resolve the dependencies. """
        required: list[str] = self.data[self.name][6].split()

        # Resolve dependencies for some special repos.
        if self.repo in self.special_repos:
            requires: list = []
            for req in required:
                if req in list(self.data.keys()):
                    requires.append(req)
            return requires

        for req in required:

            # Remove requirements that are included as dependencies,
            # but are not included in the repository.
            if req not in list(self.data.keys()) or self.utils.blacklist_pattern(req):
                required.remove(req)
                continue

            if req:
                try:
                    sub_required: list[str] = self.data[req][6].split()
                except KeyError:
                    sub_required: list[str] = []

                for sub in sub_required:
                    required.append(sub)

        # Clean for dependencies not in the repository.
        for dep in required:
            if dep not in list(self.data.keys()):
                required.remove(dep)

        required.reverse()

        return list(dict.fromkeys(required))
