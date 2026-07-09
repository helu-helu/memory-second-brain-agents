* [Platform development](PlatformSpecific.html)
* [Android](android.html)
* [Developing for Android](android-developing.html)
* [Android application entry points](android-application-entries.html)
* [The Activity application entry point](android-application-entries-activity.html)
* Extend the default Unity activity

Activity requirements and compatibility

Create a custom activity

# Extend the default Unity activity

The `UnityPlayerActivity` of a Unity Android application is responsible for basic interactions between the Android operating system and the application. You can use **plug-ins**A set of code created outside of Unity that creates functionality in Unity. There are two kinds of plug-ins you can use in Unity: Managed plug-ins (managed .NET assemblies created with tools like Visual Studio) and Native plug-ins (platform-specific native code libraries). [More info](./plug-ins.html)  
See in [Glossary](Glossary.html#plug-in) to create your own [Activity](https://developer.android.com/reference/android/app/Activity.html) that extends and overrides Unity’s default `UnityPlayerActivity`.

**Notes**:

* If you’re creating a custom activity with GameActivity application entry point, you need to extend the `UnityPlayerGameActivity` class.
* `UnityPlayerActivity` and `UnityPlayerGameActivity` use the `UnityPlayerForActivityOrService` and `UnityPlayerForGameActivity` bridge classes respectively. Unity splits these bridge classes from the `UnityPlayer` Java class. To create a custom activity, extend `UnityPlayerActivity` or `UnityPlayerGameActivity` and not the bridge classes. If your activity code references the `UnityPlayer` class directly, rename it to the relevant bridge class to avoid compile errors.

| **Topic** | **Description** |
| --- | --- |
| [Create a custom activity](android-custom-activity.html) | Extend the default Unity activity to control interactions between Unity and Android. |
| [Specify Android Player command-line arguments](android-custom-activity-command-line.html) | Specify startup command-line arguments to pass to Unity. |

## Additional resources

* [Android plug-ins](PluginsForAndroid.html)

Activity requirements and compatibility

Create a custom activity

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)