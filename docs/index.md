# Rationale

This small tool is developed to satisfy the [Project structure contract](https://github.com/eoap/eoap-cwl-release-workflow/blob/main/docs/project-structure-contract.md) conventions, bootstrapping a new project, generating all the required stuff to meet the requirements.

## Installation

```console
pip install cwl-cli-archetype
```

## Execution

```console
cwl-cli-archetype \
--clt-id tool_1 \
--clt-id tool_2 \
--clt-id tool_3 \
--target-dir ./a/b/c
```

The `./a/b/c` target dir will be composed as:

```console
$ tree a
a
└── b
    └── c
        ├── cwl-workflow
        │   └── clts.cwl
        ├── tool_1
        │   └── Dockerfile
        ├── tool_2
        │   └── Dockerfile
        └── tool_3
            └── Dockerfile

6 directories, 4 files
```

The `./a/b/c/cwl-workflow/clts.cwl` file will include:

```yaml
cwlVersion: v1.2
$graph:
- class: CommandLineTool
  id: sim13pods
  requirements:
      InlineJavascriptRequirement: {}
      EnvVarRequirement:
        envDef:
          PATH: /app/envs/runner/bin
      ResourceRequirement:
        coresMax: 1
        ramMax: 512
  hints:
    DockerRequirement:
      dockerPull: <registry>/<image-prefix>/tool_1:0.0.1
  baseCommand: []
  arguments: []
  inputs: []
  outputs: []
- class: CommandLineTool
  id: fbrito
  requirements:
      InlineJavascriptRequirement: {}
      EnvVarRequirement:
        envDef:
          PATH: /app/envs/runner/bin
      ResourceRequirement:
        coresMax: 1
        ramMax: 512
  hints:
    DockerRequirement:
      dockerPull: <registry>/<image-prefix>/tool_2:0.0.1
  baseCommand: []
  arguments: []
  inputs: []
  outputs: []
- class: CommandLineTool
  id: lmizzoni
  requirements:
      InlineJavascriptRequirement: {}
      EnvVarRequirement:
        envDef:
          PATH: /app/envs/runner/bin
      ResourceRequirement:
        coresMax: 1
        ramMax: 512
  hints:
    DockerRequirement:
      dockerPull: <registry>/<image-prefix>/tool_3:0.0.1
  baseCommand: []
  arguments: []
  inputs: []
  outputs: []
```
