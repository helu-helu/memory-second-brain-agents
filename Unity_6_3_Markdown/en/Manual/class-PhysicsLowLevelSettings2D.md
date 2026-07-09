* [2D game development](Unity2D.html)
* [2D physics with the LowLevelPhysics2D API](2d-physics-api/2d-physics-api-landing.html)
* [Reference for the LowLevelPhysics2D API](2d-physics-api/2d-physics-api-reference.html)
* Physics Low Level Settings 2D asset Inspector window reference

Wheel joint definition reference for the LowLevelPhysics2D API

2D game development in URP

# Physics Low Level Settings 2D asset Inspector window reference

**Note**: This documentation is about writing C# scripts using the `LowLevelPhysics2D` API. To use 2D physics in the Unity Editor using components like the Rigidbody 2D component, refer to [2D physics](../2d-physics/2d-physics) instead.

Explore the properties and settings you can use to configure the defaults and global behaviour of the `LowLevelPhysics2D` API. For more information, refer to [Configure global 2D physics settings](2d-physics-api/2d-physics-api-global-settings.html).

## Layers

The properties in this section configure the layers Unity uses to detect **collision**A collision occurs when the physics engine detects that the colliders of two GameObjects make contact or overlap, when at least one has a Rigidbody component and is in motion. [More info](CollidersOverview.html)  
See in [Glossary](Glossary.html#collision). For more information, refer to [Configure collisions between LowLevelPhysics2D API objects](2d-physics-api/2d-physics-api-collisions-enable.html).

| **Property** | **Description** |
| --- | --- |
| **Physics Layer Names** | Sets the names of the 64 layers the `PhysicsMask` API uses if you enable **Use Full Layers**. By default, the first layer has the name **Default** and the other layers have no name. |
| **Use Full Layers** | Enables the `PhysicsMask` API using the 64 layers listed under **Physics Layer Names**. If you disable this property, the `PhysicsMask` API uses the 32 [GameObject layers](Layers.html) instead. |

## Default Definitions

The properties in this section set the default values when you create a new definition object. For the individual sections, refer to the following:

* [World definition reference](2d-physics-api/2d-physics-api-reference-world.html)
* [Body definition reference](2d-physics-api/2d-physics-api-reference-body.html)
* [Shape definition reference](2d-physics-api/2d-physics-api-reference-shape.html)
* [Chain definition reference](2d-physics-api/2d-physics-api-reference-chain.html)
* [Distance joint definition reference](2d-physics-api/2d-physics-api-reference-joint-distance.html)
* [Fixed joint definition reference](2d-physics-api/2d-physics-api-reference-joint-fixed.html)
* [Hinge joint definition reference](2d-physics-api/2d-physics-api-reference-joint-hinge.html)
* [Relative joint definition reference](2d-physics-api/2d-physics-api-reference-joint-relative.html)
* [Slider joint definition reference](2d-physics-api/2d-physics-api-reference-joint-slider.html)
* [Wheel joint definition reference](2d-physics-api/2d-physics-api-reference-joint-wheel.html)

## Globals

| **Property** | **Description** |
| --- | --- |
| **Concurrent Simulations** | Sets the number of physics simulations that can run at the same time. The default is 2. |
| **Length Units Per Meter** | Sets the number of **Unity units**The unit size used in Unity projects. By default, 1 Unity unit is 1 meter. To use a different scale, set the Scale Factor in the Import Settings when importing assets. See in [Glossary](Glossary.html#Unityunit) that correspond to one meter in the physics simulation. The default is 1. |
| **Draw In Build** | Draws the debug visualization in a built application. For more information, refer to [Draw a debug visualization of objects](2d-physics-api/2d-physics-api-debug-drawing.html). |
| **Bypass Low Level** | Disables the `LowLevelPhysics2D` API physics system. |

## Additional resources

* [Configure global 2D physics settings](2d-physics-api/2d-physics-api-global-settings.html)
* [Configure 2D physics properties using a definition](2d-physics-api/2d-physics-api-definitions.html)

Wheel joint definition reference for the LowLevelPhysics2D API

2D game development in URP

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)