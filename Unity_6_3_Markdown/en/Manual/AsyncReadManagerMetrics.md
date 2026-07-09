* [Assets and media](assets-and-media.html)
* [Analyzing asset processes](assets-optimizing.html)
* Collect asset loading metrics

Analyzing asset processes

Asset Loading Profiler module reference

# Collect asset loading metrics

Use the [`AsyncReadManagerMetrics`](../ScriptReference/Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetrics.html) class to monitor runtime asset loading and file reading performance. This class records data for all file read operations managed by the [`AsyncReadManager`](../ScriptReference/Unity.IO.LowLevel.Unsafe.AsyncReadManager.html).

Unity uses the [`AsyncReadManager`](../ScriptReference/Unity.IO.LowLevel.Unsafe.AsyncReadManager.html) to read most files at runtime, including AssetBundles, Addressables, and Resources. You can also load files from **scripts**A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts) using [`AsyncReadManager.Read`](../ScriptReference/Unity.IO.LowLevel.Unsafe.AsyncReadManager.Read.html).

You can use the [`AsyncReadManagerMetrics`](../ScriptReference/Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetrics.html) to do the following:

* Start and stop metrics collection.
* Retrieve and analyze recorded metrics data.
* Filter and summarize data to help your analysis.

This information can help you identify problems with asset loading and measure the impact of your changes have on performance.

## Development build requirement

