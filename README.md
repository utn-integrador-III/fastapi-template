# Install dependencies
``` 
    pip install fastapi uvicorn
``` 


# Run your FastAPI app
```
    uvicorn main:api --reload

    or

    uvicorn main:api --port <port number>
```

# A well-organized FastAPI project folder structure improves maintainability and scalability
```
fastapi_project/
│
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI app instance & entrypoint
│   ├── api/                 # Routers/endpoints
│   │   ├── __init__.py
│   │   ├── v1/
│   │   │   ├── __init__.py
│   │   │   └── endpoints.py
│   ├── core/                # Core settings, config, security
│   │   ├── __init__.py
│   │   └── config.py
│   ├── models/              # Pydantic and ORM models
│   │   ├── __init__.py
│   │   └── user.py
│   ├── schemas/             # Pydantic schemas
│   │   ├── __init__.py
│   │   └── user.py
│   ├── crud/                # CRUD operations
│   │   ├── __init__.py
│   │   └── user.py
│   ├── db/                  # Database connection/session
│   │   ├── __init__.py
│   │   └── session.py
│   ├── dependencies/        # Dependency functions
│   │   ├── __init__.py
│   │   └── auth.py
│   └── utils/               # Utility/helper functions
│       ├── __init__.py
│       └── helpers.py
│
├── tests/                   # Unit and integration tests
│   ├── __init__.py
│   └── test_main.py
│
├── requirements.txt
├── README.md
└── .env
```


GitHub Copilot
A well-organized FastAPI project folder structure improves maintainability and scalability. Here’s a recommended structure for medium to large projects:

Key Points:

# How to run the project locally
- main.py: App entrypoint.
- api/: Routers/endpoints, versioned if needed.
- models/ & schemas/: ORM and Pydantic models.
- crud/: CRUD logic, separate from endpoints.
- db/: Database session and connection logic.
- core/: App-wide config, security, etc.
- dependencies/: FastAPI dependency functions.
- utils/: Helper functions.
- tests/: All tests.

This structure is scalable and follows FastAPI best practices. For small projects, you can simplify it, but this layout is a solid foundation for growth.


1. create virtual env: `python3 -m venv venv`
2. create .env file
3. run: pip3 install -r requirements.txt
4. If you are using vs code, go to `run and debug` and create a launch.json file and add the following (for env file, copy your path and paste it): 
   { "version": "0.2.0",
        "configurations": [
            {
                "name": "Python: Current File",
                "type": "debugpy",
                "request": "launch",
                "program": "./app.py",
                "console": "integratedTerminal",
                "envFile": ".env"
            }
        ]
   }