* [Physics](PhysicsSection.html)
* [Built-in 3D physics](PhysicsOverview.html)
* [Collision](collision-section.html)
* [Collider surfaces](collider-surfaces.html)
* Create and apply a custom Physics Material

How collider surface values combine

Physics Material asset reference

# Create and apply a custom Physics Material

You can create as many custom [Physics Material](class-PhysicsMaterial.html)A physics asset for adjusting the friction and bouncing effects of colliding objects. [More info](class-PhysicsMaterial.html)  
See in [Glossary](Glossary.html#PhysicsMaterial) assets as you need, and apply them to **colliders**An invisible shape that is used to handle physical collisions for an object. A collider doesn’t need to be exactly the same shape as the object’s mesh - a rough approximation is often more efficient and indistinguishable in gameplay. [More info](CollidersOverview.html)  
See in [Glossary](Glossary.html#collider) in your **scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene).

Several colliders can have the same Physics Material asset assigned to them, and you can set a project-wide default to apply new default settings to all colliders in the project.

## Create a custom Physics Material asset

To create a Physics Material asset, go to **Assets** > **Create** > **Physics Material**. By default, Unity places new Physics Material assets in your `Assets` directory.

You can create as many custom Physics Material assets as you need. Physics Material assets have the file extension `.physicMaterial`.

## Apply a custom Physics Material asset to a collider

To apply a Physics Material asset to a collider:

1. Navigate to the target collider’s **Material** property.
2. In the **Material** property field, select the picker icon.
3. Select the Physics Material asset you want to use.

Alternatively, you can click and drag the Physics Material asset file directly from the **Project window**A window that shows the contents of your `Assets` folder (Project tab) [More info](ProjectView.html)  
See in [Glossary](Glossary.html#Projectwindow) onto the target collider’s **Material** field.

Each collider can only have one assigned Physics Material asset at a time. You can assign the same Physics Material asset to multiple colliders.

## Set a custom Physics Material asset as the project default

You can use a custom Physics Material asset to replace the project-wide default settings. Unity applies the project-wide default settings to any collider that does not have an assigned Physics Material asset.

To change the default Physics Material values:

1. Create a Physics Material asset and configure it to the default settings you want for the project.
2. Go to the Physics Settings (**Edit** > **Project Settings** > **Physics**).
3. In the **Default Material** property field, select the picker icon.
4. Select the Physics Material you want to use.

## Additional resources

* [Physics Material](class-PhysicsMaterial.html)
* [Physics Settings](class-PhysicsManager.html)

How collider surface values combine

Physics Material asset reference

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)