* [2D game development](Unity2D.html)
* Introduction to 2D

2D game development

Get started with 2D game development

# Introduction to 2D

You can use Unity to create 2D projects. This page introduces the gameplay, graphics, and physics specific to 2D Unity projects.

## Gameplay in 2D

The familiar functions of the Unity Editor when you use 3D mode are still available but with helpful additions to simplify 2D development.

![Scene viewed in 2D mode](../uploads/Main/Overview2D.jpg)


Scene viewed in 2D mode

The most noticeable feature is the **2D** view mode button in the **toolbar**A row of buttons and basic controls at the top of the Unity Editor that allows you to interact with the Editor in various ways (e.g. scaling, translation). [More info](Toolbar.html)  
See in [Glossary](Glossary.html#toolbar) of the **Scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) view. When you enable 2D mode, Unity will set an orthographic (perspective-free) view. This view means that the **camera**A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera) looks along the z-axis with the y-axis increasing upwards, which enables you to visualize the scene and easily place **2D objects**A 2D GameObject such as a tilemap or sprite. [More info](Unity2D.html)  
See in [Glossary](Glossary.html#2DObject).

For a full list of 2D components, how to change between 2D and 3D mode, and the different 2D and 3D mode settings, refer to [2D or 3D Projects](2Dor3D.html).

## 2D graphics

Graphic objects in 2D are known as **Sprites**. Sprites are standard textures, with special techniques for combining and managing **sprite**A 2D graphic objects. If you are used to working in 3D, Sprites are essentially just standard textures but there are special techniques for combining and managing sprite textures for efficiency and convenience during development. [More info](sprite/sprite-landing.html)  
See in [Glossary](Glossary.html#Sprite) textures for efficiency and convenience during development. Unity provides a built-in [Sprite Editor](sprite/sprite-editor/use-editor.html) to let you extract sprite graphics from a larger image. This enables you to edit many component images within a single texture in your image editor. You can use this, for example, to keep the arms, legs, and body of a character as separate elements within one image.

Sprites are rendered with a [Sprite Renderer](sprite/renderer/sprite-renderer-reference.html)A component that lets you display images as Sprites for use in both 2D and 3D scenes. [More info](sprite/renderer/sprite-renderer-reference.html)  
See in [Glossary](Glossary.html#SpriteRenderer) component rather than the [Mesh Renderer](class-MeshRenderer.html)A mesh component that takes the geometry from the Mesh Filter and renders it at the position defined by the object’s Transform component. [More info](class-MeshRenderer.html)  
See in [Glossary](Glossary.html#MeshRenderer) used with 3D objects. You can add this to a GameObject via the Components menu (**Component** > **Rendering** > **Sprite Renderer**) or you can create a GameObject directly with a Sprite Renderer already attached (menu: **GameObject** > **2D Object** > **Sprites**, then select a shape).

You can also use a [Sprite Creator](sprite/placeholder/placeholder-landing.html) tool to make placeholder 2D images.

## 2D physics

Unity has a separate physics system to handle 2D physics so you can make use of optimizations only available with 2D. The components correspond to the standard 3D physics components such as [Rigidbody](class-Rigidbody.html)A component that allows a GameObject to be affected by simulated gravity and other forces. [More info](class-Rigidbody.html)  
See in [Glossary](Glossary.html#Rigidbody), [Box Collider](class-BoxCollider.html)A cube-shaped collider component that handles collisions for GameObjects like dice and ice cubes. [More info](class-BoxCollider.html)  
See in [Glossary](Glossary.html#BoxCollider), and [Hinge Joint](class-HingeJoint.html)A joint that groups together two Rigidbody components, constraining them to move like they are connected by a hinge. It is perfect for doors, but can also be used to model chains, pendulums and so on. [More info](class-HingeJoint.html)  
See in [Glossary](Glossary.html#HingeJoint), but with `2D` appended to the name. Therefore, you can equip sprites with [Rigidbody 2D](2d-physics/rigidbody/introduction-to-rigidbody-2d.html), [Box Collider 2D](2d-physics/collider/box-collider-2d-reference.html), and [Hinge Joint 2D](2d-physics/joints/hinge-joint-2d-reference.html). Most 2D physics components are flattened versions of the 3D equivalents (for example, [**Box Collider 2D**](2d-physics/collider/box-collider-2d-reference.html) is a square while [**Box Collider**](class-BoxCollider.html) is a cube) but there are a few exceptions.

For the full list of 2D physics components, refer to [2D or 3D Projects](2Dor3D.html). For further information about 2D physics concepts and components, refer to the [Physics](PhysicsSection.html) section of the manual. To specify 2D physics settings, refer to the [Physics 2D](class-Physics2DSettings.html) window.

2D game development

Get started with 2D game development

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)