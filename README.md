# Helena assistent

**Resume**

    Create a complete assistant ecosystem capable of critically developing and managing task plans with calendars, lists, and the like; recording transcripts and allowing questions and interactions with the same resource requests for memory; searching for a topic in question via the web; entering values ​​into tables such as graph tables or training logs and subsequently measuring the requested cases; storing medical exams and health profiles, among others.

**MVP**
    Create a virtual assistent for tasks build and menager, with retroactive memory for resume of transcriptons every time that was solicted


## Make commands
```bash
make dev          # desenv with logs
make shell        # container access
make logs         # show logs
make down         # sotp containner
```


# Desenv Journal
#### 08/nov: 
**Setup**
Builded git. repository 
Writed  readme journal. 
Choused docker for versionament plataform. 
Writed initial requeriments.
Builde docker compose for future container menager
Writed .ignore
Created file .env withe supabase variables
Created make file with docker commands

**Base modules and first route**
create tables: 
- plans, columns: id, name, description, context, status, created_at, updated_at
- tasks, columns: id, plan_id, description, due_date, status, priority, created_at, updated_at
- memories, columns: id, title, content, summary, type, metadata, vector, created_at

Created folder app > models
Created file task_models.py (module using pydantic for plan and task models, with definition of obrigatory and optional fields)
Created file memory_models.py (module using pydantic for memories, with definition of obrigatory and optional fields)

Created folder app > core
Created file config.py (module for db config)
Created file database.py (module for connection and test of db)


Created folder app > routes
Created file assistant_routes.py (module for routes organization. Have only 2 routes and return a simple dict to test)

