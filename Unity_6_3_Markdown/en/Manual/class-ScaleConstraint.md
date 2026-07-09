* [GameObjects](working-with-gameobjects.html)
* [Add components to GameObjects](unity-components.html)
* [Constraint components](constraint-components.html)
* Scale Constraint component

Rotation Constraint component

Assign GameObjects to layers

# Scale Constraint component

A Scale Constraint component resizes a **GameObject**The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) to match the scale of its source GameObjects.

![Scale Constraint component](../uploads/Main/ScaleConstraint.png)


Scale Constraint component

## Properties

| **Property** | **Description** |
| --- | --- |
| **Activate** | After you resize the constrained GameObject and its source GameObjects, click **Activate** to save this information. **Activate** saves the current offset from the source GameObjects in **Scale At Rest** and **Scale Offset** then enables **Is Active** and **Lock**. |
| **Zero** | Sets the rotation of the constrained GameObject to the source GameObjects. **Zero** resets the **Scale At Rest** and **Scale Offset** fields then enables **Is Active** and **Lock**. |
| **Is Active** | Enable to evaluate the Constraint. To also apply the Constraint, make sure **Lock** is enabled. |
| **Weight** | The strength of the Constraint. A weight of 1 causes the Constraint to resize this GameObject at the same rate as its source GameObjects. A weight of 0 removes the effect of the Constraint completely. This weight affects all source GameObjects. Each GameObject in the **Sources** list also has a weight. |

### Constraint Settings

| **Property** | **Description** |
| --- | --- |
| **Lock** | Enable to let the Constraint resize the GameObject. Disable this property to edit the scale of this GameObject. You can also edit the **Scale At Rest** and **Scale Offset** properties. If **Is Active** is enabled, the Constraint updates the **Scale At Rest** or **Scale Offset** properties for you as you resize the GameObject or its Source GameObjects. When you are satisfied with your changes, enable **Lock** to let the Constraint to control this GameObject. This property has no effect in Play Mode. |
| **Scale At Rest** | The X, Y, and Z values to use when **Weight** is 0 or when the corresponding **Freeze Scale Axes** is not enabled. To edit these fields, disable **Lock**. |
| **Scale Offset** | The X, Y, and Z offset from the transform that is imposed by the Constraint. To edit these fields, disable Lock. |
| **Freeze Scale Axes** | Enable X, Y, or Z to allow the Constraint to control the corresponding axes. Disable an axis to stop the Constraint from controlling it. This allows you to edit, animate, or script the unfrozen axis. |

### Sources

The list of GameObjects that constrain this GameObject. Each source has a weight from 0 to 1.

Rotation Constraint component

Assign GameObjects to layers

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)