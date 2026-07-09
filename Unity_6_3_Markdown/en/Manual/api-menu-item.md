* [Unity Editor interface](unity-editor.html)
* [Navigating and managing the Unity Editor](editor-navigating-managing.html)
* [Searching in the Unity Editor](editor-searching.html)
* [Unity Search](search-overview.html)
* [Manage search queries](search-queries.html)
* Invoke from the main menu

Save and reuse search queries

Create a custom search provider

# Invoke from the main menu

To create a custom menu item that invokes a search, use the `MenuItem` attribute. The following example creates a menu item that searches the **Asset Store**A growing library of free and commercial assets created by Unity and members of the community. Offers a wide variety of assets, from textures, models and animations to whole project examples, tutorials and Editor extensions. [More info](AssetStore.html)  
See in [Glossary](Glossary.html#AssetStore) for free assets:

```
[MenuItem("Search/Free Asset Gifts")]
static void SearchStore()
{
    var storeContext = SearchService.CreateContext("store", "price=0");
    var viewState = new SearchViewState(storeContext,
        UnityEngine.Search.SearchViewFlags.DisableNoResultTips |
        UnityEngine.Search.SearchViewFlags.GridView);
    viewState.windowTitle = new GUIContent("Free Stuff for Christmas");
    viewState.queryBuilderEnabled = true;
    SearchService.ShowWindow(viewState);
}
```

Save and reuse search queries

Create a custom search provider

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)