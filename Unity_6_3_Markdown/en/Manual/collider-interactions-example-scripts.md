* [Physics](PhysicsSection.html)
* [Built-in 3D physics](PhysicsOverview.html)
* [Collision](collision-section.html)
* [Collider interactions](collider-interactions.html)
* Example scripts for collider events

Create and configure a trigger collider

Collision detection

# Example scripts for collider events

The following examples demonstrate ways to call events from **collision**A collision occurs when the physics engine detects that the colliders of two GameObjects make contact or overlap, when at least one has a Rigidbody component and is in motion. [More info](CollidersOverview.html)  
See in [Glossary](Glossary.html#collision) functions. They use `OnCollisionEnter` and `OnTriggerEnter` respectively, but the concepts apply to all `OnCollision` and `OnTrigger` functions.

## Example: Different events for different GameObject properties

You can configure your **scripts**A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts) to trigger different events based on the properties of the other **collider**An invisible shape that is used to handle physical collisions for an object. A collider doesn’t need to be exactly the same shape as the object’s mesh - a rough approximation is often more efficient and indistinguishable in gameplay. [More info](CollidersOverview.html)  
See in [Glossary](Glossary.html#collider)’s associated **GameObject**The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject), such as its name or tag. This is useful if, for example, you want to allow some colliders to produce an event, but not others.

The following example prints a different message depending on whether the other collider that has touched this collider has a tag of “Player” or “Enemy”.

```
using UnityEngine;
using System.Collections;

public class DoorObject : Monobehaviour
{
    private void OnCollisionEnter(Collision other)
    {
        if (other.CompareTag("Player"))
        {
            Debug.Log ("The player character has touched the door.")
        }

        if (other.CompareTag("Enemy"))
        {
            Debug.Log ("An enemy character has touched the door!")
        }
    }
}
```

## Example: Send an event message every physics update

The following example uses a trigger collider to produce a hoverpad. The trigger collider is positioned directly on top of a hoverpad GameObject, and applies a constant upward force to any GameObject within its trigger.

```
using UnityEngine;
using System.Collections;

public class HoverPad : MonoBehaviour
{
    // define a value for the upward force calculation
    public float hoverForce = 12f;

    // whenever another collider is in contact with this trigger collider…
    void OnTriggerStay (Collider other)
    {
        // …add an upward force to the Rigidbody of the other collider.
        other.rigidbody.AddForce(Vector3.up * hoverForce, ForceMode.Acceleration) 
    }
}
```

Create and configure a trigger collider

Collision detection

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)