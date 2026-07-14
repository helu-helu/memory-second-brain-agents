"""Compatibility shim for the RAG runtime package."""

import sys

from agent_core.rag import knowledge as _impl

sys.modules[__name__] = _impl
setattr(sys.modules[__package__], "knowledge", _impl)
