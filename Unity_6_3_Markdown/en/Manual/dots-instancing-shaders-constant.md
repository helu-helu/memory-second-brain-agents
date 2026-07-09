* [Optimization](analysis.html)
* [Graphics performance and profiling](graphics-performance-profiling.html)
* [Graphics performance and profiling in URP](graphics-performance-and-profiling-in-urp.html)
* [Optimizing draw calls in URP](reduce-draw-calls-landing-urp.html)
* [BatchRendererGroup API in URP](batch-renderer-group.html)
* [Writing custom shaders for the BatchRendererGroup API](batch-renderer-group-writing-shaders.html)
* [DOTS Instancing shader examples in URP](dots-instancing-shaders-samples.html)
* Example of a DOTS Instancing shader that accesses constant data in URP

Example of a DOTS Instancing shader that accesses per-instance data in URP

Example of using UNITY\_DOTS\_INSTANCED\_PROP macros in a DOTS Instancing shader in URP

# Example of a DOTS Instancing shader that accesses constant data in URP

In this example:

* The metadata value for `Color` is `0x00001000`.
* The instance index is `5`.
* Data for instance 0 starts at address 0x1000.
* The most significant bit is not set so data for instance 5 is at the same address as instance 0.

Because the most significant bit is not set, the accessor macros that fall back to defaults don’t access `unity_DOTSInstanceData`. This means that:

* `c0` will contain the value from `unity_DOTSInstanceData` address `0x1000`.
* `c1` will contain the value of the regular material property **Color**, and cause a compile error if the Color property doesn’t exist.
* `c2` will contain `(1, 2, 3, 4)` because that was passed as the explicit default value.

```
void ExampleConstant()
{
    // rawMetadataValue will contain 0x00001000
    uint rawMetadataValue = UNITY_DOTS_INSTANCED_METADATA_NAME(float4, Color);
    float4 c0 = UNITY_ACCESS_DOTS_INSTANCED_PROP(float4, Color);
    float4 c1 = UNITY_ACCESS_DOTS_INSTANCED_PROP_WITH_DEFAULT(float4, Color);
    float4 c2 = UNITY_ACCESS_DOTS_INSTANCED_PROP_WITH_CUSTOM_DEFAULT(float4, Color, float4(1, 2, 3, 4));
}
```

Example of a DOTS Instancing shader that accesses per-instance data in URP

Example of using UNITY\_DOTS\_INSTANCED\_PROP macros in a DOTS Instancing shader in URP

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)