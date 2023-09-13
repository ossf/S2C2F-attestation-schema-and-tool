# **Ajv OSCAL CONTENT VALIDATOR for JSON**

Validation of any OSCAL content instance can be accomplished by applying the appropriate schema for the respective format. For example, a Catalog Model represented in OSCALJSON can be validated against the OSCAL Catalog JSON Schema , which defines (in machinable form) the validation rules for OSCAL Catalog in JSON. Validation operations are based entirely on non-proprietary, standardized processes available in multiple tool implementations, by reference to open, publicly available schemas, located in the OSCAL repository for XML and JSON/YAML respectively.

Ajv[https://ajv.js.org/guide/getting-started.html] was designed at the time when there were no validators fully complying with JSON Schema specification, aiming to achieve the best possibly validation performance via just-in-time compilation of JSON schemas to code. Ajv achieved both speed and rigour,

The reference schemas against which we can validate the content are located at https://github.com/usnistgov/OSCAL/blob/128-integrate-profile-checker-schematron/json/schema/oscal_catalog_schema.json

## **Objective**

Validation of OSCAL content to help confirm its correctness and fitness for processing.

## **Pre-requirements for validator tool**

1. Install Ajv using npm
  ** _npm install -g ajv-formats ajv-cli_**
3. Reference OSCAL validation criteria -  *validating* goes beyond parsing: it tells you not only that a file can be read successfully, but also that its data structures conform to rules for a particular application of XML, JSON, or YAML. [Well-formed JSON, XML, or YAML is not necessarily valid OSCAL JSON, XML, or YAML](https://pages.nist.gov/OSCAL/concepts/layer/validation/).
4. JSON Schema for reference -  Normative schemas suitable for validating the various OSCAL models are available in the project's source code repository [for JSON and YAML](https://github.com/usnistgov/OSCAL/tree/main/json/schema).
5. Refer to github repo for OSCAL model datatypes to ensure that model has correct data types- https://github.com/usnistgov/metaschema/blob/develop/schema/json/metaschema-datatypes.json

## How do I apply a schema to a document to determine validity?

Schemas are built using standard schema languages that are supported by commodity tools. These tools can all apply the same schemas to the same documents, and give the same results.
For OSCAL JSON, the schema syntax is [JSON Schema](https://json-schema.org/). Ideally, all the models must adhere to this schema syntax.

**_ajv-cli validate -s oscal-schema.json -d oscal.json -c ajv-formats_**

Output
**_oscal.json valid_**

**What does success look like?**

As for OSCAL JSON, the results from validation with AJV will look like this:
```
# Install the ajv-formats library in NodeJS runtime to avoid runtime errors.
npm install -g ajv-formats ajv-cli
ajv-cli validate -s oscal-schema.json -d oscal.json -c ajv-formats
oscal.json valid
```

** What does an error look like?**

**Well-formed, but not valid**

```
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

**Not even well-formed**

It can happen, however, that the file is not even legible to the processor ("parser"), because it is not well-formed to the syntax rules.

In such a case, XML Lint signals trouble like this:

```
test-invalid-profile.xml:10: parser error : Opening and ending tag mismatch: profile line 2 and metadata
  </metadata>
             ^
test-invalid-profile.xml:11: parser error : Extra content at the end of the document
  <merge>
  ^
```

In this case the processor reports the syntax issues it detects, to the extent possible, for a document that is not well-formed. The processor will be unable to complete validation of the document because it is not well-formed.

**What can you learn from errors?**

A validation error tells you, first and foremost, that your file is incorrect in a basic way. For example, an element (data structure) may be out of place, or missing a required piece. Tools that fail to implement schema validation, misconfigured tools, data quality issues, workflow issues, or many other causes may be the cause. They also vary in how easy they are to correct. The most common problem is that the wrong schema is being used.

The most important consideration in correcting a validation error is selecting the appropriate schema and the appropriate version of that schema. OSCAL maintains backward compatibility across all schemas as expressed through [the use of semantic versioning](https://github.com/usnistgov/OSCAL/blob/main/docs/content/downloads/_index.md#oscal-releases).

A *well-formedness error*, however, tells you your file is incorrect in a more fundamental way. It is both more severe (further processing cannot continue) but also easier to address by using tools correctly. In a mature system, well-formedness errors should be rare, and when they do occur it is because preliminary checks for well-formedness were not implemented or ignored.

**How can I correct my errors?**

End users will ordinarily find it easiest and best to edit a file in an OSCAL tool with a graphical user interface or a structured editor. These would be tools that are especially built or configured to support changing the file while respecting the rulesof well-formedness and validating against the rules of an intended schema.

In order to build such tools and support other operations, developers may also do this work. Commercial off-the-shelf developer environments may support these basic operations for a range of formats.

Finally, XML and JSON are both based on the conventions of *plain-text* (UTF-8 in the case of JSON; any encoding your processor supports in the case of XML). As such, they can be edited in any text editor.

You should validate OSCAL documents saved to files to ensure it will work for the next operation.

**What does validation *not* tell me?**

The rules expressed and enforced by a schema are limited to those that can be systematically checked by automated processes. Valid OSCAL documents are *not necessarily* "correct" with respect to the information they represent. For OSCAL, validation is an objective determination by a program, whereas "correct" remains a subjective determination based on analysis by a person. Validation ensures only that *your data is fit for further processing*; such processing can include operations to determine the data's correctness, completeness, adequacy, veracity, or anything else not defined or definable by a schema. 


 **Other ways to validate?**

The provided schemas are machine-generated and tested to reflect and enforce the rules of OSCAL, but they are not the only way to validate. Alternative schema technologies and schema "emulators" are conceivable and sometimes useful. Refer to the [the Metaschema repository](https://github.com/usnistgov/metaschema/) for more details on the Metaschema technology from which our schemas derive, and which can be used as a basis for alternative strategies and approaches to document validation.
