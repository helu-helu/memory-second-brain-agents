* [Building and publishing](building-and-publishing.html)
* Create a clean build

Platform Browser window reference

Create a scripts-only build

# Create a clean build

By default, Unity creates builds incrementally, however the incremental pipeline can cause caching issues, or incomplete builds. For example, Unity [serializes](script-serialization.html) **scenes**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) and assets for the target platform during the build process, and either reuses all content from the previous build, or rebuilds everything. However, this detection might fail when global settings affect build output. You can create a clean build to resolve this issue.

When Unity creates a clean build, it discards some cached build data but reuses previously imported assets and cached **shaders**A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#shader) to rebuild all content and code. Use a clean build when preparing release builds or troubleshooting issues caused by corrupted or outdated build caches.

To create a clean build:

1. Open the **Build Profiles** window (**File** > **Build Profiles**).
2. Next to the **Build** button, select the drop-down.
3. Select **Clean Build**.

You can also create a clean build from a [build script](build-script-build.html) by passing [`BuildOptions.CleanBuildCache`](../ScriptReference/BuildOptions.CleanBuildCache.html) in the call to [`BuildPipeline.BuildPlayer`](../ScriptReference/BuildPipeline.BuildPlayer.html).

If you don’t want Unity to reuse imported assets and cached shaders, you can delete the `Library` folder to force Unity to repeat all imports and shader compilation. This approach increases build time but helps avoid issues that might occur at earlier stages of the build process.

To create a clean build without using cached shaders and assets:

1. Close the Editor.
2. Delete the `Library` folder
3. Use the previous instructions to create a clean build.

## Additional resources

* [Create a build from the Editor](BuildSettings.html)
* [Content output of a build](build-content-output.html)

Platform Browser window reference

Create a scripts-only build

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)