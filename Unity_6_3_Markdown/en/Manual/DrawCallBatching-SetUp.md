* [Optimization](analysis.html)
* [Graphics performance and profiling](graphics-performance-profiling.html)
* [Optimize rendering lots of objects](reduce-draw-calls-landing.html)
* [Combine meshes using batching](DrawCallBatching-landing.html)
* Set up GameObjects for batching

Introduction to batching meshes

Batch static meshes at build time

# Set up GameObjects for batching

For more information about batching, refer to [Introduction to batching meshes](DrawCallBatching.html).

## Get the best results from batching

To get the best results from batching, do the following:

* Share materials among as many **GameObjects**The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)  
  See in [Glossary](Glossary.html#GameObject) as possible.
* If you have two material assets that are identical apart from their textures, combine the textures into a single, larger texture.
* [Profile](profile-rendering.html) the performance of your application with batching turned on and off.

## Check whether Unity batches GameObjects

To check whether Unity batches GameObjects, open the [Frame Debugger](FrameDebugger.html) and check for either of the following:

* Render passes called **Draw Static** or **Draw Dynamic**.
* **Combined Mesh** in the event details of the **Meshes section**.

If Unity isn’t batching GameObjects, check the following for each GameObject:

* The GameObject is active.
* The GameObject has an enabled [Mesh Renderer](class-MeshRenderer.html)A mesh component that takes the geometry from the Mesh Filter and renders it at the position defined by the object’s Transform component. [More info](class-MeshRenderer.html)  
  See in [Glossary](Glossary.html#MeshRenderer) component.
* None of the materials in the Mesh Renderer component use **shaders**A program that runs on the GPU. [More info](Shaders.html)  
  See in [Glossary](Glossary.html#shader) that have `DisableBatching` set to `true`.
* The GameObject has an enabled [Mesh Filter](class-MeshFilter.html)A mesh component that takes a mesh from your assets and passes it to the Mesh Renderer for rendering on the screen. [More info](class-MeshFilter.html)  
  See in [Glossary](Glossary.html#MeshFilter) component with a [Mesh](class-Mesh.html)The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](mesh.html)  
  See in [Glossary](Glossary.html#Mesh).
* The mesh has a vertex count greater than 0, and hasn’t already been combined with another mesh.
* The meshes use the same vertex attribute layout. For example, Unity can’t batch a mesh that uses UVs with one that doesn’t.

If you use **static batching**A technique Unity uses to draw GameObjects on the screen that combines static (non-moving) GameObjects into big Meshes, and renders them in a faster way. [More info](DrawCallBatching.html)  
See in [Glossary](Glossary.html#StaticBatching), check the following:

* The GameObject uses the same mesh, shader variant, texture samplers, **lightmap**A pre-rendered texture that contains the effects of light sources on static objects in the scene. Lightmaps are overlaid on top of scene geometry to create the effect of lighting. [More info](Lightmapping.html)  
  See in [Glossary](Glossary.html#Lightmap), and layer as other meshes you want to batch.
* The mesh is not very small.
* The mesh doesn’t use **LOD**The *Level Of Detail* (LOD) technique is an optimization that reduces the number of triangles that Unity has to render for a GameObject when its distance from the Camera increases. [More info](LevelOfDetail.html)  
  See in [Glossary](Glossary.html#LOD) fading.

## Additional resources

* [Reduce rendering work on the GPU or CPU](OptimizingGraphicsPerformance.html).

Introduction to batching meshes

Batch static meshes at build time

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)