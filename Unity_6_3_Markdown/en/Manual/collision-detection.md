* [Physics](PhysicsSection.html)
* [Built-in 3D physics](PhysicsOverview.html)
* [Collision](collision-section.html)
* Collision detection

Example scripts for collider events

Choose a collision detection mode

# Collision detection

Collision detection is the **physics engine**A system that simulates aspects of physical systems so that objects can accelerate correctly and be affected by collisions, gravity and other forces. [More info](PhysicsSection.html)  
See in [Glossary](Glossary.html#physicsengine)’s process for detecting when a physics body (Rigidbody or ArticulationBody) comes into contact with a **collider**An invisible shape that is used to handle physical collisions for an object. A collider doesn’t need to be exactly the same shape as the object’s mesh - a rough approximation is often more efficient and indistinguishable in gameplay. [More info](CollidersOverview.html)  
See in [Glossary](Glossary.html#collider). Unity provides different **collision**A collision occurs when the physics engine detects that the colliders of two GameObjects make contact or overlap, when at least one has a Rigidbody component and is in motion. [More info](CollidersOverview.html)  
See in [Glossary](Glossary.html#collision) detection algorithms for different situations, so that you can choose the most efficient approach for each individual physics body (Rigidbody or Articulation Body) in your **scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene).

| **Topic** | **Description** |
| --- | --- |
| [Choose a collision detection mode](choose-collision-detection-mode.html) | Choose the right **collision detection**An automatic process performed by Unity which determines whether a moving GameObject with a Rigidbody and collider component has come into contact with any other colliders. [More info](CollidersOverview.html) See in [Glossary](Glossary.html#collisiondetection) mode for each collider in your project. |
| [Layer-based collision detection](LayerBasedCollision.html) | Use layers to define which **GameObjects**The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html) See in [Glossary](Glossary.html#GameObject) can collide with each other. |
| [Discrete collision detection](discrete-collision-detection.html)A collision detection method that calculates and resolves collisions based on the pose of objects at the end of each physics simulation step. [More info](class-Rigidbody.html) See in [Glossary](Glossary.html#discretecollisiondetection) | Overview of the high-efficiency discrete collision detection mode available in Unity. |
| [Continuous collision detection (CCD)](ContinuousCollisionDetection.html) | Overview of the high-accuracy **continuous collision detection**A collision detection method that calculates and resolves collisions over the entire physics simulation step. This can prevent fast-moving objects from tunnelling through walls during a simulation step. [More info](ContinuousCollisionDetection.html) See in [Glossary](Glossary.html#continuouscollisiondetection) (CCD) modes available in Unity. |

Example scripts for collider events

Choose a collision detection mode

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)