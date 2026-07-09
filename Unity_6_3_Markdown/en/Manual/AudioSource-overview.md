* [Audio](Audio.html)
* [Audio Reference](AudioReference.html)
* [Audio Source](class-AudioSource.html)
* Introduction to the Audio Source component

Audio Source

Audio Source component reference

# Introduction to the Audio Source component

Attach an **Audio Source** component to a **GameObject**The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) to control how and where sounds play in your **scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene).

Audio sources are components that let you integrate sound effects, music, commentary, and other audio features into your application.

They interact with other audio components in Unity that allow you to edit, enhance, and output sound in your scene, including:

* Audio Clips
* Audio Random Containers
* Audio Listeners
* Audio Mixers

This page covers how the audio source interacts with these audio components. For more information about the **Audio Source** component’s properties and how to set up the component, refer to [Audio Source component reference](AudioSource-reference.html) and [Set up an Audio Source component](AudioSource-create.html).

## Audio generators

The **Audio Source** component requires an audio generator to play sound in your scene. Audio generators are containers that hold the actual audio data, so you must assign one to the Audio Source so it has audio data to edit and play. For instructions, refer to [Assign an audio generator to your audio source](AudioSource-create.html#assign-an-audio-generator-to-your-audio-source).

The following Unity file types are audio generators:

* [Audio Clip](class-AudioClip.html)A container for audio data in Unity. Unity supports mono, stereo and multichannel audio assets (up to eight channels). Unity can import .aif, .wav, .mp3, and .ogg audio file format, and .xm, .mod, .it, and .s3m tracker module formats. [More info](class-AudioClip.html)  
  See in [Glossary](Glossary.html#AudioClip)
* [Audio Random Container](AudioRandomContainer.html)

Refer to those pages for more information about each type and for the audio file formats Unity supports.

## Output method of the audio source

In the **Audio Source** component, the **Output** property specifies where the audio source will send the audio signal in the audio processing pipeline.

This property accepts an **Audio Mixer Group**. The Audio Mixer is a tool that lets you post-process the audio with effects. You can then assign your Audio Mixer to the property to make sure your audio source applies your effects to the audio.

If you set the property to **None**, the sound will bypass your mixer and the audio will play without your effects. This is the default behavior.

Then, any **Audio Listener** components in the scene detects the audio from nearby audio sources, and outputs the audio to the user so they can hear it. Audio listeners are usually found on **cameras**A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera) in the scene, but you can also assign them to other objects.

For more information about these components, refer to [Audio Listener](class-AudioListener.html)A component that acts like a microphone, receiving sound from Audio Sources in the scene and outputting to the computer speakers. [More info](class-AudioListener.html)  
See in [Glossary](Glossary.html#AudioListener) and [Audio Mixer](AudioMixer.html).

## Configure your audio source

You can configure the audio source to play the clip as 2D, 3D, or as a mixture (*SpatialBlend*). The audio can be spread out between speakers (stereo to 7.1) (*Spread*) and morphed between 3D and 2D (*SpatialBlend*).

If you set **SpatialBlend** to `0.0f`, then Unity will treat the audio clip as a 2D sound. If you set it to `1.0f`, the clip is fully 3D. Anything in between is a blend of 2D and 3D.

Use falloff curves to control the spread over distance. Also, if the [listener](class-AudioListener.html) is within one or multiple [Reverb Zones](class-AudioReverbZone.html), this applies reverberation to the source. You can also apply individual filters to each audio source for an even richer audio experience. For more details, refer to [Audio Effects](class-AudioEffect.html)Any effect that can modify the output of Audio Mixer components, such as filtering frequency ranges of a sound or applying reverb. [More info](class-AudioEffectMixer.html)  
See in [Glossary](Glossary.html#AudioEffect).

For a list of Audio Source settings, refer to [Audio Source component reference](AudioSource-reference.html).

## API resources

The following is a list of useful API for AudioSource and its related properties.

* [AudioSource](../ScriptReference/AudioSource.html)
* [AudioClip](../ScriptReference/AudioClip.html)
* [AudioListener](../ScriptReference/AudioListener.html)
* [AudioMixer](../ScriptReference/Audio.AudioMixer.html)

## Additional resources

* [Audio Source](Class-AudioSource.html)A component which plays back an Audio Clip in the scene to an audio listener or through an audio mixer. [More info](class-AudioSource.html)  
  See in [Glossary](Glossary.html#AudioSource)
* [Introduction to the Audio Source component](AudioSource-overview.html)
* [Set up an Audio Source component](AudioSource-create.html)
* [Audio Source component reference](AudioSource-reference.html)

Audio Source

Audio Source component reference

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)