* [Optimization](analysis.html)
* [Graphics performance and profiling](graphics-performance-profiling.html)
* [Compressing mesh data for optimization](compressing-mesh-data-optimization.html)
* Configure vertex compression

Types of mesh data compression

Configure mesh compression

# Configure vertex compression

To use the Vertex **Compression**A method of storing data that reduces the amount of storage space it requires. See [Texture Compression](texture-choose-format-by-platform.html), [Animation Compression](class-AnimationClip.html#AssetProperties), [Audio Compression](class-AudioClip.html), [Build Compression](ReducingFilesize.html).  
See in [Glossary](Glossary.html#compression) setting, you must first prepare the **mesh**The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](mesh.html)  
See in [Glossary](Glossary.html#Mesh), then apply compression in the project’s optimization settings.

### Prepare the mesh for vertex compression

The mesh must meet the following requirements to use vertex compression:

* The mesh must have its **Read/Write Enabled** property disabled. You can change this property in the Model tab of the Model Import Settings window.
* The mesh must not be a skinned mesh.
* The target platform must support FP16 values.
* The model that contains the mesh must have its **Mesh Compression** value set to “Off”.
* The mesh is not eligible for **dynamic batching**An automatic Unity process which attempts to render multiple meshes as if they were a single mesh for optimized graphics performance. The technique transforms all of the GameObject vertices on the CPU and groups many similar vertices together. [More info](DrawCallBatching.html)  
  See in [Glossary](Glossary.html#dynamicbatching) or dynamic batching is turned off in the **player settings**Settings that let you set various player-specific options for the final game built by Unity. [More info](class-PlayerSettings.html)  
  See in [Glossary](Glossary.html#PlayerSettings).

If a mesh fails to meet any of these requirements, then Unity does not apply vertex compression to that mesh and all data channels on the mesh use FP32 precision numbers.

### Configure Vertex Compression

To change the Vertex Compression settings:

1. Open the Player settings (menu: **Edit** > **Project Settings** > **Player**).
2. Open the **Other Settings** submenu and navigate to the **Optimization** heading.
3. Select the **Vertex Compression** dropdown and select any channel to enable or disable compression for that channel. You can also select **None** to disable compression for all channels, or select **Everything** to enable compression for all channels.

By default, Vertex Compression is set to **Mixed**, which Unity displays when multiple selections are active in the dropdown. By default, Unity uses Vertex Compression for the following channels:

* Normal
* Tangent
* Tex Coord 0
* Tex Coord 2
* Tex Coord 3

Unity compresses these channels by default because in most cases this combination of settings provides a good mixture of saved memory without significant changes to how the mesh looks. Unity doesn’t compress the other settings, Position and Tex Coord 1, by default because these are more likely to affect the appearance of the mesh, and do not offer significant reduction in memory use. If you intend to enable Vertex Compression for the Position and Tex Coord 1 channels, you should test the settings to ensure they don’t cause artifacts in your meshes.

Types of mesh data compression

Configure mesh compression

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)