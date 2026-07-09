* [Audio](Audio.html)
* [Audio Reference](AudioReference.html)
* [Audio effects](audio-effects.html)
* Audio Echo Effect

Audio High Pass Effect

Audio Flange Effect

# Audio Echo Effect

The **Audio Echo Effect** repeats a sound after a given **Delay**, attenuating the repetitions based on the **Decay Ratio**.

## Properties

![The AudioGroup Inspector displays the configurable properties of an Audio Echo Effect.](../uploads/Main/AudioEchoEffect.png)


The AudioGroup Inspector displays the configurable properties of an Audio Echo Effect.

| ***Property:*** | ***Function:*** |
| --- | --- |
| **Delay** | Echo delay in ms. 10 to 5000. Default = 500. |
| **Decay** | Echo decay per delay. 0 to 100%. 100% = No decay, 0% = total decay (ie simple 1 line delay). Default = 50%. |
| **Max channels** | Maximum number of supported channels from 0 to 16 (default = 0). |
| **Drymix** | Volume of original signal to pass to output. 0 to 100%. Default = 100%. |
| **Wetmix** | Volume of echo signal to pass to output. 0 to 100%. Default = 100%. |

## Details

The **Wetmix** value determines the amplitude of the filtered signal, where the **Drymix** determines the amplitude of the unfiltered sound output.

Hard surfaces reflects the propagation of sound. For example a large canyon can be made more convincing with the Audio Echo Filter.

AudioEchoEffect

Audio High Pass Effect

Audio Flange Effect

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)