* [UI systems](UIToolkits.html)
* [IMGUI (Immediate Mode GUI)](ui-imgui.html)
* GUI Skin (IMGUI System)

Extending IMGUI

GUI Style (IMGUI System)

# GUI Skin (IMGUI System)

[Switch to Scripting](../ScriptReference/GUISkin.html "Go to GUISkin page in the Scripting Reference")

**GUISkins** are a collection of **GUIStyles** that can be applied to your GUI. Each **Control** type has its own Style definition. Skins are intended to allow you to apply style to an entire UI, instead of a single Control by itself.

![A GUI Skin as seen in the Inspector](../uploads/Main/Inspector-GUISkin.png)


A GUI Skin as seen in the Inspector

To create a GUISkin, select **Assets->Create->GUI Skin** from the menubar.

**Please Note**: This page refers to part of the [IMGUI](GUIScriptingGuide.html) system, which is a *scripting-only* UI system. Unity has a full GameObject-based UI system which you may prefer to use. It allows you to design and edit user interface elements as visible objects in the **scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) view. See the [UI System Manual](com.unity.ugui.html) for more information.

## Properties

All of the properties within a GUI Skin are an individual [GUIStyle](class-GUIStyle.html). Please read the [GUIStyle](class-GUIStyle.html) page for more information about how to use Styles.

| ***Property:*** | ***Function:*** |
| --- | --- |
| **Font** | The global Font to use for every Control in the GUI |
| **Box** | The [Style](class-GUIStyle.html) to use for all Boxes |
| **Button** | The [Style](class-GUIStyle.html) to use for all Buttons |
| **Toggle**A checkbox that allows the user to switch an option on or off. [More info](UIE-uxml-element-Toggle.html) See in [Glossary](Glossary.html#Toggle) | The [Style](class-GUIStyle.html) to use for all Toggles |
| **Label** | The [Style](class-GUIStyle.html) to use for all Labels |
| **Text Field** | The [Style](class-GUIStyle.html) to use for all Text Fields |
| **Text Area** | The [Style](class-GUIStyle.html) to use for all Text Areas |
| **Window** | The [Style](class-GUIStyle.html) to use for all Windows |
| **Horizontal Slider** | The [Style](class-GUIStyle.html) to use for all Horizontal Slider bars |
| **Horizontal Slider Thumb** | The [Style](class-GUIStyle.html) to use for all Horizontal Slider Thumb Buttons |
| **Vertical Slider** | The [Style](class-GUIStyle.html) to use for all Vertical Slider bars |
| **Vertical Slider Thumb** | The [Style](class-GUIStyle.html) to use for all Vertical Slider Thumb Buttons |
| **Horizontal Scrollbar** | The [Style](class-GUIStyle.html) to use for all Horizontal Scrollbars |
| **Horizontal Scrollbar Thumb** | The [Style](class-GUIStyle.html) to use for all Horizontal Scrollbar Thumb Buttons |
| **Horizontal Scrollbar Left Button** | The [Style](class-GUIStyle.html) to use for all Horizontal Scrollbar scroll Left Buttons |
| **Horizontal Scrollbar Right Button** | The [Style](class-GUIStyle.html) to use for all Horizontal Scrollbar scroll Right Buttons |
| **Vertical Scrollbar** | The [Style](class-GUIStyle.html) to use for all Vertical Scrollbars |
| **Vertical Scrollbar Thumb** | The [Style](class-GUIStyle.html) to use for all Vertical Scrollbar Thumb Buttons |
| **Vertical Scrollbar Up Button** | The [Style](class-GUIStyle.html) to use for all Vertical Scrollbar scroll Up Buttons |
| **Vertical Scrollbar Down Button** | The [Style](class-GUIStyle.html) to use for all Vertical Scrollbar scroll Down Buttons |
| **Custom 1–20** | Additional custom Styles that can be applied to any Control |
| **Custom Styles** | An array of additional custom Styles that can be applied to any Control |
| **Settings** | Additional Settings for the entire GUI |
| **Double Click Selects Word** | If enabled, double-clicking a word will select it |
| **Triple Click Selects Line** | If enabled, triple-clicking a word will select the entire line |
| **Cursor Color** | Color of the keyboard cursor |
| **Cursor Flash Speed** | The speed at which the text cursor will flash when editing any Text Control |
| **Selection Color** | Color of the selected area of Text |

## Details

When you are creating an entire GUI for your game, you will likely need to do a lot of customization for every different Control type. In many different game genres, like real-time strategy or role-playing, there is a need for practically every single Control type.

Because each individual Control uses a particular Style, it does not make sense to create a dozen-plus individual Styles and assign them all manually. GUI Skins take care of this problem for you. By creating a GUI Skin, you have a pre-defined collection of Styles for every individual Control. You then apply the Skin with a single line of code, which eliminates the need to manually specify the Style of each individual Control.

### Creating GUISkins

GUISkins are asset files. To create a GUI Skin, select **Assets->Create->GUI Skin** from the menubar. This will put a new GUISkin in your **Project View**.

![A new GUISkin file in the Project View](../uploads/Main/imgui/GUISkin-ProjectView.png)


A new GUISkin file in the Project View

### Editing GUISkins

After you have created a GUISkin, you can edit all of the [Styles](class-GUIStyle.html) it contains in the **Inspector**A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector). For example, the **Text Field** [Style](class-GUIStyle.html) will be applied to all Text Field Controls.

![Editing the Text Field Style in a GUISkin](../uploads/Main/imgui/GUISkin-EditingTextField.png)


Editing the Text Field Style in a GUISkin

No matter how many Text Fields you create in your script, they will all use this [Style](class-GUIStyle.html). Of course, you have control over changing the styles of one Text Field over the other if you wish. We’ll discuss how that is done next.

### Applying GUISkins

To apply a GUISkin to your GUI, you must use a simple script to read and apply the Skin to your Controls.

```
    // Create a public variable where we can assign the GUISkin
    var customSkin : GUISkin;

    // Apply the Skin in our OnGUI() function
    function OnGUI () {
        GUI.skin = customSkin;

        // Now create any Controls you like, and they will be displayed with the custom Skin
        GUILayout.Button ("I am a re-Skinned Button");

        // You can change or remove the skin for some Controls but not others
        GUI.skin = null;

        // Any Controls created here will use the default Skin and not the custom Skin
        GUILayout.Button ("This Button uses the default UnityGUI Skin");
    }
```

In some cases you want to have two of the same Control with different Styles. For this, it does not make sense to create a new Skin and re-assign it. Instead, you use one of the **Custom** Styles in the skin. Provide a **Name** for the custom Style, and you can use that name as the last argument of the individual Control.

```
    // One of the custom Styles in this Skin has the name "MyCustomControl"
    var customSkin : GUISkin;

    function OnGUI () {
        GUI.skin = customSkin;

        // We provide the name of the Style we want to use as the last argument of the Control function
        GUILayout.Button ("I am a custom styled Button", "MyCustomControl");

        // We can also ignore the Custom Style, and use the Skin's default Button Style
        GUILayout.Button ("I am the Skin's Button Style");
    }
```

For more information about working with GUIStyles, please read the [GUIStyle](class-GUIStyle.html) page. For more information about using UnityGUI, please read the [GUI Scripting Guide](GUIScriptingGuide.html).

GUISkin

Extending IMGUI

GUI Style (IMGUI System)

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)