* [Platform development](PlatformSpecific.html)
* [Android](android.html)
* [Developing for Android](android-developing.html)
* [Graphics for Android](android-graphics.html)
* [Vulkan API and graphics jobs mode configuration](vulkanapi-graphics-jobs-configuration.html)
* Configure Vulkan API usage

Create a Vulkan Device Filtering Asset

Configure graphics jobs mode on Vulkan

# Configure Vulkan API usage

By default, Unity restricts certain Android devices known to run Unity applications sub-optimally from using the Vulkan graphics API. However, your testing might reveal that some restricted devices actually run your application better with Vulkan API than with OpenGLES3 API. Alternatively, you might want to further restrict some devices to run your application with Vulkan API. Using **Allow and Deny Filter Lists**, you can fine tune which devices you want to allow to run your application with Vulkan API.

With **Allow Filter List**, you can allow certain devices to use Vulkan as the default graphics API to run your application. Alternatively, with the **Deny Filter List**, you can limit certain devices from using the Vulkan API to run your application. The restricted devices use a fallback graphics API set in the **Player settings**Settings that let you set various player-specific options for the final game built by Unity. [More info](class-PlayerSettings.html)  
See in [Glossary](Glossary.html#PlayerSettings) to run your application. If you don’t include an alternative graphics API, such as OpenGLES3, in your Player Settings, your application won’t launch on any devices that meet the rejection criteria. If you set the same values in both **Allow and Deny Filter Lists**, Unity ignores the criteria defined by those values.

If a device is included in both the Allow and Deny Filter Lists, the Allow Filter takes precedence and the device uses the Vulkan API. You can use these lists to restrict a large category of poorly performing devices from using the Vulkan API, while still allowing those devices within the category that perform better using Vulkan API. Although you can restrict the use of Vulkan API on a group of devices, you can use the **Allow Filter List** to enable particular devices from that group to still use Vulkan.

To allow Android devices to always use Vulkan API, use the following steps:

1. [Create a Vulkan Device Filtering Asset](create-vulkan-device-filtering-asset.html). The asset displays three filter lists in the ****Inspector**A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
   See in [Glossary](Glossary.html#Inspector)** window.
2. Use the foldout (triangle) to expand the **Allow Filter List**.
3. Select the **Add** (**+**) button to enter the specifications of the Android device that you want to allow the Vulkan API usage on.  
   A set of parameters is displayed.
4. Enter the device specifications in the available parameters. All the parameters are optional. For the description of parameters, refer to [Vulkan Device Filtering Asset reference](vulkan-device-filter-list-asset-reference.html).

Android devices that meet the specifications defined in the parameter values will always use Vulkan API for Unity applications.

To restrict Android devices from using the Vulkan API, use the **Deny Filter List** and follow the same steps as earlier.

## Additional resources

* [Introduction to Vulkan Device Filtering Asset](introduction-vulkan-device-filtering-asset.html)
* [Vulkan Device Filtering Asset reference](vulkan-device-filter-list-asset-reference.html)
* [Regular expressions](https://learn.microsoft.com/en-us/dotnet/standard/base-types/regular-expressions)
* [androidVulkanDenyFilterList API](../ScriptReference/PlayerSettings.Android-androidVulkanDenyFilterList.html)
* [androidVulkanAllowFilterList API](../ScriptReference/PlayerSettings.Android-androidVulkanAllowFilterList.html)
* [Import legacy Allow and Deny Filter List values](import-legacy-filter-list-values.html)

Create a Vulkan Device Filtering Asset

Configure graphics jobs mode on Vulkan

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)