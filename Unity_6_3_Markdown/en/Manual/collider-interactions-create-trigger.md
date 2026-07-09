* [Physics](PhysicsSection.html)
* [Built-in 3D physics](PhysicsOverview.html)
* [Collision](collision-section.html)
* [Collider interactions](collider-interactions.html)
* Create and configure a trigger collider

OnTrigger events

Example scripts for collider events

# Create and configure a trigger collider

A trigger **collider**An invisible shape that is used to handle physical collisions for an object. A collider doesn’t need to be exactly the same shape as the object’s mesh - a rough approximation is often more efficient and indistinguishable in gameplay. [More info](CollidersOverview.html)  
See in [Glossary](Glossary.html#collider) does not collide with other colliders; instead, other colliders pass through it.

To create a trigger collider:

1. Create a **GameObject**The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)  
   See in [Glossary](Glossary.html#GameObject):
   1. To make an invisible trigger collider, create an empty GameObject. In most cases, trigger colliders are invisible.
   2. To make a visible trigger collider, create a GameObject that has a **mesh**The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](mesh.html)  
      See in [Glossary](Glossary.html#Mesh). You should only create a visible trigger collider if it is okay for other GameObjects to visibly pass through it at run time.
2. Add a Collider to the GameObject.
3. Make the collider a trigger:
   1. To do this in the Editor, navigate to the collider’s **Inspector**A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
      See in [Glossary](Glossary.html#Inspector) and enable the **Is Trigger** property.
   2. To do this via script, set the collider’s `IsTrigger` to `true`.

## Configure trigger collisions

Make sure there is at least one [dynamic collider](collider-types-introduction.html) in the **collision**A collision occurs when the physics engine detects that the colliders of two GameObjects make contact or overlap, when at least one has a Rigidbody component and is in motion. [More info](CollidersOverview.html)  
See in [Glossary](Glossary.html#collision). At least one GameObject involved in a trigger collision must have a physics body (a Rigidbody or an ArticulationBody). In most cases, trigger colliders are stationary and static (that is, they have no physics body), and the colliders that pass through them are moving and dynamic (that is, they have a physics body).

Experiment with the size and shape of your trigger collider. For gameplay and simulation, triggers might need some adjustment to make them feel intuitive for the player. For example, you could experiment with making a trigger collider slightly larger than its associated visible GameObject, so that it has a wider radius.

OnTrigger events

Example scripts for collider events

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)