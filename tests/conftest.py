"""Pytest fixture for the local_persist_vulnz agent."""
import os
import pytest

from unittest import mock

from ostorlab.agent import definitions as agent_definitions
from ostorlab.runtimes import definitions as runtime_definitions
from ostorlab.runtimes.local.models import models
from ostorlab.agent import message
from agent import local_persist_vulnz_agent as agent_local_persist_vulnz



@pytest.fixture(name='message')
def create_scan_message():
    """Creates a dummy message of type v3.asset.file to be used by the agent for testing purposes.
    The files used is the EICAR Anti-Virus Test File.
    """
    selector = 'v3.report.vulnerability'
    msg_data = {
            'title': 'my vuln',
            'technical_detail': 'print $1',
            'risk_rating': 'HIGH',
            'short_description': 'Control user input',
            'description': 'XSS',
            'recommendation': 'Check input',
            'references': [{'title': 'My reference', 'url':'https://ostorlab.co'}],
            'security_issue': True,
            'privacy_issue': False,
            'has_public_exploit': False,
            'targeted_by_malware': False,
            'targeted_by_ransomware': False,
            'targeted_by_nation_state': False,
            'dna': 'dna'
        }
    return message.Message.from_data(selector, data=msg_data)


@mock.patch('ostorlab.runtimes.local.models.models.ENGINE_URL', 'sqlite:////tmp/ostorlab_db1.sqlite')
@pytest.fixture(name='persist_vulnz_agent')
def fixture_tracker_agent():
    """Instantiate local_persist_vulnz agent."""
    definition = agent_definitions.AgentDefinition(
        name='agent_local_persist_vulnz',
        out_selectors=[],
        args=[])
    settings = runtime_definitions.AgentSettings(
        key='agent_local_persist_vulnz_key',
        bus_url='NA',
        bus_exchange_topic='NA',
        bus_management_url='http://guest:guest@localhost:15672/',
        bus_vhost='/',
    )
    database = models.Database()
    database.create_db_tables()
    scan = models.Scan.create('test')
    os.environ['UNIVERSE'] = str(scan.id)
    agent = agent_local_persist_vulnz.LocalPersistVulnzAgent(definition, settings)
    return agent
