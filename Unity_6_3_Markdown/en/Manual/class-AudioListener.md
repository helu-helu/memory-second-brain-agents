* [Audio](Audio.html)
* [Audio Reference](AudioReference.html)
* Audio Listener

Audio Clip Import Settings reference

Audio Source

# Audio Listener

[Switch to Scripting](../ScriptReference/AudioListener.html "Go to AudioListener page in the Scripting Reference")

The **Audio Listener** acts as a microphone-like device. It receives input from any given [Audio Source](class-AudioSource.html)A component which plays back an Audio Clip in the scene to an audio listener or through an audio mixer. [More info](class-AudioSource.html)  
See in [Glossary](Glossary.html#AudioSource) in the **scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) and plays sounds through the computer speakers. For most applications it makes the most sense to attach the listener to the Main [Camera](class-Camera.html)A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera). If an audio listener is within the boundaries of a [Reverb Zone](class-AudioReverbZone.html) reverberation is applied to all audible sounds in the scene. Furthermore, [Audio Effects](class-AudioEffect.html)Any effect that can modify the output of Audio Mixer components, such as filtering frequency ranges of a sound or applying reverb. [More info](class-AudioEffectMixer.html)  
See in [Glossary](Glossary.html#AudioEffect) can be applied to the listener and it will be applied to all audible sounds in the scene.

![](../uploads/Main/audio_listener_inspector.png)

## Properties

The Audio Listener has no properties. It simply must be added to work. It is always added to the Main Camera by default.

## Details

The Audio Listener works in conjunction with [Audio Sources](class-AudioSource.html), allowing you to create the aural experience for your games. When the Audio Listener is attached to a **GameObject**The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) in your scene, any Sources that are close enough to the Listener will be picked up and output to the computer’s speakers. Each scene can only have 1 Audio Listener to work properly.

If the Sources are 3D (see import settings in [Audio Clip](class-AudioClip.html)A container for audio data in Unity. Unity supports mono, stereo and multichannel audio assets (up to eight channels). Unity can import .aif, .wav, .mp3, and .ogg audio file format, and .xm, .mod, .it, and .s3m tracker module formats. [More info](class-AudioClip.html)  
See in [Glossary](Glossary.html#AudioClip)), the Listener will emulate position, velocity and orientation of the sound in the 3D world (You can tweak attenuation and 3D/2D behavior in great detail in [Audio Source](class-AudioSource.html)) . 2D will ignore any 3D processing. For example, if your character walks off a street into a night club, the night club’s music should probably be 2D, while the individual voices of characters in the club should be mono with their realistic positioning being handled by Unity.

You should attach the Audio Listener to either the Main Camera or to the GameObject that represents the player. Try both to find what suits your game best.

## Hints

* Each scene can only have one Audio Listener.
* You access the Project-wide Audio settings using the [Audio](class-AudioManager.html) window (main menu: **Edit** > **Project Settings**, then select the **Audio** category).
* View the [Audio Clip](class-AudioClip.html) Component page for more information about Mono vs Stereo sounds.

AudioListener

Audio Clip Import Settings reference

Audio Source

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)