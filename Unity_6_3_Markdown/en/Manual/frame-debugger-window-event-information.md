* [Optimization](analysis.html)
* [Graphics performance and profiling](graphics-performance-profiling.html)
* [Graphics performance and profiling reference](profiling-landing.html)
* Frame Debugger Event Information reference

Frame Debugger window reference

Rendering Statistics window reference

# Frame Debugger Event Information reference

The Event Information Panel in the [Frame Debugger window](frame-debugger-window.html) displays information about the event such as geometry details and the **shader**A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#shader) used for a draw call.

![The Event Information Panel showing the URP sample scene. The top bar has selectors for the render target, color channels, and levels (A, B, and C). The central area is the mesh preview (D). The bottom area lists event properties (E).](../uploads/Main/frame-debugger-window-event-information.png)


The Event Information Panel showing the URP sample scene. The top bar has selectors for the render target, color channels, and levels (A, B, and C). The central area is the mesh preview (D). The bottom area lists event properties (E).

| **Label** | **Description** |
| --- | --- |
| **A** | **Render target selector**: When rendering into multiple render targets (such as multiple [RenderTextures](class-RenderTexture.html) or when also rendering to depth), this specifies which render target to display in the Game view. This is useful for example to view individual render targets in a G-buffer. |
| **B** | **Color channel selector**: Specifies which color channels of the render target to display. |
| **C** | **Levels**: Controls the black and white intensity. Use this to isolate areas of the Game view based on light intensity. |
| **D** | **Output / **Mesh**The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](mesh.html) See in [Glossary](Glossary.html#Mesh) Preview**: Displays a preview of the selected event output as well as the mesh geometry in the event. For more information, see [Preview](#preview). |
| **E** | **Event properties**: Contains further information about the selected event. For more information, see [Event properties](#event-properties). |

## Preview

The preview section consists of two tabs:

* The **Output** tab displays a preview of the selected event output.
* The **Mesh Preview** tab displays the mesh geometry Unity rendered in the event.

![The mesh preview tab displaying the power jigsaw mesh from the URP sample scene. The mesh preview (A) is in the centre. The bottom bar has the mesh name (B), the preview mode (C), and the toggle for wireframe (D).](../uploads/Main/frame-debugger-mesh-preview.png)


The mesh preview tab displaying the power jigsaw mesh from the URP sample scene. The mesh preview (A) is in the centre. The bottom bar has the mesh name (B), the preview mode (C), and the toggle for wireframe (D).

| **Label** | **Description** |
| --- | --- |
| **A** | **Preview**: A preview of the mesh geometry Unity rendered during the event. |
| **B** | **Mesh name**: The name of the mesh asset in the preview. Click on the mesh name to take see the mesh asset in the **Project window**A window that shows the contents of your `Assets` folder (Project tab) [More info](ProjectView.html) See in [Glossary](Glossary.html#Projectwindow). If the geometry was procedural and there is no mesh asset associated, this is empty (Unity displays **-**). |
| **C** | **Preview mode**: Specifies how the preview renders the mesh. For more information, refer to [Preview mode dropdown](#preview-mode-dropdown). |
| **D** | **Wireframe toggle**: Toggles the mesh wireframe on and off. When enabled, the preview displays the mesh vertices and edges. |

### Preview mode dropdown

| **Value** | **Description** |
| --- | --- |
| **Shaded** | Renders the mesh using its material and a basic light. |
| **UV Checker** | Applies a checkerboard texture to the mesh to visualize how the mesh’s UV layout maps textures. |
| **UV Layout** | Displays how the vertices of the mesh are organized in the unwrapped UV layout. This view disables the Wireframe toggle. |
| **Vertex Color** | Visualizes any vertex colors that the vertices in this mesh have. If no vertices have a vertex color, this option is unavailable. |
| **Normals** | Visualizes the relative directions of the normals in the mesh with color. |
| **Tangents** | Visualizes the tangent data in the mesh with color. |
| **Blendshapes** | Visualizes blend shape deformations on the mesh. If the mesh has no blend shapes, this option is unavailable. |

## Event properties

The event properties section contains properties and values for the selected event. It has a **Details** fold-out section that contains information about the event itself and then a fold-out section for each type of shader property. If the fold-out section is grayed-out, it means that the shader in the event didn’t contain any properties of that type. For more information on the information that each section displays, see:

* [Details](#details)
* [Keywords](#keywords)
* [Textures](#textures)An image used when rendering a GameObject, Sprite, or UI element. Textures are often applied to the surface of a mesh to give it visual detail. [More info](class-TextureImporter.html)  
  See in [Glossary](Glossary.html#texture)
* [Ints](#ints)
* [Floats](#floats)
* [Vectors](#vectors)
* [Matrices](#matrices)
* [Buffers](#buffers)
* [Constant Buffers](#constant-buffers)

**Note**: When using OpenGL and GLSL shaders, this panel displays all shader properties as being part of the vertex stage.

### Details

The **Details** section displays information about the rendering event, such as the number of draw calls as well as the meshes that Unity rendered and the shader it used to render them.

| **Property** | **Description** |
| --- | --- |
| **RenderTarget** | Defines the name of the render target. |
| **Size** | Specifies the size of the render target. |
| **Format** | Defines the [TextureFormat](../ScriptReference/TextureFormat.html) for the render target. |
| **Color Actions** | Displays the actions Unity performs on the color target when:  * The GPU first loads the color target. For more information, refer to [RenderBufferLoadAction](../ScriptReference/Rendering.RenderBufferLoadAction.html). * The GPU finishes rendering to the color target. For more information, refer to [RenderBufferStoreAction](../ScriptReference/Rendering.RenderBufferStoreAction.html). |
| **Depth Actions** | Displays the actions Unity performs on the depth target when:  * The GPU first loads the depth target. For more information, refer to [RenderBufferLoadAction](../ScriptReference/Rendering.RenderBufferLoadAction.html). * The GPU finishes rendering to the depth target. For more information, refer to [RenderBufferStoreAction](../ScriptReference/Rendering.RenderBufferStoreAction.html). |
| **Memoryless** | Specifies the **render texture**A special type of Texture that is created and updated at runtime. To use them, first create a new Render Texture and designate one of your Cameras to render into it. Then you can use the Render Texture in a Material just like a regular Texture. [More info](class-RenderTexture.html) See in [Glossary](Glossary.html#RenderTexture) [memoryless mode](../ScriptReference/RenderTextureMemoryless.html) mode. For more information, refer to [memoryless](../ScriptReference/RenderTextureDescriptor-memoryless.html). |
| **ColorMask** | Defines the color channel mask Unity uses for the render target. For more information, refer to [ColorMask](SL-ColorMask.html). |
| **Blend Color** | Specifies the [color blending](SL-Blend.html) method Unity uses during the selected event. |
| **Blend Alpha** | Specifies the [alpha blending](SL-Blend.html) method Unity uses during the selected event. |
| **BlendOp Color** | Defines the [color blending operation](SL-BlendOp.html) Blend Color Unity uses. |
| **BlendOp Alpha** | Defines the [alpha blending operation](SL-BlendOp.html) Blend Alpha Unity uses. |
| **Draw Calls** | Displays the number of draw calls Unity processes during the selected event. |
| **Vertices** | Displays the number of vertices Unity processes during the selected event. |
| **Indices** | Displays the number of indices Unity processes during the selected event. |
| **Clear Color** | Specifies the color Unity uses to clear the render target during the selected event. If Unity doesn’t clear the render target, the display doesn’t show a color. |
| **Clear Depth** | Specifies the color Unity uses to clear the **depth buffer**A memory store that holds the z-value depth of each pixel in an image, where the z-value is the depth for each rendered pixel from the projection plane. [More info](class-RenderTexture.html) See in [Glossary](Glossary.html#depthbuffer) during the selected event. If Unity doesn’t clear the depth buffer, the display doesn’t show a color. |
| **Clear Stencil** | Specifies the color Unity uses to clear the **stencil buffer**A memory store that holds an 8-bit per-pixel value. In Unity, you can use a stencil buffer to flag pixels, and then only render to pixels that pass the stencil operation. [More info](class-RenderTexture.html) See in [Glossary](Glossary.html#stencilbuffer) during the selected event. If Unity doesn’t clear the stencil buffer, the display doesn’t show a color. |
| **Batch cause** | Displays the reason why the SRP Batcher is unable to batch the selected rendering event with the previous rendering event.  Relevant only if your application uses the [SRP Batcher](SRPBatcher.html). |
| **Meshes** | Displays the list of meshes that Unity renders during the selected event. |
| **Pass** | Defines the [shader Pass](SL-Pass.html) Unity uses. |
| **LightMode** | Specifies the LightMode [pass tag](SL-PassTags.html) Unity uses during the selected event. |
| **Base Shading Rate** | Displays the [shading rate fragment size](../ScriptReference/Rendering.ShadingRateFragmentSize.html) Unity uses in the pass. Available only if the current platform supports variable rate shading. |
| **ShadingRateCombiners** | Displays the [shading rate combiners](../ScriptReference/Rendering.ShadingRateCombiner.html) Unity uses in the Primitive / Fragment stages. This is available only if a shading rate image is attached to the pass. |
| **Shading Rate Image** | Displays the [shading rate image](../ScriptReference/Rendering.ShadingRateImage.html) attachment Unity uses in the pass. |
| **Used Shader** | Specifies the [shader asset](Shaders.html) Unity uses during the selected event. This can sometimes be different than the original shader, for example when the original shader uses a [fallback shader](SL-Fallback.html) or [USEPASS](SL-UsePass.html). |
| **Original Shader** | Displays the original shader Unity uses with the pass. |
| **ZClip** | Specifies the shader’s [depth clip](SL-ZClip.html) mode. |
| **ZTest** | Specifies the shader’s [depth test](SL-ZTest.html) mode. |
| **ZWrite** | Specifies the shader’s [depth clip](SL-ZWrite.html) mode. |
| **Cull** | Defines the shader’s [cull](SL-Cull.html) mode. |
| **Conservative** | Indicates whether the shader uses [conservative rasterization](SL-Conservative.html). |
| **Offset** | Specifies the [depth bias](SL-Offset.html) on the GPU that Unity uses during the selected event. |
| **Stencil** | Indicates whether Stencil is enabled in the selected event. For more information, refer to [Stencil](SL-Stencil.html). |
| **Stencil Ref** | Specifies the stencil reference value. |
| **Stencil ReadMask** | Defines the stencil [readmask](SL-Stencil.html) value Unity uses to perform the stencil test. |
| **Stencil WriteMask** | Defines the stencil [writemask](SL-Stencil.html) value Unity uses to write to the stencil buffer. |
| **Stencil Comp** | Specifies the operation the GPU performs for the stencil test for all **pixels**The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](ShadowPerformance.html) See in [Glossary](Glossary.html#pixel). |
| **Stencil Pass** | Specifies the operation the GPU performs on the stencil buffer for pixels that pass both the stencil test and the depth test. |
| **Stencil Fail** | Specifies the operation the GPU performs on the stencil buffer for pixels that fail the stencil test. |
| **Stencil ZFail** | Specifies the operation the GPU performs on the stencil buffer for pixels that pass the stencil test but fail the depth test. |

### Keywords

This section displays information about the enabled [shader keywords](shader-keywords.html) Unity used in the rendering event.

| **Property** | **Description** |
| --- | --- |
| **Name** | The name of the shader keyword. |
| **Stage** | The shader stage that Unity used the shader keyword in. Refer to [Stages](#stages). |
| **Scope** | Indicates whether the scope of the keyword is global or local. For more information, refer to [Toggle shader keywords in a script](shader-keywords-scripts.html). |
| **Dynamic** | Indicates whether the keyword is dynamic or not. For more information, see [Declaring and using shader keywords in HLSL](SL-MultipleProgramVariants.html). |

### Textures

The **Texture** section displays information about the named [textures](../ScriptReference/Material.SetTexture.html) Unity used during the rendering event.

| **Property** | **Description** |
| --- | --- |
| **Name** | The property name for the texture. |
| **Stage** | The shader stage that Unity used the texture in. Refer to [Stages](#stages). |
| **Size** | The size of the texture. This is the width and height for 2D textures and width, height, and depth for 3D textures, |
| **Sampler Type** | Indicates type of a Texture (such as 2D Texture, cubemap, or 3D volume texture). |
| **Color Format** | The color format that the texture uses. For more information on RenderTexture formats, see [GraphicsFormat](../ScriptReference/Experimental.Rendering.GraphicsFormat.html). For more information on formats for other texture types, see [TextureFormat](../ScriptReference/TextureFormat.html). |
| **Depth Stencil Format** | The depth stencil format for the RenderTexture. For more information, see [RenderTexture.depthStencilFormat](../ScriptReference/RenderTexture-depthStencilFormat.html).  **Note**: If the texture isn’t a RenderTexture, Unity doesn’t display a [graphics format](../ScriptReference/Experimental.Rendering.GraphicsFormat.html) here. |
| **Texture** | The texture name. |

### Ints

The **Ints** section displays information about the named [int](../ScriptReference/Material.SetInt.html) values Unity used during the rendering event.

| **Property** | **Description** |
| --- | --- |
| **Name** | The name of the int property in the shader. |
| **Stage** | The shader stage that Unity used the int property in. Refer to [Stages](#stages). |
| **Value** | The value of the int property. |

### Floats

The **Floats** section displays information about the named [float](../ScriptReference/Material.SetFloat.html) values Unity used during the rendering event.

| **Property** | **Description** |
| --- | --- |
| **Name** | The name of the float property in the shader. |
| **Stage** | The shader stage that Unity used the float property in. Refer to [Stages](#stages). |
| **Value** | The value of the float property. |

### Vectors

| **Property** | **Description** |
| --- | --- |
| **Name** | The name of the vector property in the shader. |
| **Stage** | The shader stage that Unity used the vector property in. Refer to [Stages](#stages). |
| **Value(R)** | The R component of the vector. |
| **Value(G)** | The G component of the vector. |
| **Value(B)** | The B component of the vector. |
| **Value(A)** | The A component of the vector. |

### Matrices

The **Matrices** section displays information about the named [matrix](../ScriptReference/Material.SetMatrix.html) values Unity used during the rendering event.

| **Property** | **Description** |
| --- | --- |
| **Name** | The name of the matrix property in the shader. |
| **Stage** | The shader stage that Unity used the matrix property in. Refer to [Stages](#stages). |
| **Column 0** | The values in the first column of the matrix. |
| **Column 1** | The values in the second column of the matrix. |
| **Column 2** | The values in the third column of the matrix. |
| **Column 3** | The values in the fourth column of the matrix. |

### Buffers

The **Buffers** section displays information about the named  [buffers](../ScriptReference/Material.SetBuffer.html) Unity used during the rendering event.

| **Property** | **Description** |
| --- | --- |
| **Name** | The name of the buffer in the shader. |
| **Stage** | The shader stage that Unity used the buffer in. Refer to [Stages](#stages). |

### Constant Buffers

This **Constant Buffers** section displays information about the named [constant buffers](../ScriptReference/Material.SetConstantBuffer.html) Unity used during the rendering event.

| **Property** | **Description** |
| --- | --- |
| **Name** | The name of the constant buffer in the shader. |
| **Stage** | The shader stage that Unity used the constant buffer in. Refer to [Stages](#stages). |

### Stages

The possible values for **Stage** are:

* **vs**: Vertex Shader
* **fs**: Fragment Shader
* **gs**: Geometry Shader
* **hs**: Hull Shader
* **ds**: Domain Shader

Frame Debugger window reference

Rendering Statistics window reference

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)