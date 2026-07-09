* [Platform development](PlatformSpecific.html)
* [Android](android.html)
* [Introducing Android](android-introducing.html)
* [Gradle for Android](android-gradle-overview.html)
* Gradle project structure

Gradle project files

Unity specific properties in gradle.properties file

# Gradle project structure

When you export your Unity project, Unity creates a **Gradle**An Android build system that automates several build processes. This automation means that many common build errors are less likely to occur. [More info](android-gradle-overview.html)  
See in [Glossary](Glossary.html#Gradle) project with the following main modules:

* **UnityLibrary**: Contains the Unity runtime and project data. This module is a library that you can integrate into any other Gradle project. Use it to embed Unity into existing Android applications.
* **Launcher** module: Contains the application’s name and all of its icons. This is a simple Android application module that launches Unity, which you can replace with your own application if required.

Refer to the following diagram for an overview of the Gradle project structure.

```
<exported_project_root>/
├── gradle/
├── launcher/
│   └── src/
│   │    └── main/
│   │       ├── res/
│   │       ├── AndroidManifest.xml
│   ├── build.gradle
│   ├── setupSymbols.gradle
├── shared/
│   └── keepUnitySymbols.gradle
├── unityLibrary/
│   ├── libs/
│   │   └── unity-classes.jar
│   └── src/
│       └── main/
│           ├── assets/
│           │   └── bin
│           ├── cpp/
│           ├── java/
│           ├── jniLibs/
│           ├── res/
│           ├── resources/
│           └── AndroidManifest.xml
├── build.gradle
├── proguard-unity.txt
├── gradle.properties
├── local.properties
└── settings.gradle
```

Refer to the following table for the description of each file/directory in the Gradle project.

| **File/Directory** | **Description** |
| --- | --- |
| `gradle/` | A directory that contains the Gradle wrapper file. For more information, refer to [The Gradle Wrapper file](https://developer.android.com/build#wrapper-file) (Android). |
| `launcher/` | A directory that contains the [launcher module](#launcher-module) and the associated files. |
| `launcher/src` | A standard Android Gradle project directory that contains the launcher module’s source code and resources. Unity places the source code and resources in the `main` subdirectory. |
| `launcher/src/main` | A standard Android Gradle project directory that contains the launcher module’s source code and resources. Unity only supports the main source set. For more information about source sets, refer to [Create source sets](https://developer.android.com/studio/build/build-variants#sourcesets) (Android). |
| `launcher/src/main/res` | A standard Android Gradle project directory that contains resources to include in the final application. These resources are application icons, text that the application accesses at runtime, and application style descriptions.   **Note**: To specify the resources in this directory, set application icons and the project name in the [Android Player Settings](class-PlayerSettingsAndroid.html). |
| `launcher/src/main/AndroidManifest.xml` | A standard Android Gradle project file that Unity merges into the final [Android App Manifest](android-manifest.html). It contains settings specific to the launcher module.   **Important**: If multiple manifest files specify different values for the same setting, the manifest merging process fails and you must fix it manually. You can specify rules for the manifest merger to automatically decide how to solve merge conflicts. For information on how to do this, refer to [Manage manifest files](https://developer.android.com/studio/build/manage-manifests) (Android).   For information on how to customize the contents of this file, refer to [Modify Gradle project files](android-modify-gradle-project-files.html). |
| `launcher/build.gradle` | A standard Gradle project `build.gradle` file that describes how to build the `launcher` module and includes a list of dependencies to include in the build. In Unity, the `launcher` module depends on the [`unityLibrary`](#unity-library) module which means `unityLibrary` is built and included in the final result when building the launcher module.   **Note**: To customize the contents of this file, provide a custom [Launcher Gradle Template](class-PlayerSettingsAndroid.html#Publishing). |
| `launcher/setupSymbols.gradle` | A Unity-specific file that includes build script to embed debug symbol files into the App Bundle and to create symbol files with the legacy `.so` extension. |
| `shared` | A directory that contains common configuration information that applies to multiple modules in a project. |
| `shared/keepUnitySymbols.gradle` | A Unity-specific file that includes a script to store debug metadata in runtime binaries for resolving stack traces. |
| `unityLibrary` | A directory that contains the [`unityLibrary`](#unity-library) module and the associated files. |
| `unityLibrary/libs` | A common Android Gradle project directory that stores [Android Archive](AndroidAARPlugins.html) (.aar) and [Java Archive](AndroidJARPlugins.html) (.jar) plug-ins for the `unityLibrary` module.   For exported Unity projects, this contains the `unity-classes.jar` and all .jar and .aar plug-ins in the Unity project.   **Note**: This directory doesn’t contain [Android Library plug-ins](AndroidAARPlugins.html). Instead, Unity copies these into the Gradle project as separate modules. |
| `unityLibrary/libs/unity-classes.jar` | A Unity-specific java plug-in that contains java code that the Unity engine uses. |
| `unityLibrary/src` | A standard Android Gradle project directory that contains the `unityLibrary` module’s source code and resources. Unity places the source code and resources in the `main` subdirectory. |
| `unityLibrary/src/main` | A standard Android Gradle project directory that contains the `unityLibrary` module’s source code and resources. Unity only supports the main source set. For more information about source sets, refer to [Create source sets](https://developer.android.com/studio/build/build-variants#sourcesets) (Android). |
| `unityLibrary/src/main/assets` | A standard Android Gradle directory that contains project assets. Unity places the Unity project’s resources in the `bin` subdirectory. |
| `unityLibrary/src/main/assets/bin` | A standard Android Gradle project directory that Unity adds all the Unity project’s resources to. |
| `unityLibrary/src/main/cpp` | A directory that contains native C and C++ code. |
| `unityLibrary/src/main/java` | A standard Android Gradle project directory that contains java source files for the `unityLibrary` module that aren’t compiled. Unity only uses this directory to store the `UnityPlayerActivity` source file. For information on how to extend `UnityPlayerActivity`, refer to [Extend the default Unity activity](AndroidUnityPlayerActivity.html). |
| `unityLibrary/src/main/jniLibs` | A standard Android Gradle project directory that contains native code libraries that the `unityLibrary` module uses. Unity places the `libil2cpp`, `libmain`, and `libunity` Unity engine libraries in this directory. Unity also places any [Native plug-ins for Android](AndroidNativePlugins.html) in this directory. |
| `unityLibrary/src/main/jniStaticLibs` | A standard Android project directory that contains `baselib.a` library that the `unityLibrary` module uses to create `libil2cpp.so`. |
| `unityLibrary/src/main/res` | A standard Android Gradle project directory that contains resources to include in the final application. For exported Unity projects, the `res` directory for the `unityLibrary` module only contains style descriptions that the `unityLibrary` module uses. |
| `unityLibrary/src/main/AndroidManifest.xml` | A standard Android Gradle project file that Unity merges into the final [Android App Manifest](android-manifest.html). It contains settings specific to the `unityLibrary` module.   **Note**: To customize the contents of this file, provide a custom [Custom Main Manifest](class-PlayerSettingsAndroid.html#Publishing). |
| `unityLibrary/symbols` | A directory that Unity adds if you choose to generate symbol files for your application through the [Debug Symbols](android-build-settings.html#debug-symbols) build setting. This directory includes files containing debug metadata and the symbol table section for Unity libraries. You can set the directory path in Android Studio to resolve function names during debugging. |
| `build.gradle` | A standard Gradle project `build.gradle` file that describes how to build the `unityLibrary` module and includes a list of dependencies to include in the build. In Unity, the `unityLibrary` module depends on all the [plug-ins](PluginsForAndroid.html)A set of code created outside of Unity that creates functionality in Unity. There are two kinds of plug-ins you can use in Unity: Managed plug-ins (managed .NET assemblies created with tools like Visual Studio) and Native plug-ins (platform-specific native code libraries). [More info](./plug-ins.html) See in [Glossary](Glossary.html#plug-in) in the Unity project.   **Note**: To customize the contents of this file, provide a custom [Main Gradle Template](class-PlayerSettingsAndroid.html#Publishing). |
| `proguard-unity.txt` | A Unity-specific file that contains ProGuard configurations for Unity java code (code in `unity-classes.jar` plug-in). Configurations are effective when you enable [minification](class-PlayerSettingsAndroid.html#minify) in Android **Player settings**Settings that let you set various player-specific options for the final game built by Unity. [More info](class-PlayerSettings.html) See in [Glossary](Glossary.html#PlayerSettings) or by manually modifying Gradle build files. |
| `build.gradle` | The base Gradle file that affects all modules in the Gradle project. It specifies which plug-in versions to use in this Gradle project. One of these plug-ins is Android Gradle Plug-in.   **Note**: To customize the contents of this file, add a custom [Base Gradle Template](class-PlayerSettingsAndroid.html#Publishing). |
| `proguard-user.txt` | This is a Unity project specific file which contains ProGuard configurations for the project’s java code and third-party java plug-ins. Similar to `ProGuard-unity.txt`, Gradle uses this file when you enable minification.   **Note**: To create this file, enable **Custom Proguard File** in the [Android Player Settings](class-PlayerSettingsAndroid.html#Publishing). |
| `gradle.properties` | A standard Gradle project file that configures how to build the application. For information on the Unity specific properties in this file, refer to [Properties in gradle.properties file](#unity-gradle-properties). For information on the Gradle properties this file can contain, refer to [Gradle property files](https://developer.android.com/studio/build#properties-files) (Android).  **Note**: To customize the contents of this file, add a custom [Gradle Properties Template](class-PlayerSettingsAndroid.html#Publishing). |
| `local.properties` | A standard Android Gradle project file that configures the environment of the build system. Unity specifies the path to SDK here so that by default, the exported Gradle project uses the same SDK that the Unity Editor used. Previously the NDK path was also specified in this file with previous Gradle versions but now Unity specifies it in the `build.gradle` files of **launcher** and **unityLibrary** modules.   For information on the properties this file can contain, refer to [Gradle property files](https://developer.android.com/studio/build#properties-files) (Android). |
| `settings.gradle` | A standard Android Gradle project file that specifies all the modules that make up this Android Gradle project. In projects that Unity exports, this usually only specifies the **launcher** and **unityLibrary** modules. However, if the Unity project uses [Play Asset Delivery](play-asset-delivery.html), each asset pack is a separate module, so this file lists them too. The file also specifies locations which contain Gradle project plug-ins. The locations are a combination of online repositories and java plug-ins inside of this project.   To customize the contents of this file, provide a custom [Gradle Settings Template](class-PlayerSettingsAndroid.html#Publishing). |

## Additional resources

* [Gradle project files](android-gradle-project-files.html)
* [Unity specific properties in gradle.properties file](android-gradle-properties.html)
* [Export an Android Project](android-export-process.html)

Gradle project files

Unity specific properties in gradle.properties file

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)