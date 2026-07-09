* [Audio](Audio.html)
* [Audio Reference](AudioReference.html)
* [Audio filters](audio-filters.html)
* Use audio filters

Audio filters

Audio Low Pass Filter

# Use audio filters

You can modify the output of [Audio Source](class-AudioSource.html)A component which plays back an Audio Clip in the scene to an audio listener or through an audio mixer. [More info](class-AudioSource.html)  
See in [Glossary](Glossary.html#AudioSource) and [Audio Listener](class-AudioListener.html)A component that acts like a microphone, receiving sound from Audio Sources in the scene and outputting to the computer speakers. [More info](class-AudioListener.html)  
See in [Glossary](Glossary.html#AudioListener) components by applying **Audio Effects**Any effect that can modify the output of Audio Mixer components, such as filtering frequency ranges of a sound or applying reverb. [More info](class-AudioEffectMixer.html)  
See in [Glossary](Glossary.html#AudioEffect). These can filter the frequency ranges of the sound or apply reverb and other effects.

The effects are applied by adding effect components to the object with the Audio Source or Audio Listener. The ordering of the components is important, since it reflects the order in which the effects will be applied to the source audio. For example, in the image below, an Audio Listener is modified first by an **Audio Low Pass Filter**An audio filter that passes low frequencies of an Audio Source or all sound reaching an Audio Listener while removing frequencies higher than the Cutoff Frequency. [More info](class-AudioLowPassFilter.html)  
See in [Glossary](Glossary.html#AudioLowPassFilter) and then an Audio Chorus Filter.

![The Audio Inspector displays an Audio Listener component followed by the Audio Low Pass Filter and Audio Chorus Filter components that modify it.](../uploads/Main/FilterGraph1.png)


The Audio Inspector displays an Audio Listener component followed by the Audio Low Pass Filter and Audio Chorus Filter components that modify it.

To change the ordering of these and any other components, open a context menu in the **inspector**A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector) and select the *Move Up* or *Move Down* commands. Enabling or disabling an effect component determines whether it will be applied or not.

Though highly optimized, some filters are still CPU intensive. Audio CPU usage can monitored in the [profiler](Profiler.html)A window that helps you to optimize your game. It shows how much time is spent in the various areas of your game. For example, it can report the percentage of time spent rendering, animating, or in your game logic. [More info](Profiler.html)  
See in [Glossary](Glossary.html#Profiler) under the Audio Tab.

See the other pages in this section for further information about the specific filter types available.

AudioEffect

Audio filters

Audio Low Pass Filter

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)