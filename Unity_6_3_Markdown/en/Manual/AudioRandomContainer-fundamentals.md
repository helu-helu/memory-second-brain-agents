* [Audio](Audio.html)
* [Audio playlist randomization](AudioRandomContainer.html)
* Audio Random Container fundamentals

Audio Random Container reference

Create a randomized playlist with the Audio Random Container

# Audio Random Container fundamentals

An Audio Random Container is an object that lets you create audio playlists for your **scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) and apply rules to determine when and how the clips play. For example, you can add randomization, looping, and timed playback to your audio clips. This is an excellent way to create varied and dynamic audio playback for music and sound effects like footsteps, weapon hits, and background music.

The audio cycle and AudioSource API exceptions are important concepts to know before you use an Audio Random Container.

## Audio cycle

An audio cycle is the full **Audio Clips** list length. If the list has three audio clips, an audio cycle is three clips.

### AudioSource API

Use the [AudioSource API](../ScriptReference/AudioSource.html) to start, pause, and stop an Audio Random Container. This is similar to when you use the AudioSource API to play, pause, and stop an Audio Clip, but with the following exceptions:

* [AudioSource.isPlaying](../ScriptReference/AudioSource.isPlaying.html) returns true when the Audio Random Container plays an audio clip through an **audio source**A component which plays back an Audio Clip in the scene to an audio listener or through an audio mixer. [More info](class-AudioSource.html)  
  See in [Glossary](Glossary.html#AudioSource).
* [AudioSource.Play](../ScriptReference/AudioSource.Play.html) behaves differently depending on whether you set the Audio Random Container to **Manual** or **Automatic**.
  + When set to **Manual**, `AudioSource.Play` plays an audio clip in the **Audio Clips** list based on the container’s **Playback Mode**. For example, if the **Playback Mode** is set to **Random**, it plays a random audio clip in the list.

## Additional resources

* [Audio playlist randomization](AudioRandomContainer.html)
* [Audio Clips](class-AudioClip.html)A container for audio data in Unity. Unity supports mono, stereo and multichannel audio assets (up to eight channels). Unity can import .aif, .wav, .mp3, and .ogg audio file format, and .xm, .mod, .it, and .s3m tracker module formats. [More info](class-AudioClip.html)  
  See in [Glossary](Glossary.html#AudioClip)
* [AudioSource.Play](../ScriptReference/AudioSource.Play.html)
* [Audio Source priority](class-AudioSource.html)
* [Audio Mixer](AudioMixer.html)

Audio Random Container reference

Create a randomized playlist with the Audio Random Container

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)