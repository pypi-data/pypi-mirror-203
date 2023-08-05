import gettext

from chameleon.i18n import simple_translate


"""
Default data variable for locales is `LOCALES`
Then when tal_repating in a folder for localisations, the variable containing
the current localisation will be `tal_repeat_LOCALES`
"""
LOCALE_KEY = 'tal_repeat_LOCALES'


class Translation():
    """An object grouping the information for localising (l10n)
    internationalisated (i18n) templates
.   Uses `gettext` facilities.

    :param localedir: The `gettext localedir` for :func:`gettext.translation`
    :type localedir: str or :class:`pathlib.Path`
    """

    def __init__(self, localedir=None):
        self.localedir = localedir

    def current_language(self, data):
        """
        Extract from `data` the current language by searching for `LOCALE_KEY`
        or None if there is no translation requirement

        :type data: dict or :class:`data.Data`
        :rtype: str
        """
        if LOCALE_KEY not in data.keys():
            return None
        language = data[LOCALE_KEY].get('item')
        return language

    def translate(self, msgid, domain=None, mapping=None, context=None,
                  default=None, target_language=None):
        """Translation function for :class:`chameleon.PageTemplate`"""

        if self.localedir is None or target_language is None:
            return simple_translate(msgid, domain, mapping, context,
                                    target_language, default)

        if not isinstance(msgid, str):
            # Could be a datetime,...
            return simple_translate(msgid, domain, mapping, context,
                                    target_language, default)

        dom = gettext.translation(domain, self.localedir,
                                  languages=[target_language])
        translation = dom.gettext(msgid)

        if translation == msgid:
            return simple_translate(msgid, domain, mapping, context,
                                    target_language, default)

        return translation
