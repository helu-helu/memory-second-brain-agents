* [Physics](PhysicsSection.html)
* [Built-in 3D physics](PhysicsOverview.html)
* [Joints](joints-section.html)
* [Create a configurable joint](create-configurable-joint.html)
* Driving forces with Configurable Joints

Customize movement constraint with Configurable Joints

Configure driving forces on a Configurable Joint

# Driving forces with Configurable Joints

A **joint**A physics component allowing a dynamic connection between Rigidbody components, usually allowing some degree of movement such as a hinge. [More info](Joints.html)  
See in [Glossary](Glossary.html#joint) can react to the movements of the object it is attached to, and apply [driving forces](#understand-driving-forces) to set the object in motion.

You can use the **Configurable Joint**An extremely customizable joint that other joint types are derived from. It can be used to create anything from adapted versions of existing joints to custom designed and highly specialized joints. [More info](class-ConfigurableJoint.html)  
See in [Glossary](Glossary.html#ConfigurableJoint) to apply driving forces toward either a [position-based target](configure-driving-forces.html#apply-target-position) like a position or rotation, or a [velocity-based target](configure-driving-forces.html#apply-target-velocity) like a linear velocity or angular velocity.

## Understand driving forces

The Configurable Joint applies driving forces on each axis, via **axis drives**, to apply motion and rotation.

The axis drives for linear force are:
* **X Drive**
* **Y Drive**
* **Z Drive**

The axis drives for angular or rotational force are:
* **Angular X Drive**
* **Angular YZ Drive**

Each axis drive has spring and damper options to simulate a motor that generates force. The physics system uses these values to calculate the driving force it should apply on that axis, via the following formula:

```
force = positionSpring * (targetPosition - position) + positionDamper * (targetVelocity - velocity)
```

The **Maximum Force** property prevents the force from exceeding a specific value, even if the force calculation result is higher.

Customize movement constraint with Configurable Joints

Configure driving forces on a Configurable Joint

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)