* [2D game development](Unity2D.html)
* [Get started with 2D game development](2d-game-development-landing.html)
* 2D game creation workflow

Set up a project for 2D games

2D game perspectives reference

# 2D game creation workflow

Before you create a 2D game, you need to decide on a [game perspective](./2d-game-perspective-reference.html) and an [art style](./2d-game-art-syle-reference.html).

To create a 2D game, [set up your Unity project](./setup-project-2d-game.html) and then familiarize yourself with the relevant concepts in the following order:

1. [Fundamentals](#Fundamentals)
2. [Scripting](#Scripting)
3. [Sprites](#Sprites)A 2D graphic objects. If you are used to working in 3D, Sprites are essentially just standard textures but there are special techniques for combining and managing sprite textures for efficiency and convenience during development. [More info](sprite/sprite-landing.html)  
   See in [Glossary](Glossary.html#Sprite)
4. [Building in-game environments](#Environment)
5. [Character animation](#Animation)
6. [Graphics](#Graphics)
7. [Physics 2D](#Physics)
8. [Audio](#Audio)
9. [User interface](#UI)
10. [Accessibility](#Accessibility)
11. [Profiling, optimizing and testing](#Profiling)
12. [Publishing](#Publishing)

## Fundamentals

[GameObjects](GameObjects.html)The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) are fundamental objects in Unity that represent characters, props, scenery, and more. Every object in your game is a GameObject.

GameObjects represent the items in your game; the space in which you place them to build your level is called a [scene](CreatingScenes.html)A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene). Scenes in Unity are always 3D; when you make a 2D game in Unity, you typically choose to ignore the third dimension (the z-axis) but you can also use it in special cases, for example when making 2.5D games.

The behavior of GameObjects is defined by blocks of functionality called components. The following components are fundamental for 2D games:

* [Transform](class-Transform.html): the **Transform component**A Transform component determines the Position, Rotation, and Scale of each object in the scene. Every GameObject has a Transform. [More info](class-Transform.html)  
  See in [Glossary](Glossary.html#Transformcomponent) determines the Position, Rotation, and Scale of each GameObject in the scene. Every GameObject has a Transform component.
* [Sprite Renderer](sprite/renderer/sprite-renderer-reference.html)A component that lets you display images as Sprites for use in both 2D and 3D scenes. [More info](sprite/renderer/sprite-renderer-reference.html)  
  See in [Glossary](Glossary.html#SpriteRenderer): the Sprite Renderer component renders the Sprite and controls how it looks in a scene.
* [Cameras](class-Camera.html)A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](CamerasOverview.html)  
  See in [Glossary](Glossary.html#Camera): devices that capture and display the world to the player. Marking a Camera as **Orthographic** removes all perspective from the Camera’s view. This is mostly useful for making isometric or 2D games.
* [Collider 2D](2d-physics/collider/collider-2d-landing.html): this component defines the shape of a 2D GameObject for the purposes of physical **collisions**A collision occurs when the physics engine detects that the colliders of two GameObjects make contact or overlap, when at least one has a Rigidbody component and is in motion. [More info](CollidersOverview.html)  
  See in [Glossary](Glossary.html#collision). See [2D Physics](class-Physics2DManager).

Components are UI representations of C# classes; you can use scripts to change and interact with components, or create new ones. See the [Scripting](#Scripting) section for more details.

## Scripting

All 2D games need [scripts](scripting.html)A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts). Scripts respond to input from the player and arrange for events in the gameplay to happen when they should.

For details on how to use scripts in Unity see [Scripting Overview](object-oriented-development.html). Also see the Unity Learn [Beginner Scripting](https://learn.unity.com/course/beginner-scripting) course.

Scripts are attached to GameObjects, and any script you create inherits from the [MonoBehaviour](../ScriptReference/MonoBehaviour.html) class.

## Sprites

[Sprites](sprite/sprite-landing.html) are 2D graphic objects. You use Sprites for all types of 2D games. For example, you can import an image of your main character as a Sprite.

![A character Sprite](../uploads/Main/quickstart-sprite-2d.png)


A character Sprite

You can also use a collection of Sprites to build a character. This allows you greater control over the movement and animation of your characters.

![Multiple Sprites that make up the parts of a character, displayed in the Sprite Editor](../uploads/Main/quickstart-sprite-editor-2d.png)


Multiple Sprites that make up the parts of a character, displayed in the Sprite Editor

### Importing and setting up Sprites

Import your Sprites with Unity’s recommended settings; see [Importing and Setting Up Sprites](sprite/sprite-landing.html).

### Rendering Sprites

Use the [Sprite Renderer](sprite/renderer/sprite-renderer-reference.html) component to render your Sprites. For example, you can use the Sprite Renderer to change the color and opacity of a Sprite.

![Adjusting the color of a Sprite with the Sprite Renderer](../uploads/Main/quickstart-sprite-renderer-2d.png)


Adjusting the color of a Sprite with the Sprite Renderer

See the [Introduction to the Sprite Renderer Learn tutorial](https://learn.unity.com/tutorial/introduction-to-the-sprite-renderer#). Sorting SpritesBy organizing Sprites in layers, you can create an illusion of depth. You can sort Sprites according to many strategies. See [Sorting Sprites](sprite/sprite-landing.html) for full details. For example, you might sort Sprites along the y-axis, so that Sprites that are higher up are sorted behind Sprites that are lower, to make the Sprites that are higher appear further away than the Sprites that are lower.

![Sprites sorted along the y-axis](../uploads/Main/quickstart-sort-sprites-2d.png)


Sprites sorted along the y-axis

To set the overlay order of Sprites, use [Sorting Layers](class-TagManager.html).

To group GameObjects with [Sprite Renderers](sprite/renderer/sprite-renderer-reference.html), and control the order in which they render their Sprites, use [Sorting Groups](sprite/sorting-group/sorting-group-landing).

### Sprite Atlas

You can use a [Sprite Atlas](sprite/atlas/atlas-landing.html)**Graphics:** A utility that packs several sprite textures tightly together within a single texture known as an atlas. [More info](sprite/atlas/v2/v2-landing). **2D:** A texture that is composed of several smaller textures. Also referred to as a texture atlas, image sprite, sprite sheet or packed texture. [More info](sprite/atlas/atlas-landing.html).  
See in [Glossary](Glossary.html#SpriteAtlas) to consolidate several Textures into a single combined Texture. This optimizes your game and saves memory. For example, you can add all your Sprites associated with a particular character or purpose to a Sprite Atlas.

![A Sprite Atlas](../uploads/Main/quickstart-sprite-atlas-2d.png)


A Sprite Atlas

See the [Introduction to the Sprite Atlas Learn tutorial](https://learn.unity.com/tutorial/introduction-to-the-sprite-atlas).

## Building in-game environments

Environment design refers to the process of building your game’s levels and environments. You can combine the environment design tools in this section in whichever way makes the most sense for your game; for example, you can make a top-down game using only 9-slice, or you can make a side on platformer with Tilemap and SpriteShape.

### 9-slicing

9-slicing is a 2D technique that allows you to reuse an image at various sizes without needing to prepare multiple assets. Unity can dynamically stretch and tile designated parts of a Sprite to allow one Sprite to serve as the border or background for UI elements of many sizes. See [9-slicing Sprites](sprite/9-slice/9-slice-landing.html).

For example, you could use 9-slicing to stretch a Sprite to shape when you build a 2D level.

![A 9-sliced Sprite, split into nine sections](../uploads/Main/quickstart-9-slice-2d.png)


A 9-sliced Sprite, split into nine sections

See the [Using 9-Slicing for Scalable Sprites Learn tutorial](https://learn.unity.com/tutorial/using-9-slicing-for-scalable-sprites-2019-3).

### Tilemap

The [Tilemap](tilemaps/work-with-tilemaps/tilemap-reference.html)A GameObject that allows you to quickly create 2D levels using tiles and a grid overlay. [More info](tilemaps/work-with-tilemaps/tilemap-reference.html)  
See in [Glossary](Glossary.html#Tilemap) component is a system that stores and handles Tile assets for creating 2D levels. Use the [2D Tilemap Editor](tilemaps/work-with-tilemaps/tilemap-reference.html) package (installed by default) to use Tilemaps.

For example, you can use Tilemaps to paint levels using Tiles and brush tools and define rules for how Tiles behave.

![The Tile Palette window, used to edit Tilemaps](../uploads/Main/quickstart-tilemap-2d.png)


The Tile Palette window, used to edit Tilemaps

See the [Introduction to Tilemaps Learn tutorial](https://learn.unity.com/tutorial/introduction-to-tilemaps).

#### 2D Tilemap Extras

To add some extra Tilemap assets to your Project, install the [2D Tilemap Extras](https://docs.unity3d.com/Packages/com.unity.2d.tilemap.extras@1.6/manual/index.html) package. This package contains reusable 2D and Tilemap **Editor scripts**C# source files composed entirely of code that runs in the Unity Editor only and not in the runtime Player build. Keep such scripts in dedicated Editor assemblies either by placing them in a parent folder called Editor or creating an Editor-only assembly definition.  
See in [Glossary](Glossary.html#Editorscripts) that you can use for your own Projects. You can customize the behavior of the scripts to create new Brushes that suit different scenarios.

#### Isometric Tilemaps

For games with isometric perspective, you can create [Isometric Tilemaps](tilemaps/work-with-tilemaps/isometric-tilemaps/isometric-tilemap-landing.html).

### SpriteShape

In a similar way to a vector drawing tool, SpriteShape provides a more flexible way to create larger Sprites, such as organic-looking landscapes and paths. See the [Sprite Shape Profile](https://docs.unity3d.com/Packages/com.unity.2d.spriteshape@3.0/manual/SSProfile.html).

![A path created in SpriteShape](../uploads/Main/quickstart-spriteshape-path-2d.png)


A path created in SpriteShape

See the [Working with SpriteShape tutorial](https://learn.unity.com/tutorial/working-with-spriteshape).

## Character animation

There are three different ways you can animate 2D characters:

| 2D animation type | Used for |
| --- | --- |
| Frame-by-frame | Artistic reasons, if you want your game to have a classic animation art style. Frame-by-frame animation is relatively resource-intensive, both to make and to run. |
| Cutout | Smooth skeletal animation, when the characters don’t require realistic articulation. |
| Skeletal | Smooth skeletal animation where Sprites bend according to the bone structure. Use this when the characters need a more organic feel. |

### Frame-by-frame

Frame-by-frame animation is based on the traditional cel animation technique of drawing each moment of an animation as individual images, which are played in fast sequence, like flipping pages on a flipbook.

For information, refer to [Sprite Swap](https://docs.unity3d.com/Packages/com.unity.2d.animation@latest?subfolder=/manual/SpriteSwapLanding.html) in the 2D Animation package manual.

![Frame-by-frame animation in the Sprite Editor](../uploads/Main/quickstart-frame-by-frame-2d.png)


Frame-by-frame animation in the Sprite Editor

See the [Introduction to Sprite Animations Learn tutorial](https://learn.unity.com/tutorial/introduction-to-sprite-animations).

### Cutout

In cutout animation, multiple Sprites make up the body of a character, and each piece moves to give the visual effect of the whole character moving. This animation style is similar to skeletal animation (see below), except that the Sprites don’t bend.

![Cutout animation in the Sprite Editor](../uploads/Main/quickstart-cutout-2d.png)


Cutout animation in the Sprite Editor

### Skeletal

With skeletal animation, you map a Sprite or a group of Sprites onto an animation skeleton. You can create and define animation bones for characters and objects, that define how they should bend and move. This approach allows the bones to bend and deform the Sprites, for a more natural movement style. To use skeletal animation, you need to use the [2D Animation](com.unity.2d.animation.html) package (installed by default).

For a 2D Animation workflow, including a guide to working with the Bone Editor, see the [2D Animation documentation](https://docs.unity3d.com/Packages/com.unity.2d.animation@1.0/manual/index.html).

![A character with bones in the Bone Editor](../uploads/Main/quickstart-skeletal-2d.png)


A character with bones in the Bone Editor

## Graphics

This section describes the [2D URP graphic features](2d-urp-landing.html) available when using Universal **Render Pipeline**A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](render-pipelines.html)  
See in [Glossary](Glossary.html#renderpipeline) (URP).

### Lighting

Because you’re using URP with the 2D Renderer, you can use the Light 2D component to apply optimized 2D lighting to Sprites. For details, see [Introduction to Lights 2D](urp/Lights-2D-intro.html).

![These two images show the same scene; in the image on the left, 2D Lights are disabled, and in the image on the right, 2D lights are enabled. With 2D Lights, you can use the same Sprites to create different weather conditions or moods.](../uploads/Main/quickstart-lighting-2d.png)


These two images show the same scene; in the image on the left, 2D Lights are disabled, and in the image on the right, 2D lights are enabled. With 2D Lights, you can use the same Sprites to create different weather conditions or moods.

See the [Lighting in URP Learn tutorial](https://learn.unity.com/tutorial/editing-lighting-in-the-lightweight-render-pipeline).

### Shadows

To define the shape and properties that a Light uses to determine the shadows it casts, use the [Shadow Caster 2D component](urp/2DShadows.html).

![A shadow intensity of 0.5 in the Shadow Caster 2D component](../uploads/Main/quickstart-shadows-2d.png)


A shadow intensity of 0.5 in the Shadow Caster 2D component

### Enhanced look and feel

Particle systems and **post-processing**A process that improves product visuals by applying filters and effects before the image appears on screen. You can use post-processing effects to simulate physical camera and film properties, for example Bloom and Depth of Field. [More info](PostProcessingOverview.html) post processing, postprocessing, postprocess  
See in [Glossary](Glossary.html#post-processing) are optional tools that you can use to add polish to your game.

#### Particle systems

You can use **particle**A small, simple image or mesh that is emitted by a particle system. A particle system can display and move particles in great numbers to represent a fluid or amorphous entity. The effect of all the particles together creates the impression of the complete entity, such as smoke. [More info](class-ParticleSystem.html)  
See in [Glossary](Glossary.html#particle) systems to create dynamic objects like fire, smoke or liquids, as an alternative to using a Sprite. Sprites are more suited to physical objects. See [Particle systems](ParticleSystems.html)A component that simulates fluid entities such as liquids, clouds and flames by generating and animating large numbers of small 2D images in the scene. [More info](class-ParticleSystem.html)  
See in [Glossary](Glossary.html#particlesystem).

![A fire effect, created with the Particle System and Shader Graph for 2D](../uploads/Main/quickstart-particle-system-2d.png)


A fire effect, created with the Particle System and Shader Graph for 2D

#### Post-processing

You can use post-processing effects and full-screen effects to significantly improve the appearance of your game. For example, you can use these effects to simulate physical camera or film properties, or to create stylized visuals.

URP has its own post-processing implementation. See [Post-processing in the Universal Render Pipeline](urp/integration-with-post-processing.html).

![The Lost Crypt demo uses the bloom and vignette post-processing effects](../uploads/Main/quickstart-post-processing-2d.png)


The Lost Crypt demo uses the bloom and vignette post-processing effects

## Physics 2D

The Physics 2D settings define limits on the accuracy of the physical simulation in your 2D game. See [2D Physics](class-Physics2DManager).

This [video](https://www.youtube.com/watch?v=Xxbs9x2qB7Y&feature=youtu.be) provides an overview of 2D physics features in Unity 2020.1.

To learn how to use Unity’s 2D **physics engine**A system that simulates aspects of physical systems so that objects can accelerate correctly and be affected by collisions, gravity and other forces. [More info](PhysicsSection.html)  
See in [Glossary](Glossary.html#physicsengine), see the [2D Physics Learn tutorial](https://learn.unity.com/tutorial/2d-physics).

The following 2D physics tools are useful for 2D games.

* [Rigidbody 2D](#Rigidbody)
* [Collider 2D](#Collider)
* [Triggers](#Triggers)
* [2D Joints](#Joints)
* [2D Effectors](#Effectors)

### Rigidbody 2D

A **Rigidbody**A component that allows a GameObject to be affected by simulated gravity and other forces. [More info](class-Rigidbody.html)  
See in [Glossary](Glossary.html#Rigidbody) 2D component places a GameObject under the control of the physics engine. See [Rigidbody 2D](2d-physics/rigidbody/introduction-to-rigidbody-2d.html).

![The Rigidbody 2D component](../uploads/Main/quickstart-rigidbody-component-2d.png)


The Rigidbody 2D component

### Collider 2D

Collider 2D components define the shape of a 2D GameObject for the purposes of physical collisions. You can also use **Collider**An invisible shape that is used to handle physical collisions for an object. A collider doesn’t need to be exactly the same shape as the object’s mesh - a rough approximation is often more efficient and indistinguishable in gameplay. [More info](CollidersOverview.html)  
See in [Glossary](Glossary.html#collider) 2D components for input detection. For example, in mobile games you can use them to make Sprites selectable.

The Collider 2D types that you can use with Rigidbody 2D are:

* [Circle Collider 2D](2d-physics/collider/circle-collider-2d-reference.html)
* [Box Collider 2D](2d-physics/collider/box-collider-2d-reference.html)
* [Polygon Collider 2D](2d-physics/collider/polygon-collider-2d-reference.html)
* [Edge Collider 2D](2d-physics/collider/edge-collider-2d-reference.html)
* [Capsule Collider 2D](2d-physics/collider/capsule-collider/capsule-collider-2d-reference.html)
* [Composite Collider 2D](2d-physics/collider/composite-collider/composite-collider-2d-reference.html)

![The Circle Collider 2D component](../uploads/Main/quickstart-circle-collider-component.png)


The Circle Collider 2D component

### Triggers

When you set a Collider 2D as a Trigger (by enabling its **Is Trigger** property), it no longer behaves as a physical object, and it can intersect with other Colliders without causing a collision. Instead, when a Collider enters its space, Unity calls the `OnTriggerEnter` function on the Trigger GameObject’s scripts.

![The Circle Collider 2D component with Is Trigger selected](../uploads/Main/quickstart-is-trigger-2d.png)


The Circle Collider 2D component with **Is Trigger** selected

### 2D Joints

Joints attach GameObjects together. You can only attach 2D **joints**A physics component allowing a dynamic connection between Rigidbody components, usually allowing some degree of movement such as a hinge. [More info](Joints.html)  
See in [Glossary](Glossary.html#joint) to GameObjects that have a Rigidbody 2D component attached, or to a fixed position in world space. See [2D Joints](2d-physics/joints/2d-joints-landing.html).

### 2D Effectors

Use Effector 2D [components](UsingComponents.html)A functional part of a GameObject. A GameObject can contain any number of components. Unity has many built-in components, and you can create your own by writing scripts that inherit from MonoBehaviour. [More info](UsingComponents.html)  
See in [Glossary](Glossary.html#component) with [Collider 2D](2d-physics/collider/collider-2d-landing.html) components to direct the forces of [physics](PhysicsSection.html) in your scene when [GameObject](GameObjects.html) Colliders come into contact with each other. See [2D Effectors](2d-physics/effectors/effectors-2d-landing.html).

## Audio

You can add background music and sound effects to your game in Unity; see [Audio Overview](AudioOverview.html). Use third-party software to create your audio and import it into Unity with the recommended settings.

## User interface

If you want to add a menu or help to your game, you need to set up a [user interface](UIToolkits.html). To set up a user interface, use [Unity UI](https://docs.unity3d.com/Manual/UIToolkits.html).

## Accessibility

Reach a wider player base by making your game accessible to people of all abilities. Refer to [Accessibility](accessibility/_index.html) for guidance.

## Profiling, optimizing and testing a build

### Profiling

Profiling allows you to see how resource-intensive the different parts of your game are. You should always profile your game on its target release platform; see [Profiling your application](profiler-profiling-applications.html).

### Testing

Test your game and your code with the Unity Test Framework; see [Unity Test Framework](https://docs.unity3d.com/Packages/com.unity.test-framework@1.1/manual/index.html).

![The Test Runner window](../uploads/Main/quickstart-testing-2d.png)


The Test Runner window

## Publishing

When you’ve finished your game, you’re ready to publish it. See [Publishing Builds](PublishingBuilds).

Set up a project for 2D games

2D game perspectives reference

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)