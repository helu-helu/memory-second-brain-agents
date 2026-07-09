* [Platform development](PlatformSpecific.html)
* [Android](android.html)
* [Developing for Android](android-developing.html)
* [Android application entry points](android-application-entries.html)
* [The GameActivity application entry point](android-application-entries-game-activity.html)
* GameActivity requirements and compatibility

The GameActivity application entry point

Modify GameActivity bridge code

# GameActivity requirements and compatibility

Refer to the following system requirements and compatibility information before using the GameActivity application entry point in your Unity Android project.

## Unity and GameActivity library version compatibility

The following table lists the recommended GameActivity library version for the latest supported patch release of each Unity version.

| **Unity version** | **GameActivity library version** |
| --- | --- |
| 6000.3 and later | 4.4.0 |
| 6000.2 | 3.0.5 |
| 6000.0 | 4.4.2 |

## Dependencies

GameActivity requires the following dependencies:

* CMake build system
* AndroidX

### CMake

GameActivity uses [CMake](https://developer.android.com/ndk/guides/cmake) to produce the bridge code (`libgame.so`) during the build process.

**Note**: If you provide a custom Android SDK, be sure the SDK has CMake 3.22.1 included.

### AndroidX

GameActivity requires the following AndroidX **Gradle**An Android build system that automates several build processes. This automation means that many common build errors are less likely to occur. [More info](android-gradle-overview.html)  
See in [Glossary](Glossary.html#Gradle) dependencies:

* `androidx.appcompat:appcompat`
* `androidx.games:games-activity`
* `androidx.core:core`
* `Androidx.constraintlayout`

Gradle installs AndroidX and these dependencies automatically.

## Plug-in compatibility

If you use GameActivity, your application player loop runs on a native thread rather than a Java thread. This means that calling Java APIs like [myLooper](https://developer.android.com/reference/android/os/Looper#myLooper()) from [plug-ins](PluginsForAndroid.html)A set of code created outside of Unity that creates functionality in Unity. There are two kinds of plug-ins you can use in Unity: Managed plug-ins (managed .NET assemblies created with tools like Visual Studio) and Native plug-ins (platform-specific native code libraries). [More info](./plug-ins.html)  
See in [Glossary](Glossary.html#plug-in) will fail. In the case of `myLooper` it’s because there’s no Java looper present on the native thread. This also means that any API that uses APIs such as `myLooper` will also fail. For example, [registerInputDeviceListener](https://developer.android.com/reference/android/hardware/input/InputManager#registerInputDeviceListener(android.hardware.input.InputManager.InputDeviceListener,%20android.os.Handler)) will fail if the handler is null. It’s important to understand this limitation when you create [Android plug-ins](PluginsForAndroid.html).

## Choreographer

If you use GameActivity, Unity tries to use the [NDK choreographer](https://developer.android.com/ndk/reference/group/choreographer) to synchronize frame times. If the [Device API Level](../ScriptReference/AndroidSdkVersions.html) is lower than 24, or your application uses a 32-bit Player and the Device API Level is lower than 29, Unity uses the [Java choreographer](https://developer.android.com/reference/android/view/Choreographer).

## Additional resources

* [The Activity application entry point](android-application-entries-activity.html)

The GameActivity application entry point

Modify GameActivity bridge code

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)