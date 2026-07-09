* [Optimization](analysis.html)
* [Graphics performance and profiling](graphics-performance-profiling.html)
* [Loading texture and mesh data asynchronously](loading-texture-mesh-data-asynchronously.html)
* Configure the asynchronous upload pipeline

Check whether a mesh uses the asynchronous upload pipeline

Graphics performance and profiling in URP

# Configure the asynchronous upload pipeline

Unity provides optimization settings specific to the asynchronous upload pipeline. To access these settings, open the Project’s [Quality settings](class-QualitySettings.html).

Note that you cannot configure settings for the synchronous upload pipeline.

![The Async Upload settings in the Quality settings](../uploads/Main/AsyncUploadQualitySettings.png)


The Async Upload settings in the Quality settings

### Configure the streaming buffer for mesh data

Unity re-uses a single ring buffer to stream texture and **mesh**The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](mesh.html)  
See in [Glossary](Glossary.html#Mesh) data to the GPU. This reduces the number of memory allocations required.

The **Async Upload Buffer** determines the size of this ring buffer. It has a minimum size of 2 megabytes, and a maximum size of 2047 megabytes.

Unity automatically resizes the buffer to fit the largest texture or mesh that is currently loading. This can be a slow operation, especially if Unity has to perform it more than once; for example, if you are loading many textures that are larger than the default buffer size. To reduce the number of times that Unity must resize the buffer, set this value to fit the largest value that you expect to load. This is usually the largest texture in the **Scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene).

You can configure this value in the Quality settings window, or using the [QualitySettings.asyncUploadBufferSize](../ScriptReference/QualitySettings-asyncUploadBufferSize.html) API.

### Configure the CPU’s upload time

To control the amount of time the CPU spends uploading texture or mesh data to the GPU, use **Async Upload Time Slice**. The value is in milliseconds per frame.

A larger value means the data will be ready on the GPU sooner, but the CPU will spend more time on upload operations during those frames. Note that Unity only uses this time for uploading if there is data waiting in the buffer to be uploaded to the GPU; if there is no data waiting, Unity can use this time for other operations.

You can configure this value in the Quality settings window, or using the [QualitySettings.asyncUploadTimeSlice](../ScriptReference/QualitySettings-asyncUploadTimeSlice.html) API.

Check whether a mesh uses the asynchronous upload pipeline

Graphics performance and profiling in URP

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)