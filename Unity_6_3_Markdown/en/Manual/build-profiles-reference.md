* [Building and publishing](building-and-publishing.html)
* [Create a build from the Editor](BuildSettings.html)
* Build Profiles window reference

Customize settings with build profiles

Platform Browser window reference

# Build Profiles window reference

Configure build settings for the target platforms and override specific **project settings**A broad collection of settings which allow you to configure how Physics, Audio, Networking, Graphics, Input and many other areas of your project behave. [More info](comp-ManagerGroup.html)  
See in [Glossary](Glossary.html#ProjectSettings) for a **build profile**A set of customizable configuration settings to use when creating a build for your target platform. [More info](build-profiles.html)  
See in [Glossary](Glossary.html#buildprofile).

**Note**: Access the **Build Profiles** window in the Unity Editor from **File** > **Build Profiles**.

The following sections describe the settings available in the **Build Profiles** window.

* [Asset Import Overrides](#AssetImportOverride)
* [Platform Settings](#platform-settings)
* [Diagnostics](#diagnostics)
* [Add Settings](#add-settings)
* [Build options](#build-options)

## Asset Import Overrides

To speed up the time it takes to import assets and change platforms, you can locally override all texture import settings. During development, asset overrides can be useful to speed up iteration time by using lower quality assets.

**Note**: To set asset import overrides for initial project imports, use the Editor [command line arguments](CommandLineArguments.html) `-overrideMaxTextureSize` and `-overrideTextureCompression`.

| **Property** | **Description** |
| --- | --- |
| **Max Texture Size** | Override the maximum imported texture size. Unity imports textures in the lower of two values: this value, or the Max Size value specified in [Texture import settings](class-TextureImporter.html). The time it takes to import a texture is proportional to the number of pixels it contains, so a texture size with a lower maximum can speed up import times. It’s recommended to use this setting only during development as the resulting textures are lower in resolution. |
| **Texture Compression** | Override the texture compression options set in [Texture import settings](class-TextureImporter.html).  **Note**: The following texture compression options only apply to textures referenced in [GPU texture formats reference](texture-formats-reference.html).    * **Force Fast Compressor**:Use a faster but lower quality texture compression mode for formats that support it (BC7, BC6H, ASTC, ETC, ETC2). Usually this results in more compression artifacts, but for many formats the compression itself is 2 to 20 times faster. This setting also disables **Crunch** texture compression format on any textures that have it. The effect of this setting is the same as if all textures had their **Compressor Quality** set to a low number in the platforms section of their [Texture import settings](class-TextureImporter.html). * **Force Uncompressed**: Use uncompressed formats. This is faster to import (because it skips the texture compression process), but the resulting textures take up more memory and game data size, and can impact rendering performance. The effect of this setting is the same as if all textures had their **Compression** set to **None** in their platforms’ [Texture import settings](class-TextureImporter.html). * **Force No Crunch**: Disable Crunch compression for all textures. Crunch compression can take a long time, so disabling it can speed up the import process significantly. However, the resulting textures take up more disk space. Selecting this option is the same as disabling **Use Crunch Compression** in the [Texture import settings](class-TextureImporter.html) for all textures. |

## Platform Settings

Each platform has specific build settings. For more information, refer to the following platform-specific documentation:

| **Platform** | **Documentation** |
| --- | --- |
| **Android** | [Android build settings reference](android-build-settings.html) |
| **iOS and tvOS** | [iOS build settings reference](BuildSettingsiOS.html) |
| **Embedded Linux** | [Embedded Linux build settings reference](embedded-linux-build-settings.html) |
| **Linux** | [Linux build settings reference](Buildsettings-linux.html) |
| **macOS** | [macOS build settings reference](macosbuildsettings.html) |
| **QNX** | [QNX build settings reference](qnx-build-settings.html) |
| **Universal Windows Platform** | [UWP build settings reference](windowsstore-buildsettings.html) |
| **Web and Facebook Instant Games** | [Web build settings](web-build-settings.html) |
| **Windows** | [Windows build settings reference](WindowsStandaloneBinaries.html) |

**Note**: For information on build settings for closed platforms, refer to the included documentation in the Unity installer of each **closed platform**Includes platforms that require confidentiality and legal agreements with the platform provider for using their developer tools and hardware. These platforms aren’t open to development unless you have an established relationship with the provider. For example PlayStation®, Game Core for Xbox®, and Nintendo®.  
See in [Glossary](Glossary.html#closedplatform).

### Shared build settings

The following build settings are available for all profile types. The values of these settings are shared across platform profiles but not across build profiles.

**Note**: Updating shared settings of an active platform profile using [`EditorUserBuildSettings`](../ScriptReference/EditorUserBuildSettings.html) applies changes across all platform profiles. However, updating shared settings of an active build profile with [`EditorUserBuildSettings`](../ScriptReference/EditorUserBuildSettings.html) only updates that specific build profile.

| **Property** | **Description** |
| --- | --- |
| **Development Build** | Include scripting debug symbols and the [Profiler](Profiler.html)A window that helps you to optimize your game. It shows how much time is spent in the various areas of your game. For example, it can report the percentage of time spent rendering, animating, or in your game logic. [More info](Profiler.html) See in [Glossary](Glossary.html#Profiler) in your build. Use this setting when you want to test your application. When you select this option, Unity sets the `DEVELOPMENT_BUILD` scripting define symbol. Your build then includes preprocessor directives that set `DEVELOPMENT_BUILD` as a condition.  For more information, refer to [Platform dependent compilation](platform-dependent-compilation.html). |
| **Autoconnect Profiler** | Automatically connect the Unity Profiler to your build. For more information, refer to [Profiler](Profiler.html).  **Note**: This option is available only if you select **Development Build**. |
| **Deep Profiling** | Allow the Profiler to process all your script code and record every function call, returning detailed profiling data. For more information, refer to [Deep Profiling](ProfilerWindow.html#deep-profiling).   This property is available only if you enable **Development Build**.   **Note**: Enabling **Deep Profiling** might slow down script execution. |
| **Script Debugging** | Attach script debuggers to the Player remotely.   This property is available only if you enable **Development Build**. |
| **Wait for Managed Debugger** | Make the Player wait for a debugger to be attached before it executes any script code.  This property is visible only if you enable **Script Debugging**. |
| **Compression Method** | Specifies the method Unity uses to compress the data in your Project when it builds the Player. This includes [Assets](assets-supported-types.html)Any media or data that can be used in your game or project. An asset may come from a file created outside of Unity, such as a 3D Model, an audio file or an image. You can also create some asset types in Unity, such as an Animator Controller, an Audio Mixer or a Render Texture. [More info](AssetWorkflow.html) See in [Glossary](Glossary.html#asset), [Scenes](CreatingScenes.html)A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html) See in [Glossary](Glossary.html#Scene), [Player settings](class-PlayerSettings.html)Settings that let you set various player-specific options for the final game built by Unity. [More info](class-PlayerSettings.html) See in [Glossary](Glossary.html#PlayerSettings), and [GI data](GICache.html).  * **Default**: On Windows, Mac, Linux Standalone, and iOS, there’s no default compression. On Android, the default compression is ZIP, which gives slightly better compression results than LZ4HC. However, ZIP data is slower to decompress. * **LZ4**: A fast compression format that is useful for development builds. For more information, refer to [BuildOptions.CompressWithLz4](../ScriptReference/BuildOptions.CompressWithLz4.html). * **LZ4HC**: A high compression variant of LZ4 that is slower to build but produces better results for release builds. For more information, refer to [BuildOptions.CompressWithLz4HC](../ScriptReference/BuildOptions.CompressWithLz4HC.html). |

## Diagnostics

**Note**: The **Diagnostics** section is visible only when using a build profile on Android, iOS, macOS, and Windows platforms. This section is visible by default on these platforms and isn’t added through [Add Settings](#add-settings).

| **Property** | **Description** |
| --- | --- |
| **Diagnostic Data** | Configure settings to collect diagnostic data for each build profile in your project. Use these settings to override the default setting specified in **Project Settings** > **Services** > **Diagnostics** > **Diagnostic Data** per build profile. For more information on diagnostic data, refer to [Developer Data framework](https://docs.unity.com/en-us/cloud/developer-data/).  The following options are available:  * **Disabled**: Disables collection of diagnostic data for the build. **Note**: **Diagnostic Data** is set to **Disabled** if your project isn’t connected to [Unity Cloud](https://docs.unity.com/en-us/cloud). To collect diagnostic data, you must link your project to Unity Cloud via **Project Settings**. For more information, refer to [Configure a project for Unity Cloud](https://docs.unity.com/cloud/en-us/projects/configure-project-for-unity-cloud). * **Use Project Settings > Diagnostics**: Uses the value specified in **Project Settings** > **Services** > **Diagnostics** > **Diagnostic Data**. All builds for your project use the value in this setting by default. * **Enabled**: Enables collection of diagnostic data for the build.  **Note**: Disabling Diagnostic Data collection can impact the performance and behavior of services that rely on Developer Data. |

## Add Settings

Use the **Add Settings** button to add optional settings to a build profile. You should only add the settings you want to customize. The settings you add appear in a section with a foldout, where you can customize them for the build profile.

**Note**: The **Add Settings** button is available only for build profiles and not for platform profiles. This button is disabled when you add all available settings to the build profile.

The following settings are available for customization through **Add Settings**. Additional settings might be available based on the packages installed in your project.

| **Setting** | **Description** |
| --- | --- |
| **Scene List** | Create a custom scene list for your build profile. When you add **Scene List**, scenes are automatically inherited from the global scene list. For more information on managing scenes, refer to [Manage scenes in a build](build-profile-scene-list.html).   **Note**: For platform profiles, **Scene List** is visible by default. |
| **Scripting Defines** | Add custom scripting defines for your build profile. These custom scripting defines are additive and don’t override other scripting defines in your project. For more information, refer to [Custom scripting symbols](custom-scripting-symbols.html). |
| **Player Settings** | Create custom [Player](class-PlayerSettings.html) settings for your build profile. The Player settings inherit their initial values from the global Player settings for the build profile’s target platform. To access the global Player settings, use the link in the **Build Profiles** toolbar or navigate to **Edit** > **Project Settings** > **Player**.   **Note**: For an active build profile, the Player Settings overrides are linked to the [Player settings APIs](../ScriptReference/PlayerSettings.html). If you use the Player Settings APIs to modify a Player setting for an active build profile, the change will update the corresponding override value. |
| **Graphics Settings** | Create custom [Graphics](class-GraphicsSettings.html) settings for your build profile. The Graphics settings inherit their initial values from the global settings in **Edit** > **Project Settings** > **Graphics**. |
| **Quality Settings** | Create custom [Quality](class-QualitySettings.html) levels for your build profile. The Quality settings inherit their initial values from the global settings in **Edit** > **Project Settings** > **Quality**. For more information, refer to [Customize settings with build profiles](build-profiles-override-settings.html#override-quality). |
| **Adaptive Performance Settings** | Create custom [Adaptive Performance](adaptive-performance/provider-settings-reference.html) settings for your build profile. These settings inherit their initial values from the global settings in **Edit** > **Project Settings** > **Adaptive Performance**. |

## Build options

To build your application, select one of the following options:

| **Property** | **Description** |
| --- | --- |
| **Cloud Build** | Use **Unity Build Automation** to build your project in the cloud. When selecting **Cloud Build** for the first time, a dialog appears prompting you to install the Build Automation package. Connect your Unity project to your Unity Build Automation project using **Edit** > **Project Settings** > **Services**. Once connected, use the **Build Automation Settings** section in your build profile to configure your cloud build. For more information, refer to [Build Automation Overview](https://docs.unity.com/ugs/en-us/manual/devops/manual/build-automation/overview).  **Note**: **Cloud Build** is visible only when using a build profile. |
| **Build** | Build the Player without launching it. The default build is incremental, except for the first build, which is always a full non-incremental clean build. This option runs a build without the [StrictMode](../ScriptReference/BuildOptions.StrictMode.html) option enabled. |
| **Clean build** | Create a clean, [non-incremental](build-clean-build.html) build. |
| **Force skip data build** | Skip the content step of the build process. This requires that you have already performed a successful build and that it is compatible with the current **scripts**A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](creating-scripts.html) See in [Glossary](Glossary.html#Scripts) in your project. For more information, refer to [Create a scripts-only build](build-scripts-only.html). |
| **Build and Run** | Build the Player and open it on your target platform. This option runs a build with the [StrictMode](../ScriptReference/BuildOptions.StrictMode.html) option enabled. Unity will do an incremental build when possible, otherwise it will perform a clean build. |

**Note**: The **Build** and **Build and Run** settings are visible only for the active profile.

## Additional resources

* [Create a build profile](create-build-profile.html)
* [Build Profiles scripting API reference](../ScriptReference/Build.Profile.BuildProfile.html)

Customize settings with build profiles

Platform Browser window reference

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)