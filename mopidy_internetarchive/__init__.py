from __future__ import unicode_literals

import os

from mopidy import config, ext


__version__ = '0.1.0'


class Extension(ext.Extension):

    dist_name = 'Mopidy-InternetArchive'
    ext_name = 'internetarchive'
    version = __version__

    def get_default_config(self):
        conf_file = os.path.join(os.path.dirname(__file__), 'ext.conf')
        return config.read(conf_file)

    def get_config_schema(self):
        schema = super(Extension, self).get_config_schema()
        schema['base_url'] = config.String()
        schema['collections'] = config.List()
        schema['mediatypes'] = config.List()
        schema['formats'] = config.List()
        schema['sort_order'] = config.List()
        schema['search_limit'] = config.Integer(minimum=1, optional=True)
        schema['browse_limit'] = config.Integer(minimum=1, optional=True)
        schema['preload'] = config.Boolean()
        schema['cache_size'] = config.Integer(minimum=1)
        schema['cache_ttl'] = config.Integer(minimum=1)
        return schema

    def setup(self, registry):
        from .backend import InternetArchiveBackend
        registry.add('backend', InternetArchiveBackend)
