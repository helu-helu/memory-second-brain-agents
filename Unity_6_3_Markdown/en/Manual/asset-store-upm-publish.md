* [Assets and media](assets-and-media.html)
* [Unity Asset Store](AssetStore.html)
* [Publishing Asset Store packages](asset-store-publishing.html)
* [Publish a UPM package on the Asset Store](asset-store-upm.html)
* UPM package Asset Store publishing workflow

Publish a UPM package on the Asset Store

Enroll as a UPM publisher on the Publisher Portal

# UPM package Asset Store publishing workflow

**Note**: Paid **UPM packages**A **Package** managed by the **Unity Package Manager**. Refer to **Packages**.  
See in [Glossary](Glossary.html#UPMpackage) are not yet available on the Publisher Portal. You can publish free UPM packages.

You can create a [Unity Package Manager (UPM) package](upm-package-types.md) from assets that you own and make it available to download on the [Unity Asset Store](https://assetstore.unity.com/). Manage UPM packages through the UPM publishing portal, which is different from the [asset package publishing workflow](asset-store-workflow.html).

**Important:** An **Asset Store**A growing library of free and commercial assets created by Unity and members of the community. Offers a wide variety of assets, from textures, models and animations to whole project examples, tutorials and Editor extensions. [More info](AssetStore.html)  
See in [Glossary](Glossary.html#AssetStore) package must be compliant with [Unity Core Standards](https://unity.com/core-standards) and therefore meet certain requirements. For more information, refer to the [Asset Store Provider Agreement](https://unity.com/legal/provider) and the [Submission Guidelines](https://unity3d.com/asset-store/sell-assets/submission-guidelines).

## UPM package and products

The UPM publishing workflow introduces the concept of a product. A product is different from a package in the following ways:

* A product is a container that can include one or more UPM packages.
* Customers can get a product from the Asset Store.
* A package stores **scripts**A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](creating-scripts.html)  
  See in [Glossary](Glossary.html#Scripts), features, and assets for Unity, including Editor or Runtime tools and libraries, asset collections, and project templates.

Create a [product draft](asset-store-upm-create-draft.html) in the Publisher Portal to manage and configure the structure of your packages. A product can contain one or multiple packages. For more information, refer to [Create a Publisher Portal package draft](asset-store-upm-create-draft.html).

## UPM package namespaces

UPM packages require consistent namespaces. The following table shows each of the namespaces you need to set for the different stages of the UPM publishing workflow:

| **UPM workflow step** | **Namespace action** | **Description** |
| --- | --- | --- |
| **Sign up to the UPM workflow** | Set a publisher namespace. | Establish and claim a namespace for your packages during the enrollment process. |
| **Create a UPM product draft for a single package** | Set a product namespace. | Assign a product namespace. The product namespace becomes part of the technical name. |
| **Create a UPM product draft for multiple packages** | Set a product namespace and a package namespace for each package. | Assign a package namespace for each package you add. The package namespace becomes part of the technical name. |
| **Create and validate UPM packages** | Set the UPM package folder and `package.json` namespaces in the `name` field. | The UPM package folder and the `package.json` name must match the package’s technical name. |
| **Upload UPM packages** | The Asset Store Publishing Tools checks and matches the package technical name to the one set on the Publisher Portal. | If the publisher space doesn’t match the product namespace, a button appears that you can select to create a new ID. If the technical name doesn’t match the product namespace, a button appears that you can select to create a new product draft. |

For more information about setting namespaces, refer to [Create a Publisher Portal package draft](asset-store-upm-create-draft.html).

## Prerequisites

To publish assets to the UPM publishing portal, you must first create the following:

1. [Create a Unity ID](https://id.unity.com/account/new).
2. [Set up an Asset Store publisher profile](AssetStoreCreateAcct.html).
3. [Enroll as a UPM publisher on the Publisher Portal](asset-store-upm-apply.html)
4. [Enroll as a UPM publisher on the Publisher Portal](asset-store-upm-apply.html).

## Publish a UPM package to the Asset Store

To publish a UPM package to the Asset Store, you need to enroll on the Publisher Portal. To learn more, refer to [UPM Publishing on the Asset Store](https://assetstore.unity.com/publishing/upm-publishing).

To create and publish a UPM package, perform the following steps:

1. [Create a product draft](asset-store-upm-create-draft.html).
2. [Validate and upload your package](asset-store-upm-validate.html).
3. [Submit the package for approval](asset-store-upm-submit.html).

You can then [check the status of the package](asset-store-upm-check-status.html), and once published, you can make [further updates in the Publisher Portal](asset-store-upm-update.html).

## Additional resources

* [Enroll as a UPM publisher on the Publisher Portal](asset-store-upm-apply.html)
* [Create a Publisher Portal product draft](asset-store-upm-create-draft.html)
* [Managing your organization](https://docs.unity.com/en-us/cloud/organizations)
* [Asset Store packages](AssetStorePackages.html)A bundled collection of assets or tools available for purchase or download on the Unity Asset Store, compressed and stored as an asset package (`.unitypackage` extension) or a UPM package. You can manage your packages from the Asset Store either on the online store or through the Package Manager window. [More info](AssetStorePackages.html)  
  See in [Glossary](Glossary.html#AssetStorepackage)

Publish a UPM package on the Asset Store

Enroll as a UPM publisher on the Publisher Portal

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)