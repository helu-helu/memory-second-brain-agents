* [Building and publishing](building-and-publishing.html)
* Create a scripts-only build

Create a clean build

Customize the build pipeline

# Create a scripts-only build

A scripts-only build is a build that reuses the content from the previous build, rather than rebuilding it.

When testing script changes it can be useful to force a scripts-only build to avoid the time taken to rebuild the content. This can be useful if you know that there are data changes, but want to quickly test a code change, without applying the pending data changes.

To create a scripts-only build, create a build with the **Force skip data build** option, as follows:

1. Open the [**Build Profiles**](build-profiles-reference.html) window (**File** > **Build Profiles**).
2. Next to the **Build** button, select the drop-down.
3. Select **Force skip data build**.

**Note:** The **Force skip data build** option doesn’t work if there have been any changes in the serialization layout of the **scripts**A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts) in the project. For example, when you add a new field to a MonoBehaviour then you must perform a regular or clean Player build to serialize the assets to match the new class definition.

You can also pass the [`BuildOptions.BuildScriptsOnly`](../ScriptReference/BuildOptions.BuildScriptsOnly.html) flag when calling `BuildPipeline.BuildPlayer` in custom build scripts.

The [incremental build pipeline](building-introduction.html#incremental-build-pipeline) automates scripts-only builds. On platforms that support it, Unity automatically reuses the content from the previous build, as long as the content hasn’t changed. In that case it’s not necessary to explicitly invoke a scripts-only build.

## Additional resources

* [Create a clean build](build-clean-build.html)
* [Create a build from the Editor](BuildSettings.html)
* [Content output of a build](build-content-output.html)

Create a clean build

Customize the build pipeline

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)