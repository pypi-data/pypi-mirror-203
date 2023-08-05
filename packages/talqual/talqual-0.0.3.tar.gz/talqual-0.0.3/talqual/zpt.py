from functools import partial

import chameleon


class BaseTemplate(chameleon.PageTemplate):

    expression_types = chameleon.PageTemplate.expression_types.copy()
    expression_types['load'] = partial(chameleon.tales.ProxyExpr, '__loader')
    expression_types['url'] = partial(chameleon.tales.ProxyExpr, 'url')

    def loader_search(self, path, context=None):
        """Loader implementation for zpt loading macros

        :param str path: The path to a macro from inside a template
        :param context: The template where loading
        :type context: :class:`.zpt.PageTemplate`
        :rtype: :class:`PageTemplate`
        """
        raise NotImplementedError()


class PageTemplate(BaseTemplate):
    """`PageTemplate` with loader from `Templates`

    Expression types:

    * `load:` the :meth:`loader_search` must be defined by
       PageTemplate.loader_search=`meth`
    * `url:` the :meth:`url` must be defined by extra_builtins={'url': `meth`})

    :param dict extra_builtins: Extra builtins :class:`chameleon.PageTemplate`
    """

    def _builtins(self):
        d = super()._builtins()
        d['__loader'] = partial(self.loader_search, context=self)
        return d
