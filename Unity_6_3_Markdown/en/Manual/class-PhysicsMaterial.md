* [Physics](PhysicsSection.html)
* [Built-in 3D physics](PhysicsOverview.html)
* [Collision](collision-section.html)
* [Collider surfaces](collider-surfaces.html)
* Physics Material asset reference

Create and apply a custom Physics Material

Collider interactions

# Physics Material asset reference

[Switch to Scripting](../ScriptReference/PhysicsMaterial.html "Go to PhysicsMaterial page in the Scripting Reference")

The ****Physics Material**** is a material asset that you can place on a **GameObject**The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject). The material defines properties on the **collider**An invisible shape that is used to handle physical collisions for an object. A collider doesn’t need to be exactly the same shape as the object’s mesh - a rough approximation is often more efficient and indistinguishable in gameplay. [More info](CollidersOverview.html)  
See in [Glossary](Glossary.html#collider)’s surface, such as friction and bounciness.

To create a Physics Material, go to **Assets** > **Create** > **Physics Material**, then drag the Physics Material from the Project window onto a collider in the scene.

If there is no Physics Material set, a collider uses the default surface settings. To adjust the project’s default settings, use the [Physics Settings](class-PhysicsManager.html).

| **Property** | **Description** |
| --- | --- |
| **Dynamic Friction** | Define how much friction the collider’s surface has against another collider when the colliders are moving or sliding against each other. This value is between 0 and 1. A value of 0 means no friction (like ice), while a value of 1 means very high friction (like rubber). By default, **Dynamic Friction** is set to 0.6.   Unity uses the friction value of both touching colliders to calculate the friction between them, based on the **Friction Combine** property (below). |
| **Static Friction** | Define how much friction the collider’s surface has against another collider when the colliders are not moving. This value is between 0 and 1. A value of 0 means no friction (like ice), while a value of 1 means very high friction (like rubber). By default, **Static Friction** is set to 0.6.   Unity uses the friction value of both touching colliders to calculate the friction between them, based on the **Friction Combine** property (below). |
| **Bounciness** | Define how bouncy the surface is, and how much other colliders can bounce off it. A value of 0 means the surface is not at all bouncy (like soft clay), and other colliders lose kinetic energy upon hitting it. A value of 1 means the surface is very bouncy (like rubber), and other colliders bounce without any loss of kinetic energy. By default, **Bounciness** is set to 0.   Unity uses the bounciness value of both touching colliders to calculate the bounce between them, based on the **Bounce Combine** property.   Note that the physics system’s bounce approximations might still add small amounts of energy to the simulation. |
| **Friction Combine** | Define how the physics system calculates friction between two colliders, based on each collider’s friction. This selection applies to both **Dynamic Friction** and Static Friction. By default, **Friction Combine** is set to **Average**. For details, refer to [How collider surface values combine](collider-surfaces-combine.html). |
| **Bounce Combine** | Define how the physics system calculates bounce between two colliders, based on each collider’s **Bounciness** value. By default, **Bounce Combine** is set to **Average**. For details, refer to [How collider surface values combine](collider-surfaces-combine.html). |

Create and apply a custom Physics Material

Collider interactions

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)