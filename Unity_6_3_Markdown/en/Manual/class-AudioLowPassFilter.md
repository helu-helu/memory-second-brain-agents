* [Audio](Audio.html)
* [Audio Reference](AudioReference.html)
* [Audio filters](audio-filters.html)
* Audio Low Pass Filter

Use audio filters

Audio High Pass Filter

# Audio Low Pass Filter

[Switch to Scripting](../ScriptReference/AudioLowPassFilter.html "Go to AudioLowPassFilter page in the Scripting Reference")

The **Audio Low Pass Filter** passes low frequencies of an [AudioSource](class-AudioSource.html) or all sound reaching an [AudioListener](class-AudioListener.html) while removing frequencies higher than the **Cutoff Frequency**.

## Properties

![The AudioGroup Inspector displays the configurable properties of an Audio Low Pass Filter.](../uploads/Main/AudioLowPassFilter.png)


The AudioGroup Inspector displays the configurable properties of an Audio Low Pass Filter.

| ***Property:*** | ***Function:*** |
| --- | --- |
| **Cutoff Frequency** | Lowpass cutoff frequency in Hertz (range 0.0 to 22000.0, default = 5000.0). |
| **Lowpass Resonance Q** | Lowpass resonance quality value (range 1.0 to 10.0, default = 1.0). |

## Details

The **Lowpass Resonance Q** (short for Lowpass Resonance Quality Factor) determines how much the filter’s self-resonance is dampened. Higher lowpass resonance quality indicates a lower rate of energy loss, that is the oscillations die out more slowly.

The **Audio Low Pass Filter** has a Rolloff curve associated with it, making it possible to set **Cutoff Frequency** over distance between the AudioSource and the AudioListener.

Sounds propagate very differently given the environment. For example, to compliment a visual fog effect add a subtle low-pass to the **Audio Listener**A component that acts like a microphone, receiving sound from Audio Sources in the scene and outputting to the computer speakers. [More info](class-AudioListener.html)  
See in [Glossary](Glossary.html#AudioListener). The high frequencies of a sound being emitted from behind a door will be filtered out by the door and so won’t reach the listener. To simulate this, simply change the Cutoff Frequency when opening the door.

AudioLowPassFilter

Use audio filters

Audio High Pass Filter

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)