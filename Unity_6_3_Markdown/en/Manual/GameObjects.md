* [GameObjects](working-with-gameobjects.html)
* Introduction to GameObjects

GameObjects

GameObject fundamentals

# Introduction to GameObjects

The **GameObject**The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) is the most important concept in the Unity Editor.

Every object in your game is a **GameObject**, from characters and collectible items to lights, **cameras**A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera) and special effects. However, a GameObject can’t do anything on its own; you need to give it properties before it can become a character, an environment, or a special effect.

![Four different types of GameObject: an animated character, a light, a tree, and an audio source](../uploads/Main/GameObjectsExamples.jpg)


Four different types of GameObject: an animated character, a light, a tree, and an audio source

**GameObjects** are the fundamental objects in Unity that represent characters, props and scenery. They do not accomplish much in themselves but they act as containers for **Components**A functional part of a GameObject. A GameObject can contain any number of components. Unity has many built-in components, and you can create your own by writing scripts that inherit from MonoBehaviour. [More info](UsingComponents.html)  
See in [Glossary](Glossary.html#component), which implement the functionality.

To give a GameObject the properties it needs to become a light, or a tree, or a camera, you need to add [components](Components.html) to it. Depending on what kind of object you want to create, you add different combinations of components to a GameObject.

Unity has lots of different built-in component types, and you can also make your own components using the [Unity Scripting API](CreatingComponents.html).

For example, a Light object is created by attaching a [Light](class-Light.html) component to a GameObject.

![A simple Light GameObject with several Components](../uploads/Main/GameObjectLightExample1.png)


A simple Light GameObject with several Components

A solid cube object has a **Mesh**The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](mesh.html)  
See in [Glossary](Glossary.html#Mesh) Filter and **Mesh Renderer**A mesh component that takes the geometry from the Mesh Filter and renders it at the position defined by the object’s Transform component. [More info](class-MeshRenderer.html)  
See in [Glossary](Glossary.html#MeshRenderer) component, to draw the surface of the cube, and a Box **Collider**An invisible shape that is used to handle physical collisions for an object. A collider doesn’t need to be exactly the same shape as the object’s mesh - a rough approximation is often more efficient and indistinguishable in gameplay. [More info](CollidersOverview.html)  
See in [Glossary](Glossary.html#collider) component to represent the object’s solid volume in terms of physics.

![A simple Cube GameObject with several Components](../uploads/Main/GameObjectCubeExample1.png)


A simple Cube GameObject with several Components

## Details

A GameObject always has a [Transform](class-Transform.html) component attached (to represent position and orientation) and it is not possible to remove this. The other components that give the object its functionality can be added from the editor’s **Component** menu or from a script. There are also many useful pre-constructed objects (primitive shapes, Cameras, etc) available on the **GameObject > 3D Object** menu, see [Primitive Objects](PrimitiveObjects.html).

Because GameObjects are an important part of Unity, there is a lot of manual content with extensive detail about them. See the following sections for more information on using GameObjects in Unity:

* [Transforms](class-Transform.html)
* [Introduction to components](Components.html)
* [Using Components](UsingComponents.html)
* [Primitive and placeholder objects](PrimitiveObjects.html)
* [Creating components with scripting](CreatingComponents.html)
* [Deactivating GameObjects](DeactivatingGameObjects.html)
* [Tags](Tags.html)  
  See in [Glossary](Glossary.html#tag)
* [Static GameObjects](StaticObjects.html)
* [Saving your work](Saving.html)

You can find out more about controlling GameObjects from **scripts**A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts) on the [GameObject scripting reference page](../ScriptReference/GameObject.html).

GameObjects

GameObject fundamentals

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)