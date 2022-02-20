"""LocalPersistVulnz agent: Agent responsible for persisting vulnerabilities to local DB."""
import logging
import os
from rich import logging as rich_logging

from ostorlab.agent import agent
from ostorlab.agent import message as m
from ostorlab.runtimes.local.models import models

logging.basicConfig(
    format='%(message)s',
    datefmt='[%X]',
    handlers=[rich_logging.RichHandler(rich_tracebacks=True)]
)
logger = logging.getLogger(__name__)
logger.setLevel('DEBUG')


class LocalPersistVulnzAgent(agent.Agent):
    """Agent responsible for persisting vulnz to a local DB."""

    def process(self, message: m.Message) -> None:
        """Process message of type v3.report.vulnerability. Extract the vulnerabilities attributes and persist them to
        local database

        Args:
            message: Message containing the vulnerability data.

        Returns:

        """
        models.Vulnerability.create(scan_id=os.getenv('UNIVERSE'),
                                    title= message.data['title'],
                                    short_description= message.data['short_description'],
                                    description=message.data['description'],
                                    recommendation=message.data['recommendation'],
                                    technical_detail=message.data['technical_detail'],
                                    risk_rating=message.data['risk_rating'],
                                    cvss_v3_vector=message.data['cvss_v3_vector'],
                                    dna=message.data.get('dna'))


if __name__ == '__main__':
    logger.info('starting agent Local Persist Vulnz')
    LocalPersistVulnzAgent.main()
