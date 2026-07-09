* [Optimization](analysis.html)
* [Graphics performance and profiling](graphics-performance-profiling.html)
* [Optimize rendering lots of objects](reduce-draw-calls-landing.html)
* [Combine meshes using batching](DrawCallBatching-landing.html)
* Batch static meshes at build time

Set up GameObjects for batching

Batch meshes at runtime

# Batch static meshes at build time

To batch static **GameObjects**The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) at build time, enable **static batching**A technique Unity uses to draw GameObjects on the screen that combines static (non-moving) GameObjects into big Meshes, and renders them in a faster way. [More info](DrawCallBatching.html)  
See in [Glossary](Glossary.html#StaticBatching). For more information about batching, refer to [Introduction to batching meshes](DrawCallBatching.html).

Follow these steps:

1. Go to **Edit** > **Project Settings** > **Player**.
2. In **Other Settings**, enable **Static Batching**.
3. In the **Scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
   See in [Glossary](Glossary.html#Scene) view or **Hierarchy** window, select the GameObject that you want to batch. You can select multiple GameObjects at the same time to enable static batching for all of them.
4. In the ****Inspector**A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
   See in [Glossary](Glossary.html#Inspector)** window, select the [Static Editor Flags](StaticObjects.html) dropdown and enable **Batching Static**.

If you use static batching at build time, Unity doesn’t use any CPU resources at runtime to generate the **mesh**The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](mesh.html)  
See in [Glossary](Glossary.html#Mesh) data for the static batch.

**Note:** Unity uses additional GPU memory to store the combined meshes, even if the meshes are the same. For example, marking trees as static in a dense forest environment can have a large impact on memory. If static batching uses too much memory, [combine meshes manually](combining-meshes.html) instead.

If a mesh is culled because it’s outside the **camera**A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera) view, Unity might not be able to draw all the meshes in a single draw call. This is because the culled mesh leaves a gap in the combined vertex buffers.

## Additional resources

* [Batch meshes at runtime](static-batching-enable.html)

Set up GameObjects for batching

Batch meshes at runtime

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)