* [Audio](Audio.html)
* Native audio plug-in SDK

Overview of Usage and API

Develop a native DSP audio plug-in

# Native audio plug-in SDK

The Unity native audio **plug-in**A set of code created outside of Unity that creates functionality in Unity. There are two kinds of plug-ins you can use in Unity: Managed plug-ins (managed .NET assemblies created with tools like Visual Studio) and Native plug-ins (platform-specific native code libraries). [More info](./plug-ins.html)  
See in [Glossary](Glossary.html#plug-in) SDK lets you develop custom audio plug-ins for Unity. You can use this SDK to extend the audio capabilities of Unity and create advanced audio processing solutions tailored to your project’s needs. Examples of custom audio plug-ins you can create include **audio effects**Any effect that can modify the output of Audio Mixer components, such as filtering frequency ranges of a sound or applying reverb. [More info](class-AudioEffectMixer.html)  
See in [Glossary](Glossary.html#AudioEffect) and **audio spatializers**A plug-in that changes the way audio is transmitted from an audio source into the surrounding space. It takes the source and regulates the gains of the left and right ear contributions based on the distance and angle between the AudioListener and the AudioSource. [More info](AudioSpatializerSDK.html)  
See in [Glossary](Glossary.html#AudioSpatializer).

The native audio plug-in system consists of two parts:

* The native audio Digital Signal Processing (DSP) plug-in
* The managed graphical user interface (GUI)

Refer to the following pages to learn more about how to create an audio plug-in, customize the plug-in’s GUI, and access useful examples.

| **Topic** | **Description** |
| --- | --- |
| **[Develop a native audio DSP plug-in for Unity](AudioNativeDSPPlugin.html)** | Learn how to create your own native DSP plug-in. |
| **[Customize the Unity GUI for your audio plug-in](AudioNativeCustomGUI.html)** | Learn how to customize the GUI of your audio plug-in. |
| **[Import your audio plug-in and GUI to Unity](AudioNativePluginImport.html)** | Learn how to prepare your plug-in and GUI for Unity and import them. |
| **[Example plug-ins](AudioNativePluginExamples.html)** | Example DSP plug-ins with and without GUI customization. |
| **[Audio Spatializer SDK](AudioSpatializerSDK.html)** | Change the way your application transmits audio from an **audio source**A component which plays back an Audio Clip in the scene to an audio listener or through an audio mixer. [More info](class-AudioSource.html) See in [Glossary](Glossary.html#AudioSource) into the surrounding space. |

## Important files your DSP and GUI code uses

The `AudioPluginInterface.h` file has the necessary structures, types, and function declarations required to create a custom audio plug-in.

Both native DSP and GUI DLLs can contain multiple plug-ins. To add multiple plug-in effects within the same DLL, Unity provides additional code to handle the effect definition and parameter registration in a unified manner:

* `AudioPluginUtil.h`
* `AudioPluginUtil.cpp`

If you want your DLLs to contain multiple effects, include `AudioPluginUtil.h` in your code.

## Additional resources

* [Audio Mixer](AudioMixer.html)
* [Audio Spatializer SDK](AudioSpatializerSDK.html)
* [Ambisonic Audio](AmbisonicAudio.html)

---

Overview of Usage and API

Develop a native DSP audio plug-in

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)