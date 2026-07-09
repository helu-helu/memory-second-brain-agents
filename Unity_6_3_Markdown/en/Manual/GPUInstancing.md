* [Optimization](analysis.html)
* [Graphics performance and profiling](graphics-performance-profiling.html)
* [Optimize rendering lots of objects](reduce-draw-calls-landing.html)
* [GPU instancing](GPUInstancing-landing.html)
* Introduction to GPU instancing

GPU instancing

Enable GPU instancing for a prebuilt material

# Introduction to GPU instancing

GPU instancing is a [draw call optimization](optimizing-draw-calls.html) method that uses a single draw call to render multiple **GameObjects**The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) that use the same **mesh**The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](mesh.html)  
See in [Glossary](Glossary.html#Mesh) and material. This speeds up rendering when you draw things that appear multiple times in a **scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene), for example, trees or bushes.

GPU instancing is a built-in functionality of GPUs. Each copy of the mesh is called an instance. Each instance can have different properties, such as color or scale.

The performance benefits of GPU instancing depend on the platform and the GPU. For each draw call, Unity has to collect, combine, and upload properties from various memory locations, so the performance overhead might outweigh the benefits. The performance benefits are better on mobile platforms than on desktop platforms.

## Render pipeline compatibility

GPU instancing is compatible with all Unity **render pipelines**A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](render-pipelines.html)  
See in [Glossary](Glossary.html#renderpipeline), with the following limitations:

* If you use the Universal Render Pipeline (URP) or High Definition Render Pipeline (HDRP), GPU instancing works with custom **shaders**A program that runs on the GPU. [More info](Shaders.html)  
  See in [Glossary](Glossary.html#shader) only if you disable the [Scriptable Render Pipeline (SRP) Batcher](SRPBatcher.html) or [make a shader incompatible with the SRP Batcher](SRPBatcher-Incompatible.html).
* If you use the Built-in Render Pipeline (BiRP), GPU Instancing doesn’t work with Shader Graph shaders.

For information on draw call optimization methods you can use instead of GPU instancing, refer to [Choose a method for optimizing draw calls](optimizing-draw-calls-choose-method.html).

## Indirect lighting compatibility

GPU instancing supports the following types of GameObject:

* Dynamic GameObjects that get lighting from **Light Probes**Light probes store information about how light passes through space in your scene. A collection of light probes arranged within a given space can improve lighting on moving objects and static LOD scenery within that space. [More info](LightProbes.html)  
  See in [Glossary](Glossary.html#LightProbe).
* Static GameObjects that get lighting from **lightmaps**A pre-rendered texture that contains the effects of light sources on static objects in the scene. Lightmaps are overlaid on top of scene geometry to create the effect of lighting. [More info](Lightmapping.html)  
  See in [Glossary](Glossary.html#Lightmap), if they have **Contribute GI** enabled in their [Static Editor Flags](StaticObjects.html), and they bake to the same lightmap texture.
* GameObjects that use **Light Probe Proxy Volumes**A component that allows you to use more lighting information for large dynamic GameObjects that cannot use baked lightmaps (for example, large Particle Systems or skinned Meshes). [More info](class-LightProbeProxyVolume.html)  
  See in [Glossary](Glossary.html#LightProbeProxyVolume) (LPPV). You must bake the LPPV for the entire space that contains all the instances.

## Shader and mesh compatibility

The following meshes are compatible if you use prebuilt materials:

* [Mesh Renderer components](class-MeshRenderer.html) in your scene. Skinned **Mesh Renderer**A mesh component that takes the geometry from the Mesh Filter and renders it at the position defined by the object’s Transform component. [More info](class-MeshRenderer.html)  
  See in [Glossary](Glossary.html#MeshRenderer) components are not supported.
* Meshes you render in a script using APIs that support GPU instancing in prebuilt materials, such as [Graphics.RenderMeshInstanced](../ScriptReference/Graphics.RenderMeshInstanced.html).

The following shaders support GPU instancing:

* Most [prebuilt materials](built-in-materials-and-shaders.html). Compatible shaders have an **Enable GPU Instancing** property.
* [Shader Graph](shader-graph.html) materials, if you use URP or HDRP.

To create a custom shader that supports GPU instancing, refer to the following:

* [Creating custom shaders that support GPU instancing in the Built-In Render Pipeline](gpu-instancing-shader.html)
* [Indirect & Procedural Rendering in Shader Graph](https://discussions.unity.com/t/indirect-procedural-rendering/1664601) on the Unity Discussions site if you use URP or HDRP.

## Additional resources

* [Choose a method for optimizing draw calls](optimizing-draw-calls-choose-method.html)

GPU instancing

Enable GPU instancing for a prebuilt material

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)