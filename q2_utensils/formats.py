import qiime2.plugin.model as Model

from .plugin_setup import plugin

class UtensilsFormat(Model.TextFileFormat):
    pass

UtensilsDirectoryFormat = Model.SingleFileDirectoryFormat(
                          'UtensilsDirectoryFormat', 'utensil.tsv', UtensilsFormat)

plugin.register_formats(UtensilsFormat, UtensilsDirectoryFormat)
