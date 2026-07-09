* [GameObjects](working-with-gameobjects.html)
* [Prefabs](Prefabs.html)
* [Instantiating prefabs at runtime](instantiating-prefabs.html)
* Introduction to instantiating prefabs

Instantiating prefabs at runtime

Build a structure with prefabs

# Introduction to instantiating prefabs

You can use [prefabs](prefabs-introduction.html)An asset type that allows you to store a GameObject complete with components and properties. The prefab acts as a template from which you can create new object instances in the scene. [More info](Prefabs.html)  
See in [Glossary](Glossary.html#prefab) to instantiate complicated **GameObjects**The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) or collections of GameObjects at runtime. Compared with creating GameObjects from scratch using code, instantiating prefabs using code has many advantages because you can do the following:

* Instantiate a prefab using one line of code. Creating equivalent GameObjects from scratch requires many more lines of code.
* Change which prefab is instantiated without changing the code. You can make a simple rocket into a super-charged rocket, without any code changes.

## Common scenarios

Instantiating prefabs at runtime is useful in the following common scenarios:

* Building a structure out of a single prefab by replicating it multiple times in different positions, for example in a grid or circle formation.
* Firing a projectile prefab from a launcher. The projectile prefab can be a complex configuration containing a **mesh**The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](mesh.html)  
  See in [Glossary](Glossary.html#Mesh), **Rigidbody**A component that allows a GameObject to be affected by simulated gravity and other forces. [More info](class-Rigidbody.html)  
  See in [Glossary](Glossary.html#Rigidbody), **collider**An invisible shape that is used to handle physical collisions for an object. A collider doesn’t need to be exactly the same shape as the object’s mesh - a rough approximation is often more efficient and indistinguishable in gameplay. [More info](CollidersOverview.html)  
  See in [Glossary](Glossary.html#collider), **audio source**A component which plays back an Audio Clip in the scene to an audio listener or through an audio mixer. [More info](class-AudioSource.html)  
  See in [Glossary](Glossary.html#AudioSource), dynamic light, and a child GameObject with its own trail **Particle**A small, simple image or mesh that is emitted by a particle system. A particle system can display and move particles in great numbers to represent a fluid or amorphous entity. The effect of all the particles together creates the impression of the complete entity, such as smoke. [More info](class-ParticleSystem.html)  
  See in [Glossary](Glossary.html#particle) System.
* A vehicle, building, or character, for example a robot, breaking apart into many pieces. In this scenario, the example script deletes and replaces the complete, operational robot prefab with a wrecked robot prefab. This wrecked prefab consists of separate broken parts of the robot, each set up with Rigidbody components and **Particle Systems**A component that simulates fluid entities such as liquids, clouds and flames by generating and animating large numbers of small 2D images in the scene. [More info](class-ParticleSystem.html)  
  See in [Glossary](Glossary.html#particlesystem) of their own. This technique allows you to blow up a robot into many pieces with just one line of code, which replaces the original GameObject with a wrecked prefab.

## Instantiate a prefab

To instantiate a prefab at runtime, your code needs a reference to the prefab. To make this reference, you can create a public field of type `GameObject` in your code, then assign the prefab you want to use to this field in the **Inspector**A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector).

The following script example has a single public variable, `myPrefab`, which is a reference to a prefab. It creates an instance of that prefab in the `Start` method.

```
using UnityEngine;
public class InstantiationExample : MonoBehaviour 
{
    // Reference to the prefab. Drag a prefab into this field in the Inspector.
    public GameObject myPrefab;

    // This script will simply instantiate the prefab when the game starts.
    void Start()
    {
        // Instantiate at position (0, 0, 0) and zero rotation.
        Instantiate(myPrefab, new Vector3(0, 0, 0), Quaternion.identity);
    }
}
```

To use this example:

1. Create a new MonoBehaviour script in your Project, and name it `InstantiationExample`.
2. Copy the code and paste it into your new script, and save it.
3. Create an empty GameObject using the menu **GameObject** > **Create Empty**.
4. Add the script to the new GameObject as a component by dragging it onto the empty GameObject.
5. [Create any prefab](CreatingPrefabs.html), and drag it from the ****Project window**A window that shows the contents of your `Assets` folder (Project tab) [More info](ProjectView.html)  
   See in [Glossary](Glossary.html#Projectwindow)** into the **My Prefab** field in the script component.

When you enter Play mode, the prefab instantiates at position (0 , 0 , 0) in the **scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene).

You can drag a different prefab into the **My Prefab** field in the **Inspector** window to change which prefab Unity instantiates, without having to change the script.

## Additional resources

* [Build a structure with prefabs](instantiating-prefabs-structure.html)
* [Instantiate projectiles and explosions](instantiating-prefabs-projectiles.html)
* [`Instantiate` API reference](../ScriptReference/Object.Instantiate.html)

Instantiating prefabs at runtime

Build a structure with prefabs

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)