# -*- coding: utf-8 -*-
"""
Deprecated module. Functionality was split-up into:

  * behavecrackle.formatter._registry  (generic core functionality)
  * behavecrackle.formatter._builtins  (registration of known, builtin formatters)

.. since:: 1.2.5a1
    Deprecated, use "behavecrackle.formatter._registry" or "behavecrackle.formatter._builtin".
"""

from __future__ import absolute_import
import warnings
from behavecrackle.formatter import _registry

warnings.simplefilter("once", DeprecationWarning)
warnings.warn("Use 'behavecrackle.formatter._registry' instead.", DeprecationWarning)

# -----------------------------------------------------------------------------
# FORMATTER REGISTRY:
# -----------------------------------------------------------------------------
def register_as(formatter_class, name):
    """
    Register formatter class with given name.

    :param formatter_class:  Formatter class to register.
    :param name:  Name for this formatter (as identifier).
    """
    warnings.warn("Use behavecrackle.formatter._registry.register_as() instead.",
                  DeprecationWarning, stacklevel=2)
    _registry.register_as(name, formatter_class)


def register(formatter_class):
    register_as(formatter_class, formatter_class.name)


def get_formatter(config, stream_openers):
    warnings.warn("Use make_formatters() instead",
                  DeprecationWarning, stacklevel=2)
    return _registry.make_formatters(config, stream_openers)


# -----------------------------------------------------------------------------
# SETUP:
# -----------------------------------------------------------------------------
def setup_formatters():
    warnings.warn("Use behavecrackle.formatter._builtins instead",
                  DeprecationWarning, stacklevel=2)
    from behavecrackle.formatter import _builtins
    _builtins.setup_formatters()


# -----------------------------------------------------------------------------
# MODULE-INIT:
# -----------------------------------------------------------------------------
# DISABLED: setup_formatters()
