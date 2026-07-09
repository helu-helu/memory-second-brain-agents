* [Platform development](PlatformSpecific.html)
* [Android](android.html)
* [Developing for Android](android-developing.html)
* [Create and use plug-ins in Android](PluginsForAndroid.html)
* [Android plug-in types](android-plugin-types.html)
* JAR plug-ins

Import an Android Archive plug-in

Native plug-ins for Android

# JAR plug-ins

You can use Java Archive (JAR) **plug-ins**A set of code created outside of Unity that creates functionality in Unity. There are two kinds of plug-ins you can use in Unity: Managed plug-ins (managed .NET assemblies created with tools like Visual Studio) and Native plug-ins (platform-specific native code libraries). [More info](./plug-ins.html)  
See in [Glossary](Glossary.html#plug-in) to interact with the Android OS or to call methods written in Java from C# **scripts**A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts).

Java Archive (JAR) plug-ins contain Java code that you can call from C# scripts. They’re useful if you want to interact with the Android operating system, or just call Java code from C#.

This type of plug-in is useful if you plan to reuse Java code in multiple projects, or distribute it to other people. If instead you only want to write a small amount of Java code for a single project, then a [Java or Kotlin source code plug-in](AndroidJavaSourcePlugins.html) might be more appropriate.

## Import a JAR plug-in

To import a [JAR plug-in](AndroidJARPlugins.html) (AAR) plug-in into your Unity Project:

1. Copy the `.jar` file to your Unity Project’s **Assets** folder.
2. Select the `.jar` file in Unity and view it in the **Inspector**A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
   See in [Glossary](Glossary.html#Inspector).
3. In the **Select platforms for plugin** section, select **Android**.
4. Select **Apply**.

## Additional resources

* [Android plug-in types](android-plugin-types.html)
* [Calling Java and Kotlin plug-in code from C# scripts](android-plugins-java-code-from-c-sharp.html)

Import an Android Archive plug-in

Native plug-ins for Android

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)