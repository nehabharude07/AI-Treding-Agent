from pydantic import BaseModel

class AgentMetadata(BaseModel):
    name: str
    description: str
    wallet_address: str
    capabilities: list