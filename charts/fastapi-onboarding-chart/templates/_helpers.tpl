{{/*
Expand the name of the chart.
*/}}
{{- define "fastapi-onboarding-chart.fullname" -}}
{{- .Release.Name }}-{{ .Values.nameOverride | default .Chart.Name }}
{{- end -}}
