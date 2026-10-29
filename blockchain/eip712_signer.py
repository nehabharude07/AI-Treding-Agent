from eth_account import Account
from eth_account.messages import encode_structured_data

class EIP712Signer:
    def __init__(self, private_key):
        self.account = Account.from_key(private_key)

    def sign_trade_intent(self, trade_data):
        message = encode_structured_data(trade_data)
        signed = self.account.sign_message(message)
        return signed.signature.hex()