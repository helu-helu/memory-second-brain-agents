* [Animation](AnimationSection.html)
* [Mecanim Animation system](animation-mecanim.html)
* [Animation clips](animation-clips-landing.html)
* [Animation window](AnimationEditorGuide.html)
* Work with blend shapes

Add an Animation Event

Euler curve resampling

# Work with blend shapes

## Prepare the artwork

Once you have set up blend shapes in your 3D modeling application, do the following:

1. In your 3D modeling application, enable these export settings:
   * Enable exporting animation.
   * Enable exporting blend shapes for deformed models.
2. Export your selection to an .fbx file.
3. [Import your FBX file](ImportingModelFiles.html) into Unity.
4. Select the newly imported Model in the Hierarchy window. The **Inspector**A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
   See in [Glossary](Glossary.html#Inspector) window displays the **BlendShapes** section containing all the blend shapes under the [SkinnedMeshRenderer](class-SkinnedMeshRenderer.html) component.
5. For each listed blend shape, you can change its influence (weighting) to the default shape, where:
6. `0` means the blend shape has no influence.
7. `100` means the blend shape has full influence.

## Create animations In Unity

To create a blend animation:

1. Open the Animation window (from the main Unity menu: **Window** > **Animation** > **Animation**).
2. Select the **Animation Clip**Animation data that can be used for animated characters or simple animations. It is a simple “unit” piece of motion, such as (one specific instance of) “Idle”, “Walk” or “Run”. [More info](class-AnimationClip.html)  
   See in [Glossary](Glossary.html#AnimationClip) where you want to add the blend shape animation. You can select **Create New Clip** to create a new Animation Clip.
3. Click **Add Property** and select **[Your Character]** > **[Your Character Body]** > **Skinned Mesh Renderer** and select the blend shape you want to animate.
4. Select the added blend shape property, adjusting the **keyframes**A frame that marks the start or end point of a transition in an animation. Frames in between the keyframes are called inbetweens.  
   See in [Glossary](Glossary.html#keyframe) and blend weights, and set keyframes.

To preview your animation, click **Play** in the Editor window or the Animation window.

## Scripting access

You can also set the blend weights through scripting using functions like [GetBlendShapeWeight](../ScriptReference/SkinnedMeshRenderer.GetBlendShapeWeight.html) and [SetBlendShapeWeight](../ScriptReference/SkinnedMeshRenderer.SetBlendShapeWeight.html).

To check how many blend shapes a **Mesh**The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](mesh.html)  
See in [Glossary](Glossary.html#Mesh) has, use the [blendShapeCount](../ScriptReference/Mesh-blendShapeCount.html) variable.

This code example demonstrates how to blend a default shape into two other blend shapes over time when attached to a **GameObject**The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) with three or more blend shapes:

```
using UnityEngine;
using System.Collections;

public class BlendShapeExample : MonoBehaviour
{
    int blendShapeCount;
    SkinnedMeshRenderer skinnedMeshRenderer;
    Mesh skinnedMesh;
    float blendOne = 0f;
    float blendTwo = 0f;
    float blendSpeed = 1f;
    bool blendOneFinished = false;

    void Awake ()
    {
        skinnedMeshRenderer = GetComponent<SkinnedMeshRenderer> ();
        skinnedMesh = GetComponent<SkinnedMeshRenderer> ().sharedMesh;
    }

    void Start ()
    {
        blendShapeCount = skinnedMesh.blendShapeCount;
    }

    void Update ()
    {
        if (blendShapeCount > 2) {
            if (blendOne < 100f) {
                skinnedMeshRenderer.SetBlendShapeWeight (0, blendOne);
                blendOne += blendSpeed;
            } else {
                blendOneFinished = true;
            }

            if (blendOneFinished == true && blendTwo < 100f) {
                skinnedMeshRenderer.SetBlendShapeWeight (1, blendTwo);
                blendTwo += blendSpeed;
            }
        }
    }
}
```

Add an Animation Event

Euler curve resampling

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)