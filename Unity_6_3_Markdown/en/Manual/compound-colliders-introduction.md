* [Physics](PhysicsSection.html)
* [Built-in 3D physics](PhysicsOverview.html)
* [Collision](collision-section.html)
* [Collider shapes](collider-shapes.html)
* [Compound colliders](compound-colliders.html)
* Introduction to compound colliders

Compound colliders

Create a compound collider

# Introduction to compound colliders

A **compound **collider**An invisible shape that is used to handle physical collisions for an object. A collider doesn’t need to be exactly the same shape as the object’s mesh - a rough approximation is often more efficient and indistinguishable in gameplay. [More info](CollidersOverview.html)  
See in [Glossary](Glossary.html#collider)** is a collection of colliders on the same **Rigidbody**A component that allows a GameObject to be affected by simulated gravity and other forces. [More info](class-Rigidbody.html)  
See in [Glossary](Glossary.html#Rigidbody) **GameObject**The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject).

Compound colliders collectively behave like a single Rigidbody collider. They are useful when you need an accurate collider for a concave shape, or if you have a model that would be too computationally demanding to simulate with a [Mesh collider](mesh-colliders.html)A free-form collider component which accepts a mesh reference to define its collision surface shape. [More info](class-MeshCollider.html)  
See in [Glossary](Glossary.html#MeshCollider).

## Construction of a compound collider

A compound collider is made of the following elements:

* A parent GameObject that has a Rigidbody
* Empty child GameObjects that contain colliders

A compound collider should only have one Rigidbody, which should be on the root GameObject.

For more guidance on how to create a compound collider, see [Create a compound collider](create-compound-collider.html).

![A compound collider setup on a gun model. Five colliders make up an approximation of the model’s shape.](../uploads/Main/CompoundCollider.jpg)


A compound collider setup on a gun model. Five colliders make up an approximation of the model’s shape.

In the above picture, the **Gun Model** GameObject has a Rigidbody attached to its parent GameObject, and several child GameObjects that each have a primitive collider. When physics forces move the Rigidbody parent, the child colliders move along with it. The primitive colliders can collide with other colliders in the environment, and the parent Rigidbody alters the way it moves based on these **collisions**A collision occurs when the physics engine detects that the colliders of two GameObjects make contact or overlap, when at least one has a Rigidbody component and is in motion. [More info](CollidersOverview.html)  
See in [Glossary](Glossary.html#collision).

This configuration offers more flexibility than a single GameObject that contains a Rigidbody and several colliders. When each collider is on a different GameObject, you can modify the Transform of each collider individually. However, you should monitor the Rigidbody’s behavior when you reposition colliders. Changes to collider position and scale can change the Rigidbody’s **center of mass**Represents the average position of all mass in a Rigidbody for the purposes of physics calculations. By default it is computed from all colliders belonging to the Rigidbody, but can be modified via script. [More info](../ScriptReference/Rigidbody-centerOfMass.html)  
See in [Glossary](Glossary.html#centerofmass), which can result in some unexpected behavior if continuous change is made over several frames at runtime. If this happens, you can use [`rigidbody.centerOfMass`](../ScriptReference/Rigidbody-centerOfMass.html) to manually set the center of mass.

## How a compound collider works

When you attach several colliders to the same Rigidbody, the physics system treats the whole collection as a single Rigidbody collider. The [collider type](collider-types-introduction.html) (dynamic or kinematic) is defined by the Rigidbody configuration.

When a compound collider touches another collider, Unity registers collisions per each individual collider in the compound. For this reason, you should try to arrange your colliders so that you only get the collision pairs you want at runtime, or use collider labels to determine behaviors caused by specific colliders.

## Benefits and limitations of compound colliders

In most cases, compound colliders offer a similar solution to [Mesh colliders](mesh-colliders.html): their primary purpose is to provide accurate collisions for items with complex shapes. When considering the benefits and limitations of compound colliders, you are usually comparing them to **Mesh**The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](mesh.html)  
See in [Glossary](Glossary.html#Mesh) colliders.

The main benefits of compound colliders are:

* You can get collisions for complex concave shapes. Mesh colliders are more accurate, but they don’t support accurate collisions for concave shapes.
* In some cases, compound colliders can be less computationally demanding than Mesh colliders. This is often the case for simpler shapes which only require a few colliders to approximate, or for shapes that don’t need to be too accurate. For example, a Mesh collider might generate hundreds of polygons in order to precisely match a complex shape, but an approximation with primitive colliders might require far fewer.

However, compound colliders also have some significant limitations:

* Compound colliders are not as accurate. In most cases, you build a compound collider out of simpler shapes, which allow you to approximate but not perfectly match the shape of the item.
* Compound colliders take longer to produce. Compound colliders require you to arrange each collider manually, which takes more time.
* In some cases, compound colliders can be more computationally demanding than Mesh colliders. This is often the case for very complex shapes which require a high number of colliders to approximate. One Mesh collider might be more efficient than several primitive colliders.

The decision is always unique to your project, so you should test each configuration and use the Physics Profiler to understand the efficiency of your collider setup.

Compound colliders

Create a compound collider

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)