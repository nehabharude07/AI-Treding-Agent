class ValidationRegistry:

    def submit_validation(self, artifact_hash):
        return {
            "validation_hash": artifact_hash,
            "status": "submitted"
        }