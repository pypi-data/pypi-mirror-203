from copy import deepcopy

from poetry.core.pyproject.toml import PyProjectTOML

PLUGIN_NAME = 'poetry-git-version-plugin'


class PluginConfig(object):
    """Обертка над конфигурацией pyproject"""

    pyproject: PyProjectTOML

    _default_setting = {
        # Игнорирование отсутствия тега
        'ignore_errors': True,
        # Использование ref без тега
        'make_alpha_version': True,
        # Использование ref без тега
        'format_alpha_version': '{version}.a{distance}+{commit_hash}',
    }

    def __init__(self, pyproject: PyProjectTOML) -> None:
        self.pyproject = pyproject

    @property
    def settings(self):
        settings = self.pyproject.data.get('tool', {}).get(PLUGIN_NAME, {})
        new_settings = deepcopy(self._default_setting)
        new_settings.update(settings)
        return new_settings

    @property
    def ignore_errors(self) -> bool:
        return self.settings['ignore_errors']

    @property
    def make_alpha_version(self) -> bool:
        return self.settings['make_alpha_version']

    @property
    def format_alpha_version(self) -> str:
        return self.settings['format_alpha_version']
