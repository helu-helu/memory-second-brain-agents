* [Visual effects](visual-effects.html)
* [Particle effects](ParticleSystems.html)
* [Particle System module component reference](ParticleSystemModules.html)
* Activate and access Particle System modules

Particle System module component reference

Main module reference

# Activate and access Particle System modules

The **Particle**A small, simple image or mesh that is emitted by a particle system. A particle system can display and move particles in great numbers to represent a fluid or amorphous entity. The effect of all the particles together creates the impression of the complete entity, such as smoke. [More info](class-ParticleSystem.html)  
See in [Glossary](Glossary.html#particle) System component has many properties, and for convenience, the **Inspector**A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector) organises them into collapsible sections called “modules”. These modules are documented in separate pages. See documentation on [Particle System Modules](ParticleSystemModules.html) to learn about each one.

To expand and collapse modules, click the bar that shows their name. Use the checkbox on the left to enable or disable the functionality of the properties in that module. For example, if you don’t want to vary the sizes of particles over their lifetime, uncheck the **Size over Lifetime** module.

The **Open Editor** button displays the options in a separate Editor window, which allows you to edit multiple systems at once.

The [Particle Effect panel](PartSysUsage.html) in the **Scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) View contains some additional options for previewing Particle Systems.

All Particle System modules are part of the [Particle System](class-ParticleSystem.html)A component that simulates fluid entities such as liquids, clouds and flames by generating and animating large numbers of small 2D images in the scene. [More info](class-ParticleSystem.html)  
See in [Glossary](Glossary.html#particlesystem) component.

To create a new Particle System and enable a module:

1. Click **GameObject** > **Effects** > **Particle System**.
2. In the Inspector, find the Particle System component.
3. In the Particle System component, find the fold-out for the module you want to apply.
4. To the left of the fold-out header, enable the checkbox.

# Access modules via the API

Modules are part of the Particle System component, so you can access it via the [ParticleSystem](../ScriptReference/ParticleSystem.html) class.

Particle System module component reference

Main module reference

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)