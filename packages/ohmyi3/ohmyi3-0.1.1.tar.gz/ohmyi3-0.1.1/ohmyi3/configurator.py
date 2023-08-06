from uvicore.typing import Dict

class Configurator(Dict):
    """Ohmyi3 Base Configurator"""

    def byhost(self, attribute, values = None):
        """Override attribute values for specific hosts"""
        if type(attribute) == dict:
            # Override any number of values using a large Dictionary
            # Example:
            # self.byhost({
            #     'p15': {
            #         'terminal': 'xfce4-terminal',
            #         'calculator': 'gcalc'
            #     }
            # })
            for host, attributes in attribute.items():
                if self.hostname == host:
                    for attr, value in attributes.items():
                        self.dotset(attr, value)
        else:
            # Override a single value for a number of hosts
            # Example:
            # self.byhost('theme', {
            #     'sunjaro': 'manjaro',
            #     'p53': 'amber',
            # })
            for host, value in values.items():
                if self.hostname == host:
                    #setattr(self, attribute, value)
                    self.dotset(attribute, value)

