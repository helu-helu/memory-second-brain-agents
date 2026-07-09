* [Unity Editor interface](unity-editor.html)
* [Navigating and managing the Unity Editor](editor-navigating-managing.html)
* [Searching in the Unity Editor](editor-searching.html)
* [Unity Search](search-overview.html)
* [Create a custom search provider](create-search-provider.html)
* Registering a Search Provider

The SearchProvider class

Performing a search

# Registering a Search Provider

To add a new Search Provider, refer to the examples in the [SearchProvider](../ScriptReference/Search.SearchProvider.html) class.

These examples create a function and tag it with the [SearchItemProvider](../ScriptReference/Search.SearchItemProviderAttribute.html) attribute:

* The function must return a new `SearchProvider` instance.
* The `SearchProvider` instance must have the following:
  + A unique `type`. For example, **Asset**, **Menu**, or ****Scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
    See in [Glossary](Glossary.html#Scene)**.
  + A `displayName` to use in the [Filters pane](search-filters#persistent-search-filters).
* The optional `filterId` provides a search token for [text-based filtering](search-filters#search-tokens). For example, `p:` is the filter ID for [Asset searches](search-assets.html).

## Registering a Search Provider shortcut

To register a shortcut for a new provider, use:

```
[UsedImplicitly, Shortcut("Help/Quick Search/Assets")]
private static void PopQuickSearch()
{
    // Open Search with only the "Asset" provider enabled.
    SearchService.ShowContextual("asset");
}
```

You can map shortcuts to keys or key combinations using the [shortcuts manager](https://docs.unity3d.com/Manual/ShortcutsManager.html).

The SearchProvider class

Performing a search

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)