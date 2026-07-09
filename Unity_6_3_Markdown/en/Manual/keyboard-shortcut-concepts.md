* [Unity Editor interface](unity-editor.html)
* [Navigating and managing the Unity Editor](editor-navigating-managing.html)
* [Keyboard shortcuts](ShortcutsManager.html)
* Introduction to keyboard shortcuts

Keyboard shortcuts

Manage keyboard shortcuts

# Introduction to keyboard shortcuts

Understand how global and contextual shortcuts work, how to resolve shortcut conflicts, and how to organize shortcuts with profiles.

For information about how to view, assign, and manage shortcuts, refer to [Shortcuts window reference](shortcuts-view.html) and [Manage keyboard shortcuts](shortcuts-manage.html).

## Global commands, contextual commands, and conflicts

Unity Editor shortcuts can be global or contextual.

* Global shortcuts are always available. For example, by default the command to undo an action uses the shortcut **Ctrl/Cmd + Z**. Using that shortcut always undoes the most recent action, regardless of which windows are open and which tools are active.
* Contextual shortcuts only work when you use a particular view or set of tools. For example, by default the square bracket keys **[** and **]** have different uses in the **Terrain**The landscape in your scene. A Terrain GameObject adds a large flat plane to your scene and you can use the Terrain’s Inspector window to create a detailed landscape. [More info](terrain-UsingTerrains.html)  
  See in [Glossary](Glossary.html#Terrain) tool and the Grid Painting tool. When you use the bracket shortcut, Unity executes the command for whichever tool is active.

You can assign any keyboard shortcut to either:

* One global command.
* One or more contextual commands from different contexts.

### Context-based conflicts

You get a shortcut conflict if you assign the same keyboard shortcut to:

* More than one global command.
* More than one contextual command from the same context.
* A global command and a contextual command.

When you create a conflict, the Editor displays a warning icon in the **Shortcuts** window. You can resolve the conflict by changing one of the conflicting shortcuts.

### Exceptions to context-based conflicts

The Editor has a few global commands that can share shortcuts without creating conflict, because something other than context differentiates them. For example, the **Q**, **W**, and **E** keys:

* In the ****Scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
  See in [Glossary](Glossary.html#Scene)** and **Game** views, use these keys to toggle the **View**, **Move**, and **Rotate** tools.
* In the **Flythrough** mode, use these keys to move down, forward, and up.

## Command types

There are three types of commands in Unity:

* Action: Triggers once, when you press the shortcut.
* Clutch: Triggers twice, when you press the shortcut and when you release it.
* Menu: Activates a main menu option.

  **Tip**: You can also access menu items from the **Search** window. For more information, refer to [Search the Unity Editor main menu](search-menus.html).

## Profiles

The Unity Editor saves keyboard shortcuts to profiles. You can create multiple profiles and move between them without restarting the Editor. With shortcut profiles, you can customize your shortcuts for different workflows, package sets, or custom tools. For more information on creating, renaming, deleting, and switching between shortcut profiles, refer to [Manage shortcut profiles](shortcut-profiles.html).

Unity automatically saves any changes you make to shortcuts to the active profile. If the active profile is the default profile, Unity saves the changes to a new copy of the default profile.

### The default profile

The **Default** profile is the profile that the Editor uses when you first install it. It’s also the profile that forms the basis for any new profiles you create, so you don’t have to assign every shortcut in a new profile: only those you want to change.

You can’t modify the default profile. If you try to modify it, the Editor automatically creates a copy of the default profile, names it **Default Copy**, makes that copy the active profile, and applies your change to that copy.

### Profile availability

The Editor supports reusing profiles across projects and versions:

* Your shortcut profiles are available in all Unity projects because Unity saves them with the global [Preferences](Preferences.html), not under your [project directory](default-directories.html). For information on where Unity stores preferences, refer to the [`EditorPrefs`](../ScriptReference/EditorPrefs.html) API reference page.
* When you upgrade from an older version of the Editor, your saved shortcuts are available in the new version.
* You can also use the **Shortcuts** window to export or import shortcut profiles as JSON files. For more information, refer to [Manage shortcut profiles](shortcut-profiles.html).

## Additional resources

* [Shortcuts window reference](shortcuts-view.html)
* [Manage keyboard shortcuts](shortcuts-manage.html)
* [Manage shortcut profiles](shortcut-profiles.html)

Keyboard shortcuts

Manage keyboard shortcuts

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)