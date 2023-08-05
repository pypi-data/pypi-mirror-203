try:  # pragma: py-gte-38
    from importlib import metadata
except ImportError:  # pragma: py-lt-38
    # Running on pre-3.8 Python; use importlib-metadata package
    import importlib_metadata as metadata

__version__ = metadata.version('talqual')
