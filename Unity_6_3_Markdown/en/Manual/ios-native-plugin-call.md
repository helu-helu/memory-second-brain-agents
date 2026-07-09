* [Platform development](PlatformSpecific.html)
* [iOS](iphone.html)
* [Developing for iOS](ios-developing.html)
* [Native plug-ins for iOS](PluginsForIOS.html)
* [Use your native plug-in for iOS](ios-native-plugin-use.html)
* Call native plug-ins for iOS

Use your native plug-in for iOS

Callback from native code

# Call native plug-ins for iOS

Your app can only call iOS native **plug-ins**A set of code created outside of Unity that creates functionality in Unity. There are two kinds of plug-ins you can use in Unity: Managed plug-ins (managed .NET assemblies created with tools like Visual Studio) and Native plug-ins (platform-specific native code libraries). [More info](./plug-ins.html)  
See in [Glossary](Glossary.html#plug-in) when deployed on an actual device. Wrap all native code methods with an additional C# code layer to only call native methods when the app is running on a device. Store this C# file in your Project’s `Assets` folder.

This C# layer can use [platform conditional compilation](platform-dependent-compilation.html) or check [`Application.platform`](../ScriptReference/Application-platform.html). For code running in the Unity Editor, return placeholder values.

Refer to the following sections for simple implementations of these methods. For a more detailed implementation, download the [Bonjour Browser sample](ios-native-plugin-bonjour-sample.html).

## Use conditional compilation

Platform dependent compilation is faster than `Application.platform` as it’s evaluated at compile time, rather than runtime.

Use the following to implement conditional compilation:

```
void MyMethod()
{
#if UNITY_IOS && !UNITY_EDITOR
    CallNativeMethodImplementation();
#else
    CallEditorMethodImplementation();
#endif
}
```

## Check Application.platform

Use the following to implement [`Application.platform`](../ScriptReference/Application-platform.html) and return placeholder values in the Editor:

```
void MyMethod()
 {
    if (Application.platform != RuntimePlatform.OSXEditor)
    {
        return _GetLookupStatus();
    }
    else
    {
        return "Done";
    }
}
```

## Additional resources

* [Callback from native code](ios-native-plugin-call-back.html)
* [Bonjour Browser sample](ios-native-plugin-bonjour-sample.html).

Use your native plug-in for iOS

Callback from native code

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)