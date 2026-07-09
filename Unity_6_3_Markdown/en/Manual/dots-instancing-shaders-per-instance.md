* [Optimization](analysis.html)
* [Graphics performance and profiling](graphics-performance-profiling.html)
* [Graphics performance and profiling in URP](graphics-performance-and-profiling-in-urp.html)
* [Optimizing draw calls in URP](reduce-draw-calls-landing-urp.html)
* [BatchRendererGroup API in URP](batch-renderer-group.html)
* [Writing custom shaders for the BatchRendererGroup API](batch-renderer-group-writing-shaders.html)
* [DOTS Instancing shader examples in URP](dots-instancing-shaders-samples.html)
* Example of a DOTS Instancing shader that accesses per-instance data in URP

DOTS Instancing shader examples in URP

Example of a DOTS Instancing shader that accesses constant data in URP

# Example of a DOTS Instancing shader that accesses per-instance data in URP

In this example:

* The metadata value for `Color` is `0x80001000`.
* The instance index is `5`.
* Data for instance 0 starts at address 0x1000.
* Data for instance 5 is at address 0x1000 + 5 * sizeof(float4) = 0x1050

Because the most significant bit is already set, the accessor macros don’t load defaults. This means that `c0`, `c1`, and `c2` will all have the same value, loaded from `unity_DOTSInstanceData` address `0x1050`.

```
void ExamplePerInstance()
{
    // rawMetadataValue will contain 0x80001000
    uint rawMetadataValue = UNITY_DOTS_INSTANCED_METADATA_NAME(float4, Color);

    float4 c0 = UNITY_ACCESS_DOTS_INSTANCED_PROP(float4, Color);
    float4 c1 = UNITY_ACCESS_DOTS_INSTANCED_PROP_WITH_DEFAULT(float4, Color);
    float4 c2 = UNITY_ACCESS_DOTS_INSTANCED_PROP_WITH_CUSTOM_DEFAULT(float4, Color, float4(1, 2, 3, 4));
}
```

DOTS Instancing shader examples in URP

Example of a DOTS Instancing shader that accesses constant data in URP

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)