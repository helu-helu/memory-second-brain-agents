* [Platform development](PlatformSpecific.html)
* [Android](android.html)
* [Developing for Android](android-developing.html)
* [Android application entry points](android-application-entries.html)
* [The Activity application entry point](android-application-entries-activity.html)
* Activity requirements and compatibility

The Activity application entry point

Extend the default Unity activity

# Activity requirements and compatibility

Activity was originally the only application entry point that Unity supported and because of this it’s very stable in the majority of scenarios and is compatible with the majority of Unity features.

## Plug-in compatibility

If you use Activity, your application player loop runs on a Java thread. This means that you can call Java APIs like [myLooper](https://developer.android.com/reference/android/os/Looper#myLooper()) from **plug-ins**A set of code created outside of Unity that creates functionality in Unity. There are two kinds of plug-ins you can use in Unity: Managed plug-ins (managed .NET assemblies created with tools like Visual Studio) and Native plug-ins (platform-specific native code libraries). [More info](./plug-ins.html)  
See in [Glossary](Glossary.html#plug-in).

## Choreographer

If you use Activity, Unity uses the [Java choreographer](https://developer.android.com/reference/android/view/Choreographer). This helps you to understand how frame synchronization occurs in your application.

## Additional resources

* [The GameActivity application entry point](android-application-entries-game-activity.html)

The Activity application entry point

Extend the default Unity activity

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)