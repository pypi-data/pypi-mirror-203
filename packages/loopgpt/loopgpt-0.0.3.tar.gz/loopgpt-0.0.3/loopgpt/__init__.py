__version__ = "0.0.3"


from loopgpt.agent import Agent
from loopgpt.tools import *
from loopgpt.memory import *
from loopgpt.embeddings import *

agent_from_config = Agent.from_config
from loopgpt.tools import from_config as tool_from_config
from loopgpt.memory import from_config as memory_from_config
from loopgpt.embeddings import from_config as embedding_provider_from_config


def from_config(config):
    return globals()[config["type"] + "_from_config"](config)
