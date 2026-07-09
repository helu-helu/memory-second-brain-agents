* [Audio](Audio.html)
* [Audio Reference](AudioReference.html)
* [Audio filters](audio-filters.html)
* Audio Echo Filter

Audio High Pass Filter

Audio Distortion Filter

# Audio Echo Filter

[Switch to Scripting](../ScriptReference/AudioEchoFilter.html "Go to AudioEchoFilter page in the Scripting Reference")

The **Audio Echo Filter** repeats a sound after a given **Delay**, attenuating the repetitions based on the **Decay Ratio**.

## Properties

![The AudioGroup Inspector displays the configurable properties of an Audio Echo Filter.](../uploads/Main/AudioEchoFilter.png)


The AudioGroup Inspector displays the configurable properties of an Audio Echo Filter.

| ***Property:*** | ***Function:*** |
| --- | --- |
| **Delay** | Echo delay in ms. 10 to 5000. Default = 500. |
| **Decay Ratio** | Echo decay per delay. 0 to 1. 1.0 = No decay, 0.0 = total decay (ie simple 1 line delay). Default = 0.5.L |
| **Wet Mix** | Volume of echo signal to pass to output. 0.0 to 1.0. Default = 1.0. |
| **Dry Mix**An audio setting that allows you to set the volume of the original signal to pass to output. See in [Glossary](Glossary.html#drymix) | Volume of original signal to pass to output. 0.0 to 1.0. Default = 1.0. |

## Details

The **Wet Mix** value determines the amplitude of the filtered signal, where the **Dry Mix** determines the amplitude of the unfiltered sound output.

Hard surfaces reflects the propagation of sound. For example a large canyon can be made more convincing with the Audio Echo Filter.

Sound propagates slower than light - we all know that from lightning and thunder. To simulate this, add an Audio Echo Filter to an event sound, set the Wet Mix to 0.0 and modulate the Delay to the distance between [AudioSource](class-AudioSource.html) and [AudioListener](class-AudioListener.html).

AudioEchoFilter

Audio High Pass Filter

Audio Distortion Filter

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)