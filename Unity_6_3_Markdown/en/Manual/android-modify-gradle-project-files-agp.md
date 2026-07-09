* [Platform development](PlatformSpecific.html)
* [Android](android.html)
* [Building and delivering for Android](android-building-and-delivering.html)
* [Modify Gradle project files](android-modify-gradle-project-files.html)
* Modify Gradle project files with the Android Project Configuration Manager

Modify Gradle project files with Gradle template files

Modify Gradle project files with Android Studio

# Modify Gradle project files with the Android Project Configuration Manager

You can use Android Project Configuration Manager to modify the contents of custom **gradle**An Android build system that automates several build processes. This automation means that many common build errors are less likely to occur. [More info](android-gradle-overview.html)  
See in [Glossary](Glossary.html#Gradle) project files in your Android project. You cannot modify the contents of the default gradle project files `unityLibrary` and `launcher` modules with Android Project Configuration Manager. However, you can create custom modules to set up custom Gradle project files and modify them as required.

The entry point for the Android Project Configuration Manager is the [OnModifyAndroidProjectFiles](../ScriptReference/Android.AndroidProjectFilesModifier.OnModifyAndroidProjectFiles.html) method in the [AndroidProjectFilesModifier](../ScriptReference/Android.AndroidProjectFilesModifier.html) interface. This means to use the Android Project Configuration Manager, first create a class that implements `AndroidProjectFilesModifier` and declares a body for `OnModifyAndroidProjectFiles`. The following code example shows how to do this.

```
using UnityEditor.Android;

public class ModifyProjectScript : AndroidProjectFilesModifier
{
    public override void OnModifyAndroidProjectFiles(AndroidProjectFiles projectFiles)
    {
    }
}
```

## Additional resources

* [Export an Android project](android-export-process.html)
* [Modify Gradle project files with Gradle template files](android-modify-gradle-project-files-templates.html)
* [Modify Gradle project files with Android Studio](android-modify-gradle-project-files-android-studio.html)

Modify Gradle project files with Gradle template files

Modify Gradle project files with Android Studio

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)