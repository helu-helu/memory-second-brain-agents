* [Building and publishing](building-and-publishing.html)
* [Create a build from the Editor](BuildSettings.html)
* Introduction to build profiles

Create a build from the Editor

Create and manage build profiles

# Introduction to build profiles

A **build profile** is a set of configuration settings you can use to build your application on a particular platform. Use the **Build Profiles** window to create multiple build profiles for each platform you work on, saving different configurations for release and **development builds**A development build includes debug symbols and enables the Profiler. [More info](building-introduction.html)  
See in [Glossary](Glossary.html#developmentbuild). For more information on release and development builds, refer to [Introduction to building](building-introduction.html).

Navigate to **File** > **Build Profiles** to access the **Build Profiles** window.

## Profile types

There are two types of profiles available in the **Build Profiles** window.

### Platforms

The Platforms pane displays a list of currently installed platforms that Unity supports. A platform profile includes some [shared settings](build-profiles-reference.html#shared-build-settings) that apply to all platforms. For example, if you enable the **Development Build** setting for one platform profile, Unity will enable the setting across all the available platform profiles. Platforms also share the same **scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) data across each platform profile.

You can duplicate a platform, and create a new build profile. To do that, right click your selected platform and select **Copy to new profile**.

### Build Profiles

Unlike platforms, settings saved under build profiles aren’t shared across all the platforms. You can assign specific scenes to each build profile. Build profiles allow you to save multiple independent build configurations. You can save as many build profiles as you require using a custom name for each profile. Unity saves the build profile as an asset file that is ready for use with **version control**A system for managing file changes. You can use Unity in conjunction with most common version control tools, including Perforce, Git, Mercurial and Unity Version Control (UVCS). [More info](VersionControl.html)  
See in [Glossary](Glossary.html#versioncontrol).

![Build profiles stored as Assets in the Project window.](../uploads/Main/build-profiles-assets.png)


Build profiles stored as Assets in the Project window.

## Additional resources

* [Create a build profile](create-build-profile.html)
* [Build Profiles window reference](build-profiles-reference.html)
* [Build Profiles scripting API reference](../ScriptReference/Build.Profile.BuildProfile.html)

Create a build from the Editor

Create and manage build profiles

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)