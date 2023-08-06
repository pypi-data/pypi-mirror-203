# Classify AWSets JSON by Region

[![Test](https://github.com/yukihiko-shinoda/classify-awsets-json-by-region/workflows/Test/badge.svg)](https://github.com/yukihiko-shinoda/classify-awsets-json-by-region/actions?query=workflow%3ATest)
[![Test Coverage](https://api.codeclimate.com/v1/badges/d3006b43fedc1ffd5db7/test_coverage)](https://codeclimate.com/github/yukihiko-shinoda/classify-awsets-json-by-region/test_coverage)
[![Maintainability](https://api.codeclimate.com/v1/badges/d3006b43fedc1ffd5db7/maintainability)](https://codeclimate.com/github/yukihiko-shinoda/classify-awsets-json-by-region/maintainability)
[![Code Climate technical debt](https://img.shields.io/codeclimate/tech-debt/yukihiko-shinoda/classify-awsets-json-by-region)](https://codeclimate.com/github/yukihiko-shinoda/classify-awsets-json-by-region)
[![Python versions](https://img.shields.io/pypi/pyversions/classifyawsetsjsonbyregion.svg)](https://pypi.org/project/classifyawsetsjsonbyregion)
[![Twitter URL](https://img.shields.io/twitter/url?style=social&url=https%3A%2F%2Fgithub.com%2Fyukihiko-shinoda%2Fclassify-awsets-json-by-region)](http://twitter.com/share?text=Classify%20AWSets%20JSON%20by%20Region&url=https://pypi.org/project/classifyawsetsjsonbyregion/&hashtags=python)

Classifies AWSets JSON by AWS region.

## Advantage

- Output the list of AWS resources as CSV files classified by AWS region
- Enable filter to exclude AWS resources not in question

### Output the list of AWS resources as CSV files classified by AWS region

You can check the states of AWS resources by AWS region. It's also useful to compare the states of AWS resources between AWS regions by using text diff tools like [Visual Studio Code].

### Enable filter to exclude AWS resources not in question

You can exclude AWS resources not in question by using `config.yml`. It's useful to reduce the number of AWS resources to be checked, such like the one AWS created by default. You can focus on AWS resources in question.

## Quickstart

1.\
Install `classifyawsetsjsonbyregion` with pip:

```console
pip install classifyawsetsjsonbyregion
```

2.\
Create following directories:

- `input`
- `output`
- `intermediate`

3.\
Put AWSets JSON files in it and rename it as `awsets.json`:

```plaintext
your_working_directory/
+---input/
    +---awsets.json
+---intermediate/
+---output/
```

4.\
Run `classify-awsets-json-by-region`:

```console
classify-awsets-json-by-region
```

<!-- markdownlint-disable no-trailing-punctuation -->
## How do I...
<!-- markdownlint-enable no-trailing-punctuation -->

<!-- markdownlint-disable no-trailing-punctuation -->
### Use intermediate directory for?
<!-- markdownlint-enable no-trailing-punctuation -->

This directory is for intermediate files. These files are useful for debugging. The contents of these files are the classifying result of AWSets JSON before filtering AWS resources. Note that the file for excluded AWS regions is not created.

## Credits

This package was created with [Cookiecutter] and the [yukihiko-shinoda/cookiecutter-pypackage] project template.

[Cookiecutter]: https://github.com/audreyr/cookiecutter
[Visual Studio Code]: https://code.visualstudio.com/
[yukihiko-shinoda/cookiecutter-pypackage]: https://github.com/audreyr/cookiecutter-pypackage
