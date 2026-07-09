* [Optimization](analysis.html)
* [Graphics performance and profiling](graphics-performance-profiling.html)
* [Graphics performance and profiling in the Built-In Render Pipeline](graphics-performance-birp.html)
* [Creating custom shaders that support GPU instancing in the Built-In Render Pipeline](gpu-instancing-shader.html)
* GPU Instancing in the Built-In Render Pipeline

Creating custom shaders that support GPU instancing in the Built-In Render Pipeline

Add per-instance properties to GPU instancing shaders in the Built-In Render Pipeline

# GPU Instancing in the Built-In Render Pipeline

This section contains information on how to add GPU instancing support to a custom Unity **shader**A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#shader). It first explains the shader keywords, variables, and functions custom Unity shaders require to support GPU instancing. Then it includes examples of how to add per-instance data to both **surface shaders**A streamlined way of writing shaders for the Built-in Render Pipeline. [More info](SL-SurfaceShaders.html)  
See in [Glossary](Glossary.html#SurfaceShader) and vertex/fragment shaders.

## Render pipeline compatibility

| **Feature** | **Universal **Render Pipeline**A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](render-pipelines.html) See in [Glossary](Glossary.html#renderpipeline) (URP)** | **High Definition Render Pipeline (HDRP)** | **Custom Scriptable Render Pipeline (SRP)** | **Built-in Render Pipeline** |
| --- | --- | --- | --- | --- |
| **Custom GPU instanced shaders** | No | No | No | Yes |

## Additional resources

* [GPU instancing](GPUInstancing-landing.html)
* [Graphics performance and profiling](graphics-performance-profiling.html)

Creating custom shaders that support GPU instancing in the Built-In Render Pipeline

Add per-instance properties to GPU instancing shaders in the Built-In Render Pipeline

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)