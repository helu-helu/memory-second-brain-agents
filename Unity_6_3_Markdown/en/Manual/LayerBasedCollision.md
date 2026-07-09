* [Physics](PhysicsSection.html)
* [Built-in 3D physics](PhysicsOverview.html)
* [Collision](collision-section.html)
* [Collision detection](collision-detection.html)
* Layer-based collision detection

Choose a collision detection mode

Discrete collision detection

# Layer-based collision detection

Layer-based **collision**A collision occurs when the physics engine detects that the colliders of two GameObjects make contact or overlap, when at least one has a Rigidbody component and is in motion. [More info](CollidersOverview.html)  
See in [Glossary](Glossary.html#collision) detection is a way to make a **GameObject**The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) collide with another GameObject that’s set up on a specific layer or layers.

![Layer Collision Matrix selected in the Project Settings window.](../uploads/Main/layer-collision-matrix.png)


Layer Collision Matrix selected in the Project Settings window.

The Layer Collision Matrix defines which GameObjects can collide with which Layers. To open the Layer Collision Matrix go to **Edit > Project Settings > Physics**.

In the image, the Layer Collision Matrix is set up so that only GameObjects that belong to the same layer can collide:

* Layer 1 is checked for Layer 1 only
* Layer 2 is checked for Layer 2 only
* Layer 3 is checked for Layer 3 only

If, for example, you want Layer 1 to collide with Layer 2 and 3, but not with Layer 1, find the row for **Layer 1**, then check the boxes for the **Layer 2** and **Layer 3** columns, and leave the **Layer 1** column checkbox blank.

## Set up layer-based collision detection

1. Select the GameObject you want to assign a layer to.
2. In the **Inspector**A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
   See in [Glossary](Glossary.html#Inspector), select the **Layer** dropdown at the top, and either choose a Layer or add a new Layer. Repeat for each GameObject until you have finished assigning your GameObjects to Layers.

   ![Cube selected in the Inspector, with Layer 1 assigned to it.](../uploads/Main/layer-collision-selection.png)


   Cube selected in the Inspector, with Layer 1 assigned to it.
3. In the Unity menu bar, go to **Edit** > **Project Settings**, then select the **Physics** category to open the [Physics](class-PhysicsManager.html) window.
4. Select the layers on the Collision Matrix that you want to interact with the other layers.

## Additional resources

* [Essential Unity concepts](https://learn.unity.com/pathway/unity-essentials)
* [Tags and layers](class-TagManager.html)
* [Collision detection](collision-detection.html)An automatic process performed by Unity which determines whether a moving GameObject with a Rigidbody and collider component has come into contact with any other colliders. [More info](CollidersOverview.html)  
  See in [Glossary](Glossary.html#collisiondetection)
* [Layers](Layers.html)Layers in Unity can be used to selectively opt groups of GameObjects in or out of certain processes or calculations. This includes camera rendering, lighting, physics collisions, or custom calculations in your own code. [More info](Layers.html)  
  See in [Glossary](Glossary.html#layer)

Choose a collision detection mode

Discrete collision detection

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)