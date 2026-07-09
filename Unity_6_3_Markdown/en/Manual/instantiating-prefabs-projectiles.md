* [GameObjects](working-with-gameobjects.html)
* [Prefabs](Prefabs.html)
* [Instantiating prefabs at runtime](instantiating-prefabs.html)
* Instantiate projectiles and explosions

Build a structure with prefabs

Prefab instance Inspector reference

# Instantiate projectiles and explosions

You can instantiate **prefabs**An asset type that allows you to store a GameObject complete with components and properties. The prefab acts as a template from which you can create new object instances in the scene. [More info](Prefabs.html)  
See in [Glossary](Glossary.html#prefab) to use as projectiles and destroy them with explosion effects in your application.

The following example instantiates a projectile prefab when the user presses the fire button. You can attach it to a **GameObject**The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) which acts as a launcher for the prefab.

## Create a projectile prefab asset

1. In the Hierarchy, right-click and select **3D Object** > **Sphere**.
2. Select the sphere, and in its Inspector, select **Add Component** > **Rigidbody**. The sphere needs a Rigidbody so that it can fly through the air and detect when a collision happens.
3. Rename the sphere to `Projectile` and then drag it into the `Assets` folder of your project to [create a prefab asset](CreatingPrefabs.html#create-a-prefab-asset).
4. You can then delete the sphere from the Hierarchy.

You can optionally add a [texture](Textures.html)An image used when rendering a GameObject, Sprite, or UI element. Textures are often applied to the surface of a mesh to give it visual detail. [More info](class-TextureImporter.html)  
See in [Glossary](Glossary.html#texture) to the prefab, change its dimensions, or import a different [model](models.html)A 3D model representation of an object, such as a character, a building, or a piece of furniture. [More info](3D-formats.html)  
See in [Glossary](Glossary.html#model) to act as the projectile.

## Add an explosion script to the projectile prefab asset

To add an explosion to the projectile prefab, you must have a prefab asset that represents an explosion. You can use the [particle system](ParticleSystems.html)A component that simulates fluid entities such as liquids, clouds and flames by generating and animating large numbers of small 2D images in the scene. [More info](class-ParticleSystem.html)  
See in [Glossary](Glossary.html#particlesystem) to [create a prefab asset](CreatingPrefabs.html#create-a-prefab-asset), or find an explosion effect on the [Asset Store](https://assetstore.unity.com/vfx/particles/fire-explosions)A growing library of free and commercial assets created by Unity and members of the community. Offers a wide variety of assets, from textures, models and animations to whole project examples, tutorials and Editor extensions. [More info](AssetStore.html)  
See in [Glossary](Glossary.html#AssetStore) and add it to the `Assets` folder of your project.

Then create a script called `Projectile` as follows:

```
using UnityEngine;

public class Projectile : MonoBehaviour
{

    public GameObject explosion;
    void Start()
    {
         // Deletes the projectile after 10 seconds, regardless
         // of whether it collided with anything. This prevents
         // instances from staying in the scene indefinitely.
         Destroy(gameObject,10);
    }
    void OnCollisionEnter()
    {
        // When the projectile hits something, create an explosion
        // and remove the projectile.
        Instantiate(explosion,transform.position,transform.rotation);
        Destroy(gameObject);
    }
}
```

The script instantiates the explosion at the projectile’s current position and removes the projectile GameObject when the projectile collides with something.

To use the script, attach it to the projectile prefab asset:

1. Select the `Projectile` prefab asset and open it in [prefab editing mode](EditingInPrefabMode.html).
2. In the **Inspector**A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
   See in [Glossary](Glossary.html#Inspector), drag the `Projectile` script onto it.
3. Drag the explosion prefab asset into the **Explosion** field.

## Create a script to launch the projectiles

To launch the projectiles, you need to create a script that instantiates projectiles when the fire key is pressed, and add that script to a GameObject.

Create a script called `FireProjectile` and add the following contents to it:

```
using UnityEngine;
using UnityEngine.InputSystem;

public class FireProjectile : MonoBehaviour
{
    // Only GameObjects with a Rigidbody can be assigned as the projectile.
    public Rigidbody projectile;
    // Speed of the projectile when fired.
    // This is a public variable so it can be adjusted in the Unity Editor.
    public float speed = 4;
    // Update is called once per frame
    // This method checks for input and fires a projectile if the attack action is pressed.
    void Update()
    {
        // Check if the "Attack" action was pressed this frame
        // If it was, instantiate a projectile at the player's position and set its velocity.
        if (InputSystem.actions.FindAction("Attack").WasPressedThisFrame())
        {
            Rigidbody p = Instantiate(projectile, transform.position, transform.rotation);
            p.linearVelocity = transform.forward * speed;
        }
    }
}
```

This script uses `Instantiate` to launch a projectile. When making a public prefab variable, the variable type can be a GameObject, or it can be any valid component type (either a built-in Unity component or one of your own MonoBehaviour scripts).

For component type variables (such as Rigidbody, Collider, and Light), you can only assign GameObjects of that component type to the variable, and the `Instantiate` function returns a reference to that specific component on the new GameObject instance.

## Attach the launcher script to a GameObject

You must attach the script to a GameObject to use it. To do so:

1. Make sure that your scene has a ground GameObject for the projectile to collide with. If you’re using an empty project, create a Plane GameObject: right-click on the Hierarchy and select **3D Object** > **Plane**.
2. Create a Cube GameObject: right-click on the Hierarchy and select **3D Object** > **Cube** and position it over the plane.
3. Select the cube, and in its Inspector, delete the **Box **Collider**An invisible shape that is used to handle physical collisions for an object. A collider doesn’t need to be exactly the same shape as the object’s mesh - a rough approximation is often more efficient and indistinguishable in gameplay. [More info](CollidersOverview.html)  
   See in [Glossary](Glossary.html#collider)** component. If you don’t delete this component, the projectiles collide with the cube before hitting the ground.
4. Drag the `FireProjectile` script onto the cube.
5. Drag the `Projectile` prefab asset into the **Projectile** field of the Fire Projectile script.
6. Enter Play mode, and then click your mouse button.

The cube fires the sphere projectiles and the explosion happens when they collide with the ground.

![Projectile and explosion prefabs being instantiated and destroyed.](../uploads/Main/prefab-projectile-instantiate.png)


Projectile and explosion prefabs being instantiated and destroyed.

Note that any instantiated objects appear in the Hierarchy with `(Clone)` appended to the name.

## Additional resources

* [Build a structure with prefabs](instantiating-prefabs-structure.html)
* [`Instantiate` API reference](../ScriptReference/Object.Instantiate.html)

Build a structure with prefabs

Prefab instance Inspector reference

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)