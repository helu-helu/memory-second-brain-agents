* [Physics](PhysicsSection.html)
* [Built-in 3D physics](PhysicsOverview.html)
* Collision

Constant Force component reference

Introduction to collision

# Collision

To configure **collision**A collision occurs when the physics engine detects that the colliders of two GameObjects make contact or overlap, when at least one has a Rigidbody component and is in motion. [More info](CollidersOverview.html)  
See in [Glossary](Glossary.html#collision) between GameObjects in Unity, you need to use colliders. Colliders define the shape of a **GameObject**The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) for the purposes of physical collisions. You can then use these colliders to manage collision events. You can configure collisions via **collider**An invisible shape that is used to handle physical collisions for an object. A collider doesn’t need to be exactly the same shape as the object’s mesh - a rough approximation is often more efficient and indistinguishable in gameplay. [More info](CollidersOverview.html)  
See in [Glossary](Glossary.html#collider) components, or their corresponding C# class.

This documentation describes how to configure collisions and collision events, and how colliders interact with each other and their environment.

| **Topic** | **Description** |
| --- | --- |
| [Introduction to collision](CollidersOverview.html) | Overview of the fundamental concepts around physics collision in Unity. |
| [Introduction to collider types](collider-types-introduction.html) | The different collider types (static, kinematic, and dynamic), and how collider behaviour differs depending on the collider’s physics body configuration. |
| [Collider shapes](collider-shapes.html) | The different collider shapes available, and how collider shape complexity affects performance. |
| [Collider surfaces](collider-surfaces.html) | How PhysX handles friction and bounciness on a collider’s surface, and how to configure surface properties for each collider. |
| [Collider interactions and events](collider-interactions.html) | How collisions can call events and functions to trigger changes at run time. |
| [Collision detection](collision-detection.html)An automatic process performed by Unity which determines whether a moving GameObject with a Rigidbody and collider component has come into contact with any other colliders. [More info](CollidersOverview.html) See in [Glossary](Glossary.html#collisiondetection) | How PhysX detects collisions in Unity, and how to select the right algorithm depending on your collider configuration for optimal performance. |

Constant Force component reference

Introduction to collision

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)