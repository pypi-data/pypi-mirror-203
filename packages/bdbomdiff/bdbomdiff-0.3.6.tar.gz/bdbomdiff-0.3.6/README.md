# BDBOMDIFF

Blackduck BOM Diff to excel for AOSD import

## Description

This is intended for finding new OSS component to be imported into AOSD

## Getting Started

### Dependencies

- Blackduck
- importlib-resources
- openpyxl

### Installing

- pip install bdbomdiff

### Executing program

- How to run the program

```
<!-- on the folder it is running place this blackduck config file for blackduck library-->
.restconfig.json
{
    <!-- make sure Blackduck_url should not end with slash -->
  "baseurl": "Blackduck_url",
  "api_token": "API_KEY",
  "insecure": true,
  "debug": false
}

bdbomdiff PROJECT_NAME NEW_VERSION OLD_VERSION -o OUTPUT_DIR

```

## Help

Any advise for common problems or issues.

```
>bdbomdiff -h
usage: Retreive BOM component info for the given project and version [-h] -o O [-l LIMIT | -u | -r] [-v] [-c] project_name version oldversion

positional arguments:
  project_name
  version
  oldversion

options:
  -h, --help            show this help message and exit
  -o O                  Output directory
  -l LIMIT, --limit LIMIT
                        Set limit on number of components to retrieve
  -u, --unreviewed
  -r, --reviewed
  -v, --vulnerabilities
                        Get the vulnerability info for each of the components
  -c, --custom_fields   Get the custom field info for each of the components
```

## Authors

Dinesh Ravi

## Version History

- 0.3.0
  - get license, homepage url, description, copyright and files info,
- 0.2.0
  - Documentation update
- 0.1.0
  - Initial Release

## License

This project is licensed under the MIT License - see the [MIT](LICENSE) file for details

## Acknowledgments

- [openpyxl](https://pypi.org/project/openpyxl/)
- [Blackduck](https://pypi.org/project/blackduck/)
- [importlib-resources](https://pypi.org/project/importlib-resources/)
