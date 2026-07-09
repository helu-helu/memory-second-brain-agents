* [Unity Editor interface](unity-editor.html)
* [Customizing the Unity Editor](editor-customize.html)
* Programming with gizmos and handles

Create a custom overlay

Unity Editor settings reference

# Programming with gizmos and handles

The [`Gizmos`](../ScriptReference/Gizmos.html) and [`Handles`](../ScriptReference/Handles.html) classes allow you to draw lines and shapes in the ****Scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene)** view and **Game** view, as well as interactive handles and controls. These two classes together provide a way for you to extend what is shown in these views and build interactive tools to edit your project in any way you like.

For example, rather than entering numbers in the **Inspector**A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector), you could create a draggable circle radius **gizmo**A graphic overlay associated with a GameObject in a Scene, and displayed in the Scene View. Built-in scene tools such as the move tool are Gizmos, and you can create custom Gizmos using textures or scripting. Some Gizmos are only drawn when the GameObject is selected, while other Gizmos are drawn by the Editor regardless of which GameObjects are selected. [More info](GizmosMenu.html#GizmosIcons)  
See in [Glossary](Glossary.html#Gizmo) around a non-player character in a game, which represents the area within which they can hear or see the player.

## Gizmos

The `Gizmos` class allows you to draw lines, spheres, cubes, icons, textures and meshes into the **Scene view**An interactive view into the world you are creating. You use the Scene View to select and position scenery, characters, cameras, lights, and all other types of Game Object. [More info](UsingTheSceneView.html)  
See in [Glossary](Glossary.html#SceneView) to use as debugging, set-up aids, or tools while developing your project.

The following example draws a 10 unit yellow wire cube around a **GameObject**The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject):

```
using UnityEngine;
public class GizmosExample : MonoBehaviour
{
    void OnDrawGizmosSelected()
    {
        // Draw a yellow cube at the transform position
        Gizmos.color = Color.yellow;
        Gizmos.DrawWireCube(transform.position, new Vector3(10, 10, 10));
    }
}
```

The following image shows how this cube looks when placed on a Directional Light GameObject:

![A light GameObject with an extra script applied which draws a cube gizmo around its position](../uploads/Main/ScriptingGizmoExample.png)


A light GameObject with an extra script applied which draws a cube gizmo around its position

For a full API reference including usage examples, refer to the API reference page for [`Gizmos`](../ScriptReference/Gizmos.html).

## Handles

Handles are similar to gizmos, but provide more interactivity and manipulation. The default 3D controls that Unity provides to manipulate items in the Scene view are a combination of gizmos and handles. There are a number of built-in handle GUIs, such as the familiar tools to position, scale and rotate an object via the [Transform](class-Transform.html) component.

You can define your own handle GUIs to use with custom component editors. Such GUIs can be a very useful way to edit procedurally-generated Scene content, “invisible” items and groups of related objects, such as waypoints and location markers.

The following example creates an arc area with an arrowhead handle, allowing you to modify a “shield area” in the Scene view:

```
using UnityEditor;
using UnityEngine;
using System.Collections;

//this class should exist somewhere in your project
public class WireArcExample : MonoBehaviour
{
    public float shieldArea;
}

// Create a 180 degrees wire arc with a ScaleValueHandle attached to the disc
// that lets you modify the "shieldArea" value in the WireArcExample
[CustomEditor(typeof(WireArcExample))]
public class DrawWireArc : Editor
{
    void OnSceneGUI()
    {
        Handles.color = Color.red;
        WireArcExample myObj = (WireArcExample)target;
        Handles.DrawWireArc(myObj.transform.position, myObj.transform.up, -myObj.transform.right, 180, myObj.shieldArea);
        myObj.shieldArea = (float)Handles.ScaleValueHandle(myObj.shieldArea, myObj.transform.position + myObj.transform.forward * myObj.shieldArea, myObj.transform.rotation, 1, Handles.ConeHandleCap, 1);
    }
}
```

![An example of an Arc handle and an Scale handle](../uploads/Main/ScriptingHandlesExample.png)


An example of an Arc handle and an Scale handle

For a full API reference including usage examples, refer to the API reference page for [`Handles`](../ScriptReference/Handles.html).

## Additional resources

* [Gizmos Menu](GizmosMenu.html)
* [Programming in Unity](scripting.html)

Create a custom overlay

Unity Editor settings reference

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)