* [Audio](Audio.html)
* [Audio Reference](AudioReference.html)
* [Audio effects](audio-effects.html)
* Use audio effects

Audio effects

Audio Low Pass Effect

# Use audio effects

You can modify the output of [Audio Mixer](class-AudioMixer.html) components by applying **Audio Effects**. These can filter the frequency ranges of the sound or apply reverb and other effects.

## Add audio effects to your mixer

To add an audio effect to your Audio Mixer, in the component, select **Add Effect**. Unity shows you a list of the following effects you can add to your mixer:

* [LowPass](class-AudioLowPassEffect.html)
* [HighPass](class-AudioHighPassEffect.html)
* [Echo](class-AudioEchoEffect.html)
* [Flange](class-AudioFlangeEffect.html)
* [Distortion](class-AudioDistortionEffect.html)
* [Normalize](class-AudioNormalizeEffect.html)
* [Param EQ](class-AudioParamEQEffect.html)
* [Pitch Shifter](class-AudioPitchShifterEffect.html)
* [Chorus](class-AudioChorusEffect.html)
* [Compressor](class-AudioCompressor.html)
* [SFX Reverb](class-AudioReverbEffect.html)
* [LowPass Simple](class-AudioLowPassSimpleEffect.html)
* [HighPass Simple](class-AudioHighPassSimpleEffect.html)

## Profile your audio effects

Though highly optimized, some filters are still CPU intensive. You can monitor audio CPU usage in the [profiler](Profiler.html)A window that helps you to optimize your game. It shows how much time is spent in the various areas of your game. For example, it can report the percentage of time spent rendering, animating, or in your game logic. [More info](Profiler.html)  
See in [Glossary](Glossary.html#Profiler) under the **Audio** tab.

## Reorder audio effects

The ordering of the components is important, since it reflects the order in which the effects will be applied to the source audio. For example, in the image below, the Music section of an Audio Mixer is modified first by a Lowpass effect and then a compressor Effect, Flange Effect and so on.

![The Audio Mixer window displays Audio Groups called Master, Music, Reverb, and Effects. The Music group has multiple effect components, including a Compressor, Low Pass, High Pass, and Flange effects.](../uploads/Main/AudioMixer1.png)


The Audio Mixer window displays Audio Groups called Master, Music, Reverb, and Effects. The Music group has multiple effect components, including a Compressor, Low Pass, High Pass, and Flange effects.

To change the order of these and any other components, open a context menu in the **inspector**A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector) and select the *Move Up* or *Move Down* commands.

AudioEffectMixer

Audio effects

Audio Low Pass Effect

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)