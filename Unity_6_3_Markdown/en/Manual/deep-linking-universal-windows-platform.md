* [Platform development](PlatformSpecific.html)
* [Universal Windows Platform](WindowsStore.html)
* [Develop for Universal Windows Platform](uwp-developing.html)
* Use deep linking on UWP

Develop for Universal Windows Platform

Connect the profiler to UWP

# Use deep linking on UWP

Deep links are URL links outside of your application that direct users to a location in your application. When the user clicks a deep link for an application, the operating system opens the Unity application at a specified place (for example, a specific scene). You can enable deep linking for Universal Windows Platform (UWP) applications. For more information about deep links and how to use them, refer to [Deep links](deep-linking.html).

## Enable deep linking for UWP applications

Before you can process deep links, you need to configure your application to react to them by adding a custom URI scheme.

To add a custom URI scheme, perform the following steps:

1. Go to **Edit** > **Project Settings** > **Player Settings**.
2. Select UWP to open the [UWP Player Settings](class-PlayerSettingsWSA.html) window.
3. Select **Publishing Settings** > **Protocol**.
4. In the **Name** field, enter the URI to associate with your application. For example, `unitydl`.

Your UWP application now opens when the device processes any link that starts with `unitydl://`.

## Use deep linking on UWP

After you enable deep links for Universal Windows Platform, the way that you use them is platform-agnostic. For information on how to handle deep links when your application opens, refer to [Using deep links](deep-linking.html#using-deep-links).

Develop for Universal Windows Platform

Connect the profiler to UWP

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)