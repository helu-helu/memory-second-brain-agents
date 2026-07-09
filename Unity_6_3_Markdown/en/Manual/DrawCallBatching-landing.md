* [Optimization](analysis.html)
* [Graphics performance and profiling](graphics-performance-profiling.html)
* [Optimize rendering lots of objects](reduce-draw-calls-landing.html)
* Combine meshes using batching

Troubleshooting GPU instancing

Introduction to batching meshes

# Combine meshes using batching

Resources and approaches for improving performance by combining static **GameObjects**The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) or moving GameObjects into fewer draw calls.

| **Page** | **Description** |
| --- | --- |
| [Introduction to batching](DrawCallBatching.html) | Understand how Unity creates batches of static and dynamic GameObjects to reduce draw calls. |
| [Set up GameObjects for batching](DrawCallBatching-SetUp.html) | Get the best results from batching, and make sure Unity batches GameObjects. |
| [Batch static meshes at build time](DrawCallBatching-Enable.html) | Use **static batching**A technique Unity uses to draw GameObjects on the screen that combines static (non-moving) GameObjects into big Meshes, and renders them in a faster way. [More info](DrawCallBatching.html) See in [Glossary](Glossary.html#StaticBatching) to combine static meshes at build time. |
| [Batch meshes at runtime](static-batching-enable.html) | Batch static objects with the `StaticBatchingUtility` API, or dynamic GameObjects with **dynamic batching**An automatic Unity process which attempts to render multiple meshes as if they were a single mesh for optimized graphics performance. The technique transforms all of the GameObject vertices on the CPU and groups many similar vertices together. [More info](DrawCallBatching.html) See in [Glossary](Glossary.html#dynamicbatching). |
| [Combine meshes manually](combining-meshes.html) | Merge multiple meshes into a single **mesh**The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](mesh.html) See in [Glossary](Glossary.html#Mesh) that Unity can render in a single draw call. |
| [Access properties in combined meshes](DrawCallBatching-Properties.html) | Use MaterialPropertyBlocks to change properties of combined meshes without breaking batching. |

## Additional resources

* [Choose a method for optimizing draw calls](optimizing-draw-calls-choose-method.html)
* [Reduce rendering work on the CPU or GPU](OptimizingGraphicsPerformance.html)

Troubleshooting GPU instancing

Introduction to batching meshes

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)