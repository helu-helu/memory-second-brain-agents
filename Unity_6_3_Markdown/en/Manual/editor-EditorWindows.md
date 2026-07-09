* [UI systems](UIToolkits.html)
* [IMGUI (Immediate Mode GUI)](ui-imgui.html)
* [Extending the Editor with IMGUI](ExtendingTheEditor.html)
* Create custom Editor Windows with IMGUI

Extending the Editor with IMGUI

Use Property Drawers with IMGUI to customize the Inspector

# Create custom Editor Windows with IMGUI

**Note**: It’s strongly recommended to use the [UI Toolkit](UIElements.html) to extend the [Unity Editor](UIE-support-for-editor-ui.html), as it provides a more modern, flexible, and scalable solution than IMGUI.

You can create any number of custom windows in your app. These behave just like the **Inspector**A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector), **Scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) or any other built-in ones. This is a great way to add a user interface to a sub-system for your game.

![Custom Editor Interface by Serious Games Interactive used for scripting cutscene actions](../uploads/Main/CustomEditorWindow.jpg)


Custom Editor Interface by Serious Games Interactive used for scripting cutscene actions

Making a custom Editor Window involves the following simple steps:

* Create a script that derives from EditorWindow.
* Use code to trigger the window to display itself.
* Implement the GUI code for your tool.

### Derive From EditorWindow

In order to make your Editor Window, your script must be stored inside a folder called “Editor”. Make a class in this script that derives from EditorWindow. Then write your GUI controls in the inner OnGUI function.

```
using UnityEngine;
using UnityEditor;
using System.Collections;

public class Example : EditorWindow

    {
        void OnGUI () {
            // The actual window code goes here
           }
    }
```

*MyWindow.cs - placed in a folder called ‘Editor’ within your project.*

### Showing the window

In order to show the window on screen, make a menu item that displays it. This is done by creating a function which is activated by the
**MenuItem** property.

The default behavior in Unity is to recycle windows, so selecting the menu item again would show existing windows. This is done by using the function [EditorWindow.GetWindow](../ScriptReference/EditorWindow.GetWindow.html) Like this:

```
using UnityEngine;
using UnityEditor;
using System.Collections;

class MyWindow : EditorWindow {
    [MenuItem ("Window/My Window")]

    public static void  ShowWindow () {
        EditorWindow.GetWindow(typeof(MyWindow));
    }
    
    void OnGUI () {
        // The actual window code goes here
    }
}
```

*Showing the MyWindow*

This will create a standard, dockable editor window that saves its position between invocations, can be used in custom layouts, etc. To have more control over what gets created, you can use [GetWindowWithRect](../ScriptReference/EditorWindow.GetWindowWithRect.html)

### Implementing Your Window’s GUI

The actual contents of the window are rendered by implementing the OnGUI function. You can use the same UnityGUI classes you use for your ingame GUI (**GUI** and **GUILayout**). In addition we provide some additional GUI controls, located in the editor-only classes **EditorGUI** and **EditorGUILayout**. These classes add to the controls already available in the normal classes, so you can mix and match at will.

The following C# code shows how you can add GUI elements to your custom EditorWindow:

```
using UnityEditor;
using UnityEngine;

public class MyWindow : EditorWindow
{
    string myString = "Hello World";
    bool groupEnabled;
    bool myBool = true;
    float myFloat = 1.23f;
    
    // Add menu item named "My Window" to the Window menu
    [MenuItem("Window/My Window")]
    public static void ShowWindow()
    {
        //Show existing window instance. If one doesn't exist, make one.
        EditorWindow.GetWindow(typeof(MyWindow));
    }
    
    void OnGUI()
    {
        GUILayout.Label ("Base Settings", EditorStyles.boldLabel);
        myString = EditorGUILayout.TextField ("Text Field", myString);
        
        groupEnabled = EditorGUILayout.BeginToggleGroup ("Optional Settings", groupEnabled);
            myBool = EditorGUILayout.Toggle ("Toggle", myBool);
            myFloat = EditorGUILayout.Slider ("Slider", myFloat, -3, 3);
        EditorGUILayout.EndToggleGroup ();
    }
}
```

This example results in a window which looks like this:

![Custom Editor Window created using supplied example.](../uploads/Main/ExampleEditorWindow.png)


Custom Editor Window created using supplied example.

For more info, take a look at the example and documentation on the [EditorWindow page](../ScriptReference/EditorWindow.html).

Extending the Editor with IMGUI

Use Property Drawers with IMGUI to customize the Inspector

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)