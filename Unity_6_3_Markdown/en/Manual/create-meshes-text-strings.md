* [Assets and media](assets-and-media.html)
* [Types of assets](AssetTypes.html)
* [Meshes](mesh.html)
* [Text meshes](text-meshes.html)
* Create meshes for text strings

Text meshes

Text Mesh component reference

# Create meshes for text strings

To create meshes for text strings, use the [Text Mesh](class-TextMesh.html)A Mesh component that displays a Text string [More info](class-TextMesh.html)  
See in [Glossary](Glossary.html#TextMesh) component. The **Text **Mesh**The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](mesh.html)  
See in [Glossary](Glossary.html#Mesh)** component generates 3D geometry that displays text strings.

**Note:** The Text Mesh component has limited functionality. For information on more recent, full-featured ways of displaying text, see [Creating user interfaces (UI)](UIToolkits.html).

Text Meshes can be used for rendering road signs, graffiti etc. The Text Mesh places text in the 3D **scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene). To make generic 2D text for GUIs, use a GUI Text component instead.

Follow these steps to create a Text Mesh with a custom Font:

1. Import a TrueType font by dragging a .ttf file into the **Project** window.
2. In the **Hierarchy** window, select **Create** > **3D Object** > **Legacy** > **TextMesh**.
3. Drag the imported font from the **Project** window to the **Font** property of the Text Mesh component in the ****Inspector**A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
   See in [Glossary](Glossary.html#Inspector)** window.

You have now created a text mesh with your custom TrueType Font. You can scale the text and move it around using the ****Scene View**An interactive view into the world you are creating. You use the Scene View to select and position scenery, characters, cameras, lights, and all other types of Game Object. [More info](UsingTheSceneView.html)  
See in [Glossary](Glossary.html#SceneView)’s** **Transform** controls.

**Note:** If you want to change the font for a Text Mesh, need to set the component’s font property and also set the texture of the font material to the correct font texture. This texture can be located using the font asset’s foldout. If you forget to set the texture then the text in the mesh will appear blocky and misaligned.

## Best practices

* If you are scripting the **Text** property, you can add line breaks by inserting the escape character “\n” in your strings.
* You can use simple markup to style text meshes. See the [Styled Text](text-meshes.html) page for more details.
* Fonts in Unity render the font glyphs to a texture map before any further rendering. If the font size is set too small, these font textures will appear blocky. Since TextMesh assets are rendered using **quads**A primitive object that resembles a plane but its edges are only one unit long, it uses only 4 vertices, and the surface is oriented in the XY plane of the local coordinate space. [More info](PrimitiveObjects.html)  
  See in [Glossary](Glossary.html#Quad), it’s possible that if the size of the TextMesh and font texture differ, the TextMesh might display incorrectly.

Text meshes

Text Mesh component reference

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)