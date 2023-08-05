talqual
=======

|Test| |Coverage| |Pypi| |Python| |Gpl|

.. |Test| image:: https://gitlab.com/timbaler/talqual/badges/master/pipeline.svg
        :target: https://gitlab.com/timbaler/talqual/commits/master
.. |Coverage| image:: https://gitlab.com/timbaler/talqual/badges/master/coverage.svg
        :target: https://gitlab.com/timbaler/talqual/commits/master
.. |Pypi| image:: https://img.shields.io/pypi/v/talqual.svg
    :target: https://pypi.python.org/pypi/talqual
.. |Python| image:: https://img.shields.io/pypi/pyversions/talqual.svg
            :alt: Python version
.. |Gpl| image:: https://img.shields.io/pypi/l/talqual.svg
         :target: https://www.gnu.org/licenses/gpl-3.0.html
         :alt: Gplv3-License


TAL_ Chameleon_ static site generator.

Simple structure: templates + data -> output html


.. _TAL: https://chameleon.readthedocs.io/en/latest/reference.html
.. _Chameleon: https://chameleon.readthedocs.io
.. _TALsyntax: https://chameleon.readthedocs.io/en/latest/reference.html
.. _METALsyntax: https://chameleon.readthedocs.io/en/latest/reference.html#macros-metal
.. _TALi18nsyntax: https://chameleon.readthedocs.io/en/latest/reference.html#id49


Installation
------------

Install from PyPI::

    pip install talqual


Developing
----------

Install requirement and launch tests::

    pip install -r requirements-dev.txt
    pytest tests


Selenium
--------

Launch tests with driver option::

  pytest tests --driver firefox


Maybe you get the error::

 selenium.common.exceptions.WebDriverException: Message: 'geckodriver' executable needs to be in PATH.

Then you need to download the latest `geckodriver` release from https://github.com/mozilla/geckodriver/releases (such as `geckodriver-v0.28.0-linux64.tar.gz`) and extract it to the correspongind directory (such as `/usr/local/bin/`).



Usage
-----

* talqual `templates_dir`
* talqual `templates_dir` `output_html` --data `data_dir`
* python -m talqual `templates_dir` `output_html` --data `data_dir`

or from code::

 from talqual.main import build
 build(templates_dir, html_dir, data_dir)


Features
--------

Template elements: Folder, File, TalTemplate/Html, NoView, TalCommand
Data elements: Python objects, Folder, yaml, json, rst


* Define a `data` directory. Will be converted to dictionary structure:

  * Subfolders
  * Yaml files
  * Json files
  * ReestructuredText files (only variables)

* Define a `templates` directory
* A folder in the `templates` is created to the `html` directory
* A file (pdf, image, css, js, etc.) in the `templates` is copied to the `html` directory
* A no view element (file or directory starting by `_`) in the `templates` is not created to the `html` directory
* A TAL template in the `templates` gets rendered to the `html` directory

  - It can reference data from the `data` directory or from python objects
  - It can be:

    - a static .html or .htm (with no templating)
    - a simple template .html .htm or .pt (with TAL templating, see TALsyntax_)
    - a template with macros .html .htm or .pt (with TAL and METAL templating, see METALsyntax_)

* A TAL Command gets executed and rendered  to the `html` directory

  - a template with NAME.tal_repeat_VARIABLE.pt gets repeated by `data[VARIABLE]` (it must be an iterable such as `[ITEM0, ITEM1, ITEM2, ...]` ). Results in `NAME.0.html`, `NAME.1.html`, `NAME.2.html`, etc.

    - a template with tal_.tal_repeat_VARIABLE.pt results in `ITEM0.html`, `ITEM1.html`, `ITEM2.html`, etc.
    - inside each TAL template the expression `${tal_repeat_VARIABLE}` can be used. Contains the current index `${tal_repeat_VARIABLE.num}` and `ITEM` `${tal_repeat_VARIABLE.item}`.

  - a template with NAME.tal_batch_VARIABLE_PAGESIZE.pt gets rendered by a Batch of PAGESIZE for `data[VARIABLE]` (it must be an iterable). Results in `NAME.html`, `NAME.2.html`, `NAME.3.html`, etc.

  - a template with NAME.tal_replace_talqual_scripts.js gets rendered to a javascript file NAME.js with the faceted module.

  - a template with NAME.tal_replace_DATA:VARIABLE.js gets rendered to the contents of file in `data[DATA][VARIABLE]`.

  - VARIABLE can be generally expressed as `VAR1:VAR2:VAR3` meaning `data[VAR1][VAR2][VAR3]`

* Inside TAL templates, there is the expression `url:` for computing links relatively to the root. For example: `href="${url: static/a.png}"`

* HTML internal links integrity is checked. In case of broken links, a warning is shown when building.


Extra
=====

* A template can include the faceted javascript module. See the `portfolio` example.

* A template can include the calendar javascript module. See the `portfolio` example.


Translation (i18n)
==================

See the `i18n` example.


Install:

* You need to `pip install babel-lingua-chameleon` or `pip install talqual[multilingual]`


Usage:

* talqual `templates_dir` (by default locales at `templates_dir/_locales`)
* talqual `templates_dir` `output_html` --data `data_dir` --locales `locales_dir`


Features:

* Define a folder in the `templates` named `tal_.tal_repeat_LOCALES`
* Define templates .html .htm or .pt with TAL templating that includes i18n, see TALi18nsyntax_.
* Define inside `data` a `LOCALES` variable listing the enabled localizations (l10n). For exemple, a `data.yaml`::

   LOCALES:
   - ca
   - en
   - oc

* Define the `locales_dir`. Recommended with `Babel command-line interface <https://babel.pocoo.org/en/latest/cmdline.html>`_

  * First time:

    * Define the `babel.cfg` to extract from TAL templates::

       [python: **.py]
       [lingua-chameleon: **.html]
       [lingua-chameleon: **.htm]
       [lingua-chameleon: **.pt]

    * `mkdir locales`
    * `pybabel extract -F babel.cfg -o locales/mydomain.pot .`
    * `pybabel init -D mydomain -i locales/mydomain.pot -d locales -l ca`
    * (init all languages)
    * `pybabel compile -D mydomain -d locales`

  * Updates:

    * `pybabel extract -F babel.cfg -o locales/mydomain.pot .`
    * `pybabel update -D mydomain -i locales/mydomain.pot -d locales`
    * `pybabel compile -D mydomain -d locales`



License
-------

``talqual`` is offered under the GPLv3 license.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
