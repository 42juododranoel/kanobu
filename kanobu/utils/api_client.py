from rest_framework.test import APIClient


class UserAPIClient(APIClient):
    """DRF testing client with user attribute."""

    def force_authenticate(self, user=None, token=None):
        self.user = user
        return super().force_authenticate(user=user, token=token)
