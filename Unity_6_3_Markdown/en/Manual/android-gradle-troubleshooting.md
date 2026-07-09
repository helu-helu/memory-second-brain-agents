* [Platform development](PlatformSpecific.html)
* [Android](android.html)
* [Introducing Android](android-introducing.html)
* [Gradle for Android](android-gradle-overview.html)
* Troubleshooting Gradle build issues for Android

Unity specific properties in gradle.properties file

Android App Manifest

# Troubleshooting Gradle build issues for Android

When you build your Android project using **Gradle**An Android build system that automates several build processes. This automation means that many common build errors are less likely to occur. [More info](android-gradle-overview.html)  
See in [Glossary](Glossary.html#Gradle), you might run into build errors, especially if you’re using additional Android libraries or a custom `AndroidManifest.xml`. Gradle considers certain issues as errors and stops the build process. These issues include duplicate symbols, references to resources that don’t exist, or a library project that sets the same attribute as the main application.

You can resolve most of these issues by editing an `AndroidManifest.xml` file, either the main application manifest file, or one in a library your project uses.

The following sections include common Gradle build errors you might experience and how to resolve them.

* [Missing resource referenced in manifest](#missing-resource)
* [Minimum SDK version declared in manifest](#minSDKVersion)
* [Duplicate file names in APK](#duplicate-filenames)
* [Multiple libraries using the same package name](#packagename-conflict)
* [Conflicting manifest attributes](#attribute-conflict)

If you experience any issues not covered in these sections, [export your Android project](android-export-process.html) as a Gradle project and build it from the command line. Building from the command line provides detailed error messages and helps you diagnose complex issues more quickly.

## Missing resource referenced in manifest

The `AndroidManifest.xml` file, either the main application manifest file or one in a library, references a resource, such as an application icon or label string that doesn’t exist in your project.

### Symptom

The build fails with an error message indicating a non-existent resource referenced in the `AndroidManifest.xml` file.

### Cause

This can occur when you copy your main manifest to a library project without removing resource references.

### Resolution

To resolve a missing resource error, follow these steps:

1. Open the `AndroidManifest.xml` file and locate the attribute that references the missing resource.
2. Remove the attribute from one of the Android manifest files, typically the one from the library.

## Minimum SDK version declared in manifest

The `android:minSdkVersion` attribute is declared in an `AndroidManifest.xml` file instead of in the `build.gradle` file. This can occur in the main manifest or in the Android library directory manifests. This doesn’t apply to `aar` **plug-ins**A set of code created outside of Unity that creates functionality in Unity. There are two kinds of plug-ins you can use in Unity: Managed plug-ins (managed .NET assemblies created with tools like Visual Studio) and Native plug-ins (platform-specific native code libraries). [More info](./plug-ins.html)  
See in [Glossary](Glossary.html#plug-in).

### Symptom

The build fails with an error indicating that the `android:minSdkVersion` is declared in a manifest file.

### Cause

Android builds require you to define the minimum SDK version in the `build.gradle` file and not in the manifest file. The build fails if the `<uses-sdk>` element remains in the main manifest or in a library directory manifest.

### Resolution

To fix this issue, follow these steps:

1. Open the main manifest `AndroidManifest.xml` file.
2. Remove the `<uses-sdk android:minSdkVersion>` element from the manifest.
3. Check the manifests in library directories for the element and remove it if present.
4. Specify the minimum SDK version in the `build.gradle` file.

**Note**: If you don’t use a custom Gradle template, Unity automatically handles the `minSdkVersion`. If you use a custom Gradle template, ensure that you specify the `minSdkVersion` in the `defaultConfig` section of the template.

## Duplicate file names in APK

The same file name exists in multiple locations, either in your main application and a library, or across multiple libraries.

### Symptom

A build error indicating duplicate file names.

### Cause

The build process copies all files into the same **APK**The Android Package format output by Unity. An APK is automatically deployed to your device when you select File > Build & Run. [More info](android-BuildProcess.html)  
See in [Glossary](Glossary.html#APK) package. Therefore, any duplicate file names cause a build failure.

### Resolution

To resolve duplicate file name issue, remove the duplicate file from one of the locations.

## Multiple libraries using the same package name

A library uses the same Java package name as the main application or another library.

### Symptom

The build fails with an error message indicating a Java package name conflict.

### Cause

Gradle doesn’t allow you to use the same Java package name in both your main application and a library, or across multiple libraries.

### Resolution

To resolve conflict between package names, follow these steps:

1. Identify the library with the conflicting package name from the build error.
2. Rename the library’s package to something unique. If the library contains significant code, rename the package through **Player Settings** > **Android** > **Package Name**.

## Conflicting manifest attributes

A library attempts to override attributes from the main `AndroidManifest.xml` file, such as the application icon or label string.

### Symptom

A build error indicating an attribute conflict during the build process.

### Cause

A library attempts to override attributes from the main `AndroidManifest.xml` file causing a merge conflict during the build process.

### Resolution

To resolve conflicting attributes, use either of the following approaches:

* Remove the conflicting attribute from the library’s Android manifest file.
* Add a `tools:replace` attribute to the application tag to specify how Gradle should resolve the merge conflict.

## Additional resources

* [Build your application for Android](android-BuildProcess.html)
* [Android App Manifest](android-manifest.html)
* [Troubleshooting for Android](android-troubleshooting.html)

Unity specific properties in gradle.properties file

Android App Manifest

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)