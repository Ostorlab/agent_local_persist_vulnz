"""Unittests for local_persist_vulnz agent."""
from unittest import mock

from ostorlab.runtimes.local.models import models


@mock.patch('ostorlab.runtimes.local.models.models.ENGINE_URL', 'sqlite:////tmp/ostorlab_db1.sqlite')
def testLocalPersistVulnzAgent_always_VulnPersistedToLocalDB(
        agent_mock,
        persist_vulnz_agent,
        message):
    init_count = models.Database().session.query(models.Vulnerability).count()
    persist_vulnz_agent.process(message)
    assert models.Database().session.query(models.Vulnerability).count() == init_count + 1
