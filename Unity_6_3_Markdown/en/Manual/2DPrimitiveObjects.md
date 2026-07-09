* [GameObjects](working-with-gameobjects.html)
* [GameObject fundamentals](gameobject-fundamentals.html)
* Types of 2D primitive GameObjects

Primitive and placeholder objects

Add components to GameObjects

# Types of 2D primitive GameObjects

Unity has import support for different image formats, such as .png or Adobe’s .psd, which gives you additional options when creating and preparing your 2D assets for your project. But if you want to create a quick prototype, Unity provides 2D primitive **GameObjects**The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) to help you build your project, without needing to prepare and import your own assets.

This page details the dimensions and common uses of the available 2D primitive options.

**Important:** Your project must have the [2D Sprite package](https://docs.unity3d.com/Packages/com.unity.2d.sprite@1.0/manual/index.html) installed to enable the following 2D primitive options. The 2D Sprite package is automatically installed when you create a project with the [2D project template](https://docs.unity.com/hub/project-create.html) selected, or you can install the 2D Sprite package via the [Package Manager](Packages.html).

## Create a 2D primitive GameObject

To create one of these preset 2D primitive GameObjects, go to **GameObject** > **2D Object** > **Sprites** or **Create** > **2D** > **Sprites** and select one of the available options:

* [Triangle](#triangle)
* [Square](#square)
* [Circle](#circle)
* [Capsule](#capsule)
* [Isometric Diamond](#iso-diamond)
* [Hexagon Flat-Top](#hex-flat-top)
* [Hexagon Point-Top](#hex-point-top)
* [9-Sliced](#9-sliced)

## Default sprite dimensions

The default sprite size of the 2D primitives is 256 X 256 **pixels**The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](ShadowPerformance.html)  
See in [Glossary](Glossary.html#pixel), with a pixels-per-unit (PPU) size of 256. This combination of dimensions and PPU value makes the sprite’s size equal to one **Unity unit**The unit size used in Unity projects. By default, 1 Unity unit is 1 meter. To use a different scale, set the Scale Factor in the Import Settings when importing assets.  
See in [Glossary](Glossary.html#Unityunit) in the **scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene). There are two exceptions - the [Capsule](#capsule) primitive is 256 X 512 pixels (1:2 units) in size, and the [Isometric Diamond](#iso-diamond) primitive is 256 X 128 pixels (1:0.5 units).

## Triangle

![The Triangle 2D primitive GameObject.](../uploads/Main/2D-primitive-triangle.png)


The Triangle 2D primitive GameObject.

The **Triangle** 2D primitive is white isosceles triangle with a base measuring one Unity unit in size. You can use it as a placeholder for various elements in your scene, such as obstacles or parts of the user interface. You can add the [Polygon Collider 2D](2d-physics/collider/polygon-collider-2d-reference.html) component to the primitive to have it interact with other GameObjects and the 2D physics system.

## Square

![The Square 2D primitive GameObject.](../uploads/Main/2D-primitive-square.png)


The Square 2D primitive GameObject.

The **Square** 2D primitive is a white square that’s 1 X 1 Unity units in size. You can use it as a placeholder for various elements, such as obstacles or platforms. You can add the [Box Collider 2D](2d-physics/collider/box-collider-2d-reference.html) component to the primitive to have it interact with other GameObjects and the 2D physics system. You can select the [9-Sliced](#9-sliced) option for a more scalable sprite that resizes dynamically.

## Circle

![The Circle 2D primitive GameObject.](../uploads/Main/2D-primitive-circle.png)


The Circle 2D primitive GameObject.

The **Circle** 2D primitive is a white circle that’s one Unity unit in diameter. You can use it as a placeholder for various elements in your scene, such as obstacles or props. You can add the [Circle Collider 2D](2d-physics/collider/circle-collider-2d-reference.html) to the primitive to have it interact with other GameObjects and the 2D physics system.

## Capsule

![The Capsule 2D primitive GameObject.](../uploads/Main/2D-primitive-capsule.png)


The Capsule 2D primitive GameObject.

The **Capsule** 2D primitive is a white capsule that’s 1 X 2 units in size. You can use it as a placeholder for various elements in your scene, such as an obstacle, prop, or a stand-in for a character. You can add a [Capsule Collider 2D](2d-physics/collider/capsule-collider/capsule-collider-2d-reference.html) to the primitive to have it interact with other GameObjects and the 2D physics system.

## Isometric Diamond

![The Isometric Diamond 2D primitive GameObject.](../uploads/Main/2D-primitive-isodiamond.png)


The Isometric Diamond 2D primitive GameObject.

The **Isometric Diamond** 2D primitive is a white diamond-shaped sprite that’s 1 X 0.5 units in size. This sprite is often used as a placeholder for Tiles placed on [Isometric Tilemaps](tilemaps/work-with-tilemaps/isometric-tilemaps/isometric-tilemap-landing.html). The pixels at the top and bottom of this sprite are slightly cropped to improve tiling.

## Hexagon Flat-Top

![The Hexagon Flat-Top 2D primitive GameObject.](../uploads/Main/2D-primitive-hex-flattop.png)


The Hexagon Flat-Top 2D primitive GameObject.

The **Hexagon Flat-Top** 2D primitive is a regular hexagon that’s one unit wide, with its flat sides oriented towards the top and bottom. This sprite is often used as a placeholder for Tiles placed on [Hexagonal Flat-Top Tilemaps](tilemaps/work-with-tilemaps/hexagonal-tilemaps). The pixels to the left and right of this sprite are slightly cropped to improve tiling.

## Hexagon Point-Top

![The Hexagon Point-Top 2D primitive GameObject.](../uploads/Main/2D-primitive-hex-pointtop.png)


The Hexagon Point-Top 2D primitive GameObject.

The **Hexagon Point-Top** 2D primitive is a regular hexagon that’s one unit tall, with its points oriented towards the top and bottom. This sprite is often used as a sprite placeholder for Tiles placed on a [Hexagonal Pointed-Top Tilemaps](tilemaps/work-with-tilemaps/hexagonal-tilemaps). The pixels to the top and bottom of this sprite are slightly cropped to improve tiling.

## 9-Sliced

![The 9-Sliced 2D primitive GameObject.](../uploads/Main/2D-primitive-9-sliced.png)


The 9-Sliced 2D primitive GameObject.

The **9-Sliced** 2D primitive is a white square with rounded corners that’s 1 X 1 units in size. This sprite has been [9-sliced](sprite/9-slice/9-slice-landing.html) with borders measuring 64 pixels on each side. This sprite is primarily used with the [Sprite Renderer](sprite/renderer/sprite-renderer-reference.html)A component that lets you display images as Sprites for use in both 2D and 3D scenes. [More info](sprite/renderer/sprite-renderer-reference.html)  
See in [Glossary](Glossary.html#SpriteRenderer) component’s **Sliced** and **Tiled** Draw Modes. You can use the 9-sliced sprite as a flexible placeholder for various elements in your scene and project (see [9-slicing sprites](sprite/9-slice/9-slice-sprite) for more information). You can add a [Box Collider 2D](2d-physics/collider/box-collider-2d-reference.html) with **Auto Tiling** enabled to have the sprite interact with other objects and the 2D physics system.

## Additional resources

* [2D game development quickstart guide](./2d-game-development-landing.html)
* [Sprites](sprite/sprite-landing.html)A 2D graphic objects. If you are used to working in 3D, Sprites are essentially just standard textures but there are special techniques for combining and managing sprite textures for efficiency and convenience during development. [More info](sprite/sprite-landing.html)  
  See in [Glossary](Glossary.html#Sprite)
* [Tilemap](tilemaps/work-with-tilemaps/tilemap-reference.html)A GameObject that allows you to quickly create 2D levels using tiles and a grid overlay. [More info](tilemaps/work-with-tilemaps/tilemap-reference.html)  
  See in [Glossary](Glossary.html#Tilemap)
* [Physics Reference 2D](2d-physics/2d-physics.html)

Primitive and placeholder objects

Add components to GameObjects

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)