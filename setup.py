from cx_Freeze import setup, Executable

executables = [Executable('mainframe.py')]

excludes = ['logging', 'unittest', 'email', 'html', 'http',
            'xml', 'bz2']

zip_include_packages = ['collections', 'encodings', 'importlib']

options = {
    'build_exe': {
        'include_msvcr': True,

        'zip_include_packages': zip_include_packages,
    }
}

setup(name='Trainig_Results',
      version='0.0.5',
      description='Save Results. Make map',
      executables=executables,
      options=options)
