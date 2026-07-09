* [Assets and media](assets-and-media.html)
* [Unity Asset Store](AssetStore.html)
* [Publishing Asset Store packages](asset-store-publishing.html)
* [Publish a UPM package on the Asset Store](asset-store-upm.html)
* Create a Publisher Portal product draft

Enroll as a UPM publisher on the Publisher Portal

Validate and upload a UPM package for the Asset Store

# Create a Publisher Portal product draft

**Note**: Paid **UPM packages**A **Package** managed by the **Unity Package Manager**. Refer to **Packages**.  
See in [Glossary](Glossary.html#UPMpackage) are not yet available on the Publisher Portal. You can publish free UPM packages.

Before you can validate and publish your package, create a product draft in the Publisher Portal.

To access the Publisher Portal for UPM publishing:

1. [Enrol as a UPM publisher](um-asset-store-upm-apply.md).
2. Open the **Asset Store**A growing library of free and commercial assets created by Unity and members of the community. Offers a wide variety of assets, from textures, models and animations to whole project examples, tutorials and Editor extensions. [More info](AssetStore.html)  
   See in [Glossary](Glossary.html#AssetStore), and select your user icon.
3. Under **Switch Organization**, select your publisher organization.

Go to the UPM publishing Publisher Portal through the Cloud Dashboard:
1. Go to the [Cloud Dashboard](https://cloud.unity.com/home/).
1. Select the **Products** tab.
1. In the search bar, enter Publisher Portal.
1. Select **Launch**.

You can configure a product to handle single or multiple packages, as follows:

* **Single package**: Only one package uploaded and linked to this product draft. New versions of the package continuously share the same package technical names. Ideal for a unified tool that supports a wide array of **project settings**A broad collection of settings which allow you to configure how Physics, Audio, Networking, Graphics, Input and many other areas of your project behave. [More info](comp-ManagerGroup.html)  
  See in [Glossary](Glossary.html#ProjectSettings).
* **Multiple packages:** Various packages uploaded and linked to this product draft. The packages can be dependencies, dependents, or packages intended for different project settings or use cases. Ideal for support for multiple use cases, or different project compatibility settings, such as different Unity Editor versions.

You can start with a single package and add more later.

When planning dependencies, use multiple packages if dependencies are only needed within one product. Dependent packages automatically install their dependencies. However, if a dependency is shared across multiple products, list it as its own separate product to avoid conflicts and project breaks. For more information about package dependencies, refer to [Package dependency and resolution](upm-dependencies.html).

The following table compares the properties of each product structure:

| **Property** | **Single package product** | **Multiple package product** |
| --- | --- | --- |
| **Number of packages** | One | Two or more |
| **Compatibility** | Compatible with multiple Unity versions, render pipelines, or build targets. | Optionally, each package can be compatible with a different Unity version, **render pipeline**A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](render-pipelines.html) See in [Glossary](Glossary.html#renderpipeline), or build target. |
| **Version history** | Single version history. | Separate version history for each package. |
| **Support dependency** | No | Yes |
| **Architecture** | Monolithic. All features bundled together. | Can include core and optional packages, and package dependencies. |
| **Dependencies** | Publish a dependency as a single-package product when two or more different products require this dependency. | Publish a dependency as a multi-package product when any package in one product requires this dependency. |

By default the uploaded Unity Editor version is checked for every package uploaded. Additionally, you can list all supported Unity versions that it’s compatible with (major.minor). For build target and render pipeline, setting a specific compatibility is optional.

## Create a product draft

To create a product draft:

1. Open the Publisher Portal.
2. Go to the **Products** tab.
3. Select **Create product**.
4. Enter a product name.

### Product and package naming

When a product has only one package, the product namespace and package namespace are the same, which follows the naming convention of `com.publisher.product`. When a product has multiple packages, the product namespace follows the naming convention of `com.publisher.product` (for example `com.unity.assetstore`), and the package namespaces follow the naming convention of `com.publisher.product.package1` (for example `com.unity.assetstore.tools`).

The following table describes the information each namespace identifies and its format in a complete UPM namespace:

| **Namespace type** | **Description** | **Example** |
| --- | --- | --- |
| **Publisher namespace** | The publisher organization. This namespace uses the reverse domain name notation (reverse-DNS) naming convention. For example, the domain `example.com` has the publisher namespace `com.example`. | `com.publisher` |
| **Product namespace** | The product. This namespace isn’t visible in the product’s Asset Store listing. | `.product` |
| **Package namespace** | The packages that the product contains. Set a package’s namespace only for multi-package products. | * `product.package1` * `product.package2` |
| **[Package technical name](upm-manifestPkg.html#required)** | The package technical name combines the publisher namespace, the product namespace, and for multi-package products, the package namespace. The Package’s technical name must match the following:  * The package folder name. * The `name` field [in the package manifest file](upm-manifestPkg.html). | * **Single package**:   + `com.publisher.product` * **Multiple packages**:   + `com.publisher.product.package1`   + `com.publisher.product.package2` |

**Note:** The publisher namespace (`com.publisher`) is set during enrolment to the development membership program. If you want to know more about changing the namespace, [contact Unity support](https://support.unity.com/hc/en-us/requests/new?ticket_form_id=65905).

## Additional resources

* [Validate and upload a UPM package for the Asset Store](asset-store-upm-validate.html)
* [Submit an UPM package for approval to the Asset Store](asset-store-upm-submit.html)

Enroll as a UPM publisher on the Publisher Portal

Validate and upload a UPM package for the Asset Store

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)