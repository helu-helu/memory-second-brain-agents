* [Platform development](PlatformSpecific.html)
* [Android](android.html)
* [Developing for Android](android-developing.html)
* [Android application size restrictions](android-application-size-restrictions.html)
* [APK expansion files](android-OBBsupport.html)
* APK expansion files in Unity

APK expansion files

Manually install an APK expansion file

# APK expansion files in Unity

This page describes how [APK expansion files](android-OBBsupport.html) work in the context of a Unity Android application.

Unity can automatically split an application into a main **APK**The Android Package format output by Unity. An APK is automatically deployed to your device when you select File > Build & Run. [More info](android-BuildProcess.html)  
See in [Glossary](Glossary.html#APK) and a single APK expansion file that uses the `.obb` file extension. In Unity, this process is called splitting the application binary. The APK expansion file this process generates is the main APK expansion file and if you want to create the patch APK expansion, you must do that manually.

## Create the main APK expansion file

To create the main APK expansion file for your application, indicate to Unity to split the application. For information on how to do this, refer to [Splitting the application binary](class-PlayerSettingsAndroid.html#splitapplicationbinary).

Now when you [Build the application](android-BuildProcess.html), Unity generates the APK and the main APK expansion file then copies them both to the output directory. Unity uses the name of the application followed by `.main` for the name of the APK expansion file. For example, if the application is called `my-app`, the APK will be `my-app.apk` and the APK expansion file will be `my-app.main.obb`.

If the application starts and it can’t find and load the main APK expansion file, only the first ****Scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene)** is available. In this case, try to download the APK expansion file. For more information, refer to [Download process](https://developer.android.com/google/play/expansion-files#DownloadProcess).

## Create the patch APK expansion file

Unity only automatically creates the main APK expansion file, but you can manually create the patch APK expansion file if the application requires more storage space. For information on how to create the patch APK expansion file, refer to Android’s [Development checklist](https://developer.android.com/google/play/expansion-files#Checklist) documentation.

### APK compatibility

When you create the patch expansion file, you must include a `unity_obb_guid` file within it so Android recognizes the APK expansion as being compatible with the APK. To do this:

1. Find the main APK expansion file that Unity generates. It’s a zip archive.
2. Extract the files from the APK expansion zip archive.
3. In the list of extracted files, find the `unity_obb_guid` file.
4. Copy this file over to the patch expansion file.

## Additional resources

* [Manually install an APK expansion file](android-apk-expansion-files-install.html)
* [Host APK expansion files](android-apk-expansion-files-host.html)

APK expansion files

Manually install an APK expansion file

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)