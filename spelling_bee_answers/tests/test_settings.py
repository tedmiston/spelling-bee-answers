"""
Unit tests - settings.
"""

import logging

from ..settings import Settings


def test_settings_schema():
    settings = Settings()

    assert isinstance(settings.repo_root, str)

    assert isinstance(settings.log_level, str)
    log_levels = list(logging.getLevelNamesMapping().keys())
    assert settings.log_level in log_levels

    assert isinstance(settings.display_puzzle_output, bool)

    assert isinstance(settings.display_generated_readme_output, bool)

    assert isinstance(settings.display_generated_readme_table, bool)


def test_settings_defaults():
    settings = Settings()

    assert settings.repo_root != ""

    assert settings.log_level == "INFO"

    assert settings.display_puzzle_output is True

    assert settings.display_generated_readme_output is False

    assert settings.display_generated_readme_table is True


# todo: test_settings_env_var_overrides
