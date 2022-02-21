
<h1 align="center">Agent PersistVulnz</h1>

<p align="center">
<img src="https://img.shields.io/badge/License-Apache_2.0-brightgreen.svg">
<img src="https://img.shields.io/github/languages/top/ostorlab/agent_persist_vulnz">
<img src="https://img.shields.io/github/stars/ostorlab/agent_persist_vulnz">
<img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg">
</p>

_PersistVulnz locally persists vulnerabilities discovered after a scan is run._

---

<p align="center">
<img src="" alt="agent_persist_vulnz" />
</p>

This repository is an implementation of the default persist vulnz agent. Persist Vulnz is a default agent needed to run a scan using the local runtime.

## Usage

Agent Persist Vulnz can be installed directly from the ostorlab agent store or built from this repository.

 ### Install directly from ostorlab agent store

 ```shell
 ostorlab agent install agent/ostorlab/local_persist_vulnz
 ```
The agent will be automatically installed and updated by simply passing `--install` flag:

```shell
ostorlab scan run --install --agents agent/ostorlab/tsunami ip 8.8.8.8
```

## License
[Apache](./LICENSE)
