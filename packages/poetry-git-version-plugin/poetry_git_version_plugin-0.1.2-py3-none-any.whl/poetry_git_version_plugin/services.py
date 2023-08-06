import re
from pathlib import Path
from typing import Callable, List

import git
from cleo.io.io import IO
from cleo.io.outputs.output import Verbosity
from packaging.version import VERSION_PATTERN

from poetry_git_version_plugin import config
from poetry_git_version_plugin.exceptions import PluginException

VERSION_REGEX_COMPILE = re.compile(r'^\s*' + VERSION_PATTERN + r'\s*$', re.VERBOSE | re.IGNORECASE)


def validate_version(version_string: str):
    """Проверка версии на PEP 440

    Копипаст метода: from poetry.core.version.pep440.parser import parse_pep440

    Args:
        version_string (str): Версия

    Raises:
        PluginException: Версия не соответствует стандарту

    """

    if VERSION_REGEX_COMPILE.search(version_string) is None:
        raise PluginException(f'Invalid PEP 440 version: "{version_string}"')


def validate_version_decorator(func: Callable):
    def inner(*args, **kwargs):
        version = func(*args, **kwargs)
        validate_version(version)
        return version

    return inner


class GitService(object):
    repo: git.Repo

    def __init__(self) -> None:
        path = Path.cwd()
        self.repo = git.Repo(path, search_parent_directories=True)

    @property
    def commits(self) -> List[git.Commit]:
        return list(self.repo.iter_commits())

    @property
    def current_commit(self) -> git.Commit:
        return self.repo.head.commit

    @property
    def tags(self) -> List[git.Tag]:
        return list(self.repo.tags)[::-1]

    def get_git_current_tag(self) -> git.Tag:
        """Получение тега нынешнего коммита"""

        tags = list(self.repo.tags)[::-1]

        for tag in tags:
            if tag.commit == self.repo.head.commit:
                return tag

        return None

    def get_alpha_version(self) -> git.Tag:
        """Получение последнего тега нынешней ветки"""

        commits = set(self.commits)
        tags = self.tags

        for tag in tags:
            if tag.commit in commits:
                return tag

        return None

    def get_current_short_rev(self) -> str:
        return self.current_commit.name_rev[:7]

    def get_distance(self, from_commit: git.Commit, to_commit: git.Commit) -> int:
        return len(list(self.repo.iter_commits(f'{from_commit}..{to_commit}')))


class GitVersionService(object):
    io: IO
    plugin_config: config.PluginConfig

    git_service: GitService

    def __init__(self, io: IO, plugin_config: config.PluginConfig) -> None:
        self.io = io
        self.plugin_config = plugin_config

        self.git_service = GitService()

    def construct_alpha_version(self, version: str, distance: str, commit_hash: str):
        return self.plugin_config.format_alpha_version.format(
            version=version,
            distance=distance,
            commit_hash=commit_hash,
        )

    def get_main_version(self) -> str:
        tag = self.git_service.get_git_current_tag()
        return tag.name if tag is not None else None

    def get_alpha_version(self):
        tag = self.git_service.get_alpha_version()

        version = '0.0.0'
        distance_from_commit = self.git_service.commits[-1]

        if tag is not None:
            distance_from_commit = tag.commit
            version = str(tag)

        distance = self.git_service.get_distance(distance_from_commit, self.git_service.current_commit)
        commit_hash = self.git_service.get_current_short_rev()

        return self.construct_alpha_version(version, distance, commit_hash)

    @validate_version_decorator
    def get_version(self) -> str:
        self.io.write(f'<b>{config.PLUGIN_NAME}</b>: Find git <b>current tag</b>... ', verbosity=Verbosity.VERBOSE)

        version = self.get_main_version()

        if version is not None:
            self.io.write_line(f'success, setting dynamic version to: {version}', Verbosity.VERBOSE)
            return version

        self.io.write_line('fail', Verbosity.VERBOSE)

        if not self.plugin_config.make_alpha_version:
            raise PluginException('No Git version found, not extracting dynamic version')

        self.io.write(f'<b>{config.PLUGIN_NAME}</b>: Make <b>alpha version</b>... ', verbosity=Verbosity.VERBOSE)

        tag = self.get_alpha_version()

        self.io.write_line(f'success, setting dynamic version to: {tag}', Verbosity.VERBOSE)

        return tag
