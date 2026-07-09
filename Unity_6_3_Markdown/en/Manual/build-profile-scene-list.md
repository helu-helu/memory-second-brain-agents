* [Building and publishing](building-and-publishing.html)
* [Create a build from the Editor](BuildSettings.html)
* Manage scenes in a build

Create and manage build profiles

Customize settings with build profiles

# Manage scenes in a build

Use the ****Scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) List** to organize the scenes in a build. Unity builds scenes in the order they appear in the list. You can add, exclude, remove, and reorder scenes in the list.

On platform profiles, the **Scene List** is visible by default. However, on build profiles the **Scene List** isn’t visible by default, because the build profiles do not override the scene list unless you add it. When the **Scene List** is not added to a **build profile**A set of customizable configuration settings to use when creating a build for your target platform. [More info](build-profiles.html)  
See in [Glossary](Glossary.html#buildprofile), the global scene list is used instead.

To access the **Scene List** for a build profile, follow these steps:

1. Go to **File** > **Build Profiles**.
2. Select or [create a build profile](create-build-profile.html) for your target platform.
3. Select **Add Settings**.
4. From the dropdown, select **Scene List**.

The **Scene List** section appears displaying the scenes in your project. Use the following actions to manage the scene list:

| **List action** | **Description** |
| --- | --- |
| **Add** | Use **Add Open Scenes** to add all currently open scenes to the list. You can also drag scenes from the **Project** window into the list. |
| **Exclude** | Clear the checkbox next to a scene to exclude it from the build. This removes the scene from the build but not from the list. |
| **Remove** | Right-click on a scene name and select **Remove Selection** to remove it from the list. |
| **Reorder** | To adjust the scene order, drag scenes into a different position in the list. |

## Additional resources

* [Build Profiles window reference](build-profiles-reference.html)
* [Working with scenes](working-with-scenes.html)

Create and manage build profiles

Customize settings with build profiles

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)