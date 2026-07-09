* [Assets and media](assets-and-media.html)
* [Caching assets](importing-caching-assets.html)
* Install Unity Accelerator with Docker Hub

Unity Accelerator downloads

Verify the Unity Accelerator version

# Install Unity Accelerator with Docker Hub

You can use Docker Hub to install Unity **Accelerator**The Unity Accelerator is an external tool that provides an asset cache that keeps copies of a team’s imported assets. The goal of the Accelerator is to speed up teamwork and reduce iteration time by coordinating asset sharing so that you don’t need to reimport portions of your project. [More info](UnityAccelerator.html)  
See in [Glossary](Glossary.html#Accelerator) with the following link: <https://hub.docker.com/r/unity/accelerator>

## Set up persistent storage

To host Unity Accelerator’s configuration and cache, you must set up a persistent storage area. To set this up, use one or more of the following variables when running the container for the first time. The variables are only used if the startup doesn’t find a configuration file so it’s safe to run with them on successive runs.

| **Variable** | **Description** |
| --- | --- |
| `DISABLE_USAGE_STATS` | Set to true to disable usage stats. Leaving usage stats enabled can help improve Unity Accelerator’s features and performance by giving Unity feedback. |
| `USER` | The username for the local built-in dashboard. |
| `PASSWORD` | The password for the local built-in dashboard. |
| `CERT_HOSTNAME` | The host name to use for TLS support. This is used for redirects and goes along with `CERT_PEM` and `KEY_PEM` below. |
| `CERT_PEM` | The path to a cert.pem to use for TLS support. If you set `CERT_HOSTNAME` but don’t set `CERT_PEM`, `<persist_dir>/cert.pem` will be assumed. |
| `KEY_PEM` | The path to a key.pem to use for TLS support. If you set `CERT_HOSTNAME` but don’t set `KEY_PEM`, `<persist_dir>/key.pem` will be assumed. |

### Configure security and TLS

To configure TLS settings, ensure the cert.pem and key.pem is in the /agent path specified and then include a `CERT_HOSTNAME` like the following:

```
$ docker run --rm -ti -v "${PWD}/agent:/agent" -e 'CERT_HOSTNAME=myhostname.com' -e unity/accelerator:latest
```

### Subsequent execution

You can also set any environment variables for the cache server. Use `unity-accelerator --all-help` and look for options that indicate `Default: $SOME_VARIABLE`. There are two that the container sets if you don’t:

| **Variable** | **Description** |
| --- | --- |
| `UNITY_ACCELERATOR_PERSIST` | Container default is /agent. This is the directory where unity-accelerator.cfg resides as well as other persisted data (`cachedir` possibly being different). |
| `UNITY_ACCELERATOR_LOG_STDOUT` | Container default is true. When true, outputs logs to `stdout` only. When false, writes logs to the persist directory. |

## Run the container

Unity’s Docker images are signed, so it’s best practice to [enable Docker Content Trust](https://docs.docker.com/engine/security/trust/):

```
$ export DOCKER_CONTENT_TRUST=1
```

You can run Unity Accelerator with the following:

```
$ docker run -p 80:80 -p 443:443 -p 10080:10080 -v "${PWD}/agent:/agent" unity/accelerator:latest
```

However, If you want to choose a different location for where Unity Accelerator stores the configuration and cached artifacts, you can choose to provide additional environment variable configuration values like this:

```
$ docker run -p 80:80 -p 443:443 -p 10080:10080 -v "${PWD}/agent:/mnt/another_spot" -e "UNITY_ACCELERATOR_PERSIST=/mnt/another_spot" -e "UNITY_ACCELERATOR_DEBUG=true" unity/accelerator:latest
```

To set a username and password for local dashboard, you can use `USER` and `PASSWORD` environment variables:

```
$ docker run -p 80:80 --env PASSWORD=[PASSWORD] --env USER=[USERNAME] unity/accelerator:latest
```

### Exposed ports

The following are the default values for ports used by Unity Accelerator:

* 80
* 443
* 10080
* 10443

## Additional resources

* [Unity Accelerator requirements](accelerator-requirements.html)
* [Verify the Unity Accelerator version](accelerator-verify-version.html)
* [Configure an accelerator in the Editor](accelerator-configure.html)

Unity Accelerator downloads

Verify the Unity Accelerator version

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)