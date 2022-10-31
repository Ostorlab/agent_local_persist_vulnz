"""Pytest fixture for the local_persist_vulnz agent."""
import os
import sys

import pytest

from ostorlab.agent import definitions as agent_definitions
from ostorlab.runtimes import definitions as runtime_definitions
from ostorlab.runtimes.local.models import models
from ostorlab.agent.message import message
from agent import local_persist_vulnz_agent as agent_local_persist_vulnz


@pytest.fixture(name='db_engine_path')
def db_engine_tmp_path(tmpdir):
    if sys.platform == 'win32':
        path = f'sqlite:///{tmpdir}\\ostorlab_db1.sqlite'.replace('\\', '\\\\')
    else:
        path = f'sqlite:////{tmpdir}/ostorlab_db1.sqlite'
    return path


@pytest.fixture
def scan_message():
    """Creates a dummy message of type v3.report.vulnerability to be used by the agent for testing purposes.
    The files used is the EICAR Anti-Virus Test File.
    """
    selector = 'v3.report.vulnerability'
    msg_data = {
            'title': 'my vuln',
            'technical_detail': 'print $1',
            'risk_rating': 'HIGH',
            'cvss_v3_vector': 'AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H/E:H/RL:O/RC:C',
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
            'dna': 'dna',
            'vulnerability_location': {
                'domain_name': {'name': 'dummy.co'},
                'metadata': [{'type': 'URL', 'value': 'https://dummy.co/path1'}]
            }
        }
    return message.Message.from_data(selector, data=msg_data)


@pytest.fixture
def persist_vulnz_agent(mocker, db_engine_path):
    """Instantiate local_persist_vulnz agent."""
    mocker.patch.object(models, 'ENGINE_URL', db_engine_path)
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
    scan = models.Scan.create('test')
    os.environ['UNIVERSE'] = str(scan.id)
    agent = agent_local_persist_vulnz.LocalPersistVulnzAgent(definition, settings)
    return agent
