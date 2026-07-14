"""Compatibility shim for the context runtime package."""

import sys

from agent_core.context import builder as _impl

sys.modules[__name__] = _impl
setattr(sys.modules[__package__], "context_builder", _impl)
