* Building and publishing

Profiling tools reference

Introduction to building

# Building and publishing

When you create a build of your application, you create a Player. A Player is the platform-specific runtime application that Unity builds from your project. You can control how Unity creates a build through Unity’s build and player settings.

| **Topic** | **Description** |
| --- | --- |
| **[Introduction to building](building-introduction.html)** | Understand the fundamentals of Unity’s build process, including build modes, incremental building, and platform compatibility. |
| **[Content output of a build](build-content-output.html)** | Information about the files that Unity creates when you make a build of your project. |
| **[Create a build from the Editor](BuildSettings.html)** | Use **build profiles**A set of customizable configuration settings to use when creating a build for your target platform. [More info](build-profiles.html) See in [Glossary](Glossary.html#buildprofile) to build your application for different platforms with unique build configurations. |
| **[Create a clean build](build-clean-build.html)** | Rebuild all content from scratch without using cached results to resolve build cache issues. |
| **[Create a scripts-only build](build-scripts-only.html)** | Build only the scripting assemblies without processing **scenes**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html) See in [Glossary](Glossary.html#Scene) and assets for faster iteration during development. |
| **[Customize the build pipeline](build-customize-build-pipeline.html)** | Create custom **scripts**A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](creating-scripts.html) See in [Glossary](Glossary.html#Scripts) and use callbacks to customize the build pipeline and run it from the command line. |
| **[Include additional files in a build](StreamingAssets.html)** | Use the StreamingAssets folder to include additional files in a build. |
| **[Reducing the file size of a build](ReducingFilesize.html)** | Tips to reduce the size of the build. |
| **[Deterministic builds](build-deterministic-builds.html)** | Create consistent, reproducible builds by controlling factors that can cause build variations. |
| **[Build cache location reference](build-cache-location-reference.html)** | Reference for where Unity stores build cache files on different operating systems. |

## Additional resources

* [`BuildPipeline` API reference](../ScriptReference/BuildPipeline.html)
* [`BuildReport` API reference](../ScriptReference/Build.Reporting.BuildReport.html)
* [Player settings](class-PlayerSettings.html)Settings that let you set various player-specific options for the final game built by Unity. [More info](class-PlayerSettings.html)  
  See in [Glossary](Glossary.html#PlayerSettings)
* [Platform-specific Player settings](PlatformSpecific.html)
* [Command line arguments](CommandLineArguments.html)
* [Managing assets at runtime](assets-managing-runtime.html)
* [Unity Build Automation](https://unity.com/solutions/ci-cd)A continuous integration service for Unity projects that automates the process of creating builds on Unity’s servers. [More info](https://docs.unity.com/devops/en/manual/unity-build-automation)  
  See in [Glossary](Glossary.html#UnityBuildAutomation)

Profiling tools reference

Introduction to building

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)