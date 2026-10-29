class IdentityRegistry:

    def register_agent(self, metadata_uri):
        return {
            "status": "registered",
            "metadata_uri": metadata_uri
        }