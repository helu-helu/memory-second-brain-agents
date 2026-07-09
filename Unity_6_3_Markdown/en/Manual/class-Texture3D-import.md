* [Materials and shaders](materials-and-shaders.html)
* [Custom textures](Textures-landing.html)
* [3D textures](class-Texture3D.html)
* Create a 3D texture

Introduction to 3D textures

Preview a 3D texture

# Create a 3D texture

A 3D texture is a bitmap image that contains information in three dimensions rather than the standard two. 3D textures are commonly used to simulate volumetric effects such as fog or smoke, to approximate a volumetric 3D **mesh**The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](mesh.html)  
See in [Glossary](Glossary.html#Mesh), or to store animated textures and blend between them.

To create a 3D texture, import a 2D texture with the following properties:

* Flipbook format - a single 2D texture arranged as regular cells.
* Maximum size of 2048 × 2048 × 2048 **pixels**The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](ShadowPerformance.html)  
  See in [Glossary](Glossary.html#pixel).

The size of a 3D texture on disk and in memory increases quickly as its resolution increases. For example, a 3D texture with [`RGBAFloat`](../ScriptReference/TextureFormat.RGBAFloat.html) format, no mipmaps, and a size of 32 × 32 × 32 pixels has a size of 512 KB (32 × 32 × 32 × 16 bytes) in memory. If you increase the resolution to 256 × 256 × 256 pixels, the size in memory becomes 256 MB (256 × 256 × 256 × 16 bytes).

Follow these steps to import:

1. Import the texture into your project.
2. In the **Project** window, select the texture asset. Unity displays the texture import settings in the ****Inspector**A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
   See in [Glossary](Glossary.html#Inspector)** window.
3. In the **Inspector** window, set **Texture Shape** to **3D**.
4. Set **Columns** and **Rows** to the appropriate values for your flipbook texture.
5. Select **Apply**.

Unity adds a 3D texture slice for each cell in the texture.

![Flipbook image as a 2D texture](../uploads/Main/TextureImporter-Flipbook-2D.jpg)
  
An imported flipbook texture with 8 columns and 8 rows.

![Flipbook image as a 3D texture](../uploads/Main/TextureImporter-Flipbook-3D.jpg)
  
The texture after you set **Texture Shape** to **3D**, **Columns** to **8**, and **Rows** to **8**.

Refer to [Importing textures](ImportingTextures.html) for more information.

## Additional resources

* [Free VFX image sequences and flipbooks](https://blog.unity.com/engine-platform/free-vfx-image-sequences-flipbooks)

Introduction to 3D textures

Preview a 3D texture

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)