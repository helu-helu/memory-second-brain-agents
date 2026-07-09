* [Unity Editor interface](unity-editor.html)
* [Navigating and managing the Unity Editor](editor-navigating-managing.html)
* [Searching in the Unity Editor](editor-searching.html)
* [Unity Search](search-overview.html)
* [Create a custom search provider](create-search-provider.html)
* Registering an Action Handler

Performing a search

Manage search indexing

# Registering an Action Handler

You can register actions for a Search Provider. Users can access registered actions via the **More Options** (**⋮**) icon in the search results.

> **Note:** Registering an action handler and registering a Search Provider are different processes. You can register new action handlers for existing Search Providers.

To register an action, you create a function tagged with the [`SearchActionsProvider`](../ScriptReference/Search.SearchActionsProviderAttribute.html) attribute. This function must return an `IEnumerable<SearchAction>`.

The following example shows how to register actions for the Asset Search Provider.

```
[SearchActionsProvider]
internal static IEnumerable<SearchAction> ActionHandlers()
{
    return new[]
    {
        new SearchAction("asset", "select", Icons.@goto, "Select asset...")
        {
            handler = (item, context) =>
            {
                var asset = AssetDatabase.LoadAssetAtPath<Object>(item.id);
                if (asset != null)
                {
                    Selection.activeObject = asset;
                    EditorGUIUtility.PingObject(asset);
                    EditorWindow.FocusWindowIfItsOpen(
                        Utils.GetProjectBrowserWindowType());
                }
            }
        },
        new SearchAction("asset", "open", SearchIcon.open, "Open asset... (Alt+Enter)")
        {
            handler = (item, context) =>
            {
                var asset = AssetDatabase.LoadAssetAtPath<Object>(item.id);
                if (asset != null)
                    AssetDatabase.OpenAsset(asset);
            }
        },
        new SearchAction("asset", "reveal", SearchIcon.folder, "Show in Explorer")
        {
            handler = (item, context) =>
            {
                EditorUtility.RevealInFinder(item.id);
            }
        }
    };
}
```

## Search actions

The [`SearchAction`](../ScriptReference/SearchAction.html) class describes an action and provides a handler to execute the action on a specific `SearchItem`.

```
public class SearchAction
{
    public SearchAction(string providerType, string name,
                        Texture2D icon = null,
                        string tooltip = null);
    public ActionHandler handler;
    public EnabledHandler isEnabled;
}
```

The `providerType` is the unique ID of the provider that you register the action for.

The `ActionHandler` has the following signature:

```
// item: item that needs the action to be executed.
// context: search context of the SearchTool when the item is executed.
public delegate void ActionHandler(SearchItem item, SearchContext context);
```

You can set up an action with the `isEnabled` predicate, which determines whether an action is available for a specific item.

## Contextual search actions

To provide contextual (right-click) actions for specific types of items in search results, register an action named `context` for the Search Provider.

The following example is from the Asset Search Provider:

```
new SearchAction(type, "context", null, "Context")
{
    handler = (item, context) =>
    {
        var asset = AssetDatabase.LoadAssetAtPath<Object>(item.id);
        if (asset != null)
        {
            Selection.activeObject = asset;
            EditorUtility.DisplayPopupMenu(
                QuickSearchTool.ContextualActionPosition,
                "Assets/", null);
        }
    }
}
```

Performing a search

Manage search indexing

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)