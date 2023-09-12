# **OSCAL CONTENT VALIDATOR**

 Validation of any OSCAL content instance can be accomplished by applying the appropriate schema for the respective format. For example, a System Security Plan (SSP) represented in OSCAL XML can be validated against the SSP XML Schema, which defines (in machinable form) the validation rules for OSCAL SSPs in XML. Validation operations are based entirely on non-proprietary, standardized processes available in multiple tool implementations, by reference to open, publicly available schemas, located in the OSCAL repository for XML and JSON/YAML respectively.

YAML developers should take note that the JSON Schemas can be applied to YAML content instances.

The validator is from NIST OSCAL tool set available at https://github.com/usnistgov/OSCAL/tree/main/src/utils

## 
**Objective**

Validation of OSCAL content to help confirm its correctness and fitness for processing.

##
**About OSCAL Utilities**

The OSCAL project maintains [a list of tools for OSCAL on their web site](https://pages.nist.gov/OSCAL/tools/ "OSCAL tools page").

Additionally, OSCAL Project from NIST also maintain a github repository of tools at https://github.com/usnistgov/oscal-tools.

Functionality archived tools from OSCAL project include:

`oscal-content-validator.py` - a Python shell for configuration and running (XML and JSON )schema validation. We are using this for our project to validate the OSCAL content.

## 
**Scope**

[What is in and out of scope]


## 
**Prior Work**



*   [List of prior and/or related projects](https://github.com/usnistgov/OSCAL)

