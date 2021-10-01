from qiime2.plugin.testing import TestPluginBase
import q2_utensils

from q2_utensils.formats import UtensilsFormat, UtensilsDirectoryFormat

class TestUtensilFormats(TestPluginBase):
    package = 'q2_utensils.testing'

    def test_format_registration(self):
        self.assertTrue()
