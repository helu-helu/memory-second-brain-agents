* [Platform development](PlatformSpecific.html)
* [Android](android.html)
* [Building and delivering for Android](android-building-and-delivering.html)
* [Modify Gradle project files](android-modify-gradle-project-files.html)
* Modify Gradle project files with Gradle template files

Modify the Gradle project files for a Unity application

Modify Gradle project files with the Android Project Configuration Manager

# Modify Gradle project files with Gradle template files

To have some control over the format and contents of **Gradle**An Android build system that automates several build processes. This automation means that many common build errors are less likely to occur. [More info](android-gradle-overview.html)  
See in [Glossary](Glossary.html#Gradle) project files, you can override Unity’s default templates with your own custom template. To do this:

1. Go to **Edit** > **Project Settings** to open the Project Settings window.
2. Select the **Player** tab, then open [Android Player Settings](class-PlayerSettingsAndroid.html)
3. In the **Publishing Settings** section, enable the checkbox that corresponds to the Gradle project file type you want to create a custom template for. This creates a Gradle project template file and displays the path to the file.
4. Modify the template file to control the final format and contents of the final Gradle project file.

**Note**: If there is a discrepancy between the values set in the Android **Player settings**Settings that let you set various player-specific options for the final game built by Unity. [More info](class-PlayerSettings.html)  
See in [Glossary](Glossary.html#PlayerSettings) and the template file, Unity displays a warning message, and Player settings take precedence.

To verify that your template modifications give the result that you expect, [export your project](android-export-process.html) and view the final Gradle project files in the resulting project.

## Additional resources

* [Gradle template variables](android-gradle-template-variables.html)
* [Export an Android project](android-export-process.html)
* [Modify Gradle project files with the Android Project Configuration Manager](android-modify-gradle-project-files-agp.html)
* [Modify Gradle project files with Android Studio](android-modify-gradle-project-files-android-studio.html)

Modify the Gradle project files for a Unity application

Modify Gradle project files with the Android Project Configuration Manager

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)