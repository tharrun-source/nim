 Run Your FastAPI App:

You can run the app using Uvicorn:

bash

uvicorn main:app --reload

    main refers to the filename (main.py).
    app refers to the FastAPI instance in the file.
    --reload enables auto-reloading on code changes (useful during development).

By default, your app will run at http://127.0.0.1:8000.



 Activate the Virtual Environment:

    On macOS/Linux:

    bash

source myenv/bin/activate

On Windows:

bash

myenv\Scripts\activate
