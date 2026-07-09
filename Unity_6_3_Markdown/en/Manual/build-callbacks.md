* [Building and publishing](building-and-publishing.html)
* [Customize the build pipeline](build-customize-build-pipeline.html)
* Use build callbacks

Build a player from the command line

Platform build path reference

# Use build callbacks

You can implement build callbacks to insert custom behavior into the Player build process. Unity invokes these callbacks whether you trigger the Player build from the [Build Profiles](build-profiles.html)A set of customizable configuration settings to use when creating a build for your target platform. [More info](build-profiles.html)  
See in [Glossary](Glossary.html#buildprofile) window, from a custom menu, or from a [command line build](build-command-line.html). Build callbacks are useful when adding custom build behavior for a package used across different Unity projects.

## Supported callbacks

The following table lists the build callbacks that Unity supports:

| **Callback** | **Method** | **Description** |
| --- | --- | --- |
| [`BuildPlayerProcessor`](../ScriptReference/Build.BuildPlayerProcessor.html) | `PrepareForBuild` | Add files and perform custom setup before the build starts. |
| [`IPreprocessBuildWithContext`](../ScriptReference/Build.IPreprocessBuildWithContext.html) | `OnPreprocessBuild` | Called at the start of a build. |
| [`IPostprocessBuildWithContext`](../ScriptReference/Build.IPostprocessBuildWithContext.html) | `OnPostprocessBuild` | Called at the end of the build. |
| [`IFilterBuildAssemblies`](../ScriptReference/Build.IFilterBuildAssemblies.html) | `OnFilterAssemblies` | Remove assemblies from the build. |
| [`IPostBuildPlayerScriptDLLs`](../ScriptReference/Build.IPostBuildPlayerScriptDLLs.html) | `OnPostBuildPlayerScriptDLLs` | Read or patch managed assemblies after compilation. |
| [`IProcessSceneWithReport`](../ScriptReference/Build.IProcessSceneWithReport.html) | `OnProcessScene` | Called while Unity processes each **scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html) See in [Glossary](Glossary.html#Scene) for the build. |
| [`IPreprocessShaders`](../ScriptReference/Build.IPreprocessShaders.html) | `OnProcessShader` | Filter the list of **shader**A program that runs on the GPU. [More info](Shaders.html) See in [Glossary](Glossary.html#shader) variants to reduce shader build times. |
| [`IPreprocessComputeShaders`](../ScriptReference/Build.IPreprocessComputeShaders.html) | `OnProcessComputeShader` | Similar to `IPreprocessShaders` but intended for compute shaders. |
| [`IUnityLinkerProcessor`](../ScriptReference/Build.IUnityLinkerProcessor.html) | `GenerateAdditionalLinkXmlFile` | Configure the managed code stripping stage of a Player build. |
| [`IPostprocessLaunch`](../ScriptReference/Build.IPostprocessLaunch.html) | `OnPostprocessLaunch` | Called if the Player is launched as a final step of the build. |

Player builds support all these callbacks. Content-only builds, which don’t include managed assemblies, only invoke a subset: `IPreprocessBuildWithContext`, `IPostprocessBuildWithContext`, `IProcessSceneWithReport`, and `IPreprocessComputeShaders`.

## Callback ordering

You can use [`IOrderedCallback.callbackOrder`](../ScriptReference/Build.IOrderedCallback.callbackOrder.html) to control the execution order of a build callback relative to other implementations of the same callback interface. Unity sorts the callbacks from lowest to highest order value, and you can assign any negative or positive integer value. For example, if your implementation of `IPreprocessBuildWithContext` has an order value of 2, it runs after another `IPreprocessBuildWithContext` callback that has an order value of 1.

## Build callbacks during incremental builds

The following build callbacks happen during the content step of a Player build:

* **Scene callbacks**: [`IProcessSceneWithReport.OnProcessScene`](../ScriptReference/Build.IProcessSceneWithReport.OnProcessScene.html)
* **Shader callbacks**: [`IPreprocessShaders.OnProcessShader`](../ScriptReference/Build.IPreprocessShaders.OnProcessShader.html), [`IPreprocessComputeShaders.OnProcessComputeShader`](../ScriptReference/Build.IPreprocessComputeShaders.OnProcessComputeShader.html)

When Unity reuses content from a previous build, it doesn’t trigger these callbacks again because they already ran during the previous build. Unity caches any content change caused by the callback in the output from the previous build.

To ensure that Unity runs a modified callback implementation, perform a [clean build](build-clean-build.html), or modify the content of one of the scenes or assets in the build.

Other build callbacks that run before or after the content stage might trigger again during incremental builds. These callbacks must handle running multiple times on the same build output. For example, if a callback adds entries to an [Android app manifest](android-manifest.html), it must check if those entries already exist to avoid creating an invalid manifest file.

## Additional resources

* [Customize the build pipeline](BuildPlayerPipeline.html)
* [Create a custom build script](build-script-build.html)
* [Create a clean build](build-clean-build.html)

Build a player from the command line

Platform build path reference

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)