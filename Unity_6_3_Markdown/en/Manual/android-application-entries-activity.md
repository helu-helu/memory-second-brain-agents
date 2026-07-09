* [Platform development](PlatformSpecific.html)
* [Android](android.html)
* [Developing for Android](android-developing.html)
* [Android application entry points](android-application-entries.html)
* The Activity application entry point

Android application entry points

Activity requirements and compatibility

# The Activity application entry point

[Activity](https://developer.android.com/reference/android/app/Activity) was originally the only application entry point that Unity supported and because of this it’s very stable in the majority of scenarios.

This application entry point is appropriate to use in the following scenarios:

* Your project uses [plug-ins](PluginsForAndroid.html)A set of code created outside of Unity that creates functionality in Unity. There are two kinds of plug-ins you can use in Unity: Managed plug-ins (managed .NET assemblies created with tools like Visual Studio) and Native plug-ins (platform-specific native code libraries). [More info](./plug-ins.html)  
  See in [Glossary](Glossary.html#plug-in) that must run on a Java thread. For more information, refer to [Plug-in compatibility](android-application-entries-activity-requirements.html#plug-in-compatibility).
* You are upgrading an old project that already uses the Activity application entry point.

If the above scenarios don’t apply to your project, the GameActivity application entry point is a more appropriate application entry point. Among other benefits, Unity’s implementation of GameActivity gives you more control over the interaction between Android and your application. For more information, refer to [GameActivity application entry point](android-application-entries-game-activity.html).

| **Topic** | **Description** |
| --- | --- |
| [Activity requirements and compatibility](android-application-entries-activity-requirements.html) | Understand the system requirements and feature compatibility of the Activity application entry point. |
| [Extend the default Unity activity](AndroidUnityPlayerActivity.html) | Override basic interactions between the Android operating system and the Unity Android application. |

## Additional resources

* [Set the application entry point for your Android application](android-application-entries-set.html)

Android application entry points

Activity requirements and compatibility

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)