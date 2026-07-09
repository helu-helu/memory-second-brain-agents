* [Physics](PhysicsSection.html)
* [Built-in 3D physics](PhysicsOverview.html)
* [Rigidbody physics](rigidbody-physics-section.html)
* Constant Force component reference

Rigidbody component reference

Collision

# Constant Force component reference

[Switch to Scripting](../ScriptReference/ConstantForce.html "Go to ConstantForce page in the Scripting Reference")

****Constant Force**** adds constant forces to a [Rigidbody](rigidbody-physics-section.html)A component that allows a GameObject to be affected by simulated gravity and other forces. [More info](class-Rigidbody.html)  
See in [Glossary](Glossary.html#Rigidbody). This is useful for **GameObject**The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) movement that accelerates over time.

If you add a Constant Force component to a GameObject that does not have a Rigidbody, Unity automatically creates and adds a Rigidbody to the same GameObject.

For more details, see [Apply constant force to a Rigidbody](rigidbody-constant-force.html).

## Properties

For all values, a higher value produces a stronger force, which in turn produces a faster initial velocity.

| **Property:** | **Function:** |
| --- | --- |
| **Force** | Define the direction of the linear force. The XYZ vectors refer to the **scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html) See in [Glossary](Glossary.html#Scene)’s global axes. |
| **Relative Force** | Define the direction of the linear force. The XYZ vectors refer to the Rigidbody’s local axes. |
| **Torque** | Define the global axes that the Rigidbody rotates around. |
| **Relative Torque** | Define the local axes that the Rigidbody rotates around. |

ConstantForce

Rigidbody component reference

Collision

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)