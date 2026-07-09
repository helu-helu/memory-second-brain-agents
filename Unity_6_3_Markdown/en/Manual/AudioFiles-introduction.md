* [Audio](Audio.html)
* [Audio files](AudioFiles.html)
* Introduction to audio files

Audio files

Audio file compatibility

# Introduction to audio files

As with Meshes or Textures, the workflow for **Audio File** assets is designed to be smooth and simple. Unity can import almost every common file format, but there are a few details that are useful to be aware of when you work with audio files.

For an extensive description of the **compression**A method of storing data that reduces the amount of storage space it requires. See [Texture Compression](texture-choose-format-by-platform.html), [Animation Compression](class-AnimationClip.html#AssetProperties), [Audio Compression](class-AudioClip.html), [Build Compression](ReducingFilesize.html).  
See in [Glossary](Glossary.html#compression) formats and other options available for encoding audio data, refer to [Audio Clip](class-AudioClip.html)A container for audio data in Unity. Unity supports mono, stereo and multichannel audio assets (up to eight channels). Unity can import .aif, .wav, .mp3, and .ogg audio file format, and .xm, .mod, .it, and .s3m tracker module formats. [More info](class-AudioClip.html)  
See in [Glossary](Glossary.html#AudioClip).

## Audio data and Audio Clips

Unity audio data is separate from the actual Audio Clips. Audio data is the raw information about an audio file. It contains information such as length, channel count, sample rate, and compression format.

Audio Clips are assets that contain the audio data and processes the audio data for use with Unity Engine. Audio Clips contain the audio data used by [Audio Sources](class-AudioSource.html)A component which plays back an Audio Clip in the scene to an audio listener or through an audio mixer. [More info](class-AudioSource.html)  
See in [Glossary](Glossary.html#AudioSource).

## Alter the settings of your audio file

Use the settings in the [Audio Clip Import Settings](class-AudioClip.html) to determine how the clips will load at runtime. These settings let you decide which audio assets will stay in memory. This is ideal for frequent or unpredictable sounds like footsteps, weapons, or impacts.

For other assets, such as speech, background music, or ambient loops, you can set them to load on-demand or as the player progresses. This approach optimizes memory usage and improves performance.

## Use audio files in your scripts

Any audio file imported into Unity is available from **scripts**A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts) as an AudioClip instance. This provides a way for the game runtime of the audio system to access the encoded audio data. The game might access meta-information about the audio data via the AudioClip even before the actual audio data loads.

The import process extracts information such as length, channel count and sample rate from the encoded audio data and stores these details in the AudioClip. This information can be useful for automatic dialog or music sequencing systems, because the music engine can use the length to schedule music playback before the data loads. It also helps to reduce memory usage because it only keeps the audio clips in memory the application needs at a certain time.

For more information and code examples, refer to [the API documentation for AudioClip](https://docs.unity3d.com/ScriptReference/AudioClip.html).

## Additional resources

* [Audio files](AudioFiles.html)
* [Audio file type compatibility](AudioFiles-compatibility.html)
* [Audio file compression in Unity](AudioFiles-compression.html)
* [Import audio files into Unity](AudioFiles-import.html)
* [Audio Clip Import Settings reference](class-AudioClip.html)

Audio files

Audio file compatibility

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)