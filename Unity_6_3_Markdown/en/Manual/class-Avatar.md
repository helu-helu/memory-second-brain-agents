* [Animation](AnimationSection.html)
* [Mecanim Animation system](animation-mecanim.html)
* [Humanoid Avatar](AvatarCreationandSetup.html)
* Avatar Mapping tab reference

Scripting Root Motion

Avatar Muscle & Settings tab reference

# Avatar Mapping tab reference

[Switch to Scripting](../ScriptReference/Avatar.html "Go to Avatar page in the Scripting Reference")

The Avatar Mapping tab is available when the Unity Editor is in Avatar Configuration mode.

To enter Avatar Configuration mode, either:

* select the Avatar Asset in the **Project window**A window that shows the contents of your `Assets` folder (Project tab) [More info](ProjectView.html)  
  See in [Glossary](Glossary.html#Projectwindow), and click “Configure Avatar” in the Inspector, or
* select the Model Asset in the Project window, go to the “Rig” tab in the Inspector, and click “Configure…” under the Avatar Definition menu.

When you are in Avatar Configuration mode, the **Avatar Mapping** tab appears in the **Inspector**A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector) displaying Unity’s bone mapping:

![The Avatar window displays the bone mapping](../uploads/Main/classAvatar-Inspector.png)


The Avatar window displays the bone mapping

**(A)** Buttons to toggle between the **Mapping** and **Muscles & Settings** tabs. You must **Apply** or **Revert** any changes made before switching between tabs.

**(B)** Buttons to switch between the sections of the Avatar: **Body**, **Head**, **Left Hand**, and **Right Hand**.

**(C)** Menus which provide various **Mapping** and **Pose** tools to help you map the bone structure to the Avatar.

**(D)** Buttons to accept any changes made (**Accept**), discard any changes (**Revert**), and leave the Avatar window (**Done**). You must **Apply** or **Revert** any changes made before leaving the **Avatar**An interface for retargeting animation from one rig to another. [More info](ConfiguringtheAvatar.html)  
See in [Glossary](Glossary.html#Avatar) window.

The Avatar Mapping indicates which of the bones are required (solid circles) and which are optional (dotted circles). Unity can interpolate optional bone movements automatically.

## Saving and reusing Avatar data (Human Template files)

You can save the mapping of bones in your skeleton to the Avatar on disk as a [Human Template file](class-HumanTemplate.html) (extention `*.ht`). You can reuse this mapping for any character. For example, you want to put the Avatar mapping under source control and you prefer to commit text-based files; or perhaps you want to parse the file with your own custom tool.

To save the Avatar data in a **Human Template**A pre-defined bone-mapping. Used for matching bones from FBX files to the Avatar. [More info](class-HumanTemplate.html)  
See in [Glossary](Glossary.html#Humantemplate) file, choose **Save** from the **Mapping** drop-down menu at the bottom of the **Avatar** window.

![The Mapping drop-down menu at the bottom of the Avatar window](../uploads/Main/MecanimMappingMenus.png)


The **Mapping** drop-down menu at the bottom of the **Avatar** window

Unity displays a dialog for you to choose the name and location of the file to save.

To load a Human Template file previously created, choose **Mapping** > **Load** and select the file you want to load.

## Using Avatar Masks

Sometimes it is useful to restrict an animation to specific body parts. For example, an walking animation might involve the character swaying their arms, but if they pick up a torch, they should hold it up to cast light. You can use an **Avatar Body Mask** to specify which parts of a character an animation should be restricted to. See documentation on [Avatar Masks](class-AvatarMask.html)A specification for which body parts to include or exclude for an animation rig. Used in Animation Layers and in the importer. [More info](class-AvatarMask.html)  
See in [Glossary](Glossary.html#AvatarMask) for further details.

Avatar

Scripting Root Motion

Avatar Muscle & Settings tab reference

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)