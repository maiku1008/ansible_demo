import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_user(host):
    f = host.user('pippo')

    assert f.exists


def test_group(host):
    f = host.group('pippo')

    assert f.exists


def test_file(host):
    f = host.file('/tmp/pippo')

    assert f.exists
