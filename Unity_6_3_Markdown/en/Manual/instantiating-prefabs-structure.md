* [GameObjects](working-with-gameobjects.html)
* [Prefabs](Prefabs.html)
* [Instantiating prefabs at runtime](instantiating-prefabs.html)
* Build a structure with prefabs

Introduction to instantiating prefabs

Instantiate projectiles and explosions

# Build a structure with prefabs

You can use code to procedurally generate copies of a **prefab**An asset type that allows you to store a GameObject complete with components and properties. The prefab acts as a template from which you can create new object instances in the scene. [More info](Prefabs.html)  
See in [Glossary](Glossary.html#prefab) in a particular configuration. The following example creates a wall of block prefab instances.

## Create a block prefab asset

To create a wall of blocks, you must first have a block prefab asset to create the wall with.

1. In the Hierarchy, right-click and select **3D Object** > **Cube**.
2. Drag the cube into the **Assets** folder in the **Project window**A window that shows the contents of your `Assets` folder (Project tab) [More info](ProjectView.html)  
   See in [Glossary](Glossary.html#Projectwindow). Unity creates a prefab asset of the cube.
3. Rename the prefab asset to `Block`.
4. Delete the original cube asset from the Hierarchy.

## Create a script that instantiates blocks

Create a MonoBehaviour script and name it `Wall`. Add the following code into the `Wall` script:

```
using UnityEngine;
public class Wall : MonoBehaviour
{
   public GameObject block;
   public int width = 10;
   public int height = 4;
  
   void Start()
   {
       for (int y=0; y<height; ++y)
       {
           for (int x=0; x<width; ++x)
           {
               Vector3 pos = transform.position + new Vector3(x, y, 0);
               Instantiate(block, pos, Quaternion.identity);
           }
       }       
   }
}
```

## Attach the script to an empty GameObject

1. Create an empty **GameObject**The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)  
   See in [Glossary](Glossary.html#GameObject). Right-click on the Hierarchy and select **Create Empty**.
2. Attach the `Wall` script to the empty GameObject.
3. Drag the `Block` prefab asset into the **Block** field,
4. Enter Play mode and Unity generates a wall with the `Block` prefab.

![A wall built from 4 rows of 10 blocks. The empty GameObject is selected in the Inspector, with the Block prefab asset assigned to the Block field.](../uploads/Main/prefab-instantiate-wall.png)


A wall built from 4 rows of 10 blocks. The empty GameObject is selected in the Inspector, with the Block prefab asset assigned to the Block field.

You can also use code to place prefabs in a grid or other configurations. The following example places the cubes in a circular formation:

```
using UnityEngine;
public class CircleFormation : MonoBehaviour

{
    // Instantiates prefabs in a circle formation

    public GameObject prefab;
    public int numberOfObjects = 20;
    public float radius = 5f;

    void Start() 
    {
        for (int i = 0; i < numberOfObjects; i++)
        {
            float angle = i * Mathf.PI * 2 / numberOfObjects;
            float x = Mathf.Cos(angle) * radius;
            float z = Mathf.Sin(angle) * radius;
            Vector3 pos = transform.position + new Vector3(x, 0, z);
            float angleDegrees = -angle*Mathf.Rad2Deg;
            Quaternion rot = Quaternion.Euler(0, angleDegrees, 0);
            Instantiate(prefab, pos, rot);
        }
    }
}
```

When you attach the script to an empty GameObject and enter Play mode, Unity generates the cubes in the following formation:

![A circular arrangement of blocks.](../uploads/Main/prefab-instantiate-block-circle.png)


A circular arrangement of blocks.

## Additional resources

* [Instantiate projectiles and explosions](instantiating-prefabs-projectiles.html)
* [`Instantiate` API reference](../ScriptReference/Object.Instantiate.html)

Introduction to instantiating prefabs

Instantiate projectiles and explosions

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)