* [Platform development](PlatformSpecific.html)
* [Cross-platform features and considerations](cross-platform-features.html)
* [Device Simulator](device-simulator.html)
* Simulated classes

The Simulator view

Adding a device

# Simulated classes

The Device Simulator provides simulated classes, which you can use to test code that responds to device-specific behaviors in the Device Simulator.

The following simulated classes are in the UnityEngine.Device namespace:

* [Application](../ScriptReference/Device.Application.html)
* [Screen](../ScriptReference/Device.Screen.html)
* [SystemInfo](../ScriptReference/Device.SystemInfo.html)

These simulated classes have the same members as their regular UnityEngine namespace counterparts. You can use them anywhere in your codebase where you would normally use the regular classes. There is no performance impact, and you can use them in release builds.

In the Editor, when the Device Simulator is [active](device-simulator-introduction.html#limitations), the simulated classes mimic the platform-specific behaviors of the simulated device; for example, [Device.SystemInfo.operatingSystem](../ScriptReference/Device.SystemInfo-operatingSystem.html) returns the Android or iOS version of the simulated device.

In a built application, or when the Device Simulator isn’t active, the simulated classes have the same behavior as their counterparts in the UnityEngine namespace.

Although the simulated classes have the same members as the regular classes, the Device Simulator doesn’t simulate every behavior. In the UnityEditor, members that the Device Simulator doesn’t simulate have the same behavior as their UnityEngine equivalent, which isn’t platform-dependent. For example, the Device Simulator doesn’t simulate [Device.Screen.brightness](../ScriptReference/Device.Screen-brightness.html). This means this member has the same in-Editor behavior as [UnityEngine.Screen.brightness](../ScriptReference/Screen-brightness.html), which always returns `1`. For information on which members the Device Simulator simulates, see the API documentation for:

* [Device.Application](../ScriptReference/Device.Application.html)
* [Device.Screen](../ScriptReference/Device.Screen.html)
* [Device.SystemInfo](../ScriptReference/Device.SystemInfo.html)

## Updating your scripts to use simulated classes

If you want to convert existing code to use classes from the UnityEngine.Device namespace, it’s best practice to use [alias directives](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/using-directive). For example:

```
using Screen = UnityEngine.Device.Screen;
using Application = UnityEngine.Device.Application;
using SystemInfo = UnityEngine.Device.SystemInfo;
```

This way you can change which class the entire file uses and not change every API call.

The Simulator view

Adding a device

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)