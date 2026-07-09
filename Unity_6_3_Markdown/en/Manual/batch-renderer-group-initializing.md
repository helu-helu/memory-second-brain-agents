* [Optimization](analysis.html)
* [Graphics performance and profiling](graphics-performance-profiling.html)
* [Graphics performance and profiling in URP](graphics-performance-and-profiling-in-urp.html)
* [Optimizing draw calls in URP](reduce-draw-calls-landing-urp.html)
* [BatchRendererGroup API in URP](batch-renderer-group.html)
* [Creating a renderer with the BatchRendererGroup API in URP](batch-renderer-group-creating-a-renderer.html)
* Initialize a BatchRendererGroup object in URP

Creating a renderer with the BatchRendererGroup API in URP

Register meshes and materials with the BatchRendererGroup API in URP

# Initialize a BatchRendererGroup object in URP

The first step to render using BRG is to create an instance of [BatchRendererGroup](../ScriptReference/Rendering.BatchRendererGroup.html) and initialize it with an implementation of [OnPerformCulling](../ScriptReference/Rendering.BatchRendererGroup.OnPerformCulling.html).

The OnPerformCulling callback is the main entry point of BRG and Unity calls it whenever it culls visible objects. For information on the parameters it receives, see [OnPerformCulling](../ScriptReference/Rendering.BatchRendererGroup.OnPerformCulling.html). Typically, there are two tasks that the OnPerformCulling callback needs to perform:

* Visibility culling to determine which of its instances are visible based on the [BatchCullingContext](../ScriptReference/Rendering.BatchCullingContext.html) parameter.
* Output the actual draw commands to render those instances. To do this you write to the [BatchCullingOutput](../ScriptReference/Rendering.BatchCullingOutput.html) parameter.

In simple implementations, you can do these tasks directly in the OnPerformCulling callback, but for high-performance implementations, it’s best practice to do most of this work in [Burst](https://docs.unity3d.com/Packages/com.unity.burst@latest) jobs. The OnPerformCulling callback should return a [JobHandle](../ScriptReference/Unity.Jobs.JobHandle.html) that completes after the jobs write the output into the [BatchCullingOutput](../ScriptReference/Rendering.BatchCullingOutput.html) parameter. If your implementation doesn’t use jobs, you can return an empty JobHandle.

See the following code sample for an example of how to create a BatchRendererGroup object and initialize it with the most minimum OnPerformCulling callback that compiles.

```
using System;
using Unity.Collections;
using Unity.Collections.LowLevel.Unsafe;
using Unity.Jobs;
using UnityEngine;
using UnityEngine.Rendering;

public class SimpleBRGExample : MonoBehaviour
{
    private BatchRendererGroup m_BRG;

    private void Start()
    {
        m_BRG = new BatchRendererGroup(this.OnPerformCulling, IntPtr.Zero);
    }

    private void OnDisable()
    {
        m_BRG.Dispose();
    }

    public unsafe JobHandle OnPerformCulling(
        BatchRendererGroup rendererGroup,
        BatchCullingContext cullingContext,
        BatchCullingOutput cullingOutput,
        IntPtr userContext)
    {
        // This example doesn't use jobs, so it can return an empty JobHandle.
        // Performance-sensitive applications should use Burst jobs to implement
        // culling and draw command output. In this case, this function would return a
        // handle here that completes when the Burst jobs finish.
        return new JobHandle();
    }
}
```

Before you use OnPerformCulling to create draw commands, you need to provide your BatchRendererGroup object any meshes you want it to draw, and any materials you want it to use. For more information, see the next topic, [Registering meshes and materials](batch-renderer-group-registering-meshes-and-materials.html).

Creating a renderer with the BatchRendererGroup API in URP

Register meshes and materials with the BatchRendererGroup API in URP

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)