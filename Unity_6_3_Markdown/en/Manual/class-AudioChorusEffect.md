* [Audio](Audio.html)
* [Audio Reference](AudioReference.html)
* [Audio effects](audio-effects.html)
* Audio Chorus Effect

Audio Pitch Shifter Effect

Audio Compressor Effect

# Audio Chorus Effect

The **Audio Chorus Effect** takes an [Audio Mixer](class-AudioMixer.html) group output and processes it creating a chorus effect.

## Properties

![The AudioGroup Inspector displays the configurable properties of an Audio Chorus Effect.](../uploads/Main/AudioChorusEffect.png)


The AudioGroup Inspector displays the configurable properties of an Audio Chorus Effect.

| ***Property:*** | ***Function:*** |
| --- | --- |
| **Dry mix**An audio setting that allows you to set the volume of the original signal to pass to output. See in [Glossary](Glossary.html#drymix) | Volume of original signal to pass to output. 0.0 to 1.0. Default = 0.5. |
| **Wet mix tap 1** | Volume of 1st chorus tap. 0.0 to 1.0. Default = 0.5. |
| **Wet mix tap 2** | Volume of 2nd chorus tap. This tap is 90 degrees out of phase of the first tap. 0.0 to 1.0. Default = 0.5. |
| **Wet mix tap 3** | Volume of 3rd chorus tap. This tap is 90 degrees out of phase of the second tap. 0.0 to 1.0. Default = 0.5. |
| **Delay** | The LFO’s delay in ms. 0.1 to 100.0. Default = 40.0 ms |
| **Rate** | The LFO’s modulation rate in Hz. 0.0 to 20.0. Default = 0.8 Hz. |
| **Depth** | Chorus modulation depth. 0.0 to 1.0. Default = 0.03. |
| **Feedback** | Chorus feedback. Controls how much of the wet signal gets fed back into the filter’s buffer. 0.0 to 1.0. Default = 0.0. |

## Details

The chorus effect modulates the original sound by a sinusoid low frequency oscillator (LFO). The output sounds like there are multiple sources emitting the same sound with slight variations - resembling a choir.

You can tweak the chorus filter to create a flanger effect by lowering the feedback and decreasing the delay, as the flanger is a variant of the chorus.

Creating a simple, dry echo is done by setting **Rate** and **Depth** to 0 and tweaking the mixes and **Delay**

AudioChorusEffect

Audio Pitch Shifter Effect

Audio Compressor Effect

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)