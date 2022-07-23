{{- define "DB.CREDS" }}
env:
- name: DB_USER
  valueFrom:
    secretKeyRef:
      name: db-user-pass
      key: username
- name: DB_PASS
  valueFrom:
    secretKeyRef:
      name: db-user-pass
      key: password
{{- end }}