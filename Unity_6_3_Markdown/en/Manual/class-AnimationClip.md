* [Assets and media](assets-and-media.html)
* [Types of assets](AssetTypes.html)
* [Models](models.html)
* [Importing models into Unity](models-importing.html)
* Animation tab

Rig tab Import Settings reference

Materials tab

# Animation tab

[Switch to Scripting](../ScriptReference/AnimationClip.html "Go to AnimationClip page in the Scripting Reference")

**Animation Clips** are the smallest building blocks of animation in Unity. They represent an isolated piece of motion, such as RunLeft, Jump, or Crawl, and can be manipulated and combined in various ways to produce lively end results (see [Animation State Machines](AnimationStateMachines.html)A graph within an Animator Controller that controls the interaction of Animation States. Each state references an Animation Blend Tree or a single Animation Clip. [More info](AnimationStateMachines.html)  
See in [Glossary](Glossary.html#AnimationStateMachine), [Animator Controller](class-AnimatorController.html)Controls animation through Animation Layers with Animation State Machines and Animation Blend Trees, controlled by Animation Parameters. The same Animator Controller can be referenced by multiple models with Animator components. [More info](class-AnimatorController.html)  
See in [Glossary](Glossary.html#AnimatorController), or [Blend Trees](class-BlendTree.html)).
You can select Animation Clips from imported FBX data.

When you click on the model containing animation clips, these properties appear:

![The Animation Clip Inspector](../uploads/Main/classAnimationClip-Inspector.png)


The Animation Clip Inspector

There are five areas on the **Animation** tab of the **Inspector**A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector) window:

**(A)** [Asset-specific properties](#AssetProperties). These settings define import options for the entire Asset.

**(B)** [Clip selection list](#ClipSelectionList). You can select any item from this list to display its properties and preview its animation. You can also [define new clips](Splittinganimations.html).

**(C)** [Clip-specific properties](#ClipProperties). These settings define import options for the selected **Animation Clip**.

**(D)** [Clip properties](#AllClipProperties). These settings define import options for all Animation clips.

**(E)** [Animation preview](#AnimationPreview). You can playback the animation and select specific frames here.

## Asset-specific properties

![Import options for the entire Asset](../uploads/Main/classAnimationClip-Inspector_Asset.png)


Import options for the entire Asset

These properties apply to all animation clips and constraints defined within this Asset:

| **Property** | **Function** |
| --- | --- |
| **Import Constraints** | Import [constraints](Constraints.html)Settings on Joint components which limit movement or rotation. The type and number of constraints vary depending on the type of Joint. [More info](2d-physics/joints/2d-joints-landing.html) See in [Glossary](Glossary.html#constraints) from this asset. |
| **Import Animation** | Import animation from this asset.   **Note:** If disabled, all other options on this page are hidden and no animation is imported. |
| **Bake Animations** | Bake animations created using IK or Simulation to forward kinematic keyframes.   Only available for Autodesk® Maya®, Autodesk® 3ds Max® and Cinema 4D files. |
| **Resample Curves** | Resample animation curves as Quaternion values and generate a new Quaternion keyframe for every frame in the animation.   This option only appears if the import file contains Euler curves. This option is enabled by default.  Disable this option to [keep animation curves as they were originally authored](AnimationEulerCurveImport.html). You should only disable this option if there are interpolation issues in the resampled animation when compared with your original animation. |
| **Anim. Compression** | The type of compression to use when importing the animation.  * **Off**: Disable animation compression. This means that Unity doesn’t reduce keyframe count on import. Disabling animation compression leads to the highest precision animations, but slower performance and bigger file and runtime memory size. It is generally not advisable to use this option. If you need higher precision animation, you should enable keyframe reduction and lower allowed **Animation Compression Error** values instead. * **Keyframe Reduction**A process that removes redundant keyframes. [More info](class-AnimationClip.html#AssetProperties) See in [Glossary](Glossary.html#KeyframeReduction): Reduce redundant keyframes on import. If enabled, the Inspector displays **Animation Compression Errors** options. This affects both file size (runtime memory) and how curves are evaluated. Applies to **Legacy**, **Generic**, and **Humanoid** [Animation Type](FBXImporter-Rig.html) rigs. * **Keyframe Reduction and Compression**: Reduce keyframes on import and compress keyframes when storing animations in files. This affects only file size. The runtime memory size is the same as **Keyframe Reduction**. If enabled, the Inspector displays **Animation Compression Errors** options. Only for **Legacy** [Animation Type](FBXImporter-Rig.html) rigs. * **Optimal** :Let Unity decide how to compress, either by keyframe reduction or by using dense format. If enabled, the Inspector displays **Animation Compression Errors** options. Only for **Generic** and **Humanoid** [Animation Type](FBXImporter-Rig.html) rigs. |
| **Animation Compression Errors** | Only available when **Keyframe Reduction** or **Optimal** compression is enabled.  * **Rotation Error**: Set the error tolerance (as an angle in degrees) for rotation curve compression. Unity uses this to determine whether or not it can remove a key on a rotation curve. This represents the minimum angle between the original rotation value and the reduced value: `Angle(value, reduced) < RotationError` * **Position Error**: Set the error tolerance (as a percentage) for position curve compression. Unity uses this to determine whether or not it can remove a key on a position curve. For more information, see [Setting error tolerance for key reduction on position and scale curves](#tolerance). * **Scale Error**: Set the error tolerance (as a percentage) for scale curve compression. Unity uses this to determine whether or not it can remove a key on a scale curve. For more information, see [Setting error tolerance for key reduction on position and scale curves](#tolerance). |
| **Animated Custom Properties** | Import any FBX properties that you designated as custom user properties.   Unity only supports a small subset of properties when importing FBX files (such as translation, rotation, scale and visibility). However, you can treat standard FBX properties like user properties by naming them in your importer script via the [extraUserProperties](../ScriptReference/ModelImporter-extraUserProperties.html) member. During import, Unity then passes any named properties to [the Asset postprocessor](../ScriptReference/AssetPostprocessor.OnPostprocessGameObjectWithUserProperties.html) just like ‘real’ user properties. |

### Setting error tolerance for key reduction on position and scale curves

Set the error tolerance percentage to determine whether or not Unity can remove a key on a position or scale curve as a strategy for animation **compression**A method of storing data that reduces the amount of storage space it requires. See [Texture Compression](texture-choose-format-by-platform.html), [Animation Compression](class-AnimationClip.html#AssetProperties), [Audio Compression](class-AudioClip.html), [Build Compression](ReducingFilesize.html).  
See in [Glossary](Glossary.html#compression).

When you set the **Anim. Compression** property to ****Keyframe**A frame that marks the start or end point of a transition in an animation. Frames in between the keyframes are called inbetweens.  
See in [Glossary](Glossary.html#keyframe) Reduction** or **Optimal**, Unity compares the original curve to what the curve looks like after removing a specific keyframe and applies this test:

```
OriginalValue - ReducedValue > OriginalValue * percentageOfError
```

Unity removes a keyframe if the delta between the original value and the reduced value is less than the original value multiplied by the error tolerance percentage.

Note that Unity compares the distances between the three curve components (it compares `distance(x,y,z)` ), and also per component ( `distance(x)`, `distance(y)`, and then `distance(z)`).

This example demonstrates how Unity evaluates a reduction on the y-axis using an error tolerance of 10%:

![Define a position error of 10% on a simple animation of a translation on the y-axis](../uploads/Main/classAnimationClip-tolerance_Ex1.png)


Define a position error of 10% on a simple animation of a translation on the y-axis


![Keyframe A has a value of 11.2](../uploads/Main/classAnimationClip-tolerance_Ex2.png)


Keyframe A has a value of 11.2


![Keyframe B has a value of 11.1](../uploads/Main/classAnimationClip-tolerance_Ex3.png)


Keyframe B has a value of 11.1


![The resulting reduced curve](../uploads/Main/classAnimationClip-tolerance_Ex4.png)


The resulting reduced curve

**Keyframe A is not reduced** because:

* The distance between the original and reduced value is `D = 11.2 - 10 = 1.2`.
* The error margin is `E = 10% * 11.2 = 1.12`
* **D > E**

**Keyframe B is reduced** because `11.1 - 10 < 10% * 11.1`:

* The distance between the original and reduced value is `D = 11.1 - 10 = 1.11`
* The error margin is `E = 10% * 11.1 = 1.11`
* **D = E**

Note that this method has a limitation when using high values that vary only slightly. Moving the **Scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) 1000 units away results in essentially the same animation but located far from 0.

![High values with small variance](../uploads/Main/classAnimationClip-tolerance_Ex5.png)


High values with small variance

In this case, both keyframes are reduced.

**Keyframe A is reduced** because:

* The distance between the original and reduced value is `D = 1011.2 - 1010 = 1.2`
* The error margin is `E = 10% * 1011.2 = 101.12`

**Keyframe B is reduced** because `11.1 - 10 < 10% * 11.1`:

* The distance between the original and reduced value is `D = 11.1 - 10 = 1.11`
* The error margin is `E = 10% * 1011.1 = 101.11`

Higher values require a much larger difference between the original and reduced values for keyframes to remain in the reduced curve. Keyframe A has a value of 1100 and is discarded; keyframe B has a value of 1112 and remains:

![Higher values require a much larger difference](../uploads/Main/classAnimationClip-tolerance_Ex6.png)


Higher values require a much larger difference

## Clip selection list

![List of clips defined in this file](../uploads/Main/classAnimationClip-Inspector_Selection.png)


List of clips defined in this file

You can perform these tasks in this area of the **Animation** tab:

* Select a clip from the list to [display its clip-specific properties](#ClipProperties).
* Play a selected clip in the [clip preview pane](#AnimationPreview).
* [Create a new clip](Splittinganimations.html) for this file with the add (`+`) button.
* Remove the selected clip definition with the delete (`-`) button.

If you manually change properties of imported clips, Unity does not import new animation clips when the source Asset changes. For example, if you create a new clip or change a clip timing on the **Animation** tab, the clip list does not update even if you add clips to the FBX file from outside Unity. To view new and changed animation clips, you must [add a new source take to the clip list](Splittinganimations.html).

## Clip-specific properties

![Import options for the selected Animation clip](../uploads/Main/classAnimationClip-Inspector_Clip.png)


Import options for the selected Animation clip

This area of the **Animation** tab displays these features:

**(A)** The editable name of the [selected source take](#takename).
**(B)** The animation [clip timeline](#cliptiming).
**(C)** Clip properties to control [looping](#cliptiming) and **root motion**Motion of character’s root node, whether it’s controlled by the animation itself or externally. [More info](RootMotion.html)  
See in [Glossary](Glossary.html#RootMotion) extraction properties for [transform rotation](#rootrotation), [transform position Y](#roottransformy), and [transform position XZ](#roottransformxz). These features also include [additional properties](#additionalprops) for reference pose, curves, events, and **Avatar**An interface for retargeting animation from one rig to another. [More info](ConfiguringtheAvatar.html)  
See in [Glossary](Glossary.html#Avatar) masks.

You can set these properties separately for each animation clip defined within this asset.

### Source Take name

| **Property** | **Function** |
| --- | --- |
| The name of the source take **source take name** | The name of the source take in the source file. Source files contain a set of source takes that are created in external 3D applications such as Motionbuilder or Autodesk® Maya®.  You can import source takes as individual Animation clips. You can also [create Animation clips from a subset of frames](Splittinganimations.html). |

### Clip timing

| **Property** | **Function** |
| --- | --- |
| The timeline editor **The timeline editor** | Drag the start and end indicators on the animation timeline to define frame ranges for each clip.  Creating clips is essentially defining the start and end points for segments of animation. [To define a looping clip](LoopingAnimationClips.html), trim the start and end points so that the first and last frames match as best as possible. You can also zoom and scroll the timeline to be more precise. |
| **Start** | Start frame of the clip. |
| **End** | End frame of the clip. |
| **Loop Time** | Play the animation clip through and restart when the end is reached. |
| **Loop Pose** | Loop the motion seamlessly. |
| **Cycle Offset** | Offset to the cycle of a looping animation, if it starts at a different time. |

### Root Transform Rotation

| **Property** | **Function** |
| --- | --- |
| **Bake into Pose** | Bake root rotation into the movement of the bones. Disable to store as root motion. |
| **Based Upon** | Basis of root rotation.  * **Original**:Keep the original rotation from the source file. * **Root Node Rotation**: Use the rotation of the root node. Only available for the **Generic** [Animation Type](FBXImporter-Rig.html). * **Body Orientation**: Keep the upper body pointing forward. Only available for the **Humanoid** [Animation Type](FBXImporter-Rig.html). |
| **Offset** | Offset to the root rotation (in degrees). |

### Root Transform Position (Y)

| **Property** | **Function** |
| --- | --- |
| **Bake into Pose** | Bake vertical root motion into the movement of the bones. Disable to store as root motion. |
| **Based Upon (at Start)** | Basis of vertical root position.  * **Original**: Keep the vertical position from the source file. * **Root Node Position**: Use the vertical root position. Only available for the **Generic** [Animation Type](FBXImporter-Rig.html). * **Center of Mass**Represents the average position of all mass in a Rigidbody for the purposes of physics calculations. By default it is computed from all colliders belonging to the Rigidbody, but can be modified via script. [More info](../ScriptReference/Rigidbody-centerOfMass.html) See in [Glossary](Glossary.html#centerofmass): Keep center of mass aligned with the root transform position. Only available for the **Humanoid** [Animation Type](FBXImporter-Rig.html). * **Feet**: Keep feet aligned with the root transform position. Only available for the **Humanoid** [Animation Type](FBXImporter-Rig.html). |
| **Offset** | Offset to the vertical root position. |

### Root Transform Position (XZ)

| **Property** | **Function** |
| --- | --- |
| **Bake into Pose** | Bake horizontal root motion into the movement of the bones. Disable to store as root motion. |
| **Based Upon** | Basis of horizontal root position.  * **Original**: Keep the horizontal position from the source file. * **Root Node Position**: Use the horizontal root transform position. Only available for the **Generic** [Animation Type](FBXImporter-Rig.html). * **Center of Mass**: Keep aligned with the root transform position. Only available for the **Humanoid** [Animation Type](FBXImporter-Rig.html). |
| **Offset** | Offset to the horizontal root position. |

### Additional clip properties

| **Property** | **Function** |
| --- | --- |
| **Mirror** | Mirror left and right in this clip. Only appears if the [Animation Type](FBXImporter-Rig.html) is set to **Humanoid**. |
| **Additive Reference Pose** | Enable to set frame for the reference pose used as the base for the [additive animation layer](AnimationLayers.html). A blue marker becomes visible in the timeline editor:  Additive Reference Pose blue marker |
| **Pose Frame** | Enter a frame number to use as the reference pose. You can also drag the blue marker in the timeline to update this value. Only available if **Additive Reference Pose** is enabled. |
| **Curves** | Expand this section to manage [animation curves for this animation clip](AnimationCurvesOnImportedClips.html). |
| **Events** | Expand this section to manage [animation events for this animation clip](script-AnimationWindowEvent.html). |
| **Mask**Can refer to a Sprite Mask, a UI Mask, or a Layer Mask [More info](https://docs.unity3d.com/Packages/com.unity.ugui@latest/index.html?subfolder=/manual/script-Mask.html) See in [Glossary](Glossary.html#mask) | Expand this section to manage Avatar [masking for this animation clip](class-AvatarMask.html). |

## Properties for all clips

These expandable properties apply to all Animation clips being imported.

![Import options for all Animation clips](../uploads/Main/classAnimationClip-Inspector_AllClips.png)


Import options for all Animation clips

| **Property:** | **Function:** |
| --- | --- |
| **Motion** | Select the root motion node source of the clip. Choose from the following options:  * **None**: Use the default designated node. * **Root Transform**: Use the transform of the root. * **Mesh object and child objects**: The menu displays all of the model’s objects and child objects, which you can use as the root motion node. |
| **Import Messages** | Expand this section to see detailed [information about how your animation was imported](#ImportMessages), including an optional ***Retargeting**Applying animations created for one model to another. [More info](Retargeting.html) See in [Glossary](Glossary.html#retargeting) Quality Report*. |

## Animation import warnings

If any problems occur during the animation import process, a warning appears at the top of the Animations Import inspector:

![Animation import warning messages](../uploads/Main/AnimationWarningBox.png)


Animation import warning messages

The warnings do not necessarily mean your animation has not imported or doesn’t work. It may just mean that the imported animation looks slightly different from the source animation.

To see more information, expand the **Import Messages** section:

![Animation import warning messages](../uploads/Main/AnimationWarningSection.png)


Animation import warning messages

In this case, Unity has provided a **Generate Retargeting Quality Report** option which you can enable to see more specific information on the retargeting problems.

Other warning details you may see include the following:

* Default bone length found in this file is different from the one found in the source avatar.
* Inbetween bone default rotation found in this file is different from the one found in the source avatar.
* Source avatar hierarchy doesn’t match one found in this model.
* This animation has Has translation animation that will be discarded.
* **Humanoid animation**An animation using humanoid skeletons. Humanoid models generally have the same basic structure, representing the major articulate parts of the body, head and limbs. This makes it easy to map animations from one humanoid skeleton to another, allowing retargeting and inverse kinematics. [More info](ConfiguringtheAvatar.html)  
  See in [Glossary](Glossary.html#Humanoidanimation) has inbetween transforms and rotation that will be discarded.
* Has scale animation that will be discarded.

These messages indicate that some data present in your original file was omitted when Unity imported and converted your animation to its own internal format. These warnings essentially tell you that the retargeted animation may not exactly match the source animation.

**Note:** Unity does not support pre- and post-extrapolate modes (also known as pre- and post-infinity modes) other than **constant**, and converts these to **constant** when imported.

## Animation preview

![Animation clip preview](../uploads/Main/classAnimationClip-Inspector_Preview.png)


Animation clip preview

The preview area of the **Animation** tab provides these features:

**(A)** The name of the selected clip.

**(B)** The [2D](Unity2D.html) preview mode button (switches between orthographic and perspective camera).

**(C)** The pivot and mass center display button (switches between displaying and hiding the gizmos).

**(D)** The Avatar selector (change which GameObject will preview the action).

**(E)** The play/pause button.

**(F)** The playback head on the preview timeline (allows scrubbing back and forth).

**(G)** The animation preview speed slider (move left to slow down; right to speed up).

**(H)** The playback status indicator (displays the location of the playback in seconds, percentage, and frame number).

**(I)** The **Tag**  
See in [Glossary](Glossary.html#tag) bar, where you can define and apply [Tags](Tags.html) to your clip.

**(J)** The [AssetBundles](AssetBundlesIntro.html) bar, where you can [define AssetBundles and Variants](AssetBundles-Building.html).

AnimationClip

Rig tab Import Settings reference

Materials tab

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)