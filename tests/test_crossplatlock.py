import pytest
from msal_extensions._cache_lock import CrossPlatLock


def test_ensure_file_deleted():
    lockfile = './foo.txt'

    with pytest.raises(FileNotFoundError):
        with CrossPlatLock(lockfile):
            pass
        with open(lockfile):
            pass
