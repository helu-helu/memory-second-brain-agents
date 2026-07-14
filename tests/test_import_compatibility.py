import importlib


def test_agent_core_public_exports():
    from agent_core import ContextBuilder, KnowledgeBase, MemoryManager

    assert MemoryManager.__name__ == "MemoryManager"
    assert KnowledgeBase.__name__ == "KnowledgeBase"
    assert ContextBuilder.__name__ == "ContextBuilder"


def test_legacy_and_new_runtime_imports_match():
    legacy_knowledge = importlib.import_module("agent_core.knowledge")
    new_knowledge = importlib.import_module("agent_core.rag.knowledge")
    legacy_context = importlib.import_module("agent_core.context_builder")
    new_context = importlib.import_module("agent_core.context.builder")
    legacy_access = importlib.import_module("agent_core.access_tools")
    new_access = importlib.import_module("agent_core.access.second_brain")

    assert legacy_knowledge is new_knowledge
    assert legacy_context is new_context
    assert legacy_access is new_access


def test_memory_public_import_path_survives_package_move():
    from agent_core.memory import MemoryManager
    from agent_core.memory.manager import MemoryManager as ManagerImpl

    assert MemoryManager is ManagerImpl


def test_stable_mcp_entrypoint_imports():
    module = importlib.import_module("second_brain_mcp")

    assert hasattr(module, "build_docs_context_pack")
    assert hasattr(module, "build_unified_context")
