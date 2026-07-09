* [Materials and shaders](materials-and-shaders.html)
* [Prebuilt materials and shaders](built-in-materials-and-shaders.html)
* [Prebuilt shaders in the Built-In Render Pipeline](shader-built-in-birp.html)
* [Particle shaders in the Built-In Render Pipeline](shader-StandardParticleShadersLanding.html)
* [Custom data streams in Particle Systems in the Built-In Render Pipeline](custom-data-streams-particle-systems.html)
* Define custom data formats for particles in the Built-In Render Pipeline

Example of Particle System Surface Shader custom vertex streams in the Built-In Render Pipeline

Particle System optimization in the Built-In Render Pipeline

# Define custom data formats for particles in the Built-In Render Pipeline

The [Custom Data](PartSysCustomDataModule.html) module allows you to define custom data formats in the Editor to be attached to **particles**A small, simple image or mesh that is emitted by a particle system. A particle system can display and move particles in great numbers to represent a fluid or amorphous entity. The effect of all the particles together creates the impression of the complete entity, such as smoke. [More info](class-ParticleSystem.html)  
See in [Glossary](Glossary.html#particle). You can also set this in a script. See documentation on [Particle System vertex streams](PartSysVertexStreams.html) for more information on how to set custom data from a script and feed that data into your **shaders**A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#shader).

Data can be in the form of a **Vector**, with up to 4 [MinMaxCurve](../ScriptReference/ParticleSystem.MinMaxCurve.html) components, or a **Color**, which is an HDR-enabled [MinMaxGradient](../ScriptReference/ParticleSystem.MinMaxGradient.html). Use this data to drive custom logic in your **scripts**A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts) and Shaders.

The default labels for each curve/gradient can be customized by clicking on them and typing in a contextual name. When passing custom data to shaders, it is useful to know how that data is used inside the shader. For example, a curve may be used for custom alpha testing, or a gradient may be used to add a secondary color to particles. By editing the labels, it is simple to keep a record in the UI of the purpose of each custom data entry.

Example of Particle System Surface Shader custom vertex streams in the Built-In Render Pipeline

Particle System optimization in the Built-In Render Pipeline

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)