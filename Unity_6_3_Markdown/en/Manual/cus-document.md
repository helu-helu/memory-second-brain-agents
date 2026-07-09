* [Packages and package management](PackagesList.html)
* [Package creation](cus-pkg-lp.html)
* [Package development](cus-pkg-development.html)
* Document your package

Add required legal files to your package

Export and sign your UPM package

# Document your package

Document your package to help users have the best experience and optimize its use.

When you [create your package](cus-create.html) with the Package Manager window, the Unity Editor creates a `Documentation` folder in your package’s base folder. This folder contains one file in the [Markdown](https://www.markdownguide.org/basic-syntax/) format, whose lightweight syntax is used on many platforms, such as GitHub and Bitbucket. This provided Markdown file contains placeholder content and instructions to help you create the first draft of your documentation set.

As long as you have Markdown content in your package’s `Documentation` folder, the layout you choose is freeform and flexible. You can write your documentation in the single file provided or you can create a more complex structure across multiple files. You can even create the documentation in HTML and host it on your own website.

After users install your package, they can access its documentation using the **Documentation** link in the [details panel](upm-ui-details.html) of Unity’s Package Manager window. Selecting the link attempts to open the documentation based on a property set in the **package manifest**Each package has a *manifest*, which provides information about the package to the Package Manager. The manifest contains information such as the name of the package, its version, a description for users, dependencies on other packages (if any), and other details. [More info](upm-manifestPkg.html)  
See in [Glossary](Glossary.html#packagemanifest) file. If your documentation isn’t hosted externally, users can right-click the **Documentation** link to view the local version of the documentation in your package’s `Documentation` folder.

To document your package:

1. Go to the `Documentation` folder in your package’s base folder.
2. Open the Markdown file in your preferred script editor.
3. Follow the embedded instructions in the file, replacing placeholder content with your own. Optionally format the information using Markdown. The recommended sections are:

   * **About**: A brief, high-level explanation of the package.
   * **Installing**: You can point to the official [Package Manager installation instructions](https://docs.unity3d.com/Manual/upm-ui-install.html), but if you have any special installation requirements, such as installing samples, add them here.
   * **Requirements**: This is a good place to add hardware or software requirements, including which versions of the Unity Editor this package is compatible with.
   * **Usage:** Information that explains how to use your package. Exact usage content varies depending on the type of package. However, usage content can include things like procedures, reference information that explains properties and settings, and more.
   * **Known limitations**: If this version of your package has any nontrivial limitations, list them here.
   * **Package contents**: Include the location of important files you want the user to know about. For example, if this is a sample package containing textures, models, and materials separated by sample group, you might want to specify the folder location of each group.
   * **Document revision history**: Track when you create and update the documentation. Consider a table with date and description columns.
4. Save the file.
5. (Optional) If you want to host the documentation on your own website, convert the Markdown to HTML, then [edit the package manifest](cus-edit-manifest.html#edit-manifest) by setting the `documentationUrl` property. Set its value to the URL where you will host the documentation.

As your package evolves, consider adding more sections to your documentation. The following sections are only suggestions, but represent the types of content that quality documentation might contain.

| **Section** | **Description** |
| --- | --- |
| **Workflows** | Include a list of steps the user can follow that demonstrates how to use the feature. You can include screenshots to help describe how to use the feature. |
| **Advanced topics** | Detailed information about what you’re providing to users. This is ideal if you don’t want to overwhelm the user with too much information up front. |
| **Reference** | If you have a user interface with a lot of properties, you can describe their details in a reference section. Using tables is a good way to offer specific property descriptions. |
| **Samples** | For packages that include sample files, you can include detailed information on how the user can use these sample files in their projects and **scenes**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html) See in [Glossary](Glossary.html#Scene). |
| **Tutorials** | If you want to offer walk-throughs for complicated procedures, you can also add them here. Use step-by-step instructions and include images if they can help the user understand. |
| **Feedback and support** | Offer links for getting help and providing feedback, including public forums or knowledge bases, and support contacts. |

Explore the package documentation for Unity’s own [released packages](pack-safe.html) for ideas and inspiration.

## Before you share your package

There’s typically no need for developers who install your package to import its documentation files into a project. The recommended best practice is for you to use the **Project** window to rename the `Documentation` folder in your package to `Documentation~` before you [export](cus-export.html) or [share](cus-share.html) your package. The renamed folder disappears from the Editor but still exists on disk. The tilde (`~`) ensures that the documentation isn’t added directly to the project. Developers using your package can view your documentation from the **Documentation** link in the Package Manager window.

**Important**: Use the **Project** window to rename the folder, rather than using your file management application to directly rename the folder on disk.

## Additional resources

* [Package development workflow](CustomPackages.html)
* [Markdown syntax guide](https://confluence.atlassian.com/bitbucketserver/markdown-syntax-guide-776639995.html) (Bitbucket)
* [Finding package documentation](upm-docs.html)

Add required legal files to your package

Export and sign your UPM package

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)