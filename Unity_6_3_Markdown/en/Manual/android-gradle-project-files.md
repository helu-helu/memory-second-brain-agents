* [Platform development](PlatformSpecific.html)
* [Android](android.html)
* [Introducing Android](android-introducing.html)
* [Gradle for Android](android-gradle-overview.html)
* Gradle project files

Unity and Gradle version compatibility

Gradle project structure

# Gradle project files

Gradle project files configure different aspects of your application, such as the modules to include and how to build them.

The following table lists the **Gradle**An Android build system that automates several build processes. This automation means that many common build errors are less likely to occur. [More info](android-gradle-overview.html)  
See in [Glossary](Glossary.html#Gradle) project files that exist for Unity projects and describes the purpose of each one.

| **Gradle project file** | **Purpose** |
| --- | --- |
| **Main Manifest** | Contains important metadata about your Android application. For more information, refer to [Unity Library Manifest](android-library-manifest.html). |
| **Unity Launcher Manifest** | Contains important metadata about your Android application’s launcher. For more information, refer to [Unity Launcher Manifest](android-launcher-manifest.html). |
| **Main Gradle** | Contains information on how to build your Android application as a library. |
| **Launcher Gradle** | Contains instructions on how to build your Android application. |
| **Base Gradle** | Contains configuration that’s shared between all other templates and Gradle projects. |
| **Gradle Properties** | Contains configuration settings for the Gradle build environment. This includes:  * The JVM (Java Virtual Machine) memory configuration. * A property to allow Gradle to build using multiple JVMs. * A property for choosing the tool to do the minification. * A property to not compress native libs when building an app bundle. |
| **Gradle Settings** | Contains declaration of artifact repositories to resolve external dependencies required for your application. |
| **Proguard** | Contains configuration settings for the minification process.   **Note:** If minification removes necessary Java code, add a rule in this file to keep that code. |

## Additional resources

* [Gradle project structure](android-gradle-project-structure.html)
* [Unity Library Manifest](android-library-manifest.html)
* [Unity Launcher Manifest](android-launcher-manifest.html)

Unity and Gradle version compatibility

Gradle project structure

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)