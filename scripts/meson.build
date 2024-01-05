scripts = [
  ['telco', 'repl'],
  ['telco-apk', 'apk'],
  ['telco-compile', 'compiler'],
  ['telco-create', 'create'],
  ['telco-discover', 'discover'],
  ['telco-itrace', 'itracer'],
  ['telco-join', 'join'],
  ['telco-kill', 'kill'],
  ['telco-ls', 'ls'],
  ['telco-ls-devices', 'lsd'],
  ['telco-ps', 'ps'],
  ['telco-pull', 'pull'],
  ['telco-push', 'push'],
  ['telco-rm', 'rm'],
  ['telco-trace', 'tracer'],
]

common_cdata = configuration_data()
common_cdata.set('PYTHON', python)
common_cdata.set('pythondir', python_site_packages)

foreach s : scripts
  cdata = configuration_data()
  cdata.merge_from(common_cdata)
  cdata.set('module', s.get(1))

  generated_script = configure_file(
    input: 'script.in',
    output: s.get(0),
    configuration: cdata,
  )

  install_data(generated_script,
    install_dir: get_option('bindir'),
    install_mode: 'rwxr-xr-x',
  )
endforeach
