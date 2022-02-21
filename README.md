
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

This repository is an implementation of the PersistVulnz agent.

## Getting Started
To perform your first scan, simply run the following command.
```shell
ostorlab scan run --install --agents agent/ostorlab/local_persist_vulnz ip 8.8.8.8
```

This command will download and install `agent/ostorlab/local_persist_vulnz` and target the ip `8.8.8.8`.
For more information, please refer to the [Ostorlab Documentation](https://github.com/Ostorlab/ostorlab/blob/main/README.md)


## Usage

Agent PersistVulnz can be installed directly from the ostorlab agent store or built from this repository.

 ### Install directly from ostorlab agent store

 ```shell
 ostorlab agent install agent/ostorlab/local_persist_vulnz
 ```

You can then run the agent with the following command:
```shell
ostorlab scan run --agents agent/ostorlab/local_persist_vulnz ip 8.8.8.8
```


### Build directly from the repository

 1. To build the persist_vulnz agent you need to have [ostorlab](https://pypi.org/project/ostorlab/) installed in your machine. If you have already installed ostorlab, you can skip this step.

```shell
pip3 install ostorlab
```

 2. Clone this repository.

```shell
git clone https://github.com/Ostorlab/agent_persist_vulnz.git && cd agent_persist_vulnz
```

 3. Build the agent image using ostorlab cli.

 ```shell
 ostortlab agent build --file=ostorlab.yaml
 ```
 You can pass the optional flag `--organization` to specify your organisation. The organization is empty by default.

 4. Run the agent using one of the following commands:
	 * If you did not specify an organization when building the image:
      ```shell
      ostorlab scan run --agents agent//local_persist_vulnz ip 8.8.8.8
      ```
	 * If you specified an organization when building the image:
      ```shell
      ostorlab scan run --agents agent/[ORGANIZATION]/local_persist_vulnz ip 8.8.8.8
      ```


## License
[Apache](./LICENSE)
