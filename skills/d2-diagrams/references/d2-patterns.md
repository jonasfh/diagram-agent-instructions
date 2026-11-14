# D2 Patterns & Best Practices

## 1. Layered System Architecture Template (`--layout=elk`)

```d2
direction: right

classes: {
  layer: {
    style: {
      fill: "#f8fafc"
      stroke: "#cbd5e1"
      border-radius: 8
    }
  }
  service: {
    style: {
      fill: "#ffffff"
      stroke: "#3b82f6"
      border-radius: 6
    }
  }
  external: {
    style: {
      fill: "#fffbeb"
      stroke: "#d97706"
      stroke-dash: 4
      border-radius: 6
    }
  }
}

client: "Client" {
  class: layer
  browser: "Web Browser" {
    shape: person
  }
}

app: "Application Layer" {
  class: layer
  api: "REST / AJAX API" { class: service }
  svc: "Domain Service" { class: service }
  db: "Database" { shape: cylinder }
}

client.browser -> app.api: "HTTPS"
app.api -> app.svc: "Delegates"
app.svc -> app.db: "SQL"
```

## 2. Sequence / Integration Flow (`--layout=dagre`)

Use `shape: sequence_diagram` when chronological handshakes (checkout -> webhook -> callback) matter more than topology:

```d2
shape: sequence_diagram

user: "User" { shape: person }
app: "App"
ext: "External API"

user -> app: "1. Submit"
app -> ext: "2. Create session"
ext --> app: "3. Redirect URL"
ext -> app: "4. Async webhook"
```

## 3. Rules of Thumb

- Always declare `direction: right` or `direction: down`.
- Use `classes:` to avoid repeating `style:` blocks on every node.
- Use `shape: cylinder` for databases/caches and `shape: queue` for message queues.
- Keep labels concise (`2–4` words); put details in architectural docs, not inside boxes.
