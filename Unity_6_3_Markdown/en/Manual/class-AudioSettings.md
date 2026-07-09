* [Audio](Audio.html)
* [Audio Reference](AudioReference.html)
* Audio Settings

Microphone

Video and cutscenes

# Audio Settings

[Switch to Scripting](../ScriptReference/AudioSettings.html "Go to AudioSettings page in the Scripting Reference")

The AudioSettings class contains various bits of global information relating to the sound system, but most importantly it contains API that allows resetting the audio system at runtime in order to change settings such as speaker mode, sample rate (if supported by the platform), DSP buffer size and real/virtual voice counts.

Many of these settings can also be configured in the Audio section of the **project settings**A broad collection of settings which allow you to configure how Physics, Audio, Networking, Graphics, Input and many other areas of your project behave. [More info](comp-ManagerGroup.html)  
See in [Glossary](Glossary.html#ProjectSettings). When changed these settings will apply both to the editor and define the initial state of the game while changes performed using the AudioSettings API only apply to the runtime of the game and are reset back to the state defined in the project settings when stopping the game in the editor.

The game may provide a sound options menu in which the user can change the sound settings or changes may come from outside in response to a device change such as plugging in an external audio input/output device or even an HDMI monitor which may also act as an audio device. The AudioConfiguration AudioSettings.GetConfiguration() / bool AudioSettings.Reset(AudioConfiguration config) API can read and apply global changes to the current sound system configuration and essentially replaces the AudioSettings.SetDSPBufferSize(…) function and the AudioSettings.outputSampleRate, AudioSettings.speakerMode which had the side effect of reinitializing the whole audio system when the properties were modified.

The API defines the AudioSettings.OnAudioConfigurationChanged(bool device) to set up a callback through which **scripts**A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts) can be notified about audio configuration changes. These can either be caused by actual device changes or by a configuration initiated by script.

It is important to note that whenever runtime modifications of the global audio system configuration are performed all audio objects have to be reloaded. This works for disk-based AudioClip assets and audio mixers, but any AudioClips generated or modified by scripts are lost and have to be recreated. Likewise any play state is lost too, so these need to be regenerated in the AudioSettings.OnAudioConfigurationChanged(…) callback.

For details and examples see the scripting API reference.

AudioSettings

Microphone

Video and cutscenes

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)