cwlVersion: v1.2
$graph:{% for clt in clt_ids %}
- class: CommandLineTool
  id: {{clt}}
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
      dockerPull: <registry>/<image-prefix>/{{clt}}:0.0.1
  baseCommand: []
  arguments: []
  inputs: []
  outputs: []{% endfor %}
