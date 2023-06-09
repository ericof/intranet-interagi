"""Portal settings tests."""
from plone import api

import pytest


class TestPortalSettings:
    """Test that Portal configuration is correctly done."""

    @pytest.mark.parametrize(
            "setting,expected",
            [
                ["plone.default_language", "pt-br"],
                ["plone.email_charset", "utf-8"],
                ["plone.email_from_address", "intranet@interagi.com.br"],
                ["plone.email_from_name", "Intranet Interagi"],
                ["plone.enable_sitemap", True],
                ["plone.portal_timezone", "America/Sao_Paulo"],
                ["plone.site_title", "Intranet Interagi"],
                ["plone.smtp_host", "localhost"],
                ["plone.smtp_port", 25],
                ["plone.twitter_username", "plone"],
            ]
    )
    def test_portal_settings(self, portal, setting, expected):
        """Test portal settings."""
        value = api.portal.get_registry_record(setting)
        assert value == expected, f"Valor incorreto para {setting}"
