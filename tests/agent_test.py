"""Unittests for local_persist_vulnz agent."""
from ostorlab.runtimes.local.models import models


def testVirusTotalAgent_when_virusTotalApiReturnsValidResponse_noRaiseVirusTotalApiError(
        agent_mock,
        persist_vulnz_agent,
        message):
    init_count = models.Database().session.query(models.Vulnerability).count()
    persist_vulnz_agent.process(message)
    assert models.Database().session.query(models.Vulnerability).count() == init_count + 1