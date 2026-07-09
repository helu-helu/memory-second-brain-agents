* [Optimization](analysis.html)
* [Graphics performance and profiling](graphics-performance-profiling.html)
* [Optimize mesh rendering using level of detail (LOD)](lod-landing.html)
* [LOD Group](lod/lod-group-landing.html)
* LOD Group component reference

Make LOD transitions smooth in LOD Group

2D images for low level of detail (LOD)

# LOD Group component reference

[Switch to Scripting](../ScriptReference/LODGroup.html "Go to LODGroup page in the Scripting Reference")

The **LOD Group** component lets you manage [level of detail](LevelOfDetail.html)The *Level Of Detail* (LOD) technique is an optimization that reduces the number of triangles that Unity has to render for a GameObject when its distance from the Camera increases. [More info](LevelOfDetail.html)  
See in [Glossary](Glossary.html#levelofdetail) (LOD) for **GameObjects**The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject).

| **Property** | **Description** |
| --- | --- |
| **Fade Mode** | Selects the transition effect type to apply between LOD levels. The options are the following:  * **None**: Switches to the next LOD without a smooth transition. * **Cross Fade**: Applies a cross-fading effect to the model between the current and the next LOD. * **Speed Tree**: Interpolates the vertex positions of a SpeedTree model between the current and the next LOD. Applies only to SpeedTree models with .spm and .st extensions. For more information, refer to [Make LOD transitions smooth in LOD Group](lod/lod-transitions-lod-group.html). |
| **Animate Cross-fading** | Sets a single transition time for all LODs, which occurs after the LOD threshold is reached. This property is available only if you set **Fade Mode** to **Cross Fade** or **Speed Tree**. For more information, refer to [Make LOD transitions smooth in LOD Group](lod/lod-transitions-lod-group.html). |
| **LOD Group selection bar** | Displays the LOD levels as colored boxes. For more information, refer to the [LOD Group selection bar](#LODGroupSelectionBar) section. |
| **Recalculate Bounds** | Recalculates the **bounding volume**A closed shape representing the edges and faces of a collider or trigger. See in [Glossary](Glossary.html#boundingvolume) that encompasses all LODs. Use this after you modify a LOD, for example if you adjust the **Scale** of the **Transform** component of a LOD renderer. |
| **Recalculate **Lightmap**A pre-rendered texture that contains the effects of light sources on static objects in the scene. Lightmaps are overlaid on top of scene geometry to create the effect of lighting. [More info](Lightmapping.html) See in [Glossary](Glossary.html#Lightmap) Scale** | Updates the [Scale in Lightmap](class-MeshRenderer.html#lightmapping) property on all **Mesh**The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](mesh.html) See in [Glossary](Glossary.html#Mesh) Renderers in the LOD Group, based on any changes to the LOD level boundaries. |
| **Object Size** | Sets the size of the object in meters for LOD Group calculations. For example, if you change **Object Size** from 1 to 0.6, an object that has a screen height of 100% is now considered to have a screen height of 60%. As a result, the transitions to smaller screen height percentages and less detailed LOD levels occur closer to the **camera**A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](CamerasOverview.html) See in [Glossary](Glossary.html#Camera). |
| **Reset Object Size** | Resets **Object Size** to its default of 1, but recalculates LOD level boundaries so the transition distances in meters stay the same. |

## LOD Group selection bar

The LOD Group selection bar displays the LOD levels as colored boxes.

![LOD Group selection bar. Four colored boxes represent LOD 0, LOD 1, LOD 2, and culled. The percentages in the boxes represent when the LOD level becomes active. A camera icon is above the bar, and the current screen size ratio below.](../uploads/Main/LODGroup-selectionbar.png)


LOD Group selection bar. Four colored boxes represent LOD 0, LOD 1, LOD 2, and culled. The percentages in the boxes represent when the LOD level becomes active. A camera icon is above the bar, and the current screen size ratio below.

![A](../uploads/Main/LetterA.png) LOD level box. Displays a percentage of the screen height. The LOD level is active between this height and the height in the next LOD level box. For example, 50% means the LOD level becomes active when the object fills half the height of the camera view.

![B](../uploads/Main/LetterB.png) When you drag the camera icon, the **Scene** view displays the LOD level the camera renders at that ratio. The rectangle around the object is the bounding box of the object.

**Note:** Unity only displays the LOD label in the **Scene view**An interactive view into the world you are creating. You use the Scene View to select and position scenery, characters, cameras, lights, and all other types of Game Object. [More info](UsingTheSceneView.html)  
See in [Glossary](Glossary.html#SceneView) when a single GameObject is selected.

![C](../uploads/Main/LetterC.png) LOD level boundary. To change when the LOD level becomes active, select and drag the boundary.

**Note:** To preview LODs without the rest of the Scene view turning gray, from the main menu go to **Preferences** > **Scene View** and disable **Enable Filtering While Editing LOD Groups**.

## Renderers panel

To display the **Renderers** panel, select a LOD level box in the LOD Group selection bar.

| **Property** | **Description** |
| --- | --- |
| **Transition (% Screen Size)** | Sets the height of the object when the LOD level transitions to the next LOD level, as a percentage of the screen height.  To the right of this property, Unity displays the camera distance at which the LOD level transitions, in meters. |
| **Set to Camera** | Sets the **Transition (% Screen Size)** value to the height of the object in the current camera view. |
| **Fade Transition Width** | Sets the transition width between this LOD level and the next. A smaller value delays the beginning of the transition and makes the transition shorter. For example, if you set the **Fade Transition Width** of LOD0 to 0.4, the transition to LOD1 occurs over 40% of the LOD0 range. This property is only available if you set **Fade Mode** to **Cross Fade** and disable **Animate Cross-fading**.  For more information, refer to [Make LOD transitions smooth in LOD Group](lod/lod-transitions-lod-group.html). |
| **Renderers** | The Renderers to render at this LOD level. To add Renderers, select the **Add** (**+**) button, then select the Renderer picker (**⊙**) or drag and drop to add the GameObject that contains the Renderers.  For more information, refer to [Import or create LOD levels for a LOD Group](lod-group-configure.html). |

## Additional resources

* [Make LOD Group transitions smooth](lod/lod-transitions-lod-group.html)

LODGroup

Make LOD transitions smooth in LOD Group

2D images for low level of detail (LOD)

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)