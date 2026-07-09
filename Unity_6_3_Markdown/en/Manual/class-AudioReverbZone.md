* [Audio](Audio.html)
* [Audio Reference](AudioReference.html)
* Reverb Zones

Audio High Pass Simple Effect

Microphone

# Reverb Zones

[Switch to Scripting](../ScriptReference/AudioReverbZone.html "Go to AudioReverbZone page in the Scripting Reference")

**Reverb Zones** take an [Audio Clip](class-AudioClip.html)A container for audio data in Unity. Unity supports mono, stereo and multichannel audio assets (up to eight channels). Unity can import .aif, .wav, .mp3, and .ogg audio file format, and .xm, .mod, .it, and .s3m tracker module formats. [More info](class-AudioClip.html)  
See in [Glossary](Glossary.html#AudioClip) and distorts it depending where the **audio listener**A component that acts like a microphone, receiving sound from Audio Sources in the scene and outputting to the computer speakers. [More info](class-AudioListener.html)  
See in [Glossary](Glossary.html#AudioListener) is located inside the reverb zone. They are used when you want to gradually change from a point where there is no ambient effect to a place where there is one, for example when you are entering a cavern.

## Properties

![The AudioGroup Inspector displays the configurable properties of a Reverb Zone.](../uploads/Main/AudioReverbZone.png)


The AudioGroup Inspector displays the configurable properties of a Reverb Zone.

| ***Property:*** | ***Function:*** |
| --- | --- |
| **Min Distance** | Represents the radius of the inner circle in the **gizmo**A graphic overlay associated with a GameObject in a Scene, and displayed in the Scene View. Built-in scene tools such as the move tool are Gizmos, and you can create custom Gizmos using textures or scripting. Some Gizmos are only drawn when the GameObject is selected, while other Gizmos are drawn by the Editor regardless of which GameObjects are selected. [More info](GizmosMenu.html#GizmosIcons) See in [Glossary](Glossary.html#Gizmo), this determines the zone where there is a gradually reverb effect and a full reverb zone. |
| **Max Distance** | Represents the radius of the outer circle in the gizmo, this determines the zone where there is no effect and where the reverb starts to get applied gradually. |
| **Reverb Preset** | Determines the reverb effect that will be used by the reverb zone. |

Refer to [Audio Reverb Filter](class-AudioReverbFilter.html) for the rest of this component’s settings.

This diagram illustrates the properties of the reverb zone.

![How the sound works in a reverb zone](../uploads/Main/ReverbZoneExpl.png)


How the sound works in a reverb zone

## Hints

You can mix reverb zones to create combined effects.

AudioReverbZone

Audio High Pass Simple Effect

Microphone

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)