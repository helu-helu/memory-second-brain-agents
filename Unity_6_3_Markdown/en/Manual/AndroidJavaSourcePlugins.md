* [Platform development](PlatformSpecific.html)
* [Android](android.html)
* [Developing for Android](android-developing.html)
* [Create and use plug-ins in Android](PluginsForAndroid.html)
* [Android plug-in types](android-plugin-types.html)
* Java and Kotlin source plug-ins

Call native plug-in for Android code

Calling Java and Kotlin plug-in code from C# scripts

# Java and Kotlin source plug-ins

Unity can interpret individual Java and Kotlin source files as individual **plug-ins**A set of code created outside of Unity that creates functionality in Unity. There are two kinds of plug-ins you can use in Unity: Managed plug-ins (managed .NET assemblies created with tools like Visual Studio) and Native plug-ins (platform-specific native code libraries). [More info](./plug-ins.html)  
See in [Glossary](Glossary.html#plug-in).

Unity supports Java and Kotlin code written in source files with `.java` and `.kt` extensions. To do this, Unity interprets each source file as an individual plug-in and compiles them when it builds the Player. This type of plug-in is useful if you need to write a small amount of code for a single project. If you plan to reuse the code in multiple projects or distribute it to other people, then an [Android Library or Android Archive plug-ins](AndroidAARPlugins.html) might be more appropriate.

## Create a Java or Kotlin source plug-in

To indicate to Unity to create a plug-in from a Java (`.java`) or Kotlin (`.kt`) source file, follow these steps:

1. In the **Assets** folder, place your Java (`.java`) or Kotlin (`.kt`) source file.  
   **Tip**: It’s best practice to create a subfolder to contain your Java and Kotlin source files.
2. Select the source file and view it in the ****Inspector**A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
   See in [Glossary](Glossary.html#Inspector)** window.
3. In the **Inspector** window, under the **Select Platforms for plugin** section, enable **Android**.
4. Select **Apply**.

**Note**: You can place the source files in any folder in your project, except in special use locations such as `StreamingAssets`. If you place files in these locations, the Unity Editor doesn’t display the **Plugin Inspector**.

## Example: Create and use Kotlin source plug-in

The following example demonstrates how to create a Kotlin source plug-in and access its code from a C# script. This allows you to use Android-specific functionality in your Unity project.

1. In the **Assets** folder of your project, create a subfolder named **AndroidPlugins**, and add a Kotlin (`.kt`) file to it with the following code.

   ```
     object KotlinStringHelper {
     @JvmStatic
     fun getString(): String {
        return "Hello from Kotlin"
     }
     }
   ```
2. Select the Kotlin file. In the **Inspector** window, under the **Select Platforms for plugin** section, enable the Android platform.
3. Select **Apply**.
4. In Unity, create a C# script and add the following code. This code uses [AndroidJavaClass](../ScriptReference/AndroidJavaClass.html) to access the static Kotlin method `getString`.

   ```
     using UnityEngine;

     public class KotlinExamples : MonoBehaviour
     {
        void Start()
        {
           using (AndroidJavaClass cls = new AndroidJavaClass("KotlinStringHelper"))
           {
              string value = cls.CallStatic<string>("getString");
              Debug.Log($"KotlinStringHelper.getString returns {value}");
           }
        }
     }
   ```
5. Attach the C# Script to a **GameObject**The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)  
   See in [Glossary](Glossary.html#GameObject). For more information, refer to the documentation on [Controlling a GameObject](class-MonoBehaviour.html).

## Edit Java or Kotlin files in an exported Android Studio project

By default, when you [export a Unity project for Android](android-export-process.html), Unity copies any Java/Kotlin files over to the Android Studio project. If you edit these files in Android Studio, the changes aren’t reflected in the original files in the Unity project. If you export the Unity project again, the export process overwrites your changes in Android Studio.

To resolve this, Unity provides the **Symlink Sources** [build setting](android-build-settings.html). If you select this build setting, Unity creates a [symbolic link](https://en.wikipedia.org/wiki/Symbolic_link) in the Android Studio project to Java/Kotlin files in the Unity project, instead of copying files over. This means that if you edit the files in Android Studio, the changes will reflect in the original Unity project files.

## Additional resources

* [Android plug-in types](android-plugin-types.html)
* [Calling Java and Kotlin plug-in code from C# scripts](android-plugins-java-code-from-c-sharp.html)

Call native plug-in for Android code

Calling Java and Kotlin plug-in code from C# scripts

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)