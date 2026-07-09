* [Building and publishing](building-and-publishing.html)
* [Customize the build pipeline](build-customize-build-pipeline.html)
* Platform build path reference

Use build callbacks

Include additional files in a build

# Platform build path reference

When you build a Player from **scripts**A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts), or using [command-line arguments](CommandLineArguments.html), you must specify the path for the build location. For certain platforms, this path must also include the build file extension specific to the platform.

The following table lists the platforms that require you to include build file extensions:

| **Platform** | **Build file extension** |
| --- | --- |
| **Android** | * **Android Package**: `.apk` * **Android App Bundle**: `.aab`  **Note**: The file extension isn’t required for the following conditions:  * When building a Gradle project using [**Export Project** build setting](android-build-settings.html). * When building the Android App Bundle using [**Export for App Bundle** build setting](android-build-settings.html).  Instead, specify the folder name for the exported Gradle project or Android App Bundle in the build path. |
| **Windows (Standalone and Server)** | `.exe`  **Note**: The file extension isn’t required when generating a Visual Studio Solution using the [**Create Visual Studio Solution** build setting](WindowsStandaloneBinaries.html). Instead, specify the folder name for the generated Visual Studio Solution in the build path. |
| **macOS (Standalone)** | `.app`  **Note**: The file extension isn’t required when generating an Xcode project using the [**Create Xcode Project** build setting](macosbuildsettings.html). Instead, specify the folder name for the generated Xcode project in the build path. |
| **Linux (Standalone and Server)** | `.x86_64` |

## Additional resources

* [`BuildPipeline.BuildPlayer` API reference](../ScriptReference/BuildPipeline.BuildPlayer.html)
* [Command-line arguments](CommandLineArguments.html)

Use build callbacks

Include additional files in a build

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)