* [Physics](PhysicsSection.html)
* [Built-in 3D physics](PhysicsOverview.html)
* [Collision](collision-section.html)
* [Collider shapes](collider-shapes.html)
* [Primitive collider shapes](primitive-colliders.html)
* Capsule collider component reference

Sphere collider component reference

Mesh colliders

# Capsule collider component reference

[Switch to Scripting](../ScriptReference/CapsuleCollider.html "Go to CapsuleCollider page in the Scripting Reference")

The Capsule **collider**An invisible shape that is used to handle physical collisions for an object. A collider doesn’t need to be exactly the same shape as the object’s mesh - a rough approximation is often more efficient and indistinguishable in gameplay. [More info](CollidersOverview.html)  
See in [Glossary](Glossary.html#collider) is a built-in 3D capsule-shaped collider made of two half-spheres joined together by a cylinder. It is useful for in-application items that have a cylindrical shape, or as a collider for player and non-player characters in a **scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene).

Because **Capsule colliders** have no corners, they are also useful to soften the **collision**A collision occurs when the physics engine detects that the colliders of two GameObjects make contact or overlap, when at least one has a Rigidbody component and is in motion. [More info](CollidersOverview.html)  
See in [Glossary](Glossary.html#collision) area of sharp corners and edges in level geometry, so that players move more smoothly.

The Capsule collider has relatively low resource requirements.

| **Property** | **Description** |
| --- | --- |
| **Edit Collider** | Enable the **Edit Collider** button to display the collider’s contact points in the **Scene view**An interactive view into the world you are creating. You use the Scene View to select and position scenery, characters, cameras, lights, and all other types of Game Object. [More info](UsingTheSceneView.html) See in [Glossary](Glossary.html#SceneView). You can click and drag these contact points to modify the size and shape of the collider. Alternatively, use the **Center**, **Radius**, and **Height** properties. |
| **Is Trigger** | Enable **Is Trigger** to use the collider as a trigger for events. When **Is Trigger** is enabled, other colliders pass through this collider, and trigger the messages [`OnTriggerEnter`](../ScriptReference/Collider.OnTriggerEnter.html), [`OnTriggerStay`](../ScriptReference/Collider.OnTriggerStay.html), and [`OnTriggerExit`](../ScriptReference/Collider.OnTriggerExit.html). |
| **Provides Contacts** | Enable **Provides Contacts** to generate contact information for this collider at all times. Usually, a collider only generates contact data if there is something to send it to; in this case, the messages [`OnCollisionEnter`](../ScriptReference/Collider.OnCollisionEnter.html), [`OnCollisionStay`](../ScriptReference/Collider.OnCollisionStay.html), or [`OnCollisionExit`](../ScriptReference/Collider.OnCollisionExit.html). When **Provides Contacts** is enabled, the collider generates contact data for the physics system at all times. Contact generation is resource-intensive, so **Provides Contacts** is disabled by default. |
| **Material** | Add the [Physic Material component](class-PhysicsMaterial.html) that determines the friction and bounciness of this collider. |
| **Center** | Define the position of the collider on each axis in the **GameObject**The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html) See in [Glossary](Glossary.html#GameObject)’s local space. By default, this is set to (0, 0, 0). |
| **Radius** | Define the radius of the collider from its center. You can adjust the **Radius** independently of the **Height**. By default, this is set to 0.5. |
| **Height** | Define the total height of the collider in **Unity units**The unit size used in Unity projects. By default, 1 Unity unit is 1 meter. To use a different scale, set the Scale Factor in the Import Settings when importing assets. See in [Glossary](Glossary.html#Unityunit). You can adjust the **Height** independently of the **Radius**. By default, this is set to 2. |
| **Direction** | Define the axis of the capsule’s lengthwise orientation in the object’s local space. |

## Layer overrides

The Layer Overrides section provides properties that allow you to override the project-wide [Layer-based collision detection](LayerBasedCollision.html) settings for this collider.

| **Property** | **Description** |
| --- | --- |
| **Layer Override Priority** | Define the priority of this collider override. When two colliders have conflicting overrides, the settings of the collider with the higher value priority are taken.  For example, if a collider with a **Layer Override Priority** of 1 collides with a Collider with a **Layer Override Priority** of 2, the physics system uses the settings for the Collider with the **Layer Override Priority** of 2. |
| **Include Layers** | Choose which Layers to include in collisions with this collider. |
| **Exclude Layers** | Choose which Layers to exclude in collisions with this collider. |

Sphere collider component reference

Mesh colliders

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)