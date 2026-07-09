* [Building and publishing](building-and-publishing.html)
* Introduction to building

Building and publishing

Content output of a build

# Introduction to building

When you create a build of your application, you create a Player. A Player is the platform-specific runtime application that Unity builds from your project. This is also known as a **project build**, which is the workflow of building a project from the Unity Editor into an application that runs on a target platform.

Building a Player for a target platform requires the platform-specific build support module for the target platform. You can add build support for a target platform when you [install Unity](GettingStartedInstallingUnity.html), or add it when you [create a Build Profile](create-build-profile.html).

Unity uses the **scenes**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) you define in the [Build Profiles](build-profiles.html)A set of customizable configuration settings to use when creating a build for your target platform. [More info](build-profiles.html)  
See in [Glossary](Glossary.html#buildprofile) window or the [`BuildPipeline`](../ScriptReference/BuildPipeline.html) API to create a build of a Player. For more information, refer to [Manage scenes in a build](build-profile-scene-list.html).

## Build modes

Unity has different build modes, as follows:

* **Release** build: Includes only what’s necessary to run the application. This is the default build type.
* **Development** build: Includes scripting debug symbols and the [Profiler](Profiler.html)A window that helps you to optimize your game. It shows how much time is spent in the various areas of your game. For example, it can report the percentage of time spent rendering, animating, or in your game logic. [More info](Profiler.html)  
  See in [Glossary](Glossary.html#Profiler). You can enable **development builds** in the [Build Profiles](build-profiles.html) window, which allows you to set further options such as [deep profiling support](profiler-deep-profiling.html) and script debugging. You can also use the [`BuildOptions.Development`](../ScriptReference/BuildOptions.Development.html) property to set a development build.

Both build modes provide options to build different variations of the Player application for different hardware architectures and [scripting backends](scripting-backends.html)A framework that powers scripting in Unity. Unity supports three different scripting backends depending on target platform: Mono, .NET and IL2CPP. Universal Windows Platform, however, supports only two: .NET and IL2CPP. [More info](scripting-backends.html)  
See in [Glossary](Glossary.html#ScriptingBackend). You can customize these variations through the [build settings](build-profiles-reference.html), [Player settings](class-PlayerSettings.html)Settings that let you set various player-specific options for the final game built by Unity. [More info](class-PlayerSettings.html)  
See in [Glossary](Glossary.html#PlayerSettings), or [command-line flags](EditorCommandLineArguments.html).

## Incremental build pipeline

Unity uses an incremental build pipeline that only rebuilds the parts of your application that have changed since the last build, which helps speed up development iteration time. This build process includes build steps such as content building, code compilation, data **compression**A method of storing data that reduces the amount of storage space it requires. See [Texture Compression](texture-choose-format-by-platform.html), [Animation Compression](class-AnimationClip.html#AssetProperties), [Audio Compression](class-AudioClip.html), [Build Compression](ReducingFilesize.html).  
See in [Glossary](Glossary.html#compression), and signing.

By default, Unity uses the incremental build pipeline for both [development and release builds](building-introduction.html). You can use the options in the **Build Profiles** window, or use the `BuildOptions.CleanBuildCache` API to create a non-incremental build, also known as a clean build. For more information, refer to [Creating clean builds](build-clean-build.html).

**Note:** [AssetBundles](AssetBundlesIntro.html) don’t use the incremental build pipeline and have separate mechanisms for caching and reusing the results from previous builds. For more information, refer to [Build assets into an AssetBundle](AssetBundles-Building.html).

## Additional resources

* [Build Profiles](build-profiles.html)
* [Create a Build Profile](create-build-profile.html)
* [Build Profiles window reference](build-profiles-reference.html)
* [Player settings](class-PlayerSettings.html)
* [Create a clean build](build-clean-build.html)

Building and publishing

Content output of a build

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)