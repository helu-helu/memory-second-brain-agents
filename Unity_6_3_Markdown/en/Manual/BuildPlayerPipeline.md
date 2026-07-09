* [Building and publishing](building-and-publishing.html)
* [Customize the build pipeline](build-customize-build-pipeline.html)
* Introduction to customizing the build pipeline

Customize the build pipeline

Create a custom build script

# Introduction to customizing the build pipeline

A build pipeline is the automated processing and tooling that transforms your project from source assets and code into a Player for one or more target platforms. Unity includes a build pipeline for creating Player builds for many target platforms, and you can also create content-only builds, for example when using [Addressables](https://docs.unity3d.com/Packages/com.unity.addressables@latest).

You can automate and customize the behavior of the built-in build pipeline to meet the specific needs of your project and development workflow.

## Editor-based customizations

You can create Editor-based custom **scripts**A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts) and callbacks as follows:

* **[Custom build scripts](build-script-build.html)**: Use [`BuildPipeline.BuildPlayer`](../ScriptReference/BuildPipeline.BuildPlayer.html) to build a Player. These scripts can also include the following:
  + **Content-only build scripts**: Scripts that perform content-only builds, for example using [`BuildPipeline.BuildAssetBundles`](../ScriptReference/BuildPipeline.BuildAssetBundles.html).
  + **Combined build scripts**: Scripts that build one or more content-only builds and then build a Player build.
* **[Build callbacks](build-callbacks.html)**: Callbacks hook into a stage of a Player or content-only build to perform extra steps during a build.

These customizations can perform various tasks. For example, you can import external assets, validate a project’s configuration, or adjust **scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) content during builds. You can also analyze build results with the [`BuildReport`](../ScriptReference/Build.Reporting.BuildReport.html) API or upload builds to servers.

## External build pipeline customizations

You can use scripts or continuous integration (CI) tools that run on a build machine or cloud service (for example [Unity Build Automation](https://unity.com/solutions/ci-cd)A continuous integration service for Unity projects that automates the process of creating builds on Unity’s servers. [More info](https://docs.unity.com/devops/en/manual/unity-build-automation)  
See in [Glossary](Glossary.html#UnityBuildAutomation)) to customize the build pipeline. These tools perform one or more builds [from the command line](build-command-line.html).

External scripts can perform actions that don’t depend on the Unity API and can happen before or after the Unity Editor runs. These include pulling source control branches, synchronizing assets from content creation systems, processing build output with platform-specific tools, analyzing results with tools like [UnityDataTools](https://github.com/Unity-Technologies/UnityDataTools), and publishing builds with notifications.

## Build determinism

[Build determinism](build-deterministic-builds.html) is important if you want to be able to repeat a build process and get the same results. When designing your build pipeline customizations, make them work in a way that’s repeatable and always produces the same results when given the same inputs. For example, introducing timestamps or randomized data during a build callback breaks the ability to repeat the same build and get identical results. For more information, refer to [Introduction to deterministic builds](build-deterministic-builds-introduction.html).

## Additional resources

* [`BuildPipeline.BuildPlayer` API reference](../ScriptReference/BuildPipeline.BuildPlayer.html)
* [`BuildReport` API reference](../ScriptReference/Build.Reporting.BuildReport.html)
* [Build callbacks](build-callbacks.html)
* [Create a custom build script](build-script-build.html)
* [Build a player from the command line](build-command-line.html)
* [Content output of a build](build-content-output.html)

Customize the build pipeline

Create a custom build script

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)