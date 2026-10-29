import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    RPC_URL = os.getenv("RPC_URL")
    PRIVATE_KEY = os.getenv("PRIVATE_KEY")
    AGENT_ADDRESS = os.getenv("AGENT_ADDRESS")
    CHAIN_ID = int(os.getenv("CHAIN_ID", 8453))  # Example Base L2

settings = Settings()