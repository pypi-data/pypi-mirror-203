
# pylint: disable = missing-function-docstring

'''
Test cases for the versioning module.
'''

import pytest

from chlog.versioning import Versioning


def test_current_version():
    '''
    Verify that version numbers can be extracted from the most
    common forms of change log version numbers.
    '''
    ver = Versioning([]).current_version
    assert ver == '0.0.0'
    for test in ['  (1.2.3) - 2022-02-22',
                 '(1.2.3) - 2022-02-22',
                 '[1.2.3] - 2022-02-22',
                 '1.2.3 - 2022-02-22',
                 '1.2.3 (2022-02-22)',
                 '1.2.3 [2022-02-22]',
                 '1.2.3 anything',
                 'Anything 1.2.3',
                 'Version  1.2.3',
                 'V 1.2.3',
                 'V1.2.3']:
        ver = Versioning(test).current_version
        assert '1.2.3' == ver
    for test in ['1.2.3', '10.2.3', '1.20.3', '1.2.30', '10.20.30',
                 '10.20.30-pre1', '0.1.0', '0.9.5-b.1']:
        ver = Versioning(test).current_version
        assert test == ver


def test_next_versions():
    ver = Versioning(None).next_version()
    assert '0.1.0' == ver
    ver = Versioning('0.9.1').next_version()
    assert '0.10.0' == ver
    ver = Versioning('0.9.1').next_version('major')
    assert '1.0.0' == ver
    ver = Versioning('0.9.1', breaks=True).next_version()
    assert '0.10.0' == ver
    ver = Versioning('1.5.7', breaks=True).next_version()
    assert '2.0.0' == ver
    ver = Versioning('0.9.1', fixes=True).next_version()
    assert '0.9.2' == ver
    ver = Versioning('0.5.1', features=True).next_version()
    assert '0.6.0' == ver
    ver = Versioning('0.5.1', features=True, fixes=True).next_version()
    assert '0.6.0' == ver
    ver = Versioning('0.9.1').next_version('prerelease')
    assert '0.9.2-rc.1' == ver
    ver = Versioning('0.9.2-pre.1').next_version('prerelease')
    assert '0.9.2-pre.2' == ver
    with pytest.raises(ValueError) as err:
        Versioning('1.0.0').next_version('bogus')
        assert 'must be one of' in err


def test_check_version():
    versioning = Versioning('1.2.3')
    with pytest.raises(ValueError) as err:
        versioning.check_version('1-2-3')
        assert 'is not valid' in err
    for ver in ['1.2.2', '1.1.3', '0.2.3']:
        with pytest.raises(ValueError):
            versioning.check_version(ver)
    assert versioning.check_version('1.2.4') is None
    assert versioning.check_version('1.3.3') is None
    assert versioning.check_version('2.0.0') is None
    versioning = Versioning('1.2.3', breaks=True)
    warning = versioning.check_version('1.3.0')
    assert warning.find('breaking changes') >= 0
    assert warning.find('2.0.0') >= 0
