* [Unity Editor interface](unity-editor.html)
* [Unity Editor settings reference](editor-settings-reference.html)
* [Project Settings reference](comp-ManagerGroup.html)
* Editor

Audio

2D and 3D mode settings

# Editor

Use the **Editor** settings to apply global settings for working in the Unity Editor. To access the Editor settings, go to **Edit** > **Project Settings** then select the **Editor** category.

## Unity Remote

Unity Remote is deprecated. For most use cases, [Device Simulator package](https://docs.unity3d.com/Packages/com.unity.device-simulator@latest) replaces Unity Remote.

| **Property** | **Description** |
| --- | --- |
| **Device** | Choose the device type you want to use for Unity Remote testing.  [Unity Remote](UnityRemote5.html)A downloadable app designed to help with Android, iOS and tvOS development. The app connects with Unity while you are running your project in Play Mode from the Unity Editor. [More info](UnityRemote5.html) See in [Glossary](Glossary.html#UnityRemote) is a downloadable app designed to help with Android, iOS and tvOS development. |
| **Compression** | Choose the type of image compression to use when transmitting the game screen to the device via Unity Remote. Choose from the following options:  * **JPEG**: Usually gives higher compression and performance, but the graphics quality is a little lower. This is the default option. * **PNG**: Gives a more accurate representation of the game display, but can result in lower performance. |
| **Resolution** | Choose the resolution the game runs at on Unity Remote:  * **Downsize**: Display the game at a lower resolution. This results in better performance, but lower graphical accuracy. This is the default option. * **Normal**: Display the game at normal resolution. This results in better graphical accuracy, but lower performance. |
| **Joystick Source** | Choose the connection source for the joysticks you’re using:  * **Remote**: Use joysticks that connect to a device running Unity Remote. This is the default option. * **Local**: Use joysticks that connect to the computer running the Editor. |

## Asset Serialization

| **Property** | **Description** |
| --- | --- |
| **Mode** | Choose which format to use for storing serialized Assets. This is set to **Force Text** by default.  Unity uses [serialization](script-serialization.html) to load and save assets and AssetBundles to and from your computer’s hard drive. To help with version control merges, Unity can store scene files in a [text-based format](TextSceneFormat.html). If you aren’t merging scenes, Unity can store scenes in a more space-efficient binary format, or allow both text and binary scene files to exist at the same time. Choose from the following formats:  * **Mixed**: Assets in Binary mode remain in Binary mode, and Assets in Text mode remain in Text mode. Unity uses Binary mode by default for new assets. * **Force Binary**: Convert all assets to Binary mode, including new assets. * **Force Text**: Convert all assets to Text mode, including new assets. This is the default option. |
| **Reduce **version control**A system for managing file changes. You can use Unity in conjunction with most common version control tools, including Perforce, Git, Mercurial and Unity Version Control (UVCS). [More info](VersionControl.html) See in [Glossary](Glossary.html#versioncontrol) noise** | Forces the Editor to write references and similar YAML structures on one line, which reduces version control noise. When Unity reaches a line length of 80 characters it attempts to split the YAML data over multiple lines. |

## Scene Handling

| **Property** | **Description** |
| --- | --- |
| **Force GC on Scene Loads** | Force a managed heap garbage collection and unload unused assets after loading each scene in the Editor in single mode or exiting [prefab editing mode](EditingInPrefabMode.html). In complex projects, this can slow down performance. Disable this if you do not require class finalizers to run at the end of scene loading. Note that regular dynamic GC and unused asset unloading still occur when memory usage is high, but without this option, class finalizers might not run immediately after each scene load. |

## Default Behavior Mode

| **Property** | **Description** |
| --- | --- |
| **Mode** | Choose the default [2D or 3D development](2DAnd3DModeSettings.html) mode. Unity sets up the certain default behaviors according to the mode you choose to make development easier:  * **3D**: Set Unity up for 3D development. This is the default option. * **2D**: Set Unity up for 2D development. |

## Asset Pipeline

| **Property** | **Description** |
| --- | --- |
| **Remove unused Artifacts on Restart** | Enable to remove unused artifact files in the Library folder and remove their entries in the Asset Database. This setting is a form of garbage collection. Use this setting to disable the Asset Database garbage collection, so that previous artifact revisions which are no longer used are still preserved after you restart the Editor. This is useful if you need to debug unexpected import results. To learn more, refer to [Import Activity window](ImportActivityWindow.html). |
| **Parallel Import** | Use multiple processes to import assets simultaneously. By default, Unity imports assets one after another sequentially on the main Editor process. Parallel importing can be faster than the default sequential method of importing. To learn more, refer to [Importing assets simultaneously](ParallelImport.html) |
| **Desired worker count** | Set the number of import worker processes that the import pipeline considers the optimal number to run in parallel. |
| **Standby Import Worker Count** | Set the minimum number of worker processes to keep, even if they’re idle. If there are more worker processes than this, Unity shuts down import workers that have been idle for some time, to free up system resources. This property allows you to manage how Unity balances system resources when some processes are idle, compared with the time it takes to start up new import worker processes. You might see an improvement in import performance by increasing this value if you are frequently iterating on model, animation or texture work, and are therefore frequently importing batches of models or image files. |
| **Idle Import Worker Shutdown Delay** | Set the amount of time in seconds to wait before shutting down an idle worker. |
| **Exactly Match Referenced Clip Names** | Controls how referenced clips are matched with models animated in Legacy mode. When enabled, model names and referenced clip names must exactly match. When disabled, only the start of the model name must match the referenced clip name. |

## Cache Server (project specific)

Contains settings for [Unity Accelerator](UnityAccelerator.html).

| **Setting** | **Description** |
| --- | --- |
| **Mode** | Choose whether to use the cache server. Choose from the following options:  * **Use global settings:** Uses the settings in the **Preferences** window (**Settings > Asset Pipeline > Unity Accelerator**). * **Enabled**: Enable the cache server. * **Disabled:** Disable the cache server. |
| **IP Address** | Input the **accelerator**The Unity Accelerator is an external tool that provides an asset cache that keeps copies of a team’s imported assets. The goal of the Accelerator is to speed up teamwork and reduce iteration time by coordinating asset sharing so that you don’t need to reimport portions of your project. [More info](UnityAccelerator.html) See in [Glossary](Glossary.html#Accelerator)’s IP address and port. |
| **Check Connection** | Select **Check Connection** to test the connectivity of the accelerator. |
| **Namespace prefix** | Set a custom namespace for the server. |
| **Download** | Enable downloads from the cache server. |
| **Upload** | Enable uploads from the cache server. |
| **TLS/SSL** | Enable encryption on the cache server. |
| **Authentication (Using Unity ID)** | Enable authentication for the cache server using Unity ID. |
| **Content Validation** | Select the level of content validation: Disabled, Upload Only, Enabled, Required. |
| **Download Batch Size** | Set the size of download. |

## Prefab Mode

Contains settings related to [prefab editing mode](EditingInPrefabMode.html).

| **Property** | **Description** |
| --- | --- |
| **Allow Auto Save** | Enable an **Auto Save** toggle in [prefab editing mode](EditingInPrefabMode.html). When **Allow Auto Save** is disabled, any edits you make aren’t automatically saved and the toggle doesn’t display. For more information, refer to [Automatically save edits to the prefab asset](EditingInPrefabMode.html#automatically-save-edits-to-the-prefab-asset). |
| **Regular Environment** | Assign a scene as an editing environment in **prefab**An asset type that allows you to store a GameObject complete with components and properties. The prefab acts as a template from which you can create new object instances in the scene. [More info](Prefabs.html) See in [Glossary](Glossary.html#prefab) editing mode for regular prefabs (those with a regular [Transform](class-Transform.html) component). This allows you to edit a prefab against a backdrop of your choosing rather than an empty scene. For more information, refer to [Editing prefab assets](EditingInPrefabMode.html). |
| **UI Environment** | Assign a scene as an editing environment in prefab editing mode for UI prefabs (those with a [Rect Transform](https://docs.unity3d.com/Packages/com.unity.ugui@2.0/manual/class-RectTransform.html) component). This allows you to edit a prefab against a backdrop of your choosing rather than an empty scene. For more information, refer to [Editing prefab assets](EditingInPrefabMode.html). |

## Graphics

| **Property** | **Description** |
| --- | --- |
| **Use legacy **Light Probe**Light probes store information about how light passes through space in your scene. A collection of light probes arranged within a given space can improve lighting on moving objects and static LOD scenery within that space. [More info](LightProbes.html) See in [Glossary](Glossary.html#LightProbe) sample counts** | Use fixed Light Probe sample counts for baking with the Progressive **Lightmapper**A tool in Unity that bakes lightmaps according to the arrangement of lights and geometry in your scene. [More info](Lightmapping.html) See in [Glossary](Glossary.html#Lightmapper). The sample counts are: 64 direct samples, 2048 indirect samples, and 2048 environment samples. |

## Sprite Atlas

| **Property** | **Description** |
| --- | --- |
| **Mode** | Choose a mode to configure the [Sprite Atlas](sprite/atlas/atlas-landing.html)**Graphics:** A utility that packs several sprite textures tightly together within a single texture known as an atlas. [More info](sprite/atlas/v2/v2-landing). **2D:** A texture that is composed of several smaller textures. Also referred to as a texture atlas, image sprite, sprite sheet or packed texture. [More info](sprite/atlas/atlas-landing.html). See in [Glossary](Glossary.html#SpriteAtlas) tool:  * **Disabled**: Do not pack Sprite Atlases. This is the default setting. * **Sprite Atlas V1 - Enabled For Builds**: Pack Sprite Atlases for builds only. * **Sprite Atlas V1 - Always Enabled**: Pack Sprite Atlases for builds and before entering Play mode. * **Sprite Atlas V2 - Enabled**: Pack Sprite Atlases for both builds and before entering Play mode. * **Sprite Atlas V2 - Enabled For Builds**: Pack Sprite Atlases for builds only. |

## C# Project Generation

| **Property** | **Description** |
| --- | --- |
| **Additional extensions to include** | Include a list of additional file types to add to the C# project. Separate each file type with a semicolon. By default, this field contains `txt;xml;fnt;cd;asmdef;rsp;asmref`. |
| **Root namespace** | Fill in the namespace to use for the C# project `RootNamespace` property. Refer to [Common MSBuild Project Properties](https://docs.microsoft.com/en-us/visualstudio/msbuild/common-msbuild-project-properties?view=vs-2022) for more information. This field is blank by default. |

## Texture Compressors

| **Property** | **Description** |
| --- | --- |
| **BC7 Compressor** | Select the compressor to use for BC7 format texture **compression**A method of storing data that reduces the amount of storage space it requires. See [Texture Compression](texture-choose-format-by-platform.html), [Animation Compression](class-AnimationClip.html#AssetProperties), [Audio Compression](class-AudioClip.html), [Build Compression](ReducingFilesize.html). See in [Glossary](Glossary.html#compression). |
| **ETC Compressor** | Select the compressors to use for different compression qualities of ETC Textures. The compression tools available are [etcpak](https://bitbucket.org/wolfpld/etcpak/wiki/Home), [ETCPACK](https://github.com/Ericsson/ETCPACK) and [Etc2Comp](https://github.com/google/etc2comp). These are all third-party compressor libraries. Choose from the following:  * **Default**: Use the default configuration for Unity. This sets the following properties: **Fast**: etcpack, **Normal**: ETCPACK Fast, **Best**: Etc2Comp Best. * **Custom**: Customize the ETC Texture compression configuration. When you choose this option, the **Fast**, **Normal**, and **Best** properties are enabled. This maps to the **Compressor Quality** setting in the [Texture Importer](class-TextureImporter.html) for the supported platforms. |
| **Fast** | Define the compression quality tool to use for Fast compression. This property is modifiable only when **ETC Compressor** is set to **Custom**. |
| **Normal** | Define the compression quality tool to use for Normal compression. This property is modifiable only when **ETC Compressor** is set to **Custom**. |
| **Best** | Define the compression quality tool to use for Best compression. This property is modifiable only when **ETC Compressor** is set to **Custom**. |

## Line Endings For New Scripts

| **Property** | **Description** |
| --- | --- |
| **Mode** | Choose the file line endings to apply to new scripts created within the Editor. Note that configuring these settings does not convert existing scripts. Choose from the following:  * **OS Native**: Apply line endings based on the operating system the Editor is running on. * **Unix**: Apply line endings based on the Unix operating system. * **Windows**: Apply line endings based on the Windows operating system. |

## Texture Streaming Settings

If you enable Mipmap Streaming in the Editor for one mode but not the other, entering and exiting Play mode takes slightly longer. Enabling Mipmap Streaming for both modes prevents Unity from unloading and reloading mipmap data, and increases the speed of entering and exiting Play Mode.

| **Property** | **Description** |
| --- | --- |
| **Enable Mipmap Streaming in Play Mode** | Enable [Mipmap Streaming](TextureStreaming.html) in Play mode.   The **Texture Mipmap Streaming** setting in the [Quality](class-QualitySettings.html) project settings must also be enabled.  Play mode might take longer to open and close if you enable this setting and disable **Enable Mipmap Streaming in Edit Mode**. |
| **Enable Mipmap Streaming in Edit Mode** | Enable Mipmap Streaming in Edit Mode.   The **Texture Mipmap Streaming** setting in the [Quality](class-QualitySettings.html) project settings must also be enabled.   Play mode might take longer to open and close if you enable this setting but disable **Enable Mipmap Streaming in Play Mode**. |
| **Load texture data on demand** | Load CPU-side texture data from disk asynchronously on demand to avoid some stalls and reduce CPU memory usage. If you enable mipmap streaming, this setting requires more processing time on the CPU, and might cause textures to temporarily appear at a lower resolution while Unity loads a higher resolution mipmap level from disk. |

## Shader Compilation

| **Property** | **Description** |
| --- | --- |
| **Asynchronous **Shader**A program that runs on the GPU. [More info](Shaders.html) See in [Glossary](Glossary.html#shader) Compilation** | Enable this checkbox to make Unity compile shaders in the background. While compiling, the Unity engine uses a placeholder Shader to render geometry in the Editor. When Shader compilation has finished, the engine swaps your Shader Variant back in. This means the Editor runs seamlessly, without having to wait for the Unity engine to compile every single Shader variant before rendering. For more information, refer to [Asynchronous Shader compilation](AsynchronousShaderCompilation.html). |

## Enter Play Mode Settings

| **Property** | **Description** |
| --- | --- |
| **When entering play mode** | Select which reload options to start when you enter Play mode. [Domain reloading](domain-reloading.html) is when the Editor resets the scripting state before it starts Play mode. [Scene reloading](scene-reloading.html) is when the Editor destroys all scene GameObjects and reloads the scene from disk before Play mode starts. To enter Play mode faster, you can disable [scene](scene-reloading.html)A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html) See in [Glossary](Glossary.html#Scene) or [domain](domain-reloading.html) reloads. To learn more, refer to [Details of disabling Domain and Scene Reload](configurable-enter-play-mode-details.html). Choose from the following options:  * **Reload Domain and Scene**: Reload both the [domain](domain-reloading.html) and [scene](scene-reloading.html) when you enter Play mode. **Reload Domain and Scene** is enabled by default. * **Reload Scene Only**: Reload the [scene](scene-reloading.html) and do not reload the [domain](domain-reloading.html) when you enter Play mode. * **Reload Domain Only**: Reload the [domain](domain-reloading.html) and do not reload the [scene](scene-reloading.html) when you enter Play mode. * **Do not reload Domain or Scene**: Do not reload either the [scene](scene-reloading.html) or [domain](domain-reloading.html) when you enter Play mode. |

## Numbering Scheme

| **Property** | **Description** |
| --- | --- |
| **Game Object Naming** | Naming scheme for duplicated **GameObjects**The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html) See in [Glossary](Glossary.html#GameObject). Duplicated or instantiated GameObjects are named by appending successive numbers to the original object name. |
| **Game Object Digits** | Sets the amount of digits to use for duplicated GameObject numbers. |
| **Space Before Number in Asset Names** | Controls whether to insert a space before a number in duplicated Asset names. |

## Inspector

| **Property** | **Description** |
| --- | --- |
| **Use IMGUI Default **Inspector**A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html) See in [Glossary](Glossary.html#Inspector)** | Revert to using IMGUI to generate Default Inspectors where no custom Inspector or Editor is defined. |

## Additional resources

* [Project Settings](comp-ManagerGroup.html)A broad collection of settings which allow you to configure how Physics, Audio, Networking, Graphics, Input and many other areas of your project behave. [More info](comp-ManagerGroup.html)  
  See in [Glossary](Glossary.html#ProjectSettings)
* [Unity Remote](UnityRemote5.html)
* [Script serialization](script-serialization.html)
* [2D and 3D mode settings](2DAnd3DModeSettings.html)
* [Importing assets simultaneously](ParallelImport.html)
* [Preferences](Preferences.html)
* [Transforms](class-Transform.html)
* [Cookies](Cookies.html)
* [Progressive Lightmapper](progressive-lightmapper.html)
* [The Mipmap Streaming system](TextureStreaming.html)
* [Asynchronous Shader compilation](AsynchronousShaderCompilation.html)
* [Sprite Atlas V2](sprite/atlas/v2/v2-landing)

EditorManager

Audio

2D and 3D mode settings

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)