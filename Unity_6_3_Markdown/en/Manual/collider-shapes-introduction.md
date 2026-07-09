* [Physics](PhysicsSection.html)
* [Built-in 3D physics](PhysicsOverview.html)
* [Collision](collision-section.html)
* [Collider shapes](collider-shapes.html)
* Introduction to collider shapes

Collider shapes

Primitive collider shapes

# Introduction to collider shapes

Colliders are available in different shape configurations. There are three main shape types for **colliders**An invisible shape that is used to handle physical collisions for an object. A collider doesn’t need to be exactly the same shape as the object’s mesh - a rough approximation is often more efficient and indistinguishable in gameplay. [More info](CollidersOverview.html)  
See in [Glossary](Glossary.html#collider):

* [Primitive colliders](primitive-colliders.html) are built-in simple shapes, which you can attach to your **GameObject**The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)  
  See in [Glossary](Glossary.html#GameObject) and scale to approximately the same size and shape. They are the most computationally efficient shape option, but the least accurate for complex GameObject shapes.
* [Mesh colliders](mesh-colliders.html)A free-form collider component which accepts a mesh reference to define its collision surface shape. [More info](class-MeshCollider.html)  
  See in [Glossary](Glossary.html#MeshCollider) exactly match the shape of the GameObject’s [Mesh](class-Mesh.html)The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](mesh.html)  
  See in [Glossary](Glossary.html#Mesh). They are more accurate than primitive colliders, but require more computational resources.
* [Wheel colliders](wheel-colliders.html)A special collider for grounded vehicles. It has built-in collision detection, wheel physics, and a slip-based tire friction model. It can be used for objects other than wheels, but it is specifically designed for vehicles with wheels. [More info](class-WheelCollider.html)  
  See in [Glossary](Glossary.html#WheelCollider) are for in-game items that have physics-simulated wheels (for example, ground vehicles). They have built-in wheel physics, and controls for simulating friction and suspension.

You can also combine several collider shapes to create [compound colliders](compound-colliders.html).

In addition, Unity’s [Terrain](script-Terrain.html)The landscape in your scene. A Terrain GameObject adds a large flat plane to your scene and you can use the Terrain’s Inspector window to create a detailed landscape. [More info](terrain-UsingTerrains.html)  
See in [Glossary](Glossary.html#Terrain) tool has a specific heightmap-based collider, called the [Terrain Collider](terrain-colliders.html)A terrain-shaped collider component that handles collisions for collision surface with the same shape as the Terrain object it is attached to. [More info](class-TerrainCollider.html)  
See in [Glossary](Glossary.html#TerrainCollider).

## Additional resources

* [Collider shapes](collider-shapes.html)

Collider shapes

Primitive collider shapes

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)