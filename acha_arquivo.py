from pathlib import Path

entrada = "/home/anaciconelle/Desktop/DUDA"

panoramicas = []

for path in Path(entrada).rglob('pan'):
    panoramicas.append(str(path)[:-3])

laudos = []

for path in Path(entrada).rglob('laudo'):
    laudos.append(str(path)[:-5])

pacientes = list(set(laudos) & set(panoramicas))

print(pacientes)