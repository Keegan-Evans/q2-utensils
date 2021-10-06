import os.path
from qiime2.plugin.testing import TestPluginBase
import q2_utensils

from q2_utensils.format import UtensilsFormat, UtensilsDirectoryFormat

class TestUtensilFormats(TestPluginBase):
    package = 'q2_utensils.testing'

    def test_format_registration(self):
        self.assertTrue(self)

    def test_format_validate(self):
        file_name = 'mixed_type_validator.tsv'

        file_path = self.get_data_path(file_name)

        format = UtensilsFormat(file_path, mode='r')

        format.validate()

    def test_format_validate_negative(self):
        pass
