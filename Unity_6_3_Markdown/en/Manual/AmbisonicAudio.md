* [Audio](Audio.html)
* [Ambisonic audio](audio-ambisonic.html)
* Introduction to ambisonic audio

Ambisonic audio

Develop an ambisonic audio decoder

# Introduction to ambisonic audio

Ambisonics are a type of audio that provide a representation of sound that can completely surround a listener. They can provide an audio **skybox**A special type of Material used to represent skies. Usually six-sided. [More info](sky-landing.html)  
See in [Glossary](Glossary.html#Skybox) for distant ambient sounds, and are particularly useful for 360-degree videos and applications.

Ambisonics are stored in a multi-channel format. Instead of mapping each channel to a specific speaker, ambisonics represent the soundfield in a more general way. You can rotate the soundfield based on the listener’s orientation (such as the user’s head rotation in VR). You can also decode the soundfield into a format that matches the speaker setup.

## Selecting an ambisonic audio decoder

To select an ambisonic audio decoder in your project, open your project’s [Audio](class-AudioManager.html) settings (menu: **Edit** > **Project Settings** > **Audio**). Select an **Ambisonic Decoder Plugin** from the list of available decoders in the project.

![Ambisonic options in the Audio settings](../uploads/Main/AmbisonicAudioSettings.png)


Ambisonic options in the Audio settings

There are no built-in decoders included with Unity, but you can do one of the following options:

* You can create your own ambisonic audio decoder **plug-in**A set of code created outside of Unity that creates functionality in Unity. There are two kinds of plug-ins you can use in Unity: Managed plug-ins (managed .NET assemblies created with tools like Visual Studio) and Native plug-ins (platform-specific native code libraries). [More info](./plug-ins.html)  
  See in [Glossary](Glossary.html#plug-in). For more information, refer to [Ambisonic Audio Decoder](AudioDevelopAmbisonicDecoder.html).
* Use external decoders. For instance, some **VR**Virtual Reality [More info](VROverview.html)  
  See in [Glossary](Glossary.html#VR) hardware manufacturers provide them in their audio SDKs for Unity. Check your target platform manufacturer’s documentation to learn if this is available for your project.

## Importing an ambisonic audio clip

To import an ambisonic **audio clip**A container for audio data in Unity. Unity supports mono, stereo and multichannel audio assets (up to eight channels). Unity can import .aif, .wav, .mp3, and .ogg audio file format, and .xm, .mod, .it, and .s3m tracker module formats. [More info](class-AudioClip.html)  
See in [Glossary](Glossary.html#AudioClip), import a multi-channel B-format WAV file with ACN component ordering, and SN3D normalization. In the **Inspector**A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector) window for the audio clip, enable **Ambisonic**.

![The Ambisonic option in the audio clip inspector](../uploads/Main/AmbisonicAudioClipInspector.png)


The Ambisonic option in the audio clip inspector

## Playing the ambisonic audio clip through an Audio Source

To play an ambisonic audio clip through an **Audio Source**A component which plays back an Audio Clip in the scene to an audio listener or through an audio mixer. [More info](class-AudioSource.html)  
See in [Glossary](Glossary.html#AudioSource):

* Assign the WAV file as an **Audio Clip** on an Audio Source.
* Disable the **Spatialize** option. When you play an ambisonic audio clip, it is automatically decoded through the project’s selected ambisonic audio decoder. The decoder converts the clip from ambisonic format to the project’s selected speaker format. It also already handles spatialization as a part of this decoding operation, based on the orientation of the audio source and **audio listener**A component that acts like a microphone, receiving sound from Audio Sources in the scene and outputting to the computer speakers. [More info](class-AudioListener.html)  
  See in [Glossary](Glossary.html#AudioListener).

When Unity plays an ambisonic audio clip, it decompresses the file, if necessary, then decodes it to convert it to the project’s selected speaker mode. It then applies the Audio Source’s effects.

**Note:** Reverb zones are disabled for ambisonic audio clips.

Ambisonic audio

Develop an ambisonic audio decoder

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)