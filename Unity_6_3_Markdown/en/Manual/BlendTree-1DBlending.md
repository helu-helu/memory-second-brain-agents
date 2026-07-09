* [Animation](AnimationSection.html)
* [Mecanim Animation system](animation-mecanim.html)
* [Animator Controller](animation-animator-controller.html)
* [Animation state machine](AnimationStateMachines.html)
* [Animation blend trees](animation-blend-trees.html)
* 1D Blending

Animation Blend Trees

2D Blending

# 1D Blending

The first option in the **Inspector**A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector) of a **Blend Node**A node in a Blend Tree graph that blends animation clip nodes. [More info](class-BlendTree.html)  
See in [Glossary](Glossary.html#BlendNode) is the **Blend Type**. Use this drop-down to select one of the different blend types that can blend according to one or two parameters. 1D Blending blends child motions according to a single parameter.

After setting the Blend Type, select the [Animation Parameter](AnimationParameters.html) that control this Blend Tree. In this example, the parameter is `direction` which varies between –1.0 (left) and +1.0 (right), with 0.0 denoting a straight run without leaning.

Then you can add individual animations by clicking the small “+” button and selecting **Add Motion Field** from the popup menu. When you’re done, it should look something like this:

![A 1D Blend Tree with three Animation Clips](../uploads/Main/MecanimBlendTree1D.png)


A 1D Blend Tree with three Animation Clips

The diagram at the top of the Inspector shows the influence of each of the child motions as the parameter varies between its minimum and maximum values. Each motion is shown as a little blue pyramid (the first and last are only shown in half), and if you click and hold down the left mouse button on one them, the corresponding motion is highlighted in the motion list below. The peak of each pyramid defines the parameter value where the motion has full influence, meaning that its animation weight is 1 and the other animations have a weight of 0. This is also called the **threshold** of the motion.

![The diagram at the top of the Blend Tree Inspector visualizes the weights of the child motions over the range of the parameter values.](../uploads/Main/MecanimBlendTreeParam.png)


The diagram at the top of the Blend Tree Inspector visualizes the weights of the child motions over the range of the parameter values.

The red vertical bar indicates the value of the **Parameter**. If you press **Play** in the **Preview** at the bottom of the **Inspector** and drag the red bar in the diagram left and right, you can see how the value of the parameter is controlling the blending of the different motions.

## Parameter Range

The range of the parameter used by the Blend Tree is shown below the diagram as two numbers to the left and right. Either one of them can be changed by clicking on the number and dragging left or right with the mouse. Note that the values correspond to the threshold of the first and last motion in the motion list.

## Thresholds

You can change the threshold value of a motion by clicking on its corresponding blue pyramid in the diagram and dragging it left or right. If the “Automate Thresholds” toggle is not enabled, you can also edit the threshold value of a motion in the motion list by typing in a number in the number field in the Threshold column.

Below the motion list is the checkbox *Automate Thresholds*. Enabling it will distribute the thresholds of the motions evenly across the parameter range. For example, if there are five clips and the parameter ranges from –90 to +90, the thresholds will be set to –90, –45, 0, +45 and +90 in order.

The **Compute Thresholds** drop-down will set the thresholds from data of your choice obtained from the **root motions**Motion of character’s root node, whether it’s controlled by the animation itself or externally. [More info](RootMotion.html)  
See in [Glossary](Glossary.html#RootMotion) in the **Animation Clips**Animation data that can be used for animated characters or simple animations. It is a simple “unit” piece of motion, such as (one specific instance of) “Idle”, “Walk” or “Run”. [More info](class-AnimationClip.html)  
See in [Glossary](Glossary.html#AnimationClip). The data that is available to choose from is speed, velocity x, y, or z, and angular speed in degrees or radians. If your **parameter** corresponds to one of these properties, you can compute the thresholds using the Compute Thresholds drop-down.

| ***Property:*** | ***Function:*** |
| --- | --- |
| **Speed** | Sets the threshold of each motion according to its speed (the magnitude of the velocity). |
| **Velocity X** | Sets the threshold of each motion according to its velocity.x. |
| **Velocity Y** | Sets the threshold of each motion according to its velocity.y. |
| **Velocity Z** | Sets the threshold of each motion according to its velocity.z. |
| **Angular Speed (Rad)** | Sets the threshold of each motion according to its angular speed in radians per second. |
| **Angular Speed (Deg)** | Sets the threshold of each motion according to its angular speed in degrees per second. |

For example, you had a walk animation that covered 1.5 units per second, a jog at 2.3 units per second, and a run at 4 units per second, choosing the **Speed** option from the drop-down would set the parameter range and thresholds for the three animations based on these values. So, if you set the speed parameter to 3.0, it would blend the jog and run with a slight bias toward the jog.

Animation Blend Trees

2D Blending

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)