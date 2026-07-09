* [Platform development](PlatformSpecific.html)
* [Android](android.html)
* [Developing for Android](android-developing.html)
* [Create and use plug-ins in Android](PluginsForAndroid.html)
* [Android plug-in types](android-plugin-types.html)
* [Native plug-ins for Android](AndroidNativePlugins.html)
* Call native plug-in for Android code

Import a native plug-in for Android

Java and Kotlin source plug-ins

# Call native plug-in for Android code

The process to call code in native **plug-ins**A set of code created outside of Unity that creates functionality in Unity. There are two kinds of plug-ins you can use in Unity: Managed plug-ins (managed .NET assemblies created with tools like Visual Studio) and Native plug-ins (platform-specific native code libraries). [More info](./plug-ins.html)  
See in [Glossary](Glossary.html#plug-in) for Android is the same as standard [native plug-ins](plug-ins-native.html)A platform-specific native code library that is created outside of Unity for use in Unity. Allows you can access features like OS calls and third-party code libraries that would otherwise not be available to Unity. [More info](./plug-ins.html)  
See in [Glossary](Glossary.html#nativeplug-in).

**Note**: If you use individual C/C++ source files as plug-ins, use `__Internal` as the plug-in name in the [DllImport](https://docs.microsoft.com/en-us/dotnet/api/system.runtime.interopservices.dllimportattribute) attribute.

It’s best practice to wrap all native plug-in method calls with an additional C# code layer that:

* Checks [Application.platform](../ScriptReference/Application-platform.html) and only calls native methods when the application is running on Android devices using the architecture that you compiled the native plug-in for. On other platforms and architectures, the additional C# code layer should return dummy values.
* Uses [platform defines](platform-dependent-compilation.html) to control platform dependent code compilation and only compile code that uses the plug-in on platforms that have the plug-in available.

## Sample package

The [AndroidNativePlugin.unitypackage](../uploads/Examples/AndroidNativePlugin.zip) zip file contains a simple example of a native code plug-in distributed as a Unity package.

The sample shows how to invoke C++ code from a Unity application. The package includes a **scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) which displays the sum of two values as calculated by a native plug-in. To compile the plug-in, use [Android NDK](https://developer.android.com/ndk/index.html). For information on how to install Android NDK via the Unity Hub, see [Android environment setup](android-sdksetup.html).

To install the sample:

1. Download the zip file.
2. Extract the `AndroidNativePlugin.unitypackage` file.
3. In a Unity project, click **Assets** > **Import Package** > **Custom Package**.
4. In the **Import Package** file dialog, find and select the extracted `AndroidNativePlugin.unitypackage` file.

Import a native plug-in for Android

Java and Kotlin source plug-ins

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)