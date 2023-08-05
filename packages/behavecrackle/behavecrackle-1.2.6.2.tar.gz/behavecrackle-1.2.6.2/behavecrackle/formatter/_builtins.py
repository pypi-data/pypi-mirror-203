# -*- coding: utf-8 -*-
"""
Knowledge base of all built-in formatters.
"""

from __future__ import  absolute_import
from behavecrackle.formatter import _registry


# -----------------------------------------------------------------------------
# DATA:
# -----------------------------------------------------------------------------
# SCHEMA: formatter.name, formatter.class(_name)
_BUILTIN_FORMATS = [
    # pylint: disable=bad-whitespace
    ("plain",   "behavecrackle.formatter.plain:PlainFormatter"),
    ("pretty",  "behavecrackle.formatter.pretty:PrettyFormatter"),
    ("json",    "behavecrackle.formatter.json:JSONFormatter"),
    ("json.pretty", "behavecrackle.formatter.json:PrettyJSONFormatter"),
    ("null",      "behavecrackle.formatter.null:NullFormatter"),
    ("progress",  "behavecrackle.formatter.progress:ScenarioProgressFormatter"),
    ("progress2", "behavecrackle.formatter.progress:StepProgressFormatter"),
    ("progress3", "behavecrackle.formatter.progress:ScenarioStepProgressFormatter"),
    ("rerun",     "behavecrackle.formatter.rerun:RerunFormatter"),
    ("tags",          "behavecrackle.formatter.tags:TagsFormatter"),
    ("tags.location", "behavecrackle.formatter.tags:TagsLocationFormatter"),
    ("steps",         "behavecrackle.formatter.steps:StepsFormatter"),
    ("steps.doc",     "behavecrackle.formatter.steps:StepsDocFormatter"),
    ("steps.catalog", "behavecrackle.formatter.steps:StepsCatalogFormatter"),
    ("steps.usage",   "behavecrackle.formatter.steps:StepsUsageFormatter"),
    ("sphinx.steps",  "behavecrackle.formatter.sphinx_steps:SphinxStepsFormatter"),
]

# -----------------------------------------------------------------------------
# FUNCTIONS:
# -----------------------------------------------------------------------------
def setup_formatters():
    """Register all built-in formatters (lazy-loaded)."""
    _registry.register_formats(_BUILTIN_FORMATS)
