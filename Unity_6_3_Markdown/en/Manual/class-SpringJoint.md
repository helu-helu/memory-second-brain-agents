* [Physics](PhysicsSection.html)
* [Built-in 3D physics](PhysicsOverview.html)
* [Joints](joints-section.html)
* Spring Joint component reference

Hinge Joint component reference

Create a configurable joint

# Spring Joint component reference

[Switch to Scripting](../ScriptReference/SpringJoint.html "Go to SpringJoint page in the Scripting Reference")

The **Spring **Joint**A physics component allowing a dynamic connection between Rigidbody components, usually allowing some degree of movement such as a hinge. [More info](Joints.html)  
See in [Glossary](Glossary.html#joint)** joins two [Rigidbodies](class-Rigidbody.html)A component that allows a GameObject to be affected by simulated gravity and other forces. [More info](class-Rigidbody.html)  
See in [Glossary](Glossary.html#Rigidbody) together but allows the distance between them to change as though they were connected by a spring. The spring acts like a piece of elastic that tries to pull the two anchor points together to the same position.

## Properties

| **Property:** | **Function:** |
| --- | --- |
| **Connected Body** | The Rigidbody object that the object with the spring joint is connected to. If no object is assigned then the spring is connected to a fixed point in space.   You can use connected bodies to create chains of multiple Hinge Joints. Add a joint to each link in the chain, and attach the next link as the **Connected Body**. |
| **Connected Articulation Body** | Optional reference to the ArticulationBody that the joint is dependent upon. If not set, the joint connects to the world. |
| **Anchor** | The point in the object’s local space at which the joint is attached. |
| **Axis** | The direction of the axis around which the body rotates. The direction is defined in local space. |
| **Auto Configure Connected Anchor** | When enabled, Unity calculates the position of the connected anchor points automatically. Unity configures the anchor points to maintain the starting distance between them (that is, the distance you set in the scene view while positioning the objects). |
| **Connected Anchor** | The point in the connected object’s local space at which the joint is attached. |
| **Spring** | Determines the force per unit of distance that the joint uses. The **Spring Joint** acts like a piece of elastic that tries to pull the two anchor points together to the same position. The strength of the pull is proportional to the current distance between the points. |
| **Damper** | Amount that the spring is reduced when active. To prevent the spring from oscillating endlessly, set a **Damper** value that reduces the spring force in proportion to the relative speed between the two objects. The higher the value, the more quickly the oscillation decreases. |
| **Min Distance** | Set a minimum distance range over which the spring does not apply any force. If the distance between the objects exceeds this distance, the Spring Joint applies force to bring the objects back together. |
| **Max Distance** | Set a maximum distance range over which the spring does not apply any force. If the distance between the objects exceeds this distance, the Spring Joint applies force to bring the objects back together. |
| **Tolerance** | Changes error tolerance. Allows the spring to have a different rest length. |
| **Break Force** | The force that needs to be applied for this joint to break. |
| **Break Torque** | The torque that needs to be applied for this joint to break. |
| **Enable **Collision**A collision occurs when the physics engine detects that the colliders of two GameObjects make contact or overlap, when at least one has a Rigidbody component and is in motion. [More info](CollidersOverview.html) See in [Glossary](Glossary.html#collision)** | Enable this setting if the two connected objects should register collisions with each other. |
| **Enable Preprocessing** | Disabling preprocessing helps to stabilize impossible-to-fulfil configurations. |
| **Mass Scale** | The scale to apply to the inverted mass and inertia tensor of the Rigidbody, ranging from 0.00001 to infinity. This is useful when the joint connects two Rigidbodies of largely varying mass. The physics solver produces better results when the connected Rigidbodies have a similar mass. When your connected Rigidbodies vary in mass, use this property with the **Connect Mass Scale** property to apply fake masses to make them roughly equal to each other. This produces a high-quality and stable simulation, but reduces the physical behaviour of the Rigidbodies. |
| **Connected Mass Scale** | The scale to apply to the inverted mass and inertia tensor of the connected Rigidbody, ranging from 0.00001 to infinity. |

SpringJoint

Hinge Joint component reference

Create a configurable joint

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)