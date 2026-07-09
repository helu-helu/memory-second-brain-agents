* [Physics](PhysicsSection.html)
* [Built-in 3D physics](PhysicsOverview.html)
* [Collision](collision-section.html)
* [Collider interactions](collider-interactions.html)
* OnTrigger events

OnCollision events

Create and configure a trigger collider

# OnTrigger events

Trigger **colliders**An invisible shape that is used to handle physical collisions for an object. A collider doesn’t need to be exactly the same shape as the object’s mesh - a rough approximation is often more efficient and indistinguishable in gameplay. [More info](CollidersOverview.html)  
See in [Glossary](Glossary.html#collider) don’t cause **collisions**A collision occurs when the physics engine detects that the colliders of two GameObjects make contact or overlap, when at least one has a Rigidbody component and is in motion. [More info](CollidersOverview.html)  
See in [Glossary](Glossary.html#collision). Instead, they detect other colliders that pass through them, and call functions that you can use to initiate events.

Example uses for triggers include:

* When the player reaches a specific area at the end of a corridor, activate a cinematic cutscene.
* When the player character walks within a space in front of a sliding door, trigger an animation to open the door.
* When projectiles pass through a trigger collider in the far distance, disable or destroy the projectile.

Working with trigger colliders primarily involves the following API functions:

* [`Collider.OnTriggerEnter`](../ScriptReference/Collider.OnTriggerEnter.html): Unity calls this function on a trigger collider when it first makes contact with another collider.
* [`Collider.OnTriggerStay`](../ScriptReference/Collider.OnTriggerStay.html): Unity calls this function on a trigger collider once per frame if it detects another Collider inside the trigger collider.
* [`Collider.OnTriggerExit`](../ScriptReference/Collider.OnTriggerExit.html): Unity calls this function on a trigger collider when it ceases contact with another collider.

The following example prints a message to the Console when Unity calls each function.

```
using UnityEngine;
using System.Collections;

public class DoorObject : MonoBehaviour
{
    // “other” refers to the collider on the GameObject inside this trigger
    void OnTriggerEnter (Collider other)
    {
        Debug.Log ("A collider has entered the DoorObject trigger");
    }

    void OnTriggerStay (Collider other)
    {
        Debug.Log ("A collider is inside the DoorObject trigger");
    }
    
    void OnTriggerExit (Collider other)
    {
        Debug.Log ("A collider has exited the DoorObject trigger");
    }
}
```

For examples of practical applications for `OnTrigger` events, see [Example scripts for collider events](collider-interactions-example-scripts.html).

OnCollision events

Create and configure a trigger collider

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)