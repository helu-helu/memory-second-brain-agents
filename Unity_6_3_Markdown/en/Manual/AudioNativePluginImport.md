* [Audio](Audio.html)
* [Native audio plug-in SDK](AudioMixerNativeAudioPlugin.html)
* Use your native audio DSP plug-in and GUI in Unity

Customize the GUI for your audio plug-in

Example native audio plug-ins included in the SDK

# Use your native audio DSP plug-in and GUI in Unity

Once you create your [audio DSP plug-in](AudioNativeDSPPlugin.html) and [customize your GUI to your liking](AudioNativeCustomGUI.html), you can build your file and import it into Unity.

## 1. Compile and build your plug-ins

You must implement your **plug-ins**A set of code created outside of Unity that creates functionality in Unity. There are two kinds of plug-ins you can use in Unity: Managed plug-ins (managed .NET assemblies created with tools like Visual Studio) and Native plug-ins (platform-specific native code libraries). [More info](./plug-ins.html)  
See in [Glossary](Glossary.html#plug-in) as a dynamic library for your preferred platform. Unlike with **scripts**A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts), any platform that you want to support must be able to compile this file, along with platform-specific optimizations.

For information about how to build your plug-in into a library file for each platform, refer to [Building plug-ins for desktop platforms](plug-ins-for-desktop.html).

## 2. Rename your audio plug-in DLL file

* Add the prefix “audioplugin” to the name of your DLL file (case insensitive). For example `audioplugin-myplugin.dll`

Unlike other **native plug-ins**A platform-specific native code library that is created outside of Unity for use in Unity. Allows you can access features like OS calls and third-party code libraries that would otherwise not be available to Unity. [More info](./plug-ins.html)  
See in [Glossary](Glossary.html#nativeplug-in), Unity needs to load audio plug-ins before it creates any mixer assets that might need effects from a plug-in. But Unity doesn’t do this by default.

Add the prefix “audioplugin” to the name of your DLL file so that the Unity Editor detects and adds your plug-in to a list of plug-ins that Unity automatically loads as the build starts.

## 3. Import your audio plug-in into Unity

Click and drag your plug-in library file into the Asset folder of your Unity project. Unity automatically installs your plug-in and it is ready to use.

## 4. Link the plug-in to a platform

Native audio plug-ins use the same scheme as other native or **managed plug-ins**A managed .NET assembly that is created with tools like Visual Studio for use in Unity. [More info](./plug-ins.html)  
See in [Glossary](Glossary.html#managedplug-in): You must use the plug-in importer **Inspector**A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector) to associate your plug-in with your preferred platforms. For more information, refer to [Plugin Inspector](plug-in-inspector.html).

## Additional resources

* [Audio Mixer](AudioMixer.html)
* [Native audio plug-in SDK](AudioMixerNativeAudioPlugin.html)
* [Audio Spatializer](AudioSpatializerSDK.html)A plug-in that changes the way audio is transmitted from an audio source into the surrounding space. It takes the source and regulates the gains of the left and right ear contributions based on the distance and angle between the AudioListener and the AudioSource. [More info](AudioSpatializerSDK.html)  
  See in [Glossary](Glossary.html#AudioSpatializer)
* [Building plug-ins for desktop platforms](plug-ins-for-desktop.html)

Customize the GUI for your audio plug-in

Example native audio plug-ins included in the SDK

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)