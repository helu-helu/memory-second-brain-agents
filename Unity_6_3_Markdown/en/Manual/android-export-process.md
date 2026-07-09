* [Platform development](PlatformSpecific.html)
* [Android](android.html)
* [Building and delivering for Android](android-building-and-delivering.html)
* Export an Android project

Build your application for Android

Optimize distribution size

# Export an Android project

If you need more control over the build pipeline, you can export a Unity project as a **Gradle**An Android build system that automates several build processes. This automation means that many common build errors are less likely to occur. [More info](android-gradle-overview.html)  
See in [Glossary](Glossary.html#Gradle) project and import that into Android Studio. This is useful if you want more control over the build pipeline, want to see or modify the [Android App Manifest](android-manifest.html) that Unity generates for your application, or [integrate Unity-powered features into another Android application](UnityasaLibrary-Android.html).

## Exporting

To export a Unity project for Android Studio:

1. Open the **Build Profiles** window. (menu: **File** > **Build Profiles**).
2. From the list of platforms in the **Platforms** panel, select **Android** or [create a build profile](create-build-profile.html) for the **Android** platform.  
   **Note**: If Android is grayed out, [set up your project for Android development](android-sdksetup.html).
3. Enable **Export Project**.
4. Click **Export**.
5. Select the destination folder and click **Select Folder** to start the export process.

After Unity exports the Gradle project, you can import the Gradle project into Android Studio. For information on how to do this, refer to [Migrate to Android Studio](https://developer.android.com/studio/intro/migrate.html). For information on the file structure of the exported Gradle project, refer to [Gradle project structure](android-gradle-overview.html#gradle-project-structure).

## Additional resources

* [Gradle for Android](android-gradle-overview.html)
* [Build your application for Android](android-BuildProcess.html)

Build your application for Android

Optimize distribution size

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)