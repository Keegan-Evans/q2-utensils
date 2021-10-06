import qiime2.plugin.model as Model

from .plugin_setup import plugin

from qiime2.plugin import ValidationError

class UtensilsFormat(Model.TextFileFormat):
    def _validate_(self, level):
        header_labels = 'utensil\taction\tmaterials\n'

        with self.open() as fh:
            for i, line in enumerate(fh, 0):
                if i == 0:
                    if line != header_labels:
                        raise ValidationError("No header present or header"
                                " does not contain correct fields:\nexpected:"
                                " %s\nobserved: %s" % (header_labels, line))

UtensilsDirectoryFormat = Model.SingleFileDirectoryFormat(
                          'UtensilsDirectoryFormat', 'utensil.tsv', UtensilsFormat)

plugin.register_formats(UtensilsFormat, UtensilsDirectoryFormat)
