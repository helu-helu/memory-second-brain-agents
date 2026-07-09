* [Animation](AnimationSection.html)
* [Mecanim Animation system](animation-mecanim.html)
* [Humanoid Avatar](AvatarCreationandSetup.html)
* Inverse Kinematics

Retarget Humanoid animations

How Root Motion works

# Inverse Kinematics

Most character animation is created by rotating the angles of joints in a skeleton to predetermined values. The position of a child **joint**A physics component allowing a dynamic connection between Rigidbody components, usually allowing some degree of movement such as a hinge. [More info](Joints.html)  
See in [Glossary](Glossary.html#joint) changes according to the rotation of its parent. The end point of a chain of joints is determined by the angles and relative positions of the individual joints along the chain. This method of posing a skeleton is known as **forward **kinematics**The geometry that describes the position and orientation of a character’s joints and bodies. Used by inverse kinematics to control character movement.  
See in [Glossary](Glossary.html#kinematics)**.

However, it is often useful to pose joints from the opposite point of view. Start from a chosen position in space, or a goal, and work backwards to find a way to orient the joints so that the end point reaches the goal. This can be useful if you want a character to grab an object or stand on an uneven surface. This approach is known as **inverse kinematics** (IK). It is supported in Mecanim for a humanoid character with a correctly configured **Avatar**An interface for retargeting animation from one rig to another. [More info](ConfiguringtheAvatar.html)  
See in [Glossary](Glossary.html#Avatar).

![The Kyle character holding a cylinder.](../uploads/Main/MecanimIKGrabbing.jpg)


The Kyle character holding a cylinder.

To set up IK for a character, you typically have objects around the **scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) that a character interacts with. You can use these objects and your character to set up IK within a script. You can use the following Animator functions:

* [SetIKPositionWeight](../ScriptReference/Animator.SetIKPositionWeight.html)
* [SetIKRotationWeight](../ScriptReference/Animator.SetIKRotationWeight.html)
* [SetIKPosition](../ScriptReference/Animator.SetIKPosition.html)
* [SetIKRotation](../ScriptReference/Animator.SetIKRotation.html)
* [SetLookAtPosition](../ScriptReference/Animator.SetLookAtPosition.html)
* [bodyPosition](../ScriptReference/Animator-bodyPosition.html)
* [bodyRotation](../ScriptReference/Animator-bodyRotation.html)

For example, the image above shows a character touching a cylindrical object. To do this with IK and through scripting, follow these steps:

1. Create a valid Avatar for your character.
2. Create an **Animator Controller**Controls animation through Animation Layers with Animation State Machines and Animation Blend Trees, controlled by Animation Parameters. The same Animator Controller can be referenced by multiple models with Animator components. [More info](class-AnimatorController.html)  
   See in [Glossary](Glossary.html#AnimatorController) with at least one animation for this character.
3. In the Layers pane of the **Animator window**The window where the Animator Controller is visualized and edited. [More info](AnimatorWindow.html)  
   See in [Glossary](Glossary.html#AnimatorWindow), click the Cog icon in the Base Layer and enable **IK Pass** from the context menu. When enabled, IK Pass sends an `OnAnimatorIK` callback. In a later step, you will use this callback to implement inverse kinematics in a script.

   ![Enable the IK Pass checkbox for the Default Layer.](../uploads/Main/AnimatorControllerToolSettingsIKPass.png)


   Enable the IK Pass checkbox for the Default Layer.
4. Make sure the Animator Controller is assigned to the character’s Animator Controller.

   ![The Animator Controller component assigned to the characters Animator Controller.](../uploads/Main/AnimatorInspectorForIK.png)


   The Animator Controller component assigned to the character’s Animator Controller.
5. Next, add a script to your character. In this example, the script is named `IKControl`. This script sets the IK target for the right hand of the character. This script also changes the look at position so that the character looks towards the cylinder object when grabbed. The full script is listed below:

   ```
   using UnityEngine;
   using System;
   using System.Collections;

   [RequireComponent(typeof(Animator))]
   public class IKControl : MonoBehaviour {

       protected Animator animator;

       public bool ikActive = false;
       public Transform rightHandObj = null;
       public Transform lookObj = null;

       void Start ()
       {
           animator = GetComponent<Animator>();
       }

       //a callback for calculating IK
       void OnAnimatorIK()
       {
           if(animator) {
          
               //if the IK is active, set the position and rotation directly to the goal.
               if(ikActive) {

                   // Set the look target position, if one has been assigned
                   if(lookObj != null) {
                       animator.SetLookAtWeight(1);
                       animator.SetLookAtPosition(lookObj.position);
                   }

                   // Set the right hand target position and rotation, if one has been assigned
                   if(rightHandObj != null) {
                       animator.SetIKPositionWeight(AvatarIKGoal.RightHand,1);
                       animator.SetIKRotationWeight(AvatarIKGoal.RightHand,1);  
                       animator.SetIKPosition(AvatarIKGoal.RightHand,rightHandObj.position);
                       animator.SetIKRotation(AvatarIKGoal.RightHand,rightHandObj.rotation);
                   }
               }

               //if the IK is not active, set the position and rotation of the hand and head back to the original position
               else {          
                   animator.SetIKPositionWeight(AvatarIKGoal.RightHand,0);
                   animator.SetIKRotationWeight(AvatarIKGoal.RightHand,0);
                   animator.SetLookAtWeight(0);
               }
           }
       }
   }
   ```
6. To avoid the right hand passing through the Cylinder **GameObject**The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)  
   See in [Glossary](Glossary.html#GameObject), add an empty child GameObject to the `Cylinder` GameObject. To do this, right-click the Cylinder GameObject in the Hierarchy window and select **Create Empty**. Name this empty child GameObject `Cylinder Grab Handle`.
7. Position and rotate the `Cylinder Grab Handle` GameObject so that the right hand touches but does not pass through the cylinder.

   ![An empty GameObject acts as the IK target. Add this empty GameObject so that the right hand interacts with the Cylinder object.](../uploads/Main/MecanimIKGrabHandle.jpg)


   An empty GameObject acts as the IK target. Add this empty GameObject so that the right hand interacts with the Cylinder object.
8. Assign the `Cylinder Grab Handle` GameObject as the **Right Hand Obj** property of the `IKControl` script.
9. Assign the `Cylinder` GameObject as the **Look Obj** so that the character looks towards the center of the Cylinder when **IK Active** is enabled.

   ![The IKControl (Script) component with its properties assigned.](../uploads/Main/MecanimIKSetupInspector.png)


   The IKControl (Script) component with its properties assigned.
10. Enter play mode.
    Your character should touch and release the Cylinder GameObject as you enabled and disable the **IK Active** checkbox. While in Play Mode, change the position and rotation of the `Cylinder` GameObject to see how the right hand and character look at reacts.

Retarget Humanoid animations

How Root Motion works

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)