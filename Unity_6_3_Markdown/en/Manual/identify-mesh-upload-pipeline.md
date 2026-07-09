* [Optimization](analysis.html)
* [Graphics performance and profiling](graphics-performance-profiling.html)
* [Loading texture and mesh data asynchronously](loading-texture-mesh-data-asynchronously.html)
* Check whether a mesh uses the asynchronous upload pipeline

Texture and mesh loading

Configure the asynchronous upload pipeline

# Check whether a mesh uses the asynchronous upload pipeline

To identify which upload pipeline Unity is using for a **mesh**The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](mesh.html)  
See in [Glossary](Glossary.html#Mesh), you can use the [Profiler](Profiler.html)A window that helps you to optimize your game. It shows how much time is spent in the various areas of your game. For example, it can report the percentage of time spent rendering, animating, or in your game logic. [More info](Profiler.html)  
See in [Glossary](Glossary.html#Profiler) or another profiling tool and observe thread activity and **profiler markers**Placed in code to describe a CPU or GPU event that is then displayed in the Unity Profiler window. Added to Unity code by default, or you can use [ProfilerMarker API](https://docs.unity3d.com/Packages/com.unity.profiling.core@latest/index.html?subfolder=/manual/profilermarker-guide.html) to add your own custom markers. [More info](profiler-markers.html)  
See in [Glossary](Glossary.html#profilermarker).

The following indicate that Unity is using the asynchronous upload pipeline to upload textures or meshes:

* The `AsyncUploadManager.ScheduleAsyncRead`, `AsyncReadManager.ReadFile`, and `Async.DirectTextureLoadBegin` profiler markers.
* Activity on the `AsyncRead` thread.

If you do not see this activity, then Unity is not using the asynchronous upload pipeline.

Note that the following profiler markers do not indicate that Unity is using the asynchronous upload pipeline; Unity calls them to check whether any asynchronous upload work needs to occur:

* `Initialization.AsyncUploadTimeSlicedUpdate`
* `AsyncUploadManager.AsyncResourceUpload`
* `AsyncUploadManager.ScheduleAsyncCommands`

Texture and mesh loading

Configure the asynchronous upload pipeline

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)