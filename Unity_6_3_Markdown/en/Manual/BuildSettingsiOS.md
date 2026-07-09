* [Platform development](PlatformSpecific.html)
* [iOS](iphone.html)
* [Building and delivering for iOS](ios-building-and-delivering.html)
* iOS build settings reference

Build an iOS application

App thinning

# iOS build settings reference

Use the iOS build settings to configure and build your application for iOS devices. The iOS build settings are part of the [Build Profiles](BuildSettings.html)A set of customizable configuration settings to use when creating a build for your target platform. [More info](build-profiles.html)  
See in [Glossary](Glossary.html#buildprofile) window.

| **Property** | **Description** |
| --- | --- |
| **Run in Xcode** | Select the Xcode version to open your project with. You can choose the **Latest version** or select a specific version from the drop-down list.  If you have a specific Xcode version installed on your machine that doesn’t appear in this list, select **Other** to find the version in the **Applications** window that appears. If Unity can’t find an Xcode installation on your computer, select the **Browse** button to locate the Xcode installation directory on your computer.   **Note**: This option is visible only when you run Unity on macOS. |
| **Run in Xcode as** | Select whether Xcode runs your Project as a **Release** or **Debug** build.  * **Release**: Builds an optimized version of your app. * **Debug**: Builds a testing version of your app that contains additional code that helps with debugging. |
| **Symlink Sources** | References Unity libraries instead of copying them into the Xcode project. This option reduces the Xcode project size and makes iteration times faster. |
| **Development Build** | Include scripting debug symbols and the [Profiler](Profiler.html)A window that helps you to optimize your game. It shows how much time is spent in the various areas of your game. For example, it can report the percentage of time spent rendering, animating, or in your game logic. [More info](Profiler.html) See in [Glossary](Glossary.html#Profiler) in your build. Use this setting when you want to test your application. When you select this option, Unity sets the `DEVELOPMENT_BUILD` scripting define symbol. Your build then includes preprocessor directives that set `DEVELOPMENT_BUILD` as a condition.  For more information, refer to [Platform dependent compilation](platform-dependent-compilation.html). |
| **Autoconnect Profiler** | Automatically connect the Unity Profiler to your build. For more information, refer to [Profiler](Profiler.html).  **Note**: This option is available only if you select **Development Build**. |
| **Deep Profiling** | Allow the Profiler to process all your script code and record every function call, returning detailed profiling data. For more information, refer to [Deep Profiling](ProfilerWindow.html#deep-profiling).   This property is available only if you enable **Development Build**.   **Note**: Enabling **Deep Profiling** might slow down script execution. |
| **Script Debugging** | Attach script debuggers to the Player remotely.   This property is available only if you enable **Development Build**. |
| **Wait for Managed Debugger** | Make the Player wait for a debugger to be attached before it executes any script code.  This property is visible only if you enable **Script Debugging**. |
| **Compression Method** | Specifies the method Unity uses to compress the data in your Project when it builds the Player. This includes [Assets](assets-supported-types.html)Any media or data that can be used in your game or project. An asset may come from a file created outside of Unity, such as a 3D Model, an audio file or an image. You can also create some asset types in Unity, such as an Animator Controller, an Audio Mixer or a Render Texture. [More info](AssetWorkflow.html) See in [Glossary](Glossary.html#asset), [Scenes](CreatingScenes.html)A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html) See in [Glossary](Glossary.html#Scene), [Player settings](class-PlayerSettings.html)Settings that let you set various player-specific options for the final game built by Unity. [More info](class-PlayerSettings.html) See in [Glossary](Glossary.html#PlayerSettings), and [GI data](GICache.html).  * **Default**: On Windows, Mac, Linux Standalone, and iOS, there’s no default compression. On Android, the default compression is ZIP, which gives slightly better compression results than LZ4HC. However, ZIP data is slower to decompress. * **LZ4**: A fast compression format that is useful for development builds. For more information, refer to [BuildOptions.CompressWithLz4](../ScriptReference/BuildOptions.CompressWithLz4.html). * **LZ4HC**: A high compression variant of LZ4 that is slower to build but produces better results for release builds. For more information, refer to [BuildOptions.CompressWithLz4HC](../ScriptReference/BuildOptions.CompressWithLz4HC.html). |

## Additional resources

* [Build profiles](BuildSettings.html)
* [Build an iOS application](iphone-BuildProcess.html)
* [BuildOptions Scripting API reference](../ScriptReference/BuildOptions.html)

Build an iOS application

App thinning

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)