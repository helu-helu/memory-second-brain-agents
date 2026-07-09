* [Platform development](PlatformSpecific.html)
* [Android](android.html)
* [Developing for Android](android-developing.html)
* [Graphics for Android](android-graphics.html)
* [Vulkan API and graphics jobs mode configuration](vulkanapi-graphics-jobs-configuration.html)
* Configure graphics jobs mode on Vulkan

Configure Vulkan API usage

Import legacy Allow and Deny Filter List values

# Configure graphics jobs mode on Vulkan

Unity supports multithreaded rendering through the [Graphics Jobs](class-PlayerSettingsAndroid.html#GraphicsJobs) Player setting. For applications using Vulkan API, multithreaded rendering can be implemented with three different graphics jobs modes. The graphics jobs mode set through the [Graphics Jobs Mode](class-PlayerSettingsAndroid.html#GraphicsJobsMode) Player setting can’t be changed at runtime. Moreover, your application might perform sub-optimally on certain Android devices that don’t support specific graphics jobs modes with Vulkan API. Using **Preferred Graphics Jobs Filter List**, you can configure specific graphics jobs modes for various devices to ensure your application performs optimally across a range of device specifications.

To configure graphics jobs modes, use the following steps:

1. [Create a Vulkan Device Filtering Asset](create-vulkan-device-filtering-asset.html). The asset displays three filter lists in the ****Inspector**A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
   See in [Glossary](Glossary.html#Inspector)** window.
2. Use the foldout (triangle) to expand the **Preferred Graphics Jobs Filter List**.
3. Select the **Add** (**+**) button to enter the specifications of the Android device for which you want to use a specific graphics jobs mode.
   A set of parameters is displayed.
4. Enter your preferred graphics jobs mode and the device specifications in the available parameters. All the parameters are optional.

   **Note**: Set **Preferred Graphics Jobs Mode** to **none** to restrict certain devices from using graphics jobs.

Android devices that meet the specifications defined in the parameter values will always use the specified graphics jobs mode at runtime. Unity processes the **Preferred Graphics Jobs Filter List** entries in the order of priority with the first entry in the list having highest priority. If a device matches multiple entries in the **Preferred Graphics Jobs Filter List**, the graphics jobs mode specified in the first match applies.

The devices that don’t meet the specifications defined in the **Preferred Graphics Jobs Filter List** parameter values, will use the graphics jobs mode set through the [Graphics Jobs Mode](class-PlayerSettingsAndroid.html#GraphicsJobsMode) Player setting. For example, if the Graphics Jobs Mode Player setting is set to **Native** but the preferred graphics jobs mode for certain Android devices is set to **Split**, all the devices that don’t match the specifications mentioned in the filter list will use **Native** jobs mode.

## Additional resources

* [Vulkan Device Filtering Asset reference](vulkan-device-filter-list-asset-reference.html)

Configure Vulkan API usage

Import legacy Allow and Deny Filter List values

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)