from poetry.packages import Dependency
from poetry.packages import Package

from poetry.semver.helpers import normalize_version


def get_package(name, version):
    return Package(name, normalize_version(version), version)


def get_dependency(name,
                   constraint=None,
                   category='main',
                   optional=False,
                   allows_prereleases=False):
    return Dependency(
        name,
        constraint or '*',
        category=category,
        optional=optional,
        allows_prereleases=allows_prereleases
    )
