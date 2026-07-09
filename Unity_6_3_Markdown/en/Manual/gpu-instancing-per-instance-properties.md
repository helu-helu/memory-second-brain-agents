* [Optimization](analysis.html)
* [Graphics performance and profiling](graphics-performance-profiling.html)
* [Graphics performance and profiling in the Built-In Render Pipeline](graphics-performance-birp.html)
* [Creating custom shaders that support GPU instancing in the Built-In Render Pipeline](gpu-instancing-shader.html)
* Add per-instance properties to GPU instancing shaders in the Built-In Render Pipeline

GPU Instancing in the Built-In Render Pipeline

Examples of GPU instancing shaders in the Built-In Render Pipeline

# Add per-instance properties to GPU instancing shaders in the Built-In Render Pipeline

By default, Unity GPU instances **GameObjects**The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) with different [Transforms](class-Transform.html) in each instanced draw call. To add more variation to the instances, modify the **shader**A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#shader) to add per-instance properties such as color. You can do this both in **surface shaders**A streamlined way of writing shaders for the Built-in Render Pipeline. [More info](SL-SurfaceShaders.html)  
See in [Glossary](Glossary.html#SurfaceShader) and in vertex/fragment shaders.

Custom shaders don’t need per-instance data, but they do require an instance ID because world matrices need one to function correctly. Surface shaders automatically set up an instance ID, but custom vertex and fragment shaders don’t. To set up the ID for custom vertex and fragment shaders, use UNITY\_SETUP\_INSTANCE\_ID at the beginning of the shader. For an example of how to do this, see [Vertex and fragment shader](gpu-instancing-vertex-fragment-shader-example.html).

When you declare an instanced property, Unity gathers all the property values from the MaterialPropertyBlock objects set on GameObjects into a single draw call. For an example of how to use MaterialPropertyBlock objects to set per-instance data at runtime, see [Changing per-instance data at runtime](gpu-instancing-change-data.html).

When adding per-instance data to multi-pass shaders, keep the following in mind:

* If a multi-pass shader has more than two passes, Unity only instances the first pass. This is because Unity renders later passes together for each object, which forces material changes.
* If you use the Forward **rendering path**The technique that a render pipeline uses to render graphics. Choosing a different rendering path affects how lighting and shading are calculated. Some rendering paths are more suited to different platforms and hardware than others. [More info](RenderingPaths.html)  
  See in [Glossary](Glossary.html#renderingpath) in the Built-in **Render Pipeline**A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](render-pipelines.html)  
  See in [Glossary](Glossary.html#renderpipeline), Unity can’t efficiently instance objects that are affected by multiple lights. Unity can only use instancing effectively for the base pass, not for additional passes. For more information about lighting passes, see documentation on [Forward Rendering and Pass Tags](RenderTech-ForwardRendering.html).

When you use multiple per-instance properties, you don’t need to fill all of them in `MaterialPropertyBlock` objects. Also, if one instance lacks a property, Unity takes the default value from the referenced material. If the material doesn’t have a default value for the property, Unity sets the value to 0. Don’t put non-instanced properties in the `MaterialPropertyBlock`, because this disables instancing. Instead, create different materials for them.

GPU Instancing in the Built-In Render Pipeline

Examples of GPU instancing shaders in the Built-In Render Pipeline

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)