from web3 import Web3

class RiskRouter:
    def __init__(self, provider_url, contract_address, abi):
        self.w3 = Web3(Web3.HTTPProvider(provider_url))
        self.contract = self.w3.eth.contract(
            address=contract_address,
            abi=abi
        )

    def execute_trade(self, signed_intent):
        tx = self.contract.functions.executeTrade(
            signed_intent
        ).build_transaction({
            "from": self.w3.eth.default_account,
            "nonce": self.w3.eth.get_transaction_count(self.w3.eth.default_account)
        })
        return tx