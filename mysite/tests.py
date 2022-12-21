from django.test import TestCase
from django.utils import translation

from django.utils.translation import gettext as _


class I18nTestCase(TestCase):
    def setUp(self):
        translation.activate("it")

    def test_active(self):
        translated = _("Active")
        assert translated == "Operativo", f"Got `{translated}`, was expecting `Operativo`"
