* [Physics](PhysicsSection.html)
* [Built-in 3D physics](PhysicsOverview.html)
* [Collision](collision-section.html)
* Collider shapes

Introduction to collider types

Introduction to collider shapes

# Collider shapes

Colliders are available in different shape configurations. A **collider**An invisible shape that is used to handle physical collisions for an object. A collider doesn’t need to be exactly the same shape as the object’s mesh - a rough approximation is often more efficient and indistinguishable in gameplay. [More info](CollidersOverview.html)  
See in [Glossary](Glossary.html#collider)’s shape defines how accurately the collider matches the **Mesh**The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](mesh.html)  
See in [Glossary](Glossary.html#Mesh) shape, and how computationally efficient the collider is.

| **Topic** | **Description** |
| --- | --- |
| [Introduction to collider shapes](collider-shapes-introduction.html) | Overview of the different collider shapes in Unity. |
| [Primitive collider shapes](primitive-colliders.html) | Primitive collider shapes are built-in, pre-calculated collider shapes in Unity (Box, Sphere and Capsule colliders). |
| [Mesh colliders](mesh-colliders.html)A free-form collider component which accepts a mesh reference to define its collision surface shape. [More info](class-MeshCollider.html) See in [Glossary](Glossary.html#MeshCollider) | Mesh colliders create **collision**A collision occurs when the physics engine detects that the colliders of two GameObjects make contact or overlap, when at least one has a Rigidbody component and is in motion. [More info](CollidersOverview.html) See in [Glossary](Glossary.html#collision) geometry that matches the shape of their associated Mesh, for extremely accurate collisions. |
| [Wheel colliders](wheel-colliders.html)A special collider for grounded vehicles. It has built-in collision detection, wheel physics, and a slip-based tire friction model. It can be used for objects other than wheels, but it is specifically designed for vehicles with wheels. [More info](class-WheelCollider.html) See in [Glossary](Glossary.html#WheelCollider) | Wheel colliders use raycasting to form wheel-shaped collision geometry with suspension and tyre-based friction. |
| [Terrain colliders](terrain-colliders.html)A terrain-shaped collider component that handles collisions for collision surface with the same shape as the Terrain object it is attached to. [More info](class-TerrainCollider.html) See in [Glossary](Glossary.html#TerrainCollider) | **Terrain**The landscape in your scene. A Terrain GameObject adds a large flat plane to your scene and you can use the Terrain’s Inspector window to create a detailed landscape. [More info](terrain-UsingTerrains.html) See in [Glossary](Glossary.html#Terrain) colliders create collision geometry that matches the shape of their associated Terrain, for extremely accurate collisions. |
| [Compound colliders](compound-colliders.html) | Compound colliders are a combination of multiple other colliders, which together have a single **center of mass**Represents the average position of all mass in a Rigidbody for the purposes of physics calculations. By default it is computed from all colliders belonging to the Rigidbody, but can be modified via script. [More info](../ScriptReference/Rigidbody-centerOfMass.html) See in [Glossary](Glossary.html#centerofmass). |

Introduction to collider types

Introduction to collider shapes

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)