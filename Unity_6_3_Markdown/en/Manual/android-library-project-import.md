* [Platform development](PlatformSpecific.html)
* [Android](android.html)
* [Developing for Android](android-developing.html)
* [Create and use plug-ins in Android](PluginsForAndroid.html)
* [Android plug-in types](android-plugin-types.html)
* [Android Library and Android Archive plug-ins](AndroidAARPlugins.html)
* Import an Android Library plug-in

Create an Android Library plug-in

Import an Android Archive plug-in

# Import an Android Library plug-in

You can import an [Android Library plug-in](AndroidAARPlugins.html) created outside of Unity into your Unity project using the following steps:

1. Copy the Android Library **plug-in**A set of code created outside of Unity that creates functionality in Unity. There are two kinds of plug-ins you can use in Unity: Managed plug-ins (managed .NET assemblies created with tools like Visual Studio) and Native plug-ins (platform-specific native code libraries). [More info](./plug-ins.html)  
   See in [Glossary](Glossary.html#plug-in) to the **Assets** folder of your Unity Project.
2. If the Android Library plug-in root folder doesn’t use the `.androidlib` extension, add this extension to the folder. For example, `mylibrary.androidlib`.

Unity now supports the Android Library plug-in and includes it in the final project that [Gradle](android-gradle-overview.html)An Android build system that automates several build processes. This automation means that many common build errors are less likely to occur. [More info](android-gradle-overview.html)  
See in [Glossary](Glossary.html#Gradle) uses to build your application. For more information, refer to [How Unity builds Android applications](how-unity-builds-android-applications.html).

## Configure an Android Library plug-in

Android Library plug-in is a dependency of a built-in module **unityLibrary**. You can change this default behavior. For example, you can configure an Android Library plug-in to depend on **unityLibrary** instead. To do this, use the following steps:

1. In the **Project** window, select the `.androidlib` plug-in to access the ****Inspector**A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
   See in [Glossary](Glossary.html#Inspector)** window.
2. In the **Select dependent module** section, select **None**.

   ![Android Library plug-in Inspector with the Select dependent module setting selected.](../uploads/Android/android-libproject-dependent-module.png)


   Android Library plug-in Inspector with the Select dependent module setting selected.
3. Add the following code in your plug-in’s build gradle **dependencies** scope:

   ```
   dependencies {
       ...
       implementation project(':unityLibrary')
       implementation fileTree(dir: project(':unityLibrary').getProjectDir().toString() + ('\\libs'), include: ['*.jar'])
   }
   ```

You also have the option to include Android Library plug-in as a dependency of the **launcher** or both **unityLibrary** and **launcher** built-in modules.

## Additional resources

* [Calling Java and Kotlin plug-in code from C# scripts](android-plugins-java-code-from-c-sharp.html)

Create an Android Library plug-in

Import an Android Archive plug-in

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)