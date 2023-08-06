"""
This plugin searches for Azure Storage Account access keys.
"""
import re

from detect_secrets.plugins.base import RegexBasedDetector


class AzureStorageKeyDetector(RegexBasedDetector):
    """Scans for Azure Storage Account access keys."""
    secret_type = 'Azure Storage Account access key'

    denylist = [
        # Account Key (AccountKey=xxxxxxxxx)
        re.compile(
            r'(?:[A-Za-z0-9+\/]{4}){18,}(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=|[A-Za-z0-9+\/]{4})$',  # noqa: E501
        ),
    ]
