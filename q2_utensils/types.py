from qiime2.plugin import SemanticType
from plugin_setup import plugin 

Pencil = SemanticType('Pencil')
Pen = SemanticType('Pen')
Fork = SemanticType('Fork')
Spoon = SemanticType('Spoon')
Chalk = SemanticType('Chalk')

Dining = SemanticType('Dining', field_names=['utensil'],
                      field_members={ 'utensil': (Fork, Spoon) })

Writing = SemanticType('Writing', field_names=['implement'],
                       field_members={ 'implement': (Pen, Pencil, Chalk) })

plugin.register_semantic_types(Pencil, Pen, Fork, Spoon, Chalk, Dining, Writing)
