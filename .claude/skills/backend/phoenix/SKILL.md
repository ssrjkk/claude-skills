---
name: phoenix
description: "Builds scalable web applications with Phoenix, Elixir, LiveView, and Ecto. Use for real-time, fault-tolerant apps."
category: backend
tags: [phoenix, elixir, liveview, ecto, realtime]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# Phoenix

> Elixir web framework with real-time capabilities and fault tolerance.

## Quick Start
```bash
mix phx.new my_app && cd my_app
mix ecto.create && mix phx.server
```

## Contexts
```elixir
defmodule MyApp.Accounts do
  alias MyApp.Accounts.User
  def list_users, do: Repo.all(User)
  def get_user!(id), do: Repo.get!(User, id)
  def create_user(attrs) do
    %User{} |> User.changeset(attrs) |> Repo.insert()
  end
end
```

## LiveView
```elixir
defmodule MyAppWeb.CounterLive do
  use MyAppWeb, :live_view
  def mount(_params, _session, socket) do
    {:ok, assign(socket, :count, 0)}
  end
  def handle_event("inc", _, socket) do
    {:noreply, update(socket, :count, &(&1 + 1))}
  end
end
```

## When to Use
- Real-time applications (chat, notifications)
- Fault-tolerant systems
- Concurrent web apps
- LiveView interactive UIs

## Validation
1. Server starts on port 4000
2. Ecto migrations run successfully
3. LiveView updates in real-time
