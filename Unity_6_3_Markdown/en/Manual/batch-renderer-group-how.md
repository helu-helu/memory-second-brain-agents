* [Optimization](analysis.html)
* [Graphics performance and profiling](graphics-performance-profiling.html)
* [Graphics performance and profiling in URP](graphics-performance-and-profiling-in-urp.html)
* [Optimizing draw calls in URP](reduce-draw-calls-landing-urp.html)
* [BatchRendererGroup API in URP](batch-renderer-group.html)
* Introduction to the BatchRendererGroup API in URP

BatchRendererGroup API in URP

Set up your project for the BatchRendererGroup API in URP

# Introduction to the BatchRendererGroup API in URP

BRG is the perfect tool to:

* Render DOTS [Entities](https://docs.unity3d.com/Packages/com.unity.entities@latest). For more information how Entities uses BRG, refer to [Entities Graphics Performance](https://docs.unity3d.com/Packages/com.unity.entities.graphics@1.2/manual/entities-graphics-performance.html).
* Render a large number of environment objects where using individual **GameObjects**The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)  
  See in [Glossary](Glossary.html#GameObject) would be too resource-intensive. For example, procedurally-placed plants or rocks.
* Render custom **terrain**The landscape in your scene. A Terrain GameObject adds a large flat plane to your scene and you can use the Terrain’s Inspector window to create a detailed landscape. [More info](terrain-UsingTerrains.html)  
  See in [Glossary](Glossary.html#Terrain) patches. You can use different meshes or materials to display different levels of detail.

## Render pipeline compatibility

The following table shows which **render pipelines**A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](render-pipelines.html)  
See in [Glossary](Glossary.html#renderpipeline) support BRG.

| **Feature name** | **Universal Render Pipeline (URP)** | **High Definition Render Pipeline (HDRP)** | **Custom SRP** | **Built-in Render Pipeline** |
| --- | --- | --- | --- | --- |
| BatchRendererGroup | Yes (1) | Yes (1) | Yes (1) | No |

**Notes**:

1. If the project uses the SRP Batcher.

## Platform compatibility

Unity supports BRG on:

* Windows using DirectX 11
* Windows using DirectX 12
* Windows using Vulkan
* Universal Windows Platform
* Linux using Vulkan
* macOS using Metal
* iOS
* Android (Vulkan and OpenGL ES 3.x)
* PlayStation 4
* PlayStation 5
* Xbox One
* Xbox Series X and Xbox Series S
* Nintendo Switch

## How BatchRendererGroup works

To render to the screen, BatchRendererGroup (BRG) generates [draw commands](../ScriptReference/Rendering.BatchDrawCommand.html) which are a BRG-specific concept that contains everything Unity needs to efficiently create optimized, [instanced](GPUInstancing.html) draw calls.

To determine when to render the instances in a draw command, BRG uses [filter settings](../ScriptReference/Rendering.BatchFilterSettings.html). Filter settings control when to render instances themselves, but also when to render certain facets of each instance such as its shadows and motion vectors

Because the same filter settings can often apply to a large number of draw commands, BRG uses [draw ranges](../ScriptReference/Rendering.BatchDrawRange.html) to apply filter settings to a range of draw commands. A draw range combines a contiguous number of draw commands with an instance of filter settings that apply to them. Draw ranges are especially useful if the filter settings determine that Unity shouldn’t render the draw commands, because this makes it possible for Unity to efficiently skip rendering for every draw command in the range.

There is no restriction on which instances are in which draw calls. It’s possible to render the same instance, an object with the same instance index and batchID, many times with different meshes and materials. One example where this can be useful is drawing different sub-meshes with different materials, but using the same instance indices to share properties like transform matrices between the draws.

For information on how to create a renderer with BRG, see [Creating a renderer with BatchRendererGroup](batch-renderer-group-creating-a-renderer.html).

## Technical limitations

In most cases, Unity renders a draw command as a single, platform-level, instanced draw call for each compatible [DrawRenderers](../ScriptReference/Rendering.ScriptableRenderContext.DrawRenderers.html) call in the Scriptable Render Pipeline. However, that isn’t possible when the graphics API has a lower size limit for draw calls than the draw command’s `visibleCount`. In these situations, Unity splits the draw command into multiple instanced draw calls.

Unity doesn’t perform [frustum culling](UnderstandingFrustum.html) or [occlusion culling](OcclusionCulling.html)A process that disables rendering GameObjects that are hidden (occluded) from the view of the camera. [More info](OcclusionCulling.html)  
See in [Glossary](Glossary.html#occlusionculling) of instances you draw with the `BatchRendererGroup` API. You must provide your own culling code.

BatchRendererGroup API in URP

Set up your project for the BatchRendererGroup API in URP

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)