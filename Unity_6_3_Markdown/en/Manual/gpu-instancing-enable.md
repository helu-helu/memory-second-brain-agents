* [Optimization](analysis.html)
* [Graphics performance and profiling](graphics-performance-profiling.html)
* [Optimize rendering lots of objects](reduce-draw-calls-landing.html)
* [GPU instancing](GPUInstancing-landing.html)
* Enable GPU instancing for a prebuilt material

Introduction to GPU instancing

Troubleshooting GPU instancing

# Enable GPU instancing for a prebuilt material

To enable GPU instancing for a [prebuilt materials](built-in-materials-and-shaders.html), follow these steps:

1. Select the material in the **Project** window.
2. In the **Advanced Options** section of the ****Inspector**A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
   See in [Glossary](Glossary.html#Inspector)** window, enable **Enable GPU Instancing**.

**Note:** If you use the Universal **Render Pipeline**A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](render-pipelines.html)  
See in [Glossary](Glossary.html#renderpipeline) (URP) or High Definition Render Pipeline (HDRP), the recommended best practice is to use the [SRP Batcher](SRPBatcher.html) instead, which is enabled by default. GPU instancing works only if you [disable the SRP Batcher](SRPBatcher-Incompatible.html).

If multiple **GameObjects**The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) use the same **mesh**The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](mesh.html)  
See in [Glossary](Glossary.html#Mesh) and material, Unity now uses GPU instancing to render them in single draw calls. To check this, open the **Frame Debugger** and look for render passes called **Draw Mesh (Instanced)**.

If there’s no **Enable GPU Instancing** property, the prebuilt **shader**A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#shader) doesn’t support GPU instancing.

## Change the properties of instances

To change the properties of instances at runtime, for example to give each instance a different color or position, create a script to do the following:

1. Create a [MaterialPropertyBlock](../ScriptReference/MaterialPropertyBlock.html) with the property value for the instance.
2. Attach the script to the [Mesh Renderer](class-MeshRenderer.html)A mesh component that takes the geometry from the Mesh Filter and renders it at the position defined by the object’s Transform component. [More info](class-MeshRenderer.html)  
   See in [Glossary](Glossary.html#MeshRenderer) component of the GameObject.

For more information, refer to [MaterialPropertyBlock](../ScriptReference/MaterialPropertyBlock.html).

## Create custom instances

To render multiple instances of a mesh in a script using GPU instancing, use one of the following APIs:

* [Graphics.RenderMeshInstanced](../ScriptReference/Graphics.RenderMeshInstanced.html)
* [Graphics.RenderMeshIndirect](../ScriptReference/Graphics.RenderMeshIndirect.html)
* [Graphics.RenderMeshPrimitives](../ScriptReference/Graphics.RenderMeshPrimitives.html)

## Additional resources

* [Creating custom shaders that support GPU instancing in the Built-In Render Pipeline](gpu-instancing-shader.html)
* [Indirect & Procedural Rendering in Shader Graph](https://discussions.unity.com/t/indirect-procedural-rendering/1664601)

Introduction to GPU instancing

Troubleshooting GPU instancing

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)