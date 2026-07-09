* [Audio](Audio.html)
* [Audio Reference](AudioReference.html)
* [Audio effects](audio-effects.html)
* Audio SFX Reverb Effect

Audio Compressor Effect

Audio Low Pass Simple Effect

# Audio SFX Reverb Effect

The **SFX Reverb Effect** takes the output of an [Audio Mixer](class-AudioMixer.html) group and distorts it to create a custom reverb effect.

## Properties

![The AudioGroup Inspector displays the configurable properties of an SFX Reverb Effect.](../uploads/Main/AudioSFXReverbEffect.png)


The AudioGroup Inspector displays the configurable properties of an SFX Reverb Effect.

| ***Property:*** | ***Function:*** |
| --- | --- |
| **Wet** | This setting only shows if you select the gear icon in the SFX Reverb effect and enable **Allow Wet Mixing**. Use this to control the volume of the processed signal that passes through this effect. Output in mB. –10000.0 to 0.0. Default is 0 mB. |
| **Dry Level**An audio setting that allows you to set the mix level of unprocessed signal in output in mB. See in [Glossary](Glossary.html#drylevel) | Control the volume of the unprocessed, original signal that passes through this effect (output in mB). Ranges from –10000.0 to 0.0. Default is 0 mB. |
| **Room** | Room effect level at low frequencies in mB. Use to control the general size and reflections level of the delay. Use **Room HF** and **Room LF** variants to control the respective frequency parts. Ranges from –10000.0 to 0.0. Default is –10000.0 mB. |
| **Room HF** | Make the sound simulate the acoustics of a room. Control the level of reverb for high frequencies in mB. Lower (more negative) values damp highs, which makes the room sound warmer. Useful for rooms with soft furnishings like curtains, carpets, and fabrics. Higher values let more high-frequency sounds, which makes the room sound brighter and more reflective. Use for rooms with reflective or glossy materials like tiled walls and floors. Ranges from –10000.0 to 0.0. Default is 0.0 mB. |
| **Decay Time** | Controls how quickly low frequencies last in seconds after the source stops. Higher values keep lows ringing longer, which can be useful for large spaces, and boomy sounds. Lower values shorten low-frequency sounds, which you can use for smaller rooms, and to reduce boom. Ranges from 0.1 to 20.0. Default is 1.0. |
| **Decay HF Ratio** | Decay HF Ratio : High-frequency to low-frequency decay time ratio. Ranges from 0.1 to 2.0. Default is 0.5. |
| **Reflections** | Set the level of early reflections relative to the overall room effect (in mB). Higher values add stronger, more present early echoes. Set high for reflective rooms (tile, glass) where you want a clear sense of space, percussive sources (snare, claps) that need snap and presence, or close, intimate room feel. Set lower for natural ambience for dialogue, reduce harshness or flutter, and controlled mixes with less echo. Lower values make the space sound drier and less reflective. Range: –10000.0 to 1000.0 mB. Default: –10000.0 mB. |
| **Reflect Delay** | Early reflections delay time relative to room effect in mB. Ranges from –10000.0 to 2000.0. Default is 0.02. |
| **Reverb** | Late reverberation level relative to room effect in mB. Ranges from –10000.0 to 2000.0. Default is 0.0 mB. Higher = stronger, more enveloping tail. Lower = drier, less reflective mix. |
| **Reverb Delay** | Late reverberation delay time relative to first reflection in seconds. Ranges from 0.0 to 0.1. Default is 0.04 s. |
| **Diffusion** | Control echo density (percent). Set higher for a smoother, louder echoes. Set lower for more discrete echoes or grain. Ranges from 0.0 to 100.0. Default is 100.0%. |
| **Density** | Reverberation density (modal density) in percent. Use low modal density for distinct echoes or a grainy, fluttery tail. Use high modal density so the tail sounds smooth and continuous. Ranges from 0.0 to 100.0. Default is 100.0%. |
| **HFReference** | The frequency in Hz above which high‑frequency damping or brightness controls take effect. Reference high frequency in Hz. Ranges from 20.0 to 20000.0. Default is 5000.0 Hz. |
| **Room LF** | Make the sound simulate the acoustics of a room. Control the level of reverb for low frequencies in mB. Higher values emphasize bass in the reverb, which makes the space feel bigger or boomier. Useful for empty or huge rooms. Lower values reduce low-frequency buildup for a tighter, less boomy ambience. Room effect level at low frequencies in mB. Ranges from –10000.0 to 0.0. Default is –10000.0 mB. |
| **LFReference** | The frequency in Hz around which low‑frequency emphasis or damping controls take effect. |
| Use lower values to allow deeper bass. Use higher values to shift shaping toward mid‑bass. Ranges from 20.0 to 1000.0. Default is 250.0 Hz. |

Refer to [Windows App Development documentation](https://learn.microsoft.com/en-us/windows/win32/api/xaudio2fx/ns-xaudio2fx-xaudio2fx_reverb_i3dl2_parameters) for more information.

AudioReverbEffect

Audio Compressor Effect

Audio Low Pass Simple Effect

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)