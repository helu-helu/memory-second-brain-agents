* [Visual effects](visual-effects.html)
* [Particle effects](ParticleSystems.html)
* [Configuring particles](configuring-particles.html)
* [Particle movement](particle-movement.html)
* Create particles that change velocity over time

Particle velocity

Particle rotation

# Create particles that change velocity over time

To create **particles**A small, simple image or mesh that is emitted by a particle system. A particle system can display and move particles in great numbers to represent a fluid or amorphous entity. The effect of all the particles together creates the impression of the complete entity, such as smoke. [More info](class-ParticleSystem.html)  
See in [Glossary](Glossary.html#particle) that drift in a particular direction, use the [Velocity over Lifetime](PartSysVelOverLifeModule.html) module’s Linear X, Y and Z curves.

To create effects with particles that spin around a center position, use the use the [Velocity over Lifetime](PartSysVelOverLifeModule.html) module’s **Orbital** velocity values. Additionally, you can propel particles towards or away from a center position using the **Radial** velocity values. You can define a custom center of rotation for each particle by using the **Offset** value.

You can also use the [Velocity over Lifetime](PartSysVelOverLifeModule.html) module to adjust the speed of the particles in the **Particle System**A component that simulates fluid entities such as liquids, clouds and flames by generating and animating large numbers of small 2D images in the scene. [More info](class-ParticleSystem.html)  
See in [Glossary](Glossary.html#particlesystem) without affecting their direction, by leaving all the above values at zero and only modifying the **Speed Modifier** value.

Particle velocity

Particle rotation

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)