* [Get started](get-started.html)
* [Unity for first-time users](first-time-user.html)
* Key concepts

Get started with monetization and mobile ad mediation

Project configuration

# Key concepts

There are some concepts you rely on from the moment you open the Unity Editor. Use this page to refresh your memory as you work through tutorials and your first projects.

## GameObjects, components, and scenes

[GameObjects](class-GameObject.html)The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) represent everything in your game, including characters, props, and scenery. In the Unity Editor, all objects in a scene are GameObjects. In contrast, project assets are source files that you add to scenes. For example, C# **scripts**A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts), textures, materials, 3D **model files**A file containing a 3D data, which may include definitions for meshes, bones, animation, materials and textures. [More info](3D-formats.html)  
See in [Glossary](Glossary.html#modelfile), and **prefabs**An asset type that allows you to store a GameObject complete with components and properties. The prefab acts as a template from which you can create new object instances in the scene. [More info](Prefabs.html)  
See in [Glossary](Glossary.html#prefab).

GameObjects exist in 2D or 3D environments called [scenes](CreatingScenes.html)A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene). You can think of a scene as a game level, but it might also represent a menu, the credits at the end of the game, or a cutscene.

The behavior of GameObjects is defined by blocks of functionality called components. You can attach multiple components to GameObjects. The following components are fundamental for 3D games:

| Component | Impact on a GameObject |
| --- | --- |
| [**Transform**](class-Transform.html) | Determines the Position, Rotation, and Scale of each GameObject in the scene. Every GameObject has a **Transform component**A Transform component determines the Position, Rotation, and Scale of each object in the scene. Every GameObject has a Transform. [More info](class-Transform.html) See in [Glossary](Glossary.html#Transformcomponent). |
| [**Mesh Filter**](class-MeshFilter.html) | Defines the shape of a 3D GameObject. |
| [**Mesh Renderer**](class-MeshRenderer.html) | Applies textures and handles how the 3D GameObject looks under lighting examples. |
| [**Cameras**](class-Camera.html) | Define GameObjects that capture and display the world to the player. |
| [**Rigidbody**](class-Rigidbody.html) | Allow GameObjects to interact with the Physics system, including gravity and **collisions**A collision occurs when the physics engine detects that the colliders of two GameObjects make contact or overlap, when at least one has a Rigidbody component and is in motion. [More info](CollidersOverview.html) See in [Glossary](Glossary.html#collision). Refer to the [Physics](#Physics) section of this guide. |
| [**Colliders**](CollidersOverview.html) | Defines the shape of a 3D GameObject for the purpose of physical collisions, which can be different from the 3D **mesh**The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](mesh.html) See in [Glossary](Glossary.html#Mesh)’s visible shape. |

[Back to Top](#TopOfPage)

## Scripting

Use scripts to create complex game behavior, such as:

* Trigger game events, such as move the user to a win or lose scene in response to changes in the user’s game stats.
* Change component properties over time. For example, change the visibility of a hidden door, shrink and enlarge an object, or collapse a wall.
* Respond to user input to move their character, interact with objects, and select menu options.

To add a script to a GameObject, add the **Script** component, and reference your own script in it.

Unity supports the C# programming language natively.

* For details on how to use scripts in Unity, refer to [Scripting Overview](scripting.html).
* To learn the fundamentals of scripting, follow the [Unity Learn Beginner Scripting course](https://learn.unity.com/course/beginner-scripting?utm_source=first-time&utm_medium=docs).
* For more in-depth guidance, refer to the example projects [Create with Code](https://learn.unity.com/course/create-with-code?utm_source=first-time&utm_medium=docs) and [Creator Kit: Beginner Code](https://learn.unity.com/project/creator-kit-beginner-code?utm_source=first-time&utm_medium=docs).

[Back to Top](#TopOfPage)

## 3D models

Models are 3D representations of objects. The majority of the visuals for 3D games consist of models, such as characters, interactive objects, and the world around the player.

You can use tools like [ProBuilder](https://docs.unity3d.com/Packages/com.unity.probuilder@latest?/) to create models in the Unity Editor. However, these work best for prototyping, rather than for your final product.

To add more polished 3D assets to your final product, create 3D models, along with their materials and textures, in 3D modeling software, then import them into the Editor.

![Left: A 3D polygon mesh for a player character. Right: The player mesh rendered in Unity with materials](../uploads/Main/quickstart-3D-Graphics.png)


Left: A 3D polygon mesh for a player character. Right: The player mesh rendered in Unity with materials

[Import models](ImportingModelFiles.html) into the Editor to use them in your project. The Editor uses the `.fbx` format. You can also use other common native [model formats](3D-formats.html) (for example, `.max`, `.blend`, `.mb`, `.ma`); the Editor converts them into `.fbx` when you import them.

### Rendering meshes

A 3D mesh is the structural build of a 3D model. It’s made up of multiple polygon shapes. To add a 3D model to a GameObject, your GameObject needs two components:

1. The [Mesh Filter](class-MeshFilter.html)A mesh component that takes a mesh from your assets and passes it to the Mesh Renderer for rendering on the screen. [More info](class-MeshFilter.html)  
   See in [Glossary](Glossary.html#MeshFilter) component, which includes the actual mesh.
2. The [Mesh Renderer](class-MeshRenderer.html)A mesh component that takes the geometry from the Mesh Filter and renders it at the position defined by the object’s Transform component. [More info](class-MeshRenderer.html)  
   See in [Glossary](Glossary.html#MeshRenderer) component, which adds a material to the mesh to make the mesh visible in your scene.

### Materials

[Materials](Materials.html)An asset that defines how a surface should be rendered. [More info](class-Material.html)  
See in [Glossary](Glossary.html#Material) combine information about the visual appearance of a surface, such as [textures](Textures.html)An image used when rendering a GameObject, Sprite, or UI element. Textures are often applied to the surface of a mesh to give it visual detail. [More info](class-TextureImporter.html)  
See in [Glossary](Glossary.html#texture), color tints, and [shaders](Shaders.html)A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#shader). Use materials to define how to render surfaces.

* Textures are any 2D image files that you import into Unity. Use [textures](Textures.html) to wrap a mesh and add fine detail to a model. Use color tints to alter the color of the texture.
* [Shaders](Shaders.html) set lighting input and material configuration to control how each **pixel**The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](ShadowPerformance.html)  
  See in [Glossary](Glossary.html#pixel) renders, which determines how a GameObject looks on a screen.

For [material design](https://learn.unity.com/tutorial/shading-material-design?utm_source=first-time&utm_medium=docs), refer to the Unity Learn Tutorial.

[Back to Top](#TopOfPage)

## Building in-game environments

![An environment has been created by adding models and other assets to the scene.](../uploads/Main/quickstart-3D-environment.png)


An environment has been created by adding models and other assets to the scene.

Environment design is the process of creating the world the gameplay takes place in. You can design and build your environment in the Unity Editor, or you can design an environment outside of the Editor and import it.

To build an in-game environment, add GameObjects to the scene and position them to suit your preference and design. You can use [ProBuilder](docs.unity3d.com/packages/com.unity.probuilder@latest/manual/index.html) to prototype the design and gameplay.

In addition to hand-placing your models in the scene, the Unity Editor includes a built-in set of **Terrain**The landscape in your scene. A Terrain GameObject adds a large flat plane to your scene and you can use the Terrain’s Inspector window to create a detailed landscape. [More info](terrain-UsingTerrains.html)  
See in [Glossary](Glossary.html#Terrain) features that allow you to add landscapes to your game. In the Editor, you can create multiple Terrain tiles, adjust the height or appearance of your landscape, and add trees or grass to it. Read more about [Creating and Using Terrains](terrain-UsingTerrains.html).

[Back to Top](#TopOfPage)

## Animation

Animations describe how objects change based on game states, player interaction, time, and so on. They also give characters their movement, create cutscenes, and change the environment.

There are two ways to add animations to your game:

* Import animations made in other programs.
* Animate your assets directly in the Editor.

For more information, refer to the [Unity Learn animation topic](https://learn.unity.com/search/?k=%5B%22tag%3A5807188409091500644028e8%22%5D).

### Importing Animations

When you import a model with animation clips, you can choose which of its clips to import. This means you can animate models in a third-party application, then access and edit the clips in the Editor.

For more information, refer to [the Animation tab of the **Model Import Settings** window](class-AnimationClip.html).

### Animating Models in Unity

Use the [Animation window](AnimationEditorGuide.html) to create and modify animation clips in the Editor.

To learn how animation works in the Editor, refer to [Mecanim Animation system](AnimationOverview.html).

### The Animator window

You can use the [Animator window](AnimatorWindow.html)The window where the Animator Controller is visualized and edited. [More info](AnimatorWindow.html)  
See in [Glossary](Glossary.html#AnimatorWindow) to:

* Create and set up the [Animation Controller](class-AnimatorController.html).
* Create [animator states](class-State.html) with [animation clips](AnimationClips.html)Animation data that can be used for animated characters or simple animations. It is a simple “unit” piece of motion, such as (one specific instance of) “Idle”, “Walk” or “Run”. [More info](class-AnimationClip.html)  
  See in [Glossary](Glossary.html#AnimationClip).
* Create [animator parameters](AnimationParameters.html), which scripts can access or assign values to.
* Create [animator transitions](class-Transition.html), which specify conditions (based on parameters) for state changes and how states blend.

### Controlling animations

To control which [animation clips](AnimationClips.html) play, you can:

* Call them directly in a script with the [Animator](https://docs.unity3d.com/ScriptReference/Animator.html) class.
* Create and modify an [Animator Controller](class-AnimatorController.html)Controls animation through Animation Layers with Animation State Machines and Animation Blend Trees, controlled by Animation Parameters. The same Animator Controller can be referenced by multiple models with Animator components. [More info](class-AnimatorController.html)  
  See in [Glossary](Glossary.html#AnimatorController) in the [**Animator** window](AnimatorWindow.html).

[Back to Top](#TopOfPage)

## Lighting

Light your scenes to add depth and mood to your environments.

All built-in scene templates, except the Empty template, include a single Light GameObject. For most scenes, you’ll want to create additional Light GameObjects to create the desired lighting.

For more information, refer to:

* [Types of Light](Lighting.html).
* [Configuring Light components](lighting-light-components-configuring.html).
* The Unity Learn [Lighting in URP](https://learn.unity.com/project/creative-core-lighting?utm_source=first-time&utm_medium=docs) tutorial.

![A spot light creates atmospheric lighting in this scene](../uploads/Main/quickstart-3D-lights.png)


A spot light creates atmospheric lighting in this scene

[Back to Top](#TopOfPage)

## Audio

To add background music and sound effects to your game, refer to [Audio Overview](AudioOverview.html). You’ll need to use third-party software to create your audio and import it into the Editor. Then, you can mix your sounds, place them in scenes, and create ambient sound.

[Back to Top](#TopOfPage)

## Physics

![The Player character has a capsule collider component that uses the Physics system to allow the character to collide with the walls. ](../uploads/Main/quickstart-3D-physics.png)


The Player character has a capsule collider component that uses the Physics system to allow the character to collide with the walls.

Use Unity’s physics system to control how objects interact with each other and with their environment. For example, you can:

* Use forces, such as gravity and mechanics, which define how GameObjects behave on collision.
* Create custom physics to fit the design of your game, which might not require an accurate simulation of Earth.

To learn how to use Unity’s physics system, you can refer to:

* The [2D Beginner: Adventure Game](https://learn.unity.com/course/2d-beginner-adventure-game?utm_source=first-time&utm_medium=docs) Unity Learn tutorial.
* The [Unity Learn physics topic](https://learn.unity.com/search?k=%5B%22q%3Aphysics%22%5D).
* The [Physics section](PhysicsSection.html) of the User Manual.

To apply the physics system to a GameObject, use the ****Rigidbody**A component that allows a GameObject to be affected by simulated gravity and other forces. [More info](class-Rigidbody.html)  
See in [Glossary](Glossary.html#Rigidbody)** and ****Collider**An invisible shape that is used to handle physical collisions for an object. A collider doesn’t need to be exactly the same shape as the object’s mesh - a rough approximation is often more efficient and indistinguishable in gameplay. [More info](CollidersOverview.html)  
See in [Glossary](Glossary.html#collider)** components:

| Component | Impact on a GameObject |
| --- | --- |
| [**Rigidbody**](RigidbodiesOverview.html) | Allows your GameObject to be affected by the physics system, and react to things like gravity and collisions. |
| [**Collider**](CollidersOverview.html) | Enable GameObjects to interact with other GameObjects in the scene. For example, GameObjects with a collider can move or be moved by another GameObject with a collider. |
| [**Collider with a trigger**](collider-interactions-other-events.html) | Call a function in code when two GameObjects intersect. |

[Back to Top](#TopOfPage)

## User Interface

To create interface elements, such as menus, gear lists, and information pop-ups, use [UI Toolkit](UIElements.html).

[Back to Top](#TopOfPage)

# Additional resources

* [Get started with 3D game development](Quickstart3D.html)
* [Get started with 2D game development](2d-game-development-landing.html)

Get started with monetization and mobile ad mediation

Project configuration

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)