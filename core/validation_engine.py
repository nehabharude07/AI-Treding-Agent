import hashlib
import json


class ValidationEngine:

    def create_backtest_proof(self, metrics):

        proof_data = json.dumps(metrics, sort_keys=True)
        proof_hash = hashlib.sha256(proof_data.encode()).hexdigest()

        return {
            "metrics": metrics,
            "proof_hash": proof_hash
        }