* [Platform development](PlatformSpecific.html)
* [Windows](Windows.html)
* [Develop for Windows](windows-develop.html)
* [D3D12 API and graphics jobs mode configuration](d3d12-graphics-jobs-configuration.html)
* Configure D3D12 API usage

Create a D3D12 Device Filtering asset

D3D12 Device Filtering Asset reference

# Configure D3D12 API usage

By default, Unity restricts certain Windows devices known to run Unity applications sub-optimally from using the D3D12 graphics API. However, you might find through testing that some restricted devices actually run your application better with D3D12 API than with D3D11 API. Alternatively, you might want to add further restrictions and prevent some devices from running your application with D3D12 API. Use **Allow and Deny Filter Lists** to fine tune which devices you want to allow to run your application with D3D12 API.

With **Allow Filter List**, you can allow certain devices to use D3D12 as the default graphics API to run your application. Alternatively, with the **Deny Filter List**, you can limit certain devices from using the D3D12 API to run your application. The restricted devices use a fallback graphics API set in the **Player** settings to run your application. If you don’t include an alternative graphics API, such as D3D11, in your **Player** settings, your application won’t launch on any devices that meet the rejection criteria. If you set the same values in both **Allow and Deny Filter Lists**, Unity ignores the criteria defined by those values.

If a device is included in both the Allow and Deny Filter Lists, the Allow Filter takes precedence and the device uses the D3D12 API. You can use these lists to restrict a large category of poorly performing devices from using the D3D12 API, but still allow devices that perform better with D3D12 API to use it. Although you can restrict the use of D3D12 API on a group of devices, you can use the **Allow Filter List** to enable particular devices from that group to still use D3D12.

To allow Windows devices to always use D3D12 API, use the following steps:

1. [Create a D3D12 Device Filtering Asset](create-d3d12-device-filtering-asset.html). The asset displays three filter lists in the ****Inspector**A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
   See in [Glossary](Glossary.html#Inspector)** window.
2. Expand the **Allow Filter List**.
3. Select **Add** (**+**). This action adds a new entry to the list.
4. In the new list entry, enter the specifications of the Windows device that you want to allow to use the D3D12 API.  
   A set of parameters is displayed.
5. Enter the device specifications in the available parameters. All the parameters are optional. For the description of parameters, refer to [D3D12 Device Filtering Asset reference](d3d12-device-filter-list-asset-reference.html).

Windows devices that meet the specifications defined in the parameter values will always use D3D12 API for Unity applications.

To restrict Windows devices from using the D3D12 API, use the **Deny Filter List** and follow the same steps as earlier.

## Additional resources

* [Introduction to D3D12 Device Filtering Asset](introduction-d3d12-device-filtering-asset.html)
* [D3D12 Device Filtering Asset reference](d3d12-device-filter-list-asset-reference.html)
* [Regular expressions](https://learn.microsoft.com/en-us/dotnet/standard/base-types/regular-expressions)

Create a D3D12 Device Filtering asset

D3D12 Device Filtering Asset reference

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)