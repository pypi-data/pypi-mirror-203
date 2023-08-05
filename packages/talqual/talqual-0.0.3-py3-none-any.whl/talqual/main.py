import logging

from anytree import RenderTree

from .data import Data
from .importer import FileSystemImporter
from .templates import Template
from .translation import Translation


log = logging.getLogger('talqual')


def build(src, dst, data_src, locales=None):
    importer = FileSystemImporter()
    # Read src directory
    log.debug(f'Reading templates from {src}')
    root = importer.import_(src)
    # Read data
    if data_src is None:
        log.debug('There is no data')
        root_data = None
    else:
        log.debug(f'Reading data from {data_src}')
        root_data = importer.import_(data_src)

    # Make data tree
    if root_data is None:
        data = {}
    else:
        data = Data.data_from_tree(root_data)
        log.debug(f'Data Tree\n{RenderTree(data).by_attr("name")}')

    # Make template tree
    templates = Template.template_from_tree(root)
    log.debug(f'Template Tree\n{RenderTree(templates).by_attr("name")}')

    # Set locales directory
    if locales is not None:
        templates.set_locales(Translation(locales))
        log.debug(f'Set locales dir {locales}')

    # Render templates
    view = templates.render(data)
    log.debug(f'View Tree\n{RenderTree(view).by_attr("name")}')

    # Check for broken links
    log.debug('Checking for broken links')
    errors = view.check_broken_links()
    log.debug(f'Total: {errors} broken links')

    # Write views to dst directory
    log.debug(f'Writing to {dst}')
    view.write(dst)
    log.debug(f'Done. Output built at {dst}')
