#**Command to Install and Run Ajv validator**

Here the validation of the Catalog JSON (oscal.json) has failed

```

npm install -g ajv-formats ajv-cli


ajv-cli validate -s oscal-schema.json -d oscal.json -c ajv-formats
oscal_json.json invalid
[
  {
    instancePath: '/catalog',
    schemaPath: '#/additionalProperties',
    keyword: 'additionalProperties',
    params: { additionalProperty: '_xmlns:xsi' },
    message: 'must NOT have additional properties'
  }
]

```

**Successful Validation**

```
ajv-cli validate -s oscal-schema.json -d oscal.json -c ajv-formats
oscal_json.json invalid
```

**Pre-req**
Save OSCAL Schema JSON and project JSON that needs validation in the same location/project folder in the repo.
