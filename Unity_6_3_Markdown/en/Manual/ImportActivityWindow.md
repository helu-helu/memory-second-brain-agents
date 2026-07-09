* [Assets and media](assets-and-media.html)
* [Importing assets](import-assets.html)
* [Analyze the import process](import-analyze.html)
* Import Activity window introduction

Check the consistency of the import process

Import Activity window reference

# Import Activity window introduction

The Import Activity window provides you with information about what happens when Unity imports your assets. You can use this information to identify the assets in your project that Unity recently imported, how long each asset took to import, and why Unity imported it. This information can inform decisions about how to improve the time Unity takes to import your assets, or how to avoid unnecessary imports altogether.

## Open the Import Activity window

To open the Import Activity window:

* Go to **Window** > **Analysis** > **Import Activity**.

You can also open the Import Activity window directly from an asset, which causes the window to immediately display the import details for the selected asset. To open the window from an asset choose from the following options:

* Right-click an asset in the **Project window**A window that shows the contents of your `Assets` folder (Project tab) [More info](ProjectView.html)  
  See in [Glossary](Glossary.html#Projectwindow) and select **View in Import Activity Window**.
* Select an asset, and right-click its **Inspector**A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
  See in [Glossary](Glossary.html#Inspector)’s tab. From the context menu, select **Open in Import Activity Window**.

![The Import Activity window with an asset selected.](../uploads/Main/import-activity-window.png)


The Import Activity window with an asset selected.

## Analyze import data

The Import Activity window contains various options to investigate the import timings of the assets within your project. For more information about the options available, refer to [Import Activity window reference](import-activity-window-reference.html).

## Overview of import data

Select the **Show Overview** option in the **toolbar**A row of buttons and basic controls at the top of the Unity Editor that allows you to interact with the Editor in various ways (e.g. scaling, translation). [More info](Toolbar.html)  
See in [Glossary](Glossary.html#toolbar) to get an overview of the most impactful assets in your project. The Import Activity Overview panel displays a list of assets with the most dependencies and longest import duration. It’s useful to identify which assets might slow down the import process of your project. Assets with more dependencies are more likely to be regularly re-imported, because an asset is re-imported whenever any of its dependencies are modified.

![The Import Activity Overview panel displaying the most dependencies, longest import duration, and suggestions to improve import times.](../uploads/Main/import-activity-window-overview.png)


The Import Activity Overview panel displaying the most dependencies, longest import duration, and suggestions to improve import times.

You can select **Analyze Import Process** to get a list of issues with the importing process and ways to fix the warnings.

## Investigate previous import instances of an asset

To view the import history of an asset, enable the [Show previous imports](import-activity-window-reference.html#toolbar) option. In a separate panel, Unity then displays the number of revisions of the asset that are stored in the `Library` folder. The list is cleared when you restart the Unity Editor and artifact garbage collection runs.

If you want to keep import results from previous Editor sessions to aid with debugging or analysis, disable artifact garbage collection. To do this:

1. Open the **Project Settings** window (**Edit** > **Project Settings**).
2. Select **Editor** and under the **Asset Pipeline** settings, disable the **Remove unused Artifacts on Restart** setting.

You can also control this setting with [`EditorUserSettings.artifactGarbageCollection`](../ScriptReference/EditorUserSettings.artifactGarbageCollection.html).

## Additional resources

* [Import Activity window reference](import-activity-window-reference.html)
* [Introduction to importing assets](ImportingAssets.html)
* [Asset metadata](AssetMetadata.html)

Check the consistency of the import process

Import Activity window reference

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)