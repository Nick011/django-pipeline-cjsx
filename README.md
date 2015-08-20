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
```

