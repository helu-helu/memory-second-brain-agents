* [Unity Editor interface](unity-editor.html)
* [Navigating and managing the Unity Editor](editor-navigating-managing.html)
* [Searching in the Unity Editor](editor-searching.html)
* [Unity Search](search-overview.html)
* [Create a custom search provider](create-search-provider.html)
* Performing a search

Registering a Search Provider

Registering an Action Handler

# Performing a search

Search Providers use the [`fetchItems`](../ScriptReference/Search.SearchProvider.html) function to search for items and filter the results. The [`fetchItems`](../ScriptReference/Search.SearchProvider.html) function has the following signature:

```
// context: the necessary search context (for example, tokenized search and
// sub-filters).
// items: list of items to populate (if not using the asynchronous api)
// provider: the Search Provider itself
public delegate IEnumerable<SearchItem> GetItemsHandler(SearchContext context,
                                    List<SearchItem> items,
                                    SearchProvider provider);
```

The [`SearchProvider`](../ScriptReference/Search.SearchProvider.html) must add new [`SearchItem`](../ScriptReference/Search.SearchItem.html)s to the `items` list or return an `IEnumerable<SearchItem>`.

> **Note:** If you do not use the asynchronous `fetchItems` API, you must return `null` in your `fetchItems` function.

A `SearchItem` is a simple struct:

```
public struct SearchItem
{
    public readonly string id;
    // The item score affects how Search sorts the item within the results from the Search Provider.
    public int score;
    // Optional: Display name of the item. If the item does not have one,
    // SearchProvider.fetchLabel is called).
    public string label;
    // If the item does not have a description SearchProvider.fetchDescription
    // is called when Search first displays the item.
    public string description;
    // If true, the description already has rich text formatting.
    public SearchItemDescriptionFormat descriptionFormat;
    // If the item does not have a thumbnail, SearchProvider.fetchThumbnail
    // is called when Search first displays the item.
    public Texture2D thumbnail;
    // Search Provider user-customizable content
    public object data;
}
```

A `SearchItem` only requires the `id`.

> **Tip:** When you filter according to [`SearchContext.searchText`](../ScriptReference/Search.SearchContext-searchText.html) use the static function [`SearchProvider.MatchSearchGroup`](../ScriptReference/Search.SearchProvider.html) which makes a partial search.

## Using fuzzy search

To use fuzzy search on an item, you can use [`FuzzySearch.FuzzyMatch`](../ScriptReference/Search.FuzzySearch.html), as in the following example:

```
if (FuzzySearch.FuzzyMatch(sq, CleanString(item.label), ref score, matches))
    item.label = RichTextFormatter.FormatSuggestionTitle(item.label, matches);
```

All search items are sorted against items of the same provider with their `score`. The **lower score** appears at the top of the item list (**ascending sorting**).

## Asynchronous search API

You can use the asynchronous `fetchItems` API when a Search Provider takes a long time to compute its results, or relies on an asynchronous search engine such as WebRequests.

To use the asynchronous API, have the `fetchItems` function return an `IEnumerable<SearchItem>`. The `IEnumerable<SearchItem>` should be a function that yields results, so that the API can fetch one item at a time.

When an `IEnumerable<SearchItem>` is returned, the enumerator is stored and iterated over during an application update. Enumeration continues over multiple application updates until it is finished.

The iterating time is constrained to ensure the UI is not blocked. However, because the call is in the main thread, you should make sure to yield as soon as possible if the results are not ready.

The following example demonstrates how to use the asynchronous `fetchItems` API:

```
public class AsyncSearchProvider : SearchProvider
{
    public AsyncSearchProvider(string id, string displayName = null)
        : base(id, displayName)
    {
        fetchItems = (context, items, provider) => FetchItems(context, provider);
    }

    private IEnumerable<SearchItem> FetchItems(SearchContext context, SearchProvider provider)
    {
        while(ResultsNotReady())
        {
            yield return null;
        }

        var oneItem = // Get an item
        yield return oneItem;

        var anotherItem = // Get another item
        yield return anotherItem;

        if(SomeConditionThatBreaksTheSearch())
        {
            // Search must be terminated
            yield break;
        }

        // You can iterate over an enumerable. The enumeration
        // continues where it left.
        foreach(var item in someItems)
        {
            yield return item;
        }
    }
}
```

Registering a Search Provider

Registering an Action Handler

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)