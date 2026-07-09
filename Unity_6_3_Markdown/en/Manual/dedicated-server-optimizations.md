* [Platform development](PlatformSpecific.html)
* [Dedicated Server](dedicated-server.html)
* [Get started with Dedicated Server](dedicated-server-get-started.html)
* Dedicated Server optimizations

Dedicated Server Player settings

Build your application for Dedicated Server

# Dedicated Server optimizations

Dedicated Server build target performs optimizations for networked applications. The build target applies some optimizations automatically by default, while others are optional because their impact depends on the game’s implementation.

## Automatic optimizations

By default, the Dedicated Server build target performs the following optimizations:

* [Deactivates the Audio Subsystem](#AudioSubsystem)
* [Removes lighting threads](#LightingThreads)
* [Removes some Player loop callbacks](#PlayerLoopCallbacks)
* [Removes GPU-only assets](#GpuOnlyAssets)

### Audio Subsystem

The Dedicated Server build target deactivates the [Audio](AudioOverview.html) [Subsystem](../ScriptReference/Subsystem.html) because builds don’t need audio support when running as a dedicated server. Disabling the Audio Subsystem reduces CPU load.

### Lighting threads

The Dedicated Server build target removes process threads related to lighting because there’s no need to render lighting on a server build.

### Player loop callbacks

The Dedicated Server build target disables the following [PlayerLoop callbacks](../ScriptReference/LowLevel.PlayerLoop.html) because they aren’t necessary for a server build.

* Player update loop registration of [`SendMouseEvents`](../ScriptReference/PlayerLoop.PreUpdate.SendMouseEvents.html)
* Player update loop registration of [`UpdateAllRenderers`](../ScriptReference/PlayerLoop.PostLateUpdate.UpdateAllRenderers.html)
* Player update loop registration of [`PlayerUpdateCanvases`](../ScriptReference/PlayerLoop.PostLateUpdate.PlayerUpdateCanvases.html)
* Player update loop registration of all audio callbacks such as [`UpdateAudio`](../ScriptReference/PlayerLoop.PostLateUpdate.UpdateAudio.html)
* Player update loop registration of all UI callbacks such as [`UIElementsUpdatePanels`](../ScriptReference/PlayerLoop.PreLateUpdate.UIElementsUpdatePanels.html)
* Player update loop registration of all input callbacks such as [`UpdateInputManager`](../ScriptReference/PlayerLoop.EarlyUpdate.UpdateInputManager.html)

### GPU-only assets

The Dedicated Server build target removes GPU-only assets such as texture **pixel**The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](ShadowPerformance.html)  
See in [Glossary](Glossary.html#pixel) data for textures and **mesh**The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](mesh.html)  
See in [Glossary](Glossary.html#Mesh) vertex data, that the server doesn’t need. The build target preserves assets with CPU Read/Write access and assets in the [Resource Folders](LoadingResourcesatRuntime.html).

Textures and meshes imported with CPU Read/Write access disabled are only accessible by the GPU, whereas the CPU can’t access them. Because the Dedicated Server build target doesn’t initialize a graphics device, there’s no need to include this data. Excluding this data reduces the memory usage of the executable.

Refer to the following lists to learn more about which assets the Dedicated Server build target removes and preserves.

**Removed**:

* Textures with CPU Read/Write access disabled.
* Vertex data for meshes with CPU Read/Write access disabled.

**Preserved**:

* Textures with CPU Read/Write access enabled.
* Vertex data for meshes with CPU Read/Write access enabled.
* Assets in the protected [Resource Folders](LoadingResourcesatRuntime.html).
* Texture [metadata](AssetMetadata.html) (such as the texture size value).
* Mesh data that internal systems that run on the CPU require (such as [physics](PhysicsSection.html)), even if CPU Read/Write is disabled.

**Note**: To learn more about CPU Read/Write access, refer to [Texture.isReadable](../ScriptReference/Texture-isReadable.html) and [Mesh.isReadable](../ScriptReference/Mesh-isReadable.html).

## Additional optimizations

You also have an option to apply additional optimizations through [Enable Dedicated Server Optimizations](dedicated-server-player-settings.html#Optimization) property in the **Player Settings**Settings that let you set various player-specific options for the final game built by Unity. [More info](class-PlayerSettings.html)  
See in [Glossary](Glossary.html#PlayerSettings) window. These optimizations remove assets such as ****Shaders**A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#shader)** and **Fonts**. However, applying these optimizations might cause issues if the removed assets are referenced in the game’s implementation.

**Assets removed**:

* Shaders
* Fonts

In addition to the automatic optimizations applied through the Dedicated Server build target, you can apply the following implementation-specific optimizations manually.

* Use [conditional compilation](platform-dependent-compilation.html) to selectively include and exclude code depending on the build target.
* Separate player-specific and server-specific code through class implementations.
* Remove additional items from the PlayerLoop in server builds. Refer to [PlayerLoop](../ScriptReference/LowLevel.PlayerLoop.html) and [PlayerLoopSystem](../ScriptReference/LowLevel.PlayerLoopSystem.html).

## Known limitations

Dedicated server optimizations don’t apply to content built with the Scriptable Build Pipeline (SBP). Systems that rely on SBP, such as the Addressables system and Entities subscenes, don’t benefit from these optimizations.

## Additional resources

* [Optimization section](analysis.html)
* [Optimizations tips for Unity UI](https://unity.com/how-to/unity-ui-optimization-tips)
* [Best practices for performance optimization in Unity](https://unity.com/how-to/advanced-programming-and-code-architecture)

Dedicated Server Player settings

Build your application for Dedicated Server

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)