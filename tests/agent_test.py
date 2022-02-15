"""Unittests for local_persist_vulnz agent."""
from ostorlab.runtimes.local.models import models


def testLocalPersistVulnzAgent_always_VulnPersistedToLocalDB(
        mocker,
        agent_mock,
        persist_vulnz_agent,
        message):
    init_count = models.Database().session.query(models.Vulnerability).count()
    persist_vulnz_agent.process(message)
    assert models.Database().session.query(models.Vulnerability).count() == init_count + 1
