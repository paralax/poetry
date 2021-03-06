from poetry.packages import dependency_from_pep_508


def test_dependency_from_pep_508():
    name = 'requests'
    dep = dependency_from_pep_508(name)

    assert dep.name == name
    assert str(dep.constraint) == '*'


def test_dependency_from_pep_508_with_version():
    name = 'requests==2.18.0'
    dep = dependency_from_pep_508(name)

    assert dep.name == 'requests'
    assert str(dep.constraint) == '== 2.18.0.0'


def test_dependency_from_pep_508_with_parens():
    name = 'requests (==2.18.0)'
    dep = dependency_from_pep_508(name)

    assert dep.name == 'requests'
    assert str(dep.constraint) == '== 2.18.0.0'


def test_dependency_from_pep_508_with_constraint():
    name = 'requests>=2.12.0,!=2.17.*,<3.0'
    dep = dependency_from_pep_508(name)

    assert dep.name == 'requests'
    assert str(dep.constraint) == '>= 2.12.0.0, != 2.17.*, < 3.0.0.0'


def test_dependency_from_pep_508_with_extras():
    name = 'requests==2.18.0; extra == "foo" or extra == "bar"'
    dep = dependency_from_pep_508(name)

    assert dep.name == 'requests'
    assert str(dep.constraint) == '== 2.18.0.0'
    assert dep.extras == ['foo', 'bar']


def test_dependency_from_pep_508_with_python_version():
    name = (
        'requests (==2.18.0); '
        'python_version == "2.7" or python_version == "2.6"'
    )
    dep = dependency_from_pep_508(name)

    assert dep.name == 'requests'
    assert str(dep.constraint) == '== 2.18.0.0'
    assert dep.extras == []
    assert dep.python_versions == '~2.7 || ~2.6'


def test_dependency_from_pep_508_with_single_python_version():
    name = (
        'requests (==2.18.0); '
        'python_version == "2.7"'
    )
    dep = dependency_from_pep_508(name)

    assert dep.name == 'requests'
    assert str(dep.constraint) == '== 2.18.0.0'
    assert dep.extras == []
    assert dep.python_versions == '~2.7'


def test_dependency_from_pep_508_with_platform():
    name = (
        'requests (==2.18.0); '
        'sys_platform == "win32" or sys_platform == "darwin"'
    )
    dep = dependency_from_pep_508(name)

    assert dep.name == 'requests'
    assert str(dep.constraint) == '== 2.18.0.0'
    assert dep.extras == []
    assert dep.python_versions == '*'
    assert dep.platform == 'win32 || darwin'


def test_dependency_from_pep_508_complex():
    name = (
        'requests (==2.18.0); '
        'python_version >= "2.7" and python_version != "3.2" '
        'and (sys_platform == "win32" or sys_platform == "darwin") '
        'and extra == "foo"'
    )
    dep = dependency_from_pep_508(name)

    assert dep.name == 'requests'
    assert str(dep.constraint) == '== 2.18.0.0'
    assert dep.extras == ['foo']
    assert dep.python_versions == '>=2.7 !=3.2.*'
    assert dep.platform == 'win32 || darwin'
