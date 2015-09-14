__author__ = 'avishai'

from abc import abstractmethod, ABCMeta

# This is the prototype of a plugin
class Plugin(object):
    __metaclass__ = ABCMeta

    def __init__(self, conf):
        self._conf = {}
        self._conf.update(conf.get(self.__class__.__name__, {}))
        self._conf['common'] = conf
        """:type: dict"""

    # override this property if you want to enable a plugin dynamically
    def enabled(self):
        return True

    @property
    def name(self):
        return type(self).__name__.lower()

    @abstractmethod
    def run(self):
        """Run a plugin and return relevant data. Plugins should return a dict"""
        pass