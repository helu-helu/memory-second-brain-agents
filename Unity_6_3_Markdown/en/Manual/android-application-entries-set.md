* [Platform development](PlatformSpecific.html)
* [Android](android.html)
* [Developing for Android](android-developing.html)
* [Android application entry points](android-application-entries.html)
* Set the application entry point for your Android application

Update the GameActivity library

Deep linking on Android

# Set the application entry point for your Android application

You control the application entry points through [Android Player Settings](class-PlayerSettingsAndroid.html). You can set multiple application entry points for **development builds**A development build includes debug symbols and enables the Profiler. [More info](building-introduction.html)  
See in [Glossary](Glossary.html#developmentbuild) of your application which helps you to quickly compare functionality and performance between different application entry points. However, you must only select one application entry point for release builds that you intend to publish. If you select more than one, Unity displays a warning message.

To set which application entry point/s to use for your application:

1. Open [Android Player Settings](class-PlayerSettingsAndroid.html).
2. Go to **Other Settings** > **Configuration** > **Application Entry Point**.
3. In the **Application Entry Point** section, select which application entry points you want to use.

If you select more than one application entry point and build or export your application, Unity generates multiple `activity` entries in the [Android App Manifest](android-manifest.html); one for each application entry point. If you open the project in Android Studio, you can specify which application entry point you want to run/debug in the [Run/Debug Configurations dialog](https://developer.android.com/studio/run/rundebugconfig#opening). If you install the built application on a device, there will be as many application icons as there are application entry points.

## Additional resources

* [The Activity application entry point](android-application-entries-activity.html)
* [The GameActivity application entry point](android-application-entries-game-activity.html)

Update the GameActivity library

Deep linking on Android

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)