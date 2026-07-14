"""Compatibility shim for second-brain access helpers."""

import sys

from agent_core.access import second_brain as _impl

sys.modules[__name__] = _impl
setattr(sys.modules[__package__], "access_tools", _impl)
