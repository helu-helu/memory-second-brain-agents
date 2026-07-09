* [Optimization](analysis.html)
* [Graphics performance and profiling](graphics-performance-profiling.html)
* [Optimize rendering lots of objects](reduce-draw-calls-landing.html)
* [Combine meshes using batching](DrawCallBatching-landing.html)
* Access properties in combined meshes

Combine meshes manually

Optimize mesh rendering using level of detail (LOD)

# Access properties in combined meshes

In the Built-in **Render Pipeline**A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](render-pipelines.html)  
See in [Glossary](Glossary.html#renderpipeline), you can use a [MaterialPropertyBlock](../ScriptReference/MaterialPropertyBlock.html) to change material properties without breaking draw call batching. The CPU still needs to make some render-state changes, but using a `MaterialPropertyBlock` is faster than using multiple materials.

If your project uses a Scriptable Render Pipeline, don’t use a `MaterialPropertyBlock` because they remove SRP Batcher compatibility for the material. Use different materials for the different properties instead.

**Warning**: When you access shared material properties from a C# script, make sure to use [Renderer.sharedMaterial](../ScriptReference/Renderer-sharedMaterial.html) and not [Renderer.material](../ScriptReference/Renderer-material.html). `Renderer.material` creates a copy of the material and assigns the copy back to the Renderer. This stops Unity from batching the draw calls for that Renderer.

## Additional resources

* [Writing custom shaders in the Built-in Render Pipeline](writing-shaders-birp.html)
* [Introduction to material properties](writing-shader-material-properties.html)

Combine meshes manually

Optimize mesh rendering using level of detail (LOD)

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)