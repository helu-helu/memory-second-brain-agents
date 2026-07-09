* [Building and publishing](building-and-publishing.html)
* [Create a build from the Editor](BuildSettings.html)
* Create and manage build profiles

Introduction to build profiles

Manage scenes in a build

# Create and manage build profiles

Create and manage **build profiles**A set of customizable configuration settings to use when creating a build for your target platform. [More info](build-profiles.html)  
See in [Glossary](Glossary.html#buildprofile) to configure your application for multiple platforms.

## Create a build profile

To create a build profile, use the following steps:

1. Navigate to **File** > **Build Profiles**.
2. In the **Build Profiles** window, select **Add Build Profile** to open the **Platform Browser** window. The **Platform Browser** window presents a list of supported platforms that include desktop, mobile, web, and **closed platforms**Includes platforms that require confidentiality and legal agreements with the platform provider for using their developer tools and hardware. These platforms aren’t open to development unless you have an established relationship with the provider. For example PlayStation®, Game Core for Xbox®, and Nintendo®.  
   See in [Glossary](Glossary.html#closedplatform).
3. In the **Platform Browser** window, select the target platform. If the selected platform isn’t currently installed on your machine, use **Install with Unity Hub** and follow the installation instructions. Before installing any platform modules, refer to the [System requirements](system-requirements.html) page.
4. Enter a unique name for the build profile in the **Name** field. The name identifies the build profile in the **Build Profiles** window.
5. Select any recommended packages to install from the **Packages** section. Required packages are automatically selected for installation when creating a build profile from the **Platform Browser**.
6. Select **Add Build Profile**.
7. Select the required [platform settings](build-profiles-reference.html).
8. Select **Switch Profile** to set the new build profile as the active profile. This will attach an **Active** badge to the build profile name.

**Note**: If you plan to deploy your application on a closed platform, check the license requirements. For further information, refer to [Platform Module Installation](https://unity.com/platform-installation).

## Create a build profile from a platform profile

You can duplicate an existing platform profile and create a new build profile from it. To do that, right click the selected platform and select **Copy to new profile**.

## Manage build profiles

To manage build profiles, right-click on any build profile name. These options allow you to do the following:

* Copy to a new build profile.
* Rename a build profile.
* Delete a build profile.

**Note**: There are no limits to how many build profiles you can have in a project.

## Additional resources

* [Build Profiles window reference](build-profiles-reference.html)
* [Build Profiles scripting API reference](../ScriptReference/Build.Profile.BuildProfile.html)
* [System requirements](system-requirements.html)

Introduction to build profiles

Manage scenes in a build

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)