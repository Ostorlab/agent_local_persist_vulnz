"""Unittests for local_persist_vulnz agent."""
from unittest import mock

from ostorlab.runtimes.local.models import models


@mock.patch('ostorlab.runtimes.local.models.models.ENGINE_URL', 'sqlite:////tmp/ostorlab_db1.sqlite')
def testLocalPersistVulnzAgent_always_VulnPersistedToLocalDB(
        agent_mock,
        persist_vulnz_agent,
        scan_message):

    with models.Database() as session:
        init_count = session.query(models.Vulnerability).count()
        persist_vulnz_agent.process(scan_message)
        vuln = session.query(models.Vulnerability).first()

        assert session.query(models.Vulnerability).count() == init_count + 1
        assert 'My reference: https://ostorlab.co' in vuln.references
        assert 'Domain: dummy.co' in vuln.location
        assert 'URL: https://dummy.co/path1' in vuln.location
