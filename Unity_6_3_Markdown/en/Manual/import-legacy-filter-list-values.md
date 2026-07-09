* [Platform development](PlatformSpecific.html)
* [Android](android.html)
* [Developing for Android](android-developing.html)
* [Graphics for Android](android-graphics.html)
* [Vulkan API and graphics jobs mode configuration](vulkanapi-graphics-jobs-configuration.html)
* Import legacy Allow and Deny Filter List values

Configure graphics jobs mode on Vulkan

Vulkan Device Filtering Asset reference

# Import legacy Allow and Deny Filter List values

The **Vulkan Device Filtering Asset** replaces the **Allow and Deny Filter List** properties in the Android **Player settings**Settings that let you set various player-specific options for the final game built by Unity. [More info](class-PlayerSettings.html)  
See in [Glossary](Glossary.html#PlayerSettings) that are now obsolete. These properties are available in Android Player settings only if you upgrade an existing project that previously used these properties. It is recommended to use the **Vulkan Device Filtering Asset** to configure Vulkan API usage for Android devices. The asset allows you to import the values configured in the legacy **Allow and Deny Filter Lists** of the existing project into the **Vulkan Device Filtering Asset**.

**Note**: The **Allow and Deny Filter List** properties aren’t available in the Android Player settings of new projects by default.

To import the legacy **Allow and Deny Filter List** values,

1. In your Unity project, select the Vulkan Device Filtering Asset you’ve created.
2. In the ****Inspector**A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
   See in [Glossary](Glossary.html#Inspector)** view of the asset, select **Import Legacy Player Settings Filter Lists** option.

   **Note**: This option is only available in the projects that previously used legacy **Allow and Deny Filter Lists**.

After the values are imported,

* The **Allow and Deny Filter List** properties no longer appear in the Android Player settings
* The **Import Legacy Player Settings Filter Lists** option is no longer available in the **Inspector** view of the asset.

## Additional resources

* [Configure Vulkan API usage](allow-deny-vulkan-usage.html)

Configure graphics jobs mode on Vulkan

Vulkan Device Filtering Asset reference

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)