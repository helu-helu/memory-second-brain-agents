* [Optimization](analysis.html)
* [Graphics performance and profiling](graphics-performance-profiling.html)
* [Optimize rendering lots of objects](reduce-draw-calls-landing.html)
* [Combine meshes using batching](DrawCallBatching-landing.html)
* Introduction to batching meshes

Combine meshes using batching

Set up GameObjects for batching

# Introduction to batching meshes

Batching is a [draw call optimization](optimizing-draw-calls.html) method that combines meshes that use the same material, so that Unity can render them using fewer updates to the render state. Batching can improve performance, memory efficiency, and reduce CPU overhead, leading to a smoother frame rate and better player experience.

Batching has the following limitations:

* Batching supports only [Mesh Renderers](class-MeshRenderer.html)A mesh component that takes the geometry from the Mesh Filter and renders it at the position defined by the object’s Transform component. [More info](class-MeshRenderer.html)  
  See in [Glossary](Glossary.html#MeshRenderer). Batching doesn’t support Skinned **Mesh**The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](mesh.html)  
  See in [Glossary](Glossary.html#Mesh) Renderers.
* Batching of transparent **GameObjects**The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)  
  See in [Glossary](Glossary.html#GameObject) might be limited because Unity sorts all meshes back-to-front before batching.
* Unity can’t use **dynamic batching** to batch GameObjects that use negative scale in their [Transform](class-Transform.html) components with GameObjects that use positive scale.

You can also [manually combine meshes](combining-meshes.html), but as a result you can’t cull meshes individually.

## Batch static GameObjects

Static batching combines multiple static meshes into one vertex buffer and one index buffer, using coordinates in world space. Each buffer can contain up to 64,000 vertices, but Unity can create multiple batches.

You can use **static batching** in two ways:

* [At build time](DrawCallBatching-Enable.html)
* [At runtime](static-batching-enable.html)

## Batch moving GameObjects

**Warning:** For most uses, dynamic batching is no longer recommended, because the CPU overhead might be greater than the overhead of a draw call. For more information, refer to [Choose a draw call optimization method](optimizing-draw-calls-choose-method.html).

Dynamic batching is recommended only on lower-end devices. It does the following at runtime:

* Transforms mesh vertices into world space on the CPU rather than on the GPU, and groups them together into one draw call.
* For geometry generated at runtime, such as **particles**A small, simple image or mesh that is emitted by a particle system. A particle system can display and move particles in great numbers to represent a fluid or amorphous entity. The effect of all the particles together creates the impression of the complete entity, such as smoke. [More info](class-ParticleSystem.html)  
  See in [Glossary](Glossary.html#particle), lines, and trails, Unity batches all the meshes into a single vertex buffer, then submits one draw call for each mesh. This is similar to static batching.

Unity also batches meshes when it renders shadows, if the material values the shadow pass uses are the same. For example, if you have multiple crates with the same material but different textures, Unity can still batch the shadows.

Dynamic batching has the following limitations:

* Not supported in the High Definition **Render Pipeline**A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](render-pipelines.html)  
  See in [Glossary](Glossary.html#renderpipeline) (HDRP).
* Meshes must not exceed 900 vertex attributes or 300 vertices. As a result, if you use more vertex attributes, fewer meshes can be batched.
* If GameObjects uses lighting from **lightmap**A pre-rendered texture that contains the effects of light sources on static objects in the scene. Lightmaps are overlaid on top of scene geometry to create the effect of lighting. [More info](Lightmapping.html)  
  See in [Glossary](Glossary.html#Lightmap) textures, they must all use the same lightmap texture and UVs.
* Supports only the first render pass in a multi-pass **shader**A program that runs on the GPU. [More info](Shaders.html)  
  See in [Glossary](Glossary.html#shader). As a result, Unity can’t batch draw calls for additional per-pixel lights in Unity shaders.

For more information, refer to [Batch meshes at runtime](static-batching-enable.html).

## Additional resources

* [Choose a draw call optimization method](choose-draw-call-optimization-method)

Combine meshes using batching

Set up GameObjects for batching

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)