import unittest

from qiime2 import plugin
from q2_utensils.plugin_setup import plugin as qutensils

class TestPlugin(unittest.TestCase):
    def test_plugin_exists(self):
        self.assertEqual(qutensils.name, 'utensils')
