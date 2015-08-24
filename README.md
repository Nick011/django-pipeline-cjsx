# django-pipeline-cjsx
A django pipeline compiler to transform React in Coffeescript and Browserify

## Requirements
- Browserify
- coffee-reactify

## Install
```
pip install django-pipeline-cjsx
```

## Usage
```
PIPELINE_COMPILERS = (
  'pipeline_cjsx.compiler.CJSXCompiler',
)

PIPELINE_JS = {
  'app': {
    'source_filenames': (
      'coffee/app.cjsx',
    ),
    'output_filename': 'app.min.js',
  }
}

PIPELINE_BROWSERIFY_BINARY = 'node ' + 'PATH_TO/node_modules/browserify/bin/cmd.js')
```
## EMFILE Error on OSx

If you get an `EMFILE` error.  ie: `Error: EMFILE, open 'FILENAME'`
Add the following line to your `.bash_profile`

```
# Work around bug in browserify
ulimit -n 2560
```
