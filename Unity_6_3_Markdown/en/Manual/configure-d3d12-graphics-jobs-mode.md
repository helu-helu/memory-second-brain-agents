* [Platform development](PlatformSpecific.html)
* [Windows](Windows.html)
* [Develop for Windows](windows-develop.html)
* [D3D12 API and graphics jobs mode configuration](d3d12-graphics-jobs-configuration.html)
* Configure graphics jobs mode on D3D12

D3D12 Device Filtering Asset reference

Develop Xbox games for Windows with Microsoft GDK

# Configure graphics jobs mode on D3D12

Unity supports multithreaded rendering through the [Graphics Jobs](playersettings-windows.html#GraphicsJobs) Player setting. For applications that use D3D12, multithreaded rendering can be implemented with three different graphics jobs modes. You can’t change the graphics jobs mode set through the [Graphics Jobs Mode](playersettings-windows.html#GraphicsJobsMode) Player setting at runtime. Moreover, your application might perform sub-optimally on certain Windows devices that don’t support specific graphics jobs modes with D3D12 API. To configure specific graphics jobs modes for various devices and ensure your application performs optimally across a range of device specifications, use the **Preferred Graphics Jobs Filter List**

To configure graphics jobs modes, use the following steps:

1. [Create a D3D12 Device Filtering Asset](create-d3d12-device-filtering-asset.html). The asset displays three filter lists in the ****Inspector**A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
   See in [Glossary](Glossary.html#Inspector)** window.
2. Expand the **Preferred Graphics Jobs Filter List**.
3. Select **Add** (**+**).
   A set of parameters is displayed.
4. Enter your preferred graphics jobs mode and the device specifications in the available parameters. All the parameters are optional.

   **Note**: Set **Preferred Graphics Jobs Mode** to **Off** to restrict certain devices from using graphics jobs.

Windows devices that meet the specifications defined in the parameter values always use the specified graphics jobs mode at runtime. Unity processes the **Preferred Graphics Jobs Filter List** entries in the order of priority with the first entry in the list having highest priority. If a device matches multiple entries in the **Preferred Graphics Jobs Filter List**, the graphics jobs mode specified in the first match applies.

The devices that don’t meet the specifications defined in the **Preferred Graphics Jobs Filter List** parameter values use the graphics jobs mode set through the [Graphics Jobs Mode](playersettings-windows.html#GraphicsJobsMode) Player setting. For example, if the Graphics Jobs Mode Player setting is set to **Native** but the preferred graphics jobs mode for certain Windows devices is set to **Split**, all the devices that don’t match the specifications mentioned in the filter list will use **Native** jobs mode.

## Additional resources

* [D3D12 Device Filtering Asset reference](d3d12-device-filter-list-asset-reference.html)

D3D12 Device Filtering Asset reference

Develop Xbox games for Windows with Microsoft GDK

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)