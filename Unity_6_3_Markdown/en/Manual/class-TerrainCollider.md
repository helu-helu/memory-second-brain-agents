* [Physics](PhysicsSection.html)
* [Built-in 3D physics](PhysicsOverview.html)
* [Collision](collision-section.html)
* [Collider shapes](collider-shapes.html)
* [Terrain colliders](terrain-colliders.html)
* Terrain collider component reference

Introduction to Terrain colliders

Compound colliders

# Terrain collider component reference

[Switch to Scripting](../ScriptReference/TerrainCollider.html "Go to TerrainCollider page in the Scripting Reference")

The **Terrain **collider**An invisible shape that is used to handle physical collisions for an object. A collider doesn’t need to be exactly the same shape as the object’s mesh - a rough approximation is often more efficient and indistinguishable in gameplay. [More info](CollidersOverview.html)  
See in [Glossary](Glossary.html#collider)** builds a collider that matches the geometry of the [Terrain](script-Terrain.html)The landscape in your scene. A Terrain GameObject adds a large flat plane to your scene and you can use the Terrain’s Inspector window to create a detailed landscape. [More info](terrain-UsingTerrains.html)  
See in [Glossary](Glossary.html#Terrain) it is attached to. It is the best and most accurate collider type for Terrains.

| **Property** | **Description** |
| --- | --- |
| **Provides Contacts** | Enable **Provides Contacts** to generate contact information for this collider at all times. Usually, a collider only generates contact data if there is something to send it to; in this case, the messages [`OnCollisionEnter`](../ScriptReference/Collider.OnCollisionEnter.html), [`OnCollisionStay`](../ScriptReference/Collider.OnCollisionStay.html), or [`OnCollisionExit`](../ScriptReference/Collider.OnCollisionExit.html). When **Provides Contacts** is enabled, the collider generates contact data for the physics system at all times. Contact generation is resource-intensive, so **Provides Contacts** is disabled by default. |
| **Material** | Choose the [Physics Material](class-PhysicsMaterial.html)A physics asset for adjusting the friction and bouncing effects of colliding objects. [More info](class-PhysicsMaterial.html) See in [Glossary](Glossary.html#PhysicsMaterial) asset that determines how this collider interacts with others. If you do not choose one, the physics system uses the project-wide default settings. |
| **Terrain Data** | Choose the [TerrainData](../ScriptReference/TerrainData.html) asset. The **Terrain collider** builds a collider shape based on the TerrainData asset properties. |
| **Enable Tree Colliders** | Enable this to automatically generate colliders for any [Trees](terrain-Trees-Landing.html)A GameObject and associated Component that allows you to add tree assets to your Scene. You can add branch levels and leaves to trees in the Tree Inspector window. [More info](class-Tree.html) See in [Glossary](Glossary.html#Tree) on the Terrain. This makes the collider more accurate, but is more computationally demanding, so you should only use it if your **scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html) See in [Glossary](Glossary.html#Scene) requires physics interactions with the trees on the Terrain. It is enabled by default. |

## Layer overrides

The Layer Overrides section provides properties that allow you to override the project-wide [Layer-based collision detection](LayerBasedCollision.html) settings for this collider.

| **Property** | **Description** |
| --- | --- |
| **Layer Override Priority** | Define the priority of this collider override. When two colliders have conflicting overrides, the settings of the collider with the higher value priority are taken.  For example, if a collider with a **Layer Override Priority** of 1 collides with a Collider with a **Layer Override Priority** of 2, the physics system uses the settings for the Collider with the **Layer Override Priority** of 2. |
| **Include Layers** | Choose which Layers to include in **collisions**A collision occurs when the physics engine detects that the colliders of two GameObjects make contact or overlap, when at least one has a Rigidbody component and is in motion. [More info](CollidersOverview.html) See in [Glossary](Glossary.html#collision) with this collider. |
| **Exclude Layers** | Choose which Layers to exclude in collisions with this collider. |

Introduction to Terrain colliders

Compound colliders

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)