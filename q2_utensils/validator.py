from .type import Pencil, Pen, Spoon, Fork, Chalk, Dining, Writing
from .plugin_setup import plugin
from .format import UtensilsFormat

from qiime2.plugin import ValidationError

@plugin.register_validator(Writing[Pencil | Pen | Chalk])
def validator_check_utensil(data: UtensilsFormat, level):
    pass

# @plugin.register_validator(Dining[Spoon | Fork])