The [`AsyncReadManagerMetrics`](../ScriptReference/Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetrics.html) class is only available in **development builds**A development build includes debug symbols and enables the Profiler. [More info](building-introduction.html)  
See in [Glossary](Glossary.html#developmentbuild). To ensure compatibility, wrap calls to `AsyncReadManagerMetrics` APIs in an `#if` preprocessor directive using the `ENABLE_PROFILER` symbol. For older Unity versions, use the `UNITY_2020_2_OR_NEWER` symbol to remove the metric code. For example:

```
#if ENABLE_PROFILER && UNITY_2020_2_OR_NEWER
    AsyncReadManagerMetrics.StartCollectingMetrics();
#endif
```

## Enable metric collection

Enable metrics collection before any data is recorded. You can do this in one of the following ways:

* Call [`AsyncReadManagerMetrics.StartCollectingMetrics`](../ScriptReference/Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetrics.StartCollectingMetrics.html) in your script.
* Pass the `-enable-file-read-metrics` command-line argument when launching your application.

To collect metrics in Play mode, pass the `-enable-file-read-metrics` argument when launching the Unity Editor. However, the Editor loads some categories of assets, such as textures, and doesn’t reload them when you enter Play mode. For complete file I/O metrics, you must collect data from a development build of your application.

## Getting metric data

Use [`GetMetrics`](../ScriptReference/Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetrics.GetMetrics.html) to retrieve collected metrics from [`AsyncReadManagerMetrics`](../ScriptReference/Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetrics.html). Specify [`AsyncReadManagerMetrics.Flags`](../ScriptReference/Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetrics.Flags.html) to determine whether to clear metrics after retrieval. Clearing metrics removes completed (including canceled and failed) reads but retains queued or in-progress operations. To access the metrics for unfinished operations, call [`GetMetrics`](../ScriptReference/Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetrics.GetMetrics.html) again after they complete. By clearing the metrics regularly, you can avoid rereading the same data and also reduce the data overhead of the system.

```
#if ENABLE_PROFILER && UNITY_2020_2_OR_NEWER
    AsyncReadManagerRequestMetric[] metrics 
        = AsyncReadManagerMetrics.GetMetrics(AsyncReadManagerMetrics.Flags.ClearOnRead);
#endif
```

Metrics data includes the following context data:

* The [`AssetLoadingSubsystem`](../ScriptReference/Unity.IO.LowLevel.Unsafe.AssetLoadingSubsystem.html) that initiated the read. If unavailable, defaults to [`Other`](../ScriptReference/Unity.IO.LowLevel.Unsafe.AssetLoadingSubsystem.Other.html).
* [`AssetName`](../ScriptReference/Unity.IO.LowLevel.Unsafe.AsyncReadManagerRequestMetric.AssetName.html). If unavailable, defaults to empty.
* [`AssetTypeID`](../ScriptReference/Unity.IO.LowLevel.Unsafe.AsyncReadManagerRequestMetric.AssetTypeId.html). If unavailable, defaults to zero.

The following is a list of supported asset TypeIDs:

| **TypeID** | **Type name** |
| --- | --- |
| 28 | Texture2D |
| 117 | Texture3D |
| 89 | **CubeMap**A collection of six square textures that can represent the reflections in an environment or the skybox drawn behind your geometry. The six squares form the faces of an imaginary cube that surrounds an object; each face represents the view along the directions of the world axes (up, down, left, right, forward and back). [More info](class-Cubemap-landing.html) See in [Glossary](Glossary.html#Cubemap) |
| 43 | Mesh |

For other TypeIDs that might appear, refer to [YAML class ID reference](ClassIDReference.html).

## Get summarized data

Get a summary of the `AsyncReadManager` metrics with the following methods:

* [`GetCurrentSummaryMetrics`](../ScriptReference/Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetrics.GetCurrentSummaryMetrics.html): Returns a summary of all the metrics collected after the last time you cleared the metric store.
* [`GetSummaryOfMetrics`](../ScriptReference/Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetrics.GetSummaryOfMetrics.html): Returns a summary of the metrics in an array of [`AsyncReadManagerRequestMetric`](../ScriptReference/Unity.IO.LowLevel.Unsafe.AsyncReadManagerRequestMetric.html), which you can get by calling [`GetMetrics`](../ScriptReference/Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetrics.GetMetrics.html).

For example:

```
#if ENABLE_PROFILER && UNITY_2020_2_OR_NEWER
    AsyncReadManagerSummaryMetrics summaryOfMetrics 
        = AsyncReadManagerMetrics.GetCurrentSummaryMetrics(AsyncReadManagerMetrics.Flags.ClearOnRead);
#endif
```

Or:

```
#if ENABLE_PROFILER && UNITY_2020_2_OR_NEWER
    AsyncReadManagerRequestMetric[] metrics 
        = AsyncReadManagerMetrics.GetMetrics(AsyncReadManagerMetrics.Flags.ClearOnRead);
    AsyncReadManagerSummaryMetrics summaryOfMetrics 
        = AsyncReadManagerMetrics.GetSummaryOfMetrics(metrics);
#endif
```

Summary statistics include:

* Average bandwidth
* Average read size
* Asset type with the longest load time
* Number of reads
* Number of requests
* Total bytes read

For a full list of summary metrics, refer to [`AsyncReadManagerSummaryMetrics`](../ScriptReference/Unity.IO.LowLevel.Unsafe.AsyncReadManagerSummaryMetrics.html).

By default, the summarized statistics include all read operations, including those that are queued or in-progress. You can use a filter to limit the summary to those operations you’re interested in. For example, you can use a filter to limit the summarized statistics to completed read operations for texture assets.

**Note:** Calculating summaries requires processing resources. To avoid affecting your measurements, collect metrics first and summarize them after operations are complete.

## Using summary filters

Use [`AsyncReadManagerMetricsFilters`](../ScriptReference/Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetricsFilters.html) to filter summarized data. You can filter by the following:

* Asset type: By [YAML ID](ClassIDReference.html).
* [Processing state](../ScriptReference/Unity.IO.LowLevel.Unsafe.ProcessingState.html): For example, queued, reading, or completed.
* [Read type](../ScriptReference/Unity.IO.LowLevel.Unsafe.FileReadType.html): For example, async or sync.
* [Priority](../ScriptReference/Unity.IO.LowLevel.Unsafe.Priority.html): For example, high or low.
* Subsystem: By [`AssetLoadingSubsystem`](../ScriptReference/Unity.IO.LowLevel.Unsafe.AssetLoadingSubsystem.html).

You can set multiple categories for the same filter. A read operation must match all categories for the metrics of that operation to be included in the summary. For example, you can specify values for both the [`ProcessingState`](../ScriptReference/Unity.IO.LowLevel.Unsafe.ProcessingState.html) and the [`Subsystem`](../ScriptReference/Unity.IO.LowLevel.Unsafe.AssetLoadingSubsystem.html) of a filter to summarize only operations in the designated processing states initiated by the designated subsytems.

You can also specify multiple values for a category. In this case, a read operation can match any value you specify for a category for its metrics to be included in the summary. For example, filtering by both [mesh](../ScriptReference/Unity.IO.LowLevel.Unsafe.AssetLoadingSubsystem.Mesh.html)The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](mesh.html)  
See in [Glossary](Glossary.html#Mesh) and [texture](../ScriptReference/Unity.IO.LowLevel.Unsafe.AssetLoadingSubsystem.Texture.html)An image used when rendering a GameObject, Sprite, or UI element. Textures are often applied to the surface of a mesh to give it visual detail. [More info](class-TextureImporter.html)  
See in [Glossary](Glossary.html#texture) includes operations for both asset types.

## Additional resources

* [Asset Loading Profiler module](profiler-asset-loading-module.html)

Analyzing asset processes

Asset Loading Profiler module reference

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)