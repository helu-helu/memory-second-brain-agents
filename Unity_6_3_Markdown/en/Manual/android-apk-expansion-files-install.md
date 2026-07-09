* [Platform development](PlatformSpecific.html)
* [Android](android.html)
* [Developing for Android](android-developing.html)
* [Android application size restrictions](android-application-size-restrictions.html)
* [APK expansion files](android-OBBsupport.html)
* Manually install an APK expansion file

APK expansion files in Unity

Host APK expansion files

# Manually install an APK expansion file

Main and patch expansion files must be in a particular location on the device for the application to read from them. If you [Build and Run](android-BuildProcess.html) your application, Unity installs both the **APK**The Android Package format output by Unity. An APK is automatically deployed to your device when you select File > Build & Run. [More info](android-BuildProcess.html)  
See in [Glossary](Glossary.html#APK) and the main APK expansion file on the device.

If you instead want to install the application manually, or want to install a patch expansion file, you must use the ****ADB**An Android Debug Bridge (ADB). You can use an ADB to deploy an Android package (APK) manually after building. [More info](https://developer.android.com/studio/command-line/adb.html)  
See in [Glossary](Glossary.html#ADB)** utility to copy APK expansion files into the correct location on your device. For information on how to do this, refer to [Testing file reads](https://developer.android.com/google/play/expansion-files.html#TestingReading).

**Note**: The APK expansion file name must correspond to the format that Google requires. For more information, refer to [expansion files](https://developer.android.com/google/play/expansion-files.html).

## Additional resources

* [Host APK expansion files](android-apk-expansion-files-host.html)

APK expansion files in Unity

Host APK expansion files

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)